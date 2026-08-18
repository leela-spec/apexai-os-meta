---
title: "START HERE — Transcript→Knowledge V2 Reuse Bake-off"
doc_type: implementation_handover
created: 2026-08-18
status: ready_for_execution
repository: leela-spec/apexai-os-meta
branch_policy: main_only_unless_operator_explicitly_changes_it
supersedes:
  - SourceTranscriptionAnalysisPipeline_Research/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md
  - SourceTranscriptionAnalysisPipeline_Research/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml
  - SourceTranscriptionAnalysisPipeline_Research/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md
supersession_scope: architecture_selection_and_implementation_sequence_only
preserve_history: true
---

# 0. Instruction to the receiving CLI AI

This is an **execution handover**, not an invitation to restart architecture research from zero.

The previous V1 over-corrected toward minimalism and wrongly removed researched reusable components before testing them. V2 corrects that failure with this rule:

> **Measure before remove.** If a mature reusable component plausibly replaces custom code, reduces expensive reasoning, improves evidence quality, or adds an independent safety/evaluation signal, benchmark it before rejecting it. Do not put every candidate in the production hot path; classify it as core, conditional, challenger, evaluator, or baseline and test its actual contribution.

The receiving AI must implement the bake-off and produce evidence. It must **not** decide in advance that the simplest architecture wins, nor decide in advance that the most feature-rich architecture wins.

## 0.1 Immediate next action

Read this file, then read `06-TRIAL1-TRANSPORT-LOCK.yaml` before any implementation or benchmark task. After that, read the remaining files below in order, verify repository state, then execute **Task P0** in `02-IMPLEMENTATION-PLAN.yaml`.

Do not begin by modifying TTK, installing all dependencies, or rewriting the pipeline.

## 0.2 Required reads, in order

1. `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/00-START-HERE.md`
2. `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/06-TRIAL1-TRANSPORT-LOCK.yaml`
3. `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/01-ARCHITECTURE-ANALYSIS.md`
4. `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/04-COMPONENT-REGISTRY.yaml`
5. `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/02-IMPLEMENTATION-PLAN.yaml`
6. `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/03-BENCHMARK-AND-TEST-SPEC.yaml`
7. `.claude/skills/transcript-to-knowledge/SKILL.md`
8. `.claude/skills/transcript-to-knowledge/references/semantic-contracts.md`
9. `.claude/skills/transcript-to-knowledge/references/architecture.md`
10. `.claude/skills/transcript-to-knowledge/references/operator-runbook.md`
11. `.claude/skills/transcript-to-knowledge/references/evals.md`
12. `.claude/skills/transcript-to-knowledge/scripts/ttk.py`
13. `.claude/skills/transcript-to-knowledge/scripts/test_ttk.py`
14. `.claude/skills/transcript-to-knowledge/scripts/execute_ttk_lifecycle.py`
15. `.claude/skills/SourceTranscriptionAnalysisPipeline/scripts/transcribe_audio.py`
16. `scripts/Run-BatchMultiPipelineBenchmark.ps1`
17. `artifacts/benchmark_runs/20260818-185245/receipt.json`
18. `SourceTranscriptionAnalysisPipeline_Research/POST_REPAIR_EVALUATION_REPORT.md`
19. `SourceTranscriptionAnalysisPipeline_Research/RESEARCH_ADVANCED_IMPROVEMENTS_AND_UNIFICATION.md`
20. `SourceTranscriptionAnalysisPipeline_Research/HYBRID_CROSS_POLLINATION_AND_UNIFICATION_STRATEGY.md`

Read historical files for evidence and previously observed failures. Where they conflict with this V2 set, this V2 set controls implementation sequencing unless the operator gives a newer explicit instruction. For **Trial 1 AI transport/provider policy specifically**, `06-TRIAL1-TRANSPORT-LOCK.yaml` is authoritative over conflicting older V2 lines.

# 1. Constant frame

```yaml
frame:
  mission: >
    Build and empirically select a resilient audio/video-to-knowledge pipeline that
    produces useful, source-grounded knowledge artifacts. Prefer mature reusable
    software over fragile custom invention, but keep only components that earn
    their complexity through measured value.

  actual_product:
    goal: trustworthy_high_value_knowledge_artifact
    asr_role: prerequisite_quality_gate
    representation: macro_meso_micro_preferred_but_replaceable_if_better_measured

  orchestration:
    normal_trigger: APEX/OpenClaw
    execution_host: Windows local machine
    qwen_role_v2: none_in_this_pipeline
    semantic_workers_available_trial1:
      - Claude Code CLI
      - Codex CLI
      - Antigravity CLI
    semantic_workers_deferred_after_trial1:
      - Gemini CLI
      - browser subscription AIs through existing OpenClaw/browser infrastructure
    trial1_ai_transport_policy: subscription_cli_only
    trial1_api_key_billing_allowed: false
    trial1_paid_api_allowed: false
    paid_api_policy_after_trial1: undesirable_but_visible_for_later_benchmark_or_escalation
    trial1_component_rule: 'If a framework needs strong AI, it must call an allowed subscription CLI through a local adapter or be marked BLOCKED_FOR_TRIAL1.'

  evidence_principles:
    - transcript is immutable source evidence
    - source support and external truth are separate dimensions
    - factual Micro claims require exact source evidence
    - non-factual semantic objects require source provenance but not forced quote quotas
    - processing windows are transport units, not semantic chapters
    - context-only text may aid interpretation but cannot become source evidence
    - deterministic validation must fail closed
    - no missing semantic stage may be reported as success
    - benchmark results must identify exact code/config/provider/input provenance

  architecture_principles:
    - deterministic code for deterministic jobs
    - specialized mature software/models for narrow solved jobs
    - strong general AI only where genuine semantic reasoning remains
    - measure before remove
    - no production hot-path dependency without a demonstrated role
    - one component may be installed as a challenger without being production-selected
    - complexity without demonstrated value is over-engineering
    - complexity that materially improves accuracy, insight recall, grounding, reliability,
      token efficiency, operator usefulness, or custom-code elimination is permitted

  local_hardware:
    os: Windows 11 Home
    cpu: Intel Core Ultra 7 258V
    cpu_cores: 8
    ram_gb: 31.63
    gpu: Intel Arc 140V integrated GPU
    gpu_reported_opencl_memory_gb: 16.5
    notes:
      - GPU memory is shared/unified system memory; do not treat 16.5 GB as dedicated VRAM.
      - Installation/runtime feasibility must be measured on this machine, not inferred from desktop NVIDIA assumptions.

  branch_policy: main_only_unless_operator_explicitly_changes_it
```

# 2. Authority and source hierarchy

Use this order when instructions conflict:

1. current explicit operator instruction;
2. `06-TRIAL1-TRANSPORT-LOCK.yaml` for Trial 1 AI transport/provider policy;
3. this V2 handover and its machine-readable plan/spec;
4. current TTK contracts and validators for existing implemented invariants;
5. measured benchmark/test evidence from the repository;
6. current official/primary documentation for external tools;
7. prior architecture/research documents;
8. prose assumptions or remembered chat context.

Never treat a research recommendation as a production selection until its promotion gate passes.

# 3. What is already known

## 3.1 Preserve TTK's trustworthy spine

TTK already provides the valuable transcript-specific state/evidence layer:

- source SHA custody;
- canonical segment IDs;
- processing windows and context halo;
- packet hashes;
- stale-result detection;
- resumability from files;
- deterministic structural/provenance validation;
- selective fact-verification queue;
- final compiler.

Do not replace these merely because a generic framework also offers chunking or orchestration.

## 3.2 Remove/disable the known pseudo-semantic failure

Current `execute_ttk_lifecycle.py` contains heuristic/regex semantic-looking generation. That code may be preserved for forensic history if necessary, but it must not remain a path that can report genuine semantic completion.

Known invalid semantic authority patterns include:

- keyword-based claim typing as final truth;
- regex proper nouns as final entities;
- arbitrary transcript sentence fragments as final claims;
- fixed mechanical Meso grouping;
- generic Macro boilerplate;
- stamping `source_support: SUPPORTED` without semantic entailment judgment.

## 3.3 Qwen is not part of this pipeline

Do not route semantic work through local Qwen. Do not invent a task for it. APEX/OpenClaw or deterministic scripts can dispatch programs directly.

# 4. V2 component lanes

```yaml
lanes:
  core:
    - existing source acquisition / yt-dlp + ffmpeg path
    - TTK custody, packets, hashes, validation, resume, verify queue, compiler
    - strong subscription CLI semantic worker as the semantic-authority class
  primary_candidate:
    - faster-whisper for first ASR reference
    - direct strong-CLI Map/Reduce reference path
  conditional:
    - WhisperX for alignment/diarization when multi-speaker provenance or timestamp quality warrants it
  challengers:
    - NVIDIA Parakeet TDT 0.6B v3 for ASR
    - LangExtract for grounded extraction/source-span handling
    - GLiNER2 for cheap local pre-extraction
    - NuExtract 2.x if GLiNER2 fails its role
    - DocETL for semantic Map/Reduce orchestration
    - Instructor if native CLI schema/retry plumbing is insufficient or multi-provider unification earns it
  advisory_safety:
    - multilingual mDeBERTa NLI
    - Vectara HHEM for English factual-consistency comparison
  evaluation:
    - deterministic benchmark metrics
    - DeepEval where it adds repeatable semantic metrics
    - targeted human gold labels
  product_baselines:
    - Fabric
    - Open Notebook
    - yt-distill / youtube-transcript knowledge tools where installable
  deferred_external_oracles_after_trial1:
    - hosted ASR/API experiments may be reconsidered only after the subscription-CLI-only first trial and explicit operator approval
```

# 5. Write scope for the receiving implementation AI

The plan declares exact write targets task-by-task. Default allowed areas are:

```text
SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/**
artifacts/transcript_pipeline_v2/**
.claude/skills/transcript-to-knowledge/**                # only in implementation tasks explicitly authorizing it
.claude/skills/SourceTranscriptionAnalysisPipeline/**    # only in ASR tasks explicitly authorizing it
scripts/transcript_pipeline_v2/**                        # new isolated benchmark/adapter code
```

Do not modify unrelated APEX/Weekly/Plan/Session/OpenClaw architecture.

Do not modify Qwen/OpenClaw FEE behavior to make this transcript experiment work.

# 6. Stop conditions

Stop the active task and record `BLOCKED` rather than improvising if:

- repository is not `leela-spec/apexai-os-meta`;
- branch is not `main` unless the operator explicitly changed policy;
- a task would overwrite unrelated user changes;
- a dependency install would require destructive system-wide changes when an isolated venv can be used;
- a candidate needs credentials/tokens that are not already configured and the plan has no permitted fallback;
- a benchmark input is missing or has changed SHA without the benchmark manifest being updated;
- a semantic worker cannot be invoked non-interactively and no declared fallback is available;
- a supposedly deterministic validator requires guessing semantic content;
- a test/benchmark result cannot be attributed to an exact component/configuration;
- the implementation would need a new database/service/workflow engine without first demonstrating that file/hash state is insufficient;
- the implementation AI is tempted to substitute heuristic semantic output when a real semantic call fails.

# 7. Commit discipline

- Work directly on `main` under the operator's established branch policy.
- Before each implementation commit: inspect `git status`, stage only declared files, run the task's validation, then `git diff --cached --check`.
- Keep component-install/benchmark harness commits separate from production-selection commits.
- Do not promote a challenger merely because installation succeeded.
- Do not delete losing experiment artifacts; preserve receipts and mark the candidate verdict.

# 8. Final handover requirement

The implementation run is incomplete until it writes a final machine-readable report matching `03-BENCHMARK-AND-TEST-SPEC.yaml` and a fresh AI can answer, from repository artifacts alone:

- which components were installed successfully;
- which were actually benchmarked;
- which configurations ran on which source slices/windows;
- what each component improved or harmed;
- which hard gates failed;
- which architecture won each stage;
- what remains `UNMEASURED`;
- what the recommended first production pipeline is;
- why every retained component earned its place;
- why every rejected component was rejected;
- the exact next implementation/test action.

If a fresh reader cannot reconstruct those answers without chat history, the handover fails.
