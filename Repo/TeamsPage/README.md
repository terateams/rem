# rem TeamsPage custody

`Repo/TeamsPage/` 是 rem 内生 HTML review artifact 的 canonical custody，不是用户外部产品。目录同时保存 Narrative Pages（影页）和确定性 MPS artifacts；两者均 non-authority/no-writeback，但来源与验证格式不同。MPS artifact 的 `#mp-data` 保存 source bytes/hash/revision 与 gates，可确定性重建；Narrative Page 没有 `#mp-data`，回到显式来源核对。

四个 2026-09-30 MPS 快照原字节迁入后曾保持冻结；当前工作树已将它们从 live custody 移除，Git 历史仍保留原件。迁移前的相对源链接已 stale，代表性 MPS deterministic rerender 检查也不通过；它们不作为当前 review 页面或导航。新 review 应基于显式获准、已审查的 Mission source group 生成。

生成后使用 `python .agents/skills/teamspage/MPS/scripts/mps.py --repo . --artifact <path>` 独立验证。Human review / Model runtime / 任务完成分别留证；旧 source 变化会 stale。清理需保留不可替代 evidence，不自动删除。

## Narrative Page（影页）

影页是 SI 基于 Repo 实况叙事生成的 HTML 页，可由 VS Code Copilot 或 Codex 生成，并与确定性 MPS artifacts 共用本目录，但不是 MPS artifact。叙事不是事实，non-authority/no-writeback。页头必须写明来源文件与提交哈希、生成工具与版本、日期；来源变更后即过期。文件名用英文，页面离线可读，不加载外部脚本或字体。影页没有 `#mp-data`，不使用 `mps.py` 验证；由 Human 回到来源核对。当前影页：[rap-teamspage.html](rap-teamspage.html)（`Ego/RAP.md`）；[agents-teamspage.html](agents-teamspage.html)（`AGENTS.md`）；rem-ready：[rem-ready-teamspage.html](rem-ready-teamspage.html)（`.agents/skills/rem-ready/SKILL.md`）。

### rem-ready Run Receipts

Each readiness assessment may create a unique `Repo/TeamsPage/rem-ready-run-<YYYYMMDDTHHMMSS>.html` paired with `Mission/evidence/rem-ready-<YYYYMMDDTHHMMSS>.json`. Create receipts for `READY`, `READY_WITH_LIMITS`, and `BLOCKED` only after any required ANDON path is resolved and local writing is permitted. Do not create either receipt during an unresolved write-prohibiting ANDON. The JSON record and its referenced observations carry the evidence; HTML is only a visual index. Do not overwrite receipts. These files are Narrative Page evidence indexes, not MPS artifacts; do not use `scripts/mirror.py`.

[Runtime contract](../../.agents/skills/teamspage/references/teamspage-runtime-contract.md) · [Motion custody](../Motion/README.md)

<!-- teamspage-index:start -->
## Generated TeamPage MPS Snapshot Index

| Target | Latest | Generated At | Snapshot | Previous | Source Check | Human Review | Agent Review | Provenance |
| ------ | ------ | ------------ | -------- | -------- | ------------ | ------------ | ------------ | ---------- |

<!-- teamspage-index:end -->
