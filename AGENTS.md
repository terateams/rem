# rem Agent 规则

> **Reader**: SI Agent（VS Code Copilot、Codex）。规则源头与给人看的说明见 [RAP](Ego/RAP.md)。
> **Player**: yangjun / bitguts
> **Freshness**: 2026-10-05

rem = T本智能软件V1.0：完整 REM（Repo × EGO × Mission）协同软件，见 [README](README.md)。

## 硬边界（Hard limits）

- 未经 Player 批准，不做：外部、破坏、付费、权限扩张、采购、release、authority 变更。
- 不读 credentials 或 tenant secrets。不把 secrets 写入仓库。不部署付费资源。
- 不覆盖未知改动。不用 stash / reset / rewrite history 自动恢复。commit / push 按 Player gate。
- 不新增第二个指令文件。生产 skills 只在 `.agents/skills/<name>/`。
- 不引入 T189 或 CRAFTS 依赖。
- 绑定、许可、来源、订阅、模型或预算有缺口时 blocked：停止对应动作，说明缺什么，不静默 fallback。

## 开始前（Start）

1. 读取 [today](Repo/today.md)、[now](Repo/now.md)、[INTENT](Repo/INTENT.md) 与 Ego 四件套：[Ego-rem](Ego/Ego-rem.md)、[EdgeTeam](Ego/EdgeTeam.md)、[Naming](Ego/Naming.md)、[Working](Ego/Working.md)。缺少任何一个时 blocked，不猜测降级。
2. 绑定：exactly one Primary=[Story-rem](Mission/Story-rem.md)，EVAL=[eval-rem-v1](Mission/EVAL/eval-rem-v1.md)，Secondary=0，selected_method=null。
3. 相对时间绑定 today 的日期 / 时区。
4. 开工与收工用 `rem-ready`。

## 工作方法（Method）

1. 闭环：岗位 / 任务 -> Mission / EVAL / 工单 -> 推演 / 执行 -> 影页 -> Human 判断 -> 修订内容或执行 Tools -> 结果 / evidence -> EVAL / 对齐 -> 完成 / 交接 / 沉淀。
2. 输出对照 Mission / EVAL。Human 岗位对齐与 acceptance 由 Human 决定并独立留证；不用渲染、机器测试或自评代替。产品 EVAL、consumer task EVAL、软件维护 tests 互不代替。
3. 当前结果、Human approval、工具观察与 accepted outcome 分开。运行最相关检查，记录命令 / 实际结果；未跑写 not_run / unknown。先验证后声称完成；无证据不宣称完成。synthetic tests 不证明真实 Human、模型、任务或 provider 可用。
4. 每次获授权 Tools 动作记录：任务 / 岗位、tool / action、权限 / cost、输入来源、实际结果或失败、证据位置、下一步。见 [action evidence](Mission/evidence/README.md)。
5. 影页（Narrative Page，旧称镜页）是 SI 基于 Repo 实况叙事生成的 HTML 页：叙事不是事实，non-authority / no-writeback。页头写明来源文件与提交哈希、生成工具与版本、日期。只读显式来源，不扩读目录；审查 secrets / 输入许可后才生成。页面不授予权限，不替代原件；原件变更后旧页 stale。
6. Skill routes：np0 处理有界叙事；rem-ready 启动 / 暂停；motioner 管 Draft -> Approved -> execution -> landing / source retirement；looper report-first 维护；teamspage 生成与验证由 `scripts/mirror.py` 产出的确定性影页。skills 单一 identity，登记在 [TeamSkill](Ego/TeamSkill/TeamSkill.md)。
7. practice / observation 归 `Repo/Dojo`。正式证据按 Mission custody。Decision / Audit / Ego admission 需 owning Human，不从 raw evidence 自动升格。完成的 Motion 经 canonical Audit、consumer audit、History triage 后退休到 `Repo/days/<date>/Motion/`。
8. NP0 capsule 与 pinned NP0 / MPS 原样继承，不改写、不自动升级。
9. 修改 Agent 配置（本文件、技能、检查、CI）前先读 [RAP](Ego/RAP.md)，改后运行 `sh scripts/ra-check.sh`。
10. 中文主叙事，English stable fields。不设第二 SSOT。冲突时本文件优先于 skill 默认值。

## 检查（Checks）

- `sh scripts/ra-check.sh`：RA仓规静态检查。
- `python scripts/verify.py`：rem 结构与 source pin 检查。

## 运行环境（Runtime）

VS Code + GitHub Copilot + Codex（版本 26.930.31730 或更高）。Copilot：Sol 为 Mission 推演 / 执行目标，Luna 为 rem 软件维护目标。Codex：模型目标尚未定义。模型与 picker 由 Human 选择并核验；不声称已自动切换或已启用。订阅 / 席位不可用时 blocked，替代方案须 Player approval。