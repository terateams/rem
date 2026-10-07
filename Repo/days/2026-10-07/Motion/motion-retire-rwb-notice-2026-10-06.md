# Motion: Retire RWB Compatibility Notice

> **Date**: 2026-10-06
> **Player**: yangjun / bitguts
> **Status**: Done
> **Type**: source retirement / path custody
> **Service Object**: former RWB notice path
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> [EVAL](../../../../Mission/EVAL/eval-rem-v1.md)
> **Execution Audit**: [canonical Audit](../../../../Mission/Audit/2026-10-06-rwb-notice-retirement.md)
> **Source Request**: Player 当前对话：“退休RWB.md”
> **Baseline**: `04c09fb8149de02a483d1bdb166de532f5b45d51`
> **Execution Closeout**: Player 当前对话：“motion下, 它没有被删除”；按此前“执行退休”请求，完成 Motion source 的日期归档。
> **Source Retirement**: `Repo/Motion/motion-retire-rwb-notice-2026-10-06.md` -> this dated archive
> **History Triage Result**: Audit First; no Concept / EGO admission; source retired after Player-directed closeout
> **Round**: R1

## 问题与拟议裁决

The accepted RWS migration consolidated RWB's valid workbench content into `Ego/Rws.md`. `Ego/Rwb.md` is no longer a baseline or independent Work-System source; it is only a retired-path notice. The Player requested retirement of that remaining active notice path.

Proposed action: preserve the notice in the existing dated EGO archive at `Repo/days/2026-10-06/Ego/Rwb.md`, remove `Ego/Rwb.md`, and update current canonical RWS / handoff references and the stale RAP Narrative Page's local RWB links to point to RWS. Preserve historical Motion/Audit statements and the RWB historical Naming token.

## 范围

**当前请求授权的本地范围：**

- Archive the current non-authority RWB notice under `Repo/days/2026-10-06/Ego/Rwb.md` with archive-relative links and explicit historical status.
- Remove the active `Ego/Rwb.md` path.
- Update active RWS and `Repo/today.md` / `Repo/now.md` handoff text to record the notice retirement; update `Repo/INTENT.md` only if its current wording names the notice path.
- Repair local RWB source links in `Repo/TeamsPage/rap-teamspage.html` to target `Ego/Rws.md`. Do not regenerate this already-stale page or claim its source hashes fresh.
- Record execution in a new canonical Audit and update this Motion; run `uv run python scripts/verify.py` and `git diff --check`.

**不纳入：**

- Changing `RWS` as canonical source, removing the historical RWB Naming token, or rewriting completed RWS/previous Motion audits and dated history.
- Rewriting the stale RAP Narrative Page, refreshing its source hashes/build, or changing other page content beyond the retired RWB local references.
- Product EVAL, runtime/model work, external/paid actions, commit, or push.

## Runtime Permission

The Player's current request explicitly authorized the bounded local retirement described above. The Motion remained Draft during execution; the Audit did not relabel it Approved or Done solely from the initial execution request. No commit/push permission was included.

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | Active `Ego/Rwb.md` is removed; its retired notice is preserved in dated custody | final path listing and archive content |
| D2 | Active RWS and handoff point to the canonical source; no active Markdown/code reference requires `Ego/Rwb.md` | targeted reference search; `uv run python scripts/verify.py` pass |
| D3 | Historical records and RWB Naming entry are preserved; stale RAP page is not represented as regenerated | targeted diff / audit boundary |
| D4 | Local retirement is recorded without inferring product acceptance | canonical Audit; Human/EVAL gates remain separate |

## Landing / Rollback

`Ego/Rws.md` remains the canonical Work-System source. The dated notice is historical/non-authority only. If Player requests restoration, create a new reviewed Motion; do not silently recreate `Ego/Rwb.md` or overwrite later sources.

## Execution Result

The original Player request authorized the bounded local retirement while this Motion was Draft; it was not represented as durable Approved status.

- D1: `Ego/Rwb.md` was removed. Its retired non-authority notice is preserved at `Repo/days/2026-10-06/Ego/Rwb.md` with archive-relative links.
- D2: canonical RWS and current handoff point to the archive / RWS; verifier returned `structure=pass`, `failures=[]`.
- D3: RWB Naming token and historical Audits/Motions were preserved. The stale RAP Narrative Page's local RWB links target RWS; its old source hashes were not refreshed and the page was not regenerated.
- D4: execution was recorded in the canonical Audit. Product EVAL and runtime gates remained separate.

No commit or push was performed.

## Closeout - 2026-10-07

Player noted “motion下, 它没有被删除” after the earlier request to execute retirement. This closeout treats that correction as the Player's instruction to retire the completed Motion source from the active `Repo/Motion/` surface. The source is preserved at `Repo/days/2026-10-07/Motion/motion-retire-rwb-notice-2026-10-06.md`; no history or evidence was deleted.

Motion status is `Done`; the canonical Audit records the D1-D4 results and current source custody. No product EVAL, runtime, or other Repo acceptance is inferred. No commit or push was performed.
