# Audit - RWS Work-System Migration

> **Date**: 2026-10-06
> **Player**: yangjun / bitguts
> **Status**: Done
> **Scope**: Consolidate RWB, Tools, and Working responsibilities under the approved rem Work System source; keep RAP independent
> **Source Motion**: [motion-work-os-concept](../../Repo/days/2026-10-06/Motion/motion-work-os-concept-2026-10-06.md)
> **Primary Route**: [Story-rem](../Story-rem.md) -> [EVAL](../EVAL/eval-rem-v1.md)
> **Runtime Approval**: Player 当前对话：“批准Motion, 开始执行, 一步一步的”
> **Player Acceptance**: Current conversation: “接受并授权退休”
> **Source Status at Approval**: Draft; execution approval recorded here, not backdated to Approved
> **Source Retirement**: `Ego/Tools.md` and `Ego/Working.md` removed; original texts are in the [Tools archive](../../Repo/days/2026-10-06/Ego/Tools.md) and [Working archive](../../Repo/days/2026-10-06/Ego/Working.md), with source blob provenance. `Ego/Rwb.md` remains a non-authority notice. Motion source `Repo/Motion/motion-work-os-concept-2026-10-06.md` -> `Repo/days/2026-10-06/Motion/motion-work-os-concept-2026-10-06.md`
> **History Triage Result**: Audit First; bounded RWS canonical-source acceptance; no product EVAL or runtime admission
> **Baseline**: `af5fd54302e389709ca88f5e8f38d6437e0689f6`; Windows workspace `D:\Github\rem`

## Decision and Target

The current Player instruction is treated as approval to execute the bounded architecture proposal in the Motion. The selected working token is `RWS = rem Work System`, scoped only to the rem repository; it is not a general industry standard, a Microsoft Copilot product name, or a fourth REM component.

Target architecture: `Ego/Rws.md` becomes the canonical Work-System source integrating the still-valid RWB workbench baseline, Tools capability/permission/evidence rules, and Working task loop. `Ego/RAP.md` remains the independent RA rules source; root `AGENTS.md` remains the SI execution instruction. “RWS and RAP are the two related files” means the two relevant Work-System/RA-rules sources, not the only files under `Ego/`.

## Baseline and Start

Before execution, RWB, Tools, and Working were separate sources. Existing consumers reference them directly: `AGENTS.md` reads Working as part of the EGO quartet; `scripts/verify.py` requires RWB and Working; NP0 `runtime_snapshot.py` selects Working as the quartet input; Ego navigation, TeamSkill registry, README, fixtures, and tests also contain references.

The approved sequence is stepwise. First create and review the consolidated RWS source while keeping legacy files intact. Then migrate Naming/navigation and each consumer, updating fixtures/tests/source pins where required. Retire `Rwb.md`, `Tools.md`, and `Working.md` only after reference searches and relevant checks pass. Do not delete them early.

Before this Audit was created, rem-ready refreshed `Repo/today.md` and `Repo/now.md` after preserving the full pre-refresh snapshot at `Repo/days/2026-10-05/today-post-revision.md`; the pre-existing `Repo/days/2026-10-05/today.md` was preserved. `uv run --offline python scripts/verify.py` returned `structure=pass`, `failures=[]`. At execution start, no EGO implementation changes had been made.

## Scope and Held Boundaries

Authorized local scope: create `Ego/Rws.md`; register `RWS` in `Ego/Naming.md`; update EGO navigation and repository consumers for the RWS canonical source; migrate NP0 snapshot adapters/tests, verifier, and source-manifest target-delta hashes only where required; remove superseded EGO source files only after all consumers and checks are updated; update relevant current handoff/Audit records.

Out of scope: changing RAP's RA rules, altering Mission/EVAL criteria, changing model/provider configuration or permissions, claiming subscription/runtime availability, accepting the RWB draft as a separate artifact, paid or external actions, installing CLIs, deployment, commit, or push. Player acceptance is limited to the canonical RWS source and this source retirement; product EVAL A1-A13, runtime models, and role alignment are not inferred complete.

## Validation Plan

Run the narrowest relevant checks after each migration step. Required final checks include `uv run python scripts/ra-check.py` if Agent configuration/CI is touched, `uv run python scripts/verify.py`, NP0 runtime snapshot tests if the quartet adapter changes, relevant MPS/source-pin checks if manifest-bound consumers change, and `git diff --check`. Record actual results here; unrun Human/runtime gates remain `not_run` / `unknown`.

## History Triage

History Triage is `Audit First`. Player acceptance and the source-retirement decision are recorded explicitly below; neither tests nor implementation are treated as that decision. No broader product EVAL, runtime admission, permission change, commit, or push is authorized or inferred.

## Execution Log

- 2026-10-06: Player approved “批准Motion, 开始执行, 一步一步的”. The approval is recorded as runtime approval for this Motion, whose source was Draft at execution start. Stable token selected for this execution is `RWS = rem Work System`; RWS/RWB acronym similarity is an accepted naming tradeoff for this scope.
- 2026-10-06: Motion status is `Executing`; its initial Draft-only scope has been amended to the approved local migration. Created `Ego/Rws.md` as the canonical Work-System integration; legacy RWB/Tools/Working files remain intact.
- 2026-10-06: Registered RWS in Naming; redirected Ego-rem, AGENTS, RAP's work-system pointer, README, TeamSkill registry, and teamsbook review-source navigation. RAP's RA rules remain unchanged.
- 2026-10-06: Updated `scripts/verify.py`, `scripts/mirror.py`, NP0 runtime snapshot adapter/tests to use Rws. Refreshed the two NP0 target-delta hashes in `Ego/TeamSkill/source-manifest.json`.
- Validation: `uv run --offline python scripts/ra-check.py`: `RA仓规 0.6.6: OK`; `uv run --offline python scripts/verify.py`: `structure=pass`, `failures=[]`; `uv run --offline python .agents/skills/np0/scripts/test_runtime_snapshot.py`: 10/10 pass.
- MPS suite: `uv run --offline python -m unittest discover -s scripts -p 'test_mirror.py'`: 16/16 pass after the approved fixture update. The test copy still excludes HTML by default and now explicitly includes only the two Markdown-referenced Narrative Pages, `rap-teamspage.html` and `rem-ready-teamspage.html`; generated MPS HTML remains excluded. No renderer, pinned asset, or HTML artifact changed.
- 2026-10-06 reference triage: no active code or primary-navigation consumer remains. Tools / Working historical Markdown links target the dated source archives. The pre-existing RAP Narrative Page was not regenerated; only its obsolete Tools href was redirected to the archive. Its recorded source hashes remain stale.
- 2026-10-06 source-content comparison: reviewed the full legacy RWB, Tools, and Working texts against `Ego/Rws.md`. The selected shell / OS / Node targets, on-demand CLI install/remove rule, Working-loop and Sol/Luna distinction are represented in RWS. Restored the omitted version-target detail. The legacy CLI acquisition priority was explicitly an SI proposal pending Player confirmation; it is preserved as a non-adopted proposal, not policy. No other known operative source content remains unrepresented.
- The pre-existing RAP Narrative Page remains stale after source changes and was not regenerated or edited; it is not added to the active source group by this Motion.
- 2026-10-06: Player reviewed and accepted `Ego/Rws.md` as the canonical Work-System source and authorized source retirement. The Tools and Working bodies were archived under `Repo/days/2026-10-06/Ego/` with their source commit/blob IDs; `Ego/Tools.md` and `Ego/Working.md` were physically removed. The RWB path remains a non-authority notice. Historical Markdown links were retargeted to the archives; the stale RAP Narrative Page was not regenerated, and its obsolete Tools href alone was redirected while its source hashes remain stale.
- Final validation: `uv run --offline python scripts/verify.py`: `structure=pass`, `failures=[]` after physical path removal; `uv run --offline python .agents/skills/np0/scripts/test_runtime_snapshot.py`: 10/10 pass; `uv run --offline python -m unittest discover -s scripts -p 'test_mirror.py'`: 16/16 pass after explicitly including the two Markdown-referenced Narrative Pages in the fixture. `uv run --offline python scripts/ra-check.py`: `RA仓规 0.6.6: OK`.
- Closeout: Motion is `Done` and its source is retired to `Repo/days/2026-10-06/Motion/` under Motioner custody. Product EVAL A1-A13, runtime models, and role alignment remain unchanged / `not_run`. No commit or push occurred.
