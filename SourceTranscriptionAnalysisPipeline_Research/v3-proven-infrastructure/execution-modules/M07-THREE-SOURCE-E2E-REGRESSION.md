# M07 — Fresh Three-Source E2E + Regression

## TARGET

Prove the R2-selected production pipeline works repeatedly on the three primary benchmark videos and produces the intended knowledge product.

## Read only

- `../CURRENT-WORK.md`
- R2-approved M05 selection report
- M06 production runner/result
- `../03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- exact source/gold fixtures needed for final scoring

## Required primary sources

1. `P-h5WSQG1Sw` — EN long science interview
2. `CygwqaNg2PY` — EN technical finance
3. `vFTuLylvYnA` — DE finance

## Freshness

Follow the selected production architecture truthfully.

If the production path owns source acquisition/ASR, run those stages for real.

If the production path legitimately consumes transcripts, identify the transcript source/version and do not call a historical transcript a fresh ASR run.

No copied historical artifact may be presented as newly generated.

## Required checks per source

- correct source identity;
- real selected tools/models invoked;
- final knowledge artifact generated;
- artifact is source-specific, not generic;
- important thesis/insights present;
- mechanisms/procedures/examples/caveats retained where present;
- late-source content not silently lost;
- source/timestamp references resolve at the promised level;
- no obvious unsupported/cross-source claims;
- EN and DE both usable;
- rerun/recovery works without hidden chat memory or manual file surgery.

## Comparative product review

Use the V3 rubric and compare against the strongest simple baseline retained from M01 where feasible.

The production system should justify its extra complexity. If it does not outperform a much simpler baseline in a meaningful way, say so.

## Optional holdout

Do **not** automatically run `oZIsMX6WgFs`.

Run it only when:

- a procedural-recall risk remains unresolved;
- the three-source result is ambiguous;
- ChatGPT requests a fourth holdout at R3.

## Output

- three final production artifacts;
- per-source evaluation notes;
- `../results/M07-THREE-SOURCE-REGRESSION.md`;
- `../results/M07-RESULT.md`.

## Review Gate R3

End with exactly one:

- `REVIEW_GATE: PRODUCTION_ACCEPTANCE`
- `REVIEW_GATE: ONE_PRODUCT_REPAIR`
- `REVIEW_GATE: ARCHITECTURE_REJECTED`

ChatGPT independently reads the remote commit/artifacts for final verdict.

## Anti-drift final rule

A bookkeeping/provenance imperfection that does not invalidate the actual product is not grounds for another multi-day correction loop. Record it as technical debt unless it blocks reproducibility, corrupts evidence, or creates material safety/data-loss risk.
