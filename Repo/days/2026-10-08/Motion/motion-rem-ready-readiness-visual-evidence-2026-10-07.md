# Motion - rem-ready Readiness Criteria and Visual Evidence

> **Date**: 2026-10-07
> **Player**: yangjun / bitguts
> **Status**: Done
> **History Triage Result**: Audit First; no Concept / EGO admission; runtime and product-EVAL unknowns remain explicit.
> **Type**: Skill revision
> **Service Object**: `rem` Repo / `.agents/skills/rem-ready/SKILL.md`
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> [eval-rem-v1](../../../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Current conversation, 2026-10-07: revise rem-ready to use the requested Copilot label `Luna Max 872K`, define readiness across Repo/GitHub alignment, RA (Rem Agent) readiness, RW (Rem work OS) readiness, and current Mission/task state and delivery requirements, specify the Copilot model-picker route, apply ASD-1000 STE style to new text, use Chinese terms when needed, and require VS Code `1.141.0` or newer; analyze and draft only, do not execute. Player confirmations, 2026-10-08: `Repo ready` requires equality between local `HEAD` and the freshly observed selected GitHub branch commit; worktree and editor-buffer state are reported separately. After the Player selects and completes an `ANDON` path, close that `ANDON`; allow tasks that do not touch or depend on known dirty paths, without requiring cleanup, commit, or push. Unknown RA runtime / Skill loading permits unrelated tasks to proceed as `READY_WITH_LIMITS`; block only tasks that depend on that loading. Player reports on 2026-10-08 that device, network, and task-required environment checks passed; record this as Player-declared evidence, not as an independent SI observation. If no current task-level Mission is bound, report Repo, RA, and RW states separately and do not mark any specific task `READY`. Mission readiness requires evidence that the current task may start; no fixed lifecycle status token is required. JSON evidence and its referenced source outputs carry the evidence; HTML is only their visual index. Player confirms `872K` denotes a context-window value; this declaration does not verify the current picker entry, provider / model ID, or runtime. Player confirms `Luna Max 872K` is the requested picker display label; record provider / model ID when observed, and block only tasks that depend on this model if identity remains unknown. Player authorization, 2026-10-08: execute the approved local scope through closeout and source retirement; source status was `Draft` at approval. Do not treat that authorization as model invocation, commit, or push permission.

## Problem

The current [rem-ready Skill](../../../../.agents/skills/rem-ready/SKILL.md) defines required inputs, inspections, Andon behavior, and validation. It does not define a final, reproducible `Ready` predicate across Repo/GitHub alignment, RA (Rem Agent) readiness, RW (Rem work OS) readiness, and current Mission / task state and delivery requirements. RA and RW are readiness domains, not additional REM components. These gates must also remain distinct from task completion, product EVAL, and actual model execution.

The Skill identifies `Luna` as a rem-maintenance workload target but does not bind a model. [RWS](../../../../Ego/Rws.md) requires role, runtime identity, access, permission, budget, and execution evidence to remain separate. A Skill declaration cannot select or prove a runtime. The requested label `Luna Max 872K` does not identify its provider or exact model ID. The Player confirms that `872K` denotes a context-window value; this is a Player-declared meaning, not independent confirmation of the current model's advertised or account-available context limit.

The current [rem-ready Narrative Page](../../../TeamsPage/rem-ready-teamspage.html) is explicitly non-authority and no-writeback. Its page source hashes are stale after the recent Skill / rules changes. [TeamsPage custody](../../../TeamsPage/README.md) distinguishes Narrative Pages from deterministic MPS artifacts; `scripts/mirror.py` is not a Narrative Page generator. A visual page can summarize evidence, but cannot itself prove runtime use, Human acceptance, or Mission EVAL.

The latest recorded rem-ready handoff lists VS Code CLI `1.140.0`. This historical CLI observation is below the requested threshold and does not verify the active VS Code client's version for a future execution.

## Proposed Decision

### VS Code Version Gate

Any future execution of this Motion must use an active VS Code client at version `1.141.0` or newer. Observe and record the client version for that execution. A CLI or historical observation alone does not prove the active client's version. If the active version is older than `1.141.0`, or cannot be observed, keep execution `Blocked`. This Draft does not authorize installing or updating VS Code to meet the gate.

### 1. Model Target

Record the request as a desired, not yet verified, target:

- Workload role: `Luna`.
- Requested Copilot picker label: `Luna Max 872K`.
- Context-window meaning of `872K`: Player-confirmed; current picker value / unit is not independently observed.
- Provider and exact model ID: record from the active picker when a task requires this model; until then, current identity is `unknown`.

Before execution of a task that requires this model, observe the exact provider and model ID in the active Copilot model picker. Record the Player-confirmed context-window meaning of `872K` separately from any value shown by the picker. In the Skill, identify this as a requested target. State that the selected and running model must be observed separately. Do not switch models or infer availability from this request. Do not fall back without approval. If the model is unavailable or its provider / ID is unknown or does not match, block only tasks that require this model; unrelated tasks may proceed as `READY_WITH_LIMITS` if their other required gates pass. Report local readiness separately.

#### Copilot Model Selection

Use the model picker in GitHub Copilot Chat. The [VS Code 1.141 release notes](https://code.visualstudio.com/updates/v1_141) say to choose a Copilot model in this picker. This Motion does not define a `settings.json` key for `Luna Max 872K`; no supported key for this label has been verified.

1. Check that the active VS Code client is version `1.141.0` or newer.
2. Open GitHub Copilot Chat. Open its model picker.
3. Look for the exact label `Luna Max 872K`. The Player selects it only if it is listed as available for the current account.
4. Confirm the provider and model ID. Record the Player-confirmed meaning of `872K` as a context-window value. If the picker shows a context limit, record that observation separately and do not infer a unit that is not displayed.
5. If the label is missing or the provider / model ID is unknown, record `unknown`. Block any task that requires this model. Do not select another model.
6. Record the VS Code and Copilot extension versions, selected label, provider / model ID, context-window value if shown, account / entitlement status without credentials, and observation time.

Model-picker selection does not prove that the model ran. Record actual runtime evidence separately.

### 2. Readiness Domains and Rem-ready Outcomes

Report each domain independently, then derive the overall outcome. A domain is ready only when its required gates have current evidence and pass:

- `Repo ready`: After a fresh, authorized remote observation, the local branch `HEAD` matches the selected GitHub branch commit. This gate tests commit equality only; it does not require a clean worktree or editor buffer. Report worktree and editor-buffer state separately as `clean`, `dirty-known`, or `unknown`. Known local changes do not change commit alignment; preserve and identify them. Unknown or task-conflicting changes block the affected work. Stale remote-tracking data or no authorized fresh observation leaves commit alignment `unknown`; do not fetch, clean, commit, or push implicitly.
- `RA ready` (Rem Agent): Root `AGENTS.md` is the sole controlling SI instruction source; `Ego/RAP.md` is active as the RA rule-definition source and its priority / boundary statements align with AGENTS; retired RCI carriers are absent; and `uv run python scripts/ra-check.py` passes for the current source. These are the RA static-integrity gates. Record active-agent / Skill runtime loading separately as `pass`, `unknown`, or `not_run`. Unknown or unrun loading does not block a task that does not depend on the affected rule or Skill; allow that task as `READY_WITH_LIMITS` and name the limit. If the task depends on that rule or Skill being loaded, block it until loading is verified. A missing source, authority conflict, or failed static check blocks affected work. This gate verifies rule integrity, not permission or acceptance.
- `RW ready` (Player's label: Rem work OS): The actual device / host and operating system, network state / connectivity, active VS Code client and relevant extensions, terminal / shell, execution environment, toolchain, and required Tools / runtime pass for the task. Use direct SI observation or a current Player / Human declaration as evidence. Record the source, scope, and observation time / timezone when supplied. A declaration is a reported pass; do not label it an independent SI observation or invent probe output. A broad declaration covers only its stated scope. If a task requires a narrower environmental fact that was not checked or declared, mark that fact `unknown` and apply task-dependency rules. For this Motion, the active VS Code version must be `1.141.0` or newer. Canonical work-system documentation remains `RWS = Rem Work System`; `RW` is a Motion-level readiness label and does not rename RWS or assert that RWS is a literal operating system. Registration or installation alone does not prove availability or execution. Current Player report (2026-10-08): device, network, and task-required environment checks passed. Exact probes and clock time were not supplied; record this as a Player-reported pass, not an independent SI measurement.
- `Mission ready`: The required rem Primary / EVAL binding and current task-level Mission are explicit; evidence from the task's source indicates that the current task may start. Preserve the source's task state and evidence; no fixed lifecycle status token is required. Role / owner, scope, inputs, dependencies, deliverables, acceptance criteria / EVAL, evidence, permissions, cost, and stop rule are clear. If no current task is bound, Mission readiness is `unknown`; report Repo, RA, and RW states separately, but do not mark any specific task `READY`. Readiness permits work; it does not mean the Mission is complete or accepted.

Derive one outcome and require the handoff to name it with its evidence:

| Outcome | Proposed predicate | Boundary |
| --- | --- | --- |
| `READY` | Repo commit alignment, RA, RW, and Mission domains all pass for the current task; worktree state is known; required local checks pass; and no `ANDON` path choice remains unresolved. | Means the specified task may begin within its approved scope. It does not mean product EVAL A1-A13, Human review, actual model execution, or task acceptance passed. Each action still needs its own authority and permission. |
| `READY_WITH_LIMITS` | Required gates across all four domains for a clearly bounded activity pass, while only task-irrelevant facts remain unknown or limited. This includes unknown RA runtime / Skill loading when the task does not depend on that rule or Skill. | List each limit and restrict work to the permitted activity. Known dirty paths may remain as limits: allow tasks that do not touch, overwrite, or depend on them. Allow tasks that do not depend on RA loading that remains unknown. Block only work that depends on an unknown or conflicting fact. Do not require cleanup, commit, or push. |
| `ANDON` | A stale date / Git / editor state or known local changes require a Player path choice, and that choice has not yet been completed. | Stop affected writes and wait for the Player's path choice. After the approved path is completed and the state is rechecked, close that `ANDON`; keep local changes as `dirty-known`. Allow tasks that do not touch, overwrite, or depend on those paths. Block only conflicting work. Do not require unrelated known local changes to be cleaned, committed, or pushed. |
| `BLOCKED` | Any required Repo, RA, RW, or Mission gate is missing or failed; a task-required fact is unknown; the local version is not aligned with GitHub; an authority conflict exists; or a task-specific model, permission, subscription, cost, or budget gate is missing. Unknown RA runtime / Skill loading blocks only a task that depends on the affected rule or Skill. | Stop the affected task. Do not silently downgrade its requirements or fall back. |

The Skill should enumerate mandatory gates in all four domains, classify dirty-but-known work and unresolved `ANDON` separately, and keep `unknown`, `not_run`, `pass`, and `fail` distinct. Report commit alignment, worktree state, RA static integrity, RA runtime / Skill loading, per-domain results, and aggregate outcome separately; distinguish readiness for the current task from completion / acceptance. Unknown RA runtime / Skill loading permits `READY_WITH_LIMITS` only when the current task does not depend on it. Passing `verify.py` or `ra-check.py` alone does not prove GitHub freshness, RA runtime / Skill loading, RW readiness, or product acceptance.

### 3. Visual Readiness Receipt

After a completed readiness assessment and any required `ANDON` path has been selected, completed, and rechecked, produce both an evidence record and a dated visual Narrative Page for `READY`, `READY_WITH_LIMITS`, and `BLOCKED`, when the local evidence write is permitted. Do not create either artifact while an unresolved `ANDON` prohibits writes. A `BLOCKED` receipt must state the blocking conditions clearly and must not look like a successful readiness result.

- Evidence record: `Mission/evidence/rem-ready-<YYYYMMDDTHHMMSS>.json`, containing observed time / timezone, local and GitHub revisions with remote-observation freshness, worktree / editor state, unresolved or resolved `ANDON` path, AGENTS / RAP source revisions, `ra-check.py` command and result, RA runtime / Skill loading evidence or `unknown` / `not_run`, whether the task depends on that loading, RW evidence source and scope (direct observation or Player / Human declaration), per-domain gate results, current Mission / task binding, actual commands and results, outcome, unknowns, and next action.
- Visual receipt: `Repo/TeamsPage/rem-ready-run-<YYYYMMDDTHHMMSS>.html`, linked to the JSON evidence record and the exact source files. It is a visual index only; it is not independent evidence.
- Keep `Repo/TeamsPage/rem-ready-teamspage.html` as the explanatory Skill Narrative Page; update it when the Skill contract changes, not as a per-run evidence substitute.

The visual receipt must display the aggregate outcome, Repo commit alignment, worktree / editor state, separate RA static-integrity and runtime-loading states, RW / Mission results, and each gate as `pass`, `fail`, `unknown`, or `not_run`; include source revision / hashes, remote-observation freshness, AGENTS / RAP revisions and `ra-check.py` result, whether the current task depends on unverified RA loading, RW evidence source and scope, Mission / task binding, generator and version, and observed date / timezone. For `BLOCKED`, identify each blocker and the affected task or action. It must be offline-readable, contain no external scripts or fonts, and be non-authority / no-writeback. Do not overwrite prior run receipts. Do not use `scripts/mirror.py` or label the receipt as MPS.

The JSON evidence record and its referenced observations / command outputs carry the proof for each gate. The HTML page only indexes and visualizes that evidence; its rendering or a screenshot is not independent proof. The page cannot claim Human acceptance, actual model execution, or EVAL completion without their separate evidence. During an Andon that prohibits writes, do not create either receipt until the Player chooses a path; report the Andon without generating a success-looking page.

## Scope

If approved, revise only the rem-ready contract and its direct visual consumers:

- `.agents/skills/rem-ready/SKILL.md`
- `Repo/TeamsPage/rem-ready-teamspage.html`
- `Repo/TeamsPage/README.md`, only as needed to describe dated receipt custody
- A narrowly scoped, non-overwriting per-run evidence / visual receipt path as specified above
- When needed to establish Repo commit alignment, one explicitly approved `git fetch` of the selected remote branch for comparison only; record the action without merging or changing worktree files.

Execution is local and documentation / artifact scoped. Before execution, verify that the active VS Code client is version `1.141.0` or newer and use the Player-approved JSON + HTML receipt policy. `872K` is Player-confirmed as a context-window value. Observe the provider / model ID only when a task depends on the requested model; an unknown ID blocks that dependent task, not this documentation-only Motion. Record actual evidence and preserve unknowns. This Motion does not authorize installing or updating VS Code.

## Out of Scope

- Selecting, switching, invoking, or claiming availability of `Luna Max 872K` or any model; no paid or external model call.
- Changes to `AGENTS.md`, RAP, RWS, product EVAL A1-A13, other Skills, `scripts/mirror.py`, MPS contracts, or cross-Repo rules.
- Any unapproved fetch; merge / pull, commit, push, deployment, credential access, or permission expansion.
- Treating an HTML page, screenshot, static test, or self-review as Human acceptance or runtime proof.

## Execution Plan

This Motion was `Draft` when the Player explicitly authorized execution on 2026-10-08; that approval does not backdate or imply durable `Approved` status. The source entered `Executing` during this run and is now closed as `Done`; the Audit records both transitions. The approval covers only the current `rem` Repo scope through required closeout and retirement. The active VS Code application process and bundle must meet `1.141.0` or newer; if not observable or older, stop as `Blocked` without installing or updating VS Code. If commit freshness is required, use only the explicitly approved comparison fetch; record the result and do not merge, pull, or alter worktree files.

Then:

1. Update the rem-ready Skill with the confirmed target semantics, status predicates, mandatory checks, stop rules, and visual-receipt workflow.
2. Update the explanatory Narrative Page and custody note; retain existing artifacts and create dated receipts without overwriting them.
3. Exercise bounded cases for `READY`, `READY_WITH_LIMITS`, `ANDON` before and after a selected path, and `BLOCKED`; verify JSON and visual receipts are produced for each final outcome when writing is permitted, while neither receipt is produced during an unresolved write-prohibiting `ANDON`. Also cover stale / unknown GitHub revision, known dirty worktree with aligned commits and a non-conflicting task, a task that touches or depends on a dirty path, RA runtime / Skill loading unknown with an unrelated task and with a dependent task, RW direct observation and Player-declared pass with source provenance, a task fact outside a declaration's scope, unavailable or unknown RW device / network / VS Code / environment, missing or unapproved Mission / delivery requirements, missing or conflicting RA instruction sources, retired RCI carrier presence, failed or unrun `ra-check.py`, mismatched runtime, failed validation, and denied refresh. Label synthetic cases as synthetic; do not use them as proof of actual sync, runtime rule loading, or model execution.
4. Run `uv run python scripts/ra-check.py`, `uv run python scripts/verify.py`, Markdown / HTML diagnostics, and direct receipt-link / provenance checks. Record actual output and limitations.
5. Record the Player's explicit closeout and retirement direction. It applies to this bounded Motion only; do not change product EVAL or claim its gates passed.

## Motion EVAL

| Gate | Acceptance condition |
| --- | --- |
| D0 - RW / VS Code version | Before any Motion execution, record the active VS Code client version and verify it is `1.141.0` or newer; an older or `unknown` version keeps execution `Blocked`. No VS Code install / update is implied. |
| D1 - Model binding | `Luna Max 872K` is the Player-confirmed requested picker label, not a model ID. Record the provider / model ID when observed; if unknown, block only tasks that require this model and allow unrelated tasks as `READY_WITH_LIMITS` when their gates pass. Record `872K` as a Player-confirmed context-window meaning, separately from current picker evidence. The Skill never claims runtime selection or switches / falls back. |
| D2 - Readiness predicate | Repo commit alignment, worktree / editor state, unresolved `ANDON`, RA static integrity, task-dependent RA runtime / Skill loading, RW, and Mission each have explicit gates and evidence; Player / Human declarations can support RW pass with source provenance and are not mislabeled as SI observations; unknown RA loading allows unrelated tasks as `READY_WITH_LIMITS` and blocks dependent tasks; aggregate outcomes and next steps are explicit and readiness remains distinct from task completion and product EVAL. |
| D3 - Visual receipt | JSON evidence and a dated visual index are produced for `READY`, `READY_WITH_LIMITS`, and `BLOCKED` after any required `ANDON` path is resolved and writing is permitted. JSON and referenced source outputs carry the evidence; HTML is only an index. Both link the source evidence and state provenance and freshness. A `BLOCKED` receipt identifies blockers and cannot look successful; no receipt is written during an unresolved write-prohibiting `ANDON`. |
| D4 - Consumer alignment | The explanatory rem-ready Narrative Page and TeamsPage custody notes agree with the Skill; no MPS / `mirror.py` route is introduced. |
| D5 - Validation | Required repository checks and direct artifact checks pass; behavior cases cover Repo sync, RA static integrity and task-dependent runtime loading, RW evidence-source handling and environment, and Mission / delivery blockers; synthetic coverage is disclosed and unobserved runtime / Human gates remain `not_run`. |
| D6 - Player acceptance | Player accepts the Motion closeout; this does not promote product EVAL or model / role gates. |

## Landing, Consumer Audit, and History

Canonical source is `.agents/skills/rem-ready/SKILL.md`. Direct consumers are `Repo/TeamsPage/rem-ready-teamspage.html` and, if changed, `Repo/TeamsPage/README.md`. Per-run evidence belongs in `Mission/evidence/`; visual receipts belong in `Repo/TeamsPage/`. Audit the Skill, explanatory page, generated receipt, verifier, and existing Andon / authority routes against one another. Keep this Motion in `Repo/Motion/` while Draft or executing; only retire it after accepted closeout and History Triage under `motioner`.

## Permission, Cost, and Stop Rule

Player's 2026-10-08 instruction authorizes execution of the local Motion scope through required closeout and retirement. It does not authorize model selection or invocation, other network actions, merge / pull, commit, or push. The approved comparison fetch does not authorize integration. No model / subscription cost is approved. If the active VS Code client is older than `1.141.0` or unknown, block execution. If the provider / model ID, source, runtime, permission, or budget is unknown, block only actions that depend on that fact; this Motion's documentation changes do not invoke the requested model. Do not infer, silently substitute, or install / update VS Code.

## Closeout and History Triage

The Player's 2026-10-08 instruction explicitly authorizes this Motion through completion and source retirement. The source was `Draft` at approval and was not backdated to `Approved`.

The canonical Audit records the implementation, readiness evidence, checks, synthetic decision-case review, and limitations. `D0`–`D6` are closed for this bounded Motion. Provider/model ID remains `unknown`; no model was selected or invoked. Product EVAL A1-A13, Human role alignment, and actual runtime gates remain unchanged.

History Triage is `Audit First`; no Concept or EGO admission is made. Retire the complete source to `Repo/days/2026-10-08/Motion/` after landing the canonical Audit. Do not commit or push.

## Rollback

After a future approved execution, rollback only the specifically approved Skill / explanatory-page diff if validation fails; preserve pre-existing and unique evidence. Do not delete dated run receipts as cleanup. Any source / receipt mismatch marks the page stale and routes review back to its sources.
