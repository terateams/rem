# Motion: REM仓规

> **Date**: 2026-10-07
> **Player**: yangjun / bitguts
> **Status**: Done
> **Type**: REM rules workflow / cross-repo Skill capability
> **Service Object**: `REM仓规` activation workflow; `shaping` hypothesis carrier; `rem-make` implementation carrier; one local REM target
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> [EVAL](../../../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Player 当前对话提出：以“REM仓规”为 Motion 标题和 Skill 激活语，覆盖 REM 仓规命名、定义、更新与评估；`shaping` 承载猜想，`rem-make` 承载实现；Skill 应能在同一 PC / Mac、VSC 可访问的另一 REM Repo 使用。
> **Target Access**: `D:\Github\EGO-T189` 可读性于 2026-10-07 验证；README 将其标为 active / pilot REM Repo。只读了 README、AGENTS、RCI 与相关 Skill；未写入目标仓。VSC 实际 Skill activation 未验证。
> **Runtime Approval**: Player 当前对话：“当前可以Read Ego-T189, so I will approved this motion and: 1. 按照Reo-T189的REM仓规, 更新当前的Repo 2. 校验的结果包括但不限于: AGENTS.MD的主导, RCI的废止, rem-ready的升级等等”
> **Execution Confirmation**: Player 当前对话：“行, 批准执行”；适用范围仍为下列 current-Repo scope，不扩展至 EGO-T189 写入或 commit / push。
> **Player Acceptance**: Current conversation: “经过验证, motion approved , 认定完成, 可以退休”。Acceptance covers closeout of this Motion with the remaining D3-D7 limitations explicitly retained below and in the canonical Audit.
> **Execution Target**: `D:\Github\rem` only; `D:\Github\EGO-T189` remains read-only reference.
> **Source Retirement**: `Repo/Motion/motion-ra-cross-repo-shaping-2026-10-07.md` -> this dated archive.
> **Canonical Audit**: [REM rules governance Audit](../../../../Mission/Audit/2026-10-07-rem-rules-governance.md)
> **History Triage Result**: Audit First; no Concept / EGO admission; source retired after Player acceptance with unrun cross-Repo VSC gates preserved.
> **Baseline**: `6af5a9bbc5e74eba246e0af952679658867717ef`
> **Round**: R2

## 问题与拟议裁决

### Proposed Name And Definition

`REM仓规` 是 Player 提议的 Motion 标题与工作流激活语：当用户要求理解、命名、更新或评估某个 REM Repo 的 Agent / 仓规时，触发一次有界、按 target 原生 authority 执行的流程。它是 workflow label / trigger，不是新的规则文件、权限源或额外 Skill identity；触发本身不授权任何仓库写入。

本 Motion 暂按以下 target-native authority 区分，不做盲目同名替换：

- 当前 `rem`：`RA仓规` 是 Agent 配置规则集；`Ego/RAP.md`（0.6.6）是规则源，根 `AGENTS.md` 是 SI 执行入口。
- 目标 `EGO-T189`：README 标识为 active / pilot REM Repo；`.github/copilot-instructions.md` 当前自称 `AI仓规 / RCI`，版本 `4.9.3`，是本仓 Copilot authoring authority；根 `AGENTS.md` 是其 bootstrap projection。RCI 已将 `REM仓规` 列作跨仓称呼。

因此，本 Motion 要定义的是跨仓 `REM仓规` workflow 如何发现、评估、更新各仓自己的规则源；不预设 `RA仓规`、`AI仓规 / RCI` 或 `RAP` 文件可被全局字符串替换。是否将 `REM仓规` 提升为各仓共用的规则集 canonical name，是独立的 Naming / authority gate，不能由标题或 Skill trigger 自动推出。

### Proposed Carrier Split

```text
REM仓规 activation -> motioner binds Motion / scope -> shaping forms a falsifiable hypothesis and revision candidate
    -> Player decision / permission -> rem-make implements the approved target diff -> target checks -> motioner audit / handoff
```

- **`shaping`**：猜想 / bet 的承载者。做 report-first inspect、比较依据并形成可证伪的 revision candidate；不实施目标规则写入，不替 Player 接受或授予权限。
- **`rem-make`**：获批后的实现承载者。当前 `rem` 新增 target-native candidate；只在 target、文件 allowlist 与 Player permission 明确后写入，并运行 target-native checks；不会因 Skill activation 获得写权限。
- **`motioner`**：Motion lifecycle 承载者，负责 binding、approval gate、执行留证、canonical Audit、Human / Player acceptance、History Triage 与 source retirement；不代替前两者完成各自工作。

基线核验发现：EGO-T189 当前 `AGENTS.md` 把 RCI 修订专属给 `shaping`；目标 `.agents/skills/rem-make/SKILL.md` 为 `candidate` 且面向新建 REM，排除现有 REM 维护。此次 runtime approval 仅覆盖当前 `rem` Repo；这些目标仓契约冲突不由本地更新解除，目标仓保持只读。

## 范围

**本次获批并执行的当前 Repo scope：**

- 将根 `AGENTS.md` 明确为本仓唯一 controlling SI instruction，设定其相对 Skill defaults 的优先级；保留 `Ego/RAP.md` 为 RA 规则语义定义与 Human-facing 说明，要求两者一致。
- 确认 RCI 在当前 `rem` Repo 退役：禁止 `.github/copilot-instructions.md` 与 `.github/instructions/`；保留历史 RCI mentions 作为 provenance，并由 `ra-check.py` 检查活动 carrier 不存在。
- 将 `REM仓规` 固定为单一显式 REM Repo 的规则评估 / 更新 workflow trigger；由 `shaping` 形成 bet / revision candidate、`rem-make` 实施获批 diff、`motioner` 管 lifecycle。
- 新增当前 `rem` 的 `rem-make` target-native Skill candidate，升级 `rem-ready` authority / cross-Repo binding route，更新 shaping、Naming、Skill registry / deployment 和 checker consumers。
- 执行本仓 Agent configuration、结构、链接与 Markdown 质量检查，并保留 target-native direct consumer / VSC discovery 等未验证 gate。

**明确不纳入：**

- 不修改 `D:\Github\EGO-T189` 或任何其它 Repo；不声称该仓的 AGENTS / RCI 冲突已解决。
- 不枚举或扫描其它 sibling repositories，不把任一 Repo 中的 EGO / Mission / policy / license / permission 自动带入另一 Repo。
- 不 fetch / pull / commit / push / rewrite history，不安装 CLI，不读 credentials / tenant secrets，不做付费、部署、外部或权限扩张动作。
- 不改 REM 产品 EVAL、RWS、T189 / CRAFTS authority、历史 Audit 内容或已退休的 `RCI` 引用；任何 canonical naming / authority 变化走 owning Motion 和 Player gate。

## Runtime Permission

Player 当前会话批准按 EGO-T189 的 REM 仓规更新**当前 `D:\Github\rem` Repo**，并验证至少包括 AGENTS 主导、RCI 退役、rem-ready 升级。批准不扩展到 EGO-T189 写入、Git commit / push、付费、安装或部署。遵循 motioner 生命周期规则，source `Status: Draft` 保持原样；Audit 记录本次 runtime approval 与 source status。

后续若扩大至 EGO-T189 target write 或真实跨 workspace VSC 行为验证，仍需单独绑定权限并满足：

1. Player 单独批准 EGO-T189 的具体 target path、责任主体、文件 allowlist、source / adaptation permission 与本地 write permission。
2. 重新读取 target owner authority 与 route 决策；解决其 `AGENTS.md` / RCI route 与 rem-make carrier 的冲突。
3. 检查 target Git / editor-buffer 状态、source license / provenance、rollback 与 direct consumers；dirty、unknown 或 merge/rebase 中止相关写入。
4. 在实际 VSC workspace 验证 Skill discovery / activation / behavior；文件读取、metadata、同机路径可访问均不替代。

Cost ceiling: no install, network write, paid action, commit, or push is included. Any such validation route requires separate Player approval.

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | `REM仓规` 的定义与 activation 清楚，且 workflow trigger、target authority file、`RA仓规` / `RAP`、`AI仓规` / `RCI` 没有混为一谈 | Player 对名称 / 定义的裁决；current RAP、target RCI 与 Naming source 的逐项映射；历史 token 保留规则 |
| D2 | carrier split 准确：`shaping` 只形成 hypothesis / revision candidate；`rem-make` 实施 Player-approved diff；`motioner` 管 lifecycle | 两个 Skill sources、各自 registry / deployment / consumer 对照；target AGENTS route conflict 的批准修订 |
| D3 | Skill host 与 target 是明确的不同 Repo，且 VSC 工作面确实可调用 host Skill 并安全寻址 target | host / target path、repo identity、workspace topology、source revision、Permission 与 Git/editor state 证据；实际 VSC invocation |
| D4 | `shaping` 运行时只输出有来源、可证伪的猜想 / revision candidate，不提前写 canonical rules | VSC 行为记录、输入来源、hypothesis / evidence / uncertainty；未批准时 target diff 为零 |
| D5 | `rem-make` 能在现有 REM 仓的批准范围内更新而非只创建新 Repo；未授权、dirty、冲突或越界输入时阻止写入 | VSC 实际调用、批准 scope、精确 diff、negative cases、rollback point；candidate / production status 以实际 target source 为准 |
| D6 | 更新后的 target rule contract 与全部 active direct consumers 一致，且保留 target-specific policy / provenance | target config checker / CI / structure checks 的真实结果；consumer audit 与语义回归，不以关键词清零代替 |
| D7 | 支持声明与实测平台一致 | Windows、macOS 各自的 host、VSC workspace、Skill invocation 与结果；未实际运行的平台标 `not_run` |
| D8 | Player acceptance、Audit custody、source status 与 History Triage 完整；未替代产品 / consumer EVAL | Player 对实际 diff 的 accept / reject evidence、canonical Audit、target evidence、History Triage Result |

Skill 文档、静态 checker、synthetic fixture、同机路径可读性均不能代替 D3-D5 的实际 VSC use 或 D8 Human decision。目标仓 RAP / RCI 自身的 agent test route需按其现行规则核验；未运行的 host / harness 记录为 `not_run`，不推断跨工具通过。

## Stop Rule

Skill host、target identity、目标规则 authority、命名裁决、source permission、Player write scope、rollback 或 VSC 实际 activation 任一缺失时，限制为已授权只读核验 / hypothesis 输出并将依赖 gate 标 `blocked`。在 target 的 AGENTS / RCI route 冲突未获 owning Player 批准修订前，`rem-make` 不可写 RCI。不得因 `REM仓规` trigger、同机路径或 `rem-make` 文件存在而自动修改目标。遇到 stale / conflicting / dirty state、secret 风险、source license gap、需要安装 / 付费 / 外部 action 时，停止对应操作并给出最小解除条件。

## Landing / Rollback

若获批，先由 `shaping` 交付 target-specific hypothesis / revision candidate；Player 接受 scope 后才允许 `rem-make` 实施。每个 Repo 的实际 canonical rule source、root projection、Skill host / target route、registry / deployment / checker 与 direct consumers 按各自 owner 独立落位和验证；Motioner 记录 approval、Audit、acceptance、History Triage 与 source retirement。Rollback 只回退本 Motion 明确批准且可识别的 target diff，不 reset / rewrite 未知历史；source 与 target 各自保留 revision / evidence。当前 EGO-T189 的 `rem-make` 仍为 `candidate`，本 Draft 不改变其 status。

## Closeout - 2026-10-07

Player 在当前对话说明：“经过验证, motion approved , 认定完成, 可以退休”，并批准本 Motion 完成与 source retirement。本次接受的是获批的当前 `D:\Github\rem` scope；EGO-T189 保持只读，目标仓冲突没有被写入解决。

Motion status 为 `Done`，canonical Audit 为 [REM rules governance Audit](../../../../Mission/Audit/2026-10-07-rem-rules-governance.md)。D3-D7 的技术状态仍按 Audit 原样保留为 partial / not_run；Player 的完成裁定不把这些 gate 转成技术 pass，也不证明 VSC discovery、macOS behavior 或实际模型运行。

History Triage 为 `Audit First`；不请求 Concept / EGO admission。此完整 source 于 Player acceptance 后退休至 `Repo/days/2026-10-07/Motion/`。
