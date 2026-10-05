---
name: teamspage
description: "为 rem 的显式 Mission 文件组生成、验证和比较内生 HTML 镜页；不做 Narrative authoring、Human验收、通用MPV/MPR或无REM绑定网页。"
metadata:
  status: in-production
  source_commit: 70090b756d2c4f4e75912ec9f3ede2ff3e8cc0a0
---

# rem built-in Mirror Page

实现identity保留小写 `teamspage`，不是额外用户产品；文件 custody 目录固定为 `Repo/TeamsPage/`，与 `Repo/Motion/` 同级。`scripts/mirror.py`读取explicit target request构造 typed inputs，generic MPS freeze source bytes/hash/revision/dirty与sentence provenance。只允许reviewed/no-secret且获授权的来源；declaration不是grant。

runtime与[contract](references/teamspage-runtime-contract.md)固定迁移；不部署CRAFTS adapter、MPV pilots或T189 Today默认值。CLI实际显示not_run gate不得转pass；deterministic rebuilt HTML、DOM、digest、G-ID/Voice/Distort与freshness分别验证。无companion manifest，#mp-data内嵌provenance，零外部runtime依赖。

scope omissions/unknowns明确；生成不是Narrative/EVAL/adoption，原件变更旧页stale。Human回原件修订或进入authorized Tools，HTML不执行/写回。stage custody在 `Repo/TeamsPage/`，actualreview独立record；只在owningcloseout后清理可再生物，保留唯一evidence。
