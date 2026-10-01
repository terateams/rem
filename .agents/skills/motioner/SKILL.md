---
name: motioner
description: "用于 rem Motion 起草、审阅、获批执行与收口；中文主叙事、明确 scope/EVAL/permission，不把 Draft 当执行许可。"
metadata:
  status: in-production
  source_commit: 70090b756d2c4f4e75912ec9f3ede2ff3e8cc0a0
---

# rem Motion operator

Motion=`Repo/shape/Motion/motion-{slug}-{YYYY-MM-DD}.md`。header含Date/Owner/Status/Type/Service Object/Primary Route/Source Request，正文含问题、裁决、scope/out-of-scope、执行、验收、landing/consumer audit/rollback。

finite Status：Draft、Approved、Executing、Blocked、Executed、Done、Withdrawn、Rejected、Superseded。R1/R2/R3是round，不是Status。Draft无批准只审阅；当前对话显式approval可以执行approved scope，Audit记录source仍Draft与runtime approval，不静默改为Approved冒充durable evidence。

execute只做approved content与必需closeout，不改peer/upstream未经批准。跑最相关验证，canonical landing / consumer audit / History Triage Result / source-retirement trace闭合后，将完成的 Motion source 移入 `Repo/days/<closeout-date>/Motion/`，更新shape/today/now。Motion lifecycle与source retirement由Motioner承载；新日志/档案类型若owner不明确，先由Motioner决定custody route，再交由专属Skill执行。admission非显然先Owner，不能raw Motion直接变History/Concept；缺证据保持Blocked/pending，不伪造Done。中文Owner-facing叙事，English字段与paths，交付前检查register。
