# ARB 0.2 Mapping Update Review

**Status:** LOCAL PASS AFTER REMEDIATION
**Mode:** REVIEW TRACE
**Review time:** 2026-07-26T17:31:30+03:00
**Base commit:** `791b1ebbc3fae8c926de8c436bd64aa55ba99fc3`
**Candidate branch:** `docs/cross-spec-claim-boundaries`

## Scope

Reviewed public candidate files:

- `README.md`;
- `AGENTS.md`;
- `spec/00_SCOPE_AND_STATUS.md` through `spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`;
- `references/RELATED_PUBLIC_SPECS.md`;
- `review/PUBLICATION_MANIFEST.md`;
- `review/test_publication.py`;
- `.github/workflows/docs.yml`;
- `.gitignore`.

The review targeted semantic ownership, fixed-source parity, false equivalence, disclosure, executable publication checks, and diff integrity. It did not attempt to define a new normative specification or infer hidden implementation details.

## Owning source revisions

```text
MPAA:            1d369f6cd091b99f9492cfaf730f0a170b55106e
PCA:             6ad1a86d7c09b36839d162c580f84f05cfe4a598
BEC:             bb46f5f8aac96d1cffba7a334c5d17fb331ef3af
Review Protocol: 595c08b877e4dfb14593454c2eec7c8f5df46c28
```

All four public `main` references were resolved again before review. Nine exact source-file links used by ARB-04 were checked through the repository API.

## Separate-context adversarial pass

This was a separate-context adversarial review, not an independent implementation, external certification, or transfer of normative authority.

Initial severity header:

```text
P0: 0
P1: 1
```

### P1 — incomplete MPAA owning-surface list

ARB-04 initially labeled its list as **Exact files used for this mapping** but omitted:

- `spec/00_SESSION_BOOTSTRAP.md`, used for session-readiness claims;
- `spec/05_RUNTIME_REPORT_SCHEMA.md`, which owns the concrete Runtime Report representation used by `task_result` and evidence-object comparisons.

This was a real source-parity defect: the analytical claims reached owning surfaces not disclosed in the source list.

**Remediation:** both required files and their exact pinned links were added to ARB-04. Because the mapping also retains a general statement about MPAA internal architecture, `spec/01_AGENT_CORE.md` was added as the corresponding owning surface. The publication checker now requires all nine named source paths used by the mapping.

### P2 — delivery surface overstated

The first candidate said that MPAA may report runtime output in the `delivered` row. The pinned Runtime Report schema owns task result and execution-state/evidence representation, but does not define canonical delivery evidence; the Runtime Contract also distinguishes transmission from delivery.

**Remediation:** ARB-04 now says that MPAA may report task result/execution outcome, that its base Runtime Report schema does not define delivery evidence, and that delivery needs a separate evidence/extension or future owning surface.

### P2 — commitment and PCA receipts conflated

The first candidate used `commitment/transition receipt`, allowing a PCA transition receipt to be read as an alternative proof of operational commitment.

**Remediation:** ARB-04 now requires a commitment receipt from the owner that defines commit. If PCA continuation is also claimed, it additionally requires a separate PCA Transition Record and transition receipt.

The complete asynchronous finding summary became available after the first merge. These P2 findings were therefore closed in a corrective pull request rather than silently treated as part of the earlier pass.

## Boundary findings after remediation

- MPAA capability, authorization, invocation, evidence, verification, result, Identity Profile, session readiness, and Runtime Report remain owned by MPAA.
- BEC `closed` remains task-claim-tree closure and is not next-state commitment.
- PCA process continuation remains distinct from verified execution and identity-profile continuity.
- PCA `CORPUS` and ARB `PERSISTENT CORPUS` are explicitly partial mappings, not exact equivalence.
- ARB-03 remains a proposal and does not select a normative owner for cross-step commitment.
- PCA is limited to separately assessing a resulting transition; it is not presented as owner of an operational commit action.
- No neighboring result or conformance status is imported through vocabulary overlap or citation.

## Deterministic checks

```text
publication tests: 11 / 11 PASS
Python compile: PASS
pinned public main revisions: 4 / 4 resolved
pinned source-file links: 9 / 9 resolved
Markdown table shape errors: 0
broken relative links: 0
stale PCA nomenclature: 0
concrete local path findings: 0
credential-shaped findings: 0
named private identity/product findings: 0
exact 18-word copied blocks from neighboring public specs: 0
git diff --check: PASS
```

The publication checker intentionally does not claim to verify analytical truth, authenticate external evidence, or inspect hidden runtime behavior. Clean-runner results are recorded by the candidate commit's GitHub Actions checks.

## Verdict

```text
PASS AFTER P1 AND P2 REMEDIATION
```

No blocking disclosure or normative-ownership defect remains in the reviewed candidate. The result applies to the fixed source revisions and candidate state identified above; later changes require a new review.
