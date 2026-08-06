# Closure, Provenance and the Next Action

**Document:** ARB-03  
**Status:** PUBLIC DRAFT — PROPOSAL  
**Mode:** OPERATIONAL PROPOSAL  
**Version:** 0.3  
**Adopted:** No  
**Normative owner selected:** No  
**Multi-implementation conformance:** Not claimed

## 1. Problem

An agent can preserve the text of a completed turn while allowing the explanatory picture built during that turn to acquire more authority than its evidence supports.

This proposal distinguishes:

```text
preserving the result and obligations of a step
from
preserving automatic preference for the step's explanatory picture
```

It does not claim that deployed agent systems already implement this rule, and it is not presented as a universal property of language models.

## 2. Proposal boundary

This document is an illustrative proposal.

It does not select a normative owner. It does not amend BEC, MPAA, PCA, the Review Protocol, or CDTS. It does not create execution, delivery, persistence, retrieval, working-state admission, commitment, continuation, identity, or memory merely by naming those concepts.

```text
proposal published
  != proposal adopted
  != implementation exists
  != normative owner selected
  != conformance established
```

ARB-03 remains a proposal until an owning specification explicitly adopts a rule and supplies its own record contract, evidence requirements, validator, migration, and conformance boundary.

## 3. Candidate closure rule

After a task step closes, a system SHOULD preserve the smallest state required for correct continuation and review:

- result or explicit unresolved status;
- provenance needed to inspect the result;
- receipt or execution trace;
- open obligations;
- changes to the working environment;
- accepted constraints or amendments;
- a reference to the authority record applicable to the next action.

A hypothesis, temporary explanation, preferred reasoning path, or local picture SHOULD NOT gain automatic authority merely because it appeared in the previous turn.

Such an item may influence the next action only when it is represented as one of:

- an accepted rule or constraint;
- an explicit open obligation;
- a versioned artifact selected for the task;
- a candidate supported by current evidence;
- an explicitly declared assumption whose uncertainty is retained.

`SHOULD` is proposal language inside ARB-03. It does not impose an external requirement.

## 4. Illustrative closure record

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

This is an illustrative proposal, not a schema required by any neighboring artifact.

A field is a place to record evidence or an assertion. The field's presence does not establish that the event occurred or that the assertion is valid.

## 5. Closure is not commitment

The proposal preserves separate claims:

```text
BEC `closed` != `delivered`
`delivered` != `persisted`
`persisted` != `retrievable`
`retrievable` != admitted into working state
working state present != `committed`
`committed` != PCA process continuation
PCA process continuation != identity or memory
```

A closure record may reference receipts for these events, but its presence does not establish any of them.

In particular, `status: completed` is local to this illustrative ARB record and MUST NOT be renamed as:

- BEC `closed`;
- BEC `FULL-for-task`;
- MPAA authorization, task result, or conformance;
- a committed next state;
- PCA continuation status;
- CDTS trace admissibility;
- review receipt validity.

`MUST NOT` here protects the internal proposal boundary. It does not modify neighboring schemas.

## 6. Restoration before the next action

Before the next action, the proposal reconstructs task-relevant working state from declared inputs rather than treating the previous response as an undifferentiated instruction.

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

A restoration claim should distinguish:

```text
artifact existed
artifact was retrievable
artifact was retrieved
artifact was admitted into working state
artifact affected the next decision
```

## 7. Lawful continuation example

A step ends with:

```text
Status: partial
Open obligations:
1. run experiment A;
2. run experiment B;
3. compare the results before accepting the hypothesis.
```

The next action should continue this line. The reason is not textual momentum. The reason is the explicit, preserved obligation.

This example does not establish that the obligation was persisted or committed in any concrete runtime. Those are separate evidence questions.

## 8. Unsupported promotion example

A step proposes a plausible explanation and ends without evidence, acceptance, or an open test. The next response treats that explanation as established fact because it is already present in context.

This proposal classifies that transition as unsupported promotion. The explanation may remain available as a candidate, but its status must remain hypothetical until new evidence or explicit acceptance changes it.

## 9. Relationship to neighboring artifacts

### BEC

BEC owns task execution evidence, deployment level, return state, and remaining open work inside a BEC claim tree.

BEC `closed` explicitly does not establish next-state commitment. An ARB closure record cannot supply that missing event.

### MPAA

MPAA owns its architecture, Identity Profile, Runtime Contract, authorization, Runtime Report, validator meaning, and conformance procedure.

Some ARB-03 concepts could be candidates for a future runtime/state surface, but this proposal does not amend MPAA or grant authorization.

### PCA

PCA owns bounded process-continuation assessment across an explicit transition.

A closure record, execution result, persisted artifact, restored state, or commit event may be evidence for a later assessment. None establishes PCA status by itself.

### Review Protocol

The Review Protocol owns exact-source, discrepancy, receipt, and handoff discipline.

A review receipt may record that ARB-03 was inspected or implemented experimentally. It does not adopt the proposal or prove the implementation correct.

### CDTS

CDTS may correlate an ARB-03 proposal reference with separately owned records. Correlation does not make ARB the normative owner, validate the closure record, or prove that the records concern the same event.

The detailed mappings are in [`ARB-04`](04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md) and [`../RELATIONS.md`](../RELATIONS.md).

## 10. Candidate evidence questions

A future implementation should answer separately:

1. Was a result produced?
2. Was it delivered, and through which channel?
3. Was an artifact persisted under an identified retention boundary?
4. Was it retrievable by the intended next runtime?
5. Was it actually retrieved?
6. What was admitted into working state?
7. Under which authority was a next state committed?
8. Can the committed state be restored?
9. Does a separate PCA assessment claim process continuation?
10. Which parts remain unknown?

These questions are analytical guidance, not a conformance suite.

## 11. Validation status

This proposal has not undergone multi-implementation conformance testing.

A stronger status would require at least:

1. an owning specification and explicit adoption record;
2. a closed record contract or schema;
3. independent implementations;
4. tests where different prior hypotheses lead to the same next task state unless one has explicit authority;
5. tests where a declared open obligation correctly preserves a line of work;
6. failure reporting when provenance, retrieval, admission, or next-step authority is unknown;
7. migration and amendment rules;
8. a validator and conformance corpus owned by the adopting domain.

Until then, ARB-03 remains a proposal.

## 12. Proposal formula

> **Preserve results, provenance, obligations, and uncertainty; do not promote yesterday's explanation into today's authority without evidence or adoption.**
