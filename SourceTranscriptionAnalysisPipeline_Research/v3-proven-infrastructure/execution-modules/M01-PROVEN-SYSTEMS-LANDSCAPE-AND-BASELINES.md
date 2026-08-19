# M01 — Proven Systems Landscape + Runnable Baselines

## TARGET

Find and run already-proven end-to-end or near-end-to-end transcript/video-to-knowledge systems before authorizing a custom composition.

## Read only

- `../CURRENT-WORK.md`
- `../00-START-HERE.md`
- `../03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- `../04-V3-COMPONENT-REGISTRY.yaml`
- `../results/M00-PROVEN-SYSTEMS-SEED.md` if it exists

Do not read V2 architecture unless a specific historical candidate needs rechecking.

## Research requirement

Use current primary repositories/documentation.

Build a landscape of approximately 10-20 credible candidates if the ecosystem supports it. Search complete systems first, including adjacent categories:

- YouTube/video-to-notes;
- podcast/lecture knowledge extraction;
- transcript-to-wiki/Markdown;
- meeting/transcript knowledge bases;
- source-grounded research assistants;
- multimodal/video distillation;
- local/self-hosted NotebookLM-style systems.

For each serious candidate record:

- canonical repo/site;
- current activity/release evidence;
- input types;
- output type;
- source/timestamp/citation support;
- language support;
- Windows/local viability where relevant;
- model/provider dependencies;
- install/runtime burden;
- license;
- actual runnable examples/tests;
- likely custom adaptation needed.

## Shortlist

Select 3-5 strongest candidates on evidence, not stars or README claims.

## Real run requirement

Run the strongest 2-3 on `CygwqaNg2PY` first.

Use real source/current transcript acquisition according to each candidate's supported path. Do not substitute historical outputs while calling the run fresh.

Preserve:

- exact version/commit;
- install/run commands;
- produced output;
- failures/blockers;
- short product inspection.

Only expand a candidate to `P-h5WSQG1Sw` or `vFTuLylvYnA` if the first output is genuinely promising.

## Baselines

If still current/runnable, include Fabric and Open Notebook as product comparators. Reverify any historical `yt-distill`/YouTube agent candidate before treating it as current.

## Product inspection

For each runnable candidate answer:

1. Does it capture the actual source thesis?
2. Does it preserve important technical claims/mechanisms/caveats/examples?
3. Is it source-specific rather than generic?
4. Are timestamps/citations/source references usable?
5. Would an operator learn the source substantially faster from the output?
6. What exact gap remains?

## Required outputs

- `../results/M01-LANDSCAPE.md`
- `../results/M01-RUN-COMPARISON.md`
- runnable candidate outputs under an M01 results/artifacts subdirectory
- `../results/M01-RESULT.md`

## Decision marker

End `M01-RESULT.md` with exactly one:

- `REVIEW_GATE: ADOPT_OR_FORK_CANDIDATE`
- `REVIEW_GATE: COMPONENT_COMPOSITION_REQUIRED`
- `REVIEW_GATE: INSUFFICIENT_EVIDENCE`

Do not design a full replacement architecture yourself.

## Stop-loss

If a candidate needs two separate rounds of custom repair merely to start, stop repairing it and mark it failed/blocked unless the candidate is uniquely valuable.
