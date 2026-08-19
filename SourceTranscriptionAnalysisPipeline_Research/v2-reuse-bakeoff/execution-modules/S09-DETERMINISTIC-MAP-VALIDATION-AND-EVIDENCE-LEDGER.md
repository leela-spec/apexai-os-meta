# S09 — Deterministic Map Validation and Evidence Ledger

**Execute only S09, then stop.**  
**Input:** S07 Map outputs through the S08 hardened seam  
**Next:** S10

## Outcome

Validate every Map result against TTK's deterministic source/provenance invariants and produce the trusted evidence ledger consumed by later semantic synthesis.

## Context to load

- this file;
- S07 and S08 handoffs;
- actual TTK packets/results;
- TTK Map validation and reduce-packet construction code/tests;
- semantic contract sections for factual evidence and source references.

Do not load external verification or final evaluation files.

## Authority boundary

This stage decides **mechanical validity**, not semantic truth.

Deterministic code may verify:

- packet/result identity and freshness;
- source segment existence;
- `core` vs `context_only` eligibility;
- exact quote/span existence when required;
- required coverage;
- schema/field/reference integrity;
- stale hashes and unresolved references.

It must not decide that a proposition is semantically supported merely because its quote exists.

## Work

1. Run TTK validation over all S07 results.
2. Produce a precise invalid-packet list, not a generic FAIL.
3. For invalid semantic outputs, use the hardened S08/S07 adapter only to regenerate the specific invalid packet with the exact validation error. Do not rerun valid packets.
4. Repeat validation until all required Map outputs are valid or a packet is truthfully blocked/failed.
5. Build the validated Reduce/evidence ledger only from current valid Map results.
6. Record packet/result hashes and total expected/valid/failed counts.

## Tests

Use existing TTK tests plus focused corruption cases when not already covered:

- wrong packet hash rejected;
- nonexistent segment ref rejected;
- factual quote absent from cited core rejected;
- `context_only` citation rejected when evidence is forbidden;
- non-factual item with valid allowed provenance and no forced quote behaves according to current V2.1 contract;
- missing window/result prevents complete evidence ledger;
- valid unchanged packet is not regenerated unnecessarily.

## Product check

Read a sample across early/middle/late Map results. Confirm that deterministic validation did not transform or flatten semantics and that the ledger contains source-specific content from across the source.

## Outputs

- validated current TTK Map result set;
- TTK Reduce/evidence packet/ledger;
- `<run>/evaluation/S09-map-validation.yaml` with counts and invalid/repair history;
- S09 handoff.

Handoff must name the exact ledger path/hash, expected/valid/failed packet counts, repair invocations performed, and any unresolved packet blocker.

## Acceptance

PASS requires complete current Map coverage and a valid evidence ledger. A validator saying PASS while required Map work is missing is not acceptable.

Commit/push any validator/test fixes, return handoff, **STOP.**