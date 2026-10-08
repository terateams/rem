---
name: rem-ready
description: "用于 rem 冷启动、开工/暂停、日期/Git/工作面核验、日交接与安全收口；AGENTS.md 是唯一控制性 SI 指令，Ego/RAP.md 定义 RA 规则且不得覆盖 AGENTS，RCI 已退役。不用于具体正文、自动同步或替代 Player 批准与 Human acceptance。"
metadata:
  status: in-production
  source_commit: 70090b756d2c4f4e75912ec9f3ede2ff3e8cc0a0
---

# rem ready

## Authority

`AGENTS.md` is the repository's only controlling SI instruction file and governs execution priority. `Ego/RAP.md` defines RA rule semantics and human-facing rationale; it must remain aligned with AGENTS and does not override it. This Skill supplies the rem-ready operating route; it does not create another instruction source or grant permission. RCI is retired in this Repo: `.github/copilot-instructions.md` and `.github/instructions/` must not exist. Preserve historical RCI references as provenance. Before changing Agent configuration, read RAP; after the change, run `uv run python scripts/ra-check.py`.

## Inspect-first

Read `Repo/today.md`, `Repo/now.md`, `Repo/INTENT.md`, and the EGO quartet. Bind exactly one Primary, its EVAL, Secondary=0, `selected_method=null`, and relative dates to the current host date/timezone. Verify `git status`, ahead/behind against existing local refs, editor-buffer dirty state, `Repo/Dojo` path status, and the previous-day archive. Do not fetch by default; without a fetch, remote freshness is unknown.

Verify terminal cwd against the workspace independently. Check VSC/Profile/Settings Sync/extensions, actual device, and necessary runtime as separately observable facts; unknown stays explicit. On-site facts may be directly observed, declared by the Player/Human, or explicitly marked as carried forward. Do not create a T189 inventory.

For a task-level check, bind the current task and its Mission/EVAL. If no task is bound, report Repo, RA, and RW states separately. Do not mark a specific task `READY`.

For an explicitly named cross-Repo rules task, bind only the stated target and active VSC workspace. Confirm the target path and whether the host Skill is actually available; same-device access or filesystem readability does not prove VSC discovery, activation, or write permission. Do not enumerate sibling repositories.

Keep subscription/picker observations or Player/Human declarations separate from actual model-run evidence. Sol and Luna are different workload goals; do not switch models or infer either workload from a picker, installed extension, or active chat.

## Readiness Decision

Assess each domain for the current task. Record `pass`, `fail`, `unknown`, or `not_run`, with evidence source and time. Do not infer `pass` from missing evidence.

- `Repo`: `commit_alignment=pass` only when local `HEAD` equals the freshly observed selected GitHub branch commit. Record both commits and branch. Report worktree and editor-buffer state separately as `clean`, `dirty-known`, or `unknown`. Known local changes do not change commit alignment. Preserve and identify them. Unknown or conflicting paths block only affected work.
- `RA`: Static gates are the sole controlling root `AGENTS.md`, aligned `Ego/RAP.md`, no active RCI carriers, and passing `uv run python scripts/ra-check.py`. Report active-agent and Skill runtime loading separately. Unknown or unrun loading permits unrelated work as `READY_WITH_LIMITS`; block tasks that depend on that rule or Skill. Missing or conflicting rule sources or a failed static check block affected work.
- `RW`: Check the task-relevant device and operating system, network, active VSC and extensions, terminal, environment, tools, and runtime. Evidence may be direct SI observation or a current Player/Human declaration. Record source, scope, and time when supplied. A declaration is a reported pass, not an independent SI measurement. Do not invent probe output. An unknown fact blocks only tasks that depend on it.
- `Mission`: Require evidence from the current task source that the task may start. Keep the source's status label; no fixed lifecycle token is required. Record owner, scope, inputs, dependencies, deliverables, acceptance criteria/EVAL, evidence, permission, cost, and stop rule. Readiness does not mean completion or acceptance.

Use these overall results:

| Result | Rule |
| --- | --- |
| `READY` | All gates required by the bound task pass; worktree/editor state is known; no `ANDON` path is unresolved. |
| `READY_WITH_LIMITS` | Required task gates pass. List facts that remain unknown but do not affect this task. Known dirty paths and unknown RA loading may remain if the task does not touch, overwrite, or depend on them. |
| `ANDON` | A stale date with dirty, behind, or unknown Git/editor state requires a Player path choice, and that path is not complete and rechecked. Pause affected writes. |
| `BLOCKED` | A required gate fails or is unknown; an authority conflict exists; or a task-specific permission, subscription, budget, or model requirement is missing. Block only the affected task/action. |

After the Player selects and completes an `ANDON` path, recheck the state and close that `ANDON`. Keep unrelated known changes as `dirty-known`; do not require cleanup, commit, or push. Allow non-conflicting work. If no task-level Mission is bound, report Repo/RA/RW only and do not assign a task-level `READY`.

### Copilot Model Target

The Player-requested picker label is `Luna Max 872K`. The Player states that `872K` is a context-window value; this declaration does not verify the current picker value, unit, provider, or model ID. Use the Copilot Chat model picker. Do not invent a `settings.json` key. For this model-picker route, require VS Code `1.141.0` or newer. When a task needs this model, record the displayed label and the provider/model ID if available. If identity is unknown or the model is unavailable, block only that model-dependent task. Do not switch models or fall back. A picker selection does not prove a model run.

## Andon and Refresh

If the date baseline is stale and Git/editor state is dirty, behind, or unknown, raise `ANDON` and wait for the Player's path choice. Do not stash, reset, pull, overwrite, or silently refresh. After explicit refresh approval, preserve the complete pre-refresh `Repo/today.md` at `Repo/days/YYYY-MM-DD/today.md` using the previous-day date; then replace `today.md`, followed by `now.md`. Do not rewrite `INTENT` as routine daily maintenance.

Do not fetch by default. For Repo commit alignment, fetch the selected remote branch only after explicit Player approval. Compare `HEAD` with the fetched ref. Record the fetch and comparison. Do not merge, pull, commit, push, or clean the worktree as part of this check.

## Validation and Handoff

Read the actual output of `uv run python scripts/verify.py`; report `not_run` / `unknown` where checks were not performed. Call `scripts/mirror.py` only for an explicitly scoped and authorized deterministic MPS artifact; Narrative Pages are not MPS artifacts. A valid local startup entry does not mean all EVAL A1-A13 gates passed.

Report Repo, RA, RW, Mission, and overall status. Preserve each unknown and `not_run` state. Do not call an unrelated task blocked because a non-required fact is unknown.

After a completed readiness assessment, create a unique JSON evidence record and an HTML visual receipt for `READY`, `READY_WITH_LIMITS`, or `BLOCKED`, if local evidence writing is permitted. If an `ANDON` still prohibits writes, create neither until the Player selects and completes a path. Use `Mission/evidence/rem-ready-<YYYYMMDDTHHMMSS>.json` and `Repo/TeamsPage/rem-ready-run-<YYYYMMDDTHHMMSS>.html`. Do not overwrite prior receipts.

The JSON record must include observed date/time/timezone, source revisions and hashes, local and fetched remote commits and freshness, worktree/editor state, the selected or unresolved `ANDON` path, RA source/check result and runtime-loading state, RW evidence source/scope, task and Mission binding, gate results, commands and outcomes, unknowns, and next action.

The JSON record and its referenced observations/command outputs carry the evidence. The HTML is only a visual index. It must link the JSON and exact source files. Show the aggregate outcome, each Repo/RA/RW/Mission gate as `pass`, `fail`, `unknown`, or `not_run`, source hashes and freshness, generator/version, and observed date/time/timezone. Identify each blocker for `BLOCKED`; do not style it as success. Keep the explanatory page separate. Make receipts offline-readable with no external scripts or fonts. Do not use `scripts/mirror.py` to generate Narrative Pages.

`REM仓规` activates the Agent-rule workflow, not this startup Skill's write authority. Route a named rules Motion to `motioner`; `shaping` supplies the evidence-backed bet / revision candidate, and `rem-make` implements only its Player-approved path scope. If an RCI carrier reappears in this Repo, report an authority conflict and block dependent writes until Player resolution.

An optional rem-ready Narrative Page is a read-only projection. It is non-authority / no-writeback, does not replace this skill, `AGENTS.md`, or RAP, and does not prove readiness. Scope its sources explicitly; mark it stale when a source changes. Away work is limited to date, Git, Dojo, and cursor risks, with a clear return entry. External, destructive, paid, release, commit/push, permission expansion, and configuration changes require the applicable Player approval. Never claim synced or ready without evidence.
