# Evidence - 独立 VSC / rem-ready 启动观察

> **Evidence Type**: Owner-provided screenshot / bounded UI observation
> **Source**: Owner 于 2026-09-30 当前 EGO-T189 对话提供的截图，并陈述“这是完成后的截屏，看起来顺利”。原图在会话附件，本文件为观察摘要，不伪造独立原图文件或精确截图时刻。
> **Observer**: GitHub Copilot；工作面操作由 Owner 报告
> **Acceptance Boundary**: startup smoke only；不是产品整体验收或模型完整 workload 归因

## 可见事实

- 独立 VSC Explorer/workspace 名为 rem，打开 target README；用户命令为 `get rem ready`。
- Chat 显示 `Completed 12 steps in 1m 12s`，返回“rem 本地开工入口已就绪”。
- 返回报告声明：日期 2026-09-30 / UTC+08:00 与基线一致；git clean，相对本地 origin/main 为 0 ahead / 0 behind，未 fetch；`python scripts/verify.py` 通过、无 failures。
- 返回报告声明：terminal 已对齐，VSC 1.139.1 / PowerShell 7.6.6 / Python 3.14.0；唯一 Primary=Story-rem、selected_method=null，未刷新日期或修改文件。
- picker 可见标签=`GPT-6 Luna / Max / 872K`。这是截图时的 UI selection，不证明每步实际 backend model、official context limit 或完整 Luna software-maintenance run。
- 返回仍列 unknown：未保存 buffer、Profile/Sync、订阅及模型runtime核验、Human/EVAL。

报告正文是该 Chat 的声明；原始 terminal outputs/完整 transcript 未提供。截图能支持独立 workspace 中实际调用启动流程与 picker 可见性，不能独立证明五项 skills 每一项均已被加载、远端最新事实、实际 Sol 运行、不同 Human 已对齐或 A1-A13 全部通过。

## 后续独立观察

本次范围拆分前只读检查 target HEAD=`2fdbbca18e0ea122a62a286cbc3a8ecf4f804fda`；worktree 有未提交 `Repo/shape/teamspage/MPS-260930S3004-rem-instance-rem.html`。它是另一窗口产生的既有工件，来源未归因，不由本次改写、删除或提交；不把截图报告的旧 clean 状态沿用为当前事实。2026-10-01 Owner 将 live custody 目录大小写统一为 `Repo/shape/TeamsPage/`；此处保留观察当时的原始路径。
