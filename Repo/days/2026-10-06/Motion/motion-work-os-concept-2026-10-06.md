# Motion: rem Work-OS 概念定义

> **Date**: 2026-10-06
> **Player**: yangjun / bitguts
> **Status**: Done
> **Updated**: 2026-10-06
> **Type**: EGO concept / Naming proposal
> **Service Object**: rem Work-OS and its relation to RWB, Tools, and Working
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> [EVAL](../../../../Mission/EVAL/eval-rem-v1.md)
> **Player Approval**: Current conversation: “批准Motion, 开始执行, 一步一步的”
> **Player Acceptance**: Current conversation: “接受并授权退休”
> **Execution Audit**: [canonical Audit](../../../../Mission/Audit/2026-10-06-rws-work-system-migration.md)
> **Source Retirement**: Former EGO source bodies retired; this Motion source is archived at `Repo/days/2026-10-06/Motion/`
> **History Triage Result**: Audit First; bounded RWS canonical-source acceptance; no product EVAL or runtime admission
> **Source Request**: Player 当前对话：“启动Motion: Ego下, 定义Work-OS, 它是包括了: Rwb、Tools、Wokring 以上3个维度的。Rem 的 repo 是智力工作的场所，where ‘brain’ is；repo 配套 SI（超级智能）via VSC；rem 的主体 Player 是商务人士，超越了程序员；以上跃迁产生 Work-OS 新概念。梳理推敲。”
> **Continuation Request**: Player 当前对话：“工作前提中: SI要明确定义, 有预算, 有可用性, 有使用中, 被封号的风险等等, 也就是 SI的Ontology性”
> **Scope Clarification**: Player 当前对话：“继续补充: SI这里, 特指VSCode下, copilot的对话窗口, 包括了 原生的copilot enterprise, 也包括codex claude code等, 以当前实际为参考”
> **Naming Proposal**: Player 当前对话：“用rem work os, aka Rws, 如何?”
> **Context Source**: [Satya Nadella on X](https://x.com/satyanadella/status/2103455884366188544), posted 2026-09-25; reviewed 2026-10-06
> **Round**: R1

## 问题与拟议裁决

在本 Motion 起草时，EGO 文件分别描述工作台、可调用能力和工作闭环，尚无稳定词说明三者合在一起服务什么样的工作：

- [RWB notice archive](../Ego/Rwb.md) 起草时描述操作系统之上的 VS Code / CLI 工作台；其正文现已退休，职责纳入 RWS。
- [Tools source archive](../Ego/Tools.md) 起草时描述可授权、可验证的能力与副作用边界；其正文现已退休，职责纳入 RWS。
- [Working source archive](../Ego/Working.md) 起草时描述从任务绑定到证据、Human 判断、EVAL、交接与沉淀的闭环；其正文现已退休，职责纳入 RWS。
- [Naming](../../../../Ego/Naming.md) 现已登记 `RWS = rem Work System`；此记录保留起草时的命名问题与候选比较。

`Work-OS` 是本 Motion 起草阶段的临时工作名，不是最终 Stable token。Player 已选定 `RWS = rem Work System`，只用于 rem 内部概念，不主张成为通用行业标准；下方保留当时的候选比较与命名权衡。

关键区分：**Repo / SI / Player 是工作主体与场景前提；Player 已接受 `RWS = rem Work System` 与 `Ego/Rws.md` 为 canonical Work-System source，整合 RWB、Tools、Working；`Ego/RAP.md` 继续独立承载 RA rules。** 本地迁移与 source retirement 已完成；此接受不改变 Mission / EVAL、不验证 live SI runtime，也不增加 REM 第四组成部分。

## Current state vs. proposed target

| 项目 | 当前仓库事实 | 已批准目标 / 状态 |
| --- | --- | --- |
| Work-System 内容 | 起草基线由 RWB、Tools、Working 分别描述；旧 Tools / Working 正文见 [dated archive](../Ego/)。 | `Ego/Rws.md` 已由 Player 接受为 active canonical Work-System source；Tools / Working 原 `Ego/` 路径已移除。 |
| RA rules | `Ego/RAP.md` 是 RA rules 唯一源；SI 执行指令另在根 `AGENTS.md`。 | `Ego/RAP.md` 继续独立保留，不吸收入 RWS，也不由 RWS 取代。 |
| “RWS + RAP 两文件” | Ego 还包含 EGO quartet、Naming 等其他文件。 | 只表示 Work-System 与 RA-rules 两份相关主题文件，不是整个 `Ego/` 目录只剩两份文件。 |

起草基线的消费者包括根 `AGENTS.md`、`scripts/verify.py`、NP0 `runtime_snapshot.py`、Ego 导航、TeamSkill registry 与 README。启动 quartet、结构校验器、MPS source group、NP0 adapter/tests、Naming 与主要导航均已迁移；引用清点、source retirement 与测试结果见 [canonical Audit](../../../../Mission/Audit/2026-10-06-rws-work-system-migration.md)。当前无活动代码或主要导航消费旧来源。

## 三个工作前提

以下是本 Motion 对 Player 提供的 framing 的整理，不把比喻自动升格为事实或 authority：

1. **Repo 是智力工作的场所。** “where the brain is” 建议解释为 Repo 承载可回查、可治理的工作上下文、材料、决定、产物与 evidence。Repo 是外化的工作记忆与协作场所；它本身不推理，不等于 Player 的心智、SI 模型权重或完整组织记忆。
2. **SI 经 VS Code 对话/Agent 窗口进入工作现场。** 本 Motion 中的 SI 特指 Player 通过 VS Code 内的 AI 对话/Agent surfaces 使用的 assistant actor；当前 scope 以 Player 声明为准，包括原生 GitHub Copilot Chat（含 Copilot Enterprise 使用场景）、Codex、Claude Code 等相应窗口/客户端。窗口或客户端是工作入口，不等于底层 provider/model identity，也不证明 extension 安装、entitlement、availability、backend 或该次实际运行；这些仍按 task binding 分别核验。每次 action 仍受 Mission、permission、cost 与 evidence 边界约束。
3. **Player 以商务/专业工作主体进入。** Player 定义业务目标、任务、责任与验收结果；在 Work-OS 的默认分工中，Player 下达任务，SI 在获授 scope / permission 内完成程序实现与自动化工作，Player 判断并验收结果。这里包括流程自动化、Python 等程序、以及交付物中的 HTML / CSS 等程序工作。编程能力是 Work-OS 默认承载的基础设施能力，通常由 SI 运用；它不再是 Player 必须亲自承担的职业身份或最终业务目标。“超越程序员”指 Player 不必先成为程序员才能组织这类工作，不是对程序员作等级判断，也不排除程序员作为 Human 参与者。Player 的 authority 来自明确角色与 decision-rights，不单由职业称谓推导。

### SI 的 operational ontology（proposed）

Work-OS 不把 SI 当作一个身份固定、能力无限且随时可用的抽象“超级智能”。本 Motion 的 SI scope 是 VS Code 内 Player 使用的 assistant conversation / agent surfaces；概念上须区分 host interface、SI 工作角色与每项 bounded task 实际绑定的 Agent / Runtime instance。当前列举的 Copilot、Codex、Claude Code 是 Player 指定的 scope examples，不声明它们均已独立核实为已安装、可用或正在运行。至少梳理以下字段：

| Ontology area | Per-task binding | Boundary |
| --- | --- | --- |
| `Host / interface surface` | VS Code 内实际使用的对话窗口、client / extension 名称与可观察版本 | 窗口是交互入口；名称不证明底层 provider/model identity、subscription、entitlement 或本次实际调用。 |
| `Agent / role` | 承担的 SI 工作角色与责任边界 | 角色名不等于底层 model 或 provider identity。 |
| `Runtime instance` | 与该窗口关联的 provider、model / version，以及可观测的 runtime identity | 未暴露的 ID 明确记 `unknown`，不按窗口名称或 picker 猜测。 |
| `Access / entitlement` | 访问主体、订阅 / entitlement 状态与适用范围 | Player / 组织的访问权需有来源；不读取或记录 credentials / tenant secrets。 |
| `Capability / permission` | 此 runtime 实际可承担的任务类型、Tools / action scope 与授权 | 能力描述不自行授予权限；按 Mission 和 Tools 边界核验。 |
| `Budget / usage` | 任务 cost ceiling / cost basis、quota 或 usage / remaining（若可观测） | 未批准或未知的预算不能默认为零成本或可用。 |
| `Availability / execution state` | 带观察时点的可用状态，以及 configured、installed、selectable、selected、in-session、running、completed、failed、unavailable 等实际状态 | 已安装、picker 可见、已选中、当前会话与有证据的实际运行互不代证；状态会随时间变化。 |
| `Lifecycle / risk` | entitlement expiry、quota / rate limit、服务中断、account restriction / suspension 等已观察状态或待核风险 | 风险须标 source / time / status；`ban` 或停用风险未核验时写 `unknown`，不得陈述为已发生事实。 |
| `Evidence / provenance` | 来源、观察时间、实际结果、失败与验证路径 | 只留必要的非秘密证据；旧观察不自动证明当前可用。 |

因此，实际 SI 调用前需把 host surface、runtime identity、访问权、permission、预算和 availability / execution state 绑定到当前任务。任何必要项缺失时，按相关 authority stop / block；可提出获授权的核验步骤，但不自动换模型、provider、账号或付费路径。该 ontology 是 Work-OS 对 SI 的约束描述，不是 RWB / Tools / Working 之外的新维度，也不是当前设备 / entitlement / model 状态已验证的声明。

**Cross-source note:** 起草时的 RWB 正文写明“Claude Code 暂不在工作台内”，与 Player 对 SI 使用范围的最新声明不同。Player 已接受的 RWS scope 按其最新声明列入 VS Code 中的 Claude Code surface；旧 RWB 正文已退休且未作为独立文件接受，原始文本保留在 Git 历史，原路径现为非权威告示。

## Work-OS 三个维度

| 维度 | 在 Work-OS 中的作用 | Canonical source / boundary |
| --- | --- | --- |
| `RWB` | 计算环境与工作台：OS、VSC 及按需接入的 CLI 等运行底座。 | [RWS Workbench Substrate](../../../../Ego/Rws.md)；RWB 正文已退休。 |
| `Tools` | 可调用的动作能力；同时要求明确输入、permission、cost / side effect 与 result evidence。 | [RWS Tools and Permission](../../../../Ego/Rws.md)；登记不等于安装或单次调用授权；Tools 正文已退休。 |
| `Working` | 组织人、SI、Mission 与工具的任务方法：绑定 -> SI 执行（包括获授权的程序 / 自动化工作）-> evidence -> Human judgment -> EVAL / handoff / learning。 | [RWS Working Loop](../../../../Ego/Rws.md)；测试或渲染不能替代 Human acceptance；Working 正文已退休。 |

三个维度是互补视角，不是先后阶段：Working 组织任务如何使用 RWB 与 Tools；RWB 提供工作面，Tools 提供受控动作能力。编程是该工作面承载、由 SI 按任务调用的基础能力，不是另一个独立维度，也不自动产生 permission。RWS 是三个维度唯一 active canonical source；原路径上的 retirement notices 只维持历史链接，不增加新的 permission surface。

## Accepted Definition

> **RWS（rem Work System）**：rem 面向 Player 主导的专业知识与商务工作所采用的概念性运行框架。Repo 承载可治理、可回查的工作上下文；Player 定义任务与验收结果，SI 经 VS Code 内当前纳入 scope 的对话/Agent surfaces，以有 host、runtime identity、权限、预算、可用状态与 evidence 约束的实例，在授权范围内完成包括程序实现和自动化在内的工作；RWS 整合 RWB 底座、Tools 能力和 Working 闭环，RA rules 仍由独立的 RAP 规范。

这是对“Repo / SI / Player 三个跃迁”与“RWB / Tools / Working 三个维度”的合并解释。SI 的 ontology 约束每次 task binding；不能从“via VSC”推导当前 runtime、availability、entitlement 或预算。编程被视为 SI 可在获授权任务中运用的默认基础设施能力，Player 的主要责任是定义目标、下达任务并验收结果。它描述工作如何组织，不声称 Repo 是真正的大脑、VSC 自带超级智能，或 rem 提供了新的底层操作系统。

## Microsoft 的 work-OS 产品表述

2026-09-25，Microsoft CEO Satya Nadella 在 [X 帖文](https://x.com/satyanadella/status/2103455884366188544)中写道：**“We’re building Copilot as a new OS for work that spans every model, every form factor, and every task.”** 帖文随后把这项 Copilot 产品更新具体描述为 Autopilot、Code、Home（Chat + Cowork）、Office，并提到 Teams 调用与主动呈现 M365 信息的 Today。

**事实边界：**这是 Microsoft CEO 对 Copilot 产品方向的公开定位，说明“OS for work”这一说法已被用于 Copilot 的市场/产品 framing；它不是通用技术标准，也不证明 Copilot 当前已在所有 model、form factor、task 或 tenant 中普遍可用。“Every ...”在此按原帖的产品愿景措辞引用，不扩写成实测兼容性事实。

**与 rem 提案的区分：**Microsoft 的句子以 Copilot 产品体验为中心，强调跨模型、设备形态与任务的入口和集成；本 Motion 的 rem 概念以 Repo、Player、SI 的责任关系及 RWB / Tools / Working 为内部结构，还显式包含权限、预算、证据与 Human 验收。Copilot（及 Codex、Claude Code 等 VS Code 对话 surfaces）可以是 rem SI 的入口之一，但不是 rem 工作体系本身。本 Motion 不声称创造了“OS for work”这一通用说法，也不把 rem 概念称为 Microsoft Copilot 的延伸或替代品。

## 候选解释与选择

- **Candidate A - Work-OS as an integration concept（推荐）**：为 Repo-centered、Player-directed、SI-executed 的专业知识工作命名，并以 RWB / Tools / Working 三个维度说明其运行结构。Player 设定任务并验收结果；SI 以受 identity、access、permission、budget 与 runtime state 约束的实例完成授权工作。保留现有词的各自职责，补足它们之间的关系。
- **Candidate B - Work-OS as a rename of RWB（不推荐）**：会把 OS/VSC/CLI 工作台扩成方法、能力与责任框架，抹掉 RWB 与 Tools / Working 的边界；起草时的 RWB 本身为 Draft。
- **Candidate C - Work-OS as a fourth REM component（拒绝）**：与 `REM = Repo × EGO × Mission` 的现有定义冲突；Work-OS 不能变成 REM 的第四组成部分。

## Naming options（仅 rem 内）

`rem` 是 scope 前缀；以下候选只命名本产品内部概念，不代表通用行业分类或标准。Microsoft CEO 已用相近的“new OS for work”表述定位 Copilot；这令 `rem Work-OS` 更容易理解为类比，但也提高了产品联想与 OS 歧义。候选比较：

| Candidate token | 中文读法 / 记忆点 | Fit / friction |
| --- | --- | --- |
| `RWS`（`rem Work System`，Player-selected token） | rem 工作体系；RWS 作 EGO source filename/token，首次出现写出全名。 | 与现有 `RWB = Rem Workbench` 只差一个字母，口头/视觉易混；Player 本次选择此 tradeoff，source 中须明确区分。 |
| `rem Work System`（不设简称） | rem 工作体系；常用词，直接说明它组织一套工作的要素。 | 通俗、易记且避开 RWS/RWB 近似；token 较长。 |
| `rem Work-OS` | rem Work OS；突出“工作操作系统”隐喻。 | 好记并与 Nadella 的类比呼应；容易和 Microsoft Copilot 产品 framing、Windows/macOS 或底层 OS 混淆，需明确不是同一产品/标准。若选此全名，不应把它缩写成 `RWS`。 |
| `rem Work Framework` | rem 工作框架；强调由 RWB / Tools / Working 组成的整合框架。 | 边界中性；比 `System` 稍抽象，口语记忆摩擦略高。 |
| `rem Work Environment` | rem 工作环境；容易理解为人、SI 与工作条件所在环境。 | 读起来直观；容易被误解为只指设备/软件环境，从而与 RWB 混淆。 |

命名裁决：`RWS = rem Work System` 已按 Player 指令选定为 rem 内 Stable token。RWS/RWB 的字母近似作为已呈报 tradeoff 保留。`rem Work-OS` 仅作解释性类比，不作 canonical token。

## 已批准目标与执行步骤

按 Player 已批准的目标架构逐步执行，进度以 canonical Audit 为准：

- 已在 [Ego/Naming.md](../../../../Ego/Naming.md) 登记 `RWS = rem Work System`，作为名称索引与边界摘要。
- 已创建并由 Player 接受 `Ego/Rws.md`，现为 active canonical Work-System source，整合三份旧正文的仍有效内容并标注迁移来源。
- 已独立保留 `Ego/RAP.md` 为 RA rules 唯一 source，SI 执行指令仍在 `AGENTS.md`；RWS 不取代 RAP 或 `AGENTS.md`。
- 已迁移启动绑定、Ego 导航、结构校验器、MPS source group、NP0 `runtime_snapshot.py` 与 tests、TeamSkill registry、README 与 teamsbook review-source navigation；source-manifest target-delta hashes 按实际改动更新。
- 三份旧正文已退休；原路径只保留非权威告示，用于历史链接解析；原始版本留存在 Git 历史。
- 本 Motion 仅定义 SI ontology 的概念边界；不盘点或登记当前账号、订阅、provider、模型、预算、使用状态或封号风险。任何 live SI registry、availability probe 或 account-risk monitoring 均需另行定义 scope / permission / evidence。

Initial Draft review did not itself admit a concept or change authority. The Player's later execution approval and selected target are recorded below; final source retirement still depends on consumer migration and verification.

## Initial Draft Scope (superseded by execution approval)

**当前授权仅包括：**

- 起草本 Motion，梳理 Work-OS 的概念候选、三前提、三维度、边界、反例与建议落点。
- 在本 Motion 中提出一个可供 Player 反驳或接受的候选定义。

**不包括：**

- 本轮直接修改 `Ego/Naming.md`、`Ego/Ego-rem.md`、RWB / Tools / Working 正文或其他 authority source。
- 将 Work-OS 注册为已接受名称、分配 Naming ID、改变 REM 定义或写入新的权限。
- 接受 `Ego/Rwb.md` Draft，验证或宣称 SI/model/provider 实际运行，或改变 Mission / EVAL。
- 新建 AgentSkill、调整 `AGENTS.md` / RAP、安装工具、调用外部/付费能力、commit 或 push。

## Runtime Permission

初始 Draft 授权只覆盖概念梳理。Player 后续明确批准 Motion 并要求开始 stepwise execution；该授权范围见下方 Execution Scope 与 canonical Audit。

## Execution Scope - 2026-10-06

Player 当前对话“批准Motion, 开始执行, 一步一步的”批准以 `RWS = rem Work System` 为 Stable token，执行 RWS/RAP 目标架构。此 amendment 覆盖初始 Draft-only scope 与相冲突的 out-of-scope 项，仅授权以下本地变更：

1. 创建 `Ego/Rws.md`，整合 RWB、Tools、Working 的有效内容与边界，并清楚标记来源、状态、permission / evidence 限制。
2. 更新 `Ego/Naming.md`、`Ego/Ego-rem.md`、`AGENTS.md`、README 与 EGO quartet / RWS 导航，使 RWS 成为 Work-System source、RAP 继续独立。
3. 迁移结构校验器、NP0 runtime snapshot adapter/tests、TeamSkill registry 与其它已核实的直接消费者；只按实际变更更新 fixtures 和 source-manifest target-delta hashes。
4. 在消费者和验证全部迁移通过后，才退休 `Ego/Rwb.md`、`Ego/Tools.md`、`Ego/Working.md`；不提前删除或覆盖未知内容。
5. 分阶段运行 relevant checks，结果记入 [canonical Audit](../../../../Mission/Audit/2026-10-06-rws-work-system-migration.md)。

边界：RWS 描述工作系统，不取代 RAP 规则、不改变 Mission/EVAL、不新增 permission。SI 账号/runtime、entitlement 或预算不在本次核验。外部/付费动作、安装、部署、commit 与 push 均未获授权。

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | Repo、SI/VSC、Player 三项被清楚写成概念前提；SI role 与 Runtime instance 分开，不把未核验状态写成事实 | Player review；ontology fields、来源与 unknowns 清楚标注 |
| D2 | RWB、Tools、Working 三维度各有唯一 source、职责和边界；与三项前提不混为一组 | 命名表述及本 Motion 链接 review |
| D3 | Work-OS 明确不是实际 OS、字面“大脑”、REM 第四组成部分、RWB 改名或授权来源 | Definition / Boundary review |
| D4 | canonical Work-System source 为 `Ego/Rws.md`、Stable token 为 `RWS = rem Work System`、RA rules source 保持 `Ego/RAP.md`；所有消费者迁移后才退役旧来源 | consumer inventory；迁移 diff / tests / pins；`uv run python scripts/verify.py` pass |
| D5 | 未把 Motion Draft、结构测试或 SI 说法升级为概念 acceptance、产品 EVAL 或实际模型证据；availability / in-use / completed 不互相代证 | Audit / status review；Human gates 与有时点的 runtime evidence 独立留证 |

## Decision Record - 2026-10-06

Player approved this Motion for stepwise execution. For this execution, the approved target is `RWS = rem Work System`, scoped to rem; `Ego/Rws.md` is the canonical Work-System source, `Ego/RAP.md` remains the independent RA rules source, and `Ego/Naming.md` / `Ego/Ego-rem.md` provide naming and navigation. “RWS + RAP” identifies these two related subject files, not the only files under `Ego/`.

The approved content framing treats Repo as governed work context (not a literal brain), Player as task/decision-rights holder and result acceptor, and SI as the authorized executor of code/automation work. RWB, Tools, and Working are complementary dimensions consolidated under RWS, not a fourth REM component.

Player later reviewed and accepted the current `Ego/Rws.md` as canonical Work-System source and explicitly authorized retirement of the three former source bodies. That bounded acceptance does not imply product EVAL completion or prove any live SI/runtime status. The canonical Audit is the execution and source-retirement record.

## Closeout / History Triage

Player review、consumer audit、source retirement 与相关 checks 均已记录；Motion `Done`。History Triage 为 `Audit First`：记录的是 Player 对 rem Work-System canonical source 的有界接受，不推导产品 EVAL、真实 runtime / model availability 或额外 permission。Motion source 已按 motioner 路由归档到 `Repo/days/2026-10-06/Motion/`。
