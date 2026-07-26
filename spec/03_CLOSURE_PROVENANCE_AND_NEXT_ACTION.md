# Closure, Provenance and the Next Action

**Document:** ARB-03
**Status:** PUBLIC DRAFT — PROPOSAL
**Mode:** OPERATIONAL PROPOSAL
**Version:** 0.2

## 1. Problem

An agent can preserve the text of a completed turn while allowing the explanatory picture built during that turn to acquire more authority than its evidence supports.

This proposal distinguishes:

```text
preserving the result and obligations of a step
from
preserving automatic preference for the step's explanatory picture
```

It does not claim that deployed agent systems already implement this rule, and it is not presented as a universal property of language models.

## 2. Candidate closure rule

After a task step closes, a system SHOULD preserve the smallest state required for correct continuation and review:

- result or explicit unresolved status;
- provenance needed to inspect the result;
- receipt or execution trace;
- open obligations;
- changes to the working environment;
- accepted constraints or amendments;
- a reference to the authority record applicable to the next action.

A hypothesis, temporary explanation, preferred reasoning path or local picture SHOULD NOT gain automatic authority merely because it appeared in the previous turn.

Such an item may influence the next action only when it is represented as one of:

- an accepted rule or constraint;
- an explicit open obligation;
- a versioned artifact selected for the task;
- a candidate supported by current evidence;
- an explicitly declared assumption whose uncertainty is retained.

## 3. Closure record

A minimal closure record can be represented as:

```yaml
step_id: string
status: completed | partial | blocked | refused
result_refs: []
provenance_refs: []
receipt_refs: []
open_obligations: []
state_changes: []
accepted_constraints: []
next_authority_ref: string | unknown
retained_candidates:
  - claim: string
    status: accepted | open | hypothetical | unknown
    evidence_refs: []
```

This is an illustrative proposal, not a schema required by MPAA, PCA or BEC.

### 3.1 Closure is not commitment

The proposal preserves separate claims:

```text
BEC `closed` != `delivered`
`delivered` != `persisted`
`persisted` != `retrievable`
`retrievable` != admitted into working state
working state present != `committed`
`committed` != PCA process continuation
```

A closure record may reference receipts for these events, but its presence does not establish any of them. In particular, `status: completed` is local to this illustrative ARB record and MUST NOT be renamed as BEC `closed`, BEC `FULL-for-task`, a committed next state, or a PCA result.

The detailed ownership and evidence mapping is in [ARB-04](04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md). ARB-04 identifies candidate homes for future rules but does not select a normative owner.

## 4. Restoration before the next action

Before the next action, the system reconstructs task-relevant working state from declared inputs rather than treating the previous response as an undifferentiated instruction.

```text
mission or active objective
current task
accepted constraints
open obligations
selected sources and versions
available capabilities
current environment state
applicable authority
```

The previous response may be a source, but it is not automatically the authoritative source.

## 5. Lawful continuation example

A step ends with:

```text
Status: partial
Open obligations:
1. run experiment A;
2. run experiment B;
3. compare the results before accepting the hypothesis.
```

The next action should continue this line. The reason is not textual momentum. The reason is the explicit, preserved obligation.

## 6. Unlawful promotion example

A step proposes a plausible explanation and ends without evidence, acceptance or an open test. The next response treats that explanation as established fact because it is already present in context.

This proposal classifies that transition as unsupported promotion. The explanation may remain available as a candidate, but its status must remain hypothetical until new evidence or explicit acceptance changes it.

## 7. Relationship to public specifications

- BEC owns task execution evidence, deployment level, return state, and remaining open work inside a BEC claim tree. BEC `closed` explicitly does not establish next-state commitment.
- PCA owns bounded process-continuation assessment across an explicit transition. A closure record, execution result, or restored artifact does not establish PCA continuation.
- MPAA owns its architecture, Identity Profile, Runtime Contract, authorization, Runtime Report, and MPAA conformance. A free-form authority reference does not grant authorization or alter those layers.
- ARB owns none of those normative results. This proposal preserves distinctions and candidate fields only.

[ARB-04](04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md) records the exact pinned revisions, allowed mappings, forbidden inferences, evidence requirements, and unresolved candidate homes. A citation carries a trace; it does not import the cited system's conclusion.

## 8. Validation status

This rule has not yet undergone multi-implementation conformance testing. A stronger status would require at least:

1. independent implementations of the closure record;
2. tests where two different prior hypotheses lead to the same next task state unless one has explicit authority;
3. tests where a declared open obligation correctly preserves a line of work;
4. failure reporting when provenance or next-step authority is unknown.

Until then, the document remains a proposal.
