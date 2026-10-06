# rem TeamSkill / Skill Registry

| Capability | What / Why | How identity | Target state |
| --- | --- | --- | --- |
| Narrative / bounded action | [NP0](np0/SKILL.md) | [np0](../../.agents/skills/np0/SKILL.md) | target-adapted wrapper, universal capsule unchanged |
| Complete REM | [REM](rem/SKILL.md) | rem-ready / motioner / looper | independent target bindings, no T189 runtime |
| Startup / pause | [RWS](../Rws.md) | [rem-ready](../../.agents/skills/rem-ready/SKILL.md) | subscription / model facts remain independently gated; prior daily snapshots go to `Repo/days/YYYY-MM-DD/today.md` |
| Motion lifecycle | [REM](rem/SKILL.md) | [motioner](../../.agents/skills/motioner/SKILL.md) | finite lifecycle, landing / Audit / retirement to `Repo/days/<closeout-date>/Motion/` |
| Maintenance / path migration | [REM](rem/SKILL.md) | [looper](../../.agents/skills/looper/SKILL.md) | report-first, bounded repair; inventory and relink dated asset moves |
| Deterministic MPS artifact | [Naming](../Naming.md) | [teamspage](../../.agents/skills/teamspage/SKILL.md) | seven MPS source assets remain pinned; path-only `mps.py` / contract target deltas are hash-checked; custody at `Repo/TeamsPage/` |

Daily snapshot custody belongs to rem-ready; closed Motion source retirement belongs to motioner; looper performs approved path/asset migrations. If an archive category has no clear owner, motioner decides the route first. The Skill identity remains lowercase `teamspage`; only the repository custody directory uses `TeamsPage`.

production identities only under `.agents/skills/`. Model Workloads / Human gates / deterministic Tools are not new identities. Freshness / source / rollback / behavior evidence see [deployment](deployment.md).
