# Research Source Index

**Status:** CURRENT  
**Date:** 2026-08-20

## A. Current decision-workspace sources

1. `sources/2026-08-20-GPT-V21-DR-OPTION-MATRIX.md` — reconciliation of V2.1 against Deep Research; stage/process option matrix; evidence/value/risk framing.
2. `sources/2026-08-20-GPT-V3-LANGGRAPH-LANGEXTRACT-RECONCILIATION.md` — V3 value analysis; LangGraph vs LangExtract; local/cloud inventory; ASR and synthesis explanation.
3. `03-PIPELINE-OPTIONS-MATRIX.md` — canonical live comparison matrix derived from research; not a source archive.
4. `06-SCENARIO-SIMULATIONS.md` — scenarios that determine whether local, subscription, API, or hybrid paths are justified.

## B. Repository research authorities to preserve

- `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/archive-pre-v3-authority/10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.original.md`
- `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/archive-pre-v3-authority/11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.original.md`
- `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/01-ARCHITECTURE-ANALYSIS.md`
- `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/04-COMPONENT-REGISTRY.yaml`
- `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/05-SOURCE-DECISION-EVIDENCE.yaml`
- `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/01-V3-ARCHITECTURE.md`
- `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/02-V3-IMPLEMENTATION-PLAN.md`
- `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/04-V3-COMPONENT-REGISTRY.yaml`

## C. Deep Research

Deep Research report from the 2026-08-20 reconciliation session. The report recommended a proven-component composition centered on mature acquisition/ASR, grounded extraction, full-source global synthesis, source-support checking, selective external verification, and deterministic compilation.

Important limitation: the DR run itself explicitly lacked access to the live V2/V2.1 project files, so its recommendations are evidence to reconcile, not direct supersession authority.

## D. Existing Apex research-index pattern reused

The organizational model is adapted from the existing Apex KB research-index approach: distinguish current authority, active module sources, research evidence, and provenance/history instead of loading or treating every historical file as co-equal authority.

Reference:
`FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/04-Apex-KB-Current-Research-Index.md`

## E. Evidence classification

For each component or architectural option, distinguish:

1. **Component existence/capability evidence** — does the maintained tool really implement the claimed capability?
2. **Architecture-fit evidence** — is the proposed role/integration itself a known/proven pattern or our hypothesis?
3. **Project evidence** — did it actually improve this pipeline on our real fixtures/hardware?

Never upgrade level 1 evidence into level 3 evidence.

## F. High-priority externally verified component families

- yt-dlp / FFmpeg — acquisition and media normalization.
- faster-whisper — local ASR, timestamps, VAD, diagnostics.
- NVIDIA Parakeet TDT 0.6B v3 — local multilingual ASR challenger.
- WhisperX — forced alignment and optional speaker diarization.
- LangExtract — grounded structured extraction, long-document processing, multipass extraction, source locations, Ollama/cloud providers.
- LangGraph — deterministic/stateful workflow runtime, checkpoints, branching, retry/resume, human interrupts.
- GLiNER2 / NuExtract — local specialist extraction candidates.
- Instructor — typed output/validation/retry adapter.
- DocETL — document Map/Reduce orchestration candidate.
- mDeBERTa NLI / HHEM — optional advisory support/consistency models.
- DeepEval — auxiliary evaluation harness, not semantic authority.
- Fabric / Open Notebook / NotebookLM — product-output baselines/comparators.

## G. Source rule

When a new claim affects architecture selection, prefer current primary documentation/repository/model cards and save the material conclusion in the matrix or recommendation file. Do not let chat memory become the only source of a decision.