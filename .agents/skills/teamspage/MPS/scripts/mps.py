from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import html
import json
import re
import uuid
from datetime import datetime, timedelta, timezone, tzinfo
from html.parser import HTMLParser
from pathlib import Path
from string import Template
from urllib.parse import quote

from embedded_manifest import build_embedded_payload, encode_embedded_payload, extract_embedded_payload
from np0_runtime import SnapshotBlocked, generate_observations, git, prepare, require, source_file


SCHEMA_VERSION = "1.0"
RENDERER_VERSION = "1.3.0"
CONTRACT_VERSION = "3.3.0"
AUTHORITY = "non-authority/no-writeback"
MP_ID_PATTERN = re.compile(r"\d{6}S[1-7]\d{3}")
MP_FILENAME_PATTERN = re.compile(r"MPS-(\d{6}S[1-7]\d{3})-([a-z0-9-]+)\.html")
INDEX_START = "<!-- teamspage-index:start -->"
INDEX_END = "<!-- teamspage-index:end -->"
TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "mps.html"


def canonical(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def timestamp(value: str) -> datetime:
    require(isinstance(value, str) and re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value
    ) is not None, "Expected RFC 3339 timestamp with offset")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise SnapshotBlocked("Invalid timestamp") from error


def slug(value: str) -> str:
    require(isinstance(value, str) and re.fullmatch(
        r"[A-Za-z0-9]+(?:[-.][A-Za-z0-9]+)*", value
    ) is not None, "Invalid filename key")
    result = value.lower().replace(".", "-")
    require(result not in {"con", "prn", "aux", "nul", *(
        f"{prefix}{number}" for prefix in ("com", "lpt") for number in range(1, 10)
    )}, "Reserved filename key")
    return result


def input_source(repo: Path, relative: str) -> Path:
    if isinstance(relative, str) and relative.endswith(".md"):
        return source_file(repo, relative)
    require(isinstance(relative, str) and "\\" not in relative, "Invalid source path")
    path = Path(relative)
    require(not path.is_absolute() and ".." not in path.parts and bool(path.parts), "Source path escapes repo")
    require(path.parts[0] in {"EGO", "Mission"} and path.suffix == ".json", "Unsupported structured source")
    target = (repo / path).resolve()
    require(target.is_relative_to(repo) and target.is_file(), f"Missing or escaped source: {relative}")
    return target


def capture_request(repo: Path, request: dict) -> dict:
    result = copy.deepcopy(request)
    snapshot = result["snapshot"]
    snapshot["source_commit"] = git(repo, "rev-parse", "HEAD")
    snapshot["observed_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    snapshot["source_sha256"] = {
        relative: digest(input_source(repo.resolve(), relative).read_bytes())
        for relative in snapshot["permission"]["allowed_sources"]
    }
    return result


def select_view(request: dict, selector: str) -> dict:
    views = request.get("views", [])
    require(isinstance(views, list), "Invalid view list")
    selected = [view for view in views if view.get("target", {}).get("target_ref") == selector]
    require(len(selected) == 1, "View selector is missing or ambiguous")
    require(set(selected[0]) == {"target", "narrative", "viewpoint"}, "View cannot override binding or permission")
    result = copy.deepcopy(request)
    result.pop("views")
    result.update(copy.deepcopy(selected[0]))
    return result


def target_key(target: dict) -> str:
    require(isinstance(target, dict), "Missing typed target")
    require(set(target) == {"namespace", "target_kind", "target_ref", "scope"}, "Invalid target fields")
    namespace = slug(target["namespace"])
    kind = target["target_kind"]
    require(kind in {"system", "method", "area", "name", "instance"}, "Unknown target kind")
    selector = slug(target["target_ref"])
    require(isinstance(target["scope"], str) and bool(target["scope"].strip()), "Missing target scope")
    suffix = "" if kind in {"system", "method"} and selector == namespace else f"-{selector}"
    return f"{namespace}-{kind}{suffix}"


def _narrative_text_slots(narrative: dict) -> dict[str, str]:
    slots = {}

    def collect(value: object, prefix: str) -> None:
        if isinstance(value, str):
            slots[prefix] = value
        elif isinstance(value, list):
            for index, item in enumerate(value):
                collect(item, f"{prefix}.{index}")
        elif isinstance(value, dict):
            for key, item in sorted(value.items()):
                collect(item, f"{prefix}.{key}")
        else:
            raise SnapshotBlocked(f"Unsupported narrative value at {prefix}")

    for field, value in sorted(narrative.items()):
        if field != "title":
            collect(value, field)
    return slots


def _validate_voice_sources(narrative: dict, voice_sources: dict, sources: dict,
                            allowed_sources: list[str]) -> None:
    slots = _narrative_text_slots(narrative)
    require(isinstance(voice_sources, dict) and set(voice_sources) == set(slots),
            "G-Voice requires provenance for every narrative sentence")
    for slot, text in slots.items():
        record = voice_sources[slot]
        require(isinstance(record, dict), f"Invalid G-Voice record: {slot}")
        kind = record.get("kind")
        if kind in {"source_claim", "signed_quote"}:
            expected_fields = {"kind", "source", "signer"} if kind == "signed_quote" else {"kind", "source"}
            require(set(record) == expected_fields, f"Invalid G-Voice source record: {slot}")
            relative = record.get("source")
            require(relative in allowed_sources and relative in sources, f"G-Voice source is not authorized: {slot}")
            source_text = base64.b64decode(sources[relative]["bytes_base64"], validate=True).decode("utf-8-sig")
            require(text in source_text, f"G-Voice text is not present in its source: {slot}")
            if kind == "signed_quote":
                require(isinstance(record["signer"], str) and bool(record["signer"].strip()),
                        f"G-Voice signed quote has no signer: {slot}")
        elif kind == "rule_marker":
            require(set(record) == {"kind", "rule_id", "sources"}, f"Invalid G-Voice rule record: {slot}")
            require(isinstance(record["rule_id"], str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", record["rule_id"]),
                    f"Invalid G-Voice rule ID: {slot}")
            evidence = record["sources"]
            require(isinstance(evidence, list) and bool(evidence)
                    and all(path in allowed_sources and path in sources for path in evidence),
                    f"G-Voice rule has no authorized evidence: {slot}")
        else:
            raise SnapshotBlocked(f"Unknown G-Voice record kind: {slot}")


def _validate_distortion_declarations(declarations: object) -> list[dict]:
    require(isinstance(declarations, list), "G-Distort requires an explicit declaration list")
    normalized = []
    for item in declarations:
        require(isinstance(item, dict) and set(item) == {"surface", "omitted_count", "reason"},
                "Invalid G-Distort declaration")
        require(isinstance(item["surface"], str) and bool(item["surface"].strip()),
                "G-Distort surface is required")
        require(isinstance(item["omitted_count"], int) and not isinstance(item["omitted_count"], bool)
                and item["omitted_count"] > 0, "G-Distort omitted_count must be a positive integer")
        require(isinstance(item["reason"], str) and bool(item["reason"].strip()),
                "G-Distort reason is required")
        normalized.append(copy.deepcopy(item))
    return normalized


def _gate_statuses(gate_evidence: object, source_revision: str) -> dict[str, str]:
    require(isinstance(gate_evidence, dict), "Invalid external MPS gate evidence")
    require(set(gate_evidence).issubset({"g_tier", "g_orphan"}), "Unknown external MPS gate")
    statuses = {}
    tier = gate_evidence.get("g_tier")
    if tier is None:
        statuses["g_tier"] = "not_run"
    elif tier.get("status") in {"not_run", "not_applicable"}:
        require(isinstance(tier.get("reason"), str) and bool(tier["reason"].strip()),
                "G-Tier non-run state requires a reason")
        statuses["g_tier"] = tier["status"]
    else:
        require(set(tier) == {"command", "exit_code", "evidence"}, "Invalid G-Tier execution record")
        require(isinstance(tier["command"], str) and bool(tier["command"].strip()), "G-Tier command is required")
        require(isinstance(tier["exit_code"], int) and not isinstance(tier["exit_code"], bool),
                "G-Tier exit_code must be an integer")
        require(isinstance(tier["evidence"], str) and bool(tier["evidence"].strip()), "G-Tier evidence is required")
        statuses["g_tier"] = "pass" if tier["exit_code"] == 0 else "fail"

    orphan = gate_evidence.get("g_orphan")
    if orphan is None:
        statuses["g_orphan"] = "not_run"
    elif orphan.get("status") == "not_applicable":
        require(isinstance(orphan.get("reason"), str) and bool(orphan["reason"].strip()),
                "G-Orphan not_applicable state requires a reason")
        statuses["g_orphan"] = "not_applicable"
    else:
        required = {"target", "source_revision", "orphans", "dangling_edges", "cycles", "evidence"}
        require(set(orphan) == required, "Invalid G-Orphan extraction record")
        require(orphan["source_revision"] == source_revision, "G-Orphan report source revision mismatch")
        require(isinstance(orphan["target"], str) and bool(orphan["target"].strip()), "G-Orphan target is required")
        for field in ("orphans", "dangling_edges", "cycles"):
            require(isinstance(orphan[field], int) and not isinstance(orphan[field], bool) and orphan[field] >= 0,
                    f"Invalid G-Orphan count: {field}")
        require(isinstance(orphan["evidence"], str) and bool(orphan["evidence"].strip()), "G-Orphan evidence is required")
        statuses["g_orphan"] = "pass" if all(orphan[field] == 0 for field in ("orphans", "dangling_edges", "cycles")) else "fail"
    return statuses


def _build_failure_records(semantic: dict, checks: dict) -> list[dict]:
    failures = []
    for index, finding in enumerate(semantic["findings"], 1):
        failures.append({
            "id": f"SRC-{index:02d}",
            "severity": "HIGH",
            "assertion": f"{finding['target']} {finding['field']}: {finding['expected']} != {finding['actual']}",
            "evidence": f"{finding['expected_source']} <> {finding['actual_source']}",
            "next": "改登记: 由 owning source authority 核查冲突后修订。",
        })
    evidence = semantic["gate_evidence"]
    if checks["g_tier"] == "fail":
        failures.append({
            "id": "G-TIER",
            "severity": "HIGH",
            "assertion": "Tier A structure check returned a non-zero exit code.",
            "evidence": evidence["g_tier"]["evidence"],
            "next": "改登记: 依据 gate output 由 owning Repo workflow 处理。",
        })
    if checks["g_orphan"] == "fail":
        report = evidence["g_orphan"]
        failures.append({
            "id": "G-ORPHAN",
            "severity": "HIGH",
            "assertion": (f"{report['target']} contains {report['orphans']} orphan(s), "
                          f"{report['dangling_edges']} dangling edge(s), {report['cycles']} cycle(s)."),
            "evidence": report["evidence"],
            "next": "改登记: 先核对 source graph，再由 owning authority 修正关系。",
        })
    return failures


def _historical_mps_page_ids(repo: Path) -> list[tuple[str, str]]:
    history = []
    for custody_path in ("Repo/shape/TeamsPage", "Repo/shape/teamspage"):
        output = git(repo, "log", "--all", "--diff-filter=A", "--format=", "--name-only",
                     "--", custody_path)
        history.extend(line.strip() for line in output.splitlines() if line.strip())
    historical = []
    for relative in dict.fromkeys(history):
        match = MP_FILENAME_PATTERN.fullmatch(Path(relative).name)
        if match:
            historical.append((match.group(1), relative))
    return historical


def _allocate_mp_id(repo: Path, generated_at: str) -> str:
    generated = timestamp(generated_at).astimezone(timezone.utc)
    date_key = generated.strftime("%y%m%d")
    weekday = generated.isoweekday()
    historical = _historical_mps_page_ids(repo)
    historical_counts = {}
    used_ids = set()
    for mp_id, _relative in historical:
        page_date = datetime.strptime(f"20{mp_id[:6]}", "%Y%m%d").replace(tzinfo=timezone.utc)
        require(int(mp_id[7]) == page_date.isoweekday(), f"G-ID weekday/date mismatch in Git history: {mp_id}")
        historical_counts[mp_id] = historical_counts.get(mp_id, 0) + 1
        used_ids.add(mp_id)
    duplicates = [mp_id for mp_id, count in historical_counts.items() if count > 1]
    require(not duplicates, f"G-ID historical reuse detected: {', '.join(sorted(duplicates))}")

    custody = repo / "Repo" / "shape" / "TeamsPage"
    local_ids = {}
    if custody.is_dir():
        for path in custody.glob("MPS-*.html"):
            match = MP_FILENAME_PATTERN.fullmatch(path.name)
            if not match:
                continue
            mp_id = match.group(1)
            page_date = datetime.strptime(f"20{mp_id[:6]}", "%Y%m%d").replace(tzinfo=timezone.utc)
            require(int(mp_id[7]) == page_date.isoweekday(), f"G-ID weekday/date mismatch in live custody: {mp_id}")
            local_ids.setdefault(mp_id, set()).add(path.name)
            used_ids.add(mp_id)
    collisions = [mp_id for mp_id, names in local_ids.items() if len(names) > 1]
    require(not collisions, f"G-ID duplicate live MPS page ID: {', '.join(sorted(collisions))}")

    used_today = {int(mp_id[8:]) for mp_id in used_ids
                  if mp_id[:6] == date_key and int(mp_id[7]) == weekday}
    next_sequence = max(used_today, default=0) + 1
    require(next_sequence <= 999, "G-ID exhausted the daily MPS sequence")
    return f"{date_key}S{weekday}{next_sequence:03d}"


def _validate_mp_id_date(mp_id: str, generated_at: str) -> None:
    require(MP_ID_PATTERN.fullmatch(mp_id) is not None, "Invalid MPS page ID")
    generated = timestamp(generated_at).astimezone(timezone.utc)
    require(mp_id[:6] == generated.strftime("%y%m%d"), "MPS page ID date differs from generated_at")
    require(int(mp_id[7]) == generated.isoweekday(), "MPS page ID weekday differs from UTC date")
    require(1 <= int(mp_id[8:]) <= 999, "MPS page ID sequence is outside 001-999")


def _validate_mp_id_history(repo: Path, mp_id: str, artifact: Path) -> None:
    historical_ids = [existing_id for existing_id, _relative in _historical_mps_page_ids(repo)]
    require(historical_ids.count(mp_id) <= 1, "G-ID identifier was reused in Git history")
    custody = repo / "Repo" / "shape" / "TeamsPage"
    if custody.is_dir():
        matches = [path.resolve() for path in custody.glob("MPS-*.html")
                   if (match := MP_FILENAME_PATTERN.fullmatch(path.name)) and match.group(1) == mp_id]
        require(len(matches) == 1 and matches[0] == artifact.resolve(),
                "G-ID identifier is missing or duplicated in live custody")


def build_model(repo: Path, request: dict, *, generated_at: str | None = None,
                snapshot_id: str | None = None, previous: dict | None = None,
                sample: bool | None = None, as_of: str | None = None) -> dict:
    repo = repo.resolve()
    require(isinstance(request, dict), "Expected TeamPage MPS input object")
    sample = request.get("mp:sample", False) if sample is None else sample
    require(isinstance(sample, bool), "mp:sample must be boolean")
    binding = request.get("snapshot", {})
    run_id, documents = prepare(repo, binding)
    require(binding["permission"].get("teamspage_write") is True, "TeamPage MPS write not authorized")
    target = request.get("target", {})
    key = target_key(target)
    method = binding["selected_method"]
    if target["namespace"] not in {"REM", "NP0"}:
        require(method is not None and method["name"] == target["namespace"], "Target requires its selected-method source")
    rem_id = request.get("rem_id", "")
    rem_key = slug(rem_id)
    locator = request.get("repo_locator", "")
    require(isinstance(locator, str) and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", locator) is not None, "Expected credential-free owner/repo locator")
    narrative = request.get("narrative", {})
    require(isinstance(narrative, dict), "Missing narrative")
    for field in ("title", "summary", "decision_rights", "next_action", "verification_route"):
        require(isinstance(narrative.get(field), str) and bool(narrative[field].strip()), f"Missing narrative {field}")
    for field in ("claims", "unknowns"):
        require(isinstance(narrative.get(field), list) and all(isinstance(item, str) for item in narrative[field]), f"Invalid {field}")
    distortion_declarations = _validate_distortion_declarations(request.get("distortion_declarations"))
    viewpoint = request.get("viewpoint", "")
    require(isinstance(viewpoint, str) and bool(viewpoint.strip()), "Missing viewpoint")
    source_link_policy = request.get("source_link_policy", "local")
    require(source_link_policy == "local", "New MPS artifacts use local source links; sidecar links are retired")
    generated_at = generated_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    require(timestamp(generated_at) >= timestamp(binding["observed_at"]), "Generation precedes observation")
    as_of = as_of or request.get("as_of", binding["baseline_date"])
    require(isinstance(as_of, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", as_of) is not None,
            "Expected as_of as an ISO date")
    try:
        datetime.strptime(as_of, "%Y-%m-%d")
    except ValueError as error:
        raise SnapshotBlocked("Invalid as_of date") from error
    snapshot_id = snapshot_id or uuid.uuid4().hex
    require(re.fullmatch(r"[a-f0-9]{32}", snapshot_id) is not None, "Expected full snapshot UUID hex")
    envelopes = {
        name: json.loads(document.partition("```json\n")[2].rpartition("\n```")[0])
        for name, document in documents.items()
    }
    revisions = next(iter(envelopes.values()))["binding_revisions"]
    projection_sources = request.get("projection_sources", {})
    require(isinstance(projection_sources, dict), "Invalid projection sources")
    reference_sources = request.get("reference_sources", {})
    require(isinstance(reference_sources, dict), "Invalid reference sources")
    require(all(isinstance(label, str) and bool(label.strip()) and isinstance(relative, str)
                and relative.endswith(".md") for label, relative in reference_sources.items()),
            "Reference sources must map labels to Markdown paths")
    for relative in projection_sources.values():
        require(relative in binding["permission"]["allowed_sources"], "Projection source not authorized")
        content = input_source(repo, relative).read_bytes()
        checksum = digest(content)
        require(binding["source_sha256"].get(relative, "").lower() == checksum, f"Projection source hash changed: {relative}")
        revisions[relative] = {"commit": binding["source_commit"], "sha256": checksum,
                               "dirty": bool(git(repo, "status", "--porcelain", "--", relative))}
    require(len(set(reference_sources.values())) == len(reference_sources), "Duplicate reference source")
    for relative in reference_sources.values():
        require(relative in binding["permission"]["allowed_sources"], "Reference source not authorized")
        content = input_source(repo, relative).read_bytes()
        checksum = digest(content)
        require(binding["source_sha256"].get(relative, "").lower() == checksum,
                f"Reference source hash changed: {relative}")
        revisions[relative] = {"commit": binding["source_commit"], "sha256": checksum,
                               "dirty": bool(git(repo, "status", "--porcelain", "--", relative))}
    sources = {}
    for relative, revision in revisions.items():
        content = input_source(repo, relative).read_bytes()
        require(digest(content) == revision["sha256"], "Source changed while freezing input")
        sources[relative] = {**revision, "bytes_base64": base64.b64encode(content).decode("ascii")}
    voice_sources = request.get("voice_sources")
    _validate_voice_sources(narrative, voice_sources, sources, binding["permission"]["allowed_sources"])
    gate_evidence = copy.deepcopy(request.get("gate_evidence", {}))
    gate_status = _gate_statuses(gate_evidence, binding["source_commit"])
    entries, findings = project_entries(target, sources, projection_sources)
    semantic = {
        "rem_id": rem_id, "repo_locator": locator, "target": copy.deepcopy(target),
        "viewpoint": viewpoint, "narrative": copy.deepcopy(narrative),
        "observations": copy.deepcopy(binding["observations"]),
        "selected_method": copy.deepcopy(method), "entries": entries, "findings": findings,
        "reference_sources": copy.deepcopy(reference_sources),
        "voice_sources": copy.deepcopy(voice_sources),
        "distortion_declarations": distortion_declarations,
        "gate_evidence": gate_evidence,
        "mission_context": request.get("mission_context", binding["binding"]["mission"]),
        "source_link_policy": source_link_policy,
    }
    mp_id = None if sample else _allocate_mp_id(repo, generated_at)
    model = {
        "schema_version": SCHEMA_VERSION, "renderer_version": RENDERER_VERSION,
        "projection_contract_version": CONTRACT_VERSION,
        "template_sha256": digest(TEMPLATE.read_bytes()),
        "authority": AUTHORITY, "snapshot_id": snapshot_id, "run_id": run_id,
        "mp:sample": sample, "as_of": as_of,
        "stem": f"sample-{key}" if sample else f"MPS-{mp_id}-{key}",
        "observed_at": binding["observed_at"], "generated_at": generated_at,
        "source_revision": binding["source_commit"], "binding_revisions": revisions,
        "sources": sources, "projection_sources": copy.deepcopy(projection_sources), "semantic": semantic,
        "binding_observations": envelopes, "permission_declaration": copy.deepcopy(binding["permission"]),
        "semantic_sha256": digest(canonical(semantic).encode("utf-8")),
        "previous_snapshot_id": None,
        "checks": {"projection": "not_run", "source_consistency": "not_run",
                   "human_review": "not_run", "runtime": "not_run", "freshness": "unknown",
                   "g_id": "not_applicable" if sample else "pass", "g_distort": "pass", "g_voice": "pass",
                   **gate_status},
    }
    if mp_id is not None:
        model["mp:id"] = mp_id
    if projection_sources:
        model["checks"]["source_consistency"] = "issues_found" if findings else "no_differences_in_checked_fields"
    model["failures"] = _build_failure_records(semantic, model["checks"])
    model["delta"] = compare(previous, model) if previous else None
    if previous:
        model["previous_snapshot_id"] = previous["snapshot_id"]
        model["previous_stem"] = previous["stem"]
    return model


def project_np0(target: dict, sources: dict, projection_sources: dict) -> tuple[list, list]:
    registry_path = projection_sources.get("registry", "EGO/TeamSkill/np0/references/name-registry.md")
    entries = []
    findings = []
    chinese_map = {
        "NP0": "零阶叙事",
        "Universe Firstness": "宇宙第一性",
        "Domain Firstness": "领域第一性",
        "Four-Order Narrative Contract": "四阶叙事契约",
        "Ontology-Driven Narrative": "本体驱动叙事",
        "NP0-U0": "最小叙事宇宙",
        "Frontier-Capability Gate": "前沿模型门禁",
        "Narrative": "零阶行动叙事",
        "RIG": "RAM 信息图 (已退役)",
        "Actionable Reality": "行动现实三元公式",
        "Tri-Distinction Rule": "三维区分律",
        "Decision Rights Envelope": "决策权包络律",
        "Ontology Addressability": "本体可寻址律",
        "Belief Revision Invariant": "闭环可修正律",
        "Non-Authority Projection": "非权威投影律",
    }
    domain_map = {
        "teamskill/np0": "Core (公理核心)",
        "teamskill/np0/axiom": "Axiom (公理体系)",
        "teamskill/np0/layer": "Layer (四阶契约)",
        "teamskill/np0/method": "Method (工作模式)",
        "teamskill/np0/eval": "Eval (评测夹具)",
        "teamskill/np0/runtime": "Runtime (运行门禁)",
        "teamskill/np0/narrative": "Narrative (零阶叙事)",
        "teamskill/np0/infographic": "Infographic (信息图)",
        "teamskill/np0/infographic/legacy": "Legacy (历史代号)",
        "teamskill/np0/rule": "Rule (五大元规则)",
        "teamskill/np0/legacy": "Legacy (历史前身)",
    }
    if registry_path in sources:
        text = base64.b64decode(sources[registry_path]["bytes_base64"], validate=True).decode("utf-8-sig")
        lines = [line.strip() for line in text.splitlines()]
        data_rows = []
        for line_number, line in enumerate(lines, 1):
            if line.startswith("|") and not line.startswith("|---") and not line.startswith("| Name"):
                cols = [col.strip().strip("`") for col in line.split("|")[1:-1]]
                if len(cols) >= 9:
                    data_rows.append((line_number, cols))
        for index, (line_number, cols) in enumerate(data_rows):
            name, name_key, namespace, lifecycle, authority_route, projection, update_cadence, evidence, no_confusion = cols[:9]
            chinese_name = chinese_map.get(name, name)
            domain = domain_map.get(namespace, "General")
            allocation = "assigned" if lifecycle == "active" else "retired"
            entry = {
                "naming_id": f"NP0.{index+1:02d}",
                "token": name,
                "chinese_name": chinese_name,
                "distinction": projection or evidence or "L0 zero-order governed name.",
                "name_key": name_key,
                "labels": f"Namespace: {namespace} | Cadence: {update_cadence}",
                "domain": domain,
                "authority_route": authority_route,
                "boundary": no_confusion,
                "source": f"{registry_path}#L{line_number}",
                "allocation": allocation,
                "lifecycle": lifecycle,
                "entity_lifecycle": "not_applicable (L0 axiom)",
                "ontology_disposition": "axiom_foundation" if lifecycle == "active" else "retired",
                "oid": "none",
            }
            entries.append(entry)
    else:
        entries.extend([
            {
                "naming_id": "NP0.01",
                "token": "NP0",
                "chinese_name": "零阶叙事",
                "distinction": "Narrative is Principle Zero (Synthetic fixture).",
                "name_key": "np0",
                "labels": "Namespace: teamskill/np0 | Cadence: Audit + eval + consumer review",
                "domain": "Core (公理核心)",
                "authority_route": "EGO/TeamSkill/np0/SKILL.md",
                "boundary": "NP0 = Narrative is Principle Zero; P0 is not a fifth layer",
                "source": "EGO/Naming.md#L1",
                "allocation": "assigned",
                "lifecycle": "active",
                "entity_lifecycle": "not_applicable (L0 axiom)",
                "ontology_disposition": "axiom_foundation",
                "oid": "none",
            },
            {
                "naming_id": "NP0.02",
                "token": "Narrative",
                "chinese_name": "零阶行动叙事",
                "distinction": "显影差异与赋能行动 (Synthetic fixture).",
                "name_key": "narrative",
                "labels": "Namespace: teamskill/np0/narrative | Cadence: Audit",
                "domain": "Narrative (零阶叙事)",
                "authority_route": "EGO/TeamSkill/np0/Narrative.md",
                "boundary": "L0 executable context; distinct from CRAFTS S-domain Story",
                "source": "EGO/Naming.md#L1",
                "allocation": "assigned",
                "lifecycle": "active",
                "entity_lifecycle": "not_applicable (L0 axiom)",
                "ontology_disposition": "axiom_foundation",
                "oid": "none",
            },
            {
                "naming_id": "NP0.03",
                "token": "Naming",
                "chinese_name": "离散固态记忆",
                "distinction": "不可变数学寻址 (Synthetic fixture).",
                "name_key": "naming",
                "labels": "Namespace: teamskill/np0/naming | Cadence: Audit",
                "domain": "Naming (离散固态记忆)",
                "authority_route": "EGO/TeamSkill/np0/Naming.md",
                "boundary": "Master Naming Registry SSOT",
                "source": "EGO/Naming.md#L1",
                "allocation": "assigned",
                "lifecycle": "active",
                "entity_lifecycle": "not_applicable (L0 axiom)",
                "ontology_disposition": "axiom_foundation",
                "oid": "none",
            },
            {
                "naming_id": "NP0.04",
                "token": "Ontology",
                "chinese_name": "语义强约束",
                "distinction": "防止散文腐败 (Synthetic fixture).",
                "name_key": "ontology",
                "labels": "Namespace: teamskill/np0/ontology | Cadence: Audit",
                "domain": "Ontology (语义强约束)",
                "authority_route": "EGO/TeamSkill/np0/Narrative.md",
                "boundary": "Bounded semantics",
                "source": "EGO/Naming.md#L1",
                "allocation": "assigned",
                "lifecycle": "active",
                "entity_lifecycle": "not_applicable (L0 axiom)",
                "ontology_disposition": "axiom_foundation",
                "oid": "none",
            },
        ])
    return entries, findings


def project_entries(target: dict, sources: dict, projection_sources: dict) -> tuple[list, list]:
    if target["namespace"] == "REM":
        require(not projection_sources, "REM core must not require domain projection sources")
        return [], []
    if target["namespace"] == "NP0":
        return project_np0(target, sources, projection_sources)
    require(target["namespace"] == "CRAFTS", "No adapter for this namespace")
    from mps_crafts import project
    return project(target, sources, projection_sources)


def compare(previous: dict, current: dict) -> dict:
    for field in ("rem_id", "repo_locator", "target", "viewpoint"):
        require(previous["semantic"][field] == current["semantic"][field], f"Incomparable {field}")
    before = previous["sources"]
    after = current["sources"]
    changed = sorted(relative for relative in set(before) | set(after)
                     if before.get(relative, {}).get("sha256") != after.get(relative, {}).get("sha256"))
    return {"source_paths": changed, "semantic_changed": previous["semantic_sha256"] != current["semantic_sha256"],
            "presentation_changed": previous.get("template_sha256") != current.get("template_sha256")
            or previous["renderer_version"] != current["renderer_version"],
            "review_delta": "review_events_are_separate"}


def view_bindings(model: dict) -> dict[str, str]:
    semantic = model["semantic"]
    values = {field: str(model[field]) for field in ("snapshot_id", "generated_at", "observed_at", "as_of", "source_revision")}
    for field in ("rem_id", "repo_locator", "viewpoint", "mission_context"):
        values[field] = str(semantic[field])
    for field, value in sorted(semantic["target"].items()):
        values[f"target.{field}"] = value
    for field, value in semantic["narrative"].items():
        if isinstance(value, list):
            for index, item in enumerate(value):
                values[f"narrative.{field}.{index}"] = item
        else:
            values[f"narrative.{field}"] = str(value)
    for index, entry in enumerate(semantic["entries"]):
        for field, value in entry.items():
            values[f"entry.{index}.{field}"] = str(value)
    for index, finding in enumerate(semantic["findings"]):
        for field, value in finding.items():
            values[f"finding.{index}.{field}"] = str(value)
    for name, observation in semantic["observations"].items():
        values[f"observation.{name}.Credence"] = observation["Credence"] or "unknown"
        for field in ("source_claims", "Claim", "unknowns", "delta"):
            for index, value in enumerate(observation[field]):
                values[f"observation.{name}.{field}.{index}"] = value
        for index, fact in enumerate(observation["Fact"]):
            for field, value in fact.items():
                values[f"observation.{name}.Fact.{index}.{field}"] = value
    for label, relative in semantic.get("reference_sources", {}).items():
        values[f"reference_source.{label}"] = f"{label}: {relative}"
    for slot, record in semantic["voice_sources"].items():
        if record["kind"] in {"source_claim", "signed_quote"}:
            detail = record["source"]
            if record["kind"] == "signed_quote":
                detail += f" · signer: {record['signer']}"
        else:
            detail = f"rule: {record['rule_id']} · evidence: {', '.join(record['sources'])}"
        values[f"voice_source.{slot}"] = detail
    for index, declaration in enumerate(semantic["distortion_declarations"]):
        for field in ("surface", "omitted_count", "reason"):
            values[f"distortion.{index}.{field}"] = str(declaration[field])
    for index, failure in enumerate(model["failures"]):
        for field in ("id", "severity", "assertion", "evidence", "next"):
            values[f"failure.{index}.{field}"] = failure[field]
    for field, value in model["checks"].items():
        values[f"check.{field}"] = value
    values["authority"] = AUTHORITY
    return values


class MpsDocument(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.bindings = {}
        self.active = None
        self.text = []
        self.external_resources = []
        self.script_types = []
        self.mp_data_count = 0
        self.mp_data_active = False
        self.mp_data = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        key = attributes.get("data-mp-key")
        if key:
            require(key not in self.bindings and self.active is None, "Duplicate or nested semantic binding")
            self.active = key
            self.text = []
        if tag in {"script", "link", "img", "iframe", "audio", "video", "source"}:
            if attributes.get("src") or attributes.get("href"):
                self.external_resources.append(attributes)
        if tag == "script":
            self.script_types.append(attributes.get("type", ""))
            if attributes.get("id") == "mp-data":
                self.mp_data_count += 1
                self.mp_data_active = True

    def handle_data(self, data):
        if self.mp_data_active:
            self.mp_data.append(data)
        elif self.active:
            self.text.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.mp_data_active:
            self.mp_data_active = False
        if self.active:
            self.bindings[self.active] = "".join(self.text)
            self.active = None


def validate_html(model: dict, document: str) -> None:
    parsed = MpsDocument()
    parsed.feed(document)
    require(parsed.bindings == view_bindings(model), "Visible DOM / semantic payload mismatch")
    require(not parsed.mp_data_active, "Unclosed #mp-data envelope")
    require(parsed.mp_data_count == 1, "Expected exactly one #mp-data envelope")
    require(extract_embedded_payload(document) == build_embedded_payload(model),
            "Embedded manifest / semantic model mismatch")
    require(not parsed.external_resources, "External rendering dependency")
    require(all(kind == "application/json" for kind in parsed.script_types), "Unexpected executable script")
    require("@import" not in document and "url(" not in document, "External CSS resource")


def read_artifact_model(artifact: Path) -> dict:
    require(artifact.suffix == ".html", "Expected a TeamPage HTML artifact")
    return extract_embedded_payload(artifact.read_text(encoding="utf-8"))


def validate_artifact(artifact: Path, repo: Path | None = None) -> dict:
    require(artifact.suffix == ".html", "Expected a TeamPage MPS HTML artifact")
    content = artifact.read_bytes()
    try:
        model = extract_embedded_payload(content.decode("utf-8"))
    except ValueError as error:
        raise SnapshotBlocked(str(error)) from error
    return _validate_embedded_artifact(model, artifact, content, repo)


def _validate_embedded_artifact(model: dict, artifact: Path, content: bytes,
                                repo: Path | None = None) -> dict:
    required = {"artifact_type", "schema_version", "renderer_version", "projection_contract_version",
                "authority", "snapshot_id", "stem", "observed_at", "generated_at", "as_of", "source_revision",
                "mp:sample", "semantic", "sources", "projection_sources", "permission_declaration",
                "semantic_sha256", "checks", "failures"}
    require(required.issubset(model), "Incomplete embedded MPS envelope")
    require(model["artifact_type"] == "mirror-page", "Unknown embedded TeamPage artifact type")
    require(model["schema_version"] == SCHEMA_VERSION and model["authority"] == AUTHORITY,
            "MPS schema or authority mismatch")
    target_slug = target_key(model["semantic"]["target"])
    require(isinstance(model["mp:sample"], bool), "Invalid MPS sample marker")
    if model["mp:sample"]:
        require("mp:id" not in model, "MPS golden samples must not allocate mp:id")
        require(model["stem"] == f"sample-{target_slug}" and artifact.name == "expected.html",
                "Invalid MPS golden sample identity")
        require({"MPS", "evals", "baseline"}.issubset(set(artifact.parts))
            and artifact.parent.name.startswith("golden_"),
            "MPS samples are only valid under MPS/evals/baseline/golden_*")
        require(model["checks"].get("g_id") == "not_applicable", "MPS golden sample must not claim G-ID pass")
    else:
        require(re.fullmatch(r"MPS-\d{6}S[1-7]\d{3}-[a-z0-9-]+", model["stem"]) is not None,
                "Unsafe artifact stem")
        require(artifact.name == model["stem"] + ".html", "Artifact filename / identity mismatch")
        _validate_mp_id_date(model["mp:id"], model["generated_at"])
        expected_stem = f"MPS-{model['mp:id']}-{target_slug}"
        require(model["stem"] == expected_stem, "Filename / identity mismatch")
        require(model["checks"].get("g_id") == "pass", "MPS runtime artifact must pass G-ID allocation")
    try:
        datetime.strptime(model["as_of"], "%Y-%m-%d")
    except (TypeError, ValueError) as error:
        raise SnapshotBlocked("Invalid embedded as_of date") from error
    require(timestamp(model["generated_at"]) >= timestamp(model["observed_at"]),
            "Generation precedes observation")
    for relative, source in model["sources"].items():
        frozen = base64.b64decode(source["bytes_base64"], validate=True)
        require(digest(frozen) == source["sha256"], f"Frozen source corrupt: {relative}")
    semantic = model["semantic"]
    _validate_distortion_declarations(semantic.get("distortion_declarations"))
    permission = model["permission_declaration"]
    require(isinstance(permission, dict) and isinstance(permission.get("allowed_sources"), list),
            "Missing frozen permission source allowlist")
    _validate_voice_sources(semantic["narrative"], semantic.get("voice_sources"), model["sources"],
                            permission["allowed_sources"])
    external_gates = _gate_statuses(semantic.get("gate_evidence", {}), model["source_revision"])
    require(model["checks"].get("g_id") == ("not_applicable" if model["mp:sample"] else "pass"),
            "G-ID allocation evidence is missing or invalid")
    require(model["checks"].get("g_distort") == "pass", "G-Distort declaration check mismatch")
    require(model["checks"].get("g_voice") == "pass", "G-Voice provenance check mismatch")
    for gate_name, status in external_gates.items():
        require(model["checks"].get(gate_name) == status, f"{gate_name} evidence / check state mismatch")
    require(model["failures"] == _build_failure_records(semantic, model["checks"]),
            "Failure records do not match source and gate evidence")
    reference_sources = semantic.get("reference_sources", {})
    require(isinstance(reference_sources, dict), "Invalid frozen reference source map")
    require(all(isinstance(label, str) and isinstance(relative, str) and relative in model["sources"]
                for label, relative in reference_sources.items()),
            "Reference source missing frozen bytes")
    entries, findings = project_entries(semantic["target"], model["sources"], model["projection_sources"])
    require(semantic["entries"] == entries and semantic["findings"] == findings,
            "Frozen source / projected rows mismatch")
    require(digest(canonical(semantic).encode("utf-8")) == model["semantic_sha256"],
            "Semantic hash mismatch")
    document = content.decode("utf-8")
    validate_html(model, document)
    require(render_html(model).encode("utf-8") == content, "Deterministic MPS rerender mismatch")
    result = {"projection": "pass", "source_consistency": model["checks"]["source_consistency"],
              "human_review": "not_run", "runtime": "not_run", "freshness": "unknown",
              "artifact_sha256": digest(content)}
    for gate_name in ("g_id", "g_distort", "g_voice", "g_tier", "g_orphan"):
        result[gate_name] = model["checks"][gate_name]
    if repo is not None and not model["mp:sample"]:
        _validate_mp_id_history(repo.resolve(), model["mp:id"], artifact)
        result["g_id"] = "pass"
        changed = [relative for relative, source in model["sources"].items()
                   if digest(input_source(repo.resolve(), relative).read_bytes()) != source["sha256"]]
        result["freshness"] = "stale" if changed else "matches_observed_files"
        result["freshness_checked_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        result["changed_sources"] = changed
    return result


def render_html(model: dict) -> str:
    semantic = model["semantic"]
    narrative = semantic["narrative"]
    values = view_bindings(model)
    used = set()

    def bound(key, tag="span", css=""):
        require(key not in used, f"Repeated render binding: {key}")
        used.add(key)
        class_attr = f' class="{css}"' if css else ""
        return f'<{tag}{class_attr} data-mp-key="{html.escape(key)}">{html.escape(values[key])}</{tag}>'

    def link(relative, label=None):
        address = "../../../" + quote(relative, safe="/#")
        return f'<a class="source-link" href="{address}">{html.escape(label or relative)}</a>'

    labels = {"rem_id": "REM", "repo_locator": "Repository", "as_of": "as_of", "generated_at": "生成时间", "observed_at": "观察时间",
              "source_revision": "来源 HEAD", "snapshot_id": "快照 ID", "viewpoint": "评审视角", "mission_context": "Mission context"}
    metadata = "".join(f'<div><dt>{label}</dt>{bound(key, "dd", "mono")}</div>' for key, label in labels.items())
    header = f'{bound("narrative.title", "h1")}<p class="subtitle">{bound("narrative.summary")}</p><dl class="meta">{metadata}</dl>'
    check_labels = {"projection": "投影一致性", "source_consistency": "来源字段比对", "human_review": "人类评审", "runtime": "现实验收", "freshness": "当前新鲜度", "g_id": "编号唯一性", "g_distort": "失真声明", "g_voice": "句子来源", "g_tier": "Tier A 结构", "g_orphan": "孤儿与悬挂引用"}
    checks = '<ul class="checks">' + "".join(
        f'<li class="{html.escape(value)}"><strong>{check_labels[field]}</strong>{bound(f"check.{field}", css="status")}</li>'
        for field, value in sorted(model["checks"].items())) + '</ul>'
    failures_html = '<section class="failures"><h2>Failures First</h2>'
    if model["failures"]:
        failures_html += '<ol>' + "".join(
            f'<li><strong>{bound(f"failure.{index}.id", css="status")} · {bound(f"failure.{index}.severity", css="status")}</strong>'
            f'<p>{bound(f"failure.{index}.assertion")}</p><p>Evidence: {bound(f"failure.{index}.evidence", css="source-link")}</p>'
            f'<p>Next: {bound(f"failure.{index}.next")}</p></li>'
            for index, _failure in enumerate(model["failures"])) + '</ol>'
    else:
        failures_html += '<p>当前 envelope 未包含失败记录；未运行检查仍按其状态显示。</p>'
    failures_html += '</section>'
    groups = {}
    for entry in semantic["entries"]:
        prefix = entry["naming_id"].partition(".")[0]
        groups.setdefault((prefix, entry["domain"]), []).append(entry)
    overview = '<div class="domains">'
    for (prefix, domain), records in groups.items():
        assigned = sum(record["allocation"] == "assigned" for record in records)
        admitted = sum(record["ontology_disposition"] == "admitted" for record in records)
        overview += f'<article class="domain"><span class="id">{html.escape(prefix)}</span><strong>{html.escape(domain)}</strong><small>{len(records)} records · {assigned} assigned · {admitted} admitted</small></article>'
    if not groups:
        if semantic["target"]["namespace"] == "NP0":
            for title, label in (
                ("Narrative", "零阶行动叙事 (显影差异与赋能行动)"),
                ("Naming", "离散固态记忆 (不可变数学寻址)"),
                ("Ontology", "语义强约束 (防止散文腐败)"),
                ("Pipeline", "四维核心能力 (态势/语义/决策/进化)"),
            ):
                overview += f'<article class="domain"><strong>{title}</strong><small>{label}</small></article>'
        else:
            for title, label in (("EGO", "持续行动主体"), ("Mission", "可验收承诺"), ("Repo", "制度化执行与交接")):
                overview += f'<article class="domain"><strong>{title}</strong><small>{label}</small></article>'
    overview += '</div><p class="scope">' + " · ".join(bound(f"target.{field}") for field in sorted(semantic["target"])) + '</p>'
    overview += '<section class="distortions"><h3>失真声明</h3>'
    if semantic["distortion_declarations"]:
        overview += '<ul>' + "".join(
            f'<li>{bound(f"distortion.{index}.surface")} · omitted_count={bound(f"distortion.{index}.omitted_count")} · {bound(f"distortion.{index}.reason")}</li>'
            for index, _item in enumerate(semantic["distortion_declarations"])) + '</ul>'
    else:
        overview += '<p>Caller 未声明省略、截断、聚合或取整。</p>'
    overview += '</section>'
    if semantic["findings"]:
        overview += f'<aside class="callout"><h3>{len(semantic["findings"])} 项来源差异</h3><a href="#findings">查看待裁决项</a></aside>'
    if model["delta"]:
        delta = model["delta"]
        overview += '<p class="delta">上一版：<a href="' + quote(model["previous_stem"] + '.html') + '">' + html.escape(model["previous_snapshot_id"][:8]) + '</a>'
        overview += f' · source paths: {len(delta["source_paths"])} · semantic changed: {delta["semantic_changed"]} · presentation changed: {delta["presentation_changed"]}</p>'

    # 1. Modern Four-Layer Cockpit Architecture
    l1_items = [f'<li><strong>结构定位</strong>: <code>{html.escape(str(semantic.get("repo_locator", "")))}</code> 结构自洽承载</li>']
    if groups:
        l1_items.append(f'<li><strong>领域大盘</strong>: 包含 {len(groups)} 个领域分区，已注册 {sum(len(r) for r in groups.values())} 实体坐标</li>')
        admitted_cnt = sum(record["ontology_disposition"] == "admitted" for r in groups.values() for record in r)
        assigned_cnt = sum(record["allocation"] == "assigned" for r in groups.values() for record in r)
        l1_items.append(f'<li><strong>准入统计</strong>: {admitted_cnt} admitted · {assigned_cnt} assigned</li>')
    else:
        l1_items.append('<li><strong>零阶公理</strong>: Universal Core，通用零阶行动叙事与不可变寻址</li>')
    l1_list = "".join(l1_items)

    l2_items = []
    for index in range(len(narrative["claims"])):
        l2_items.append(f'<li><strong>主张 {index + 1}</strong>: {bound(f"narrative.claims.{index}")}</li>')
    if "delta" in narrative:
        for field in sorted(narrative["delta"]):
            l2_items.append(f'<li><strong>Delta {field}</strong>: {bound(f"narrative.delta.{field}")}</li>')
    if "eval_target" in narrative:
        for field in sorted(narrative["eval_target"]):
            l2_items.append(f'<li><strong>EVAL Target {field}</strong>: {bound(f"narrative.eval_target.{field}")}</li>')
    l2_list = "".join(l2_items)

    l3a_items = []
    for index in range(len(narrative["unknowns"])):
        l3a_items.append(f'<li><strong>未知 {index + 1}</strong>: {bound(f"narrative.unknowns.{index}")}</li>')
    l3a_list = "".join(l3a_items)

    l3b_items = [
        f'<li><strong>Decision Rights</strong>: {bound("narrative.decision_rights")}</li>',
        f'<li><strong>Next Action</strong>: {bound("narrative.next_action")}</li>',
        f'<li><strong>Verification</strong>: {bound("narrative.verification_route")}</li>'
    ]
    l3b_list = "".join(l3b_items)

    four_layers = f"""<section class="four-layers">
  <div class="layer-card c1 card-order l3b">
    <div class="layer-title">
      <span>1. Order (愿)</span>
      <span class="layer-tag">关键工单与刚性约束</span>
    </div>
    <div class="layer-desc">当下做什么？向前发愿，锁定决策责任人、边界动作与验证路线。</div>
    <ul class="layer-list">{l3b_list}</ul>
  </div>
  <div class="layer-card c2 card-event l2">
    <div class="layer-title">
      <span>2. Event (业)</span>
      <span class="layer-tag">现实底账与现场事实</span>
    </div>
    <div class="layer-desc">发生了什么？承接当下运行态事实、准入事件与业务主张。</div>
    <ul class="layer-list">{l2_list}</ul>
  </div>
  <div class="layer-card c3 card-trace l3a">
    <div class="layer-title">
      <span>3. Trace (缘)</span>
      <span class="layer-tag">因果溯源与已知未知</span>
    </div>
    <div class="layer-desc">为什么？向后逆观，核对来源一致性与尚未显影的未知项。</div>
    <ul class="layer-list">{l3a_list}</ul>
  </div>
  <div class="layer-card c4 card-name l1">
    <div class="layer-title">
      <span>4. Name (名)</span>
      <span class="layer-tag">实体本体与地址坐标</span>
    </div>
    <div class="layer-desc">是什么？标定认知对象、领域边界与物理地址寻址体系。</div>
    <ul class="layer-list">{l1_list}</ul>
  </div>
</section>"""

    # 2. Tactical Grid: 2fr Left (Lexicon & Bindings) + 1fr Right (Observations & Sources)
    entries_html = ""
    if semantic["entries"]:
        entries_html = '<div class="table-wrap scrollable" tabindex="0"><table class="lexicon"><thead><tr><th>NID</th><th>Token / 语义与来源</th><th>Allocation</th><th>Lifecycle</th><th>Ontology</th></tr></thead><tbody>'
        for index, entry in enumerate(semantic["entries"]):
            prefix = f"entry.{index}."
            entries_html += f'<tr><td class="key">{bound(prefix + "naming_id", css="mono")}</td><td class="name">{bound(prefix + "token", "strong")}{bound(prefix + "chinese_name", css="cn")}'
            entries_html += f'<p>{bound(prefix + "distinction")}</p><details><summary>Labels / 边界</summary><dl class="binding-detail">'
            for field in ("name_key", "labels", "domain", "authority_route", "boundary"):
                entries_html += f'<dt>{field}</dt>{bound(prefix + field, "dd")}'
            entries_html += '</dl></details>' + link(entry["source"], "来源") + ' ' + bound(prefix + "source", css="source-link") + '</td>'
            entries_html += f'<td>{bound(prefix + "allocation", css="status")}</td><td>Naming: {bound(prefix + "lifecycle", css="status")}<br>Entity: {bound(prefix + "entity_lifecycle", css="status")}</td>'
            entries_html += f'<td>{bound(prefix + "ontology_disposition", css="status")}<br>{bound(prefix + "oid", css="mono")}</td></tr>'
        entries_html += '</tbody></table></div>'
    else:
        if semantic["target"]["namespace"] == "NP0":
            entries_html = '<p class="empty">当前为 NP0 零阶公理与核心能力范围，无领域数字词条；未申请 Entity / Oid 准入。</p>'
        else:
            entries_html = '<p class="empty">当前为 REM 通用范围，无领域数字词条；未申请 Entity / Oid 准入。</p>'

    findings_html = ""
    if semantic["findings"]:
        findings_html = f'<div class="sub-panel" id="findings"><div class="panel-header" style="font-size:14px; margin: 12px 0 8px;"><span>来源差异与待裁决项 (Findings)</span><span class="badge badge-wait">{len(semantic["findings"])} 项差异</span></div><div class="table-wrap scrollable" tabindex="0"><table class="findings"><thead><tr><th>目标 / 字段</th><th>Naming 来源</th><th>另一来源</th><th>分诊 / 路由</th></tr></thead><tbody>'
        for index, finding in enumerate(semantic["findings"]):
            prefix = f"finding.{index}."
            findings_html += f'<tr><td>{bound(prefix + "target", css="mono")}<br>{bound(prefix + "field")}</td>'
            findings_html += f'<td>{bound(prefix + "expected")}<br>{link(finding["expected_source"], "来源")} {bound(prefix + "expected_source", css="source-link")}</td>'
            findings_html += f'<td class="actual">{bound(prefix + "actual")}<br>{link(finding["actual_source"], "来源")} {bound(prefix + "actual_source", css="source-link")}</td>'
            findings_html += f'<td>{bound(prefix + "classification", css="status")}<br>{bound(prefix + "route")}</td></tr>'
        findings_html += '</tbody></table></div></div>'
    else:
        findings_html = '<p class="empty" style="margin-top: 14px;">当前检查范围未记录来源字段差异；不构成现实效果证明。</p>'

    left_panel = f"""<div class="panel">
  <div class="panel-header">
    <span>词条与实体操纵台 (Lexicon & Bindings)</span>
    <span class="badge badge-live">{len(semantic["entries"])} 条记录</span>
  </div>
  {entries_html}
  {findings_html}
</div>"""

    obs_html = '<details open><summary>四件套声明、独立观测与信念度</summary>'
    for name, observation in sorted(semantic["observations"].items()):
        prefix = f"observation.{name}"
        obs_html += f'<div class="source-item"><h3>{html.escape(name)}</h3><p>Credence: {bound(prefix + ".Credence", css="status")}</p>'
        for field in ("source_claims", "Claim", "unknowns", "delta"):
            obs_html += f'<dl><dt>{field}</dt>'
            for index in range(len(observation[field])):
                obs_html += bound(f"{prefix}.{field}.{index}", "dd")
            obs_html += '</dl>'
        for index, fact in enumerate(observation["Fact"]):
            obs_html += '<dl><dt>Fact</dt>'
            for field in fact:
                obs_html += bound(f"{prefix}.Fact.{index}.{field}", "dd")
            obs_html += '</dl>'
        obs_html += '</div>'
    obs_html += '</details>'

    reference_labels = {relative: label for label, relative in semantic.get("reference_sources", {}).items()}
    sources_html = '<div class="sub-panel"><h4>来源与版本</h4><dl class="sources">'
    for relative, revision in sorted(model["sources"].items()):
        label = reference_labels.get(relative)
        title = bound(f"reference_source.{label}", "span", "mono") if label else link(relative)
        source_path = f'{link(relative)}<br>' if label else ""
        sources_html += f'<div class="source-item"><dt>{title}</dt><dd>{source_path}sha256: {html.escape(revision["sha256"])}<br>dirty: {revision["dirty"]}</dd></div>'
    sources_html += f'</dl><p class="delta">schema {SCHEMA_VERSION} · contract {CONTRACT_VERSION} · renderer {RENDERER_VERSION}<br>semantic sha256: {model["semantic_sha256"]}</p></div>'
    sources_html += '<div class="sub-panel"><h4>句子来源与规则</h4><dl>'
    for slot in sorted(semantic["voice_sources"]):
        sources_html += f'<dt>{html.escape(slot)}</dt>{bound(f"voice_source.{slot}", "dd", "source-link")}'
    sources_html += '</dl></div>'

    right_panel = f"""<div class="panel">
  <div class="panel-header">
    <span>独立观测与来源审计 (Observations & Sources)</span>
    <span class="badge badge-wait">四件套独立观测</span>
  </div>
  <div class="panel-body">
    {obs_html}
    {sources_html}
  </div>
</div>"""

    tactical_grid = f"""<section class="tactical-grid">
  {left_panel}
  {right_panel}
</section>"""

    authority = bound("authority", css="mono")
    require(used == set(values), f"Unrendered semantic fields: {set(values) - used}")
    footer = semantic.get("footer_html") or f'TeamPage MPS · Mirror Page · Authority: {authority}<br>Owner / owning workflow 持有裁决权。生成时间不代表来源实时状态。'
    document = Template(TEMPLATE.read_text(encoding="utf-8")).substitute(
        page_title=html.escape(narrative["title"]), header=header, checks=checks, failures=failures_html, overview=overview,
        four_layers=four_layers, tactical_grid=tactical_grid, footer=footer)
    require(document.count("</body>") == 1, "Expected one HTML body end tag")
    mp_data = encode_embedded_payload(model)
    script = f'<script id="mp-data" type="application/json">{mp_data}</script>\n'
    return document.replace("</body>", script + "</body>", 1)


def write_index(repo: Path, folder: Path | None = None) -> Path:
    if folder is None:
        folder = repo.resolve() / "Repo/shape/TeamsPage"
    else:
        folder = Path(folder).resolve()
    require(folder.is_dir() and folder.resolve() == folder, "Missing or redirected TeamPage custody")
    snapshots = []
    groups = {}
    for path in sorted(folder.glob("*.html")):
        if not path.name.startswith("MPS-"):
            continue
        document = path.read_text(encoding="utf-8")
        model = read_artifact_model(path)
        if model.get("projection_contract_version") != CONTRACT_VERSION:
            continue
        validate_artifact(path)
        envelope_label = "embedded #mp-data"
        if "semantic" not in model:
            continue
        semantic = model["semantic"]
        family = canonical({
            "rem_id": semantic.get("rem_id", semantic.get("ram_id", "")),
            "repo_locator": semantic["repo_locator"],
            "target": semantic["target"],
            "viewpoint": semantic["viewpoint"],
        })
        groups.setdefault(family, []).append(timestamp(model["generated_at"]))
        snapshots.append((path, model, family, envelope_label))
    rows = []
    for path, model, family, envelope_label in sorted(snapshots, key=lambda item: timestamp(item[1]["generated_at"]), reverse=True):
        title = model["semantic"]["narrative"]["title"].replace("|", "\\|").replace("\n", " ")
        title = re.sub(r"([\[\]\\])", r"\\\1", title)
        latest_time = max(groups[family])
        latest = "no"
        if timestamp(model["generated_at"]) == latest_time:
            latest = "same-second tie" if groups[family].count(latest_time) > 1 else "yes"
        review_labels = {"human": "not_run", "agent": "not_run"}
        reviews = []
        for review_path in folder.glob(model["stem"] + "--review-*.json"):
            event = json.loads(review_path.read_text(encoding="utf-8"))
            require(event["snapshot_id"] == model["snapshot_id"] and event["html_sha256"] == digest(path.read_bytes()), "Review targets a different artifact")
            reviews.append((event, review_path))
        for event, review_path in sorted(reviews, key=lambda pair: timestamp(pair[0]["reviewed_at"])):
            require(event["reviewer_type"] in review_labels and event["result"] in {"pass", "issues_found", "inconclusive"}, "Invalid review disposition")
            review_labels[event["reviewer_type"]] = f'[{event["result"]}]({review_path.name})'
        previous = "none"
        if model["previous_snapshot_id"]:
            previous = f'[{model["previous_snapshot_id"][:8]}]({model["previous_stem"]}.html)'
        rows.append(f'| [{title}]({path.name}) | {latest} | {model["generated_at"]} | {model["snapshot_id"][:8]} | {previous} | {model["checks"]["source_consistency"]} | {review_labels["human"]} | {review_labels["agent"]} | {envelope_label} |')
    index = '## Generated TeamPage MPS Snapshot Index\n\n'
    index += '| Target | Latest | Generated At | Snapshot | Previous | Source Check | Human Review | Agent Review | Provenance |\n|---|---|---|---|---|---|---|---|---|\n'
    index += '\n'.join(rows) + '\n'
    generated_block = f"{INDEX_START}\n{index}{INDEX_END}"
    path = folder / "README.md"
    require(not path.is_symlink(), "Redirected TeamPage index")
    if path.is_file():
        raw = path.read_bytes()
        newline = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        has_start = INDEX_START in text
        has_end = INDEX_END in text
        if has_start or has_end:
            require(text.count(INDEX_START) == 1 and text.count(INDEX_END) == 1,
                    "TeamPage index markers are missing or ambiguous")
            start = text.index(INDEX_START)
            end = text.index(INDEX_END)
            require(start < end, "TeamPage index markers are out of order")
            text = text[:start] + generated_block + text[end + len(INDEX_END):]
        else:
            text = text.rstrip() + "\n\n" + generated_block + "\n"
    else:
        newline = "\n"
        text = ('# Repo/shape/TeamsPage - Mirror Page review output\n\n'
                '> non-authority/no-writeback；当前实践索引，不是验收或长期 archive。\n\n'
            '[TeamPage runtime contract](../../../.agents/skills/teamspage/references/teamspage-runtime-contract.md) · [shape custody](../Motion/README.md)\n\n'
                + generated_block + "\n")
    path.write_text(text, encoding="utf-8", newline=newline)
    return path


def generate(repo: Path, request: dict, *, destination: Path | None = None, **options) -> Path:
    repo = repo.resolve()
    model = build_model(repo, request, **options)
    require(not model["mp:sample"], "MPS sample pages are built as eval baselines, not emitted as review artifacts")
    if destination is None:
        destination = repo / "Repo" / "shape" / "TeamsPage"
    else:
        destination = Path(destination).resolve()
    require(destination.is_relative_to(repo), "Destination escapes repo")
    require(not (destination.is_relative_to(repo / "Repo/Dojo") and destination != (repo / "Repo/Dojo")),
            "Illegal Dojo subdirectory; TeamPage outputs to Repo/shape/TeamsPage or flat Repo/Dojo")
    destination.mkdir(parents=True, exist_ok=True)
    model["checks"]["projection"] = "pass"
    if destination == (repo / "Repo/shape/TeamsPage"):
        for existing in destination.glob("MPS-*.html"):
            existing_model = read_artifact_model(existing)
            require(existing_model["snapshot_id"] != model["snapshot_id"],
                    "Snapshot ID already emitted; create a new snapshot identity")
    document = render_html(model).encode("utf-8")
    validate_html(model, document.decode("utf-8"))
    artifact = destination / f'{model["stem"]}.html'
    require(not artifact.exists(), "Snapshot collision; never overwrite")
    for relative, revision in model["binding_revisions"].items():
        require(digest(input_source(repo, relative).read_bytes()) == revision["sha256"], "Source changed before output")
    with artifact.open("xb") as stream:
        stream.write(document)
    return artifact


def export_delivery(source_html: Path, destination: Path, repo: Path) -> Path:
    repo = repo.resolve()
    source_html = source_html.resolve()
    destination = destination.resolve()
    require(source_html.is_file() and source_html.suffix == ".html", "Source must be an existing TeamPage HTML file")
    require(destination.is_relative_to(repo / "Mission"), "Delivery destination must be within Mission/")
    require(not destination.is_relative_to(repo / "Repo"), "Delivery destination cannot be within Repo/")
    if destination.is_dir() or destination.suffix != ".html":
        destination = destination / source_html.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(source_html.read_bytes())
    return destination


def record_review(artifact: Path, review: dict) -> Path:
    validate_artifact(artifact)
    model = read_artifact_model(artifact)
    html_artifact = artifact if artifact.suffix == ".html" else artifact.parent / f'{model["stem"]}.html'
    html_sha256 = digest(html_artifact.read_bytes())
    require(isinstance(review, dict), "Expected review object")
    require(set(review) == {"reviewer", "reviewer_type", "reviewed_at", "criteria", "result", "findings", "evidence"}, "Invalid review fields")
    require(review["reviewer_type"] in {"human", "agent"}, "Unknown reviewer type")
    require(review["result"] in {"pass", "issues_found", "inconclusive"}, "Unknown review result")
    for field in ("reviewer", "criteria", "evidence"):
        require(isinstance(review[field], str) and bool(review[field].strip()), f"Missing review {field}")
    require(isinstance(review["findings"], list) and all(isinstance(item, str) and item.strip() for item in review["findings"]), "Invalid findings")
    require(bool(review["findings"]) or review["result"] != "issues_found", "Missing issue evidence")
    require(timestamp(review["reviewed_at"]) >= timestamp(model["generated_at"]), "Review precedes generation")
    review_id = uuid.uuid4().hex
    event = {"schema_version": SCHEMA_VERSION, "authority": AUTHORITY, "review_id": review_id,
             "snapshot_id": model["snapshot_id"], "html_sha256": html_sha256, **review}
    path = html_artifact.parent / f'{model["stem"]}--review-{review_id}.json'
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(event, ensure_ascii=False, indent=2) + "\n")
    return path


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for directory in [current, *current.parents]:
        if (directory / ".git").is_dir() or ((directory / "Repo").is_dir() and (directory / "EGO").is_dir()):
            return directory
    return current


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a non-authority TeamPage MPS artifact")
    parser.add_argument("--repo", type=Path, default=None, help="Repository root path")
    parser.add_argument("--input", type=Path)
    parser.add_argument("--capture", action="store_true")
    parser.add_argument("--artifact", type=Path)
    parser.add_argument("--review-input", type=Path)
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--index", action="store_true")
    parser.add_argument("--observations", action="store_true")
    parser.add_argument("--view")
    parser.add_argument("--export", type=Path, default=None, help="Export a standalone TeamPage HTML file to Mission delivery destination")
    parser.add_argument("--from-teamspage", type=Path, default=None, help="Source TeamPage HTML artifact to export")
    args = parser.parse_args()
    try:
        repo = find_repo_root(args.repo)
        if args.export:
            source = args.from_teamspage
            if source is None:
                teamspage_dir = repo / "Repo" / "shape" / "TeamsPage"
                candidates = sorted(teamspage_dir.glob("*.html"), key=lambda p: p.stat().st_mtime, reverse=True)
                require(bool(candidates), "No source TeamPage HTML found in Repo/shape/TeamsPage to export")
                source = candidates[0]
            exported = export_delivery(source, args.export, repo)
            try:
                rel = exported.relative_to(repo)
            except ValueError:
                rel = exported
            print(f"Exported TeamPage MPS artifact to: {rel.as_posix()}")
            return
        if args.index:
            print(write_index(repo))
            return
        if args.artifact:
            if args.review_input:
                print(record_review(args.artifact, json.loads(args.review_input.read_text(encoding="utf-8-sig"))))
            else:
                print(json.dumps(validate_artifact(args.artifact, repo), ensure_ascii=False, indent=2))
            return
        require(args.input is not None, "Provide --input or --artifact")
        request = json.loads(args.input.read_text(encoding="utf-8-sig"))
        if args.view:
            request = select_view(request, args.view)
        if args.capture:
            request = capture_request(repo, request)
        if args.observations:
            print(generate_observations(repo, request["snapshot"]))
        previous = None
        if args.previous:
            validate_artifact(args.previous)
            previous = json.loads(args.previous.read_text(encoding="utf-8"))
        views = request.pop("views", None)
        if views is None:
            print(generate(repo, request, previous=previous))
        else:
            require(previous is None and isinstance(views, list) and bool(views), "Invalid batch or previous baseline")
            for view in views:
                require(isinstance(view, dict) and set(view) == {"target", "narrative", "viewpoint"}, "Views may only specialize target, narrative and viewpoint")
                build_model(repo, {**request, **view})
            for view in views:
                print(generate(repo, {**request, **view}))
    except (SnapshotBlocked, OSError, ValueError) as error:
        parser.exit(1, f"blocked: {error}\n")


if __name__ == "__main__":
    main()
