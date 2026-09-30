# rem Agent Bootstrap

Authority: [.github/copilot-instructions.md](.github/copilot-instructions.md)，RCI Version=`1.0.0`，Freshness=`2026-09-30`。本文件为 non-authority projection。

开始前读取 authority；不存在、不可达、版本不为 1.0.0 或冲突时 blocked，不猜测降级。读取 [today](Repo/today.md)、[now](Repo/now.md) 以及 EGO 四件套：[EGO-rem](EGO/EGO-rem.md)、[EdgeTeam](EGO/EdgeTeam.md)、[Naming](EGO/Naming.md)、[Working](EGO/Working.md)。

生产 skills 只在 `.agents/skills/<name>/`。持有 exactly one Primary Mission，selected_method=null。外部、破坏、付费、权限 / authority 变更须 Owner gate；先验证后声称完成。不改动外部 EGO-T189 source repo。适用规则优先级：authority -> target instructions -> 本 projection -> skill defaults。
