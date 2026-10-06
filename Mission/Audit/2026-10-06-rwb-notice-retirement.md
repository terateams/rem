# Audit - RWB Notice Retirement

> **Date**: 2026-10-06
> **Player**: yangjun / bitguts
> **Status**: Executed; Player acceptance pending
> **Scope**: Remove the active RWB compatibility notice path and preserve dated provenance
> **Source Motion**: [motion-retire-rwb-notice](../../Repo/Motion/motion-retire-rwb-notice-2026-10-06.md)
> **Primary Route**: [Story-rem](../Story-rem.md) -> [EVAL](../EVAL/eval-rem-v1.md)
> **Runtime Approval**: Player 当前对话：“退休RWB.md”
> **Source Status at Execution Start**: Draft; direct local execution request recorded, not backdated to Approved
> **Baseline**: `04c09fb8149de02a483d1bdb166de532f5b45d51`

## Decision and Action

The accepted RWS migration already consolidated RWB's valid workbench content into `Ego/Rws.md`; `Ego/Rwb.md` only remained as a non-authority compatibility notice. The current Player request authorized retirement of that active path.

The notice was preserved as a dated archive at [Repo/days/2026-10-06/Ego/Rwb.md](../../Repo/days/2026-10-06/Ego/Rwb.md), and active `Ego/Rwb.md` was removed. The canonical [RWS source](../../Ego/Rws.md) points to the archive and records the retired path. The archived RWS Motion's old local link was retargeted to the dated archive without changing its historical narrative. The RAP Narrative Page's local links were redirected to `Ego/Rws.md`; the page remains stale, and its historical source hashes were not regenerated or represented as fresh. Current `today`, `now`, and `INTENT` were updated. The RWB row in Naming, completed RWS Audit, prior RWB plan/Audit, and other historical records were preserved.

No product authority, EVAL criterion, runtime permission, or Human acceptance was inferred. No external, paid, model, deployment, commit, or push action occurred.

## Validation

- `uv run python scripts/verify.py`: `structure=pass`, `failures=[]`; `human_review`, `runtime_models`, and `role_alignment` remain `not_run`.
- The stale RAP Narrative Page HTML parser checked 51 links; all relative targets resolve, key document tags are balanced, and no scripts are present. The page's provenance hashes remain stale by design and it was not regenerated.
- Final `git diff --check` and worktree status: pending closeout.

## Consumer Audit and History Triage

Active Work-System consumers use `Ego/Rws.md`; the old RWB notice exists only in dated custody. Historical statements in completed Audits/Motions are retained as records of their time. History Triage is `Audit First`; no Concept or authority admission is inferred. The Motion remains active pending Player review/acceptance; no source retirement of the Motion itself occurred.
