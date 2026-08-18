# START HERE — Future V2.1 Test Evaluator

This file is for a **fresh AI evaluating the completed or partially completed V2.1 transcript-pipeline implementation and benchmark**. It is not an invitation to restart architecture design.

## Read first

1. `06-TRIAL1-TRANSPORT-LOCK.yaml`
2. `07-DECIDED-FRAMEWORK-AND-TEST-EVALUATION-HANDOVER.yaml`
3. `03-BENCHMARK-AND-TEST-SPEC.yaml`
4. `02-IMPLEMENTATION-PLAN.yaml`
5. `04-COMPONENT-REGISTRY.yaml`
6. `artifacts/transcript_pipeline_v2/SELECTION.yaml` if it exists
7. `artifacts/transcript_pipeline_v2/FINAL-REPORT.yaml` if it exists
8. `06-FINAL-HANDOVER.md` if P22 has created it

If `SELECTION.yaml` or `FINAL-REPORT.yaml` does not exist, do **not** infer a winner or final success. Report the run as not ready for final evaluation or partial according to the benchmark contract.

## The decided framework — do not drift

The product is a trustworthy, high-value knowledge artifact from audio/video. ASR is a prerequisite quality gate, not the product.

The control plane is deterministic: APEX/OpenClaw eventually triggers a thin local runner over TTK state. Qwen has no role in this pipeline.

Trial 1 strong-AI transport is **subscription CLI only**:

- Claude Code CLI;
- Codex CLI;
- Antigravity CLI only after a real local headless subprocess smoke test passes.

Gemini CLI, browser subscription AIs, API-key billing, pay-as-you-go model APIs, hosted model APIs, and paid APIs are **post-Trial-1 only**. If a framework cannot use an allowed CLI adapter, mark it `BLOCKED_FOR_TRIAL1`; do not silently change transport.

TTK is the locked canonical evidence/state spine for source SHA custody, segment IDs, processing windows, packet hashes, deterministic provenance/schema validation, stale detection, coverage, resumability, selective verification routing, and compilation.

The bake-off is deliberately bounded:

- ASR: faster-whisper reference vs Parakeet; WhisperX only as a conditional alignment/diarization stage.
- Map: direct strong CLI vs LangExtract with allowed CLI provider adapter vs GLiNER2-assisted direct CLI. NuExtract only if GLiNER2 fails its intended narrow role.
- Structured output: native CLI schema + TTK validation first; Instructor only if its trigger is demonstrated.
- Source support: strong semantic worker is authoritative; TTK verifies source references/quotes; mDeBERTa and HHEM are advisory only.
- Reduce: direct strong CLI vs fixed DocETL challenger. DocETL optimizer is OFF for the first comparison. DocETL is `BLOCKED_FOR_TRIAL1` if it requires API transport.
- External verification: only important/checkworthy factual claims; allowed subscription CLI transport only; insufficient evidence remains `UNVERIFIED`.
- Evaluation: deterministic hard gates and targeted human gold are primary; DeepEval is auxiliary and must obey the same Trial-1 CLI transport restriction.
- Product baselines: Fabric/Open Notebook only where they can be run without violating Trial-1 transport policy.

Factual claims and externally testable estimates require exact source evidence. Non-factual semantic objects still require source provenance but do not have a forced exact-quote quota. Source support and external truth are separate.

## What is *not* decided yet

Do not invent these before reading actual benchmark evidence:

- final ASR engine/model;
- whether WhisperX is promoted conditionally;
- winning Map lane;
- whether GLiNER2, NuExtract, or Instructor survive;
- whether mDeBERTa/HHEM survive as advisory layers;
- winning Reduce lane / whether DocETL earns production use;
- final selected production composition.

Those are selected only by P16 from measured evidence.

## Evaluation procedure

Evaluate primary artifacts, not prose claims. In order:

1. capture live repo/branch/HEAD/dirty state;
2. verify Trial-1 transport receipts contain only allowed subscription CLI transports and no forbidden transport;
3. inspect P0–P15 receipts/scorecards for missing cases, blocked cases, and `UNMEASURED` values;
4. inspect P16 `SELECTION.yaml` and independently check each selected component against hard gates and material-gain policy;
5. inspect P17 evidence-policy tests;
6. inspect P18 runner and prove heuristic/regex pseudo-semantic output cannot report semantic completion;
7. inspect P19 receipt truth logic;
8. inspect P20 four-source semantic regression;
9. inspect P21 fresh German + English audio-to-knowledge runs;
10. inspect P22 mandatory tests and clean-room resume/idempotency proof;
11. cross-check `FINAL-REPORT.yaml` against receipts/hashes/results rather than trusting it as authority;
12. issue `PASS`, `PARTIAL`, `FAIL`, or `NOT_READY_FOR_FINAL_EVALUATION` with the exact next action.

The hard gates are HG01–HG10 in `03-BENCHMARK-AND-TEST-SPEC.yaml`. A hard-gate failure cannot be averaged away by a good utility score.

## Known V2.1 documentation reconciliation

The Trial-1 patch commit was `c3719abd466427ecfe35f3838f970fd46ec99e6c`. Verification found three stale historical lines still present in older V2 documents:

- Architecture S8 still mentions Gemini as a generic fallback.
- Implementation P10 still mentions a small capped DocETL API experiment.
- Implementation P13 still lists a hosted ASR oracle as optional.

These lines **do not control Trial 1**. `06-TRIAL1-TRANSPORT-LOCK.yaml` is the authoritative resolution: Gemini and hosted ASR are post-Trial-1; DocETL must use an allowed CLI adapter or be `BLOCKED_FOR_TRIAL1`.

## Anti-drift rule

Do not redesign the architecture merely because a component is inconvenient or because another library looks interesting. Recommend a framework change only if measured evidence activates a documented reversal trigger or exposes a new named capability gap. State the failed target, evidence, smallest viable change, expected value, and required regression test.
