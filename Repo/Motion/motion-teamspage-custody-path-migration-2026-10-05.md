# Motion: TeamPage Custody Path Migration

> **Date**: 2026-10-05
> **Owner**: yangjun / bitguts
> **Status**: Executed
> **Type**: repository structure / asset custody path migration
> **Service Object**: rem Mirror Page custody
> **Primary Route**: [Story-rem](../../Mission/Story-rem.md) -> [EVAL](../../Mission/EVAL/eval-rem-v1.md)
> **Source Request**: Owner 当前对话：“TeamsPage提升到Repo下, 同时取消了Shape的子目录, 给出判断后, 全Repo对齐”
> **Execution Audit**: [canonical Audit](../../Mission/Audit/2026-10-05-teamspage-custody-path-migration.md)
> **Round**: R1

## 问题与拟议裁决

工作树已将 `Repo/shape/TeamsPage/` 搬至 `Repo/TeamsPage/`，且 `Repo/shape/` 不再存在；skill、MPS runtime、manifest、tests 和导航仍登记旧 custody。当前 `python scripts/verify.py` 因必需路径与链接仍旧而失败。

将 `Repo/TeamsPage/` 定为唯一活动 Mirror Page custody，与 `Repo/Motion/` 同级；不重建 `Repo/shape/`。旧目录只作为 MPS Git 历史扫描输入及 dated records 的历史事实保留。

四个 2026-09-30 HTML 快照原字节搬迁，不手改、不重建。它们已 stale：原相对源链接在新深度下失效，且代表性 MPS deterministic rerender 报 mismatch；README 标明其不可作为当前 review 或导航。后续新页面须使用显式获准、已审查的 Mission source group 生成。

## 范围

**当前 Owner 指令授权：**

- 保留已发生的 `Repo/shape/TeamsPage/` -> `Repo/TeamsPage/` 搬迁。
- 对齐活动 custody 路由、MPS 默认输出 / 索引 / export、离线源链接深度、历史 G-ID 扫描、TeamSkill registry、source manifest、tests、verify 与 README。
- 保留旧 Git history scan 路径及历史 Audit/evidence 叙述；仅更新活动导航，不回写历史事实。
- 运行结构、MPS tests、source pin、仓规及 frozen HTML 字节校验。

**不纳入：**

- 编辑或重建已有冻结 HTML；这次不创建新的 review page。
- 改写 dated records 中的旧路径观察、Mission/EVAL 判据或 Human review 结果。
- 修改 `Ego/Rap.md`、刷新 `Repo/today.md` / `Repo/now.md`、提交或推送。

## Runtime Permission

Owner 当前对话明确要求对 `Repo/TeamsPage/` 搬迁做判断并全仓对齐，授权本 Motion 范围内的本地路径、skill、adapter、test、manifest 与导航修订。该指令不授权重建冻结镜页、commit/push 或修改排除项。

## EVAL

| Gate | 判据 | 必需证据 |
| --- | --- | --- |
| D1 | 唯一活动 custody 为 `Repo/TeamsPage/`，`Repo/shape/` 不存在；旧路径仅留作 history / provenance | 全仓路径搜索与目录检查 |
| D2 | required paths、Markdown links 与 source pins 通过 | `python scripts/verify.py` |
| D3 | MPS allocator / output / retired-path guard 行为正确 | `python -m unittest discover -s scripts -p "test_mirror.py"` |
| D4 | 四个既有 HTML bytes 不变且 stale 边界清楚 | frozen blob comparison、README 和 Audit |
| D5 | 无关用户改动未覆盖，未 commit/push | 最终 `git status --short --branch` |

## Landing / Rollback

活动 custody 为 `Repo/TeamsPage/`；生成页面从该目录及允许的 flat `Repo/Dojo/` 产出。MPS allocator 同时扫描当前路径和两个迁移前历史路径，避免复用 G-ID。若需回退，以新变更恢复先前 custody 与 adapters；不重写 Git history 或覆盖冻结页面。

## Execution Result - 2026-10-05

活动路由已对齐，`Repo/shape/` 不存在；旧路径仅保留在 Git 历史扫描、回归测试和 dated history 中。四个 HTML 快照 blob 与迁移前完全一致。

- `python scripts/verify.py`: `structure=pass`, `failures=[]`。
- `python -m unittest discover -s scripts -p "test_mirror.py"`: 16/16 pass。
- `bash scripts/ra-check.sh`: `RA仓规 0.6.1: OK`。
- `git diff --check`: 无 whitespace errors；Git 对 `Repo/days/README.md` 提示 CRLF/LF 归一化。

四个冻结 HTML 未编辑或重建；代表性 MPS validator 与新 renderer 不匹配，移动后其旧相对链接不再解析，已在 custody README 标明 stale。Owner acceptance pending；本次未刷新 daily handoff、未提交或推送。
