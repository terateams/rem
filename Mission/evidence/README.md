# rem Action evidence

每次获授权 Tools 动作记录任务 / 岗位、actor、tool/action、permission / cost、inputs、实际 result/failure、source revision、time、evidence locator、next action。敏感值不入仓。

`python scripts/verify.py --record-tool --actor bitguts --approval-evidence Mission/Audit/2026-09-30-bootstrap.md` 是真实本地 deterministic tool 调用；其 JSON result 证明该工具执行与结构结果，不证明其他 Human、模型或 Mission 已验收。

Task completion、review 与 admitted learning 按 EVAL / Audit / EGO owning gate 留证。测试 fixture / dry-run / synthetic 与真实动作标签明确，不混写。
