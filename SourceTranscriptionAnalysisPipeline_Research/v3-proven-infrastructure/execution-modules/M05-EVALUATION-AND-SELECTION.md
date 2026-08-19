# M05 — Evaluation and Architecture Selection

## TARGET

Select the **smallest proven production composition** from real candidate outputs.

This is a decision module, not an implementation expansion module.

## Read only

- `../CURRENT-WORK.md`
- `../03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- M01 result and R1 decision
- M02/M03/M04 results only if those modules ran
- actual candidate output artifacts

## Required evaluation order

1. hard product failures;
2. source fidelity and important-insight retention;
3. multilingual/EN-DE viability;
4. repeatability and operational resilience;
5. user/operator usefulness;
6. implementation complexity / custom-code surface;
7. token/runtime cost where measurable;
8. architectural elegance last.

## Evaluation methods

Use deterministic checks only for deterministic properties.

Use source-grounded/human review for semantic product quality.

DeepEval or another existing framework may provide auxiliary scores only when the judge/provider/language path is actually valid.

Compare against simple product baselines from M01 where available.

## Required selection table

For every finalist state:

- what it reuses unchanged;
- what is configured;
- what needs a light adapter/fork;
- what custom code remains;
- observed strengths;
- observed failures;
- operational burden;
- evidence source/candidate outputs.

## Selection preference

1. adopt existing system;
2. light fork;
3. 2-4 component composition;
4. existing TTK/custom pieces only where a benchmark proves a gap;
5. new framework only with explicit observed justification.

## Required output

- `../results/M05-SELECTION-REPORT.md`
- `../results/M05-RESULT.md`

`M05-SELECTION-REPORT.md` must name exactly one primary production path and one fallback.

It must also list explicit rejections so they do not reappear later without new evidence.

## Review Gate R2

End with:

`REVIEW_GATE: FREEZE_PRODUCTION_COMPOSITION`

Do not begin M06 until ChatGPT independently reviews the remote artifacts and records the selected composition in `CURRENT-WORK.md` or another V3 authority update.

## Forbidden

- adding another candidate because the decision feels uncomfortable;
- redesigning the benchmark after seeing a preferred result;
- preserving every experimental dependency in the production hot path;
- treating sunk implementation effort as evidence.
