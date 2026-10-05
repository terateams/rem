# Motion: Active Motion Custody Path Alignment

> **Date**: 2026-10-05
> **Owner**: yangjun / bitguts
> **Status**: Done
> **Updated**: 2026-10-05
> **Execution Audit**: [canonical Audit](../../../../Mission/Audit/2026-10-05-motion-custody-path-alignment.md)
> **Type**: repository structure / path alignment
> **Service Object**: rem Motion lifecycle source path
> **Primary Route**: [Story-rem](../../../../Mission/Story-rem.md) -> [EVAL](../../../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Owner 当前对话：“将Motion, 移动到了Repo下, 据此生成Motion, 对齐整个rem”
> **Round**: R1

## 问题与拟议裁决

当前工作树已将 active Motion 工作面放在 `Repo/Motion/`，但 README、motioner skill、结构校验器及既有 Motion/Audit 链接仍有 `Repo/shape/Motion/` 或旧相对路径。现有 `python scripts/verify.py` 因此报告缺失路径与无效链接。

本 Motion 将 active Motion source 的 canonical path 对齐为 `Repo/Motion/`。已完成来源仍按既有生命周期规则退役至 `Repo/days/<closeout-date>/Motion/`；TeamsPage 继续位于 `Repo/shape/TeamsPage/`。

## 范围

**当前对话授权范围：**

- 保留工作树中已发生的 `Repo/shape/Motion/` -> `Repo/Motion/` 移动，不重新移动或暂存文件。
- 对齐 Motion README、motioner skill route、`scripts/verify.py` required path，以及现存 Motion 与 canonical Audit 的链接。
- 运行 rem 结构 / Markdown link 校验和工作区 diff 检查。

**不纳入：**

- 修改 `Ego/Rap.md` 或其他无关工作树改动。
- 刷新 `Repo/today.md` / `Repo/now.md`、修改 Mission/EVAL 判据、归档其他历史 Motion、提交或推送。
- 变更 TeamsPage 资产、上游源、外部资源、凭据、模型或权限。

**Owner closeout approval - 2026-10-05：**

- Owner 当前对话：“批准, 执行, 校验后退休”，授权在校验通过后退休本 Motion source；不扩展到其他 Motion、每日 handoff 刷新或 commit/push。

## Runtime Permission

Owner 原始请求授权本 Motion 所列的本地文档 / 校验器路径对齐，不构成 durable `Approved` 状态。Owner 后续明确批准执行校验并在通过后退休本 source；该批准不授权提交、推送、每日 handoff 刷新或其他外部动作。开始核验时，目录移动已作为未暂存 worktree 状态存在；本次保留该状态。

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | active Motion canonical path 登记一致为 `Repo/Motion/`；历史 retirement 路径保持不变 | authority / skill / README / verifier 搜索结果 |
| D2 | Motion、Audit 与 README 的本地 Markdown 链接均可解析 | `python scripts/verify.py` pass |
| D3 | 无关未跟踪文件与既有用户改动未被覆盖或暂存 | 最终 `git status --short` |

## Landing / Rollback

Active source path 为 `Repo/Motion/`；已完成 Motion 的 closeout custody 保持 `Repo/days/<closeout-date>/Motion/`。若需回退，仅新增反向路径与引用变更，不丢弃或重写已有工作树 / Git 历史。

## Execution Result - 2026-10-05

Motion README、motioner route、结构校验器及既有 Motion/Audit 链接已对齐到 `Repo/Motion/`。Owner 批准后，`python scripts/verify.py` 与 `bash scripts/ra-check.sh` 均通过；归档后的路径校验及 source retirement trace 见 canonical Audit。Motion 已完成并退休。
