# rem Tools

| Tool | 动作与副作用 | Permission / evidence |
|---|---|---|
| scripts/verify.py | 只读结构、来源 pin 与本地链接检查 | 返回实际 pass/fail；`--record-tool` 经显式 actor / approval 后新增本地 evidence，不代替 Human acceptance |
| scripts/mirror.py | 读取批准的显式 Markdown，写唯一新镜页 | reviewed / approval flags 只是声明，调用者须确认许可；无写回、无网络执行 |
| Git | source revision、diff、commit / handoff | 写入 / push / history / external 按 Owner gate；不静默覆盖未知改动 |
| VSC / Copilot | Human 修改任务内容，Agent 推演 / 执行 | 订阅、picker、scope 与 action permission 实际确认；不伪造模型切换 |

其它 Tools 只有在任务需要、权限 / cost / 输入 / 结果验证已明确时才接入；没有预装云账号或 provider entitlement。每次执行留真实 result/failure，不把模拟证据当真实动作。
