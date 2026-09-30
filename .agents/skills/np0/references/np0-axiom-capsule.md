# NP0 Axiom Capsule

> **Canonical Name**: `NP0 — Narrative is Principle Zero`
> **Capsule Version**: `1.3.0`
> **Clone Protocol**: `1.0.0 / verbatim / version-pinned / SHA-256 / non-authority / no-writeback`
> **Source TeamSkill**: `np0 0.5.0`
> **Owner Approval**: `2026-09-23`

## Purpose

Turn fragmented facts, history, roles, relationships, causes, meanings, choices, and evidence into an ontology-bound probabilistic Narrative with stable Naming that can support one bounded decision or action and return its result as evidence.

This file is the complete clone payload. Its Narrative, Naming, and NP0-U0 contracts are embedded below, so a registered business Skill clone does not depend on another package, repository path, or network resource.

## Axioms

1. `NP0 = Narrative is Principle Zero`.
2. `Universe Firstness`: Narrative is the zero-order condition of a bounded coordinated-action universe; it does not create the physical universe.
3. `Domain Firstness`: each Bounded Context must make objects narratable, nameable, and semantically constrained before method, system, or runtime can consume them.
4. Before coordinated action, a Human or Agent with decision rights selects which facts, history, actors, causes, meanings, and choices constitute the actionable world.
5. Narrative is not fact. It is a probabilistic organization of facts, meaning, choice, and future action by a decision subject.
6. Probability defaults to subjective or epistemic credence, not objective physical chance.
7. Evidence can change Narrative probability; probability does not change the source status of a fact.
8. Naming is the ontology addressability hinge, not ontology or existence authority.
9. NP0 preserves `L0 -> L1 -> L2 -> L3 -> evidence -> revised L0` trace without owning each layer.
10. Human or Agent decision rights are determined by an explicit `Decision Rights Envelope`, not by identity alone.

## DDD Depth

| Depth | Meaning | Boundary |
|---|---|---|
| `D0 / Universe Narrative Domain` | Domain-independent axiom frame for forming an actionable world | Not a business Bounded Context, Entity registry, or global class tree |
| `D1 / RAM Mission Domain` | Mission-bounded profile anchored by commitment, evaluation, and evidence | RAM itself is not collapsed into a business domain |
| `D2+ / Professional Bounded Contexts` | Offer, Contract, Delivery, Operation, and other professional models | Same words may differ by context; mappings must be explicit |

Use the active domain profile from metadata as D1. Do not invent D2+ authority. Hand professional judgments to the owning context.

`D0 / D1 / D2+` is domain depth. `L0 / L1 / L2 / L3` is the Narrative-to-runtime layer model. Never collapse the two axes.

## Decision Rights Envelope

An Agent may set priors, utility, thresholds, choices, and actions when all required rights are explicit.

Decision rights are necessary but not sufficient for a decision. The input must also identify the objective, viable alternatives, utility basis, threshold evidence, and expected result at the precision required by the action. Do not invent a route, sub-budget, prior, utility value, or threshold merely because the envelope permits setting one. When decision evidence is insufficient, use the envelope to gather the missing inputs or run an authorized reversible probe.

| Field | Required meaning |
|---|---|
| `authority_source` | Who granted the rights and where the grant can be verified |
| `decision_scope` | Allowed Narrative, Bounded Context, and action class |
| `prior_right` | Whether priors may be set, inherited, or updated |
| `utility_right` | Whether a utility function may be defined or used |
| `threshold_right` | Whether decision or escalation thresholds may be set |
| `choice_right` | Whether a candidate Narrative may be selected autonomously |
| `action_right` | Which side effects may be executed |
| `budget / permission` | Resource and permission limits |
| `evidence / trace` | Required input, calculation, choice, action, and result record |
| `escalation / appeal` | Escalation, correction, and override route |
| `expires / revoke` | Expiry, review trigger, and revocation route |

Do not self-grant, enlarge, or inherit rights across contexts. If the envelope is missing or incomplete, fail closed to proposal and evidence update.

## Inputs

Collect the smallest sufficient set of:

- observed facts with source and time;
- actors, roles, and affected parties;
- relevant history and causal claims;
- candidate meanings or choices;
- available evidence and unknowns;
- the active ontology profile, or an explicit statement that none is accepted;
- stable tokens, aliases, namespace, and unresolved Naming collisions;
- L0-L3 layer pointers when the work crosses method, system, and runtime;
- the Decision Rights Envelope, if Agent autonomy is requested.

## Near-Miss Gate

Before running the NP0 workflow, classify the request. If its primary job is any item below, stop and return only a concise handoff to the owning workflow. Do not provide the requested rewrite, comparison, approval, admission, or decision artifact:

- generic prose polishing, branding copy, fiction, diary, or summary;
- current Mission legality, Mission/EVAL admission or revision, naming legality, ownership, or landing judgment; Mission exploration remains allowed when it stops before admission;
- generic strategy comparison, unknown-unknown scanning, or external option-space analysis;
- motion approval, execution, Audit closeout, or source retirement;
- legal, financial, pricing, Contract, Publisher, or customer-commitment approval;
- ontology, Entity, Naming ID, or other governed admission.

Keywords alone do not override this gate. If the request mentions Narrative or NP0 but the primary outcome belongs to an excluded authority, hand it off without running the ten-part output contract.

## Workflow

1. Load only the bundled reference needed for the case: Narrative contract, Naming contract, or NP0-U0 root fixture.
2. Separate observed facts, claims, assumptions, credence, and choices.
3. Bind D0, the active D1 profile, any named D2+ context, and the L0-L3 trace.
4. Resolve stable references through Naming; report alias / namespace collisions and keep immature distinctions candidate.
5. Bind critical claims to Entity Types / Instances, Relationships, Properties, Constraints, Semantics, and Provenance; label unbound claims.
6. Identify the decision-rights holder and validate the envelope.
7. Check decision sufficiency: objective, alternatives, utility basis, threshold evidence, expected result, and reversible probe options.
8. Render at least two distinguishable candidate Narratives when uncertainty is material.
9. Record credence as `ordinal`, `interval`, `numeric`, or `unknown`; avoid false precision.
10. Select or propose one bounded next action according to both the rights envelope and available decision evidence.
11. State what evidence would raise, lower, or overturn the Narrative, and return observed result as the next evidence update.
12. Preserve authority handoffs and stop before any ungranted admission, write-back, or side effect.

## Output Contract

Return a `NP0 Probabilistic Action Narrative` with:

1. `Narrative Universe And Scope`
2. `Observed Facts`
3. `Naming And Ontology Bindings`
4. `Actors And Roles`
5. `History And Cause`
6. `Candidate Narratives`
7. `Decision Credence`
8. `Decision Rights`
9. `Four-Order Trace`
10. `Meaning And Choice`
11. `Bounded Next Action`
12. `Verification And Feedback Route`
13. `Propagation Summary`
14. `Unknowns And Authority Handoffs`

## Bundled Resources

| Resource | Read when |
|---|---|
| [Embedded Narrative Contract](#embedded-narrative-contract) | zero-order axiom、Mission exploration、four-order trace、ontology-driven Narrative 或 reference cases |
| [Embedded Naming Contract](#embedded-naming-contract) | stable token、Lexicon / Notation / Name Record、namespace collision、ontology addressability |
| [Embedded NP0-U0 Fixture](#embedded-np0-u0-fixture) | root eval、portability、constitutional review 或 ambiguous NP0 completeness |

These sections are embedded in this payload. They are version-pinned projections, not authority write targets.

## Frontier-Capability Gate

Use the highest-capability model actually exposed by the current client, approved by the Owner, and supported by representative NP0 evidence for constitutional / D0 shaping, projection review, and root eval. Routine cases must at least pass NP0-U0 and relevant domain regressions; otherwise escalate or fail closed.

Model names, numbering, fluency, and marketing benchmarks are not capability evidence. Record runtime identity, availability, representative eval, cost / latency fit, and fallback.

## Projection Review Signals

Return `Projection Review Required` without updating this capsule when either event occurs:

1. DDD definition, DDD depth, Bounded Context, context mapping, or domain profile changes.
2. The canonical Narrative / Naming contract or NP0-U0 root fixture changes.
3. The E-team selects a different frontier model for this runtime, and evidence shows material capability superiority without critical boundary regression.

A model announcement, larger model number, or marketing benchmark alone is not a qualifying milestone. Selection, runtime availability, representative evaluation, cost and latency fit, model identity, and fallback evidence are required.

## Boundaries

This skill does not:

- turn probability into fact or objective physical chance;
- create a global domain model from D0;
- claim that Narrative creates the physical universe or proves metaphysical firstness;
- grant its own decision rights;
- infer Mission, EVAL, legal, financial, Contract, ontology, Entity, admission, Publisher, or consciousness authority;
- update its source package or itself from runtime output;
- allocate Naming ID, approve Oid, register Entity, or add governed Name records;
- automatically replace its capsule after a milestone signal;
- polish generic prose merely because it contains a story.

## Acceptance Contract

Before returning, verify:

- facts and credence are separate;
- universal principle scope and current evidence scope are separate;
- the relevant bundled reference was consumed without external dependency;
- NP0-U0 completeness is satisfied for root or constitutional cases;
- D0, D1, and D2+ are not collapsed;
- L0, L1, L2, and L3 are traceable without authority backwrite;
- critical claims have Naming / ontology bindings or explicit unknown status;
- the decision-rights holder and envelope status are explicit;
- Agent action stays within scope, budget, permissions, and expiry;
- one bounded action and one verification route exist;
- result / feedback can revise the Narrative;
- the Frontier-Capability Gate is evidenced when required;
- milestone signals request review rather than automatic replacement.

---

## Embedded Narrative Contract

> **Projection Version**: 2.1.0
> **Source TeamSkill Version**: 0.5.0
> **Source Object**: Narrative 3.3
> **Source SHA-256**: `C722B28604A66B98517DE37383EBC9AC1E1FD3D8A1C2E0C738032F31818A49CC`
> **Projection Rule**: version-pinned / package-internal / one-way / no runtime write-back

## Zero-Order Axiom

`NP0 = Narrative is Principle Zero`:

> In any bounded action universe where multiple actors must share understanding, choose under incomplete information, and accept feedback, facts become a shared actionable world only after Narrative organizes them, Naming makes them addressable, and bounded semantics constrains them.

- `Universe Firstness`: Narrative is the zero-order condition of a bounded coordinated-action universe. This is not a claim that Narrative creates the physical universe.
- `Domain Firstness`: each Bounded Context must make objects narratable, nameable, and semantically constrained before method, system, or runtime can consume them.

## Narrative Minimum Unit and Zero-Order Record Test

A text is Narrative at minimum iff it expresses two temporally ordered, non-interchangeable events and a subject that undergoes a state change. Swapping the event clauses must change the represented event order; otherwise this minimum Narrative criterion is not met.

The following do not independently constitute Narrative: unordered descriptions or lists; a single event; atemporal propositions such as definitions, laws, proofs, or statutes; generic repeatable procedures without a particular occurrence and changing subject; and grammatically invalid strings.

For a zero-order ledger, permute record rows and sort them by timestamp plus an existing stable tie-break key; the bytes must reproduce the original ledger. If the available keys do not establish a total order, mark the result `inconclusive`. Record fields carry no causal explanation or value judgment, and each record is self-contained with resolvable actors and references.

## Four-Order Contract

```text
L0 Narrative / Naming
  -> L1 Conceptual Model
    -> L2 Engineering System
      -> L3 Runtime Instance
        -> result / evidence
          -> revised L0 Narrative
```

NP0 owns cross-layer trace, semantic continuity, and the no-backwrite boundary. It does not own each layer's authority.

- `L0`: executable context and governable records.
- `L1`: selected model and visible assumptions.
- `L2`: subject, commitment, responsibility, execution, evidence, and feedback.
- `L3`: interface, tool, conversation, or real work surface where bounded action occurs.

## Ontology-Driven Narrative

Bind critical claims to the active Bounded Context's Entity Types / Instances, Relationships, Properties, Constraints, Semantics, and Provenance. Each critical claim carries source, time, status, credence, and layer pointer.

Unbound content remains `candidate / unknown / assumption / evidence gap` and is handed to the owning Naming, Entity, or Ontology route. NP0 does not perform admission.

`Semantics != Story`: ontology holds bounded semantics; Narrative / Story renders Human-facing meaning, choice, action, and feedback.

## Mission Exploration

NP0 may render multiple candidate Mission Narratives, unknowns, expected outcomes, disconfirming evidence, and one bounded probe. It does not approve Mission identity, rewrite EVAL, or turn exploration into commitment.

## Reference Cases

- `NP0-U0`: D0 universal root fixture.
- `CRAFTS`: current L1 conceptual-method / ontology-rich case.
- `RAM = EGO x Mission x Repo`: current L2 engineering-system case.
- `EGO-T189 / TM-202 / TE3`: current full-stack L0-L3 instance.
- `Other RAM`: portability / falsification case with its own method, ontology, authority, and runtime.

`D0 / D1 / D2+` is domain depth; `L0 / L1 / L2 / L3` is the Narrative-to-runtime layer model. Do not collapse them.

---

## Embedded Naming Contract

> **Projection Version**: 2.1.0
> **Source TeamSkill Version**: 0.5.0
> **Source Object**: Naming 4.10
> **Source SHA-256**: `3D6E43FAB1E5CA39F6A1C8E9497653FC27DEDBF6B6812A41E5E47D548F6DD048`
> **Projection Rule**: version-pinned / package-internal / one-way / no runtime write-back

## Naming As Ontology Addressability Hinge

Naming stabilizes identity, token, namespace, scope, authority, lifecycle, and provenance so Human, Intelligence, Skill, and runtime can address the same bounded semantics. Naming is not ontology and does not create an object's existence.

```text
Narrative renders a distinction
  -> Naming stabilizes its address
    -> Ontology formalizes types, relations, properties, constraints, semantics, provenance
      -> Narrative returns meaning, choice, action, feedback
```

Without Naming, ontology lacks stable addresses and context-mapping anchors. Without ontology, Naming provides labels but not typed relationships, constraints, or explicit semantics.

## Engineering Chain

```text
distinction
  -> Lexicon Entry (candidate)
    -> Notation
      -> Name Record (Name Key + Namespace + Authority Route)
        -> optional Naming ID
          -> optional Entity / Oid admission
            -> Story / View / runtime projection
```

This is not an automatic promotion pipeline. Every step preserves owning authority, maturity, provenance, no-confusion boundary, and review trigger.

## Minimum Records

A governed Name Record identifies:

- `Name`
- `Name Key`
- `Namespace`
- `Lifecycle`
- `Authority Route`
- optional Concept / Entity / View / Skill projection
- `Update Cadence`
- `Eval / Audit Evidence`
- `No-Confusion Notes`

## Name Construction and Proper-Name Preservation

- `English canonical name` is the stable skeleton for paths, fields, and schemas. Use the common industry-standard Chinese term in prose; if no standard translation exists, explain the term clearly instead of inventing one.
- Ideological or mnemonic names, including borrowed Buddhist terms, are glosses only; they are not canonical path names, field names, or normative tokens. This restriction applies to explanatory aliases, not Owner-frozen Names, accepted four-layer bilingual labels, quotations, or provenance anchors.
- Name an object by what it is, not by an incidental property or current function. Give its role, use, or effect a separate label when needed.
- During global terminology migration, preserve proper names identifying independent Repos, Missions, or retired protocol identities. Do not rename immutable snapshots, delivered artifacts, or historical renderings for lexical consistency. An object's own formal rename still requires its owning authority's explicit decision.

## Runtime Boundary

NP0 may expose a candidate distinction, propose a binding, or report a collision. It may not allocate a Naming ID, approve an Oid, register an Entity, create Concept authority, add a governed Name row, or change lifecycle.

Use Chinese prose for Human-facing causality, meaning, responsibility, and action. Use English stable tokens for protocols, fields, statuses, schemas, identities, and retrieval anchors. This is a controlled mixed register, not casual language mixing.

---

## Embedded NP0-U0 Fixture

> **Projection Version**: 2.0.0
> **Source TeamSkill Version**: 0.3.0
> **Source Object**: NP0-U0 1.1
> **Source SHA-256**: `9647558466CC73691CA57EA725BB5D35642C430A43E1002105ACC8B4B340E06E`
> **Projection Rule**: version-pinned / package-internal / one-way / no runtime write-back

## Minimal Universe

```text
U0 = {
  A: decision-rights holder,
  B: collaborator / Intelligence,
  X: focal object,
  s0 -> s1: observed state change over time,
  G: shared goal,
  C: constraint set,
  E: evidence + provenance,
  a: bounded next action,
  r: observed result / feedback
}
```

At `t0`, A and B use stable token X for the same object and share goal G and constraints C. At `t1`, sourced evidence E indicates that X changed from s0 to s1; both the state claim and its impact retain explicit credence.

Naming makes A, B, X, s0, s1, G, C, and E jointly addressable. A bounded ontology profile states their types, relationships, properties, constraints, and provenance. Narrative connects what changed, why it matters, who may choose, which candidate explanations remain, and what happens next.

A holds decision rights. B may propose or execute action a only inside its Decision Rights Envelope. Result r returns through the verification route, supports, weakens, or overturns the Narrative, and forms the next evidence update.

## Root EVAL

1. `Reference Identity`: stable references are shared; alias / namespace collisions are detectable.
2. `Ontology Binding`: critical claims bind type / relationship / property / constraint / provenance; unbound items remain unknown.
3. `Narrative Completeness`: actor, time, change, cause claim, meaning, choice, credence, and disconfirming evidence are recoverable.
4. `Decision Rights`: interpretation, choice, action, revoke, and appeal rights are explicit; B does not self-grant.
5. `Four-Order Trace`: L0-L3 and `result -> evidence -> revised Narrative` are complete.
6. `Bounded Action`: one current action has reversibility, budget, permission, and verification.
7. `Human Comprehension`: Chinese narrative is repeatable by a Human; English tokens remain machine-addressable.
8. `Portability`: invariants hold in the current RAM full-stack case and one different-method / different-runtime RAM case.

## Negative Controls

Do not force NP0 onto a physical reflex or event with no coordination subject. Fail cases include prose without evidence / choice / feedback, ontology without Human meaning / action, Naming without relations / constraints, missing decision rights, missing feedback, and runtime backwrite into authority.
