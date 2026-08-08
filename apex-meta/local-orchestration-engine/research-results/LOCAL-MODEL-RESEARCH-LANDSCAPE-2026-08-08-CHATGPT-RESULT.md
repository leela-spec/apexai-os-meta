---
title: "Local Model Research Result — Landscape — ChatGPT"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08.md
prompt_id: A
agent: chatgpt
agent_model_label: "ChatGPT, reasoning effort: Mittel (Medium, UI default)"
agent_mode: "standard reasoning + web search (Websuche toggle manually enabled)"
account_tier: "subscription (plan tier not disclosed by UI)"
run_id: R1
run_started: "2026-08-08"
run_duration_seconds: null
evidence_date: 2026-08-08
chat_url: "https://chatgpt.com/c/6a774be6-4fe0-83eb-95d2-0a5494c6613c"
bundle_sha256: "638c150c3503cf9ee2e802a1870db18c088b268fc4efb1712b770e62a3da7d10"
retries: 0
interruptions:
  - "Composer became unresponsive for roughly 20 seconds after the ~37KB bundle was inserted via execCommand('insertText'); confirmed via screenshot that the full bundle was intact once responsive again."
uncontrolled_variables:
  - "Fresh chat outside any ChatGPT Project (not run inside e.g. FusionAi2/Master of Arts) to avoid inherited custom instructions."
  - "Reasoning effort left at UI default (Mittel/Medium) rather than a maximum-effort mode."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Landscape — ChatGPT

> Operator note: this file is the verbatim (reformatted-for-markdown) output of ChatGPT executing Research Prompt A (Local Model Landscape) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection. A UI "thought for 1m 38s" indicator preceding the response has been omitted as a cosmetic artifact.

## APEX OS — Local Model Landscape Research Packet

Evidence date: 2026-08-08

Authority basis: Operator Decision Lock R3 + Local Model Benchmark Portfolio supplied in the prompt.
Scope: candidate landscape only; no production model or runtime selection.

Claim taxonomy used throughout:

MEASURED — directly measured on the target APEX laptop or APEX benchmark harness.

DOCUMENTED — stated by a primary source or supplied APEX authority document.

INFERRED — analytical conclusion from documented evidence, not yet locally verified.

UNKNOWN — evidence is insufficient; local APEX testing is required.

MEASURED: No APEX model/runtime trials were performed for this research packet. Therefore no model-quality, throughput, RAM, latency, context-reliability, coexistence, prompt-injection, or task-success claim below is classified MEASURED.

### 1. Executive finding

DOCUMENTED: The current landscape contains credible candidates on both sides of the operator's ~7–8B hypothesis. The strongest directly aligned family discovered is Ministral 3, released December 2, 2025, with matched dense 3B, 8B, and 14B variants under Apache 2.0. The 8B version is explicitly designed for edge/local deployment, has a 256K advertised context, native function calling, JSON output, system-prompt support, and official GGUF artifacts.

DOCUMENTED: Qwen3-8B remains a serious 8B-class comparator: 8.2B parameters, Apache 2.0, 32,768-token native context, 131,072 with validated YaRN configuration, switchable thinking/non-thinking operation, documented agent/tool integration, and official local-runtime support including llama.cpp.

DOCUMENTED: The efficiency-control class is substantially stronger than a generic "small model" baseline. Qwen3-4B-Instruct-2507 is 4.0B parameters with 262,144 native context and explicit improvements in instruction following, coding and tool usage; Phi-4-mini-instruct is 3.8B with 128K context and a documented tool-enabled function-calling format; Ministral 3 3B supplies a clean same-family control against Ministral 3 8B.

DOCUMENTED: Credible 12–14B challengers exist. Gemma 4 12B Unified, released June 3, 2026, has 11.95B parameters, 256K context, configurable thinking, native function calling, coding positioning and an official QAT Q4_0 GGUF weighing about 6.98 GB. Ministral 3 14B supplies the clean matched-family larger control.

INFERRED: The evidence therefore supports the operator's research design rather than falsifying it in advance: ~7–8B remains the correct primary bake-off center, but it is not obvious that it will win every APEX task class.

INFERRED: The most decision-efficient initial hypothesis test is:

Ministral 3 3B Instruct
↓
Ministral 3 8B Instruct
Ministral 3 8B Reasoning
↓
Ministral 3 14B Instruct / Reasoning

plus cross-family controls:
Qwen3-4B-Instruct-2507
Qwen3-8B
Phi-4-mini-instruct
Gemma 4 12B-it

This isolates size effects inside one family while retaining strong cross-family alternatives.

INFERRED: For APEX specifically, the likely 8B advantage over 3–4B is not generic knowledge. The relevant expected gain is fewer false-success states, missed escalations, malformed tool arguments, ambiguous-state guesses, and micro-coding mistakes. That remains unverified.

INFERRED: A 12–14B configuration deserves promotion only if it materially reduces those execution failures or CLI escalations. Generic reasoning gains alone would not justify its extra memory and coexistence burden under LM-25/LM-26.

UNKNOWN: No public evidence establishes that any candidate achieves:

zero successful unauthorized actions;
adequate prompt-injection resistance;
reliable APEX UNKNOWN/escalation classification;
correct bounded recovery;
reliable ~32K working context rather than merely accepting 32K+ tokens;
acceptable browser/IDE/test/CLI coexistence on the HP OmniBook;
correct candidate/verified authority separation.

Those are benchmark-gated APEX questions.

### 2. Evidence date and freshness map

| Candidate / runtime | Evidence freshness | Status |
|---|---|---|
| Gemma 4 E4B / 12B | DOCUMENTED: Gemma 4 initial family release March 31, 2026; 12B Unified release June 3, 2026; technical report July 2026. | Very current |
| OpenVINO 2026.x | DOCUMENTED: Current 2026 documentation includes Windows GenAI/NPU instructions; OpenVINO 2026.2 was announced June 2026 and current docs expose the 2026.3 documentation line. | Very current |
| Qwen3-Coder-Next | DOCUMENTED: Current coding model designed for local development; 80B total / 3B active. | Current but hardware-misaligned |
| Mistral 3 family | DOCUMENTED: Released December 2, 2025. | Current |
| Qwen3-Coder-30B-A3B | DOCUMENTED: Current official repository remains available with agentic coding/browser positioning. | Current |
| Qwen3-8B | DOCUMENTED: Qwen3 generation; official repository remains active and supported by current local applications. | Older than 2026 entrants but still relevant |
| Qwen3-4B-Instruct-2507 | DOCUMENTED: July 2025 revision with 256K-context/tool-use improvements. | Relevant control |
| Phi-4-mini-instruct | DOCUMENTED: Released February 26, 2025. | Older but strong control |
| Phi-4 14B | DOCUMENTED: Released December 12, 2024; only 16K context. | Stale / context-misaligned |
| llama.cpp | DOCUMENTED: Current server supports quantized CPU/GPU inference, SYCL for Intel GPU, hybrid CPU/GPU inference, schema-constrained JSON and function/tool calling. | Current moving runtime |

INFERRED: Freshness matters most where it changed the decision surface: Mistral 3 and Gemma 4 make a shortlist centered exclusively on 2024–early-2025 models obsolete.

### 3. Primary ~7–8B shortlist

**3.1 Ministral 3 8B Instruct 2512**
Exact artifact: mistralai/Ministral-3-8B-Instruct-2512
DOCUMENTED — release: December 2, 2025. Apache 2.0.
DOCUMENTED — architecture: 8.4B language model plus ~0.4B vision encoder.
DOCUMENTED — context: 256K advertised.
DOCUMENTED — tools: native function calling and JSON output; system-prompt support. Mistral's hosted model card separately exposes Structured Outputs and Function Calling.
DOCUMENTED — local footprint: official card states FP8 fits in 12 GB VRAM and quantized representations require less.
DOCUMENTED — artifact: Mistral publishes official GGUF variants including Q4_K_M.
INFERRED — APEX fit: strongest first candidate for the main 8B execution profile because its documented attributes match tool invocation, schema production, local deployment and bounded agent operation unusually directly.
UNKNOWN: whether 32K execution trajectories remain semantically reliable on APEX fixtures.
UNKNOWN: prompt-injection/authority-boundary behavior.
UNKNOWN: actual Arc 140V performance and coexistence.
Research priority: P1.

**3.2 Ministral 3 8B Reasoning 2512**
Exact artifact: mistralai/Ministral-3-8B-Reasoning-2512
DOCUMENTED — architecture: same 8.4B language-model class plus 0.4B vision encoder.
DOCUMENTED — license: Apache 2.0.
DOCUMENTED — context: 256K.
DOCUMENTED — tools: native function calling, JSON output and explicit agentic positioning.
DOCUMENTED — representation: official GGUF repository exists; quantized version is documented as less than 12 GB RAM/VRAM.
DOCUMENTED — operational caveat: Mistral recommends retaining reasoning traces across multi-turn operation and limiting tool count.
INFERRED — APEX fit: essential intra-size comparator. It can test whether extra reasoning reduces CODE-03/CODE-04/MA-05 failures or instead increases latency, output churn and unnecessary autonomy.
INFERRED: the reasoning variant should not automatically supersede Instruct. APEX rewards bounded correctness, not maximum reasoning.
UNKNOWN: whether retaining reasoning traces creates unacceptable 32K context/KV pressure under laptop coexistence.
Research priority: P1/P2, paired with the Instruct version.

**3.3 Qwen3-8B**
Exact artifact: Qwen/Qwen3-8B
DOCUMENTED — architecture: dense causal LM, 8.2B total parameters / 6.95B non-embedding, 36 layers, GQA. Apache 2.0 repository.
DOCUMENTED — context: 32,768 native; Qwen reports validation to 131,072 using YaRN.
DOCUMENTED — operation modes: switchable thinking and non-thinking modes.
DOCUMENTED — agent positioning: official model card states external-tool integration in thinking and non-thinking modes.
DOCUMENTED — runtime breadth: official card lists Ollama, LM Studio, llama.cpp and other local applications.
DOCUMENTED — artifact: official Qwen GGUF repository exists; AWQ 4-bit also exists.
DOCUMENTED — important generation caveat: Qwen explicitly warns against greedy decoding for thinking mode because it can degrade performance and produce repetition.
INFERRED — APEX fit: high-value cross-family benchmark because its native 32K context aligns almost exactly with LM-23, eliminating the need to infer 32K capability from a much larger advertised maximum.
INFERRED: its dual-mode operation could become two planner profiles if APEX fixtures show a meaningful task-class distinction.
UNKNOWN: whether thinking-mode tool trajectories outperform the newer Ministral 3 8B family.
UNKNOWN: whether Qwen's long-context YaRN mode is useful or necessary beyond APEX's 32K default.
Research priority: P1.

### 4. ~3–4B efficiency controls

**4.1 Qwen3-4B-Instruct-2507**
DOCUMENTED: Exact model is Qwen/Qwen3-4B-Instruct-2507, 4.0B parameters / 3.6B non-embedding.
DOCUMENTED: Native context is 262,144 tokens.
DOCUMENTED: Qwen specifically reports improvements in instruction following, coding and tool use.
DOCUMENTED: Qwen's own reported public agent evaluations include BFCL-v3 and TAU task suites; these are vendor benchmark evidence, not APEX certification.
INFERRED: this is probably the strongest pure 4B efficiency control for APEX because it directly targets tool use and instruction compliance rather than merely reasoning.
UNKNOWN: whether its resource savings versus an 8B are large enough on the target laptop to offset any execution-quality loss.
Priority: P2.

**4.2 Ministral 3 3B Instruct 2512**
DOCUMENTED: Current 3B-class member of the same December 2025 Mistral 3 generation.
DOCUMENTED: Designed for edge deployment; official documentation says FP8 fits in 8 GB VRAM and further quantization reduces footprint.
DOCUMENTED: Official GGUF is available.
INFERRED: this is the most scientifically useful efficiency control, because comparing Ministral 3 3B → 8B → 14B reduces family/training-generation confounds.
UNKNOWN: whether 3B can maintain correct escalation and scope discipline under ambiguous CODE/MA fixtures.
Priority: P2.

**4.3 Phi-4-mini-instruct**
DOCUMENTED: microsoft/Phi-4-mini-instruct, 3.8B parameters, MIT license, 128K context.
DOCUMENTED: Model card includes a dedicated tool-enabled function-calling format; Microsoft states function-calling post-training was part of the release.
DOCUMENTED: Microsoft publishes official ONNX artifacts including CPU/mobile INT4 and GPU INT4 variants.
DOCUMENTED: Microsoft explicitly positions it for memory/compute-constrained and latency-bound environments.
INFERRED: its main value is not freshness but a runtime-diverse control: ONNX/OpenVINO-oriented deployment may behave differently from GGUF/llama.cpp.
UNKNOWN: whether its older post-training is competitive with Qwen3-4B-2507 or Ministral 3 3B on modern agentic flows.
Priority: P3.

Gemma 4 E4B note
DOCUMENTED: Gemma 4 E4B is not a clean 4B parameter-count control. Google defines it as 4.5B effective parameters but 8B including embeddings, due to Per-Layer Embeddings. Its official Q4 GGUF alone is about 5.15 GB plus a ~992 MB multimodal projector.
INFERRED: It should therefore be treated as an architectural-efficiency boundary case, not silently counted as a conventional 4B model.
INFERRED: It is worth a second-wave benchmark if Gemma 4 12B performs well, but not required for the minimum first bake-off.

### 5. ~12–14B challengers

**5.1 Gemma 4 12B-it**
Exact artifact: google/gemma-4-12B-it
DOCUMENTED: Gemma 4 12B Unified was released June 3, 2026.
DOCUMENTED: 11.95B parameters, dense/encoder-free unified architecture.
DOCUMENTED: 256K context.
DOCUMENTED: configurable thinking, native system prompts, function calling, coding and agentic positioning.
DOCUMENTED: Apache 2.0.
DOCUMENTED: Google publishes a QAT Q4_0 GGUF; Hugging Face reports the 4-bit file at about 6.98 GB and provides Windows llama.cpp launch instructions.
INFERRED: this is unusually plausible for a 12B-class laptop challenger because the official QAT representation makes weight storage substantially smaller than naïve BF16 size.
INFERRED: on a ~31.6 GB unified-memory machine, the model weights themselves are unlikely to be the sole obstacle; the real question is KV cache, runtime buffers, OS/browser/IDE pressure and iGPU shared-memory contention.
UNKNOWN: actual 32K KV/cache footprint on the selected runtime.
UNKNOWN: tool-call semantic reliability versus Ministral 3 8B.
UNKNOWN: whether multimodal components create unnecessary memory/runtime cost for text-centric APEX tasks.
Priority: P2/P3 challenger.

**5.2 Ministral 3 14B Instruct 2512**
DOCUMENTED: Exact artifact mistralai/Ministral-3-14B-Instruct-2512; December 2025 family, Apache 2.0.
DOCUMENTED: Native function-calling examples are included in the official model repository.
DOCUMENTED: Official GGUF artifacts are published.
INFERRED: highest-value 14B challenger because it provides a clean size escalation from the same 3B/8B family.
INFERRED: use primarily to answer one question: does doubling the practical-center model size materially reduce APEX execution failures?
UNKNOWN: coexistence on this laptop at 32K.
UNKNOWN: whether any quality advantage survives quantization to the configuration required for local coexistence.
Priority: P3.

**5.3 Ministral 3 14B Reasoning 2512**
DOCUMENTED: 14B-class reasoning-specific member exists under Apache 2.0 with native function calling and JSON output.
DOCUMENTED: Mistral's own deployment instructions warn that fully exploiting its very large context is GPU-intensive.
INFERRED: locally, APEX should benchmark it only at the relevant ~32K tier rather than attempting the advertised maximum context.
INFERRED: useful only if CODE-04/MA-05 or difficult recovery fixtures expose a real reasoning deficit in 8B.
UNKNOWN: whether that gain would justify memory/latency penalties.
Priority: P4 conditional challenger.

### 6. Justified >14B stretch case

Devstral Small 2 24B — coding-only stretch
Exact artifact: mistralai/Devstral-Small-2-24B-Instruct-2512
DOCUMENTED: 24B dense model specifically trained for agentic software engineering, codebase exploration, tool use and multi-file editing; Apache 2.0 weights remain available.
DOCUMENTED: Mistral's current offline-model guidance recommends Devstral Small 2 for local coding and states that 4-bit operation at ~32K can target a 24 GB GPU; CPU offload is also supported when sufficient RAM is available, although it is significantly slower.
DOCUMENTED: The original full repository is approximately 51.6 GB in its supplied higher-precision artifacts, demonstrating why quantization is mandatory here.
INFERRED: this provides enough evidence to classify Devstral Small 2 as technically runnable in a constrained quantized/offloaded configuration, but not as likely laptop-coexistence winner.
INFERRED: it is decision-relevant only for the bounded CODE task class, where reduced Claude Code/Codex escalation could conceivably pay for much heavier resource use.
INFERRED: it should not participate in the first general-executor bake-off.
UNKNOWN: whether ~31.6 GB shared system RAM leaves enough operational headroom once Windows, browsers, IDE, tests, KV cache and runtime buffers are included.
UNKNOWN: usable speed on the Core Ultra 7 258V.
UNKNOWN: whether CODE-01..05 gains over an 8B justify the footprint.
Conclusion: INFERRED — justified as a late coding stretch case, not a general-executor candidate.

### 7. Coding challengers

| Candidate | Evidence | APEX role hypothesis |
|---|---|---|
| Ministral 3 8B Reasoning 2512 | DOCUMENTED: reasoning version explicitly targets coding/STEM while retaining native function calling. | INFERRED: first coding challenger because no size penalty versus main 8B class. |
| Qwen3-8B | DOCUMENTED: thinking mode explicitly targets coding/reasoning and tool integration. | INFERRED: bounded micro-coder/generalist candidate. |
| Qwen3-Coder-30B-A3B-Instruct | DOCUMENTED: 30B total / ~3B active MoE coding model, positioned for agentic coding and browser use; native 256K context is documented. | INFERRED: potentially strong specialist, but total-weight memory makes it a later resource-gated test. |
| Devstral Small 2 24B | DOCUMENTED: purpose-built agentic software-engineering model. | INFERRED: heavy specialist to test whether CLI escalation can be materially reduced. |
| Qwen3-Coder-Next | DOCUMENTED: local-development coding agent model with only 3B active parameters but 80B total parameters. | INFERRED: architecturally attractive but not credible for routine coexistence on 31.6 GB RAM; exclude from local bake-off unless a representation materially changes the memory equation. |

INFERRED: The critical coding metric is not SWE-bench. It is:
bounded patch success + correct stop/escalation + zero unauthorized scope + minimal diff + acceptance-test correctness + reduction in Claude Code/Codex escalations
UNKNOWN: No public coding benchmark answers that APEX-specific question.

### 8. Excluded or deprioritized candidates

| Candidate | Decision |
|---|---|
| Phi-4 14B | DOCUMENTED: only 16K context despite strong reasoning positioning. INFERRED: fails the LM-23 target without compensating evidence; deprioritize. |
| Ministral-8B-Instruct-2410 | DOCUMENTED: officially deprecated in favor of Ministral 3 8B. INFERRED: obsolete for new APEX integration. |
| Gemma 3 4B/12B | DOCUMENTED: superseded by Gemma 4 generation. INFERRED: retain only for regression/history, not current shortlist. |
| Qwen2.5-Coder 7B | INFERRED: formerly attractive size-fit but superseded as a research priority by newer Qwen/Mistral agentic models; not needed in a small current portfolio. |
| Qwen3-Coder-480B-A35B | DOCUMENTED: 480B total / 35B active flagship. INFERRED: plainly outside this machine's decision-relevant envelope. |
| Qwen3-Coder-Next 80B total / 3B active | DOCUMENTED: 80B total weights despite 3B activation. INFERRED: active-parameter efficiency does not eliminate weight-memory requirements; too risky for 31.6 GB coexistence. |
| Gemma 4 26B A4B | DOCUMENTED: 25.2B total / 3.8B active MoE. INFERRED: interesting architecture but unnecessary in the first experiment because Gemma 12B already tests the family with much simpler resource economics. |
| Gemma 4 E4B | DOCUMENTED: 4.5B effective / 8B including embeddings. INFERRED: useful later, but parameter-class ambiguity makes it a poor first control. |
| Llama 3.x 8B-era candidates | INFERRED: no longer the strongest freshness-aligned way to test the 8B hypothesis given current Mistral 3/Qwen3 options; use only if runtime compatibility creates a specific need. |
| Models >30B dense | INFERRED: no demonstrated APEX value sufficient to justify their likely coexistence cost on this machine. |

### 9. Capability-by-task-class matrix

Legend: H = high documented plausibility; M = plausible; L = weak/deprioritized; ? = unknown until APEX test. Ratings are INFERRED, not certifications.

| Configuration | CODE | Weekly browser/state | MA worker/evidence | Tool/schema | 32K plausibility | Coexistence | Likely registry hypothesis |
|---|---|---|---|---|---|---|---|
| Ministral 3 8B Instruct | H | H | H | H | H | M/H | Default bounded executor |
| Ministral 3 8B Reasoning | H | M/H | H | H | H | M | Difficult bounded reasoning |
| Qwen3-8B | H | H | H | H | H | M/H | General executor / reasoning toggle |
| Qwen3-4B-2507 | M/H | M/H | H | H | H | H | Efficiency executor |
| Ministral 3 3B Instruct | M | M | M/H | M/H | H | H | Low-cost routine worker |
| Phi-4-mini | M | M | M/H | H | H | H | ONNX/runtime-diverse control |
| Gemma 4 12B-it | H | H | H | H | H | M/L | High-capability challenger |
| Ministral 3 14B Instruct | H | H | H | H | H | M/L | Larger general challenger |
| Ministral 3 14B Reasoning | H | M | H | H | H | L/M | Hard-reasoning challenger |
| Devstral Small 2 24B | H | L | M | H | H | L | CODE specialist only |
| Qwen3-Coder-30B-A3B | H | M/H | M | H | H | L | CODE/browser specialist stretch |

DOCUMENTED: Ministral 3, Gemma 4, Qwen3 and Phi-4-mini all provide documented tool/function-call mechanisms; llama.cpp can separately constrain schema output at the runtime level.
UNKNOWN: Hostile-content resistance is ? for every row. No candidate should receive a favorable rating from generic safety benchmarks alone.

### 10. Context / tool / structured-output evidence

Context:
DOCUMENTED: Ministral 3 8B advertises 256K.
DOCUMENTED: Ministral 3 14B likewise belongs to the long-context family; Mistral warns that maximum-context deployment is hardware intensive.
DOCUMENTED: Qwen3-8B has 32,768 native context and Qwen reports YaRN validation to 131,072.
DOCUMENTED: Qwen3-4B-Instruct-2507 has 262,144 native context.
DOCUMENTED: Phi-4-mini has 128K.
DOCUMENTED: Gemma 4 12B supports 256K; E4B supports 128K.
INFERRED: Every shortlisted candidate clears the advertised 32K requirement except deprecated Phi-4 14B.
UNKNOWN: Advertised maximum context does not establish LM-23's "reliably usable working context." APEX must test 8K / 16K / 32K / 64K with actual trajectories and retrieval.

Tool use:
DOCUMENTED: Ministral 3 8B Instruct and Reasoning advertise native function calling and JSON output.
DOCUMENTED: Mistral's current API model documentation exposes Structured Outputs and Function Calling for Ministral 3 8B.
DOCUMENTED: Qwen3 describes strong agent capability and external-tool integration.
DOCUMENTED: Qwen3-4B-2507 specifically reports improved tool usage.
DOCUMENTED: Phi-4-mini provides an explicit tool-enabled function-calling format.
DOCUMENTED: Gemma 4 provides native function calling.
UNKNOWN: None of these claims establish correct tool selection, argument semantics, stop behavior, least privilege, or escalation under APEX packets.

Runtime-enforced structured output:
DOCUMENTED: Current llama.cpp server supports schema-constrained JSON response format and function/tool calling.
DOCUMENTED: llama.cpp's GBNF grammars can force syntactically valid JSON or other formal output languages.
DOCUMENTED: llama.cpp notes that only a subset of JSON Schema features is supported by its schema-to-grammar machinery.
INFERRED: This fits LM-24 well: model tool decision + runtime/schema constraint + APEX semantic validator + capability broker + bounded retry.
INFERRED: Native model JSON capability should therefore be treated as a quality feature, not the sole correctness mechanism.

### 11. Runtime / artifact availability map

**11.1 llama.cpp**
DOCUMENTED: Supports Windows-capable local CPU/GPU inference, numerous quantized formats, Vulkan and SYCL backends, CPU+GPU hybrid inference and an OpenAI-style server.
DOCUMENTED: SYCL target is explicitly Intel GPU.
DOCUMENTED: Server supplies schema-constrained JSON, tool use, monitoring and controllable context/KV settings.
INFERRED: highest-priority portability/reference runtime for the first APEX bake-off because it exposes the controls the benchmark needs and accepts GGUF across multiple shortlisted families.
UNKNOWN: whether SYCL or Vulkan is faster/more stable on Arc 140V.
UNKNOWN: exact current per-model parser/chat-template behavior must be regression-tested.

**11.2 OpenVINO GenAI**
DOCUMENTED: OpenVINO has Windows deployment support and GenAI pipelines targeting Intel hardware.
DOCUMENTED: 2026 NPU documentation provides Windows installation for OpenVINO/OpenVINO GenAI.
DOCUMENTED: OpenVINO documentation supports direct GGUF loading for supported architectures without mandatory IR conversion.
DOCUMENTED: Intel has documented OpenVINO use across Intel CPU/iGPU/dGPU, and newer Windows ML support spans Intel Core Ultra CPU/GPU/NPU.
INFERRED: highest-priority Intel-optimized challenger runtime.
UNKNOWN: support maturity for every newest model architecture in this shortlist.
UNKNOWN: whether NPU execution supports the generation modes/tool interfaces required by each candidate.
UNKNOWN: whether NPU use improves total job completion time versus Arc GPU/CPU once prompt processing, generation and transfers are counted.

**11.3 ONNX Runtime path**
DOCUMENTED: Microsoft publishes official Phi-4-mini ONNX INT4 artifacts for CPU/mobile and GPU configurations.
INFERRED: Phi-4-mini is therefore useful as a second runtime-stack control rather than only a model-quality control.

**11.4 Model artifact map**

| Model | Official high-precision weights | Official quantized/local artifact |
|---|---|---|
| Ministral 3 8B Instruct | DOCUMENTED: FP8/BF16 family artifacts. | DOCUMENTED: official GGUF including Q4_K_M. |
| Ministral 3 8B Reasoning | DOCUMENTED: BF16. | DOCUMENTED: official GGUF. |
| Qwen3-8B | DOCUMENTED: safetensors. | DOCUMENTED: official GGUF and AWQ. |
| Qwen3-4B-2507 | DOCUMENTED: official safetensors. | DOCUMENTED: compatible third-party GGUF ecosystem exists; no official Qwen GGUF was verified in this run. |
| Phi-4-mini | DOCUMENTED: official HF weights. | DOCUMENTED: official ONNX INT4. |
| Gemma 4 12B-it | DOCUMENTED: official safetensors. | DOCUMENTED: official QAT Q4_0 GGUF, ~6.98 GB. |
| Ministral 3 14B | DOCUMENTED: official FP8/BF16. | DOCUMENTED: official GGUF. |

### 12. Size-vs-resource-vs-execution hypothesis matrix

| Class | Resource hypothesis | Execution hypothesis | What falsifies it |
|---|---|---|---|
| 3–4B | INFERRED: lowest RAM/KV pressure; strongest coexistence. | INFERRED: likely adequate for deterministic-ish Weekly/MA hygiene, but higher risk on ambiguity, recovery and micro-coding. | MEASURED future result: matches 8B on hard execution metrics while materially reducing resource cost. |
| 7–8B | INFERRED: quantized weights comfortably below total system RAM; plausible room for browser/IDE/tests. | INFERRED: best expected balance of semantic judgement, tool use, recovery and resource load. | 3–4B matches it, or 12–14B materially lowers interventions/escalations without unacceptable coexistence loss. |
| 12–14B | INFERRED: runnable with modern 4-bit representations, but KV/runtime/shared-memory pressure becomes materially more consequential. | INFERRED: likely better on ambiguity and difficult coding/reasoning; gains may be irrelevant for closed-state routine execution. | No meaningful improvement on APEX failure classes, or coexistence penalty dominates. |
| 24–30B coding | INFERRED: technically possible only under aggressive quantization/offload; high coexistence risk. | INFERRED: may reduce hard-code escalation, especially repo-scale/tool-heavy work. | CLI-escalation reduction insufficient to pay resource/latency cost. |
| 80B+ total MoE | INFERRED: total weight storage becomes incompatible with the intended routine laptop envelope even where active parameters are small. | UNKNOWN: capability may be strong but operationally irrelevant. | Only reconsider if new representations demonstrate safe coexistence on this hardware. |

Explicit comparison required by the prompt:

What does ~7–8B appear to gain over ~3–4B?
DOCUMENTED: Vendor-reported family benchmarks for Ministral 3 generally increase from 3B to 8B on reasoning and instruction evaluations.
INFERRED: For APEX, the expected consequential gain is: better ambiguity discrimination; fewer wrong tool arguments; stronger instruction hierarchy adherence; fewer false-success classifications; better tiny-fix reasoning; improved recovery after partial failures.
UNKNOWN: Whether those improvements actually occur on CODE/WEEKLY/MA fixtures.

What does ~12–14B appear to gain over ~7–8B?
DOCUMENTED: Mistral's own same-family public evaluations generally show 14B ahead of 8B on reasoning and instruction suites.
INFERRED: The APEX-relevant gain would principally be harder ambiguity resolution, CODE-03 micro-fixes, CODE-04 escalation discrimination and MA-05 failure routing.
UNKNOWN: Whether the delta is large enough to affect human-intervention or CLI-escalation rates.

Are those gains relevant to bounded execution rather than generic intelligence?
INFERRED: Possibly, but not yet established. The model only earns its extra footprint if gains appear in trajectory correctness and final environment outcomes.
UNKNOWN: Public reasoning/coding scores cannot answer this.

### 13. Benchmark priority order

Phase A — falsify or support the 7–8B center cheaply:
1. mistralai/Ministral-3-8B-Instruct-2512-GGUF, Q4_K_M, first with llama.cpp.
2. Qwen/Qwen3-8B official GGUF, comparable ~4-bit representation, llama.cpp.
3. mistralai/Ministral-3-8B-Reasoning-2512-GGUF, same runtime/quantization policy.
4. mistralai/Ministral-3-3B-Instruct-2512-GGUF, matched-family efficiency control.
5. Qwen/Qwen3-4B-Instruct-2507, closest practical quantization supported by selected runtime.
6. microsoft/Phi-4-mini-instruct-onnx, primarily as runtime/efficiency control.

Phase B — larger-model falsification:
7. google/gemma-4-12B-it-qat-q4_0-gguf, official 6.98 GB Q4_0 artifact.
8. mistralai/Ministral-3-14B-Instruct-2512-GGUF.
9. mistralai/Ministral-3-14B-Reasoning-2512-GGUF, only if reasoning-sensitive failures remain.

Phase C — coding-only stretch:
10. Qwen3-Coder-30B-A3B-Instruct, only after a memory/load probe confirms safe launch headroom.
11. Devstral Small 2 24B at 4-bit / ~32K, only for CODE fixtures and only if 8–14B profiles still escalate frequently.

Runtime sequence (INFERRED):
Reference: GGUF + llama.cpp CPU
↓ Intel acceleration: GGUF + llama.cpp SYCL / GGUF + llama.cpp Vulkan
↓ Intel-specialized: OpenVINO GenAI CPU / GPU / NPU where model support permits
↓ cross-stack control: Phi-4-mini ONNX
This sequence separates model effects from backend effects rather than changing both simultaneously.

### 14. Major unknowns only local APEX testing can settle

- Authority discipline: Which model most consistently refuses undeclared roots, unauthorized commands, promotion and workflow widening?
- Injection resistance: Which model attempts poisoned instructions in files, browser results, code comments or tool output?
- False success: Which model is most likely to declare success after incomplete/ambiguous actions?
- UNKNOWN handling: Which model reliably selects UNKNOWN rather than inventing a state?
- Typed escalation: Which model distinguishes mechanical/transient/hard-code/reasoning/security/authority failures correctly?
- Tool arguments: Which model produces semantically correct arguments, not merely valid JSON?
- Structured retry: How frequently does each configuration need schema retry or semantic repair?
- Micro-coding: Does 8B materially outperform 3–4B on CODE-03 without exceeding the one-attempt envelope?
- Ambiguity restraint: Does 12–14B reduce CODE-04 guessing or does stronger capability make unauthorized fixing more tempting?
- 32K reliability: At 32K, what happens to action correctness, state tracking, tool churn and false-success rate?
- 64K stretch: Does any profile preserve enough quality to justify certification beyond 32K?
- Retrieval: How much JIT retrieval offsets parameter-size differences?
- Reasoning traces: Does retaining Ministral reasoning state improve multi-turn correctness enough to justify KV/context cost?
- Inference mode: Qwen3 thinking versus non-thinking — which task classes actually benefit?
- Quantization loss: Which model families suffer meaningful tool/semantic degradation at Q4 relative to higher precision?
- Arc 140V backend: llama.cpp SYCL versus Vulkan versus OpenVINO GPU.
- NPU usefulness: Whether Core Ultra NPU execution can support candidate architectures and required generation features productively.
- Peak RAM: real committed/resident RAM at 8K/16K/32K/64K.
- Shared-memory contention: actual effect of integrated Arc graphics and browser workloads.
- Coexistence: responsiveness under COEX-02 through COEX-06.
- Load/swap: model loading, unloading and planner profile switching cost.
- Throughput under work: tokens/sec is insufficient; successful bounded jobs per wall-time remains unmeasured.
- Intervention: human interventions per 100 jobs.
- CLI displacement: Claude Code/Codex escalations per 100 CODE jobs.
- Profile topology: whether the registry ultimately needs one 8B generalist, Instruct+Reasoning pair, 4B+8B ladder, or coding specialist.
- Public-vs-APEX correlation: whether generic tool/coding/reasoning benchmarks predict any important APEX outcome.

### 15. Source appendix

Primary model sources:
- Mistral: Mistral 3 release announcement, December 2, 2025; matched 3B/8B/14B models, Apache 2.0.
- Mistral: Ministral 3 8B Instruct official model repository.
- Mistral: Ministral 3 8B Reasoning official repository.
- Mistral: Ministral 3 8B official model documentation, including structured outputs/function calling.
- Mistral: official Ministral 3 GGUF artifacts.
- Qwen: Qwen3-8B official model card.
- Qwen: official Qwen3-8B GGUF repository.
- Qwen: Qwen3-4B-Instruct-2507 official model card.
- Microsoft: Phi-4-mini-instruct official model card.
- Microsoft: February 26, 2025 Phi-4-mini release announcement.
- Microsoft: official Phi-4-mini ONNX artifact repository.
- Google: Gemma 4 official model card / architecture data.
- Google: Gemma release chronology.
- Google: official Gemma 4 12B QAT Q4_0 GGUF.
- Mistral: Devstral Small 2 official weights/model documentation.
- Qwen: Qwen3-Coder-30B-A3B official model repository.
- Qwen: Qwen3-Coder-Next official model card.

Primary runtime sources:
- llama.cpp: current project README and supported backends, including SYCL for Intel GPUs and hybrid CPU/GPU inference.
- llama.cpp: server documentation covering JSON-schema constrained output, function calling, observability and context/KV controls.
- llama.cpp: GBNF structured-output mechanism.
- OpenVINO: 2026 Windows NPU GenAI documentation.
- OpenVINO: direct GGUF loading in GenAI for supported architectures.
- Intel: current Core Ultra/Windows ML/OpenVINO CPU/GPU/NPU support direction.

INFERRED — evidence quality: The candidate conclusions above are dominated by model developers' repositories, model cards and runtime documentation. Vendor benchmark numbers were used only as prioritization evidence, never as APEX certification.

INFERRED — overall confidence: 84/100 for the landscape and benchmark shortlist; substantially lower confidence for actual execution ranking because no target-machine APEX trials have yet occurred.

### 16. YAML

```yaml
local_model_landscape:
  evidence_date: "2026-08-08"
  primary_7_8b_candidates:
    - model: "mistralai/Ministral-3-8B-Instruct-2512"
      status: "DOCUMENTED"
      parameter_class: "~8B"
      exact_parameters: "8.4B language model + ~0.4B vision encoder"
      license: "Apache-2.0"
      context_documented: 262144
      primary_role_hypothesis: "default bounded executor"
    - model: "mistralai/Ministral-3-8B-Reasoning-2512"
      status: "DOCUMENTED"
      parameter_class: "~8B"
      exact_parameters: "8.4B language model + ~0.4B vision encoder"
      license: "Apache-2.0"
      context_documented: 262144
      primary_role_hypothesis: "reasoning-sensitive bounded executor"
    - model: "Qwen/Qwen3-8B"
      status: "DOCUMENTED"
      parameter_class: "~8B"
      exact_parameters: "8.2B total; 6.95B non-embedding"
      license: "Apache-2.0"
      context_documented:
        native: 32768
        yarn_validated: 131072
      primary_role_hypothesis: "general executor with thinking/non-thinking profiles"
  efficient_3_4b_controls:
    - model: "Qwen/Qwen3-4B-Instruct-2507"
      status: "DOCUMENTED"
      parameters: "4.0B total; 3.6B non-embedding"
      context_documented: 262144
      role: "strong efficiency/tool-use control"
    - model: "mistralai/Ministral-3-3B-Instruct-2512"
      status: "DOCUMENTED"
      parameter_class: "~3B"
      role: "matched-family efficiency control"
    - model: "microsoft/Phi-4-mini-instruct"
      status: "DOCUMENTED"
      parameters: "3.8B"
      license: "MIT"
      context_documented: 128000
      role: "efficiency and ONNX runtime control"
  larger_12_14b_challengers:
    - model: "google/gemma-4-12B-it"
      status: "DOCUMENTED"
      parameters: "11.95B"
      license: "Apache-2.0"
      context_documented: 262144
      quantized_artifact: "google/gemma-4-12B-it-qat-q4_0-gguf"
      quantized_artifact_size_gb: 6.98
      role: "current 12B general/agentic challenger"
    - model: "mistralai/Ministral-3-14B-Instruct-2512"
      status: "DOCUMENTED"
      parameter_class: "~14B"
      license: "Apache-2.0"
      role: "matched-family larger challenger"
    - model: "mistralai/Ministral-3-14B-Reasoning-2512"
      status: "DOCUMENTED"
      parameter_class: "~14B"
      license: "Apache-2.0"
      role: "conditional difficult-reasoning challenger"
  over_14b_stretch_candidates:
    - model: "mistralai/Devstral-Small-2-24B-Instruct-2512"
      status: "INFERRED"
      parameter_class: "24B"
      license: "Apache-2.0"
      role: "coding-only stretch"
      rationale: "Official local guidance makes quantized 32K operation technically credible, but coexistence on the target 31.6 GB shared-memory laptop is unverified."
  coding_challengers:
    - model: "mistralai/Ministral-3-8B-Reasoning-2512"
      priority: 1
      rationale: "No size penalty relative to primary class; explicit coding/reasoning and native tool support."
    - model: "Qwen/Qwen3-8B"
      priority: 2
      rationale: "Thinking mode, coding capability and external-tool integration."
    - model: "Qwen/Qwen3-Coder-30B-A3B-Instruct"
      priority: 3
      rationale: "Agentic coding/browser specialist; resource-gated because total model size is ~30B despite ~3B active parameters."
    - model: "mistralai/Devstral-Small-2-24B-Instruct-2512"
      priority: 4
      rationale: "Purpose-built software-engineering specialist; test only if smaller profiles leave material CLI escalation."
  benchmark_priority:
    - "Ministral 3 8B Instruct / GGUF Q4_K_M / llama.cpp"
    - "Qwen3-8B / official GGUF comparable ~4-bit / llama.cpp"
    - "Ministral 3 8B Reasoning / GGUF Q4_K_M / llama.cpp"
    - "Ministral 3 3B Instruct / GGUF / llama.cpp"
    - "Qwen3-4B-Instruct-2507 / compatible ~4-bit representation"
    - "Phi-4-mini-instruct / official ONNX INT4"
    - "Gemma 4 12B-it / official QAT Q4_0 GGUF"
    - "Ministral 3 14B Instruct / official GGUF"
    - "Ministral 3 14B Reasoning / conditional"
    - "Qwen3-Coder-30B-A3B / coding-only resource-gated stretch"
    - "Devstral Small 2 24B / coding-only resource-gated stretch"
  excluded_or_deprioritized:
    - model: "microsoft/phi-4"
      reason: "DOCUMENTED: 16K context is below APEX ~32K target."
    - model: "mistralai/Ministral-8B-Instruct-2410"
      reason: "DOCUMENTED: deprecated and replaced by Ministral 3 8B."
    - model: "Gemma 3 family"
      reason: "INFERRED: superseded by current Gemma 4 generation for this research."
    - model: "Qwen2.5-Coder-7B"
      reason: "INFERRED: older coding generation; not required for the small current candidate set."
    - model: "Qwen/Qwen3-Coder-480B-A35B-Instruct"
      reason: "INFERRED: not locally plausible on target hardware."
    - model: "Qwen/Qwen3-Coder-Next"
      reason: "DOCUMENTED: 80B total parameters despite 3B active; INFERRED: incompatible with desired laptop coexistence without new memory evidence."
    - model: "google/gemma-4-26B-A4B"
      reason: "INFERRED: interesting MoE but unnecessary before 12B challenger evidence."
    - model: "google/gemma-4-E4B-it"
      reason: "DOCUMENTED: 4.5B effective but 8B including embeddings; INFERRED: parameter-class ambiguity makes it a secondary architectural-efficiency control."
  context_findings:
    apex_target: "~32K reliable working context; 64K stretch"
    advertised_context_is_not_certification: true
    primary_candidates_clear_32k_advertised_gate: true
    qwen3_8b_native_context: 32768
    qwen3_8b_yarn_validated_context: 131072
    ministral3_8b_context: 262144
    qwen3_4b_2507_context: 262144
    phi4_mini_context: 128000
    gemma4_12b_context: 262144
    required_local_tests:
      - 8192
      - 16384
      - 32768
      - 65536
    reliability_at_32k: null
  structured_tool_findings:
    ministral3_native_function_calling: true
    ministral3_json_output: true
    qwen3_documented_tool_integration: true
    qwen3_4b_2507_documented_tool_improvement: true
    phi4_mini_function_calling_format: true
    gemma4_native_function_calling: true
    llamacpp_schema_constrained_json: true
    llamacpp_function_calling: true
    semantic_tool_correctness: null
    authority_compliance: null
    prompt_injection_resistance: null
  windows_runtime_findings:
    preferred_reference_runtime_hypothesis: "llama.cpp"
    preferred_intel_optimized_challenger_hypothesis: "OpenVINO GenAI"
    llama_cpp:
      windows: true
      cpu: true
      intel_gpu_sycl: true
      vulkan: true
      hybrid_cpu_gpu: true
      schema_constrained_output: true
      tool_calling: true
    openvino_genai:
      windows: true
      intel_cpu_gpu_npu_targeting: true
      direct_gguf_for_supported_architectures: true
      newest_candidate_architecture_coverage: null
    phi4_mini_onnx:
      official_cpu_int4: true
      official_gpu_int4: true
    arc_140v_best_backend: null
    core_ultra_npu_usefulness_for_apex: null
  size_tradeoff_hypotheses:
    "3_4b":
      quality: "May absorb routine closed-state work but may fail more often on ambiguity, recovery and micro-coding."
      resources: "Expected best coexistence."
      status: "INFERRED"
    "7_8b":
      quality: "Expected practical optimum for bounded semantic execution."
      resources: "Expected workable balance on target laptop when quantized."
      status: "INFERRED"
    "12_14b":
      quality: "May improve difficult ambiguity, reasoning and coding."
      resources: "Higher KV/runtime/shared-memory and coexistence risk."
      promotion_rule: "Must materially reduce APEX failures/interventions/escalations."
      status: "INFERRED"
    "over_14b":
      quality: "Potentially useful only for specialized coding."
      resources: "High coexistence risk."
      status: "INFERRED"
  resource_unknowns:
    - "Peak committed and resident RAM by model/runtime/context."
    - "Arc 140V device/shared-memory pressure."
    - "NPU compatibility and useful generation performance."
    - "KV-cache footprint at 8K/16K/32K/64K."
    - "Model load/unload/switch latency."
    - "llama.cpp SYCL versus Vulkan versus OpenVINO performance."
    - "Browser/IDE/test coexistence impact."
    - "Claude Code/Codex coexistence impact."
    - "Quantization-quality loss for semantic tool trajectories."
  apex_benchmark_unknowns:
    - "Successful unauthorized actions."
    - "Unauthorized action attempts."
    - "Prompt-injection following."
    - "Wrong-root access."
    - "Scope drift."
    - "False-success rate."
    - "UNKNOWN-state correctness."
    - "Typed escalation correctness."
    - "Tool-selection and argument correctness."
    - "Structured-output validity."
    - "Micro-fix correctness."
    - "Ambiguous-bug restraint."
    - "Recovery success."
    - "Resume-without-duplication reliability."
    - "32K working-context reliability."
    - "64K stretch reliability."
    - "Human interventions per 100 jobs."
    - "CLI escalations per 100 jobs."
    - "Successful bounded jobs per wall time."
    - "Best planner-routed profile topology."
  overall_confidence_0_to_100: 84
```
