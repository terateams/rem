---
name: rem-ready
description: "用于 rem 冷启动、开工/暂停、日期/Git/工作面核验、日交接与安全收口；遵循 AGENTS.md，RA规则以 Ego/RAP.md 为唯一源头。不用于具体正文、自动同步或替代 Player 批准与 Human acceptance。"
metadata:
  status: in-production
  source_commit: 70090b756d2c4f4e75912ec9f3ede2ff3e8cc0a0
---

# rem ready

## Authority

SI follows root `AGENTS.md`; `Ego/RAP.md` is the sole source of RA rules. This skill is an operational route, not another authority or permission grant. Do not treat retired RCI as a current rules source. Before changing Agent configuration, read RAP; after the change, run `uv run python scripts/ra-check.py`.

## Inspect-first

Read `Repo/today.md`, `Repo/now.md`, `Repo/INTENT.md`, and the EGO quartet. Bind exactly one Primary, its EVAL, Secondary=0, `selected_method=null`, and relative dates to the current host date/timezone. Verify `git status`, ahead/behind against existing local refs, editor-buffer dirty state, `Repo/Dojo` path status, and the previous-day archive. Do not fetch by default; without a fetch, remote freshness is unknown.

Verify terminal cwd against the workspace independently. Check VSC/Profile/Settings Sync/extensions, actual device, and necessary runtime as separately observable facts; unknown stays explicit. On-site facts may be directly observed, declared by the Player/Human, or explicitly marked as carried forward. Do not create a T189 inventory.

Keep subscription/picker observations or Player/Human declarations separate from actual model-run evidence. Sol and Luna are different workload goals; do not switch models or infer either workload from a picker, installed extension, or active chat.

## Andon and Refresh

If the date baseline is stale and Git/editor state is dirty, behind, or unknown, raise Andon and wait for the Player's path choice. Do not stash, reset, pull, overwrite, or silently refresh. After explicit refresh approval, preserve the complete pre-refresh `Repo/today.md` at `Repo/days/YYYY-MM-DD/today.md` using the previous-day date; then replace `today.md`, followed by `now.md`. Do not rewrite `INTENT` as routine daily maintenance.

## Validation and Handoff

Read the actual output of `uv run python scripts/verify.py`; report `not_run` / `unknown` where checks were not performed. Call `scripts/mirror.py` only for an explicitly scoped and authorized deterministic MPS artifact; Narrative Pages are not MPS artifacts. A valid local startup entry does not mean all EVAL A1-A13 gates passed.

An optional rem-ready Narrative Page is a read-only projection. It is non-authority / no-writeback, does not replace this skill, `AGENTS.md`, or RAP, and does not prove readiness. Scope its sources explicitly; mark it stale when a source changes. Away work is limited to date, Git, Dojo, and cursor risks, with a clear return entry. External, destructive, paid, release, commit/push, permission expansion, and configuration changes require the applicable Player approval. Never claim synced or ready without evidence.
