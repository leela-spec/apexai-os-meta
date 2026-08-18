# SourceTranscriptionAnalysisPipeline Research: Master Index (00-INDEX)

## 0. Current authoritative continuation path

**Start here for all new implementation/research work.** These three documents supersede older architectural recommendations where they conflict, while older artifacts remain historical evidence:

1. [`PIPELINE_DECISION_CONTRACT_2026-08-18.yaml`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml) — machine-readable operator decisions, authority boundaries, V1 pipeline, deferred-component triggers, benchmark order, and stop conditions.
2. [`PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md) — full step/options matrix, researched alternatives, value analysis, V1 recommendation, and future upgrade map.
3. [`V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md) — implementation-ready plan for a local CLI AI to replace pseudo-semantic heuristics with a strong CLI semantic worker and test the four-source corpus.

**Critical current boundary:** Qwen has no V1 role in this transcript pipeline. Deterministic code/TKK owns mechanical custody/validation/resume/compilation; a strong subscription CLI AI owns semantic Map/Reduce and external evidence judgment. Do not add deferred frameworks unless their named failure trigger in the decision contract is demonstrated.

---

## 1. Directory Mission & Scope
This directory serves as the centralized research, benchmarking, and multi-AI evaluation archive for the **SourceTranscriptionAnalysisPipeline** subsystem. It documents all architectural experiments, code deliverables, comparative evaluations, and integration roadmaps.

---

## 2. Master Document Index

| Priority | Document / Asset | Type | Purpose & Summary |
| :---: | :--- | :--- | :--- |
| **00** | [`00-INDEX.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/00-INDEX.md) | Index | Master catalog and current continuation path. |
| **00.1** | [`PIPELINE_DECISION_CONTRACT_2026-08-18.yaml`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml) | Decision Contract | **Current authority:** machine-readable operator constraints, V1 architecture, ownership boundaries, fallback triggers, and stop conditions. |
| **00.2** | [`PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md) | Architecture Analysis | **Current authority:** full step/options matrix, research findings, V1 selections, and future improvement map. |
| **00.3** | [`V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md) | Implementation Plan | **Current execution plan:** surgical TTK repair using a strong CLI semantic worker, staged benchmark, ASR calibration, and acceptance tests. |
| **01** | [`POST_REPAIR_EVALUATION_REPORT.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/POST_REPAIR_EVALUATION_REPORT.md) | Evaluation Report | Historical post-repair evaluation across all 4 benchmark sources and 3 architectures. |
| **02** | [`RESEARCH_ADVANCED_IMPROVEMENTS_AND_UNIFICATION.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/RESEARCH_ADVANCED_IMPROVEMENTS_AND_UNIFICATION.md) | Research & Blueprint | Historical research on resilience, simplicity, value, token efficiency, and hybrid unification. May be superseded by the current decision contract. |
| **02.1** | [`HYBRID_CROSS_POLLINATION_AND_UNIFICATION_STRATEGY.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/HYBRID_CROSS_POLLINATION_AND_UNIFICATION_STRATEGY.md) | Strategy Analysis | Historical cross-pollination strategy; retain as evidence, not current authority where conflicting. |
| **03** | [`PROCESS_STEP_COMPARISON_MATRIX.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/PROCESS_STEP_COMPARISON_MATRIX.md) | Comparison Matrix | Step-by-step lifecycle matrix comparing all 3 prior pipelines across 14 discrete steps. |
| **04** | [`HANDOVER_MULTI_PIPELINE_EVALUATION.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/HANDOVER_MULTI_PIPELINE_EVALUATION.md) | Handover | Historical evaluation handover with remote paths and ranked improvement matrix. |
| **05** | [`transcript_engine.py`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/transcript_engine.py) | Python Module | Prior deterministic Macro → Meso → Micro representation/renderer experiment. |
| **06** | [`test_transcript_engine.py`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/test_transcript_engine.py) | Unit Tests | Prior tests covering timestamp validation, verdict enums, claim types, and quote grounding. |
| **07** | [`run_tests.py`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/run_tests.py) | Test Runner | Zero-dependency local test execution runner. |

---

## 3. Benchmark Execution Receipts (4 Benchmark Sources)

The latest committed receipt at the current decision point is:

`artifacts/benchmark_runs/20260818-185245/receipt.json`

It reports **only 1 fully complete source and 3 incomplete sources** because Pipeline 2 synthesis is pending for three sources. It also records a dirty working tree and prior run-start commit, so future benchmark receipts must preserve exact run provenance and must never infer success from artifact presence alone.

Initial cross-domain regression corpus:

1. **Andrew Huberman (`P-h5WSQG1Sw`):** long English neuroscience interview.
   - [P1 transcript artifacts](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/P-h5WSQG1Sw/)
   - [P3 TTK run](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/P-h5WSQG1Sw/)
2. **Elliott Prechter (`CygwqaNg2PY`):** technical finance / Elliott Wave.
   - [P1 transcript artifacts](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/CygwqaNg2PY/)
   - [P3 TTK run](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/CygwqaNg2PY/)
3. **Markus Koch (`vFTuLylvYnA`):** German financial commentary.
   - [P1 transcript artifacts](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/vFTuLylvYnA/)
   - [P3 TTK run](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/vFTuLylvYnA/)
4. **Foundation for Cycles (`oZIsMX6WgFs`):** technical market-cycle procedure/analysis.
   - [P1 transcript artifacts](file:///c:/GitDev/apexai-os-meta/.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/oZIsMX6WgFs/)
   - [P3 TTK run](file:///c:/GitDev/apexai-os-meta/artifacts/ttk_runs/oZIsMX6WgFs/)
