---
title: "Local Model Research Result — Windows / Intel Runtime — Chatgpt"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-WINDOWS-INTEL-RUNTIME-2026-08-08.md
prompt_id: D
agent: chatgpt
agent_model_label: "ChatGPT, reasoning effort: Mittel (Medium, UI default)"
agent_mode: "standard reasoning + web search (Websuche toggle manually enabled)"
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

# Local Model Research Result — Windows / Intel Runtime — Chatgpt

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Chatgpt executing Research Prompt D (Windows / Intel Runtime) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

# Windows / Intel Runtime Decision Packet — APEX Local Execution Layer (ChatGPT)

**Research target:** Windows 11 runtime configurations for the HP OmniBook X Flip 16-as0xxx / Intel Core Ultra 7 258V / ~31.6 GB system RAM / Intel Arc 140V integrated graphics.

**Evidence date:** 2026-08-09.

**Classification rule:** Every substantive research conclusion below is marked DOCUMENTED, INFERRED, MEASURED, or UNKNOWN.
MEASURED: No APEX-local runtime measurements were performed in this research pass. All performance/coexistence conclusions remain benchmark-gated.

## 1. Executive finding

DOCUMENTED — Primary runtime family: OpenVINO 2026.3.0 and OpenVINO Model Server 2026.3.0 are the strongest first-party Intel candidates for the APEX Windows bake-off. OpenVINO explicitly supports Intel CPU, GPU and NPU execution; current OpenVINO GenAI/OVMS documentation includes Windows 11 and Intel Core Ultra testing, OpenAI-compatible LLM endpoints, structured generation, model-management facilities, and Intel-specific model optimization. OpenVINO 2026.3.0 was released on 2026-08-07; OVMS 2026.3.0 was released on 2026-08-04. (OpenVINO Dokumentation, GitHub)

INFERRED — First configuration to benchmark: The highest-priority APEX configuration should therefore be OpenVINO/OVMS + Intel Arc 140V GPU + INT4 ~7–8B model, with an equivalent OpenVINO CPU configuration as a mandatory comparator. The rationale is not an assumption that GPU will win: Arc/iGPU is directly supported, while CPU provides the cleanest reliability/control baseline. Device choice must remain empirical. (OpenVINO Dokumentation)

DOCUMENTED — NPU is not presently a primary 32K APEX path: OpenVINO supports Core Ultra NPUs on Windows 11, but the current OVMS 2026.3 release documents an 8K maximum prompt limitation for LLM execution on NPU. That conflicts directly with APEX LM-23's ~32K reliable-context target. (OpenVINO Dokumentation)

INFERRED — NPU role: NPU should therefore be included only as an experimental efficiency comparator, especially for smaller models or short-context execution. It should not be considered a candidate for the default APEX ~32K profile until the documented 8K limitation is removed and locally verified.

DOCUMENTED — llama.cpp is the strongest independent control runtime: llama.cpp build b10331, released 2026-08-08, publishes Windows x64 builds for CPU, Vulkan, OpenVINO and SYCL. Its SYCL backend explicitly targets Intel Arc and integrated Intel GPUs, and its newer OpenVINO backend exposes Intel CPU/GPU/NPU acceleration while retaining GGUF compatibility. Its server supports OpenAI-style serving, grammar-constrained generation, resource fitting and sleep/unload behavior. (GitHub)

INFERRED — llama.cpp bake-off role: The most decision-relevant independent comparison is therefore llama.cpp Vulkan vs SYCL vs OpenVINO, using the same GGUF model quantization where technically possible. This isolates backend effects better than comparing unrelated runtime/model combinations.

DOCUMENTED — Ollama remains useful but should not be the Intel performance reference: Ollama v0.32.6 runs natively on Windows and provides model lifecycle management, an API, structured output, tool calling, usage timing, keep_alive, explicit unload, and configurable context. Its current Windows documentation explicitly advertises NVIDIA and AMD Radeon GPU support, while Intel GPU use is handled through the more generic Vulkan path rather than a dedicated first-party Intel execution path. (Ollama, GitHub)

INFERRED — Ollama role: Ollama should be tested as an operational lifecycle/API convenience layer, not used as the reference implementation for Arc 140V performance. If its Vulkan results approach direct llama.cpp/OpenVINO while lifecycle reliability is materially better, it may still deserve an APEX profile.

DOCUMENTED — ONNX Runtime GenAI is current but not first-line: ONNX Runtime GenAI v0.15.2 was released 2026-08-07 with Windows x64 CPU and WinML packages. Microsoft describes the GenAI API as Preview, and DirectML is now in sustained engineering with new Windows feature development moving toward WinML. (GitHub, ONNX Runtime)

INFERRED — ONNX Runtime role: ONNX Runtime GenAI/WinML is a useful secondary Windows-native control, but it should not displace OpenVINO or llama.cpp from the first bake-off round because its GenAI API is still explicitly preview-stage and APEX would gain little from adding another serving topology before its structured-output/tool/runtime behavior has been validated.

DOCUMENTED — IPEX-LLM is deprioritized: Intel's IPEX-LLM repository, although it historically supported Windows Intel iGPU/dGPU execution and Ollama integration, was archived on 2026-01-28. (GitHub)

INFERRED — Runtime shortlist:

1. OpenVINO GenAI / OVMS 2026.3.0 — first priority
2. llama.cpp b10331 — Vulkan / SYCL / OpenVINO backends
3. Ollama 0.32.6 — CPU/Vulkan lifecycle-control comparator
4. ONNX Runtime GenAI 0.15.2 / WinML — secondary Windows-native comparator
5. NPU configurations — exploratory efficiency tests only
6. IPEX-LLM — no new APEX dependency

UNKNOWN — Production winner: No production runtime can be selected from documentation. APEX requires the prescribed local fixtures, context tests, safety trajectories and coexistence measurements.

## 2. Evidence date + exact runtime versions

| Runtime/component | Verified version | Status | Evidence |
|---|---|---|---|
| OpenVINO | 2026.3.0 | DOCUMENTED — latest release located in current official repository; released 2026-08-07. | GitHub |
| OpenVINO Model Server | 2026.3.0 / tag v2026.3 | DOCUMENTED — latest OVMS release; released 2026-08-04. | GitHub |
| OpenVINO GenAI | 2026.3 generation | DOCUMENTED — release branch/package family aligned with OpenVINO 2026.3; exact independent GenAI package build should be pinned from installed artifact during bake-off. | GitHub |
| llama.cpp | b10331, commit 7ba604f | DOCUMENTED — latest release located; released 2026-08-08. | GitHub |
| Ollama | v0.32.6, commit c82ebbd | DOCUMENTED — latest release located; released 2026-08-04. | GitHub |
| ONNX Runtime GenAI | v0.15.2, commit ed5f4e8 | DOCUMENTED — latest release located; released 2026-08-07. | GitHub |
| IPEX-LLM | N/A for new adoption | DOCUMENTED — repository archived 2026-01-28. | GitHub |

INFERRED — Pinning discipline: APEX trial identities should pin the executable/package hash as well as the semantic runtime version because llama.cpp in particular releases multiple builds per day and Ollama embeds evolving llama.cpp engines.

## 3. Windows / Intel compatibility matrix

| Runtime | Windows 11 | Core Ultra 7 258V CPU | Arc 140V / Intel iGPU | Intel NPU | APEX assessment |
|---|---|---|---|---|---|
| OpenVINO GenAI | DOCUMENTED — supported | DOCUMENTED — OpenVINO targets Intel CPUs | DOCUMENTED — integrated Intel GPU execution supported | DOCUMENTED — Core Ultra NPU support on Windows | INFERRED — strongest Intel-native candidate |
| OVMS 2026.3 | DOCUMENTED — current LLM demo tested on Windows 11/Core Ultra | DOCUMENTED | DOCUMENTED — Arc GPU path supported | DOCUMENTED, but current LLM prompt limit is 8K | INFERRED — strongest serving candidate if bare-metal Windows packaging behaves reliably |
| llama.cpp CPU | DOCUMENTED — official Windows x64 binary | DOCUMENTED | N/A | N/A | INFERRED — mandatory reference baseline |
| llama.cpp Vulkan | DOCUMENTED — official Windows x64 Vulkan binary | CPU fallback possible | DOCUMENTED — Vulkan backend exists; actual 140V quality/performance must be measured | No | INFERRED — high-priority Arc comparator |
| llama.cpp SYCL | DOCUMENTED — official Windows x64 SYCL build | Yes | DOCUMENTED — SYCL backend explicitly supports Arc and Intel iGPU | No primary path | INFERRED — high-priority Intel GPU comparator |
| llama.cpp OpenVINO backend | DOCUMENTED — official Windows x64 OpenVINO build | Yes | DOCUMENTED | DOCUMENTED by backend design | INFERRED — particularly useful because GGUF is retained while backend becomes Intel-native |
| Ollama 0.32.6 | DOCUMENTED — native Windows app | DOCUMENTED — CPU execution available | DOCUMENTED — generic Vulkan support exists; Windows page does not advertise Intel GPU as first-class | UNKNOWN — no current official NPU path found | INFERRED — lifecycle/API comparator, not Intel reference |
| ORT GenAI / WinML | DOCUMENTED — Win x64 WinML artifact exists | DOCUMENTED | DOCUMENTED at Windows/EP abstraction level | DOCUMENTED at ORT/OpenVINO/WinML ecosystem level; exact GenAI+258V dispatch needs local verification | INFERRED — secondary comparator |
| IPEX-LLM | DOCUMENTED — historically supported Windows Intel GPUs | Yes | Yes | Historical paths existed | DOCUMENTED/INFERRED — archived; reject for new APEX dependency |

## 4. CPU / GPU / NPU backend comparison

### CPU

DOCUMENTED: OpenVINO, OVMS, llama.cpp, Ollama and ORT GenAI all have Windows CPU execution paths.

INFERRED: CPU must remain a first-round baseline because it eliminates uncertainty around iGPU shared-memory behavior and lets APEX distinguish model/harness failures from accelerator/backend failures.

INFERRED: CPU may also prove competitive on low-concurrency APEX tasks if GPU acceleration materially reduces browser/desktop responsiveness through shared memory bandwidth contention.

MEASURED: No 258V APEX CPU throughput, prefill latency, peak RAM or coexistence measurements yet.

### Intel Arc 140V iGPU

DOCUMENTED: OpenVINO supports inference on integrated Intel graphics; current OVMS documentation explicitly positions ARC GPUs as an optimized LLM serving target. llama.cpp provides Windows Vulkan, SYCL and OpenVINO builds, creating three independently testable Arc paths.

INFERRED: Arc 140V is the most important accelerator target because it offers the best chance of improving generation while retaining the CPU for browser, IDE and test processes.

UNKNOWN: The actual division of system memory between inference allocations, graphics use and other Windows processes on this exact laptop is not established by documentation.

UNKNOWN: Stable ~32K context for a ~7–8B INT4 model on Arc 140V under APEX coexistence workloads remains unverified.

### Intel NPU

DOCUMENTED: OpenVINO supports Intel Core Ultra NPU hardware under Windows 11.

DOCUMENTED: OVMS 2026.3 reports an 8K maximum prompt limit for LLM execution on NPU.

INFERRED: The NPU currently fails the APEX default-context requirement before performance is considered.

INFERRED: It remains worth one exploratory test at ~8K using the smaller control and possibly one ~7–8B configuration, because offloading routine low-context work might improve system coexistence.

UNKNOWN: Whether future OpenVINO/NPU releases remove this prompt restriction.

## 5. Model-format / quantization compatibility

| Runtime | Primary artifacts | Quantization / representation | Assessment |
|---|---|---|---|
| OpenVINO GenAI / OVMS | DOCUMENTED — OpenVINO IR is the primary optimized path; current GenAI can also directly load supported GGUF architectures. | DOCUMENTED — INT4 and INT8 LLM weight compression are supported; OpenVINO 2026 also includes advanced low-precision mechanisms and INT4 KV-cache work. | INFERRED — benchmark OpenVINO INT4 first; keep exact export parameters frozen. |
| llama.cpp | DOCUMENTED — GGUF required. | DOCUMENTED — native llama-quantize; Q4_K_M and numerous GGUF quantizations available. | INFERRED — Q4_K_M-class quant should be an initial control, but quantization must be model-specific and quality-tested rather than assumed optimal. |
| Ollama | DOCUMENTED — GGUF imports supported; Safetensors may be converted/imported through supported workflows. | DOCUMENTED — local quantization workflow exists. | INFERRED — use identical GGUF artifact to llama.cpp where possible to isolate lifecycle/API overhead. |
| ORT GenAI | DOCUMENTED — ONNX/ORT model packaging. | DOCUMENTED — execution-provider dependent. | INFERRED — adds artifact-conversion complexity relative to the two leading paths. |

INFERRED — representation control: Do not compare an OpenVINO INT4 model against an arbitrary low-quality GGUF quant and interpret the result as a runtime difference. Quantization fidelity is part of the unit under test.

## 6. Structured output / API / observability comparison

| Runtime | Structured output | API/tool support | Observability |
|---|---|---|---|
| OpenVINO GenAI | DOCUMENTED — JSON Schema, regex and EBNF-style grammar constraints are compiled into token masks; StructuredOutputConfig exposes JSON-schema generation. | DOCUMENTED — library API, not inherently the APEX authority layer. | DOCUMENTED — runtime performance controls/metrics exist; APEX must add its own trial tracing. |
| OVMS 2026.3 | DOCUMENTED — inherits GenAI generation capabilities; exact OpenAI endpoint exposure of every structured-output mechanism must be verified in bake-off client. | DOCUMENTED — OpenAI-compatible chat/completions and responses; tool calling supported for enabled model/parser combinations. | DOCUMENTED — REST responses include usage; v2026.3 adds verbose raw prompt/response debugging. |
| llama.cpp server | DOCUMENTED — GBNF constraints and JSON-schema-to-grammar machinery. | DOCUMENTED — OpenAI-compatible serving is available. | DOCUMENTED — server exposes substantial runtime/config information; sleep mode is documented. APEX-specific traces remain external. |
| Ollama | DOCUMENTED — JSON or explicit JSON Schema structured outputs. | DOCUMENTED — native API, partial OpenAI compatibility, tool calling. | DOCUMENTED — API reports total_duration, load_duration, token counts and eval durations. |
| ORT GenAI | UNKNOWN — no equally mature server-level JSON-schema enforcement path was established from the reviewed current primary sources. | DOCUMENTED — GenAI generation API exists; library is preview. | DOCUMENTED — runtime profiling exists at ORT level, but an APEX-ready server/health abstraction would need additional integration. |

INFERRED — APEX rule: Native structured generation should reduce malformed output retries but must not replace semantic validation, capability enforcement or authority checks. JSON-schema validity proves syntax/shape, not permitted action semantics.

## 7. Load / unload / hot-swap capability comparison

### OpenVINO / OVMS

DOCUMENTED: OVMS provides explicit model-management capabilities and multi-model configuration. Current releases support model repository management, enabling/disabling models and configurable deployment.

DOCUMENTED: OpenVINO 2026.2/2026.3 work includes model-loading and memory-management improvements, including faster GPU model loading through cached compiled blobs in recent releases.

INFERRED: OVMS is the best candidate for an APEX runtime in which the deterministic scheduler controls which certified model profile is resident.

UNKNOWN: Exact Windows memory release latency after disabling/unloading a 7–8B or 12–14B model on Arc 140V.

### llama.cpp

DOCUMENTED: llama-server supports sleep mode that unloads the model and associated memory, including KV cache, and reloads on the next task.

INFERRED: This maps well to laptop coexistence if memory release is complete and reliable.

UNKNOWN: Reload cost and whether Windows shared-GPU allocations return sufficiently promptly under Arc 140V pressure.

### Ollama

DOCUMENTED: Ollama exposes model residency control via keep_alive; ollama stop or a zero-like lifecycle setting can unload a model.

DOCUMENTED: Ollama can preload a model and returns model load duration in API telemetry.

INFERRED: Ollama has the simplest out-of-box lifecycle semantics among the candidates.

UNKNOWN: Whether its abstraction releases Intel iGPU/shared-memory resources more cleanly or less cleanly than direct llama.cpp/OVMS.

### ORT GenAI

DOCUMENTED: It is fundamentally a library/API rather than the mature local model-management server presented by OVMS or Ollama.

INFERRED: APEX would need to implement more lifecycle supervision around it, reducing its attractiveness for the first runtime bake-off.

## 8. Context / memory behavior evidence

DOCUMENTED: Increasing context length increases model memory use; Ollama explicitly documents this relationship.

DOCUMENTED: OpenVINO provides KV-cache optimization mechanisms and recent releases include memory-oriented improvements such as INT4 KV cache and model-specific long-context cache controls.

DOCUMENTED: OVMS 2026.2.1 introduced a cache_interval_multiplier specifically relevant to long-prompt memory behavior in linear-attention models, with its release notes using >20K-token prompts as the motivating case.

DOCUMENTED: llama.cpp's server exposes configuration for fitting workloads to available device memory and treats model and KV-cache memory as unloadable resources.

UNKNOWN: No primary source establishes that the operator's ~31.6 GB shared-memory laptop can run a particular ~7–8B model at APEX's ~32K target while browsers, IDE, test processes and subscription sessions remain responsive.

UNKNOWN: No acceptable inference can be made about dedicated Arc 140V VRAM; the APEX authority document correctly prohibits this.

INFERRED — likely memory hierarchy: A 7–8B INT4 configuration is materially more plausible than an equivalent 12–14B model for 32K + coexistence because model weights, KV cache and runtime allocations all compete with Windows and applications for the same finite system-memory envelope. This is a capacity inference only, not a viability result.

MEASURED: Actual peak working set, commit charge, GPU shared-memory allocation, NPU allocation, context-scaling curve and post-unload residual memory remain unmeasured.

## 9. ~7–8B primary runtime configurations to test first

The configurations below are bake-off candidates, not selections.

### P1 — OpenVINO GenAI / OVMS GPU

INFERRED — highest-priority configuration

- Runtime: OpenVINO / OVMS 2026.3.0
- Device: Intel Arc 140V iGPU / GPU
- Model class: ~7–8B
- Artifact: validated OpenVINO IR
- Weights: INT4
- Context tiers: 8K / 16K / 32K; 64K only after 32K coexistence succeeds
- API: OVMS local OpenAI-compatible REST
- Structured output: JSON-schema constrained where task requires it
- State: external APEX scheduler/checkpoint

DOCUMENTED rationale: Current OVMS documentation provides a Qwen3-8B INT4 GPU deployment example and its LLM serving path has been tested on Windows 11/Core Ultra-class hardware.

UNKNOWN: Arc 140V-specific throughput and 32K coexistence.

### P2 — OpenVINO GenAI / OVMS CPU

- Runtime: OpenVINO / OVMS 2026.3.0
- Device: CPU
- Model class: same ~7–8B as P1
- Artifact: same model family/export settings
- Weights: INT4
- Context: same tiers

INFERRED rationale: Controls whether GPU acceleration improves successful bounded jobs per wall time without damaging foreground responsiveness.

### P3 — llama.cpp Vulkan

- Runtime: llama.cpp b10331
- Backend: Vulkan
- Device: Arc 140V
- Artifact: GGUF
- Quantization: quality-controlled Q4-class starting point
- Context: 8K / 16K / 32K
- Server: llama-server

DOCUMENTED rationale: Official Windows Vulkan binary exists.

### P4 — llama.cpp SYCL

- Runtime: llama.cpp b10331
- Backend: SYCL
- Device: Intel Arc 140V
- Artifact: same GGUF as P3
- Context: same

DOCUMENTED rationale: SYCL backend explicitly supports Intel Arc, built-in GPU and iGPU hardware.

INFERRED: P3 vs P4 is a particularly valuable controlled experiment because model artifact and server semantics can remain nearly identical.

### P5 — llama.cpp OpenVINO backend

- Runtime: llama.cpp b10331
- Backend: OpenVINO
- Device: GPU first; CPU second
- Artifact: same GGUF family where supported
- Context: same

DOCUMENTED rationale: The OpenVINO llama.cpp backend is explicitly designed to accelerate GGUF workloads on Intel CPU/GPU/NPU.

INFERRED: This configuration helps separate the benefits of the OpenVINO backend from OVMS-specific serving/model-conversion differences.

### P6 — Ollama lifecycle comparator

- Runtime: Ollama 0.32.6
- Backend: CPU and Vulkan as available
- Artifact: matching GGUF
- Context: same
- Lifecycle: explicit keep_alive and stop/unload

INFERRED rationale: Retain only if operational simplicity offsets any measured Intel backend disadvantage.

## 10. Smaller-control and larger-challenger configurations

### ~3–4B efficiency control

INFERRED — required configurations:

- OpenVINO INT4 GPU.
- OpenVINO INT4 CPU.
- llama.cpp GGUF Vulkan.
- Optionally NPU at 8K if model architecture is supported.

Purpose: Determine whether ~7–8B yields enough additional semantic/tool/authority correctness to justify higher memory and wall-time cost.

DOCUMENTED: Current OpenVINO model support spans smaller LLMs across CPU/GPU/NPU, and OpenVINO 2026.3 explicitly added additional ~1–3B-class models.

### ~12–14B challenger

INFERRED — minimum useful configuration:

```
OpenVINO GPU INT4
+
llama.cpp best-performing GPU backend / comparable Q4-class GGUF
```

Run only after identifying the best ~7–8B backend.

INFERRED: This avoids wasting the full backend matrix on a model class that may immediately fail coexistence.

UNKNOWN: Whether a dense 12–14B-class model at ~32K context will maintain acceptable Windows/browser/IDE/test coexistence on 31.6 GB system RAM.

### >14B

INFERRED — no first-round candidate.

DOCUMENTED: OpenVINO can technically support substantially larger models on suitable Intel hardware, but runtime capability alone does not establish relevance to this laptop.

INFERRED: Do not include >14B unless later measurements demonstrate substantial unused coexistence margin or a sparse/MoE configuration creates a specifically decision-relevant case.

## 11. Coexistence bake-off plan

For every certified candidate configuration, freeze: runtime version, runtime binary/hash, model artifact/hash, quantization/export configuration, generation configuration, context, prompt contract, tool schema, guardrail version, Windows power mode, Intel driver versions, background workload recipe.

- **COEX-01 — model only.** MEASURED target: TTFT, prompt-eval tokens/s, generation tokens/s, full job elapsed time, process RAM, system commit, GPU shared-memory allocation, CPU/GPU/NPU utilization, load time, unload time.
- **COEX-02 — model + normal browser workload.** MEASURED target: above metrics plus browser interaction responsiveness and memory pressure.
- **COEX-03 — model + three subscription sessions.** MEASURED target: input latency, tab-switch responsiveness, browser memory pressure, inference degradation.
- **COEX-04 — model + IDE / terminals.** MEASURED target: IDE responsiveness, terminal command latency, compile/indexing contention.
- **COEX-05 — model + repo tests.** MEASURED target: test wall time delta versus no-model baseline and inference degradation during test execution.
- **COEX-06 — model + browser + occasional Codex/Claude Code process.** MEASURED target: whether either process experiences unacceptable memory pressure, swapping or crash/restart events.
- **COEX-07 — context growth.** Run the same representative fixture at 8K / 16K / 32K / 64K (only where supported and 32K passes). Record peak RAM, GPU shared memory, TTFT, generation latency, tool correctness, structured-output validity, false success, tool churn, OS responsiveness.
- **COEX-08 — unload verification.** Sequence: load model → run 32K-context fixture → measure committed/system/device memory → unload → sample resource state at fixed intervals → start browser + test workload → reload model. MEASURED pass criterion: memory must actually become available to the operating environment; an API reporting "unloaded" is insufficient.
- **COEX-09 — switch test.** 3–4B profile → unload/switch → 7–8B profile → unload/switch → 12–14B challenger → return to 7–8B. Record switch wall time, residual memory, crash/restart, warm-cache effects, first-request correctness, APEX checkpoint continuity.
- **COEX-10 — accelerator comparison.** Use identical model family and task fixture where representation permits: CPU, Arc/OpenVINO GPU, Arc/llama.cpp Vulkan, Arc/llama.cpp SYCL, Arc/llama.cpp OpenVINO, NPU only for supported ≤8K experiment.

INFERRED decision metric: Prefer successful bounded jobs per wall time subject to intervention, safety and coexistence constraints, not tokens/sec.

## 12. Rejected / deprioritized runtime paths

- **IPEX-LLM.** DOCUMENTED — deprioritized: Intel archived the project on 2026-01-28. INFERRED: Existing binaries may still function, but APEX should not build a new orchestration dependency around an archived runtime.
- **AI Playground.** DOCUMENTED: Intel AI Playground remains active and supports relevant Core Ultra hardware, but it is an end-user AI PC application rather than a clean deterministic model-serving substrate; its own repository describes beta software and notes potential component/version conflicts. INFERRED — deprioritized: useful for hardware experimentation, not appropriate as the APEX runtime contract.
- **ONNX Runtime GenAI as primary.** DOCUMENTED: GenAI Generate API remains marked Preview, while Microsoft's Windows strategy is moving from DirectML feature development toward WinML. INFERRED — deprioritized, not rejected: revisit if WinML demonstrates materially stronger Core Ultra resource scheduling, NPU access or model portability than the OpenVINO paths.
- **Ollama as Intel performance baseline.** DOCUMENTED: Ollama is a strong Windows lifecycle/API system, but the Windows support page advertises NVIDIA and AMD GPU support rather than a specific Intel GPU backend; Intel acceleration relies on the generic Vulkan ecosystem. INFERRED — deprioritized for performance reference: keep it as a usability/lifecycle comparator.
- **llama.cpp OpenCL.** DOCUMENTED: llama.cpp describes its Intel OpenCL applicability as primarily a fallback for GPUs lacking SYCL support and states that performance is not optimal. INFERRED — reject from first bake-off: Arc 140V already has more relevant Vulkan, SYCL and OpenVINO paths.
- **NPU as default runtime.** DOCUMENTED: Current OVMS LLM-on-NPU execution has an 8K prompt ceiling. INFERRED — reject from default 32K profile: keep only exploratory low-context trials.

## 13. Unresolved unknowns

- UNKNOWN — Arc 140V throughput: No verified APEX-local tokens/sec, TTFT or total-job latency exists for OpenVINO, Vulkan, SYCL or llama.cpp/OpenVINO on the operator's machine.
- UNKNOWN — 32K viability: It is not yet established which ~7–8B INT4 configurations can sustain ~32K while Windows, browser sessions, IDE and tests remain usable.
- UNKNOWN — 64K stretch: No evidence currently justifies treating 64K as practically usable rather than merely technically configurable.
- UNKNOWN — shared-memory pressure: Exact Arc 140V shared-memory allocation behavior under concurrent Windows workloads is unmeasured.
- UNKNOWN — unload completeness: Whether OVMS, llama.cpp and Ollama return model/KV/device allocations rapidly enough for APEX model switching must be measured.
- UNKNOWN — NPU roadmap: The date/version at which the current OVMS 8K LLM prompt restriction will be eliminated is not verified.
- UNKNOWN — structured-output equivalence: OpenVINO GenAI has explicit schema/grammar enforcement, but exact feature parity through every OVMS OpenAI endpoint/request combination should be exercised rather than assumed.
- UNKNOWN — backend reliability: Vulkan, SYCL and llama.cpp's OpenVINO backend all require repeated APEX trajectory testing on Arc 140V; generic backend availability is not evidence of equal correctness/stability.
- UNKNOWN — model conversion effects: OpenVINO IR INT4 versus GGUF Q4-class quality differences must be controlled before attributing semantic correctness differences to runtimes.
- UNKNOWN — larger challenger envelope: No 12–14B configuration is yet proven meaningful on this 31.6 GB coexistence-constrained system.
- UNKNOWN — driver sensitivity: Exact Intel graphics/NPU driver versions on the target laptop were not provided and must become part of every trial configuration identity.
- UNKNOWN — simultaneous residency: The resource economics of keeping a smaller control and a 7–8B model simultaneously resident are not known.
- UNKNOWN — crash semantics: Recovery behavior after forced runtime termination, GPU device loss, Windows sleep/resume or a browser/runtime crash requires explicit fault injection.
- UNKNOWN — APEX semantic reliability: None of the runtime documentation establishes capability on CODE/WEEKLY/MA/INJECT fixtures. Runtime support is not model certification.

## 14. Source appendix

### Primary Intel / OpenVINO evidence

- DOCUMENTED: OpenVINO 2026.3.0 official release establishes the current toolkit version, model updates and Intel device scope. (GitHub)
- DOCUMENTED: OpenVINO system requirements and NPU documentation establish Windows/Core Ultra CPU/GPU/NPU support boundaries. (OpenVINO Dokumentation)
- DOCUMENTED: OpenVINO GenAI documentation establishes direct GGUF support for supported architectures, INT4 export paths and structured-output facilities. (OpenVINO Dokumentation)
- DOCUMENTED: OVMS 2026.3 release establishes current serving features, /v1 OpenAI-compatible API behavior, tool parsers, automatic device selection and the current 8K NPU LLM prompt limitation. (GitHub)
- DOCUMENTED: Current OVMS LLM serving documentation reports testing on Intel Core Ultra under Windows 11 and exposes OpenAI-compatible endpoints. (OpenVINO Dokumentation)

### Primary llama.cpp evidence

- DOCUMENTED: llama.cpp b10331 is the current verified build in this research pass and publishes Windows x64 CPU, Vulkan, OpenVINO and SYCL artifacts. (GitHub)
- DOCUMENTED: llama.cpp SYCL documentation explicitly supports Intel Arc and integrated GPUs. (GitHub)
- DOCUMENTED: llama.cpp's OpenVINO backend explicitly targets Intel CPU/GPU/NPU while preserving GGUF. (GitHub)
- DOCUMENTED: llama-server documents sleep/unload behavior and configurable resource fitting. (GitHub)
- DOCUMENTED: GBNF and JSON-schema-to-grammar support establish constrained generation capability. (GitHub)

### Primary Ollama evidence

- DOCUMENTED: Ollama 0.32.6 is the current verified release. (GitHub)
- DOCUMENTED: Official Windows documentation establishes native Windows service/API behavior and advertised GPU scope. (Ollama)
- DOCUMENTED: Structured outputs, tool calls, context configuration, lifecycle controls and timing metrics are documented official capabilities. (Ollama)

### Primary Microsoft / ONNX Runtime evidence

- DOCUMENTED: ONNX Runtime GenAI 0.15.2 is the current verified release and includes Windows x64 WinML/CPU artifacts. (GitHub)
- DOCUMENTED: Microsoft labels the Generate API Preview. (ONNX Runtime)
- DOCUMENTED: DirectML is in sustained engineering; Windows feature development has moved toward WinML. (ONNX Runtime)

### Historical/deprioritization evidence

- DOCUMENTED: IPEX-LLM's repository is archived. (GitHub)
- DOCUMENTED: Intel AI Playground remains beta-oriented end-user software, despite active Core Ultra support. (GitHub)

## 15. YAML

```yaml
windows_intel_runtime_research:
  evidence_date: "2026-08-09"

  runtimes:
    - "OpenVINO GenAI / OpenVINO Runtime"
    - "OpenVINO Model Server"
    - "llama.cpp"
    - "Ollama"
    - "ONNX Runtime GenAI / WinML"

  versions:
    openvino: "2026.3.0"
    openvino_model_server: "2026.3.0"
    openvino_genai: "2026.3 generation; exact package build to pin during bake-off"
    llama_cpp: "b10331 (commit 7ba604f)"
    ollama: "0.32.6 (commit c82ebbd)"
    onnxruntime_genai: "0.15.2 (commit ed5f4e8)"
    ipex_llm: "archived 2026-01-28; no new APEX adoption version"

  windows_support:
    openvino: "official Windows support"
    openvino_model_server: "official Windows packages and Windows 11/Core Ultra LLM testing documented"
    llama_cpp: "official Windows x64 CPU, Vulkan, OpenVINO and SYCL builds"
    ollama: "native Windows application"
    onnxruntime_genai: "official Windows x64 CPU and WinML packages"

  intel_gpu_support:
    openvino: "official Intel integrated/discrete GPU support"
    openvino_model_server: "Intel GPU supported; ARC-oriented LLM serving documented"
    llama_cpp_vulkan: "supported backend; Arc 140V behavior requires local measurement"
    llama_cpp_sycl: "official backend explicitly covering Intel Arc and integrated GPUs"
    llama_cpp_openvino: "official OpenVINO backend for Intel GPU"
    ollama: "generic Vulkan path; Intel GPU is not advertised as a dedicated first-class Windows backend"
    onnxruntime_genai: "available through Windows execution-provider/WinML ecosystem; exact Arc 140V GenAI behavior requires local verification"

  intel_npu_support:
    openvino: "official Core Ultra NPU support on Windows"
    openvino_model_server: "supported but current LLM execution documents an 8K maximum prompt limitation"
    llama_cpp_openvino: "backend claims Intel NPU support; exact model/path coverage requires bake-off"
    ollama: null
    onnxruntime_genai: "possible through Windows/EP ecosystem; exact target configuration unverified"

  cpu_support:
    openvino: true
    openvino_model_server: true
    llama_cpp: true
    ollama: true
    onnxruntime_genai: true

  model_format_support:
    openvino_genai:
      primary: "OpenVINO IR"
      additional: "GGUF direct loading for supported architectures"
      quantization:
        - "INT4 weight compression"
        - "INT8 weight compression"
        - "additional OpenVINO low-precision mechanisms"
    openvino_model_server:
      primary: "OpenVINO-format generative model repository"
      notes: "model pulling and local repository management supported"
    llama_cpp:
      primary: "GGUF"
      quantization:
        - "Q4-class"
        - "Q5-class"
        - "Q8-class"
        - "other GGUF quantizations"
    ollama:
      primary: "GGUF / Ollama model packaging"
      import:
        - "GGUF"
        - "supported Safetensors conversion/import workflows"
    onnxruntime_genai:
      primary: "ONNX / ONNX Runtime model packages"

  structured_output_support:
    openvino_genai:
      status: "documented"
      mechanisms:
        - "JSON Schema"
        - "regex"
        - "grammar-constrained decoding"
    openvino_model_server:
      status: "requires endpoint-level bake-off"
      notes: "GenAI backend supports structured generation; exact OpenAI endpoint feature parity must be verified"
    llama_cpp:
      status: "documented"
      mechanisms:
        - "GBNF"
        - "JSON-schema-to-grammar"
    ollama:
      status: "documented"
      mechanisms:
        - "JSON mode"
        - "JSON Schema"
    onnxruntime_genai:
      status: null

  api_and_observability:
    openvino_model_server:
      api:
        - "OpenAI-compatible chat/completions"
        - "OpenAI-compatible responses"
        - "REST"
        - "gRPC for supported serving cases"
      observability:
        - "request usage metadata"
        - "verbose raw prompt/response mode"
        - "runtime logging"
    llama_cpp:
      api:
        - "OpenAI-compatible local server"
      observability:
        - "server runtime/configuration information"
        - "timing/resource output"
    ollama:
      api:
        - "native local API"
        - "partial OpenAI compatibility"
        - "tool calling"
      observability:
        - "total_duration"
        - "load_duration"
        - "prompt token/eval metrics"
        - "generation token/eval metrics"
    onnxruntime_genai:
      api:
        - "library Generate API"
      maturity: "preview"

  load_unload_swap:
    openvino_model_server:
      model_management: true
      multi_model_configuration: true
      memory_release_on_target_machine: "unmeasured"
    llama_cpp:
      sleep_unload: true
      reload_on_request: true
      memory_release_on_target_machine: "unmeasured"
    ollama:
      preload: true
      keep_alive: true
      explicit_stop_unload: true
      memory_release_on_target_machine: "unmeasured"
    onnxruntime_genai:
      managed_server_lifecycle: null

  context_memory_findings:
    apex_target_context: "approximately 32K reliably usable"
    stretch_context: "64K"
    openvino_gpu_32k_target_machine: "unmeasured"
    llama_cpp_gpu_32k_target_machine: "unmeasured"
    ollama_32k_target_machine: "unmeasured"
    openvino_npu:
      documented_current_llm_prompt_limit: "8K in OVMS 2026.3"
      apex_default_32k_candidate: false
    dedicated_arc_vram_assumption: null
    system_ram: "~31.6 GB per authority document"
    key_requirement: "measure complete laptop coexistence, not isolated inference speed"

  primary_7_8b_bakeoff_configs:
    - id: "P1"
      runtime: "OpenVINO Model Server 2026.3.0"
      backend: "OpenVINO GPU"
      device: "Intel Arc 140V"
      representation: "OpenVINO IR INT4"
      context_tests:
        - "8K"
        - "16K"
        - "32K"
        - "64K only if 32K passes"

    - id: "P2"
      runtime: "OpenVINO Model Server 2026.3.0"
      backend: "OpenVINO CPU"
      device: "Intel Core Ultra 7 258V CPU"
      representation: "same model family / INT4"
      context_tests:
        - "8K"
        - "16K"
        - "32K"

    - id: "P3"
      runtime: "llama.cpp b10331"
      backend: "Vulkan"
      device: "Intel Arc 140V"
      representation: "GGUF quality-controlled Q4-class"
      context_tests:
        - "8K"
        - "16K"
        - "32K"

    - id: "P4"
      runtime: "llama.cpp b10331"
      backend: "SYCL"
      device: "Intel Arc 140V"
      representation: "same GGUF as P3 where supported"
      context_tests:
        - "8K"
        - "16K"
        - "32K"

    - id: "P5"
      runtime: "llama.cpp b10331"
      backend: "OpenVINO"
      device: "Intel Arc 140V"
      representation: "same GGUF family where supported"
      context_tests:
        - "8K"
        - "16K"
        - "32K"

    - id: "P6"
      runtime: "Ollama 0.32.6"
      backend: "CPU and Vulkan comparator"
      device: "CPU / Intel Arc 140V where stable"
      representation: "matching GGUF"
      purpose: "lifecycle/API convenience comparison"

  smaller_control_configs:
    - "OpenVINO GPU INT4 ~3-4B"
    - "OpenVINO CPU INT4 ~3-4B"
    - "llama.cpp Vulkan GGUF ~3-4B"
    - "optional OpenVINO NPU <=8K efficiency experiment"

  larger_challenger_configs:
    - "best OpenVINO GPU INT4 ~12-14B configuration after primary 7-8B backend is identified"
    - "best llama.cpp GPU backend with comparable ~12-14B GGUF"
    - ">14B excluded from first round unless later measurements make it decision-relevant"

  coexistence_tests_required:
    - "COEX-01 model-only baseline"
    - "COEX-02 model + normal browser workload"
    - "COEX-03 model + three subscription sessions"
    - "COEX-04 model + IDE/terminals"
    - "COEX-05 model + repo test workload"
    - "COEX-06 model + browser + occasional Claude Code/Codex process"
    - "context scaling at 8K, 16K, 32K and conditional 64K"
    - "load/unload timing"
    - "post-unload memory-release verification"
    - "3-4B -> 7-8B -> 12-14B -> 7-8B model-switch test"
    - "CPU vs OpenVINO GPU vs Vulkan vs SYCL vs llama.cpp OpenVINO backend"
    - "CPU/GPU/NPU utilization sampling"
    - "Windows responsiveness under memory pressure"
    - "runtime crash/restart and APEX checkpoint-resume test"

  rejected_or_deprioritized:
    - runtime: "IPEX-LLM"
      reason: "repository archived 2026-01-28; do not create new APEX dependency"
    - runtime: "Intel AI Playground"
      reason: "beta/end-user application rather than deterministic serving substrate"
    - runtime: "llama.cpp OpenCL"
      reason: "documented as fallback where SYCL is unavailable and not performance-optimal"
    - runtime: "ONNX Runtime GenAI as first-line runtime"
      reason: "GenAI API remains Preview; keep as secondary Windows-native comparator"
    - runtime: "Ollama as Intel performance reference"
      reason: "useful lifecycle/API layer but Intel GPU is not the dedicated first-party Windows acceleration path"
    - runtime: "NPU as default APEX execution device"
      reason: "current OVMS LLM NPU prompt limit is 8K, below APEX ~32K target"

  unresolved_unknowns:
    - "Arc 140V throughput for each backend on the operator machine"
    - "reliable 32K context coexistence for 7-8B"
    - "practical 64K stretch viability"
    - "shared-memory pressure under browser/IDE/test load"
    - "complete memory release after model unload"
    - "NPU roadmap beyond current 8K prompt limit"
    - "structured-output feature parity through OVMS OpenAI endpoints"
    - "Vulkan vs SYCL vs OpenVINO backend stability on Arc 140V"
    - "OpenVINO IR INT4 versus GGUF quantization quality equivalence"
    - "12-14B coexistence envelope"
    - "exact installed Intel GPU/NPU driver versions"
    - "simultaneous model residency economics"
    - "crash/sleep/resume recovery behavior"
    - "APEX CODE/WEEKLY/MA/INJECT semantic and authority reliability for every candidate"

  overall_confidence_0_to_100: 88
```
