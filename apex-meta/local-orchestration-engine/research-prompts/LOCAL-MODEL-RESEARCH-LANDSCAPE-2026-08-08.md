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

The operator's working hypothesis is that **~7–8B is the practical optimum** for the main local executor on the current Windows laptop. Treat that as the primary research center, not as an already-proven winner.

The deliverable must identify a small, current candidate set that can test this hypothesis against smaller efficiency controls and larger challengers.

Do not choose the production model.

## Authority model

1. `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` defines the role, authority, 7–8B practical-center prior and planner-routing architecture.
2. `LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md` defines what must ultimately be measured.
3. Current official model cards, repositories, release notes and technical reports define candidate reality.
4. Current official runtime documentation may establish deployability, not execution quality.
5. Independent benchmarks may inform prioritization but never replace APEX fixtures.

## Research framing

Start from this comparison structure:

```text
PRIMARY:    ~7–8B current strong general/instruction/tool-capable models
CONTROL:    ~3–4B efficient candidates
CHALLENGER: ~12–14B where hardware/runtime evidence makes local use credible
>14B:       only when specifically plausible and decision-relevant on this machine
```

The purpose is not to fill size buckets mechanically. The purpose is to test whether the expected 7–8B sweet spot actually gives the best APEX balance.

A smaller model may win a task class if it matches execution quality while materially improving coexistence. A larger model may win only if its measured execution gains are large enough to justify memory, latency, load/swap and coexistence costs.

## What to research

For each serious candidate establish, from current primary sources where possible:

- exact model/version/date;
- architecture and parameter class;
- license/local-use constraints;
- supported context length and evidence about reliable long-context use;
- structured output, tool-use or function-calling training where documented;
- reasoning and instruction-following positioning;
- coding capability where relevant;
- model artifact formats and quantization/representation availability;
- realistic Windows local-runtime compatibility;
- Intel CPU/GPU/NPU compatibility through relevant runtimes where known;
- memory/compute implications, clearly labeled as measured/documented/inferred;
- known limitations relevant to bounded execution, tool use, refusal, prompt injection or long context.

## Required candidate breadth

Prioritize the best current ~7–8B candidates first.

Then include only enough adjacent classes to test the prior:

- at least one credible ~3–4B efficiency control;
- at least one credible ~12–14B challenger if practical local execution appears realistic;
- coding-specialized candidates when they plausibly reduce Claude Code/Codex escalation;
- >14B only when concrete current runtime/hardware evidence makes the configuration realistic enough to matter.

Do not broaden the shortlist merely because a larger model scores higher on generic reasoning benchmarks.

## Evaluation lens

Map each candidate qualitatively against:

- CODE bounded execution;
- Weekly browser/state/recovery execution;
- Multi-Agent worker/evidence support;
- hostile-content resistance potential;
- ~32K reliable working-context plausibility;
- structured/tool output plausibility;
- resource coexistence risk;
- runtime support maturity;
- likely role in a planner-routed registry.

Explicitly compare:

1. what ~7–8B appears to gain over ~3–4B;
2. what ~12–14B appears to gain over the strongest ~7–8B candidate;
3. whether those gains are likely relevant to APEX's bounded executor role rather than generic intelligence.

Do not claim benchmark certification from public benchmarks.

## Required deliverables

Produce one coherent research packet containing:

1. executive finding;
2. evidence date and freshness map;
3. **primary ~7–8B shortlist** with exact versions;
4. ~3–4B efficiency controls;
5. ~12–14B challengers where practical;
6. any justified >14B stretch case and why it is actually runnable;
7. coding challengers;
8. excluded/deprioritized candidates and why;
9. capability-by-task-class matrix;
10. context/tool/structured-output evidence;
11. runtime/artifact availability map;
12. size-vs-resource-vs-execution hypothesis matrix;
13. benchmark priority order;
14. major unknowns that only local APEX testing can settle;
15. source appendix dominated by current primary sources;
16. YAML:

```yaml
local_model_landscape:
  evidence_date: null
  primary_7_8b_candidates: []
  efficient_3_4b_controls: []
  larger_12_14b_challengers: []
  over_14b_stretch_candidates: []
  coding_challengers: []
  benchmark_priority: []
  excluded_or_deprioritized: []
  context_findings: {}
  structured_tool_findings: {}
  windows_runtime_findings: {}
  size_tradeoff_hypotheses: {}
  resource_unknowns: []
  apex_benchmark_unknowns: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- No production selection.
- **Do not treat 7–8B as already proven; treat it as the operator's primary hypothesis.**
- Do not silently replace that hypothesis with a largest-model or maximum-reasoning objective.
- Do not confuse public benchmark strength with APEX execution reliability.
- Do not infer dedicated VRAM from integrated-GPU memory reporting.
- Separate measured, documented, inferred and unknown claims.
- Prefer current primary sources.

## Success condition

The run succeeds when the benchmark team has a **7–8B-centered, evidence-backed candidate set** plus only the smaller/larger comparators needed to decide whether that practical-optimum hypothesis holds on the actual APEX workloads and hardware.
