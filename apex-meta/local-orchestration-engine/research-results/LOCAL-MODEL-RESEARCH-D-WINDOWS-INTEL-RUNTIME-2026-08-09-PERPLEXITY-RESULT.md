---
title: "Local Model Research Result — Windows / Intel Runtime — Perplexity"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-WINDOWS-INTEL-RUNTIME-2026-08-08.md
prompt_id: D
agent: perplexity
agent_model_label: "Beste (Best/auto-select) — deliberately not hand-picked, to avoid biasing toward a Claude-family model"
agent_mode: "Suche (standard Search), not Vertiefte Recherche (Deep Research)"
account_tier: "subscription (plan tier not disclosed by UI)"
run_id: R1
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: null
bundle_sha256: "daa41a73f2b5a81a7de6004e8874f7a08bd568b7e5c3a683a885a97e87f67fc6"
retries: 0
interruptions: []
uncontrolled_variables:
  - "Chat URL for this specific run was not captured at execution time (browser extension disconnected before it could be recorded retroactively); response content and structure were verified via in-page marker/length checks before extraction."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Windows / Intel Runtime — Perplexity

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Perplexity executing Research Prompt D (Windows / Intel Runtime) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

# APEX OS — Local Model Research Packet: Windows / Intel Runtime (Research Prompt D)

**Evidence date:** 2026-08-09
**Document type:** Runtime decision packet (research-only; no production lock)

## 1. Executive finding

On the operator's HP OmniBook X Flip / Core Ultra 7 258V / ~31.6 GB RAM / Arc 140V / Windows 11, the current primary-source evidence supports three credible local-serving paths for ~7–8B models: llama.cpp (SYCL/Vulkan backends), OpenVINO GenAI (CPU/GPU/NPU), and Ollama (as model-lifecycle/API layer, typically backed by llama.cpp).

The ~7–8B practical-optimum hypothesis is testable immediately with Q4_K_M / Q5_K_M GGUF in llama.cpp or INT4/INT8 IR in OpenVINO GenAI, using ~32K working context and schema-constrained output. A ~3–4B efficiency control (e.g., Gemma 4 E2B/E4B) is already demonstrated on identical hardware via OpenVINO NPU/GPU at practical speeds, and a ~12–14B challenger is plausible only under careful quantization and context discipline (Q4_K_S or lower, context ≤16–24K).

No single runtime is selected here; instead, the packet defines concrete bake-off configurations and coexistence tests that can falsify or support the 7–8B prior under real laptop conditions.

## 2. Evidence date + exact runtime versions

All versions below are taken from current official documentation or release notes as of 2026-08-09:

- OpenVINO Toolkit: 2026.1 (quarterly release; preview llama.cpp backend)
- OpenVINO GenAI: 2026.1.0 (structured output, NPU/GPU/CPU)
- Intel NPU Driver (Windows): 32.0.100.4841 (supports OpenVINO 2026.2.1; Core Ultra 7 258V explicitly listed)
- llama.cpp: latest stable release series (b9xxx in 2026; Windows x64 builds with Vulkan, SYCL, and OpenVINO backends available)
- Ollama: v0.32.x (July 2026 notes; Windows support; keep_alive control, /api/ps, /api/generate, /api/chat, structured format)

MEASURED/DOCUMENTED: Version strings and support claims are sourced from official release notes, driver pages, and API docs. Any performance numbers tied to specific hardware are marked separately.

## 3. Windows / Intel compatibility matrix

| Runtime / Stack | Windows 11 support | Core Ultra 7 258V (Lunar Lake) | Arc 140V iGPU | Intel NPU (AI Boost) |
|---|---|---|---|---|
| OpenVINO 2026.1 + GenAI | Explicitly supported (22H2+) | Listed in NPU driver and GenAI articles | Supported (GPU device) | Supported with NPU driver 32.0.100.4xxx |
| llama.cpp (SYCL backend) | Supported via oneAPI/Level Zero on Windows 11 | SYCL targets Intel GPUs; CPU always available | Verified for Arc GPUs; examples include Arc 140V class | NPU not a primary SYCL target; NPU path via OpenVINO backend |
| llama.cpp (Vulkan backend) | Windows x64 Vulkan binaries provided | Works on integrated GPUs including Arc 140V | Explicitly used for Arc A770/B580 and iGPUs | No NPU; Vulkan is GPU-only |
| llama.cpp (OpenVINO backend) | Preview in OpenVINO 2026.1; Windows supported via OpenVINO toolkit | Documented for Core Ultra series | CPU/GPU via OpenVINO devices | NPU via OpenVINO NPU plugin |
| Ollama (Windows) | Official Windows builds; server on 11434 | Runs on standard Windows laptops; no special CPU requirement | Uses underlying backend (typically llama.cpp); GPU acceleration depends on build | No direct NPU abstraction; NPU effects only via backend |

DOCUMENTED: All cells reflect explicit OS/CPU/GPU/NPU statements in official docs or release notes. Anecdotal performance is not used to fill this matrix.

## 4. CPU / GPU / NPU backend comparison

### 4.1 Throughput & latency (evidence-backed)

OpenVINO GenAI on NPU (Core Ultra 7 258V, Arc 140V):

- Gemma 4 E2B INT4: ~18 tok/s on NPU; E4B INT4: ~16.8 tok/s on NPU.
- Same hardware, GPU (Arc 140V) reported ~36 tok/s (E2B) and ~18.5 tok/s (E4B), i.e., GPU faster for these small models in that test.
- Another report on similar Lunar Lake hardware found NPU at 93% utilization but slower than CPU+GPU for some workloads, underscoring the need for empirical comparison.

llama.cpp SYCL/Vulkan on Arc-class GPUs:

- Community benchmarks for Qwen3-8B Q4_K_M on Arc GPUs show ~17–53 tok/s decode depending on backend and card (SYCL vs Vulkan, different Arc models).
- SYCL backend explicitly supports all Intel GPUs, with Windows examples using Arc hardware.

CPU-only:

- Viable for small models and low concurrency, but context growth and multi-session load quickly pressure CPU and RAM.
- OpenVINO-backed llama.cpp on NPU reported ~21 tok/s for Llama 3.1 8B Q4_K_M vs ~4 tok/s CPU-only in one configuration, highlighting potential NPU gains when the stack is correctly wired.

INFERRED: For ~7–8B on this laptop, GPU (Arc 140V) and NPU are both credible; which wins depends on model, quantization, context length, and backend tuning. NPU may excel in power/thermals but not always raw tok/s.

### 4.2 Usable context & memory footprint

- System RAM: ~31.6 GB shared; Arc 140V uses system memory, not dedicated VRAM.
- Integrated GPU memory reporting: On Windows, integrated devices can report up to ~94% of system RAM minus internal reserves, but this is not guaranteed usable for LLM KV cache plus browser/IDE load.
- Context targets from APEX: ~32K working context; 64K stretch.

Practical implication:

- ~7–8B Q4_K_M (~4.7 GB file) plus KV cache for 32K can fit comfortably in RAM if the runtime releases unused memory and coexistence is managed.
- ~12–14B Q4 (~8–10 GB) leaves less headroom for browser/IDE/tests; context may need capping at 16–24K for stable coexistence.

DOCUMENTED/INFERRED: File sizes and quantization classes are from model cards and community GGUF pages; memory behavior is inferred from driver docs and benchmark reports, not assumed from Geekbench.

### 4.3 Stability & coexistence

- Coexistence fixtures in the APEX benchmark portfolio explicitly require browser, IDE, tests, and occasional CLI agents to remain viable.
- OpenVINO GenAI exposes logging, structured output, and device selection, enabling controlled experiments across CPU/GPU/NPU.
- llama.cpp server offers /health and /v1/health readiness endpoints and can be run as a local service for scheduler integration.
- Ollama provides /api/ps to inspect loaded models and memory, plus keep_alive and ollama stop to unload on demand.

DOCUMENTED: These capabilities are described in official API docs and release notes.

## 5. Model format & quantization compatibility

| Runtime | Primary model format | Quantization support | Notes |
|---|---|---|---|
| OpenVINO GenAI | OpenVINO IR (XML/FP16/INT8/INT4), some GGUF via backend | INT4, INT8, FP16; NNCF compression available | Best evidence for NPU execution; models often need conversion to IR. |
| llama.cpp | GGUF (native) | Q4_0, Q4_K_M, Q5_K_M, Q6_K, Q8_0, IQ variants, etc. | Mature GGUF ecosystem; easy to test many 7–8B models. |
| Ollama | Internal model bundles (often GGUF-based) | Quantizations handled upstream; users pull tagged variants (e.g., q4_k_m) | Simplifies lifecycle; backend details depend on Ollama build. |

DOCUMENTED: Format and quantization details come from model repos, runtime docs, and integration guides.

## 6. Structured output / API / observability comparison

### 6.1 Structured output

- **OpenVINO GenAI:** StructuredOutputConfig with JSON Schema; uses XGrammar-style constrained decoding to guarantee valid JSON. Direct Pydantic → JSON Schema workflow documented.
- **llama.cpp:** Supports JSON Schema via --json-schema / -j in server/CLI, compiling schemas to GBNF grammars. Also supports raw GBNF grammars for tighter control.
- **Ollama:** format parameter accepts a JSON schema object for constrained decoding. Also supports function calling via tools array with local models (as of 2026).

DOCUMENTED: All three runtimes explicitly support schema-constrained generation in their current docs.

### 6.2 API compatibility & stability

- **OpenVINO GenAI:** Python API (openvino_genai), plus OpenVINO Model Server (OVMS) with OpenAI-compatible and health endpoints. Server readiness endpoint /v2/health/ready fixed in 2026.1 to report correct ready state.
- **llama.cpp server:** Built-in HTTP server with OpenAI-compatible /v1/chat/completions, /v1/completions, and /health. Grammar/JSON schema options available in server mode.
- **Ollama:** Native REST API (/api/generate, /api/chat, /api/ps, etc.) and OpenAI-compatible /v1/* endpoints. Function calling and structured outputs supported as of mid-2026.

DOCUMENTED: API capabilities are drawn from official API references and integration guides.

### 6.3 Observability & metrics

- **OpenVINO:** Configurable log levels via OPENVINO_LOG_LEVEL (ERR/WARN/INFO/DEBUG/TRACE). Server logs report KV cache allocation vs usage and other metrics.
- **llama.cpp:** Server logs token timings, prompt vs generation stats; health endpoints for monitoring. Bench tools (llama-bench) for systematic performance measurement.
- **Ollama:** /api/ps shows loaded models, memory usage, and expiry times. Generation responses include timing and token stats.

DOCUMENTED: Observability features are described in runtime docs and API references.

## 7. Load / unload / hot-swap capability comparison

| Runtime | Load model | Unload model | Hot-swap / multi-model | Notes |
|---|---|---|---|---|
| OpenVINO GenAI / OVMS | Load via API/config; models initialized before ready | Model can be unloaded via server control; readiness endpoint reflects state | Multiple models possible via server config; switching requires explicit load/unload | Orchestration state must live outside inference process per APEX law. |
| llama.cpp server | Loads model at startup or on first request (depending on args) | Typically one active model per server instance; swap requires restart or multiple instances | Multi-model via multiple server processes or orchestration layer | Suitable for APEX if scheduler manages processes and checkpoints externally. |
| Ollama | Auto-loads on request; can preload with empty prompt | keep_alive=0 or ollama stop <model> unloads immediately | Switching models unloads previous after timeout or immediate via keep_alive=0 | /api/ps exposes memory and expiry for scheduler integration. |

DOCUMENTED: Load/unload behaviors are specified in API docs and FAQs.

## 8. Context / memory behavior evidence

- Context targets: APEX specifies ~32K reliably usable working context, 64K stretch.
- GGUF models: Qwen3-8B-GGUF examples show commands with 32K context (-c 40960, --no-context-shift).
- OpenVINO GenAI: Articles demonstrate running Gemma 4 on Core Ultra 7 258V with practical speeds at meaningful context lengths, though exact token counts vary by experiment.
- Memory sharing: Arc 140V uses system RAM; driver docs indicate integrated GPUs can access up to ~94% of system memory minus reserves on Windows, but this is not a guarantee for LLM workloads under coexistence.

DOCUMENTED/INFERRED: Context capabilities are evidenced by example commands and benchmark reports; exact usable context under coexistence must be measured in APEX fixtures.

## 9. ~7–8B primary runtime configurations to test first

These are candidate bake-off configurations for the ~7–8B practical-center class, aligned with APEX requirements (schema output, ~32K context, coexistence):

### 9.1 llama.cpp (SYCL or Vulkan) — GGUF Q4_K_M

- Model: Qwen3-8B-Instruct-GGUF:Q4_K_M or Llama-3.1-8B-Instruct-GGUF:Q4_K_M
- Runtime: llama.cpp server (Windows x64, SYCL or Vulkan build)
- Backend flags (examples): SYCL: --n-gpu-layers 99 (or tuned), --ctx-size 32768, --temp 0.6, --top-p 0.95; Vulkan: similar, with Vulkan binary
- Structured output: --json-schema or --grammar-file for APEX tool/response schemas
- Health: /health or /v1/health for readiness checks
- Rationale: Mature GGUF support, explicit Intel GPU acceleration, easy to test multiple 7–8B models.

### 9.2 OpenVINO GenAI — INT4/INT8 IR on GPU/NPU

- Model: 7–8B instruct model converted to OpenVINO IR (INT4 or INT8 via NNCF)
- Runtime: OpenVINO GenAI 2026.1 + Python API or OVMS
- Device: Test GPU (Arc 140V) and NPU separately; compare tok/s, latency, and coexistence
- Context: Target 32K if memory permits; otherwise measure degradation at 16K/24K
- Structured output: StructuredOutputConfig(json_schema=...) for APEX schemas
- Rationale: Best-documented path to NPU execution on Core Ultra 7 258V; strong evidence for small models, needs extension to 7–8B.

### 9.3 Ollama (llama.cpp backend) — Q4_K_M 8B

- Model: qwen3:8b-q4_k_m or equivalent 8B instruct tag
- Runtime: Ollama v0.32.x on Windows
- Config: Use format with JSON schema for APEX tool responses; control residency with keep_alive (0 for immediate unload after job, or short TTL)
- Observability: /api/ps for memory, /api/generate / /api/chat for execution
- Rationale: Simplifies model lifecycle and API; good for scheduler integration if backend performance is acceptable.

DOCUMENTED/INFERRED: These configs combine official capabilities with model availability; performance numbers must be filled by APEX benchmark runs.

## 10. Smaller-control and larger-challenger runtime configurations

### 10.1 ~3–4B efficiency control

Candidate models:
- Gemma 4 E2B / E4B (already benchmarked on Core Ultra 7 258V via OpenVINO NPU/GPU)
- Qwen2.5-3B-Instruct-GGUF:Q4_K_M or similar 3B class

Runtimes:
- OpenVINO GenAI (NPU/GPU) for Gemma 4 INT4
- llama.cpp GGUF Q4_K_M for 3B models

Goal: Establish minimal resource cost and capability floor; compare CLI escalations and human interventions per 100 jobs against 7–8B.

### 10.2 ~12–14B challenger

Candidate models:
- Qwen3-14B-GGUF:Q4_K_S or similar 12–14B instruct in aggressive quantization
- Any 12–14B model with confirmed GGUF and community usage on Windows

Runtimes:
- llama.cpp SYCL/Vulkan with reduced context (16–24K) to preserve coexistence
- OpenVINO IR INT4 if conversion and memory behavior are acceptable

Goal: Test whether quality gains justify higher RAM pressure, longer load times, and worse coexistence under APEX fixtures.

### 10.3 >14B

Include only if a concrete configuration (model + quantization + runtime + context) appears locally plausible and decision-relevant (e.g., a specific 20B Q3/Q4 that still leaves enough RAM for browser/IDE/tests). Otherwise, treat as out of scope for this bake-off.

INFERRED/DOCUMENTED: Model classes and quantizations are from model cards and benchmark aggregators; inclusion criteria follow APEX guidance.

## 11. Coexistence bake-off plan

Aligned with LOCAL-MODEL-BENCHMARK-PORTFOLIO coexistence fixtures (COEX-01..COEX-06) and LM-26 (laptop coexistence hard requirement):

### 11.1 Fixture set

For each primary runtime/config (9.1–9.3) and size class (~3–4B, ~7–8B, ~12–14B where plausible):

- COEX-01: Model only (baseline throughput, latency, RAM).
- COEX-02: Model + normal browser workload (multiple tabs, media).
- COEX-03: Model + three subscription sessions (simulated Weekly Orchestrator workload).
- COEX-04: Model + browsers + IDE/terminals (VS Code, terminals, tests).
- COEX-05: Model + browser + repo test workload (running test suites in background).
- COEX-06: Model + browser + occasional CLI-agent process (e.g., Claude Code/Codex-like agent) where practical.

### 11.2 Measured metrics

Per fixture, record:

- Elapsed time per job; time to first token/action.
- Peak RAM (MB) and memory release after unload.
- CPU/GPU/NPU utilization (via task manager or runtime metrics).
- Context growth impact: run selected fixtures at ~8K, 16K, 32K, and (if supported) 64K.
- Responsiveness under pressure: subjective + objective (input lag, browser/IDE stutter).
- Load/unload and model-switch cost: time and memory delta.
- CLI escalations per 100 jobs and human interventions per 100 jobs.

DOCUMENTED: Metrics mirror the benchmark portfolio's scoring dimensions and resource economics section.

## 12. Rejected / deprioritized runtime paths

Based on current evidence and APEX constraints:

- **NPU-only strategies without GPU/CPU fallback:** NPU shows promise but is not universally faster; some workloads report NPU slower than CPU+GPU despite high utilization. APEX requires reliability-first, so NPU should be tested, not assumed.
- **Runtimes without Windows 11 or Core Ultra validation:** Any stack lacking explicit Windows 11 support or Intel GPU/NPU driver alignment is deprioritized pending verification.
- **Configurations that require dedicated VRAM assumptions:** Arc 140V uses shared system RAM; designs assuming dedicated VRAM are invalid for this machine.
- **Maximum-model-size optimization:** Optimizing for the largest model that can technically load contradicts the 7–8B-centered hypothesis and coexistence requirement.

INFERRED: These rejections follow from APEX laws and observed hardware/runtime behavior.

## 13. Unresolved unknowns

Explicitly marked to avoid overclaiming:

- Exact tok/s and latency for specific 7–8B models on this exact laptop (HP OmniBook X Flip / Core Ultra 7 258V / Arc 140V) under 32K context and coexistence load.
- Memory release behavior after unload for each runtime under sustained multi-session load (does RAM fully return to OS, or are there leaks/fragmentation issues)?
- NPU compiler/model coverage for all candidate 7–8B models in OpenVINO IR INT4/INT8 (some models may not compile or run stably on NPU yet).
- Long-term stability of OpenVINO 2026.1 llama.cpp backend on Windows with frequent load/unload cycles and context shifts.
- Function calling reliability for smaller models (~3–4B) under APEX tool schemas (some may fail to produce valid tool-call JSON consistently).

UNKNOWN: These items require APEX benchmark runs and local measurement; no authoritative numbers are asserted here.

## 14. Source appendix (official documentation & primary sources)

Key primary sources used (non-exhaustive):

- OpenVINO 2026.1 release & llama.cpp backend: Intel announcement and AI/TLDR summary.
- OpenVINO system requirements & NPU support: OpenVINO docs (Windows 11, NPU plugin, devices).
- OpenVINO GenAI structured output & logging: StructuredOutputConfig docs, debug logging guide, Medium article.
- Intel NPU driver for Windows (Core Ultra 7 258V): Intel download pages listing supported CPUs and OpenVINO versions.
- llama.cpp SYCL backend on Intel GPUs: Intel article "Run LLMs on Intel GPUs Using llama.cpp".
- llama.cpp backends & Windows binaries: llama.cpp SYCL.md, release notes, backend summaries (Vulkan, SYCL, HIP).
- llama.cpp server health & JSON schema: Health endpoint guide, server/CLI docs for JSON schema and grammars.
- Ollama API, structured output, model management: Ollama docs (structured outputs, generate/chat API, FAQ on unload, API reference).
- Gemma 4 on Intel NPU/GPU (Core Ultra 7 258V): Zenn articles with explicit hardware and performance numbers.
- NPU vs CPU/GPU performance observation: Note article on X1 Carbon (Core Ultra 7 258V) showing NPU at 93% but slower than CPU+GPU in some cases.
- GGUF model examples (Qwen3-8B, 3B, etc.): Hugging Face model pages and quantization guides.
- llama.cpp benchmarks across hardware: MyAIHardware benchmark index and community runs.

DOCUMENTED: All links point to official docs, release notes, driver pages, or primary model repositories; secondary aggregators are only used where they reproduce official data or clearly label benchmarks.

## 15. YAML block

```yaml
windows_intel_runtime_research:
  evidence_date: "2026-08-09"
  runtimes:
    - "OpenVINO 2026.1 + GenAI (CPU/GPU/NPU)"
    - "llama.cpp (SYCL backend, Windows x64)"
    - "llama.cpp (Vulkan backend, Windows x64)"
    - "llama.cpp (OpenVINO backend, preview in 2026.1)"
    - "Ollama v0.32.x (Windows; llama.cpp-based backend)"
  versions:
    openvino_toolkit: "2026.1"
    openvino_genai: "2026.1.0"
    intel_npu_driver_windows: "32.0.100.4841"
    llama_cpp_release_series: "b9xxx (2026)"
    ollama: "0.32.x (July 2026)"
  windows_support:
    openvino_genai: "Windows 11 64-bit (22H2+)"
    llama_cpp_sycl: "Windows 11 (via oneAPI/Level Zero)"
    llama_cpp_vulkan: "Windows x64 Vulkan binaries"
    ollama: "Windows 10/11 official builds"
  intel_gpu_support:
    openvino_genai: "Arc 140V and other Intel GPUs supported as GPU device"
    llama_cpp_sycl: "All Intel GPUs supported (SYCL/Level Zero)"
    llama_cpp_vulkan: "Arc and integrated GPUs supported via Vulkan"
    ollama: "Depends on underlying backend; typically llama.cpp GPU builds"
  intel_npu_support:
    openvino_genai: "NPU 3720 on Core Ultra series; driver 32.0.100.4xxx required"
    llama_cpp_sycl: "NPU not a primary SYCL target; NPU via OpenVINO backend"
    llama_cpp_vulkan: "No NPU support (GPU-only)"
    ollama: "No direct NPU abstraction; NPU effects only via backend"
  cpu_support:
    openvino_genai: "All Intel CPUs; Core Ultra 7 258V explicitly in examples"
    llama_cpp_sycl: "CPU always available; SYCL optional"
    llama_cpp_vulkan: "CPU fallback available"
    ollama: "Standard x64 CPU support"
  model_format_support:
    openvino_genai: "OpenVINO IR (FP16/INT8/INT4); some GGUF via backend"
    llama_cpp_sycl: "GGUF native"
    llama_cpp_vulkan: "GGUF native"
    ollama: "Internal bundles (often GGUF-based)"
  structured_output_support:
    openvino_genai: "StructuredOutputConfig with JSON Schema (XGrammar-style)"
    llama_cpp_sycl: "JSON Schema -> GBNF; --json-schema / --grammar"
    llama_cpp_vulkan: "Same as SYCL for JSON schema/grammars"
    ollama: "format parameter with JSON schema; function calling via tools"
  api_and_observability:
    openvino_genai: "Python API; OVMS with OpenAI-compatible endpoints; /v2/health/ready; logs incl. KV cache metrics"
    llama_cpp_sycl: "HTTP server with /health, /v1/*; token/timing stats; llama-bench"
    llama_cpp_vulkan: "Same as SYCL"
    ollama: "/api/generate, /api/chat, /api/ps, /api/delete; OpenAI-compatible /v1/*; timing stats in responses"
  load_unload_swap:
    openvino_genai: "Load via API/config; unload via server control; readiness reflects state"
    llama_cpp_sycl: "Typically one model per server; swap via restart or multiple instances"
    llama_cpp_vulkan: "Same as SYCL"
    ollama: "Auto-load on request; keep_alive=0 or 'ollama stop' to unload; model switch unloads previous"
  context_memory_findings:
    openvino_genai: "Gemma 4 E2B/E4B demonstrated on Core Ultra 7 258V (NPU/GPU); 7–8B context behavior to be measured"
    llama_cpp_sycl: "GGUF models commonly run at 32K context; memory depends on quantization and KV cache"
    llama_cpp_vulkan: "Same as SYCL"
    ollama: "Context limits set per model/config; memory tracked via /api/ps"
  primary_7_8b_bakeoff_configs:
    - runtime: "llama.cpp (SYCL or Vulkan)"
      model_family: "Qwen3-8B-Instruct or Llama-3.1-8B-Instruct"
      quantization: "Q4_K_M (GGUF)"
      context_target: 32768
      structured_output: "JSON Schema via --json-schema"
      device: "Arc 140V (GPU)"
    - runtime: "OpenVINO GenAI"
      model_family: "7–8B instruct (IR)"
      quantization: "INT4 or INT8"
      context_target: 32768
      structured_output: "StructuredOutputConfig(json_schema=...)"
      device: ["Arc 140V (GPU)", "NPU (AI Boost)"]
    - runtime: "Ollama"
      model_family: "qwen3:8b or equivalent 8B"
      quantization: "q4_k_m tag"
      context_target: 32768
      structured_output: "format: <JSON schema>"
      device: "Backend-dependent (GPU/CPU)"
  smaller_control_configs:
    - runtime: "OpenVINO GenAI"
      model_family: "Gemma 4 E2B/E4B"
      quantization: "INT4"
      context_target: 16384
      device: ["NPU", "GPU"]
    - runtime: "llama.cpp"
      model_family: "Qwen2.5-3B-Instruct or similar 3B"
      quantization: "Q4_K_M"
      context_target: 16384
      device: "GPU or CPU"
  larger_challenger_configs:
    - runtime: "llama.cpp (SYCL/Vulkan)"
      model_family: "Qwen3-14B-Instruct or similar 12–14B"
      quantization: "Q4_K_S or more aggressive"
      context_target: 16384
      device: "Arc 140V (GPU)"
      notes: "Include only if memory/coexistence remain acceptable"
  coexistence_tests_required:
    - "COEX-01: model only baseline"
    - "COEX-02: model + normal browser workload"
    - "COEX-03: model + three subscription sessions"
    - "COEX-04: model + browsers + IDE/terminals"
    - "COEX-05: model + browser + repo test workload"
    - "COEX-06: model + browser + occasional CLI-agent process"
  rejected_or_deprioritized:
    - "NPU-only strategies without GPU/CPU fallback"
    - "Runtimes lacking explicit Windows 11 / Core Ultra validation"
    - "Configurations assuming dedicated VRAM on Arc 140V"
    - "Optimizations targeting maximum model size instead of 7–8B practical optimum"
  unresolved_unknowns:
    - "Exact tok/s and latency for specific 7–8B models at 32K context on this laptop under coexistence load"
    - "Memory release behavior after unload for each runtime under multi-session load"
    - "Full NPU model coverage and stability for all candidate 7–8B models in OpenVINO IR"
    - "Long-term stability of OpenVINO 2026.1 llama.cpp backend on Windows with frequent load/unload"
    - "Function calling reliability for ~3–4B models under APEX tool schemas"
  overall_confidence_0_to_100: 70
```

**DOCUMENTED/INFERRED/UNKNOWN:**

- Runtime capabilities, versions, and support claims: DOCUMENTED from official sources.
- Performance numbers for Gemma 4 and some Arc benchmarks: DOCUMENTED for those specific setups.
- Exact behavior of 7–8B/12–14B on this machine under APEX fixtures: UNKNOWN until benchmark runs; confidence reflects maturity of runtimes, not measured APEX results.
