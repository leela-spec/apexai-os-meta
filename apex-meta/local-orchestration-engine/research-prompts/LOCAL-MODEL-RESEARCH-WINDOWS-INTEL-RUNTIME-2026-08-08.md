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

The deliverable must identify current realistic inference runtimes/configurations that can support planner-routed high-reasoning local models with controlled load/unload, stable APIs, structured outputs, observability, reproducibility and real coexistence with browsers/development tools.

Do not select production runtime without local bake-off evidence.

## Machine profile to ground the research

```text
HP OmniBook X Flip 16-as0xxx
Windows 11
Intel Core Ultra 7 258V
~31.6 GB system RAM
Intel Arc 140V integrated graphics
```

Geekbench evidence is hardware context only. Do not infer LLM throughput, dedicated VRAM or practical context capacity from it.

## Authority and runtime contract

Round-3 LM-23..LM-30 define the requirements:

- ~32K reliably usable working context target; 64K stretch where practical;
- schema-constrained output plus external validators/guards;
- reliability-first but latency measured;
- browser/IDE/test/CLI coexistence is mandatory;
- execution planner routes only to benchmark-certified profiles;
- model topology remains open;
- runtime must support controlled load/unload/switching and reproducible configuration;
- run/orchestration state must live outside the inference runtime.

## Candidate runtime space

Research current realistic options rather than assuming these exact examples remain best:

- OpenVINO / OpenVINO GenAI / OpenVINO Model Server paths;
- llama.cpp-family Windows backends including Intel-relevant acceleration;
- Ollama where useful as a model lifecycle/API layer;
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
- integration with an external scheduler/checkpoint system;
- current limitations/issues relevant to this exact hardware.

## Resource/coexistence research

The runtime must be evaluated for the real APEX environment, not isolated tokens/sec.

Design the local bake-off to capture:

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

Treat device choice as empirical. Do not prefer NPU merely because it is power-efficient in theory, and do not prefer GPU merely because it is faster in generic benchmarks.

Compare current supported paths and define the smallest tests that settle:

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
9. coexistence bake-off plan;
10. recommended first runtime configurations to test locally;
11. rejected/deprioritized runtime paths;
12. unresolved unknowns;
13. source appendix dominated by official current documentation/issues;
14. YAML:

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
  coexistence_tests_required: []
  recommended_bakeoff_configs: []
  rejected_or_deprioritized: []
  unresolved_unknowns: []
  overall_confidence_0_to_100: null
```

## Boundaries

- No production runtime selection from documentation alone.
- Do not infer dedicated VRAM on the integrated Arc GPU.
- Do not let runtime convenience dictate APEX authority architecture.
- Keep orchestration state external to model-serving process.
- Separate official support from anecdotal compatibility.
- Prefer current primary sources.

## Success condition

The run succeeds when APEX has a small set of **current, reproducible Windows/Intel runtime configurations** ready for local model+runtime+harness bake-off, with all material coexistence and switching questions converted into measurable tests.
