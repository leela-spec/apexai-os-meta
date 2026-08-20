# Current Recommendation — Transcript-to-Knowledge

**Status:** PROVISIONAL RECOMMENDATION, NOT OPERATOR DECISION  
**Date:** 2026-08-20

This file answers one question only: **if implementation had to start from today's evidence, what would be the leading option for each responsibility?**

It must be updated when the experiments in `05-OPEN-QUESTIONS-AND-TESTS.md` produce contradictory evidence.

## 1. Workflow/orchestration

**Recommendation:** deterministic workflow ownership first; compare plain Python against LangGraph based on actual resume/fallback requirements.

- AI should not be required to remember pipeline state.
- LangGraph is a serious candidate because checkpointing, explicit branching, retries and human gates are existing implemented capabilities.
- Do not select LangGraph merely because it is feature-rich.
- Autonomous CLI execution is allowed, but avoid by default until it shows a large value gain and reliable execution pattern.

## 2. Source acquisition

**Recommendation:** yt-dlp + FFmpeg + local-file/transcript input.

No custom acquisition framework.

## 3. Transcript / ASR

**Recommendation:** keep the decision open until a small same-fixture benchmark.

Leading local reference: faster-whisper.  
Local challenger: Parakeet TDT 0.6B v3.  
Hosted quality challenger: Scribe v2 or another strong current hosted ASR only if its quality/simplicity gain could justify dependency/cost.

Use an already trustworthy source transcript when available rather than retranscribing for architectural purity.

## 4. Alignment / diarization

**Recommendation:** conditional only.

Use no additional layer unless speaker attribution or timestamp quality materially affects the selected product. If needed, use an existing implementation such as WhisperX/pyannote rather than custom alignment/diarization.

## 5. Canonical source/custody

**Recommendation:** preserve the useful deterministic invariants while reopening how much TTK is needed.

Likely requirements:
- source identity;
- transcript text;
- segment/word timing when available/needed;
- stable references needed for resume;
- hashes/state where they prevent stale reuse;
- optional evidence mapping depending on product mode.

Do not make strict quote/timestamp traceability universal because the operator explicitly made it optional by use case.

## 6. Long-document extraction

**Recommendation:** if LangExtract wins the extraction comparison, let LangExtract own its built-in long-document chunking/parallel/multipass process unless a measured gap requires external TTK windowing.

Reason: custom semantic transport chunking should not duplicate a maintained system's own long-document process without evidence.

## 7. Grounded semantic extraction

**Recommendation:** LangExtract is the leading extraction framework candidate, with two first-class lanes:

1. **LangExtract + local Qwen/Ollama** — local-cost baseline and possible production winner.
2. **LangExtract + supported strong external provider** — quality ceiling/challenger.

A custom subscription-CLI provider is a secondary option, not the first implementation, because the adapter is project-specific even though LangExtract's provider extension mechanism is real.

## 8. Pre-extraction specialists

**Recommendation:** not default. Test GLiNER2 only if it plausibly reduces expensive model work or improves recall enough to justify the extra stage. NuExtract is a second challenger only if a gap remains.

## 9. Structured output/retries

**Recommendation:** provider-native structured output plus deterministic schema validation first. Instructor becomes a candidate only when this seam is actually brittle or multi-provider unification gives material value.

## 10. Source-support / trust

**Recommendation:** match the trust layer to the product mode.

- evidence-light output: no universal exact-evidence requirement;
- source-grounded mode: map important claims back to source evidence;
- high-trust mode: stricter exact quote/time support.

mDeBERTa/HHEM remain advisory candidates, not automatic authority.

## 11. Global synthesis

**Recommendation:** do not freeze the synthesis input strategy yet. Execute the approved three-way comparison:

- full transcript only;
- extracted evidence only;
- full transcript + extracted evidence.

Current hypothesis: full transcript + evidence may preserve global context while using extraction to improve attention/recall, but this must win the actual product test.

## 12. Global synthesis model

**Recommendation:** local Qwen must be measured first rather than dismissed or promoted by assumption.

Compare it against a strong external model on identical input. A hybrid local-extraction + external-synthesis architecture is explicitly allowed if that is where the material quality gap occurs.

External API/CLI should enter production only when the gain is significant enough to justify cost/dependency/reliability tradeoffs.

## 13. External factual verification

**Recommendation:** optional/selective only when the product needs external truth. Keep source support and external truth separate.

## 14. Output representation

**Recommendation:** OPEN. Do not inherit Macro/Meso/Micro as mandatory.

Candidate output forms should be judged on how much useful knowledge a reader can recover efficiently. Macro/Meso/Micro remains one candidate alongside article/wiki/report/task-specific structures and mixed source+external knowledge products.

## 15. Compilation

**Recommendation:** deterministic boring output rendering. Reuse TTK compiler functions only where they fit the selected artifact contract.

## 16. Evaluation

**Recommendation:** product-level real-source comparison, not schema/receipt PASS.

Use:
- human must-find/important-insight review;
- source-fidelity checks appropriate to the selected evidence mode;
- output usefulness/readability;
- EN/DE comparison;
- local vs external same-input comparison;
- established products such as NotebookLM/Fabric/Open Notebook as baselines when practical;
- DeepEval only as auxiliary evidence, not sole authority.

## 17. Resume/recovery

**Recommendation:** resume expensive completed stages. Choose between minimal state/hashes and LangGraph checkpointing after the workflow branching/fallback experiment. Do not introduce a heavyweight workflow engine without a demonstrated need.

## 18. Explicitly out of current scope

- visual-only video evidence / multimodal branch;
- non-factual provenance policy;
- broader future knowledge-base integration beyond what is required for the current artifact.

See `07-FUTURE-DEVELOPMENT.md`.