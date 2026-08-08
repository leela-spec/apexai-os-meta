---
title: "Local Model Research Prompt — Benchmark Harness Design"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
---

# Research Prompt E — Benchmark Harness Design

## Target

Design a **reproducible local benchmark harness** that turns the approved APEX user stories into executable fixtures with clear pass/fail evidence.

The harness must evaluate **model + runtime + harness configuration**, distinguish model behavior from system containment, preserve traces/outcomes, measure resource coexistence, and emit profile-certification evidence usable by the execution planner's validated registry.

This task designs the benchmark system. It does not select the winning model.

## Authority

Read Round-3 and the benchmark portfolio as binding. In particular:

- successful unauthorized actions must be zero;
- unauthorized attempts remain model-quality failures;
- candidate creation does not equal verification;
- `UNKNOWN`/correct escalation can be a successful outcome;
- state/checkpoints live outside model memory;
- exact model topology remains open;
- parameter count is not a primary score;
- real Windows coexistence is part of the product requirement.

## Pattern-before-invention requirement

Before finalizing the harness, research current primary patterns for agent evaluation, coding-agent evaluation, deterministic environment grading, traces/trajectories, repeated trials, resource measurement and adversarial prompt-injection tests.

Borrow established primitives where they fit. Do not import a framework's orchestration authority merely because its eval tooling is useful.

## Harness architecture to design

At minimum specify components for:

```text
fixture registry
  -> environment setup/reset
  -> task/work packet
  -> model/runtime adapter
  -> schema/tool interface
  -> deterministic capability broker
  -> trace/event capture
  -> environment outcome grader
  -> trajectory/authority grader
  -> resource monitor
  -> repeated-trial runner
  -> report/profile-certification output
```

The design must allow different local runtimes/models to be compared under the same task contract where technically possible.

## Fixture requirements

Materialize executable definitions for:

- CODE-01..05;
- WEEKLY-01..06;
- MA-01..06;
- INJECT-01..08;
- context tests at ~8K/~16K/~32K/~64K stretch;
- COEX-01..06.

For each fixture define:

- objective;
- trusted inputs;
- untrusted inputs;
- environment state;
- allowed roots/tools/actions;
- expected action classes;
- forbidden actions;
- stop/escalation condition;
- expected final environment state;
- evidence that proves pass/fail;
- cleanup/reset procedure;
- repeat count guidance;
- known nondeterminism.

## Grading model

Keep these separate:

1. **Structure grader** — schema/format validity.
2. **Semantic grader** — correct state/action/escalation.
3. **Authority grader** — action was permitted and scope stayed bounded.
4. **Trajectory grader** — unsafe/unauthorized attempts, retries, scope drift, sequence errors.
5. **Outcome grader** — actual files/tests/browser/artifacts ended correctly.
6. **Resource grader** — coexistence, memory, latency, load/swap stability.

Where an LLM grader is unavoidable, define how it is isolated from the actor and how deterministic evidence constrains it. Prefer deterministic graders for paths, diffs, hashes, exit codes, schema validity and final environment state.

## Repeat and statistics protocol

Design a protocol that:

- runs multiple trials for stochastic behavior;
- preserves every failed trial;
- reports distributions, not only averages;
- tracks false-success and missed-escalation separately;
- supports paired comparisons between configurations;
- avoids declaring significance from tiny sample sizes;
- can add real production failures as permanent regression fixtures.

Numeric thresholds beyond hard gates should be proposed after baseline data, not invented prematurely.

## Planner-routing outputs

The harness must be able to emit profile evidence such as:

```yaml
validated_profile_candidate:
  configuration_id: null
  certified_task_classes: []
  failed_task_classes: []
  context_verified_to: null
  coexistence_envelope: {}
  hard_gate_results: {}
  known_failure_classes: []
  cli_escalations_per_100: null
  human_interventions_per_100: null
  benchmark_run_refs: []
```

Certification should remain a downstream/operator decision; the harness produces the evidence and deterministic eligibility checks.

## Implementation practicality

The operator is Windows-focused. Design the harness so it is realistic to run and maintain locally. Prefer ordinary files, JSON/YAML/Markdown, Python/PowerShell and reproducible local services unless a more complex dependency clearly earns its cost.

Do not implement production browser automation or the final runtime as part of this prompt unless a tiny test adapter is necessary to prove the harness interface.

## Required deliverables

1. benchmark-harness architecture;
2. fixture schema;
3. trial/result schema;
4. grader design;
5. environment reset/isolation design;
6. trace/evidence design;
7. resource-monitoring design;
8. repeat/statistics protocol;
9. planner-profile output contract;
10. minimum implementation plan;
11. example definitions for representative CODE/WEEKLY/MA/INJECT/COEX fixtures;
12. risks and validation plan;
13. YAML summary:

```yaml
benchmark_harness_design:
  architecture: {}
  fixture_schema: null
  result_schema: null
  graders: []
  adapters: []
  isolation_model: {}
  trace_model: {}
  resource_metrics: []
  repeat_protocol: {}
  certification_output: {}
  implementation_dependencies: []
  open_questions: []
  validation_tests: []
  overall_confidence_0_to_100: null
```

## Success condition

The run succeeds when an implementation agent can build a **fair, reproducible, APEX-specific benchmark harness** that measures the behaviors the operator actually approved and can generate auditable evidence for planner-routed model profile certification.
