# rem RWS (Rem Work System)

> **Player**: yangjun / bitguts
> **Status**: active
> **Version**: 1.0.0
> **Freshness**: 2026-10-06
> **Primary**: [Story-rem](../Mission/Story-rem.md)
> **EVAL**: [eval-rem-v1](../Mission/EVAL/eval-rem-v1.md)
> **RA rules**: [RAP](RAP.md)
> **SI instructions**: [AGENTS.md](../AGENTS.md)
> **Player Acceptance**: Current conversation; recorded in [RWS migration Audit](../Mission/Audit/2026-10-06-rws-work-system-migration.md)

## Purpose and Boundary

`RWS = rem Work System`. RWS names rem's internal work system for Player-led professional and business work. It integrates three dimensions: the workbench substrate, authorized Tools, and the Working loop. `RWS` is a rem-scoped token, not a general industry standard.

RWS supports work organized through REM; it is not a fourth REM component and does not replace `Repo × EGO × Mission`, Mission / EVAL, or Human decision rights. RWS is not a literal operating system, a claim that the Repo thinks, or a Microsoft Copilot product. Any “work OS” wording is explanatory analogy only.

Player accepted this file as rem's canonical Work-System source on 2026-10-06. The former Tools and Working source bodies are retained as historical archives at [Tools](../Repo/days/2026-10-06/Ego/Tools.md) and [Working](../Repo/days/2026-10-06/Ego/Working.md); their active `Ego/` paths have been removed. The former RWB notice is archived at [RWB notice](../Repo/days/2026-10-06/Ego/Rwb.md); the active `Ego/Rwb.md` path is retired.

## Work Object and Participants

- **Repo** is the governed work context: source material, decisions, task artifacts, and evidence are addressable and reviewable here. The Repo is an externalized work context; it does not reason and is not the Player's mind, model weights, or complete organizational memory.
- **Player** sets business objectives, tasks, responsibility, permission boundaries, and acceptance criteria; the Player reviews and accepts or rejects results.
- **SI** means the assistant actor used through the Player's in-scope VS Code conversation / agent surfaces. Current scope examples declared by the Player include GitHub Copilot Chat (including the Copilot Enterprise use context), Codex, and Claude Code. A surface name does not identify the provider or underlying model, prove entitlement, or prove that a runtime was used.
- The default division is Player-directed and SI-executed: SI performs authorized programming and automation work, including scripts, Python, and HTML/CSS artifacts; Player evaluates the result. Programming is a capability carried by the work system, not a separate RWS dimension or a requirement that the Player personally act as a programmer.

## SI Task Binding and Operational Ontology

Bind SI facts per task and observation time. Keep the host interface, agent role, runtime, access, permission, budget, and execution evidence distinct.

| Area | Record for a task | Boundary |
| --- | --- | --- |
| Host surface | VS Code window, client / extension name, observable version | The UI entry point does not prove provider, model, entitlement, or runtime use. |
| Agent / role | SI responsibility and task scope | Role is not model identity or authority. |
| Runtime instance | Provider, model / version, runtime ID when observable | Unexposed identity is `unknown`; do not infer from picker labels. |
| Access / entitlement | Access subject, subscription / entitlement status and scope | Do not read or record credentials or tenant secrets. |
| Capability / permission | Allowed task, Tools, and action scope | Capabilities do not grant permission; use the bound Mission and Player decision. |
| Budget / usage | Cost ceiling and basis; quota / usage / remaining when observable | Unknown budget is not zero cost or permission to proceed. |
| Availability / execution | Time-bound state: configured, installed, selectable, selected, in-session, running, completed, failed, unavailable | Installed, visible, selected, in-session, and actually run are different states. Stale observations do not prove current availability. |
| Lifecycle / risk | Expiry, quota / rate limits, service interruption, account restriction or suspension, when observed | Record source/time/status. Unverified suspension or ban risk remains `unknown`, not an asserted event. |
| Evidence | Inputs, source revision, actual result/failure, verification route | Preserve only necessary non-secret evidence; do not use synthetic evidence as a real run. |

If a task requires runtime identity, access, permission, budget, or availability evidence and it is missing, block that action. Do not silently switch accounts, models, providers, or paid routes. This ontology describes the required binding; it is not a live account registry or a claim that current service status has been checked.

## Workbench Substrate

The workbench is the operating environment for the Repo: host operating system, VS Code, and approved / as-needed CLI. It is a substrate used by RWS, not the whole work system.

- **Operating systems and shells**: macOS, Linux, and WSL2 use a bash-family shell; native Windows uses PowerShell 7. Shell scripts should invoke tools; use Python or Node.js for multi-step logic. Do not maintain duplicate `.sh` and `.ps1` implementations for the same task.
- **Linux / WSL2**: WSL2 with Ubuntu 26.04 LTS and its bash 5.x are carried forward as the selected baseline targets from the 2026-10-05 RWB source. This is not an installation observation or permission; machine setup still requires Player approval.
- **macOS shell**: use syntax common to bash and zsh; the bundled bash version is unverified, and no separate bash installation is implied.
- **Windows PowerShell**: 7.6 LTS is the selected baseline target; Windows PowerShell 5.1 is outside that baseline. This does not assert the target is installed on a particular host.
- **Node.js**: Node 26 is the selected LTS target carried forward from the RWB source. Verify the actual version / release channel when a task depends on it; no installation is implied.
- **Python**: repository Python scripts use `uv run python ...`; `.python-version` pins Python 3.14.
- **uv**: the RWB draft's target was 0.12.23; the last recorded macOS observation was 0.12.14 / Python 3.14.4, and the current Windows execution environment was observed as uv 0.12.20 / Python 3.14.0 on 2026-10-06. These are device/time-specific observations, not a universal baseline or an install/upgrade authorization.
- **Access order**: CLI, then MCP, then computer use as fallback. A tool's availability or registration does not prove permission or a particular execution.
- **Shell baselines**: bash should use portable bash/zsh syntax on macOS; native Windows uses PowerShell 7. Specific version choices remain subject to observed compatibility and Player-approved changes.

## Tools and Permission

Tools are deterministic or bounded capabilities used to inspect, modify, render, or communicate. Each invocation is governed by its own source, inputs, permission, cost / side effect, and verifiable result.

| Tool class | Action / effect | Required boundary |
| --- | --- | --- |
| `scripts/verify.py` | Read-only structure, source-pin, and local-link checks | Report actual pass/fail. `--record-tool` adds local evidence only with explicit actor and approval evidence; it is not Human acceptance. |
| `scripts/mirror.py` | Reads an approved explicit Markdown group and writes one deterministic MPS artifact | Not a Narrative Page generator; caller must confirm source custody and approval. No network writeback. |
| CLI | Install, invoke, or remove a command-line tool | Install on demand and remove after use unless explicitly retained; any install, including `npx` / `uvx`, requires Player approval. Pin runner versions; record install/removal/action evidence. |
| Git | Read source revision/diff; stage, commit, push, or alter history | Commit/push and external effects require Player gate. Never overwrite unknown changes or rewrite history. |
| VSC / AI clients | Human task authoring and SI conversation/agent execution | Verify client, entitlement, picker, scope, action permission, and actual runtime separately. Never claim model switching or execution without evidence. |

Other Tools are added only when needed and when input source, permission, budget/cost, side effects, and result verification are clear. A registered or pinned CLI version does not prove that it is installed or authorized for a specific action.

### Retained CLI register

| CLI | Purpose | Source / invocation | Boundary |
| --- | --- | --- | --- |
| `cf@1.0.0-beta.9` | Manage Cloudflare resources | M2 decision; `npx --yes --package=cf@1.0.0-beta.9 cf` | Version selected; no global installation; no implicit account/resource permission. |
| `wrangler@4.145.0` | Cloudflare Pages Direct Upload | M2 decision; `npx --yes wrangler@4.145.0` | Version selected; does not authorize deployment or a paid action. |
| PDF CLI / engine | Not selected | Pending Player decision | Not registered or installed. |

## Open Baselines and Decisions

- The exact meaning of “CLI use” (Player and SI entering through a command line versus SI operating CLIs) remains to be specified.
- The legacy RWB source contains an SI-proposed CLI acquisition priority: package runner (`npx` / `uvx`), then a portable single-file tool in a temporary location, then the platform package manager, otherwise stop and discuss. The proposal was explicitly pending Player confirmation and is not adopted policy; each install still requires separate approval.
- Whether individual retained CLIs also expose an MCP entry remains unreviewed; an MCP interface does not remove the applicable permission and evidence gates.
- The PDF CLI and PDF rendering engine remain undecided.
- The Windows execution environment was observed at uv 0.12.20 / Python 3.14.0 on 2026-10-06; the prior macOS observation was uv 0.12.14 / Python 3.14.4. The baseline source cites uv 0.12.23. No upgrade follows from those observations; any installation or upgrade requires Player approval.
- The RWB source recorded Python 3.15 publication and macOS's bundled bash version as unverified. Recheck before making a new baseline decision; preserve the old observation date instead of treating it as current fact.
- Warp is not part of the selected workbench baseline unless Player revises that decision.

## Maintenance and Source Custody

- RWS does not import T189 service/runtime, CRAFTS dependencies, credentials, or source history. Maintenance sync records only its approved conclusions.
- A structural gate does not prove snapshot content or permission. Runtime snapshots bind an authorized `targetrun_id / slug / quartet / date / hash / no-writeback` group and remain non-authority observations.
- Pinned NP0 / MPS sources are not automatically upgraded. Before moving or removing an artifact, identify its custody and whether it is unique evidence; do not delete valid outputs as cleanup.
- Tool runs, model-picker observations, actual model workloads, and Human/EVAL acceptance are separate evidence classes.

## Working Loop

Complete work through a traceable loop:

`role / task -> Mission / EVAL / ticket -> reasoning / execution -> Narrative Page when useful -> Human review -> content revision or authorized Tools -> result / evidence -> EVAL / alignment -> completion / handoff / learning`

- A task handoff states object, diff, evidence, owner, scope, and stop rule.
- `Sol` is the Mission reasoning / execution target and `Luna` the rem maintenance target. These role labels do not identify a selected model or prove availability; verify runtime identity and execution independently.
- Business-task content belongs to the Mission flow; software rules, skills, and adapters belong to rem maintenance.
- A Narrative Page is read-only, non-authority, and no-writeback. It points to explicit source files and does not replace them.
- Human acceptance and role alignment require Human evidence. Tests, generated HTML, model picker state, and self-assessment do not substitute.
- Product EVAL, consumer-task EVAL, and software-maintenance tests remain separate.
- Stop the corresponding action when binding, source, permission, subscription, model identity, cost, or budget is missing. Do not silently fall back.

## Authority Boundaries

- `Ego/Rws.md` describes the work system and its operational boundaries; it does not grant access, model capability, Tools permission, or Mission acceptance.
- `Ego/RAP.md` remains the sole RA rules source. Root `AGENTS.md` remains the single SI instruction file and execution route.
- `Story-rem` / `eval-rem-v1` remain the Primary Mission binding. RWS does not amend product EVAL A1-A13.
- RWS is rem-specific; it does not import T189 service/runtime, CRAFTS dependencies, credentials, or source history.
- The VS Code / SI list is a Player-declared scope. Current installed client, active profile, subscription, provider/model identity, and actual run must be independently observed before task execution.
