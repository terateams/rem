# Audit - Cloudflare `cf` CLI / Stack decision (M2)

> **Date**: 2026-09-30
> **Owner**: yangjun / bitguts
> **Status**: Blocked after public capability review and bounded local validation
> **Source Motion**: [motion-cf-cli-stack-decision](../../Repo/days/2026-10-01/Motion/motion-cf-cli-stack-decision-2026-09-30.md)
> **Current closeout**: This is the 2026-09-30 historical M2 snapshot. The accepted Pages implementation and `Done` decision are recorded in [2026-10-01 closeout Audit](2026-10-01-cloudflare-motions-followup.md).
> **Source Status at Runtime Approval**: Draft
> **Runtime Approval**: Owner instruction in the current conversation to split and execute sequentially; bounded to public documentation/package checks and pinned, unauthenticated local CLI smoke

## Observed Inputs

- Cloudflare official CLI documentation, updated 2026-09-29: `cf` remains beta; it covers the public Cloudflare API and Workers projects. The documentation reports 2,900+ commands; the 2026-09-28 launch blog reports 3,000+ API operations. These are different measures and are not treated as a discrepancy or as proof that every service has complete declarative lifecycle support.
- Official `cloudflare/cf` GitHub repository reports latest release `cf@1.0.0-beta.5`; npm registry metadata for the same package reports version `1.0.0-beta.5`, repository `https://github.com/cloudflare/cf`, and integrity `sha512-IKGKDAQNs8hbu7jOt3qSWKxDjmJTS+hcHCJ5B0IkF7gZ3RmEfMTUxZ0Fi7GRftjag04J127u8Nk8uppXx3OBZw==`.
- Published package metadata declares binaries `cf` and `cloudflare` at `bin/cf`, Node `>=22`, and no `preinstall`, `install`, or `postinstall` script. Local Node was `v24.12.0`.
- Official docs describe `cloudflare.config.ts` for Workers projects. They do not establish that every Cloudflare product has complete typed configuration or lifecycle management.
- Owner follow-up input: private portal/files at `rem.teamsbook.org`, Microsoft Entra ID organization SSO, shared read-only files with no upload/per-user ACL, and Free-only for staging then production; any paid dependency is a stop condition. Owner selected an Access rule allowing any verified email ending `@TeraTeams.com`; this is domain-wide, not a named Entra group.
- Owner reports an active full Cloudflare Zone/control and Free entitlement confirmed. These are Owner self-attestations, not independent account observations; no account was accessed. The EGO/DNS record remains `target / unverified` pending attributable evidence accepted by the owning workflow.
- Domain ownership/Entra claim mapping for `@TeraTeams.com` has not been verified. A new non-authority content draft now exists at `Mission/teamsbook.org/index.md`; it is not Human-accepted or built into a site.
- Actual files/root to serve, accepted evidence for Zone/Free status, and rollback details remain unresolved. The hostname is recorded as `rem.teamsbook.org` / `target / unverified`; no DNS operation occurred.
- Cloudflare Access docs: a hostname-based self-hosted application requires a domain in an active Cloudflare Zone and an explicit Allow policy; applications are deny-by-default. Cloudflare IdP and one-time PIN to explicitly allowed email addresses are documented options. Zero Trust Free onboarding still asks for payment details but says the account will not be charged. This does not establish current account entitlement or make the provided Cloudflare login email an approved application user.
- The earlier possible USD 20 Pro option was superseded by Owner's explicit Free-only decision. Workers/Zero Trust Free entitlement has not been verified in the account; if the selected stack requires payment, stop rather than upgrade or purchase.
- Anonymous local `cf cli search 'create a self-hosted Access application for a Worker hostname'` returned `cf zero-trust access applications create` and a policy-create operation. This was local command discovery only; no API call was made.

## Tool Action and Result

- Actor: GitHub Copilot under the bounded current-conversation runtime approval.
- `npm view cf version dist.integrity repository.url dist-tags --json`: version and repository matched the official release as above.
- `npm view cf@1.0.0-beta.5 bin scripts engines --json`: package entrypoint, scripts and Node requirement observed as above.
- `npx --yes --package cf@1.0.0-beta.5 cf --help`: pinned package ran from `C:/Users/yangjun/AppData/Local/Temp/rem-cf-m2-20260930-a91c7e4d2b63`; help displayed command groups including `dns`, `zone`, `workers`, `access`, `rulesets`, storage, security and observability.
- `npx --yes --package cf@1.0.0-beta.5 cf cli search 'list DNS records'`: returned five command matches, including `cf dns records list`. Query contained only action/resource type, following the CLI's instruction not to include domains, account/resource IDs, email or other identifying values.
- Two `npm exec` invocations returned npm usage text and did not start `cf`; the successful smoke used `npx`.
- `cf init <temporary>/worker-smoke --package-manager npm`: created an isolated generic Worker sample, installed 56 packages and generated `.cloudflare/types/index.d.ts`. The sample config had no account ID, domain, credentials or rem-specific data.
- `npm audit` in the temporary sample: 5 package findings (4 moderate, 1 high); the dependency path includes `undici` via `miniflare`, with `cf` / `@cloudflare/vite-plugin` in the affected graph. No `npm audit fix` or dependency upgrade was run. Do not copy this sample lockfile into rem without a fresh advisory review.
- `npm run typecheck` printed the generated types path and no TypeScript diagnostics; the final exit code was not separately captured.
- `npm run build` / `cf build`: Vite built the Worker bundle and printed `Build complete`; no account operation was requested.
- `npm run deploy -- --dry-run` reached a missing-authentication-token error after the local build; no token was supplied and no account request/deploy followed. Direct invocation of the sample's local `cf.cmd deploy --dry-run` then completed with exit code `0`, printed `--dry-run: exiting now`, and made no upload or API request.
- No `cf login`, `cf whoami`, account/Zone resource command, deployment, DNS mutation or resource API operation was run. No Cloudflare credentials were read. Package retrieval used public npm; no Cloudflare account cost was incurred or assessed.

## Decision and Blocker

**Subsequent content decision**: Owner authorized local content creation and later accepted [Mission/teamsbook.org/index.md](../teamsbook.org/index.md) for staging-preview preparation. It remains a non-authority draft; no HTML build, Cloudflare staging or publication occurred.

The bounded toolchain smoke supports using the official `cf` CLI as the candidate API tool, pinned to the tested beta version for any later approved experiment. The isolated generic sample verified typed-config generation, local build and the direct no-auth dry-run path, but npm reported a high-severity transitive dependency advisory. Owner accepted Worker Static Assets plus hostname-based Access for private portal/files at `rem.teamsbook.org`, Microsoft Entra SSO, shared read-only files, and an allow rule for any verified `@TeraTeams.com` email. The [capability matrix](../../Repo/days/2026-09-30/cloudflare-capability-matrix.md) records that this is domain-wide, not a named group.

Owner selected Free-only and staging->production and reports Zone/control and Free entitlement verified; these remain self-attestations, not independent account observations. Domain ownership/Entra claim mapping for `@TeraTeams.com`, acceptance of the content draft, any additional files, and rollback boundaries remain unresolved or unverified. Resource-level rem config/build and all account operations remain `not_run`.

M2 status is `Blocked`: C1=pass; C2=partial (candidate matrix, Access constraints and generic sample validated; exact rem resource matrix pending); C3=pass for candidate selection and single-tool ownership (`cf`); C4=blocked pending attributable Zone evidence, domain ownership/Entra claim mapping, actual content, Free entitlement, permissions and rollback; C5=pass for the absence of authenticated account/resource operations. M2 is not `Done` and does not authorize Cloudflare login, deployment or paid services.

Next bounded input: Owner confirms domain-wide `@TeraTeams.com` access is intended, supplies or identifies existing content (or separately approves content authoring and custody), provides attributable non-secret evidence for domain/Zone/Free claims, and defines rollback. No credentials are requested. M3 stays blocked until these inputs and specific external-action approvals are complete.
