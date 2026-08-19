# S10 — Advisory Source-Support Checks

**Execute only S10, then stop.**  
**Input:** validated S09 evidence/claim pairs  
**Next:** S11

## Outcome

Test whether cheap local support/factual-consistency models provide useful warning signals without becoming semantic authority.

## Context to load

- this file;
- S09 handoff + relevant validated factual claim/evidence pairs;
- `support_mdeberta` registry entry;
- `support_hhem` entry only for English comparison;
- existing human/gold support-pair fixture if available.

Do not load Reduce or final reports.

## Recommended route

- multilingual mDeBERTa NLI: primary advisory challenger for EN/DE;
- HHEM: optional English comparator;
- strong CLI semantic worker remains authoritative for nuanced `source_support` judgment.

## Work

1. Build a bounded evaluation set from real S09 claim/evidence pairs; include supported and deliberately difficult/overreaching cases where trustworthy labels exist.
2. Run the actual local mDeBERTa model and record model revision/runtime/configuration.
3. On English subset, optionally run real HHEM if available and material.
4. Compare warning usefulness against human/gold labels where available. Do not convert AI-silver guesses into human gold.
5. Decide one of:
   - `KEEP_ADVISORY` — warning signal is useful enough to retain;
   - `EVAL_ONLY` — useful only for diagnostics/regression;
   - `REJECT` — no material value;
   - `BLOCKED` — real model could not run.
6. If retained, store scores/warnings as sidecars. They may trigger review/retry but must not silently overwrite semantic support states.

## Tests

- real model identity/revision recorded;
- input premise/evidence and hypothesis/claim mapping is correct;
- EN/DE behavior is not conflated;
- thresholds/labels are not invented as ground truth;
- advisory output cannot mutate TTK source evidence;
- production pipeline remains functional if the advisory component is disabled.

## Outputs

- `<run>/advisory/mdeberta.*` and optional HHEM sidecars;
- `<run>/advisory/decision.yaml`;
- S10 handoff.

Handoff must give component/version, sample size, label authority, observed value/limitations, selected advisory status, and whether S11 should receive the sidecar as a warning input.

## Acceptance

A blocked or rejected advisory model does not fail the core pipeline. PASS means the experiment was truthful and a clear keep/reject decision exists.

Commit/push stage-specific adapters/tests if any, return handoff, **STOP.**