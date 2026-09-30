# rem Tools

| Tool | 动作与副作用 | Permission / evidence |
| --- | --- | --- |
| scripts/verify.py | 只读结构、来源 pin 与本地链接检查 | 返回实际 pass/fail；`--record-tool` 经显式 actor / approval 后新增本地 evidence，不代替 Human acceptance |
| scripts/mirror.py | 读取批准的显式 Markdown，写唯一新镜页 | reviewed / approval flags 只是声明，调用者须确认许可；无写回、无网络执行 |
| Git | source revision、diff、commit / handoff | 写入 / push / history / external 按 Owner gate；不静默覆盖未知改动 |
| VSC / Copilot | Human 修改任务内容，Agent 推演 / 执行 | 订阅、picker、scope 与 action permission 实际确认；不伪造模型切换 |

其它 Tools 只有在任务需要、权限 / cost / 输入 / 结果验证已明确时才接入；没有预装云账号或 provider entitlement。每次执行留真实 result/failure，不把模拟证据当真实动作。

## Maintenance constraints

[本次source维护同步](../Mission/Audit/2026-09-30-source-maintenance-sync.md)只承接维护结论，不导入sourceCRAFTS/T189规则。结构gate通过不证明snapshot内容或permission真实；snapshot按targetrun_id/slug/quartet/date/hash/no-writeback验证，合法输出不得为“清目录”删除。targetpinned NP0/MPS不自动升级，原件/唯一证据先custody判断。Tools运行、模型picker与实际Human/EVAL分开留证，另一窗口工作不在本次提交范围。
