# Agent and Reviewer Instructions

Review this repository as a public candidate, not as evidence about an unpublished source corpus.

## Source discipline

1. Use the exact public revisions listed in `references/RELATED_PUBLIC_SPECS.md`.
2. Do not reconstruct missing private material from names, prior chats or memory.
3. Report source discrepancies before drawing architectural conclusions.
4. Do not treat this repository as canonical for MPAA, PCA or BEC.

## Claim discipline

- Keep OBSERVATION, FUNCTIONAL RECONSTRUCTION, ANALYTICAL INTERPRETATION, PROPOSAL and UNKNOWN distinct.
- Do not infer physical model modules from functional boundaries.
- Do not infer execution from fluent text or a visible progress label.
- Do not infer continuity from a name, style or retained artifact alone.
- Do not grant a prior hypothesis authority merely because it appears earlier in the corpus.

## Public-boundary discipline

Stop review and report a blocking issue if the repository contains:

- a named private person or agent;
- a named model, provider or product not required as a public specification reference;
- a private event, correspondence excerpt, source-share link or account identifier;
- a local filesystem path;
- a credential, token, secret or protected endpoint;
- a mapping that allows reconstruction of an unpublished source corpus.

## Review output

A useful review contains:

```text
reviewed commit or candidate timestamp
exact files reviewed
blocking issues
non-blocking issues
unknowns
final readiness status
```

Do not expand the theory during a disclosure review. Review the candidate that exists.
