# Audit - Cloudflare M1-M3 deployment follow-up

> **Date**: 2026-10-01
> **Owner**: yangjun / bitguts
> **Status**: M1-M3 Done; Owner-accepted closeout
> **Scope**: Owner-reported Cloudflare account/domain work and public Pages delivery; local Motion/EGO/Audit handoff only
> **Supersedes for current status**: 2026-09-30 Cloudflare approval, M1, M2, and M3 blocked-state summaries; those records remain historical
> **History Triage Result**: Audit First
> **Source Retirement**: Original M1-M3 Motion files archived under `Repo/days/2026-10-01/Motion/`; retained as provenance, no longer pending sources

## Owner decisions and reports

Owner reported that `bitguts@gmail.com` was used to log in to Cloudflare, the `teamsbook.org` account/Zone was confirmed, and the related services were deployed. Owner also reported `cf` CLI deployment/execution/verification as effective and provided the deployment report and snapshots referenced in [evidence](../evidence/2026-10-01-cloudflare-pages-owner-report.md).

In the current conversation, Owner explicitly confirmed:

1. Refresh `Repo/today.md` and `Repo/now.md` to 2026-10-01, preserving the full prior `today.md` snapshot and leaving existing Teamspage changes untouched.
2. Replace the prior M2 candidate with the implemented tool split: `cf@1.0.0-beta.9` for Cloudflare resource management and `wrangler@4.145.0` for Pages Direct Upload.
3. Replace M3's private Entra portal target with a public static HTML service at `rem.teamsbook.org/<slug>`, without login or access control.
4. Owner closeout ruling: all three Motions are `Done`; cost is `0` and has been verified; rollback rehearsal is unnecessary; a separate operations handoff is discontinued.

The production deployment predates these local record edits and is attributed to the Owner's report. GitHub Copilot did not log in to Cloudflare, call account/resource APIs, change DNS, run `cf`/Wrangler, or deploy Pages during this follow-up.

## M1 - EGO DNS record

The canonical `teamsbook.org` entry records the Owner-confirmed Cloudflare account/Zone and operational hostname, with a direct evidence locator. Registrar/registrant identity remains unknown, and the account/DNS assertions were not independently rechecked by the Agent. Owner accepts the local EGO record and M1 as `Done`; registrar identity is not asserted or required for the selected hostname service.

## M2 - CLI and stack

The current matrix is [Cloudflare Pages capability matrix](../../Repo/days/2026-10-01/cloudflare-capability-matrix.md). The previously accepted Worker Static Assets + Access/Entra candidate is superseded for this public Pages service. The supplied deployment report and Owner's CLI confirmation support M2 `Done`; package integrity/account state were not independently queried by the Agent. Owner confirms verified cost `0` and waives rollback rehearsal for this scope.

## M3 - public Pages delivery

Owner confirmed the public, no-authentication scope and the `/slug` route. The supplied report records a successful Pages deployment, active custom domain/HTTPS, five unit tests, response/content checks, and a working `/demo` page; the integrated-browser observation is limited to loading `/demo`. The earlier Entra SSO/private-portal scope is superseded. Owner accepts M3 as `Done`, confirms verified cost `0`, states rollback rehearsal is unnecessary, and discontinues a separate operations handoff deliverable.

## Closeout decisions

- Registrar/registrant identity remains unknown. Owner's account/Zone and operating-hostname confirmation is retained with its provenance; the unknown legal registrant is not represented as verified and is not a closeout blocker for this delivered hostname.
- Cost is `0`, verified per Owner confirmation in the current conversation. GitHub Copilot did not inspect billing or query the Cloudflare account.
- Rollback rehearsal is `not_applicable` by Owner decision. No rehearsal was performed or claimed.
- A separate operations handoff deliverable is discontinued by Owner decision. Existing project publishing/operations documentation remains available; it was not removed.
- The live site's content has not been reconciled against `Mission/teamsbook.org/index.md`; that draft remains non-authority. This does not reopen the accepted scope of the deployed public Pages service.

## Consumer Audit and History Triage

- M1 consumer: [EGO DNS canonical record](../../Ego/DNS/teamsbook.org.md) remains the single root-domain source and now records `rem.teamsbook.org` as Owner-confirmed operational while retaining unknown registrar/registrant identity.
- M2 consumer: [2026-10-01 capability matrix](../../Repo/days/2026-10-01/cloudflare-capability-matrix.md) matches the supplied project materials: `cf` resource management, Wrangler Pages Direct Upload, complete `site/` upload, public static HTML, no Access/Entra runtime.
- M3 consumer: Owner-accepted public route `https://rem.teamsbook.org/<slug>` matches the deployment record and `/demo` browser load. The prior private Entra design is historical and not an active requirement.
- **History Triage Result**: `Audit First`. Current EGO, stack decision, evidence, and closeout outcomes are landed in canonical records; 2026-09-30 Motions and audits remain provenance, not current execution instructions.
- **Source retirement trace**: completed M1-M3 Motion sources are moved intact as closed records to `Repo/days/2026-10-01/Motion/`. Their pending-work copies are removed only after this Audit, consumer review, and repository validation; no audit or evidence is deleted.

All three Motions are `Done` by Owner decision. Product EVAL A1-A13, Human/model/runtime acceptance, and `Mission/teamsbook.org/index.md` authority/content status are unchanged.

## Local action and validation

- Preserved the prior daily handoff at [today-2026-09-30 archive](../../Repo/days/2026-09-30/today.md); existing Teamspage worktree changes were left untouched.
- `python scripts/verify.py`: baseline `structure=pass`, `failures=[]`; the first archive run found a broken relative link, which was corrected and rerun to pass; M2, M3, and final runs all returned `structure=pass`, `failures=[]`. Each run reported `human_review`, `runtime_models`, and `role_alignment` as `not_run`. This validates repository structure/links/pins, not Cloudflare or Human acceptance.
