# M04 — Global Synthesis and Knowledge-Product Bake-off (Conditional)

## RUN THIS MODULE ONLY IF

The selected path still needs a separate global synthesis/Reduce layer after M01/M03.

Otherwise write `SKIPPED_NOT_NEEDED`.

## TARGET

Produce the best complete source-specific knowledge artifact with the smallest reliable synthesis machinery.

## Read only

- `../CURRENT-WORK.md`
- M01/R1 decision
- M03 result if it ran
- selected transcript/evidence artifacts
- `../03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- DocETL/current synthesis entries from `../04-V3-COMPONENT-REGISTRY.yaml`

## Required comparison

### A — Direct strong CLI synthesis

Use the same source/evidence material and ask a real authenticated strong CLI to produce the target knowledge artifact.

### B — DocETL fixed pipeline

Run only if the current DocETL provider seam can be used without building a large adapter framework or violating current provider constraints.

Keep automatic optimizer/rewrite behavior OFF for the first controlled comparison.

If DocETL cannot practically use the allowed worker route, mark it `BLOCKED/NOT_JUSTIFIED`; do not redesign the project around making DocETL fit.

## Scope

Start with full `CygwqaNg2PY`.

Only run finalists on:

- `P-h5WSQG1Sw`;
- `vFTuLylvYnA`.

Do not run every weak lane on every source.

## Required product shape

The artifact should preserve, where present:

- source thesis / Macro understanding;
- coherent semantic modules/chapters;
- important atomic claims;
- mechanisms and procedures;
- warnings/caveats/uncertainty;
- examples;
- decisions/recommendations made in the source;
- important entities/concepts;
- usable timestamp/source traceability.

Do not force Macro/Meso/Micro labels if an existing product representation is demonstrably better; preserve the underlying information requirements.

## Evaluation

Inspect actual artifacts, not only machine scores.

Compare:

- important insight recall;
- source fidelity;
- semantic organization;
- late-source coverage;
- generic boilerplate;
- unsupported claims;
- reading efficiency;
- integration/recovery complexity.

## Output

- `../results/M04-SYNTHESIS-COMPARISON.md`
- final candidate knowledge artifacts
- `../results/M04-RESULT.md`

End with one:

- `PASS: DIRECT_CLI_SYNTHESIS`
- `PASS: DOCETL`
- `PASS: EXISTING_SYSTEM_SYNTHESIS`
- `APPROACH_SUSPECT`
- `BLOCKED`
- `SKIPPED_NOT_NEEDED`

## Stop-loss

Do not perform a third repair on a synthesis framework that has already failed twice without producing a comparable product.
