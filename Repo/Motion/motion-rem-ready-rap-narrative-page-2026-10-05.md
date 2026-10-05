# Motion: rem-ready RAP Alignment and Narrative Page

> **Date**: 2026-10-05
> **Player**: yangjun / bitguts
> **Status**: Executed; Player acceptance pending
> **Type**: AgentSkill alignment / Narrative Page
> **Service Object**: rem-ready startup and handoff route
> **Primary Route**: [Story-rem](../../Mission/Story-rem.md) -> [EVAL](../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Player 当前对话：“启动Motion, 更新rem-ready: 1. 对齐当前REM (RCI被取消了, 有了RAP) 2. 影页(动词) rem-ready skill”
> **Execution Audit**: [canonical Audit](../../Mission/Audit/2026-10-05-rem-ready-rap-narrative-page.md)
> **Round**: R1

## 问题与拟议裁决

当前规则源头为 `Ego/RAP.md`；根目录 `AGENTS.md` 是 SI 执行指令，`rem-ready` 是启动 / 暂停工作流。`rem-ready` skill 目前未显式说明此 authority boundary，也没有自己的 Narrative Page。RA仓规已将旧 RCI 残留列为已解决；不应把 RCI 当作现行规则源。

拟议裁决：在 `rem-ready` skill 中简要写明 `AGENTS.md`、`Ego/RAP.md` 与 Skill 的分工，并标明 Narrative Page 是 non-authority / no-writeback；新建一页仅叙述该 Skill 的 Narrative Page，列出来源、版本、提交基线、生成工具 / 版本 / 日期与未知项；在 `Repo/TeamsPage/README.md` 增加该页入口。

## 范围

**当前请求授权范围：**

- 更新 `.agents/skills/rem-ready/SKILL.md` 的 description 与 authority / Narrative Page 边界；保留既有 startup、日期、Git、Dojo、cursor、模型 / 权限和离开前收口要求。
- 新建 `Repo/TeamsPage/rem-ready-teamspage.html`，只读本 Motion 指定的 rem-ready / RA authority 来源；页面 offline、non-authority / no-writeback。
- 更新 `Repo/TeamsPage/README.md` 导航，链接该页。
- 运行 `sh scripts/ra-check.sh`、`python scripts/verify.py` 与针对新增页面的本地链接 / HTML 检查。

**不纳入：**

- 修改 `AGENTS.md`、`Ego/RAP.md`、EGO / Mission / EVAL / INTENT authority 或生产 AgentSkill identity。
- 修改 `scripts/mirror.py`、MPS `#mp-data` / manifest / source pins，或把 Narrative Page 当成 MPS artifact。
- 执行模型 workload、外部 Tools、付费 / 部署动作；commit / push；刷新 daily handoff。
- 推断 Active Profile、Settings Sync、Copilot entitlement、picker / backend 或 Human acceptance。

## Runtime Permission

Player 当前请求明确要求更新 rem-ready 并为其制作 Narrative Page；据此授权以上本地文件范围及必要本地验证。此次授权不将 Motion source 从 Draft 静默改为 Approved，不扩展到未列出的源文件、外部或发布动作。执行时须在 Audit 中保留 source 当时为 Draft 与本次对话授权的事实。

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | Skill 明确 `AGENTS.md` 执行路由、`Ego/RAP.md` 唯一规则源、Skill 非 authority；不将 RCI 当现行 authority | Skill diff；`sh scripts/ra-check.sh` pass |
| D2 | Narrative Page 准确叙述 rem-ready 边界，标注 source files / hashes / base commit / generator / version / date / unknowns，且 non-authority / no-writeback | HTML source / metadata review；HTML parser 与 local-link check |
| D3 | `Repo/TeamsPage/README.md` 可导航到新页；结构与 Markdown links 通过 | `python scripts/verify.py` pass |
| D4 | 范围外来源、MPS pins、现有页面和用户改动未被改写 | `git status --short`、`git diff --check`、source-path review |
| D5 | 不冒称 Player acceptance 或产品 EVAL 完成 | Motion / Audit 明确保留 acceptance pending 与其它 not_run gates |

## Landing / Rollback

Canonical rule source 保持 `Ego/RAP.md`；SI 指令仍由 `AGENTS.md` 承载；运行入口为 `.agents/skills/rem-ready/SKILL.md`。Narrative Page 只作可重建的 review projection，来源改变即 stale。若 Player 不接受，后续经授权仅反向修改本 Motion 列出的 Skill、README 导航与新页；不回滚或覆盖既有用户状态。

## Execution Result

The local scope was executed under the current Player request while the source status was Draft; it was not represented as durably Approved.

- D1: Skill authority boundaries now name `AGENTS.md` as SI execution instructions and `Ego/RAP.md` as the sole RA rules source; legacy RCI is explicitly retired. `sh scripts/ra-check.sh` returned `RA仓规 0.6.5: OK`.
- D2: The offline Narrative Page records its source paths, SHA-256 values, base commit, generator, tool version, date, and unknown model/runtime ID. It is marked non-authority / no-writeback. A standard-library parser confirmed valid HTML, 8 resolving local links, and no scripts.
- D3: The canonical TeamsPage README links the new page. `python scripts/verify.py` returned `structure=pass`, `failures=[]`.
- D4: Scope stayed within the Motion; `git diff --check` passed, and the new Motion, Audit, and HTML files have no trailing whitespace and exactly one final newline. The final worktree state is recorded in the Audit.
- D5: Player acceptance pending. Human review, runtime models, and role alignment remain `not_run`; no product EVAL completion is inferred.
