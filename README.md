# Agent Runtime Boundaries

**Status:** Draft public candidate 0.1 — not yet published
**Mode:** Descriptive and analytical companion material
**Normative force:** None outside explicitly identified proposals

## Purpose

Agent Runtime Boundaries is a vendor-neutral guide to distinctions that are easy to blur in model-based agent systems.

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

The repository does not propose that every implementation contains the same physical modules. It identifies functional responsibilities that can be inspected, tested, or reported without guessing a provider's hidden implementation.

## Core distinctions

```text
model output != verified reasoning
reasoning about an action != execution of that action
stored information != retrieved information
retrieved information != active working state
visible status != execution evidence
response delivery != committed state transition
human participant != technical component
```

## Relationship to existing specifications

This repository is a non-normative companion to:

- Minimal Portable Agent Architecture (MPAA);
- Process Continuity Architecture (PCA);
- Behavioral Execution Contract (BEC);
- Repository Canon and Review Protocol.

It does not amend, replace, or become canonical for any of them. Each referenced specification owns its own normative scope. Exact reviewed revisions are listed in [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md).

## Reading order

1. [`spec/00_SCOPE_AND_STATUS.md`](spec/00_SCOPE_AND_STATUS.md)
2. [`spec/01_FUNCTIONAL_BOUNDARIES.md`](spec/01_FUNCTIONAL_BOUNDARIES.md)
3. [`spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md`](spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md)
4. [`spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md`](spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md)
5. [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md)

## Publication status

This folder is a candidate, not a released repository. It MUST NOT be published until:

- an independent disclosure and scope review is complete;
- the public repository name and owner are confirmed;
- a public license is selected;
- the publication manifest reports no blocking issue.

## License

This candidate is licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
