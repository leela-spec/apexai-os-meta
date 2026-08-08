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

The packet must determine whether the operator's **~7–8B practical-optimum hypothesis** holds, which model+runtime configurations should enter the first local bake-off, which task-specific capability profiles they are hypotheses for, how planner routing should use certified profiles, what remains unknown, and what evidence would change the recommendation.

Do not force one model or a model ladder. Model topology remains evidence-driven.

## Authority

1. `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` — operator-approved behavior, ~7–8B practical-center prior, planner routing and authority boundaries.
2. `LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md` — benchmark classes and hard gates.
3. Completed current research packets — evidence and candidate hypotheses.
4. Local APEX benchmark results — measured execution reality when available.
5. Current primary sources only where needed to resolve stale/conflicting claims.

No research packet may silently override an operator boundary.

## Core synthesis question

Answer:

> **Does a strong current ~7–8B model provide the best practical balance for APEX local execution, and where—if anywhere—does a smaller or larger benchmark-certified configuration justify displacing it for a specific task class?**

Possible outcomes include:

- one ~7–8B configuration covers all certified local classes;
- a ~7–8B general profile plus a coding specialist;
- a smaller model is sufficient for selected cheap/routine classes;
- a larger model is justified for a narrow high-difficulty local class;
- some classes should bypass local escalation and go directly to Claude/Codex/subscription reasoning.

Do not reward complexity without measured value.

## Required reconciliation

Reconcile at least:

- ~7–8B execution quality versus ~3–4B resource advantage;
- ~12–14B quality gain versus ~7–8B memory/latency/coexistence advantage;
- coding specialization versus general-model simplicity;
- context requirements versus retrieval/tool churn;
- structured-output capability versus semantic correctness;
- public benchmark evidence versus APEX fixture evidence;
- runtime throughput versus load/swap/context/coexistence behavior;
- CPU/GPU/NPU/backend trade-offs;
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

Weighted utility cannot compensate for a hard-gate failure.

## Planner-routing synthesis

Do not rank models globally and stop there.

Build candidate registry profiles such as:

```yaml
candidate_profiles:
  practical_center_general:
    expected_parameter_class: "~7–8B"
    configuration: null
    target_task_classes: []
    required_benchmarks: []
    resource_envelope: {}
    fallback_profile: null

  bounded_code:
    expected_parameter_class: null
    configuration: null
    target_task_classes: []
    required_benchmarks: []
    resource_envelope: {}
    fallback_profile: null
```

Only call a profile `validated` when actual APEX benchmark evidence supports it.

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

Keep the planner subordinate to deterministic policy validation.

## First bake-off design

The first bake-off should be centered on the operator's prior, not on maximum candidate breadth.

Include:

1. **the strongest one or two ~7–8B primary configurations**;
2. **one credible ~3–4B efficiency control**;
3. **one ~12–14B challenger** only if runtime/hardware research says it is realistically usable and likely to settle a meaningful question;
4. a coding specialist only if research says it may materially reduce CLI escalation;
5. materially distinct runtime/backend options only where runtime uncertainty could change the result.

Do not include >14B by default. Include it only when current evidence makes it locally plausible and likely to alter a decision.

Avoid combinatorial explosion. Screen out configurations that cannot plausibly meet resource/hard-gate requirements before full trials.

## Required comparison outputs

For each surviving configuration provide:

- exact version/artifact/runtime/backend;
- parameter class;
- target APEX task classes;
- expected strengths;
- expected failure modes;
- context tier to test;
- structured/tool support;
- resource risk;
- required CODE/WEEKLY/MA/INJECT/COEX fixtures;
- evidence confidence;
- reversal trigger.

For the ~7–8B prior specifically report:

```text
CONFIRMED
  evidence supports ~7–8B as practical optimum

PARTIAL
  ~7–8B is default, but another class wins selected task classes

REJECTED
  another class gives a clearly better total APEX outcome

UNRESOLVED
  evidence insufficient; name the smallest decisive test
```

## Required deliverables

Produce one coherent decision packet with:

1. executive recommendation for first bake-off;
2. **verdict on the ~7–8B practical-optimum hypothesis**;
3. evidence freshness/version map;
4. cross-research contradiction table;
5. candidate configuration matrix;
6. per-task-class model/runtime hypotheses;
7. hard-gate status;
8. size/reasoning versus resource/authority-risk analysis;
9. proposed planner-routing capability profiles;
10. proposed local bake-off sequence;
11. runtime/backend tests required;
12. rejected/deprioritized candidates and why;
13. remaining unknowns;
14. reversal triggers;
15. final operator decisions required before production selection;
16. YAML:

```yaml
local_model_synthesis:
  evidence_date: null
  research_packets: []
  benchmark_results_available: []
  practical_7_8b_hypothesis_verdict: null
  candidate_configurations: []
  hard_gate_summary: {}
  task_class_hypotheses: {}
  planner_profile_hypotheses: {}
  size_resource_findings: {}
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
- **Do not replace the ~7–8B practical-center prior with a largest-model optimization objective.**
- Do not treat the ~7–8B prior as proof; make evidence confirm or reject it.
- Do not equate bigger with better or smaller with efficient without workload evidence.
- Do not increase model authority based on capability.
- Keep platform selection and model selection distinct while surfacing dependencies.
- Do not hide contradictory measurements behind an average score.

## Validation

Before delivery verify that:

- every recommendation maps to approved APEX fixtures;
- the ~7–8B prior was tested rather than assumed or silently discarded;
- smaller/larger comparisons quantify both execution value and resource cost;
- resource coexistence is treated as product behavior;
- planner routing uses only benchmark-certified profiles in final architecture;
- model/runtime versions are explicit;
- hard gates override weighted utility;
- remaining uncertainty becomes the smallest decisive test;
- operator receives choices rather than a silent production decision.

## Success condition

The run succeeds when the operator can decide whether **~7–8B really is the optimal practical center**, which exceptions deserve separate routed profiles if any, and exactly what local evidence is still required before model/runtime configurations enter the validated registry.
