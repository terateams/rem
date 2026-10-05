# Audit - Ego canonical path migration

> **Date**: 2026-10-05
> **Owner**: yangjun / bitguts
> **Status**: Executed; Owner acceptance pending
> **Scope**: Git-tracked root and entry-path casing migration, target path adapters, references, validation, and push
> **Source Motion**: [motion-ego-path-migration](../../Repo/Motion/motion-ego-path-migration-2026-10-05.md)
> **Runtime Approval**: Owner current conversation: “要发布 Ego，还需先把大小写改名和相关路径迁移正式登记到 Git，再验证并推送”
> **Implementation Commit**: `c3158d3` (`Adopt canonical Ego path casing`)
> **History Triage Result**: Audit First; source retirement pending Owner acceptance

## Baseline and Action

Before the change, the Windows worktree displayed `Ego/`, while `HEAD` tracked `EGO/`; `core.ignorecase=true` meant `git status` did not report the case-only mismatch. The Owner authorized the bounded migration, validation, commit, and normal push in the current conversation. The Motion was Draft when execution began; this Audit does not claim a durable Approved state.

Git now tracks `Ego/` and `Ego/Ego-rem.md`. The rename used temporary intermediate names so Git recorded exact casing. Current authority, README, Mission bindings, executable adapters, tests, `.gitattributes`, source manifest, and Markdown link targets were migrated. Historical prose and upstream identifier `EGO-T189` remain unchanged; old TeamsPage HTML was not regenerated and is stale under its existing source-freshness rule.

The NP0 runtime snapshot and its tests are registered as target deltas for `Ego/`; the canonical NP0 capsule remains byte-identical at SHA-256 `0b534f72ba37df8799616f91b993f466530611f6eb4b5d084494260f6a0754f6`. The manifest now records five unchanged files and four target deltas.

## Validation and Sync

- `python -m compileall -q scripts .agents/skills/np0/scripts .agents/skills/teamspage/MPS/scripts`: pass.
- `python .agents/skills/np0/scripts/test_runtime_snapshot.py`: 10/10 pass.
- `python -m unittest discover -s scripts -p "test_*.py"`: 15/15 pass.
- `python scripts/verify.py`: `structure=pass`, `failures=[]`; `human_review`, `runtime_models`, and `role_alignment` are `not_run`.
- Case-sensitive link and source/config searches found no live `EGO/` path references. Git index records `Ego/Ego-rem.md` and no tracked `EGO/` root.
- `git diff --cached --check`: pass.
- Commit `c3158d3` was pushed with ordinary `git push`; remote advanced `596ce1a..c3158d3` on `main`.

No Cloudflare, DNS, model, credential, paid, or deployment action occurred. Machine checks do not establish Human acceptance or product Mission completion. Owner acceptance remains pending; the Motion stays on the working surface and is not retired.
