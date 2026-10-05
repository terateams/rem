# rem RAP（Rem Agent Protocol）

> **Player**: yangjun / bitguts
> **Status**: active
> **Version**: 0.6.6（与 `scripts/ra-check.py` 的 `RA_VERSION` 一致）
> **Freshness**: 2026-10-05

**Reader**: Player（商务人士与 Human 参与者）。SI Agent 平时读 [AGENTS.md](../AGENTS.md)；修改 Agent 配置时读本文件。

RA = Rem Agent。RA仓规是 Agent 配置的规则集，本文件（RAP）是它的**唯一规则源头**。RAP 不是 REM 的第四组成部分，不赋权，不替代 Mission / EVAL。给 SI 执行的那部分规则写在 `AGENTS.md`。

RA仓规的 HTML 页是本文件的影页（Narrative Page）：叙事不是事实，只说明本文件；两者不一致以 RAP 为准。当前影页：`Repo/TeamsPage/rap-teamspage.html`（离线可读；不写成链接，因为 `verify.py` 的测试夹具会排除 HTML）。

## 范围（Scope）

- RA仓规是单个 REM 仓库中 SI Agent 的工作规则；它说明 Agent 如何在仓库中工作，不定义 REM 方法本身。
- REM 是方法与模板，当前仍在完善中；RA仓规领先 REM。两者有差异时，REM 按 Player 决定修订。RAP 是规则源，影页跟随 RAP。
- 工作台是 VS Code、Copilot 与 Codex。Claude Code、Visual Studio、JetBrains、Xcode、Eclipse 与其它工具不在当前范围内。
- 范围内包括 VS Code 中的 Copilot、GitHub Copilot Enterprise 与 Codex。RA仓规服务商务人士，不覆盖程序员工作场景，例如代码审查、Copilot CLI 或构建工具。
- 操作系统与 terminal 基线见 [RWB](Rwb.md)。RWB 是工作台说明，不是 REM 第四组成部分、指令文件或权限来源。

## 规则（Rules）

| # | 规则 | 来源 |
|---|---|---|
| 1 | `AGENTS.md` 是仓库根目录唯一的指令文件。 | Player 决定。VS Code、Codex、cloud agent 都读它：[VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions)、[Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md)、[cloud agent](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/) |
| 2 | 不保留 `.github/copilot-instructions.md` 和 `.github/instructions/`。 | Player 决定：一个文件，一个事实源。二者是 Copilot 文件：[support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support) |
| 3 | 不用嵌套的 `AGENTS.md`，只用根目录一个。 | VS Code 中嵌套文件是实验性且默认关闭：[docs](https://code.visualstudio.com/docs/agent-customization/custom-instructions) |
| 4 | Copilot 组织级指令只放全组织规则，不放 REM 规则。 | Player 决定。优先级最低：[GitHub docs](https://docs.github.com/en/copilot/concepts/prompting/response-customization)；适用于 github.com 界面：[changelog](https://github.blog/changelog/2026-04-02-copilot-organization-custom-instructions-are-generally-available/) |
| 5 | 指令是建议，钩子才是执法。硬性安全规则（保护凭证、阻止破坏性操作）写进钩子或 CI 门禁，不靠 `AGENTS.md`。 | 钩子是 `.github/hooks/*.json`：[cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)。上下文大时模型可能忘记指令：SI 判断 |
| 6 | 使用 Codex 26.930.31730 或更高版本。 | Player：2026-10-03 发布 |
| 7 | 默认不建技能。某个 REM 步骤重复出现、需要脚本或模板时再加。 | SI：先做最小可用版本 |
| 8 | 每个技能（AgentSkill）放在 `.agents/skills/<name>/SKILL.md`，不建其他技能目录。例外：`Ego/TeamSkill/<name>/SKILL.md` 是 REM 的 TeamSkill 说明，不是技能，工具不会加载它；路径被固定的上游代码引用（`mps.py`），保留。除这两处，不许出现 `SKILL.md`。 | 两个工具都读 `.agents/skills/`（SI 判断：文档没有把 `Ego/` 列为扫描路径）。`ra-check` 检查这条：[VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills)、[Codex](https://learn.chatgpt.com/docs/build-skills) |
| 9 | 技能 `description` 不超过 1024 字符，写明功能、触发条件、排除条件；`name` 与目录名一致。 | 上限与命名：[VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills)。触发词放前面：[Codex](https://learn.chatgpt.com/docs/build-skills)。排除条件：SI 判断 |
| 10 | 验收测试先在 VS Code 做，再在 Codex 做。 | Player 决定。VS Code 1.140 于 2026-09-30 发布：[release notes](https://code.visualstudio.com/updates) |
| 11 | 每次合并前 `ra-check` 必须通过，并在 CI 运行。 | SI：把规则 5 用于规则集本身 |
| 12 | 每个新的 REM 仓库从 RA 模板（`terateams/rem`）创建，创建时即部署 RA仓规。 | Player 决定。模板仓库复制文件并只有一个初始提交：[GitHub docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) |
| 13 | `AGENTS.md` 先写给 SI：硬边界在前，运行环境在后。给人看的说明放在本文件。规则源头是本文件。所有文件名用英文。 | Player 决定。章节顺序：SI 判断。`ra-check` 只检查 `Ego/RAP.md` 存在，章节顺序由人检查 |

## 落地位置（Landing）

| 要素 | 位置 | 状态 |
|---|---|---|
| 规则源头 | 本文件 | 已落地 |
| 唯一指令文件 | [AGENTS.md](../AGENTS.md) | 已落地 |
| 技能 | `.agents/skills/<name>/SKILL.md` | 已落地；`Ego/TeamSkill/*/SKILL.md` 是 TeamSkill 说明，按规则 8 例外保留 |
| 静态检查 | `uv run python scripts/ra-check.py` | 已落地 |
| CI 门禁 | `.github/workflows/ra-check.yml` | 已落地；Actions 结果由 Player 核验 |
| 硬性安全规则的钩子 / CI | 未建 | pending |
| 验收测试记录 | `Mission/evidence/` | not_run |
| 模板仓库设置 | GitHub “Template repository” | 由 Player 核验 |

## 与 REM 的矛盾（Contradictions）

RA仓规领先 REM：两者不一致时，REM 改。下表保留以 `df022f4` 为基线的历史项；本次活动文件复核基线为 `f192d17`，具体修订见当前 Motion 与 Audit。

| # | 矛盾 | 处理 | 状态 |
|---|---|---|---|
| 1 | `AGENTS.md` 把给人看的内容放在前面 | 改为 SI 优先：硬边界在前，运行环境在后 | 已解决（补丁） |
| 2 | 仓库部分活动文件用 Owner，RA仓规用 Player | 本次对齐列明的活动文件；历史记录与哈希锁定文件保留当时用词 | 已解决（本次对齐） |
| 3 | 镜页与影页 | 活动说明统一使用 Narrative Page / 影页；确定性 MPS artifact 与历史来源保持各自边界 | 已解决（本次对齐） |
| 4 | 已退役权威文件的残留：`eval-rem-v1` A1 的 RCI、`TeamSkill/rem` 的 AI仓规、`looper` 的 RCI | 改为现行名称 | 已解决（补丁） |
| 5 | 规则 8 与 `Ego/TeamSkill/*/SKILL.md` | 规则 8 加 TeamSkill 例外（REM 自己区分 TeamSkill 与 AgentSkill，`mps.py` 固定引用该路径）；`ra-check` 拒绝其他位置的 `SKILL.md` | 已解决（补丁） |
| 6 | TeamsPage 目录说明只讲镜页 | `Repo/TeamsPage/README.md` 增加影页说明 | 已解决（补丁） |
| 7 | 规则 5：没有钩子，也没有凭证扫描 | 未建。Player 先定哪些规则是硬性的 | open |
| 8 | Naming 要求新名字走 Player Motion | RWB 名称经本次 Player 修订 Motion 授权 | 已解决（本次 Motion） |
| 9 | RAP 缺少 Scope，旧影页含有未由 RAP 约束的范围段落 | 将有来源的范围陈述写入 RAP，并让影页跟随 RAP；OS / terminal 基线指向 RWB | 已解决（本次修订） |

## 验收测试（LANTERN）

1. 在 `AGENTS.md` 临时加一行：`End each answer with the word LANTERN.`
2. 在 VS Code Copilot Chat 问一个问题。回答必须以 LANTERN 结尾。
3. 在 Codex 重复一次。
4. 删除该行，不提交。
5. 在 `Mission/evidence/` 记录：工具与版本、日期、结果。未跑写 not_run。

回答不以 LANTERN 结尾，说明该工具没有读取 `AGENTS.md`。

## 边界（Boundary）

- 不新增第二个指令文件。
- RAP 与 RAM 只差一个字母。RAM 是 NP0 里的 `EGO × Mission × Repo` 方法名，见 [capsule](../.agents/skills/np0/references/np0-axiom-capsule.md)。