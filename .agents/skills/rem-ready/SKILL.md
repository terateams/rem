---
name: rem-ready
description: "用于 rem 开工、冷启动、日期/git/工作面对齐与离开前安全收口；不用于具体正文任务或自动同步。"
metadata:
  status: in-production
  source_commit: 70090b756d2c4f4e75912ec9f3ede2ff3e8cc0a0
---

# rem ready

Inspect-first：读 today/now/INTENT 与 EGO quartet；核验当前运行日期、git status、ahead/behind、cursor dirty、Dojo path status、前日归档。terminal cwd与workspace、VSC/Profile/Sync/extensions、实际设备与必要runtime独立核验；unknown 显式，现场只由 Human 声明或标明沿用，不设 T189 inventory。

订阅/picker实际或Human声明与模型run evidence分开；Mission Sol / self Luna不自动切换。日期 stale + dirty/behind/unknown 拉Andon，等待Human路径选择，不stash/reset/pull/overwrite。批准refresh后先完整保存前日快照到 `Repo/days/YYYY-MM-DD/today.md`，整体reset today再now，INTENT不每日无故重写。

读 `scripts/verify.py`实际输出，必要且获授权时调用 `scripts/mirror.py`；核心入口成立不等所有A1-A13完成。Away只做日期/git/Dojo/cursor风险，给返回入口。External / commit/push / paid / config change需批准，不伪造 synced/ready。
