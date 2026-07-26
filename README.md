# Agent Runtime Boundaries

**Status:** Public draft 0.2
**Mode:** Descriptive and analytical companion material
**Normative force:** None outside explicitly identified proposals

## Purpose

Agent Runtime Boundaries (ARB) is a vendor-neutral guide to distinctions that are easy to blur in model-based agent systems.

It separates:

```text
human participant
agent
model
runtime / host
platform / control plane
working state
persistent corpus and memory
resources and tools
evidence and user-visible observability
```

The repository does not assert that every implementation contains the same physical modules. It identifies functional responsibilities that can vary independently and can be inspected, tested, or reported without guessing a hidden implementation.

## Core distinctions

```text
model output != verified reasoning
reasoning about an action != execution of that action
stored information != retrieved information
retrieved information != active working state
visible status != execution evidence
response delivery != committed state transition
BEC closed != next working state committed
identity-profile continuity != process continuation
human participant != technical component
```

## Relationship to existing specifications

ARB is a non-normative analytical companion to:

- Minimal Portable Agent Architecture (MPAA);
- Process Continuity Architecture (PCA);
- Behavioral Execution Contract (BEC);
- Repository Canon and Review Protocol.

It does not amend, replace, or become canonical for any of them. Each referenced specification owns its own terms, records, validation, and result domain.

The four-way mapping is in [`spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`](spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md). Exact reviewed revisions are in [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md).

## Reading order

1. [`spec/00_SCOPE_AND_STATUS.md`](spec/00_SCOPE_AND_STATUS.md)
2. [`spec/01_FUNCTIONAL_BOUNDARIES.md`](spec/01_FUNCTIONAL_BOUNDARIES.md)
3. [`spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md`](spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md)
4. [`spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md`](spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md)
5. [`spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`](spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md)
6. [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md)

## ARB-03 status

ARB-03 remains an operational proposal. ARB-04 identifies possible normative homes for closure and next-state concepts but does not select one. No closure-record field creates authorization, BEC acceptance, PCA continuation, identity continuity, or a committed next state by itself.

## Publication checks

```bash
python -m unittest discover -s review -p "test_*.py" -v
```

The checker verifies fixed source revisions, required mapping surfaces, analytical/non-normative boundaries, relative links, Markdown integrity, declared document status, and absence of local path or credential markers. Passing it establishes repository consistency only, not the truth of neighboring records or hidden runtime behavior.

## Publication status

The 0.1 baseline was published on 2026-07-25. Draft 0.2 adds a fixed-revision cross-specification mapping and automated publication checks. It remains descriptive/analytical companion material and does not amend MPAA, PCA, BEC, or the Review Protocol.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
