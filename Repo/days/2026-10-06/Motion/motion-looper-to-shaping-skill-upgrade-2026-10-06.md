# Motion: Upgrade rem Looper to Shaping

> **Date**: 2026-10-06
> **Player**: yangjun / bitguts
> **Status**: Done
> **Type**: AgentSkill capability migration / repo-wide maintenance route
> **Service Object**: rem maintenance, resolver hygiene, bounded repository shaping
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> [EVAL](../../../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Player 当前对话：“理解 skill of shaping，它是对原来 looper 的升级。理解后，升级当下的 looper，改名为 shaping，实行同样或者更好的效果；起草 Motion 先”
> **Target Baseline**: rem `main` at `08028b361b3822ca910788713cb0a00234256255`; clean worktree
> **Source Observation**: `/Users/bitguts/Github/EGO-T189/.agents/skills/shaping/SKILL.md`, local `HEAD=7481175f8390dfcd95b0abed43e65d9fe25cd1a0`; existing local `origin/main=7acef414`; the one ahead commit adds only `Repo/shape/days/2026-10/2026-10-05-today.md`. The shaping package and checked RCI / authority paths are unchanged between these local refs; no fetch performed.
> **Source Hashes**: SKILL `035831609519f55bd0db4e2613a4aed891af604a4a01427cc65438502da9304d`; portable contract `76ab62513bba5fcdd951c1c9967ec485ef8451dcc688be9390e50b81236b18f0`; eval corpus `5b314b2c4552d71f9a99203a5c51487655937c4ceca04581a6b65ed614e80509`
> **Round**: R1

## 问题与拟议裁决

The current rem `looper` is a target-adapted, report-first maintenance Skill. It already owns bounded inspection/repair, path drift, asset placement, Dojo boundaries, handoff, and migration of approved dated assets. The observed EGO-T189 `shaping` Skill broadens this predecessor capability: it retains Recover -> Inspect -> Condition -> Handoff while adding repo-wide layer/authority classification, resolver and consumer audits, motion/process hygiene, experience retention, shared-slop review, capability/cost conditioning, revision-candidate routing, and a behavior-eval map.

The proposal is therefore a capability upgrade plus identity/path migration, not a rename-only edit. The target must adapt the portable behavior to rem's `RWS` work-system source, independent `RAP` rules source, exactly-one-Primary binding, local Mission/EVAL, rem paths, and existing Skill owners. The source's CRAFTS, ILYA/THALES, RCI-specific and EGO-T189 path bindings are not rem authority and must not be copied as target prescriptions.

## Scope

**Proposed local execution scope, only after a separate Player execution gate:**

- Create target `.agents/skills/shaping/SKILL.md` as a rem-native adaptation of the source Skill, retaining useful looper behavior while adding bounded repo-wide shaping, resolver/source routing, consumer audit, experience-retention and cost/quality review.
- Retire `.agents/skills/looper/SKILL.md` and its active Skill identity after a visible consumer search; do not add an alias Skill or silently forward `/looper` to `/shaping`.
- Define target trigger and exclusion boundaries: repo-wide REM maintenance / shaping can use shaping; daily startup, date/cursor refresh and Away handoff remain rem-ready; named Motion drafting/execution/closeout remains motioner; NP0 narrative remains np0; deterministic MPS generation/validation remains teamspage.
- Keep `Ego/Rws.md` as the work-system authority and `Ego/RAP.md` as the sole RA-rules authority. Shaping may inspect or propose RA refinements but may not bypass RAP, the Player Motion gate, or required RA validation.
- Update only required active consumers: `AGENTS.md`, `Ego/TeamSkill/TeamSkill.md`, `Ego/TeamSkill/deployment.md`, `Repo/Motion/README.md`, `Repo/days/README.md`, `scripts/verify.py`, and direct active Skill references identified by the consumer audit.
- Adapt a small target-native subset of behavior tests from the shaping eval corpus. Preserve rem's explicit permission, Motion ownership, no-CRAFTS, no-secret, source custody, rollback, and no-silent-fallback boundaries; do not bulk-copy source evals or create a second policy matrix.
- Retire the old Skill source and update dated `today` / `now` only through rem-ready after the authorized execution and validation; preserve provenance and existing user state.

**Held / out of scope:**

- The original request was Draft-only; the subsequent Player approval recorded under Runtime Permission authorizes only the bounded local target changes in Scope. No upstream EGO-T189 or rem RWS/RAP authority change is authorized.
- No copying EGO-T189 RCI / CRAFTS / ILYA / THALES policy, source-instance bindings, unadapted paths, or source eval corpus as rem rules.
- No new `skill-creator` identity, generic dispatcher, model router, scheduler, private inventory, or duplicate looper compatibility package.
- The initial Motion approval excluded CLI/tool install or upgrade, external/provider action, paid action, release, commit, and push. Before execution, the local EGO-T189 HEAD and local `origin/main` were compared; the shaping package and checked authority paths were unchanged between those refs. The Player later gave a separate current-conversation Git gate: “审计, commit and push”, scoped to this audited shaping change. This remains a private rem adaptation, not public redistribution.
- No claim of improved capability, behavior parity, independent benchmark, Human acceptance, product EVAL completion, or runtime/model change without the relevant evidence.

## Runtime Permission

Player subsequently approved this Motion with “批准, 执行”. That authorizes the local target-adaptation and migration scope listed above, not source-repository changes, CLI installs/upgrades, external/paid actions, commit, or push. Execution starts while the Motion status is `Draft`; record that fact in the Audit and do not backdate the durable status to `Approved`. The source package is a private EGO-T189 asset; this work is a Player-authorized private rem adaptation and does not authorize public redistribution.

After implementation acceptance and D5 closeout, the Player separately authorized “审计, commit and push” in the current conversation. This later Git permission is limited to auditing and synchronizing this worktree's shaping migration; it does not expand the implementation scope above.

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | Target `shaping` identity has a rem-specific trigger/exclusion contract and required Skill metadata | `ra-check.py`; description/name validation |
| D2 | Existing looper capabilities are retained unless explicitly rejected; daily/rem-ready, Motion/motioner, narrative/np0, MPS/teamspage ownership remains distinct | source-to-target capability map; active consumer audit |
| D3 | Target shaping consumes RWS/RAP/Mission/EVAL and does not import source-only CRAFTS/RCI/ILYA/THALES authorities | Skill/source review; targeted negative references |
| D4 | Old `looper` active identity is fully drained without a duplicate alias; historical references remain provenance-only | repo-wide active reference search; `verify.py` |
| D5 | Target behavior tests cover positive/negative triggers, authority boundaries, permission/stop, consumer routing, rollback and handoff | target-native eval cases and actual execution results |
| D6 | Skill route, registry, verifier, docs, and handoff agree; source/license/freshness are explicit | `ra-check.py`, `verify.py`, focused tests, source hash/revision and Audit |
| D7 | No unsupported readiness, cost, model, Human acceptance, or product EVAL claims | explicit `not_run` / `unknown`; Player review recorded separately |

## Landing / Rollback

The approved local landing makes `.agents/skills/shaping/SKILL.md` the single active repo-shaping Skill identity; `.agents/skills/looper/SKILL.md` and its empty directory are retired, with no alias. The EGO Skill Registry and active route docs point to shaping; startup snapshots remain with rem-ready and Motion lifecycle remains with motioner. Player acceptance is recorded; D5 passed in an eight-case manual in-session self-evaluation, with no claim of independent benchmarking. The completed Motion source is archived at `Repo/days/2026-10-06/Motion/`. Rollback requires a reviewed reverse migration restoring the previous looper route from Git history; do not keep both production identities active or rewrite history.

## Execution Result

Implemented the target-native shaping Skill and eight manual regression prompts; migrated active routes and verifier identity; retired the old looper Skill after consumer search. The canonical [Audit](../../../../Mission/Audit/2026-10-06-shaping-skill-upgrade.md) records the capability map, consumer findings, source boundary, checks, acceptance, D5 results, and limitations.

`ra-check.py`, `verify.py`, JSON parsing, NP0 runtime-snapshot tests (10/10), and the MPS suite (16/16 with canonical macOS `TMPDIR`) passed. The default MPS test invocation exposed one unrelated `/var` versus `/private/var` temp-path assertion mismatch; no test code was changed. All eight shaping prompts passed a manual in-session self-evaluation recorded in the Audit; this is not independent evaluation or a broad capability benchmark. Player acceptance is recorded. Runtime/model availability, role alignment, and product EVAL remain `not_run`. This Motion is `Done` and its source is retired to `Repo/days/2026-10-06/Motion/`.
