# rem Agent 规则

> **Owner**: yangjun / bitguts
> **Freshness**: 2026-10-05
> **Authority**: 本文件是本 repo 唯一的 agent 指令文件，不继承 EGO-T189 实例规则。

## 目的（Purpose）

rem = T本智能软件V1.0：完整 REM（Repo × EGO × Mission）协同软件，见 [README](README.md)。

## 开始前（Start）

读取 [today](Repo/today.md)、[now](Repo/now.md) 以及 EGO 四件套：[EGO-rem](Ego/Ego-rem.md)、[EdgeTeam](Ego/EdgeTeam.md)、[Naming](Ego/Naming.md)、[Working](Ego/Working.md)。缺少任何一个时 blocked，不猜测降级。

## 工作方法（Method）

1. REM = Repo × EGO × Mission。加载 EGO 四件套与 Repo/today、now、INTENT；相对时间绑定 today 的日期 / 时区。 exactly one Primary=`Mission/Story-rem.md`；EVAL=`Mission/EVAL/eval-rem-v1.md`；Secondary=0；selected_method=null。
2. 以完整 REM 定义、执行、EVAL、反馈 / 修订、对齐 / 交接、完成与沉淀。NP0 capsule 原样继承，通用原理不因场景变化重写；scope / evidence / decision-rights / bounded action 明确。不携带 T189 或 CRAFTS active dependency。
3. VSC + GitHub Copilot 订阅 / 席位为 runtime 前提。Sol 为 Mission 推演 / 执行目标，Luna 为软件维护目标。仅 Human 在 picker 明确选择，不声称自动切换或已启用；不可用时 blocked，equivalent fallback 须 Owner approval。
4. Human 由岗位 / 责任 / 任务驱动。Agent 输出对照 Mission/EVAL；Human 岗位对齐与 acceptance 独立留证，不由渲染、机器测试或 Agent 自评推导。
5. 镜页是 rem 内生、non-authority/no-writeback HTML 功能。NP0 组织叙事，adapter 绑定来源，renderer 只呈现。只读显式来源，不扩读目录；审查 secrets / 输入许可后才生成；页面不授予权限或替代原件，修改后旧页 stale。
6. Human 看镜页后在 VSC 修订内容或执行获授权 Tools。记录任务 / 岗位、tool/action、权限 / cost、输入来源、实际结果或失败、证据、下一步。外部、destructive、costly、权限扩张、采购、release 与 authority 变更须批准；no-secret。
7. Skill routes：np0 处理有界叙事；rem-ready 启动 / 暂停；motioner 管 Draft -> Approved -> execution -> landing / source retirement；looper report-first 维护；teamspage 仅内部 MPS 实现，不额外产品品牌。skills 单一 identity，登记在 Ego/TeamSkill/TeamSkill.md。
8. 当前结果、Human approval、工具观察与 accepted outcome 分开。运行最相关检查，记录命令 / 实际结果；未跑写 not_run / unknown。synthetic tests 不证明真实 Human、模型、生产 task 或 provider 可用。
9. 输入 practice / observation 归 Repo/Dojo，正式证据按 Mission custody；Decision/Audit/EGO admission 需 owning Human，不从 raw evidence 自动升格。completed Motion 在 canonical Audit / consumer audit / History triage 后退休。
10. 不覆盖未知改动，不 stash/reset/rewrite history 自动恢复。不读 credentials 或 tenant secrets，不部署付费资源。中文主叙事，English stable fields；不设第二 SSOT。

适用规则优先级：本文件 -> target instructions -> skill defaults。

## 检查（Checks）

- `sh scripts/ra-check.sh`：RA仓规静态检查。
- `python scripts/verify.py`：rem 结构与 source pin 检查。

## 禁止（Do not）

- 生产 skills 只在 `.agents/skills/<name>/`。
- 外部、破坏、付费、权限 / authority 变更须 Owner gate；先验证后声称完成。
- 不改动外部 EGO-T189 source repo。
- 不新增第二个指令文件。
