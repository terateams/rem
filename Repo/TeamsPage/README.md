# rem Mirror Page custody

HTML 镜页是 rem 内生功能；`Repo/TeamsPage/` 是 canonical custody，不是用户外部产品。页面 non-authority/no-writeback，`#mp-data` 保存来源 bytes/hash/revision 与 gates，HTML 可确定性重建。

现存四个 2026-09-30 快照从旧 custody 原字节迁入，内容保持冻结；其来源路径和相对链接已 stale，不能作为当前 review 页面或导航使用。迁移未改写或重生成这些 HTML；代表性 MPS deterministic rerender 检查仍不通过。新 review 应基于显式获准、已审查的 Mission source group 生成。

生成后使用 `python .agents/skills/teamspage/MPS/scripts/mps.py --repo . --artifact <path>` 独立验证。Human review / Model runtime / 任务完成分别留证；旧 source 变化会 stale。清理需保留不可替代 evidence，不自动删除。

[Runtime contract](../../.agents/skills/teamspage/references/teamspage-runtime-contract.md) · [Motion custody](../Motion/README.md)

<!-- teamspage-index:start -->
## Generated TeamPage MPS Snapshot Index

| Target | Latest | Generated At | Snapshot | Previous | Source Check | Human Review | Agent Review | Provenance |
|---|---|---|---|---|---|---|---|---|
| [rem - 产品工作面评审](MPS-260930S3004-rem-instance-rem.html) | yes | 2026-09-30T01:43:49+00:00 | 49712a58 | [ba20de8d](MPS-260930S3003-rem-instance-rem.html) | not_run | not_run | not_run | embedded #mp-data |
| [rem - 产品工作面评审](MPS-260930S3003-rem-instance-rem.html) | no | 2026-09-30T00:32:20+00:00 | ba20de8d | [7be0bdc6](MPS-260930S3002-rem-instance-rem.html) | not_run | not_run | not_run | embedded #mp-data |
| [rem - 产品工作面评审](MPS-260930S3002-rem-instance-rem.html) | no | 2026-09-30T00:31:26+00:00 | 7be0bdc6 | [e915eedf](MPS-260930S3001-rem-instance-rem.html) | not_run | not_run | not_run | embedded #mp-data |
| [rem - 产品工作面评审](MPS-260930S3001-rem-instance-rem.html) | no | 2026-09-30T00:29:39+00:00 | e915eedf | none | not_run | not_run | not_run | embedded #mp-data |
<!-- teamspage-index:end -->
