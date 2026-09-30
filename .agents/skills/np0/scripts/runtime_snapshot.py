from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path


class SnapshotBlocked(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SnapshotBlocked(message)


def git(repo: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *arguments],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    require(result.returncode == 0, "Git source baseline unavailable")
    return result.stdout.strip()


def source_file(repo: Path, relative: str) -> Path:
    require(isinstance(relative, str) and bool(relative), "Missing source path")
    require("\\" not in relative, "Use repository-relative POSIX paths")
    path = Path(relative)
    require(not path.is_absolute() and ".." not in path.parts, "Source path escapes repo")
    require(path.parts[0] in {"EGO", "Mission", "Repo", ".github"}, "Source outside allowlisted surfaces")
    require(path.suffix == ".md", "Only explicit Markdown sources are supported")
    require(not relative.startswith("Repo/Dojo/"), "Practice output cannot supply authority")
    target = (repo / path).resolve()
    require(target.is_relative_to(repo), "Source symlink escapes repo")
    require(target.is_file(), f"Missing source: {relative}")
    return target


def prepare(repo: Path, payload: dict) -> tuple[str, dict[str, str]]:
    repo = repo.resolve()
    require(isinstance(payload, dict), "Expected snapshot object")
    require(payload.get("schema_version") == "1.0", "Unsupported snapshot schema")
    run_id = payload.get("run_id", "")
    slug = payload.get("slug", "")
    require(isinstance(run_id, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", run_id) is not None, "Invalid run_id")
    require(isinstance(slug, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", slug) is not None, "Invalid EGO slug")
    observed_at = payload.get("observed_at")
    require(isinstance(observed_at, str), "Missing observed_at")
    try:
        observed = datetime.fromisoformat(observed_at)
    except ValueError as error:
        raise SnapshotBlocked("Invalid observed_at") from error
    require(observed.utcoffset() is not None, "observed_at requires timezone")
    require(payload.get("scope") not in (None, ""), "Missing scope")
    require(isinstance(payload.get("scope"), str), "scope must be text")
    permission = payload.get("permission", {})
    require(isinstance(permission, dict), "Missing permission declaration")
    require(permission.get("snapshot_write") is True, "Snapshot write not authorized")
    require(isinstance(permission.get("approved_by"), str) and bool(permission["approved_by"].strip()), "Missing decision-rights holder")
    require(isinstance(permission.get("approval_evidence"), str) and bool(permission["approval_evidence"].strip()), "Missing approval evidence")
    require(permission.get("content_reviewed_no_secrets") is True, "Payload custody review required")
    allowed = permission.get("allowed_sources")
    require(isinstance(allowed, list) and all(isinstance(item, str) for item in allowed), "Missing source allowlist")
    binding = payload.get("binding", {})
    require(isinstance(binding, dict), "Missing RAM binding")
    for name, prefix in (("mission", "Mission/Story-"), ("eval", "Mission/EVAL/"), ("authority", ".github/")):
        require(isinstance(binding.get(name), str) and binding[name].startswith(prefix), f"Missing or invalid {name} binding")
    method = payload.get("selected_method")
    require("selected_method" in payload, "Declare selected_method, including null")
    if method is not None:
        require(isinstance(method, dict) and isinstance(method.get("name"), str) and bool(method["name"]), "Invalid selected method")
        require(isinstance(method.get("source"), str) and method["source"].startswith("EGO/"), "Missing selected-method source")
    working_name = "Working.md" if (repo / "EGO" / "Working.md").is_file() else "ATM.md"
    filenames = [f"EGO-{slug}.md", "EdgeTeam.md", "Naming.md", working_name]
    paths = [f"EGO/{name}" for name in filenames]
    paths += [binding["mission"], binding["eval"], binding["authority"], "Repo/today.md", "Repo/now.md"]
    if method is not None:
        paths.append(method["source"])
    require(set(paths).issubset(set(allowed)), "Source read not authorized")
    expected = payload.get("source_sha256", {})
    require(isinstance(expected, dict), "Missing source hashes")
    head = git(repo, "rev-parse", "HEAD")
    require(payload.get("source_commit") == head, "Source commit changed")
    revisions = {}
    contents = {}
    for relative in paths:
        target = source_file(repo, relative)
        content = target.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        require(isinstance(expected.get(relative), str) and expected[relative].lower() == digest, f"Source hash changed: {relative}")
        contents[relative] = content.decode("utf-8-sig")
        revisions[relative] = {
            "commit": head,
            "sha256": digest,
            "dirty": bool(git(repo, "status", "--porcelain", "--", relative)),
        }
    baseline = re.search(r"(?m)^# today - (\d{4}-\d{2}-\d{2})\s*$", contents["Repo/today.md"])
    require(baseline is not None, "Missing today date baseline")
    baseline_date = baseline.group(1)
    require(payload.get("baseline_date") == baseline_date == observed.date().isoformat(), "Stale date baseline")
    require(baseline_date in contents["Repo/now.md"], "now / today date disagreement")
    observations = payload.get("observations")
    require(isinstance(observations, dict) and set(observations) == set(filenames), "Expected exactly four observation records")
    documents = {}
    for name in filenames:
        record = observations[name]
        require(isinstance(record, dict), f"Invalid observation: {name}")
        require(set(record) == {"source_claims", "Fact", "Claim", "Credence", "unknowns", "delta"}, f"Invalid observation fields: {name}")
        require(record["Credence"] in (None, "unknown", "low", "medium", "high"), "Use ordinal or unknown Credence")
        for field in ("source_claims", "Claim", "unknowns", "delta"):
            require(isinstance(record[field], list) and all(isinstance(item, str) for item in record[field]), f"Invalid {field}: {name}")
        require(isinstance(record["Fact"], list), "Fact must be a list")
        for fact in record["Fact"]:
            require(isinstance(fact, dict) and set(fact) == {"statement", "evidence", "observed_at"}, "Facts require independent evidence and time")
            require(all(isinstance(value, str) and bool(value.strip()) for value in fact.values()), "Empty fact evidence")
        envelope = {
            "authority": "non-authority/no-writeback",
            "source_path": f"EGO/{name}",
            "source_revision": revisions[f"EGO/{name}"],
            "binding_revisions": revisions,
            "observed_at": observed_at,
            "scope": payload["scope"],
            "selected_method": method,
            "permission_declaration": permission,
            **record,
        }
        documents[name] = f"# NP0 Observation: {name}\n\n> non-authority/no-writeback\n\n```json\n{json.dumps(envelope, ensure_ascii=False, indent=2)}\n```\n"
    return run_id, documents


def generate(repo: Path, payload: dict) -> Path:
    repo = repo.resolve()
    run_id, documents = prepare(repo, payload)
    dojo = repo / "Repo" / "Dojo"
    require(dojo.is_dir() and not dojo.is_symlink(), "Missing or symlinked Dojo")
    require(dojo.resolve() == dojo, "Dojo parent is redirected")
    destination = dojo / f"np0-runtime-{run_id}"
    require(not destination.exists(), "Run already exists; use a new run_id")
    with tempfile.TemporaryDirectory(prefix=".np0-stage-", dir=dojo) as temporary:
        stage = Path(temporary) / "snapshot"
        stage.mkdir()
        for name, text in documents.items():
            (stage / name).write_text(text, encoding="utf-8", newline="\n")
        require(prepare(repo, payload)[1] == documents, "Source changed during generation")
        require(not destination.exists(), "Run already exists")
        stage.rename(destination)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate or render an approved NP0 observation snapshot")
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8-sig"))
        if args.check:
            prepare(args.repo, payload)
            print("PASS: snapshot input checks only; no authority or factual-truth certification")
        else:
            print(generate(args.repo, payload))
    except (SnapshotBlocked, OSError, ValueError) as error:
        parser.exit(1, f"blocked: {error}\n")


if __name__ == "__main__":
    main()
