# M03 — Grounded Extraction Bake-off (Conditional)

## RUN THIS MODULE ONLY IF

R1 concluded that no near-complete candidate adequately solves grounded extraction/knowledge capture and the selected path still needs this layer.

Otherwise write `SKIPPED_NOT_NEEDED`.

## TARGET

Find the smallest grounded extraction method that preserves important source meaning and evidence without custom pseudo-semantics.

## Read only

- `../CURRENT-WORK.md`
- M01/R1 result
- M02 result only if transcript selection affects the fixture
- `../03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- relevant entries from `../04-V3-COMPONENT-REGISTRY.yaml`

## Required lanes

### A — Direct strong CLI control

Use the active authenticated strong CLI route selected for the benchmark. The coding/orchestration layer must not fake this output.

### B — LangExtract

Run current LangExtract against the same windows. Use a supported provider path. If a custom provider adapter is needed, keep it minimal and prove it invokes the real worker. Do not reimplement LangExtract.

### C — GLiNER2-assisted strong CLI

Run only to test whether cheap local entity/relation/schema hints materially help quality or reduce strong-model work.

## Conditional lane

Instructor is allowed only if real validation/retry brittleness exists in A/B. Do not add it pre-emptively.

NuExtract is allowed only if GLiNER2 fails the intended auxiliary role and there remains a measured need for a local structured extractor.

## Fixture

Use 12 total windows:

- 4 from each primary video;
- early;
- middle;
- late;
- one difficult/domain-heavy window.

All lanes consume identical source text/evidence.

## Product scoring

Check:

- important insight recall;
- exact/source grounding;
- unsupported overreach;
- caveats/uncertainty;
- mechanisms/procedures/examples;
- usefulness of entities/relations if emitted;
- retries/failures;
- custom integration surface;
- tokens/runtime only when actually measurable.

## Hard failure

- fabricated source evidence;
- wrong-source contamination;
- heuristic/template output presented as semantic reasoning;
- wrapper tested without real model execution.

## Output

- `../results/M03-EXTRACTION-COMPARISON.md`
- candidate output packets/artifacts
- `../results/M03-RESULT.md`

End with one:

- `PASS: DIRECT_CLI`
- `PASS: LANGEXTRACT`
- `PASS: GLINER2_ASSISTED`
- `PASS: OTHER_PROVEN_ROUTE`
- `APPROACH_SUSPECT`
- `BLOCKED`
- `SKIPPED_NOT_NEEDED`

## Stop rule

If an extra framework does not visibly improve product quality, resilience, token use, or custom-code elimination, remove it rather than inventing another reason to keep it.
