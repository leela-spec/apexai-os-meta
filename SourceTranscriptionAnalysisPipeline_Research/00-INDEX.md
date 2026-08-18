# SourceTranscriptionAnalysisPipeline Research: Master Index (00-INDEX)

## 0. Current authoritative continuation path — V2 reuse bake-off

**Start here for all new transcript-pipeline implementation work.** The V2 set below supersedes the earlier V1 architecture/implementation sequence where they conflict. V1 remains historical evidence of the over-correction that V2 fixes.

1. [`v2-reuse-bakeoff/00-START-HERE.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/00-START-HERE.md) — execution handover, constant frame, authority hierarchy, read order, stop conditions.
2. [`v2-reuse-bakeoff/01-ARCHITECTURE-ANALYSIS.md`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/01-ARCHITECTURE-ANALYSIS.md) — corrected reuse-first architecture, full per-stage option matrices, promotion/rejection logic.
3. [`v2-reuse-bakeoff/02-IMPLEMENTATION-PLAN.yaml`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/02-IMPLEMENTATION-PLAN.yaml) — **machine-readable P0–P22 execution plan** with task dependencies, reads/writes, commands, acceptance, commits, final tests.
4. [`v2-reuse-bakeoff/03-BENCHMARK-AND-TEST-SPEC.yaml`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/03-BENCHMARK-AND-TEST-SPEC.yaml) — benchmark levels, hard gates, metrics, thresholds, four-source and fresh end-to-end acceptance, final report schema.
5. [`v2-reuse-bakeoff/04-COMPONENT-REGISTRY.yaml`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/04-COMPONENT-REGISTRY.yaml) — component roles, isolated install paths, hypotheses, triggers, fallbacks, official sources.
6. [`v2-reuse-bakeoff/05-SOURCE-DECISION-EVIDENCE.yaml`](file:///c:/GitDev/apexai-os-meta/SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/05-SOURCE-DECISION-EVIDENCE.yaml) — operator decisions, project-resource inputs, hardware evidence, repository evidence, rationale trace, unresolved questions.

### V2 governing rule

> **Measure before remove.** A mature reusable component that plausibly replaces fragile custom code, reduces expensive reasoning, improves evidence quality, or adds a useful independent safety/evaluation signal receives a bounded benchmark before rejection. Installed/benchmarked does not mean production-selected.

### Current authority boundaries

- **Qwen:** no role in this transcript pipeline now.
- **TTK:** retain deterministic transcript custody, packet/hash state, validation, verification routing, resume, compiler unless a measured replacement proves all hard invariants.
- **Strong subscription CLI AI:** semantic authority for irreducible meaning/synthesis; Claude/Codex/Gemini/browser subscription AIs are available resources.
- **Reusable candidates:** faster-whisper, Parakeet, WhisperX, LangExtract, GLiNER2, NuExtract, Instructor, mDeBERTa, HHEM, DocETL, DeepEval, Fabric/Open Notebook are classified in the registry and tested only in their declared lanes.
- **Paid APIs:** undesirable but not forbidden; small capped experiments are allowed when they answer a material architecture question and cost/value are recorded.
- **Factual Micro claims:** exact source evidence required; non-factual objects still need source provenance but not artificial quote quotas.

---

## 1. Historical documents and evidence

| Priority | Document / Asset | Status | Purpose |
| :---: | :--- | :--- | :--- |
| **00** | `00-INDEX.md` | Current | Master catalog and V2 continuation path. |
| **00.V2** | `v2-reuse-bakeoff/**` | **Current authority** | Reuse-first architecture, machine-readable implementation, benchmark/test system, component registry, decision/evidence log. |
| **H-V1.1** | `PIPELINE_DECISION_CONTRACT_2026-08-18.yaml` | Superseded where conflicting | Earlier minimal V1 decision contract; useful history only. |
| **H-V1.2** | `PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md` | Superseded where conflicting | Earlier architecture analysis that over-corrected by excluding reusable candidates from V1. |
| **H-V1.3** | `V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md` | Superseded where conflicting | Earlier direct-CLI-only execution plan. |
| **01** | `POST_REPAIR_EVALUATION_REPORT.md` | Historical evidence | Post-repair evaluation across four benchmark sources / three architectures. |
| **02** | `RESEARCH_ADVANCED_IMPROVEMENTS_AND_UNIFICATION.md` | Historical research | Resilience, simplicity, token efficiency, hybrid unification research. |
| **02.1** | `HYBRID_CROSS_POLLINATION_AND_UNIFICATION_STRATEGY.md` | Historical research | Prior cross-pollination ideas; retain for evidence. |
| **03** | `PROCESS_STEP_COMPARISON_MATRIX.md` | Historical evidence | Prior lifecycle comparison. |
| **04** | `HANDOVER_MULTI_PIPELINE_EVALUATION.md` | Historical handover | Prior evaluation context. |
| **05** | `transcript_engine.py` | Historical experiment | Prior deterministic representation/renderer experiment. |
| **06** | `test_transcript_engine.py` | Historical tests | Prior representation/grounding tests. |
| **07** | `run_tests.py` | Historical utility | Prior test runner. |

---

## 2. Benchmark corpus

Initial cross-domain regression corpus:

1. **`P-h5WSQG1Sw` — Huberman / Adolphs:** long English neuroscience interview; multi-speaker and long-source coverage case.
2. **`CygwqaNg2PY` — Elliott Prechter:** technical finance/Elliott Wave case.
3. **`vFTuLylvYnA` — Markus Koch:** German finance, domain-term/numeric ASR case.
4. **`oZIsMX6WgFs` — Market Cycles:** technical procedure/mechanism case.

Latest pre-V2 committed batch receipt retained as historical baseline:

`artifacts/benchmark_runs/20260818-185245/receipt.json`

It reports only one fully complete source and three incomplete sources. V2 requires stronger stage-level execution receipts, a real semantic-worker proof, and fresh-ASR proof for final end-to-end acceptance.

---

## 3. Next step

A receiving CLI AI should **not** edit the pipeline from this index. It should open `v2-reuse-bakeoff/00-START-HERE.md`, follow the required reads, then execute `P0` from `v2-reuse-bakeoff/02-IMPLEMENTATION-PLAN.yaml`.
