# Repo Days

Repo-level dated records live under `Repo/days/YYYY-MM-DD/`.

- Daily snapshots use the snapshot date, for example `2026-09-30/today.md`; the active handoff remains at `Repo/today.md` and `Repo/now.md`.
- Dated plans and capability matrices use their document date.
- Completed Motion sources use their closeout date under `YYYY-MM-DD/Motion/`; preserve their source date in the document metadata.
- Mission decisions and evidence remain in `Mission/Audit/` and `Mission/evidence/`; this tree does not replace Mission custody.

Skill routing: `rem-ready` owns daily snapshot refresh; `motioner` owns Motion lifecycle and archive routing; `looper` inventories and performs approved path/asset moves; `teamspage` owns Mirror Page custody at `Repo/shape/TeamsPage/`. If a dated artifact has no clear owner, `motioner` decides its route first.
