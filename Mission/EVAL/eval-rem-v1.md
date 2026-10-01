# EVAL - rem V1.0

> **Owner**: bitguts
> **Status**: in-progress
> **Source**: Owner 已批准的 EGO-T189 rem bootstrap Motion A1-A13；见 [bootstrap](../Audit/2026-09-30-bootstrap.md)

## 阶段边界（Owner-approved scope split）

Owner于2026-09-30当前会话明确“批准一次范围拆分”。bootstrap R1按独立创建/软件基线交付/验证交接清单收口；本EVAL仍持全部A1-A13产品判据，不删除、不降级、不自动通过真实Human/model/task要求。后续工作见 [runtime validation plan](../../Repo/days/2026-09-30/plan-runtime-validation.md)。R1关闭不等于本EVAL完成或V1.0release。

独立VSC启动与Luna picker证据见 [startup observation](../evidence/2026-09-30-vsc-startup.md)；这是实际startup smoke与UI观察，不是全部技能加载/backend model/full双场景归因。

| ID | Criterion | Required evidence | Status |
| --- | --- | --- | --- |
| A1 | EGO / one Primary / EVAL / RCI / VSC binding | target structure and authority checks | machine_pass / independent VSC startup observed / full behavior pending |
| A2 | independent target, no T189 / CRAFTS active dependency | allowlist / pins / dependency / negative probes | machine_pass |
| A3 | explicit group, revision/hash/dirty/scope/omissions | target adapter and negative tests | machine_pass |
| A4 | built-in offline HTML Mirror Page, rebuild/freshness/voice/ID | actual target artifact + validator | machine_pass / Human review separate |
| A5 | Agent output evaluated against bound Mission | actual Human accept / correct / reject, evidence | not_run |
| A6 | missing/stale/permission/secret cases blocked | negative test results, no half-true page | machine_pass / scope-limited patterns |
| A7 | five single skills, discovery / behavior / rollback | target checks and coverage caveats | metadata_pass / independent behavior benchmark not_run |
| A8 | different Human roles aligned against Mission | actual participants / handoff / confirmation | not_run |
| A9 | visual relations and source/action navigation | target page / source links + owning workflow evidence | static_links_pass / desktop_nonblank / full action review pending |
| A10 | complete define/act/EVAL/revise/align/handoff/DONE/learning | real representative task trace, accepted outcome / admission | not_run |
| A11 | valid Copilot and actual Sol / Luna workloads | actual model / action / result / entitlement, not picker alone | Luna startup UI observed / actual dual workloads pending |
| A12 | Human source revision + authorized Tools action | real diff / tool result / permission / new snapshot / task EVAL | authorized Agent local_tool_pass / actual Human task loop pending |
| A13 | Luna bounded maintenance + Mission regression | actual Luna work, approved change / tests / handoff | not_run |

Owner 声明本机订阅有效且 picker 两者可选；该声明只覆盖 entitlement / visibility observation，不证明 Sol/Luna 两场景已跑。单人 Owner 不虚构第二 Human；软件 tests 不代替 A5/A8/A10/A11/A13。

机器检查命令与结果见 [bootstrap Audit](../Audit/2026-09-30-bootstrap.md)。原样文件pins与adapter测试的通过只证明其具体slice，绝不把所有验收项改成pass。

Stop Rule：source / authority / permission / runtime / cost 有缺口时明确 blocked；已批准安全本地软件构建可独立完成，不冒称缺失的实际验收。目标软件 EVAL、consumer task EVAL、软件维护 tests 分开。
