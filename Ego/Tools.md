# rem Tools

| Tool | 动作与副作用 | Permission / evidence |
| --- | --- | --- |
| scripts/verify.py | 只读结构、来源 pin 与本地链接检查 | 返回实际 pass/fail；`--record-tool` 经显式 actor / approval 后新增本地 evidence，不代替 Human acceptance |
| scripts/mirror.py | 读取批准的显式 Markdown，写唯一新确定性 MPS artifact；不是 Narrative Page | reviewed / approval flags 只是声明，调用者须确认许可；无写回、无网络执行 |
| CLI（按需安装） | 安装、运行、移除 | 任何安装都须 Player 批准，包括 npx / uvx 临时调用；运行器调用钉版本、不用 latest；每次安装与移除按 Method 4 留证 |
| Git | source revision、diff、commit / handoff | 写入 / push / history / external 按 Player gate；不静默覆盖未知改动 |
| VSC / Copilot | Human 修改任务内容，Agent 推演 / 执行 | 订阅、picker、scope 与 action permission 实际确认；不伪造模型切换 |

其它 Tools 只有在任务需要、权限 / cost / 输入 / 结果验证已明确时才接入；没有预装云账号或 provider entitlement。每次执行留真实 result/failure，不把模拟证据当真实动作。

## 保留 CLI 登记

下表登记经 Player 决定保留的版本与用途；登记不代表已安装或授权某次调用。全局安装 `cf` 不在 M2 授权内。

| CLI | 用途 | 来源 | 调用方式 | 保留理由 / 边界 |
| --- | --- | --- | --- | --- |
| `cf@1.0.0-beta.9` | 管理 Cloudflare 资源 | [M2 决定](../Repo/days/2026-10-01/Motion/motion-cf-cli-stack-decision-2026-09-30.md) | `npx --yes --package=cf@1.0.0-beta.9 cf` | M2 已定版本；不得浮动到 latest；不授权全局安装 |
| `wrangler@4.145.0` | Cloudflare Pages Direct Upload | [M2 决定](../Repo/days/2026-10-01/Motion/motion-cf-cli-stack-decision-2026-09-30.md) | `npx --yes wrangler@4.145.0` | M2 已定版本；不得浮动到 latest |

PDF CLI 与引擎待 Player 决定，本表暂不登记。

## Maintenance constraints

[本次 source 维护同步](../Mission/Audit/2026-09-30-source-maintenance-sync.md)只承接维护结论，不导入 source CRAFTS / T189 规则。结构 gate 通过不证明 snapshot 内容或 permission 真实；snapshot 按 `targetrun_id/slug/quartet/date/hash/no-writeback` 验证，合法输出不得为“清目录”删除。target-pinned NP0/MPS 不自动升级，原件 / 唯一证据先做 custody 判断。Tools 运行、模型 picker 与实际 Human / EVAL 分开留证，另一窗口工作不在本次提交范围。
