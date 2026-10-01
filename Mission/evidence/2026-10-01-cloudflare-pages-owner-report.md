# Evidence - Owner-provided Cloudflare Pages deployment report

> **Date**: 2026-10-01
> **Owner**: yangjun / bitguts
> **Type**: Owner-provided deployment and acceptance report; not an independent tenant observation
> **Status**: Source documents reviewed; no credentials or Cloudflare account APIs accessed by GitHub Copilot

## Sources

- Owner's current-conversation report: the `bitguts@gmail.com` Cloudflare account was used to log in and confirm the `teamsbook.org` account/Zone; related services were deployed and verified.
- `D:\codex\rem.teamsbook.org\DEPLOYMENT-RECORD.md`
- `D:\codex\rem.teamsbook.org\evidence\domain-check.json`
- `D:\codex\rem.teamsbook.org\evidence\pages-deployment.json`
- Implementation and operating materials under `D:\Codex\projects\rem.teamsbook.org`, including `README.md`, `OPERATIONS.md`, `PUBLISHING-GUIDE.md`, `rem.py`, `tests/test_rem.py`, `domain.json`, and `site/`.

## Reported implementation and results

- Platform: Cloudflare Pages Direct Upload, project `rem-teamsbook`, custom hostname `rem.teamsbook.org`.
- Tools reported by the deployment record: `cf@1.0.0-beta.9` for Cloudflare resource management and `wrangler@4.145.0` for Pages asset upload.
- The public service hosts self-contained HTML pages by slug, such as `/demo`; the project documentation explicitly says there is no login or access control and a slug is not an authorization boundary.
- The post-deployment snapshot reports deployment status `success`, custom-domain and certificate states `active`, and these checks: `/` 200 with local-byte match; `/demo` 200 with local-byte match; `/demo.html` 308 to `/demo`; unknown path 404; `/domain.json` 404.
- The same snapshot reports five Python unit tests passing, `rem.py check` succeeding, and inline JavaScript syntax checks passing for the homepage, demo, and 404 page.
- The pre-deployment `domain-check.json` is a historical baseline: it reports an active full Zone but no hostname record and `remote_changes_made: false` at that earlier check. The later deployment snapshot records the configured Pages hostname and DNS. These are different points in the reported sequence, not contradictory current states.

## Agent observation and limits

- GitHub Copilot opened `https://rem.teamsbook.org/demo` in the integrated browser. The page title was `单页示例 · REM` and the counter initially displayed `0`; no button interaction or broader end-to-end test was performed here. Owner separately confirmed that the page opened successfully.
- The source documents and JSON snapshots were read from the paths above. Their Cloudflare account/resource claims were not independently queried during this session; the account login, DNS mutation, deployment commands, test commands, and rollback were not performed by GitHub Copilot.
- The files report no secrets in the publishing project. They do not independently establish registrar/registrant identity, current billing/plan entitlement, a rollback rehearsal, or whether `Mission/teamsbook.org/index.md` is the content source for the live homepage.

This evidence records supplied observations and their provenance. It does not by itself grant Cloudflare permissions or establish product/Mission acceptance beyond the Owner decisions separately recorded in the follow-up Audit.
