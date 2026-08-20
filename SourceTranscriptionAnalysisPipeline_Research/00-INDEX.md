# SourceTranscriptionAnalysisPipeline Research: Master Index (00-INDEX)

## 0. CURRENT continuation path — decision workspace (2026-08-20)

**Start here for all new transcript-pipeline architecture/research work. Do not treat the old V2.1/V3 implementation PASS state as current product authority.**

The project is currently in a **decision and evidence phase**, not another broad implementation pass.

1. [`current-decision-workspace/00-START-HERE.md`](current-decision-workspace/00-START-HERE.md) — current authority/read order and anti-drift rules.
2. [`current-decision-workspace/02-DECISIONS.md`](current-decision-workspace/02-DECISIONS.md) — operator-verified decisions; highest authority inside this workspace.
3. [`current-decision-workspace/04-CURRENT-RECOMMENDATION.md`](current-decision-workspace/04-CURRENT-RECOMMENDATION.md) — one-file provisional recommendation for every responsibility.
4. [`current-decision-workspace/03-PIPELINE-OPTIONS-MATRIX.md`](current-decision-workspace/03-PIPELINE-OPTIONS-MATRIX.md) — options with value/evidence/risk, including local/external paths and LangGraph/LangExtract.
5. [`current-decision-workspace/05-OPEN-QUESTIONS-AND-TESTS.md`](current-decision-workspace/05-OPEN-QUESTIONS-AND-TESTS.md) — unresolved questions and mandatory experiments; local Qwen questions are tests, not operator Q&A.
6. [`current-decision-workspace/06-SCENARIO-SIMULATIONS.md`](current-decision-workspace/06-SCENARIO-SIMULATIONS.md) — local, hybrid, external, CLI-autonomy, evidence-mode and synthesis scenarios.
7. [`current-decision-workspace/01-RESEARCH-SOURCE-INDEX.md`](current-decision-workspace/01-RESEARCH-SOURCE-INDEX.md) — routing/index for V2.1, V3, Deep Research and current primary-source evidence.
8. [`current-decision-workspace/07-FUTURE-DEVELOPMENT.md`](current-decision-workspace/07-FUTURE-DEVELOPMENT.md) — explicitly deferred visual-only evidence and non-factual provenance work.
9. [`current-decision-workspace/sources/2026-08-20-GPT-V21-DR-OPTION-MATRIX.md`](current-decision-workspace/sources/2026-08-20-GPT-V21-DR-OPTION-MATRIX.md) — preserved V2.1 × Deep Research reconciliation source.
10. [`current-decision-workspace/sources/2026-08-20-GPT-V3-LANGGRAPH-LANGEXTRACT-RECONCILIATION.md`](current-decision-workspace/sources/2026-08-20-GPT-V3-LANGGRAPH-LANGEXTRACT-RECONCILIATION.md) — preserved V3/LangGraph/LangExtract/local-cloud reconciliation source.

### Current governing rules

> **Reuse before invention.** Existing maintained systems own capabilities first.

> **Measure before remove.** A credible reusable component that plausibly adds value receives a bounded test before rejection.

> **Product value, not stage count.** Simplification is only good when value is preserved or improved.

> **Local-first preference, not absolute prohibition.** External APIs/subscription models may be selected only when they demonstrate significant value over practical local alternatives.

> **Deterministic workflow state.** Normal pipeline sequence/state/retry/recovery is owned by code/workflow runtime, not chat memory. Autonomous CLI agents remain allowed but high-risk and must earn their role through large value and reliable execution.

> **Recommendations are not decisions.** `current-decision-workspace/02-DECISIONS.md` is the operator decision authority.

---

## 1. V3 historical/current research layer

V3 corrected the process failure in V2.1 by moving from a frozen 15-stage architecture toward evidence-first selection:

`find proven systems -> run them -> compare actual products -> identify gaps -> benchmark needed components -> integrate the smallest winning composition`

Relevant files:

- `v3-proven-infrastructure/01-V3-ARCHITECTURE.md`
- `v3-proven-infrastructure/02-V3-IMPLEMENTATION-PLAN.md`
- `v3-proven-infrastructure/03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
- `v3-proven-infrastructure/04-V3-COMPONENT-REGISTRY.yaml`
- `v3-proven-infrastructure/05-V3-OPENCLAW-ANTIGRAVITY-ORCHESTRATION.md`
- `v3-proven-infrastructure/06-V3-ORCHESTRATOR-HANDOVER.md`

V3 is **research/process evidence**, not proof of a selected working product pipeline. Its most valuable rules have been incorporated into the current decision workspace.

---

## 2. V2/V2.1 preserved research and implementation history

The earlier V2/V2.1 set remains important evidence and candidate knowledge but is no longer the current continuation authority.

Key files:

1. `v2-reuse-bakeoff/00-START-HERE.md`
2. `v2-reuse-bakeoff/06-TRIAL1-TRANSPORT-LOCK.yaml`
3. `v2-reuse-bakeoff/01-ARCHITECTURE-ANALYSIS.md`
4. `v2-reuse-bakeoff/02-IMPLEMENTATION-PLAN.yaml`
5. `v2-reuse-bakeoff/03-BENCHMARK-AND-TEST-SPEC.yaml`
6. `v2-reuse-bakeoff/04-COMPONENT-REGISTRY.yaml`
7. `v2-reuse-bakeoff/05-SOURCE-DECISION-EVIDENCE.yaml`
8. `v2-reuse-bakeoff/archive-pre-v3-authority/10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.original.md`
9. `v2-reuse-bakeoff/archive-pre-v3-authority/11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.original.md`

### Important interpretation correction

Historical V2.1 files reported completed implementation and satisfied hard gates. The actual operator outcome did not deliver a satisfactory working pipeline. Therefore these PASS labels are retained as historical evidence about the old validation process, **not treated as proof of product success**.

---

## 3. Historical documents and evidence

| Priority | Document / Asset | Status | Purpose |
| :---: | :--- | :--- | :--- |
| **00** | `00-INDEX.md` | **Current** | Master catalog and current decision-workspace route. |
| **00.C** | `current-decision-workspace/**` | **Current authority** | Current decisions, recommendation, matrix, scenarios, open tests and source captures. |
| **00.V3** | `v3-proven-infrastructure/**` | Research/process evidence | Evidence-first process correction and component registry. |
| **00.V2** | `v2-reuse-bakeoff/**` | Historical/candidate evidence | Reuse-first research, old bake-off and prior implementation. |
| **H-V1.1** | `archive/transcript-pipeline-v1-2026-08-18/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml` | Superseded | Earlier minimal V1 decision contract. |
| **H-V1.2** | `archive/transcript-pipeline-v1-2026-08-18/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md` | Superseded | Earlier architecture analysis. |
| **H-V1.3** | `archive/transcript-pipeline-v1-2026-08-18/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md` | Superseded | Earlier direct-CLI-only execution plan. |
| **01** | `POST_REPAIR_EVALUATION_REPORT.md` | Historical evidence | Post-repair evaluation. |
| **02** | `RESEARCH_ADVANCED_IMPROVEMENTS_AND_UNIFICATION.md` | Historical research | Resilience/simplicity/token-efficiency research. |
| **02.1** | `HYBRID_CROSS_POLLINATION_AND_UNIFICATION_STRATEGY.md` | Historical research | Prior cross-pollination ideas. |
| **03** | `PROCESS_STEP_COMPARISON_MATRIX.md` | Historical evidence | Prior lifecycle comparison. |
| **04** | `HANDOVER_MULTI_PIPELINE_EVALUATION.md` | Historical handover | Prior evaluation context. |

---

## 4. Benchmark corpus retained

1. `P-h5WSQG1Sw` — long English neuroscience interview; long-context/multi-speaker stress.
2. `CygwqaNg2PY` — technical finance/Elliott Wave source.
3. `vFTuLylvYnA` — German finance/domain-term/numeric ASR source.
4. `oZIsMX6WgFs` — optional technical procedure/mechanism source.

The current workspace may reduce fixture scope for individual component tests; do not rerun every full source for every question.

---

## 5. Current next step

Do **not** run another monolithic implementation.

Execute the highest-leverage bounded research/tests in `current-decision-workspace/05-OPEN-QUESTIONS-AND-TESTS.md`, beginning with product/output use-case clarification and the local-Qwen/LangExtract/synthesis comparisons that materially determine whether local, subscription, API, or hybrid semantic paths are viable.

After the high-leverage questions close, freeze a new selected architecture and implementation plan. Until then, `current-decision-workspace/04-CURRENT-RECOMMENDATION.md` is explicitly provisional.