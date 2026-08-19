# S06 — Optional Local Pre-extraction

**Execute only S06, then stop.**  
**Input:** representative/all TTK Map packets from S05  
**Next:** S07

## Outcome

Determine whether a cheap local pre-extractor earns a role as **hints only** before the strong semantic Map. It must never become final semantic authority.

## Context to load

- this file;
- S05 handoff and selected representative packets;
- `preextract_gliner2` registry entry;
- `preextract_nuextract` entry only if the GLiNER2 trigger fires;
- existing local tool adapter code for these components, if any.

Do not read Reduce/evaluation history.

## Recommended experiment

Reference lane: **no pre-extraction**.  
Primary challenger: **real GLiNER2 local**.  
NuExtract only if GLiNER2 demonstrably fails the intended cheap-IE role and the additional test is still material.

## Work

1. Select a small representative packet set including EN and DE if available for this implementation cycle.
2. Install/use GLiNER2 in its isolated environment; record exact package/model version.
3. Run actual extraction for narrow hint categories such as people, organizations, products, technologies, financial instruments, or relations where schema support exists.
4. Save hints separately from TTK source evidence.
5. Inspect false/noisy hints and usefulness.
6. Decide `USE_HINTS_FOR_S07`, `DO_NOT_USE`, or `BLOCKED`.
7. If `DO_NOT_USE` because GLiNER2 does not satisfy the role and NuExtract is plausibly useful, a bounded NuExtract test is allowed; otherwise do not add it.

## Hard boundary

Never use regex/keyword code, GLiNER2, or NuExtract to decide final thesis, claim truth/support, mechanisms, arguments, Meso structure, or Macro synthesis.

## Tests

- actual package/model identity is proven;
- hints point to source text rather than invented entities;
- German behavior is explicitly observed when tested rather than assumed;
- hints are stored as non-authoritative sidecars;
- S07 can run with hints disabled;
- no fake component implementation is created under a real component name.

## Outputs

- `<run>/preextract/decision.yaml`;
- optional real hint sidecars keyed by packet ID;
- install/smoke metadata where needed;
- S06 handoff.

Handoff must say whether S07 receives hints, which packets/hint paths, component/version, and known failure/noise modes.

A blocked/losing challenger does **not** fail the overall pipeline; it simply exits the hot path.

Commit/push stage code/test changes, return handoff, **STOP.**