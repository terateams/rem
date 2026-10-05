# rem Skill Deployment / Provenance

Source=`terateams/EGO-T189` commit `70090b756d2c4f4e75912ec9f3ede2ff3e8cc0a0`。Player 在当前会话批准 target architecture / creation / initial commit-push，明确 Private、独立新历史、D:\Github\rem、TeraTeams持有、bitguts Player、授权材料/必要证据保留与org默认访问。

## 能力清单

| Capability | Identity / carrier | Disposition | Authority / source | Target delta / validation | Rollback / gate |
|---|---|---|---|---|---|
| Narrative / naming / bounded action | np0 | adapt-for-target | source package + unchanged canonical capsule | target wrapper / binding，capsule hash parity、generic snapshot tests | target baseline；上游公理改动另 gate |
| startup / pause | rem-ready | adapt-for-target | source skill workflow / complete REM | no T189 defaults；实际日期/git/cursor/permission核验 | 不覆盖未知游标；sync/config另 gate |
| Motion lifecycle | motioner | adapt-for-target | source Motion Lifecycle semantics | finite statuses / runtime approval / landing / retirement，target wrapper | canonical trace留存，非显然 admission Player |
| maintenance / feedback | looper | adapt-for-target | source portable maintenance contract | target report-first / no CRAFTS resolver / bounded fixes | rollback source pin；authority/external/cost另 gate |
| built-in deterministic MPS artifact | teamspage | adapt-for-target | generic MPS original engine / runtime contract | explicit Mission-group adapter / all selected source lines / voice/provenance / rebuild/freshness | fixed engine pin；new snapshot不覆盖，source不写回 |
| subscription / two workloads | Human + VSC/Copilot | target configuration, no new Skill | Player declaration / runtime gates | Sol Mission；Luna self；actual runs not inferred | no automated picker/billing change；fallback另批 |
| task actions / Tools evidence | Human/generic Agent + deterministic tools | target capability binding | approved scope / Mission/EVAL | actual verify tool evidence、source changes、new snapshot；真实任务验收另判 | no unapproved cloud or irreversible action |

identity_gap_count=0 identified；Skill adaptation_work_count=5；provider_route_count=0 installed；Human gate groups=2；deterministic tool groups=4。Five packages不是完整技能行为benchmark；静态metadata/discovery、target runtime smoke和negative fixtures必须分别说明局限。

## 原样与适配分开

[source-manifest.json](source-manifest.json) 记录五项原样 bytes/hash，以及四项 target deltas。NP0 runtime snapshot 与配套 tests 只适配目标 `Ego/` 路径；MPS 的 `mps.py` 与 runtime contract 记录当前 `Ego/` / `Repo/TeamsPage/` 路径，allocator 扫描当前 custody 和迁移前的大小写路径以保留 Git 历史编号。其余 MPS engine manifest/loader/template 与 generic MPS tests 保持原样。target delta hashes 与理由均入 manifest 并由 `scripts/verify.py` 检查。没有复制 source mps_crafts.py、MPV pilot、T189 fast registry、业务包、历史、Dojo、用户配置、.venv或credentials。

源 generic MPS 可描述 CRAFTS / NP0 alternatives，但目标 adapter只构造 namespace=REM、selected_method=null、不提供projection_sources；该 dormant code不是 target active domain dependency。原样文件中的历史词条 / 来源出处不冒称 target runtime fact，也不对原样代码作全词机械替换。

五项 SKILL wrappers 重新绑定目标，属于 adaptation 而非原版 hash parity。各 wrapper覆盖 trigger正例/排除项、permission/stop、target paths和工作流程；独立 with/without-skill agent benchmark未运行，不能把loader能发现当作全部行为等价。

## Access / license / retention

Private，org 默认可继承访问，不另授用户/团队权限。目标责任与访问由 Player 确认。Source pin没有root LICENSE；此处只有Player授权的私有派生，不发明开源许可、不publish或宣称第三方材料可无条件分发。公开或commercial发布须另审source package/license/notice与distribution许可。

原件、必要审批与行动证据保留；影页与确定性 MPS artifact 是阶段性 HTML review artifacts，来源变化后各自 stale，清理需要 owning review closeout，唯一 evidence 不自动删除。source unchanged pins在需要升级时走Motion/source delta/tests。

## 验证与回退

`uv run python scripts/verify.py`：target结构/links/source pin；`uv run python -m unittest discover -s scripts -p "test_*.py"`：adapter负例与MPS rebuild/freshness；原样NP0 snapshot suite独立执行。它们不证明actual model ID、Human acceptance、不同Human对齐或完整real任务。

目标初始commit作为rollback point。软件后续改动保留diff/test/evidence；未批准不reset/rewrite/delete远端，不撤销Player权限或订阅。模型picker/config/账号与外部tool副作用不能由本地Git回退冒称已撤销。
