# EGO DNS Register

> **Player**: yangjun / bitguts
> **Authority**: rem EGO
> **Purpose**: Register EGO-owned DNS domain identities and their intended use.

This register is the canonical home for EGO's DNS-domain intent. It does not configure DNS, prove registration/control, establish a Cloudflare Zone, or authorize external changes.

## Record Contract

- One canonical Markdown record per registered root domain.
- A record separates the Player's intended use from verified registrar, delegation, account, and Zone facts.
- `target / unverified` means the EGO target is selected but domain control and DNS operation have not been verified.
- Hostnames and URLs are separate from root-domain identity and require an explicit delivery decision.
- Provider choice, Cloudflare stack design, CLI selection, live DNS records, and credentials do not belong in this register.
- EGO instances link to the canonical record; they do not repeat its domain value as another source of truth.

## Current Record

- [teamsbook.org](teamsbook.org.md): rem external delivery root-domain target; Player reports the delivery hostname operational, while registrar/registrant identity remains unknown and independent account/DNS re-check is pending.
