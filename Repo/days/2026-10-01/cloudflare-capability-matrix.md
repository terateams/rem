# Cloudflare capability matrix for the public rem Pages service

> **Date**: 2026-10-01
> **Owner**: yangjun / bitguts
> **Status**: Done by Owner acceptance; source retired 2026-10-01
> **Binding**: [EGO DNS record](../../../Ego/DNS/teamsbook.org.md) · [M2 Motion](Motion/motion-cf-cli-stack-decision-2026-09-30.md) · [M3 Motion](Motion/motion-teamsbook-cloudflare-delivery-2026-09-30.md)
> **Evidence**: [Owner-provided deployment report](../../../Mission/evidence/2026-10-01-cloudflare-pages-owner-report.md) · [follow-up Audit](../../../Mission/Audit/2026-10-01-cloudflare-motions-followup.md)
> **Previous candidate**: [2026-09-30 matrix](../2026-09-30/cloudflare-capability-matrix.md), retained as historical and superseded

## Current decision

The current service is a public Cloudflare Pages site at `https://rem.teamsbook.org`. Each business page is a self-contained HTML file addressed by a slug, for example `/demo` or `/sales-report`. Owner explicitly selected this public, no-login/no-access-control model on 2026-10-01. A slug is routing, not authorization; content must be suitable for public disclosure.

The implemented tool split reported by Owner is `cf@1.0.0-beta.9` for Cloudflare resource management and project-pinned `wrangler@4.145.0` for Pages Direct Upload. The Python standard-library `rem.py` importer validates and adds pages, and deployment uploads the complete `site/` directory. It is not a Worker Static Assets + Access application and does not use Entra SSO.

## Capability matrix

| Capability | Current implementation | Reported evidence | Boundary / remaining state |
| --- | --- | --- | --- |
| Static hosting | Cloudflare Pages project `rem-teamsbook` | Deployment record reports `success` | Public static files only; no server runtime, database, or Functions |
| Resource management | `cf@1.0.0-beta.9` | Owner reports CLI use; deployment materials identify version | Package integrity/current official release not independently rechecked in this follow-up |
| Asset deployment | `wrangler@4.145.0` Pages Direct Upload | Project lockfile and deployment record | Upload the complete `site/`; keep that directory as source of truth |
| Publishing workflow | Python standard-library `rem.py publish <file> <slug>` | Source script and five-test report | Existing slugs require `--replace`; validation does not analyze dynamic JavaScript network behavior |
| URL routing | `site/<slug>.html` serves at `/<slug>`; unknown paths return 404 | Reported `/`, `/demo`, `.html` redirect, unknown-path and config-path checks | Slugs are not access control; the homepage does not list every business page |
| DNS and TLS | Custom hostname `rem.teamsbook.org` on Pages | Owner-provided record reports custom domain, DNS and certificate active | Not independently resolved or checked against the Cloudflare account in this session |
| Identity/access | None for site visitors | Owner selected public access | No Cloudflare Access, Entra SSO, user ACL, or private-file guarantee |

## Security, cost, and rollback

- Publish only information suitable for public access. Do not place secrets, personal information, or internal material in HTML. Random or obscure slugs do not provide confidentiality.
- The importer checks common declarative resource references, but does not execute scripts and cannot prove they never make runtime network requests. Review scripts, forms, external links, embedded data, and navigation before publication.
- Owner confirms cost was verified as `0`; this is an Owner-confirmed result, not a billing API observation by the Agent.
- Owner rules a rollback rehearsal unnecessary for this static Pages service. No rehearsal was performed or claimed. Pages Direct Upload replaces the deployed site with the submitted `site/` contents; preserve the complete source directory.
- Owner discontinues a separate operations handoff deliverable. The project's publishing and operations documents remain available to operators.
- No Access policy, Worker API, database, upload path, CI credential, paid service, or additional Cloudflare product is included in this public static scope.

## Reported verification

The supplied deployment snapshot reports `/` and `/demo` as HTTP 200 with local-byte matches, `/demo.html` redirecting to `/demo`, an unknown path returning 404, and `/domain.json` returning 404. It reports five Python unit tests and inline JavaScript syntax checks passing. GitHub Copilot separately opened `/demo` in the integrated browser; this was a page-load check only, not an account/API or full workflow test.
