---
title: "Local Model Research Prompt — Current Model Landscape"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
---

# Research Prompt A — Local Model Landscape

## Target

Research and produce a **current local-model candidate landscape for APEX planner-routed bounded execution**.

The deliverable must identify which current local model families/configurations are plausible enough to enter benchmark screening, with emphasis on **high reasoning capability that remains practically sustainable** on the operator's Windows laptop.

Do not choose the production model. Produce a decision-quality candidate set and evidence map.

## Authority model

1. `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` defines the role, authority, reasoning-first objective and planner-routing architecture.
2. `LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md` defines what must ultimately be measured.
3. Current official model cards, repositories, release notes and technical reports define candidate reality.
4. Current official runtime documentation may establish deployability, not execution quality.
5. Independent benchmarks may inform prioritization but never replace APEX fixtures.

## Research framing

Do **not** begin from parameter-count buckets or the old 7–8B assumption.

Instead build the candidate set from these capability hypotheses:

- efficient baseline/control model;
- strong-reasoning general executor candidates;
- higher-reasoning stretch candidates that may fit with aggressive/runtime-efficient representations;
- coding-reasoning challengers;
- architecture-efficient models that may deliver unusually strong reasoning per resident resource.

A larger model may be preferred when quality gains materially reduce bad actions, retries, human intervention or CLI escalation. A smaller model may still win a task class when the larger candidate adds little useful reliability or harms coexistence.

## What to research

For each serious candidate establish, from current primary sources where possible:

- exact model/version/date;
- architecture and parameter class;
- license and local-use constraints;
- supported context length and any evidence about reliable long-context use;
- structured output / tool-use / agent or function-calling training where documented;
- reasoning and instruction-following positioning;
- coding capability where relevant;
- model artifact formats and quantization availability;
- realistic Windows local-runtime compatibility;
- Intel CPU/GPU/NPU compatibility through relevant runtimes where known;
- memory/compute implications as evidence or estimates, clearly labeled;
- known limitations relevant to bounded execution, tool use, refusal, prompt injection or long context.

## Required candidate breadth

Include enough diversity to test the reasoning-first thesis rather than only one size family. Do not include candidates merely to fill a quota.

Explicitly ask whether current models materially stronger than the old practical-center class are now realistic on ~32 GB shared-memory hardware through quantization, partial offload, CPU/GPU/NPU execution or load-on-demand scheduling.

## Evaluation lens

Map each candidate qualitatively against:

- CODE bounded execution;
- Weekly browser/state/recovery execution;
- Multi-Agent worker/evidence support;
- hostile-content resistance potential;
- 32K reliable working-context plausibility;
- structured/tool output plausibility;
- resource coexistence risk;
- runtime support maturity;
- likely role in a planner-routed registry.

Do not claim benchmark certification from public benchmarks.

## Required deliverables

Produce one coherent research packet containing:

1. executive finding;
2. evidence date and freshness map;
3. serious-candidate shortlist with exact versions;
4. excluded/not-priority candidates and why;
5. capability-by-task-class matrix;
6. context/tool/structured-output evidence;
7. local artifact/runtime availability map;
8. reasoning-strength versus resource-risk matrix;
9. benchmark priority order;
10. major unknowns that only local APEX testing can settle;
11. source appendix dominated by current primary sources;
12. YAML output:

```yaml
local_model_landscape:
  evidence_date: null
  candidates: []
  benchmark_priority: []
  efficient_baseline_candidates: []
  strong_reasoning_candidates: []
  stretch_reasoning_candidates: []
  coding_challengers: []
  architecture_efficient_challengers: []
  excluded_or_deprioritized: []
  context_findings: {}
  structured_tool_findings: {}
  windows_runtime_findings: {}
  resource_unknowns: []
  apex_benchmark_unknowns: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- No production selection.
- No parameter-count ceiling in advance.
- Do not confuse public benchmark strength with APEX execution reliability.
- Do not infer dedicated VRAM from integrated-GPU memory reporting.
- Separate measured, documented, inferred and unknown claims.
- Prefer primary sources and current versions.
- Preserve important disagreement or missing evidence as benchmark questions.

## Success condition

The run succeeds when the benchmark team has a **small but sufficiently broad, current and evidence-backed candidate set** capable of testing whether higher reasoning materially improves APEX local execution under the operator's actual hardware constraints.
