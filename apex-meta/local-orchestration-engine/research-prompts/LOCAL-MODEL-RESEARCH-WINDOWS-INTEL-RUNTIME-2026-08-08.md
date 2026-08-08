---
title: "Local Model Research Prompt — Windows / Intel Runtime"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-08
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
---

# Research Prompt D — Windows / Intel Runtime

## Target

Research and produce a **runtime decision packet for local APEX model execution on the operator's Windows laptop**.

The runtime research should primarily establish the best ways to serve the operator's expected **~7–8B practical-center models**, while also showing what is required to test a smaller control and credible ~12–14B challengers. Do not bias the runtime design toward the largest model that can technically load.

Do not select a production runtime without local bake-off evidence.

## Machine profile

```text
HP OmniBook X Flip 16-as0xxx
Windows 11
Intel Core Ultra 7 258V
~31.6 GB system RAM
Intel Arc 140V integrated graphics
```

Geekbench is hardware context only. Do not infer LLM throughput, dedicated VRAM or usable context capacity from it.

## Authority and runtime contract

Round-3 LM-23..LM-30 define the requirements:

- ~32K reliably usable working context target; 64K stretch where practical;
- schema-constrained output plus external validators/guards;
- reliability-first but latency measured;
- browser/IDE/test/CLI coexistence is mandatory;
- execution planner routes only to benchmark-certified profiles;
- ~7–8B is the primary model-size hypothesis, not an unchangeable production lock;
- model topology remains open;
- runtime must support controlled load/unload/switching and reproducible configuration;
- run/orchestration state must live outside inference runtime.

## Candidate runtime space

Research current realistic options rather than assuming these examples remain best:

- OpenVINO / OpenVINO GenAI / OpenVINO Model Server paths;
- llama.cpp-family Windows backends including Intel-relevant acceleration;
- Ollama where useful as model-lifecycle/API layer;
- other currently credible Windows/Intel local-serving stacks.

Verify current support before including a stack.

## Questions to resolve

For each serious runtime/configuration determine:

- Windows 11 support quality;
- Intel Core Ultra / Arc 140V support;
- CPU, GPU and NPU support where current and practical;
- model/artifact formats supported;
- quantization/representation support;
- context control and memory behavior;
- structured output / grammar / JSON-schema mechanisms;
- local API compatibility and stability;
- tool-call mediation implications;
- model load, unload, switch and memory release behavior;
- simultaneous model residency where possible;
- crash/restart behavior;
- health/readiness interfaces;
- logging and performance metrics;
- ease of pinning exact runtime/model/config versions;
- integration with external scheduler/checkpoint system;
- current limitations/issues relevant to this hardware.

## Size-class/runtime comparison

The bake-off design must answer:

```text
~3–4B control:
  How cheap/fast can it be, and what capability is lost?

~7–8B primary:
  Can it run comfortably with browsers, IDE, tests and expected context?
  Which backend/representation gives the best reliability/resource balance?

~12–14B challenger:
  Can it run stably enough to be a meaningful comparator?
  What load/swap/coexistence penalty does it impose?

>14B:
  Include only if concrete current evidence makes local testing realistic and decision-relevant.
```

## Resource/coexistence research

Design local tests for:

- model-only baseline;
- model + browser workload;
- model + multiple subscription sessions;
- model + IDE/terminals;
- model + repo test workload;
- model + occasional CLI-agent process where practical;
- load/unload and model-switch cost;
- memory actually released after unload;
- responsiveness under pressure;
- CPU/GPU/NPU utilization;
- context growth impact.

## NPU/GPU/CPU stance

Treat device choice empirically. Do not prefer NPU for theoretical efficiency or GPU for generic speed.

Compare supported paths on:

- throughput;
- latency;
- usable context;
- memory footprint;
- coexistence;
- stability;
- model coverage.

## Deliverables

1. executive finding;
2. evidence date + exact runtime versions;
3. Windows/Intel compatibility matrix;
4. CPU/GPU/NPU backend comparison;
5. model-format/quantization compatibility;
6. structured-output/API/observability comparison;
7. load/unload/hot-swap capability comparison;
8. context/memory behavior evidence;
9. **~7–8B primary runtime configurations to test first**;
10. smaller-control and larger-challenger runtime configurations where useful;
11. coexistence bake-off plan;
12. rejected/deprioritized runtime paths;
13. unresolved unknowns;
14. source appendix dominated by current official documentation/issues;
15. YAML:

```yaml
windows_intel_runtime_research:
  evidence_date: null
  runtimes: []
  versions: {}
  windows_support: {}
  intel_gpu_support: {}
  intel_npu_support: {}
  cpu_support: {}
  model_format_support: {}
  structured_output_support: {}
  api_and_observability: {}
  load_unload_swap: {}
  context_memory_findings: {}
  primary_7_8b_bakeoff_configs: []
  smaller_control_configs: []
  larger_challenger_configs: []
  coexistence_tests_required: []
  rejected_or_deprioritized: []
  unresolved_unknowns: []
  overall_confidence_0_to_100: null
```

## Boundaries

- No production runtime selection from documentation alone.
- Do not infer dedicated VRAM on the integrated Arc GPU.
- Do not let runtime convenience dictate APEX authority architecture.
- Keep orchestration state external to model-serving process.
- Do not optimize the runtime around maximum model size; optimize around the APEX comparison plan centered on ~7–8B.
- Separate official support from anecdotal compatibility.
- Prefer current primary sources.

## Success condition

The run succeeds when APEX has current, reproducible Windows/Intel runtime configurations ready to test the **~7–8B practical-optimum hypothesis** against only the smaller/larger comparators needed to make a sound decision.
