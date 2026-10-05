# rem RAP（Rem Agent Protocol）

> **Owner**: yangjun / bitguts
> **Status**: active
> **Version**: 0.6.1（采用版本；与 `scripts/ra-check.sh` 的 `RA_VERSION` 一致）
> **Freshness**: 2026-10-05

**Reader**: 商务人士与 Human 参与者。SI Agent 读 [AGENTS.md](../AGENTS.md)，不读本文件。

RA仓规是 rem 里 Agent 配置的规则：有哪些指令文件、技能放在哪里、如何检查。RA = Rem Agent。RAP 是它在本 repo 的人读说明；规则的唯一载体是 `AGENTS.md`。RAP 不是 REM 的第四组成部分，不赋权，不替代 Mission / EVAL。

本文件只记录采用版本与落地位置。规则全文、来源与审计见上游规范：[RA仓规 HTML](https://claude.ai/artifact/QRffFZS2MwvYBLGvYmd2sH)。上游规范领先本 repo；两者不一致时，本 repo 向上游对齐。

## 落地位置（Landing）

| 要素 | 位置 | 状态 |
|---|---|---|
| 唯一指令文件 | [AGENTS.md](../AGENTS.md) | 已落地 |
| 技能 | `.agents/skills/<name>/SKILL.md` | 已落地；`Ego/TeamSkill/*/SKILL.md` 不是技能，待 Owner 决定改名 |
| 静态检查 | `sh scripts/ra-check.sh` | 已落地 |
| CI 门禁 | `.github/workflows/ra-check.yml` | 已落地；Actions 结果由 Owner 核验 |
| 硬性安全规则的钩子 / CI | 未建 | pending |
| 验收测试记录 | `Mission/evidence/` | not_run |
| 模板仓库设置 | GitHub “Template repository” | 由 Owner 核验 |

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
