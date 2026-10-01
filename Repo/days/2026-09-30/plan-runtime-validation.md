# Plan - rem 真实运行验证 / bootstrap 后续

> **Date**: 2026-09-30
> **Owner / Decision Rights**: yangjun / bitguts
> **Status**: pending validation；不是新 Mission 或产品 accepted 声明
> **Source**: 原 bootstrap Motion A1-A13；Owner 当前对话“批准一次范围拆分”
> **Binding**: [Story-rem](../../../Mission/Story-rem.md) / [EVAL](../../../Mission/EVAL/eval-rem-v1.md)
> **Prerequisite**: Owner已明确接受bootstrap R1交付/交接，source治理收口在同批完成；本计划只准备验证，不自行启动付费、外部、模型切换或真实task

## 范围不删减

当前 R1 负责创建并交付可验证 software baseline；下列剩余要求承接到目标 EVAL 与本计划。目标“完整 REM、Sol/Luna 双场景、内生镜页、Human 岗位任务行动”功能不缩水，产品不因 R1 关闭而变为 Done/Passed/V1.0 released。

| Gate | 当前已知 / 尚缺 | Next bounded work | Owner / evidence / stop |
| --- | --- | --- | --- |
| A1 / A11 startup slice | 独立 rem VSC 调用 rem-ready，Luna picker可见；actual model/backend/controls仍有限 | [startup evidence](../../../Mission/evidence/2026-09-30-vsc-startup.md) 留观察边界，核验 actual run binding | Owner 在 target VSC 确认模型；缺证据保持 partial，不以 screenshot 代 backend proof |
| A5 输出 EVAL | machine gates非 Human acceptance | 选一个有权/有界 Mission，对 Agent 输出按 EVAL 做 accept/correct/reject | Owner 指定 reviewer/criteria/output/evidence；裁决缺失不自动通过 |
| A7 技能行为 | 五项 metadata、sourcepins、24项代码测试已过；独立 trigger/行为适配未验 | 定义正/负触发与有界行为 cases，观察五项 target wrappers 的实际 route/stop/parity | Owner 批准 runtime与可观察 cost；记录 shared/independent context限制，无调用能力不伪造 benchmark |
| A8 Human 岗位对齐 | 只有 Owner，不虚构第二位 Human | Owner 点名实际参与者、岗位/责任/交付/接受位，同一 Mission 进行 confirmation/correction | 参与者与权限由 Human 决定，未参与/确认 not_run |
| A9 / A12 行动联动 | 原件/HTML机器检查及 Agent本地Tools已有；Human真实task路径未过 | Human据镜页修订原件，再执行一项已有授权 Tools，记录实际结果/失败与source delta | action权限/cost/inputs/result明确；链接/fixture/dry-run不等执行 |
| A10 完整闭环 | target合同已覆盖完整REM，真实代表性task未闭合 | 从定义到执行/EVAL/correction/handoff/DONE/admitted learning 完成一条任务链 | task由 Owner指定；Scope/权限/真实证据缺失停止，不以文档多或HTML完成代替 |
| A11 双场景 | 订阅/picker为Human声明；Sol task 与 Luna self-workload需独立运行 | 在 target VSC 分别选择模型，记录model/source/mission/action/result与可见usage | 无可靠automaticmodelcontrol，Human选择；不可用且无approvedfallback即blocked |
| A13 软件维护 | software tests通过不证明Luna实际维护 | 经批准有界修订一项target software，跑focused checks与Mission回归 | owningapproval/diff/test/rollback/handoff；不能把maintenance pass当业务Missionaccepted |

A2/A3/A4/A6 的现有machine evidence继续保留，并在上述实际执行中按source delta重跑适用检查。A1-A13 全部留在 target EVAL，不另分配 TM 编号、不添加 active Secondary。

## 接续顺序

1. bootstrap Human接受已记录；验收后的第一步仍由Owner指定真实验证任务，不把R1关闭当runtime gate pass。
2. Owner 在 target VSC 选定首个 bounded Mission、reviewer、权限/成本与停止条件，再开展 Sol 场景。
3. 实际 Human 评审/修订/Tools行动与另一岗位交接；镜页重新生成、旧页stale、结果回查。
4. 获准 Luna self-maintenance 与回归，补技能行为证据。
5. 逐项更新 EVAL，每条保留原始 status / evidence / unknown / acceptance holder；阶段未过不发布 V1.0。

其他窗口的未提交内容保持 custody，不自动commit/push。本计划不代替允许具体动作的permission grant。归档 retained evidence，镜页只作non-authority projection。
