---
title: "Local Model Research Prompt — Cross-Research Synthesis"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
---

# Research Prompt F — Local Model / Runtime / Routing Synthesis

## Target

Research, reconcile and produce a **local-model execution decision packet** for APEX from the completed model-landscape, coding, Weekly/Multi-Agent, Windows/runtime and benchmark-harness research plus any available local benchmark results.

The packet must recommend **which model+runtime configurations should enter the first local bake-off, which task-specific capability profiles they are hypotheses for, how planner routing should use certified profiles, what remains unknown, and exactly what evidence would change the recommendation**.

Do not force one model or a model ladder. Model topology is intentionally evidence-driven.

## Authority

1. `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` — operator-approved behavior, reasoning-first objective, planner routing and authority boundaries.
2. `LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md` — benchmark classes and hard gates.
3. Completed current research packets — evidence and candidate hypotheses.
4. Local APEX benchmark results — measured execution reality when available.
5. Current primary sources only where needed to resolve stale/conflicting claims.

No research packet may silently override an operator boundary.

## Core synthesis question

Answer:

> Which current local model+runtime configurations provide the strongest practically sustainable reasoning for each approved APEX task class, and how should the bounded execution planner route among configurations that have passed the relevant benchmark gates?

The answer may be:

- one configuration for all certified classes;
- one strong general profile plus coding or other specialist profiles;
- several task-specific profiles;
- local execution for some classes and direct Claude/Codex/subscription escalation for others.

Do not reward complexity without measured value.

## Required reconciliation

Reconcile at least:

- model reasoning strength versus scope-drift/missed-escalation risk;
- coding specialization versus general-model simplicity;
- context requirements versus retrieval/tool churn;
- structured-output capability versus semantic correctness;
- public benchmark evidence versus APEX fixture evidence;
- runtime throughput versus load/swap/context/coexistence behavior;
- CPU/GPU/NPU/backend trade-offs;
- larger-model quality gains versus shared-memory pressure;
- one-resident-model simplicity versus planner-routed switching;
- model behavior versus harness containment;
- platform/executor-runtime dependencies that could change model feasibility.

Preserve contradictions and distinguish measured evidence from inference.

## Hard gates

A configuration/profile cannot be recommended for certification if local evidence shows an unmitigated hard-gate failure.

At minimum:

- successful unauthorized actions = zero;
- no candidate/verified authority bypass;
- no untrusted-content-created authority;
- correct halt/escalation for consequential unknowns;
- reconstructable evidence/checkpoint behavior;
- workable Windows coexistence for the task class.

A weighted aggregate cannot compensate for a hard-gate failure.

## Planner-routing synthesis

Do not simply rank models globally.

Build a proposed registry shape such as:

```yaml
validated_profile_hypotheses:
  high_reasoning_general:
    configuration: null
    target_task_classes: []
    required_benchmarks: []
    resource_envelope: {}
    fallback_profile: null

  bounded_code:
    configuration: null
    target_task_classes: []
    required_benchmarks: []
    resource_envelope: {}
    fallback_profile: null
```

Only call a profile `validated` when actual APEX benchmark evidence supports it. Before local trials, use `candidate_profile` or equivalent.

Define what the execution planner should inspect when routing:

- task class;
- reasoning requirement;
- context requirement;
- tool complexity;
- latency sensitivity;
- risk class;
- current machine/resource state;
- available certified profiles;
- fallback/escalation policy.

Keep the planner itself subordinate to deterministic policy validation.

## First bake-off design

Choose the smallest bake-off that can settle the consequential questions.

Include enough candidates to test:

- efficient baseline;
- strong-reasoning general configuration(s);
- higher-reasoning stretch configuration(s) if feasible;
- coding specialist if evidence says it could earn complexity;
- materially distinct runtime/backend options where runtime uncertainty affects results.

Avoid combinatorial explosion. Use screening to eliminate configurations that cannot plausibly meet resource/hard-gate requirements before full trials.

## Required comparison outputs

For each surviving candidate/configuration provide:

- exact version/artifact/runtime/backend;
- target APEX task classes;
- expected strengths;
- expected failure modes;
- context tier to test;
- structured/tool support;
- resource risk;
- required CODE/WEEKLY/MA/INJECT/COEX fixtures;
- evidence confidence;
- reversal trigger.

## Required deliverables

Produce one coherent decision packet with:

1. executive recommendation for first bake-off;
2. evidence freshness/version map;
3. cross-research contradiction table;
4. candidate configuration matrix;
5. per-task-class model/runtime hypotheses;
6. hard-gate status;
7. reasoning-strength versus resource/authority-risk analysis;
8. proposed planner-routing capability profiles;
9. proposed local bake-off sequence;
10. runtime/backend tests required;
11. rejected/deprioritized candidates and why;
12. remaining unknowns;
13. reversal triggers;
14. final operator decisions required before production selection;
15. YAML:

```yaml
local_model_synthesis:
  evidence_date: null
  research_packets: []
  benchmark_results_available: []
  candidate_configurations: []
  hard_gate_summary: {}
  task_class_hypotheses: {}
  planner_profile_hypotheses: {}
  reasoning_vs_resource_findings: {}
  contradictions: []
  recommended_first_bakeoff: []
  runtime_backend_tests: []
  rejected_or_deprioritized: []
  unknowns: []
  reversal_triggers: []
  operator_questions_remaining: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- No production selection before operator review and required local benchmarks.
- Do not pre-lock one model, two models, ladder or coder split.
- Do not make parameter count the optimization target.
- Do not equate bigger with better or smaller with efficient without workload evidence.
- Do not increase model authority based on reasoning quality.
- Keep platform selection and model selection distinct while surfacing real dependencies.
- Do not hide contradictory measurements behind an average score.

## Validation

Before delivery verify that:

- every recommendation maps to approved APEX fixtures;
- stronger reasoning is tested for actual execution value, not assumed valuable;
- resource coexistence is treated as product behavior;
- planner routing uses only benchmark-certified profiles in the final architecture;
- model and runtime versions are explicit;
- hard gates override weighted utility;
- remaining uncertainty is converted into the smallest decisive test;
- the operator receives choices rather than a silent production decision.

## Success condition

The run succeeds when the operator can decide **which model+runtime configurations to benchmark first and what evidence is required before they may enter the planner-routable registry**, without precommitting APEX to a model size, family or topology.
