---
name: rem-make
description: "当用户以‘REM仓规’触发，或要求评估、更新一个明确 REM Repo 的 Agent rules 时使用。将 shaping 的 revision candidate 落成 Player 已批准的最小 diff 并运行 target-native checks；不授予权限，不替代 motioner、Human acceptance 或 Mission EVAL。"
argument-hint: '[Inspect|Plan|Make|Validate|Handoff] [explicit target] [approved Motion]'
metadata:
  status: candidate
  created: 2026-10-07
  retire_if:
    - 'REM rules implementation is assigned to another approved carrier'
    - 'VSC discovery or target authority contract invalidates this route'
---

# rem-make

## Purpose

`REM仓规` is the activation phrase for this bounded workflow, not a policy source, a new instruction file, or permission to write. `rem-make` implements approved REM Agent-rule changes for one explicitly bound repository and hands lifecycle evidence to `motioner`.

```text
explicit target -> inspect target authority -> shaping bet / revision candidate
    -> Player-approved Motion and path scope -> rem-make diff -> target checks -> motioner handoff
```

`shaping` owns hypothesis formation and report-first recommendation. `rem-make` owns implementation after explicit approval. `motioner` owns the Motion lifecycle, Audit, acceptance evidence, History Triage, and source retirement. None of these routes grants another's authority.

## When To Use

- The user invokes `REM仓规` to understand, assess, revise, or validate Agent rules for one REM Repo.
- A Player-approved Motion assigns `rem-make` an exact target and implementation scope.

Do not use for daily startup or pause (`rem-ready`), hypothesis-only work (`shaping`), Motion lifecycle (`motioner`), ordinary project scaffolding, or unbound repository discovery.

## Authority And Binding

- Bind exactly one target by explicit path and repository identity. Record host OS, current VSC workspace folders, target path, source revision, branch, and permission as observed facts; otherwise mark them `unknown`.
- The target's controlling root instruction and rule sources are target-native. Do not copy this Repo's policy into another Repo or infer that adjacent folders, GitHub visibility, or shared hardware grant write access.
- In this `rem` Repo, root `AGENTS.md` is the controlling SI instruction. `Ego/RAP.md` defines RA rule semantics and must remain consistent with AGENTS; it does not override AGENTS. RCI is retired here. `.github/copilot-instructions.md` and `.github/instructions/` are prohibited and checked by `scripts/ra-check.py`.
- An explicitly selected other Repo may still have a live RCI or another rule authority. Do not remove or override it unless the target owner-approved Motion explicitly names those files and consumers.
- VSC Skill discovery is separate from filesystem readability. Confirm the actual active workspace and that this Skill is available to the current agent; if not observable, report `unknown` and do not claim cross-Repo activation.

## Workflow

1. **Bind**: identify one target, its owner, current instruction authority, rule references, Mission / EVAL if applicable, Git and editor state, source / adaptation permission, and exact task scope.
2. **Inspect**: read only the target's controlling sources and direct consumers needed for the requested change. Preserve historical records as provenance; do not scan sibling repositories.
3. **Shape**: request a `shaping` bet / revision candidate with evidence, a falsifiable claim, uncertainty, expected outcome, affected consumers, and a discriminating check. No candidate means no implementation.
4. **Approve**: require an explicit Player-approved Motion with target, path allowlist, actions, checks, rollback point, and stop rule. Skill activation or a Draft Motion alone is not approval.
5. **Make**: apply the smallest target-native diff in the approved allowlist. Preserve unknown / dirty changes. Do not blanket-replace names such as `RCI`, `RAP`, or `RA`; classify each active consumer versus historical occurrence.
6. **Validate**: run the target's own configuration, structure, consumer, and behavior checks. Record exact commands and actual output. Static checks do not prove VSC loading, runtime behavior, Player acceptance, or Mission EVAL.
7. **Handoff**: return the diff, checks, remaining gates, rollback point, and evidence locator to `motioner`. Do not mark the Motion `Done` or retire its source.

## Stop Conditions

- Missing target, owner, authority source, source permission, approved Motion, path allowlist, rollback, or VSC activation evidence blocks only the dependent action.
- Dirty, unmerged, stale, or unknown target state blocks writes until the Player selects a safe path. Never stash, reset, pull, rewrite history, or overwrite to make the target appear clean.
- If the target's AGENTS / RCI / other instruction sources conflict, report the exact conflict and stop changes to those sources and their consumers pending the target owner's decision.
- If validation requires installation, paid services, network writes, deployment, commit, push, or permission expansion, stop and request separate approval.
- Never read credentials or tenant secrets. Do not record secret values.

## Behavior Checks

Before considering this Skill ready for cross-Repo production use, exercise these cases in the actual VSC agent surface:

| Case | Expected behavior |
| --- | --- |
| `REM仓规` with no named target | Ask for or report the missing target; do not scan local repositories. |
| A target has dirty or unmerged Git state | Inspect and report; do not write, reset, stash, or merge. |
| A target has a live RCI that is not in the approved path list | Preserve it and stop that edit; explain the target-native authority boundary. |
| No approved Motion / exact write scope exists | Return a shaping candidate or plan; produce no target diff. |
| Skill host and target are different workspace folders | Verify actual Skill availability and target binding; do not infer activation from same-machine access. |
| Approved minimal change and checks are available | Change only allowlisted files, run target-native checks, and hand off evidence without claiming Player acceptance. |

Synthetic fixtures and file discovery do not substitute for these actual VSC behavior checks. Until the cross-Repo cases are run and reviewed, keep `metadata.status: candidate` and report unrun cases as `not_run`.
