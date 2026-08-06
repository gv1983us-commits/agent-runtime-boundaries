# Agent and Reviewer Instructions

Review this repository as a canonical public analytical artifact, not as a normative specification and not as evidence about hidden runtime internals or an unpublished source corpus.

## Reading order

1. `CANON.md`
2. `ARTIFACT.json`
3. `spec/00_SCOPE_AND_STATUS.md`
4. `spec/01_FUNCTIONAL_BOUNDARIES.md`
5. `spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md`
6. `spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md`
7. `spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`
8. `RELATIONS.md`
9. `PROVENANCE.md`
10. `references/RELATED_PUBLIC_SPECS.md`

## Source discipline

1. Use the exact public revisions listed in `references/RELATED_PUBLIC_SPECS.md`.
2. Distinguish a moving branch from the exact revision actually inspected.
3. Do not reconstruct missing private material from names, prior chats, summaries, or memory.
4. Report source discrepancies before drawing analytical conclusions.
5. Do not treat ARB as canonical for BEC, MPAA, PCA, the Review Protocol, or CDTS.
6. Use `spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md` and `RELATIONS.md` for mappings; do not infer an unstated equivalence.

## Zero-normative-surface discipline

ARB declares:

```text
normative_surface_count = 0
analytical_surface_count = 4
proposal_surface_count = 1
```

Do not:

- relabel an ARB distinction as a neighboring requirement;
- describe ARB-03 as adopted;
- select a normative owner for ARB-03 without an owning-repository change;
- call the publication checker a conformance validator;
- report an ARB interpretation as proof of physical module separation;
- make ARB the normative owner of a CDTS trace or external record.

## Claim discipline

Keep these classes distinct:

```text
OBSERVATION
FUNCTIONAL RECONSTRUCTION
ANALYTICAL INTERPRETATION
PROPOSAL
UNKNOWN
```

Preserve these boundaries:

```text
model output != verified reasoning
reasoning about an action != execution
visible status != execution evidence
stored != retrieved
retrieved != active working state
delivered != persisted
persisted != retrievable
retrievable != admitted into working state
working state present != committed
BEC closed != next-state commitment
committed != PCA process continuation
process continuation != identity or memory
```

## Public-boundary discipline

Stop review and report a blocking issue if the repository contains:

- a named private person or agent not required by the public artifact;
- a private event, correspondence excerpt, source-share link, or account identifier;
- a local filesystem path;
- a credential, token, secret, private key, or protected endpoint;
- a mapping that permits reconstruction of an unpublished source corpus;
- a claim of hidden-runtime observation without addressable public evidence.

Public names of the six technical artifacts, their repositories, Claude (Anthropic) as corpus representation, and JARVIS OS inside the reviewed donor-profile boundary are allowed only where required to describe public sources accurately.

## Change discipline

A substantive change should identify:

```text
analytical or proposal surface
claim class
exact neighboring revisions
permitted inference
forbidden inference
publication-test impact
relation impact
provenance impact
```

Updating a SHA without inspecting semantic changes is not a relation update.

## Review output

A useful review contains:

```text
reviewed commit or candidate timestamp
exact files reviewed
source receipt
blocking issues
non-blocking issues
unknowns
proposal-boundary status
zero-normative-surface status
final publication readiness
```

Do not expand the theory during a disclosure review. Review the candidate that exists.
