# rem Mirror Page custody

HTML 镜页是 rem 内生功能；目录名仅复用 source runtime convention，不是用户外部产品。页面 non-authority/no-writeback，`#mp-data` 保存来源 bytes/hash/revision 与 gates，HTML 可确定性重建。

生成后使用 `python .agents/skills/teamspage/MPS/scripts/mps.py --repo . --artifact <path>` 独立验证。Human review / Model runtime / 任务完成分别留证；旧 source 变化会 stale。清理需保留不可替代 evidence，不自动删除。
