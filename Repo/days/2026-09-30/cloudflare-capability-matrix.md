# Cloudflare capability matrix for rem delivery

> **Date**: 2026-09-30
> **Owner**: yangjun / bitguts
> **Status**: Superseded 2026-10-01 by [the public Pages matrix](../2026-10-01/cloudflare-capability-matrix.md); this file preserves the original private Worker + Access candidate.
> **Binding**: [EGO DNS target](../../../Ego/DNS/teamsbook.org.md) · [M2 Motion](../2026-10-01/Motion/motion-cf-cli-stack-decision-2026-09-30.md)
> **Evidence**: [M2 Audit](../../../Mission/Audit/2026-09-30-cf-cli-stack-m2.md)
> **Content**: [REM method draft](../../../Mission/teamsbook.org/index.md) — local only, non-authority; its relationship to live Pages content is not established

**Historical note**: The candidate below was for a private Entra/Access portal. Owner replaced it on 2026-10-01 with the public Cloudflare Pages scope in the linked current matrix. Do not use this file as the current implementation decision.
> **Latest Owner inputs**: private static content; `rem.teamsbook.org`; Microsoft Entra SSO; allow any verified `@TeraTeams.com` email; Free-only, staging then production. The email-domain/Entra claim and Zone are not independently verified. Content draft: [Mission/teamsbook.org/index.md](../../../Mission/teamsbook.org/index.md), pending Human acceptance.

## Decision boundary

This is a product-level candidate matrix, not an exhaustive listing of `cf`'s 2,900+ commands and not permission to use a Cloudflare account. `cf cli search` locates operations; command `--help` / `cf schema` must be checked before any future operation. API command availability, typed configuration support, account entitlement, cost, and safe lifecycle ownership are separate facts.

Owner selected private portal/file delivery at `rem.teamsbook.org`, accepted Worker Static Assets plus hostname-based Cloudflare Access, selected Microsoft Entra ID organization SSO, confirmed shared read-only static files with no upload/per-user ACL, and specified Free-only for staging then production. Owner selected allowing any verified `@TeraTeams.com` email, a domain-wide rule rather than a named group. Owner reports an active full Cloudflare Zone and control are confirmed; this has not been independently verified. Domain ownership/Entra claim, exact file/root path, Free entitlement, and rollback remain unknown. Any paid dependency is a stop condition; the earlier possible USD 20 Pro option is superseded.

Latest access-scope clarification: Owner explicitly chose allowing any verified `@TeraTeams.com` email. This is a domain-wide allow, not a named Entra group. Whether the organization owns that email domain and Entra emits matching verified-email claims remains unverified.

## Candidate capability matrix

| Capability / rem use | `cf` / API surface | Typed project config | Cost / access boundary | Candidate gate / state |
| --- | --- | --- | --- | --- |
| **EGO DNS target**: root-domain intent | `cf` can manage Zones and DNS records; command discovery is local, resource reads/writes require auth | `accountId` can set a Worker project's default account; DNS records are not thereby declared | Owner reports active full Zone/control; not independently verified. DNS writes change external routing | Canonical root target is `teamsbook.org`; hostname target is `rem.teamsbook.org`, both remain non-operational `target / unverified`. No operation run. |
| **Static content serving**: shared private portal/files | `cf init`, `cf build`, `cf deploy`; no account operation is needed for local build/dry-run | Vite output can be deployed as Worker Static Assets; `cloudflare.config.ts` does not set an `assets.directory` for the Vite plugin | Static asset request pricing is free/unlimited in official docs; account entitlement remains unverified. Owner selected Free-only | Accepted candidate only if authorized users share the same static files with no upload/per-user ACL; no rem app scaffold or deployment yet. |
| **CI / deployment automation**: repeatable build and release after stack selection | Official `cf` CI flow pins project-local `cf`; API token and account ID are supplied to deploy step; `cf deploy --dry-run` should not need credentials/API | Commit `cloudflare.config.ts` and lockfile; keep build and deploy mode aligned | API token must be least-privilege and stored as CI secret; no CI identity, token or repo secret is configured | No CI workflow added. Requires explicit delivery, repository/CI scope, token permissions and separate production approval. |
| **Custom hostname / TLS**: bind selected subdomain to a Worker | `cf` API/resource commands; discover exact current operation and inspect schema/help before use | Worker `domains` / fetch-trigger fields exist in current config docs | Requires an active Cloudflare Zone and Worker; custom-domain setup creates DNS and certificate records. This is an external write | Exact hostname and Zone authority required; separate permission before staging/production. Not run. |
| **Private access**: Microsoft Entra organization SSO | `cf zero-trust access applications create` and policy operations exist; no account operation run | Access policy is separate from Worker `cloudflare.config.ts`; attach by hostname. `cf` is the candidate writer for both Worker and Access resources; no Terraform writer selected | Access is deny-by-default. Owner selected allowing any verified email ending `@TeraTeams.com`, which is broader than a named group. Entra claim/domain ownership and Free entitlement are not verified | Policy intent selected but not configured; verify organization/domain ownership and Entra email claim before implementation. Do not infer tenant membership from an email string. |
| **WAF / rate limiting**: protect a selected public application | `cf` exposes security/resource command groups; inspect each rule's plan support and API schema | Not a blanket `cloudflare.config.ts` whole-zone policy | Feature availability differs by Cloudflare plan; rules can affect legitimate traffic | Threat model, plan and hostname needed. Review first; no default rules enabled. |
| **State and background work**: D1, KV, R2, Queues, Durable Objects, Workflows | `cf` has resource APIs/commands for these families | Current typed bindings cover multiple storage and messaging services within Worker projects | Usage/retention costs and data responsibility differ per product; some workloads can incur cost during development | No current state/upload/job use case in Story/outputs. Exclude from minimum candidate until a requirement names it. |
| **Logs / analytics**: operational visibility | `cf` exposes logs, observability and analytics command groups | Worker config includes observability settings; some destinations/features are separate resources | Retention, sampling, plan limits and log contents must be reviewed | Decide only after delivery/privacy requirements; avoid recording secrets or personal data. |
| **Other product families**: AI, Vectorize, Containers, Tunnel/networking, email, media, etc. | `cf` public API surface may expose operations; command discovery does not imply need | Some bindings/configuration exist for Workers; not a general config for every account product | Several features are plan/usage dependent and can be billable | No rem-specific use case is recorded. Explicitly out of first-stack scope unless Owner adds a bounded requirement. |

## Minimum candidate and alternatives

> **Current decision takes precedence:** the later candidate paragraph records Owner's domain-wide `@TeraTeams.com` intent and the new local content draft; older candidate wording above is superseded. Implementation remains blocked.

For the selected **private portal/files at `rem.teamsbook.org`**, the accepted candidate is one pinned-`cf` Worker Static Assets project plus a hostname-based Access application using Microsoft Entra ID SSO. Shared read-only static files with no upload/per-user ACL is confirmed. `cloudflare.config.ts` is the Worker config authority; `cf zero-trust` API commands manage the Access app/policy; do not add Terraform as a second writer. Execution is blocked until the allowed Entra groups/users and exact file/root path are defined, Owner-reported Zone control has attributable evidence, Free entitlement is confirmed, and rollback is specified. Never expose the Worker before Access is configured. Do not add D1/KV/R2/Queues/AI; any paid requirement stops the work.
For the selected **private portal/files at `rem.teamsbook.org`**, the accepted candidate is one pinned-`cf` Worker Static Assets project plus a hostname-based Access application using Microsoft Entra ID SSO. Shared read-only static files with no upload/per-user ACL is confirmed. Owner selected allowing any verified email ending `@TeraTeams.com`; this is a whole-domain allow, not a named Entra group. `cloudflare.config.ts` is the Worker config authority; `cf zero-trust` API commands manage the Access app/policy; do not add Terraform as a second writer. Execution is blocked until the email domain is verified as the organization's, the Entra claim matches, allowed access scope is confirmed, exact file/root path exists, Zone/Free claims have attributable evidence, and rollback is specified. Never expose the Worker before Access is configured. Do not add D1/KV/R2/Queues/AI; any paid requirement stops the work.

If the portal needs user-specific files, uploads, or application-side roles, the static candidate is insufficient; define the app/data model and cost before adding a Worker API or storage. The supplied Cloudflare login email is not an Access allowlist decision.

If the first delivery is a **dynamic application**, identify its API, persistence, identity and data-retention requirements before selecting Worker bindings or storage. If it is **private source/file delivery**, compare the repository's existing private distribution path before making a public Worker hostname. Neither alternative is selected here.

## Required gates before any remote change

1. Owner confirms the broad `@TeraTeams.com` allow scope is intended, the organization controls that email domain, and Entra asserts matching verified email claims; identify the exact file/root path to serve.
2. Owner supplies attributable non-secret evidence of domain/Zone authority; the current full-Zone/control statement is Owner-reported, not independently verified.
3. Confirm Free entitlement for both staging and production, data classification, and that any paid feature blocks execution; no paid fallback.
4. Pin project-local `cf` version and lock integrity; declare one write authority per resource; review command `--help` / schema and `--dry-run` output before write operations.
5. Define staging data, least-privilege API token custody, health checks, rollback and who approves each DNS, Access, security and production change.

Cloudflare CI docs state `cf deploy --dry-run` builds and validates without credentials or API requests. This was verified in an isolated generic Worker sample; it is not a rem project validation. Any staging or production deployment remains a separate authorized action.

An isolated temporary Worker sample was created under the current M2 local validation scope. It verified that the installed beta can generate types, build, and complete a direct `cf deploy --dry-run`; this does not validate rem's application or authorize account use. Its sample dependency audit reported 5 findings (4 moderate, 1 high), including a high-severity `undici` advisory in the `miniflare` dependency path. No dependency fix was applied; do not reuse the sample lockfile for rem without a fresh security review.

## Sources checked

- [Cloudflare CLI overview](https://developers.cloudflare.com/cf/) — beta; public API commands and Worker project commands; documentation updated 2026-09-29.
- [Manage resources with `cf`](https://developers.cloudflare.com/cf/get-started/resources/) — DNS operations, local command discovery, preview/dry-run behavior; updated 2026-09-29.
- [Programmatic Worker configuration](https://developers.cloudflare.com/cf/projects/cloudflare-config/) — Worker/Container config and typed bindings; updated 2026-09-29.
- [Deploy your first Worker](https://developers.cloudflare.com/cf/get-started/first-worker/) — `cf init`, local project files and generated config/types; updated 2026-09-29.
- [Use `cf` in CI](https://developers.cloudflare.com/cf/ci/) — project-local version, secret/token scope, and no-credential dry-run flow; updated 2026-09-29.
- [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/) — static asset behavior and Vite/Worker deployment path; updated 2026-07-03.
- [Worker Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) — active Zone/Worker prerequisite and DNS/certificate effects; updated 2026-09-29.
- [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) — plan, static requests, included usage and metered services; updated 2026-08-28.
- [Cloudflare Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) — policy semantics and common misconfiguration risk; updated 2026-09-04.
- [Cloudflare WAF](https://developers.cloudflare.com/waf/) — feature and plan availability; updated 2026-08-19.
- [Access for Workers](https://developers.cloudflare.com/workers/configuration/cloudflare-access/) — hostname/Worker protection and policy behavior; updated 2026-08-18.
- [Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) — Cloudflare IdP and one-time PIN options; updated 2026-06-19.
- [Cloudflare Zero Trust setup](https://developers.cloudflare.com/cloudflare-one/setup/) — Free plan onboarding/payment-details step; updated 2026-04-17.

Re-check official support, version, pricing and account entitlements immediately before implementation; this matrix is dated research, not live account evidence.
