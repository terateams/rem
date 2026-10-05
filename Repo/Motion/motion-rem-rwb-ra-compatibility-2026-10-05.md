# Motion: RWB and RA Cross-Platform Alignment

> **Date**: 2026-10-05
> **Player**: yangjun / bitguts
> **Status**: Executed; Player acceptance pending
> **Type**: Rem Workbench / RA rules / cross-platform maintenance
> **Service Object**: rem RWB baseline, RA configuration, and linked Narrative Page
> **Primary Route**: [Story-rem](../../Mission/Story-rem.md) -> [EVAL](../../Mission/EVAL/eval-rem-v1.md)
> **Execution Audit**: [canonical Audit](../../Mission/Audit/2026-10-05-rwb-ra-compatibility.md)
> **Source Request**: Player 当前对话：“理解REM修订方案后, 比照当前的实际情况, 予以执行”；本机方案文件：`/Users/bitguts/Downloads/REM修订方案.md`（不随仓库共享）
> **Baseline**: `f192d175879321a745b1095f5279f7f85f2883ef`; current user-authored `Ego/Rwb.md` is untracked and retained
> **Round**: R1

## 问题与拟议裁决

The supplied plan was written against `a789753`, but execution began at `f192d17`. The local `Ego/Rwb.md` draft already existed as an untracked file; the plan's proposed RWB Naming Motion did not. `Repo/today.md` and `Repo/now.md` already carried the date 2026-10-05, but their handoff content predates this revision. At baseline, RAP was version 0.6.5, `scripts/ra-check.sh` was the only RA checker, and the RAP Narrative Page contained stale audit/source claims and scope not present in RAP.

The Player explicitly requested execution. Apply only the settled, locally executable plan items against current files. D3 was resolved by the Player as `uv run python`; D4 (PDF CLI) remains open. Preserve the existing RWB draft body, hash-pinned source material, historical records, and all unrelated worktree state.

## Scope

**Authorized local scope:**

- Integrate the existing RWB draft without overwriting its narrative: add the RWB entry/links, RWB baseline to `AGENTS.md`, and the Player-approved `RWB` token to Naming.
- Add the missing Scope section to `Ego/RAP.md`, bump RA version to 0.6.6, synchronize the checker version, and regenerate the RAP Narrative Page from the current source state using Copilot.
- Register the approved, pinned `cf` and Wrangler CLI versions and CLI approval/evidence policy in `Ego/Tools.md`.
- Convert `scripts/ra-check.sh` to `scripts/ra-check.py`, remove the shell implementation, update CI and instructions, and use `uv run python` in repository-facing Python commands. Use the existing local `uv`; do not install or upgrade it.
- Apply the listed active-file Owner -> Player and Mirror Page -> Narrative Page terminology changes, preserving historical records and hash-pinned files.
- Apply plan item 3.5's spacing/readability cleanup to `Ego/Tools.md`, `Repo/DONE.md`, and `Repo/INTENT.md` only; preserve historical decision terms and meaning in `DONE.md`.
- Update `Repo/INTENT.md`, `Repo/today.md`, and `Repo/now.md` through the rem-ready route. The current Player request supplies the bounded maintenance task; do not overwrite historical snapshots.

**Out of scope / held:**

- D4 PDF CLI / PDF engine, RAP Rule 5 hooks or credential scanning, Player-only LANTERN acceptance, CI Actions result verification, and any cloud/provider action.
- Install or upgrade `uv`, Python, Node, or other CLI; no global installation. Local `uv 0.12.14` is below the draft's cited `0.12.23` baseline and will be recorded, not silently upgraded.
- Modify source-manifest-pinned files, historical Audits/Motions/evidence, the existing RWB draft narrative, `.venv`, or unrelated files.
- Commit, push, release, deploy, or change permissions.

## Runtime Permission

The current Player request explicitly authorizes local execution of the revision plan, superseding the plan document's earlier statement that the Player would manually apply changes. D3 is resolved as `uv run python`. This does not authorize CLI installation/upgrade, external actions, or commit/push. During execution the source Motion remains `Draft`; the canonical Audit must preserve that fact and the direct conversation approval.

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | RWB draft is preserved and linked from README, AGENTS, and EGO; Naming includes RWB under this Player Motion | exact diffs; local links resolve |
| D2 | RAP contains a sourced Scope; version 0.6.6 matches the checker; shadow page is regenerated with accurate provenance and no stale source claims | page/source hashes; HTML parse; link checks |
| D3 | Python checker replaces the shell checker; CI and repo instructions use the selected commands | local `uv run python` output; checker pass; workflow diff |
| D4 | M2 CLI decisions and installation/evidence gates are recorded; no CLI install occurs | Tools registry review; no install action |
| D5 | Active terminology and plan 3.5 readability updates are scoped; historical and pinned files are untouched | targeted search; source-manifest check |
| D6 | Current daily handoff reflects the task; no existing snapshot is overwritten | Pre-refresh today archived at `Repo/days/2026-10-05/today.md`; today/now/INTENT refreshed and links verified |
| D7 | Required local gates pass; baseline test failures and unknown Human/runtime gates stay explicit | RA checker, verifier, NP0 tests, baseline MPS comparison, final worktree |

## Landing / Rollback

Canonical authorities remain `AGENTS.md`, `Ego/RAP.md`, and Mission/EVAL. `Ego/Rwb.md` remains a Player-facing draft unless separately accepted. The RAP HTML remains a read-only Narrative Page and is stale after source changes. Rollback is a new, reviewed reverse diff; do not reset, overwrite, or rewrite history. Preserve the user-authored RWB draft and the existing `.venv`.

## Execution Result

The current conversation explicitly authorized local execution while this Motion was Draft; no durable Approved status is claimed.

- D1-D5: executed. RWB links/draft, RAP 0.6.6 Scope, Python checker/CI route, M2 CLI registry, scoped terminology, and plan 3.5 readability edits are landed locally. Historical and pinned files were preserved.
- D6: executed. The complete pre-refresh `Repo/today.md` was preserved at `Repo/days/2026-10-05/today.md`; its body matches after relative-link rebasing. `Repo/today.md`, `Repo/now.md`, and `Repo/INTENT.md` now reflect this revision. The existing `Repo/days/2026-10-04/today.md` was not overwritten.
- D7: required RA checker, repository verifier, 10 NP0 snapshot tests, RAP HTML parser, and source hashes pass. The additional MPS suite is 13/16; all three failures reproduce on clean baseline `f192d17` and are recorded in the canonical Audit. `git diff --check` passes and final worktree status is recorded in the Audit.
- D4 PDF CLI, Rule 5 hooks/secrets, LANTERN, CI Actions status, Template repository setting, and Player acceptance remain open or unverified.
