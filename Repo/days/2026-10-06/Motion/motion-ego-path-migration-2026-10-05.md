# Motion: Ego 领域路径大小写迁移

> **Date**: 2026-10-05
> **Owner**: yangjun / bitguts
> **Status**: Done
> **Updated**: 2026-10-06
> **Execution Audit**: [canonical Audit](../../../../Mission/Audit/2026-10-05-ego-path-migration.md)
> **Closeout**: Player accepted 2026-10-06; source retired to `Repo/days/2026-10-06/Motion/`
> **Type**: repository naming / path migration
> **Service Object**: rem canonical Ego path
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> EVAL
> **Source Request**: Owner 当前对话：“要发布 Ego，还需先把大小写改名和相关路径迁移正式登记到 Git，再验证并推送”
> **Round**: R1

## 问题与拟议裁决

当前 Windows 工作区显示 `Ego/`，但 Git 当前提交记录 `EGO/`；`core.ignorecase=true` 使大小写差异未出现在 `git status`。仅在 Windows 保留工作区大小写不能发布稳定路径，也不能证明大小写敏感系统可用。

本次将领域根目录 canonical path 设为 `Ego/`，实例入口文件从 `EGO-rem.md` 改为 `Ego-rem.md`。稳定字段 / acronym `EGO` 与上游来源标识 `EGO-T189` 仍按语义保留，不做全文替换。

## 范围

**当前对话授权范围：**

- 通过临时中间路径将 Git 跟踪的目录 `EGO/` 正式改名为 `Ego/`，并将实例入口改名为 `Ego-rem.md`。
- 更新当前 authority、README、Mission bindings、可执行 adapter、tests、`.gitattributes`、source manifest 与 Markdown 链接目标；历史叙事文本保留其当时用词，只修复需要继续可导航的链接目标。
- 将 NP0 runtime snapshot 与其 tests 的路径改动记录为 target deltas；保留 canonical NP0 capsule 原字节与 hash。扩展既有 MPS target-delta 理由与 hash，不改其 frozen upstream source。
- 运行结构 / 链接 / pin 检查、Python test suites 与 Git diff 检查，创建本地提交，并向配置的 upstream 做普通、非强制 push。

**不纳入：**

- 修改 `EGO-T189`、NP0 canonical capsule 或已生成的 TeamsPage HTML；迁移后旧镜页依现有规则保持原件并视为 stale。
- 修改 Mission/EVAL 判据、Cloudflare / DNS 资源、模型配置、凭据或外部服务。
- force push、重写既有历史或丢弃工作区改动。

## Runtime Permission

当前 Owner 对话明确要求执行上述路径迁移、验证与推送；执行开始时本 Motion 为 Draft。该 runtime approval 不冒充 durable Approved 状态；执行范围与实际结果须由 canonical Audit 留证。

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | Git 跟踪树只使用 `Ego/` 与 `Ego/Ego-rem.md` 的 canonical casing | staged/committed tree path listing |
| D2 | 适配器、固定来源路径与 Markdown 链接迁移完成 | `scripts/verify.py` pass、路径检查 |
| D3 | NP0 target snapshot tests 与仓库 Python tests 通过 | 两组测试的实际输出 |
| D4 | frozen capsule bytes/hash 不变，manifest 中 target deltas 与实际 hash 一致 | source-manifest pin check pass |
| D5 | 变更已提交并推送，无 force push | commit id 与普通 push 结果 |

## Landing / Rollback

canonical 路径为 `Ego/`；历史事实文字与上游标识不因目录改名重写。若后续需要回退，使用新的反向迁移提交，不 reset、rewrite 或 force-push 既有历史。Human acceptance 与产品 Mission EVAL 不由机器检查推导。

## Execution Result - 2026-10-05

实现、验证与首次 push 结果见 [canonical Audit](../../../../Mission/Audit/2026-10-05-ego-path-migration.md)。Commit `c3158d3` 已普通推送到 `main`；执行时 Owner acceptance pending，后续 closeout 见上方记录。
