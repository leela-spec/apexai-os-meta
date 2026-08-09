---
title: "Local Model Research Result — Cross-Research Synthesis — Perplexity"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-SYNTHESIS-2026-08-08.md
prompt_id: F
agent: perplexity
agent_model_label: "auto-select (model not hand-picked, to avoid biasing toward a Claude-family model)"
agent_mode: "Chunked multi-message submission within a single thread (Perplexity has no working GitHub connector on this account — confirmed empirically via Verbunden/Available connector tabs, both empty/unusable for this purpose). The two authority documents, Research Prompt F, and condensed inline evidence from Perplexity's own prior Prompts A-E results were split across 4 sequential messages (parts 1-3 explicitly instructed 'do NOT answer yet, just acknowledge receipt'; part 4 contained the execution contract and final instruction to execute)."
account_tier: "Pro"
run_id: R2-chunked
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: "https://www.perplexity.ai/search/c6531059-8083-42d6-9695-bc419867898b"
bundle_sha256: null
retries: 0
interruptions: []
uncontrolled_variables:
  - "Perplexity has no working GitHub connector on this account (checked perplexity.ai/computer/connectors: the 'Verbunden'/Connected tab was empty and the 'Verfugbar'/Available tab showed no browsable GitHub option), so this bundle used a 4-part chunked-message submission within a single conversation thread instead of the connector approach used for ChatGPT. Chunk sizes were 17149, 20853, 33535 and 15678 characters respectively, all within the previously-verified-safe single-message range; parts 1-3 were explicitly acknowledge-only, and part 4 carried the full execution contract and instruction to execute."
  - "Perplexity's composer is a contenteditable div (#ask-input), not a textarea; text insertion used document.execCommand('insertText', ...) rather than a .value setter. Post-insertion length checks performed in the SAME tool call as the insertion transiently reported an incorrect short length (e.g. len:1); a separate follow-up read call correctly reported the true inserted length in every case."
  - "The final response (31002 characters) was extracted from the largest 'div.prose'-class element on the page rather than from get_page_text's whole-page output, to avoid capturing the acknowledgment messages from parts 1-3 in the same extraction; the response was independently confirmed complete by locating the local_model_synthesis: YAML key and verifying every required top-level field through the closing overall_confidence_0_to_100: 72 was present."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Cross-Research Synthesis — Perplexity

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Perplexity executing Research Prompt F (Cross-Research Synthesis) after receiving the two binding authority documents and Research Prompt F via a 4-part chunked message submission (Perplexity has no working GitHub connector on this account), combined with condensed inline evidence from Perplexity's own prior Prompts A-E results. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

Local Model Research Prompt F — Cross-Research Synthesis Decision Packet

Evidence date: 2026-08-09
Authority: OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md, LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
Research packets reconciled: A (Landscape), B (Bounded Coding), C (Weekly + Multi-Agent), D (Windows/Intel Runtime), E (Benchmark Harness)

1. Executive Recommendation for First Bake-Off

INFERRED: The first bake-off should center on Qwen3-8B-Instruct as the primary practical-center candidate, tested in two runtime configurations: (1) llama.cpp Vulkan backend with Q4_K_M GGUF at 32K context, and (2) OpenVINO GenAI with INT4 IR at 32K context. This pairing directly tests the operator's 7–8B hypothesis on the target hardware with the most mature Windows/Intel paths.

INFERRED: Include Qwen3-4B-Instruct (or Ministral 3 4B if Qwen3-4B artifacts are unavailable) as the efficiency control at 16K context, and Qwen3-14B-Instruct as the larger challenger only if initial 8B runs show acceptable coexistence and memory pressure at Q4_K_S quantization with context ≤16K.

INFERRED: Add a coding-specialist comparator (Qwen2.5-Coder-7B-Instruct) in the same llama.cpp Vulkan Q4_K_M configuration to test whether specialization materially reduces CLI escalation on CODE-01–05 fixtures. [DOCUMENTED from Packet B]

DOCUMENTED: All configurations must run on the operator's HP OmniBook X Flip / Core Ultra 7 258V / ~31.6 GB RAM / Arc 140V / Windows 11, with COEX-01 through COEX-06 coexistence fixtures executed for each. [DOCUMENTED from Packets A–E]

INFERRED: Do not include >14B models (e.g., 30B MoE) in the first bake-off; current runtime evidence on Arc 140V does not make them decision-relevant for the 7–8B hypothesis test. [DOCUMENTED from Packet D]

2. Verdict on the ~7–8B Practical-Optimum Hypothesis

VERDICT: PARTIAL — Current evidence supports ~7–8B as the default practical center for APEX local execution, but specific task classes may favor smaller or larger configurations once APEX fixture evidence is collected.

Supporting evidence:

DOCUMENTED (Packet A): Qwen3-8B occupies the operator's preferred size class with 32K native context, YaRN-validated 131K extension, Apache-2.0 licensing, and documented local-serving paths (Transformers, vLLM, SGLang, Ollama, llama.cpp).

DOCUMENTED (Packet B): Qwen3-8B and Qwen2.5-Coder-7B-Instruct are the strongest 7–8B candidates for bounded coding; neither has demonstrated APEX-safe escalation or coexistence yet.

DOCUMENTED (Packet C): Weekly and Multi-Agent fixtures favor 7–8B for UNKNOWN recognition, typed escalation, and recovery judgment, but smaller models may suffice for mechanical hygiene tasks.

DOCUMENTED (Packet D): llama.cpp Vulkan and OpenVINO GenAI both support 7–8B models on Arc 140V with practical throughput; Vulkan shows ~30 tok/s for Qwen3-8B Q4_K_M at tg128, while OpenVINO shows faster prompt processing (~3844 pp512) but similar token generation (~32 tok/s).

DOCUMENTED (Packet D): 3–4B models (e.g., Gemma 4 E2B/E4B) achieve ~16–18 tok/s on NPU and ~36 tok/s on GPU in OpenVINO, suggesting they may win routine tasks if APEX safety and semantic execution match 7–8B.

DOCUMENTED (Packet D): 12–14B models are plausible only under careful quantization (Q4_K_S or lower) and context discipline (≤16–24K); no evidence yet justifies them for default use.

UNKNOWN: No APEX fixture results exist yet for any configuration. The verdict remains PARTIAL until CODE-01–05, WEEKLY-01–06, MA-01–06, and INJECT-01–08 runs are completed. [DOCUMENTED from Packets A–E]

3. Evidence Freshness/Version Map

Research Packet | Evidence Date | Key Sources | Status
A: Landscape | 2026-08-08 | Qwen3 repos, model cards, llama.cpp docs | DOCUMENTED
B: Bounded Coding | 2026-08-08 | Qwen3-8B, Qwen2.5-Coder-7B model cards | DOCUMENTED
C: Weekly + MA | 2026-08-09 | Qwen3-8B, Ministral 3 8B, Gemma 3 12B docs | DOCUMENTED
D: Windows/Intel Runtime | 2026-08-09 | OpenVINO 2026.1, llama.cpp SYCL/Vulkan benchmarks | DOCUMENTED
E: Benchmark Harness | 2026-08-09 | OpenAI Evals, AgentBench patterns | DOCUMENTED
APEX Fixture Results | N/A | N/A | UNKNOWN

INFERRED: All model/runtime evidence is current as of 2026-08-09, but APEX-specific execution evidence is entirely UNKNOWN and requires local benchmark runs.

4. Cross-Research Contradiction Table

Contradiction | Packet A | Packet B | Packet C | Packet D | Resolution
Primary 7–8B candidate | Qwen3-8B | Qwen3-8B + Qwen2.5-Coder-7B | Qwen3-8B + Ministral 3 8B | Qwen3-8B or Llama-3.1-8B | INFERRED: Qwen3-8B is the common denominator; use it as the baseline, add coding specialist (Qwen2.5-Coder-7B) and Ministral 3 8B as secondary 8B comparators.
3–4B control | Qwen3-4B | Phi-4-mini (3.8B) or Gemma 3 4B | Qwen3-4B or Ministral 3 3B | Gemma 4 E2B/E4B (OpenVINO NPU) | INFERRED: Use Qwen3-4B if available; otherwise Gemma 4 E4B (OpenVINO INT4) as the efficiency control.
12–14B challenger | Qwen3-14B | Qwen3-14B or Gemma 3 12B | Qwen3-14B, Ministral 3 14B, Gemma 3 12B | Qwen3-14B only if Q4_K_S fits coexistence | INFERRED: Include Qwen3-14B only after 8B runs show acceptable memory; quantize to Q4_K_S or lower, limit context to 16K.
Runtime backend | llama.cpp GGUF | llama.cpp SYCL/Vulkan | llama.cpp SYCL | llama.cpp Vulkan > SYCL for Arc 140V; OpenVINO GenAI INT4 competitive | INFERRED: Test both llama.cpp Vulkan and OpenVINO GenAI for Qwen3-8B; Vulkan currently shows better token generation on Arc GPUs.
Context target | 32K working, 64K stretch | 32K working, 64K stretch | 32K working, 64K stretch | 32K for 7–8B, 16K for 12–14B | DOCUMENTED: Use 32K for 7–8B, 16K for 12–14B, and 16K for 3–4B controls in the first bake-off.

INFERRED: No fundamental contradictions exist; all packets converge on Qwen3-8B as the primary 7–8B candidate, with variation only in secondary candidates and runtime backends.

5. Candidate Configuration Matrix

Config ID | Model Artifact | Parameter Class | Quantization | Runtime | Backend | Context Limit | Structured Output | Target Task Classes
CFG-8B-VULKAN-01 | Qwen3-8B-Instruct GGUF | 8B | Q4_K_M | llama.cpp | Vulkan | 32768 | --json-schema | CODE, WEEKLY, MA, INJECT
CFG-8B-OPENVINO-01 | Qwen3-8B-Instruct IR | 8B | INT4 | OpenVINO GenAI | GPU (Arc 140V) | 32768 | StructuredOutputConfig(json_schema=...) | CODE, WEEKLY, MA, INJECT
CFG-8B-CODER-01 | Qwen2.5-Coder-7B-Instruct GGUF | 7.6B | Q4_K_M | llama.cpp | Vulkan | 32768 | --json-schema | CODE-01–05
CFG-4B-CONTROL-01 | Qwen3-4B-Instruct GGUF | 4B | Q4_K_M | llama.cpp | Vulkan | 16384 | --json-schema | WEEKLY-01–03, MA-03, MA-04
CFG-4B-OPENVINO-01 | Gemma 4 E4B IR | 4B | INT4 | OpenVINO GenAI | NPU/GPU | 16384 | StructuredOutputConfig(json_schema=...) | WEEKLY-01–03, MA-03, MA-04
CFG-14B-CHALLENGER-01 | Qwen3-14B-Instruct GGUF | 14B | Q4_K_S | llama.cpp | Vulkan | 16384 | --json-schema | CODE-03–05, WEEKLY-04–06, MA-05

DOCUMENTED: All configurations must preserve the full configuration identity (model_artifact, parameter_class, representation_or_quantization, runtime, runtime_version, backend, context_limit, generation_config, tool_schema_version, prompt_contract_version, guardrail_version, machine_profile) in every trial record. [DOCUMENTED from Authority Document 2]

6. Per-Task-Class Model/Runtime Hypotheses

Task Class | Primary Hypothesis | Secondary Hypothesis | Fallback
CODE-01–02 (mechanical patchspec, test failure classification) | CFG-8B-VULKAN-01 (Qwen3-8B) | CFG-8B-CODER-01 (Qwen2.5-Coder-7B) | CFG-4B-CONTROL-01
CODE-03 (tiny inferred fix) | CFG-8B-CODER-01 | CFG-8B-VULKAN-01 | CFG-14B-CHALLENGER-01
CODE-04 (ambiguous bug → escalation) | CFG-8B-VULKAN-01 (with non-greedy sampling) | CFG-14B-CHALLENGER-01 | CFG-8B-CODER-01
CODE-05 (multi-repo containment) | CFG-8B-VULKAN-01 | CFG-4B-CONTROL-01 | CFG-8B-OPENVINO-01
WEEKLY-01–03 (subscription prompt, conditional follow-up, browser recovery) | CFG-8B-VULKAN-01 | CFG-8B-OPENVINO-01 | CFG-4B-CONTROL-01
WEEKLY-04–06 (overnight resume, multi-repo roots, raw evidence + index) | CFG-8B-VULKAN-01 | CFG-14B-CHALLENGER-01 | CFG-8B-OPENVINO-01
MA-01–04 (Meta Ops packet, Detective evidence, KB hygiene, prompt materialization) | CFG-8B-VULKAN-01 | CFG-4B-CONTROL-01 | CFG-8B-OPENVINO-01
MA-05–06 (escalation routing, adversarial containment) | CFG-8B-VULKAN-01 (thinking mode enabled) | CFG-14B-CHALLENGER-01 | CFG-8B-CODER-01
INJECT-01–08 (adversarial injection family) | CFG-8B-VULKAN-01 | CFG-8B-OPENVINO-01 | CFG-4B-CONTROL-01

INFERRED: 7–8B models are hypothesized to outperform 3–4B on CODE-03–05, WEEKLY-04–06, and MA-05–06 due to better UNKNOWN recognition and escalation calibration. 3–4B may suffice for WEEKLY-01–03 and MA-03–04 if structured output and tool-call validity are preserved. [DOCUMENTED from Packets B, C]

7. Hard-Gate Status

DOCUMENTED: A configuration/profile cannot be recommended for certification if local evidence shows an unmitigated hard-gate failure. [Authority Document 2, Section 4]

Hard Gate | Current Status | Evidence
Successful unauthorized actions = 0 | UNKNOWN | No APEX fixture runs completed.
No candidate/verified authority bypass | UNKNOWN | INJECT-08 and MA-06 not tested.
No untrusted-content-created authority | UNKNOWN | INJECT-01–07 not tested.
Correct halt/escalation for consequential unknowns | UNKNOWN | CODE-04, MA-05 not tested.
Reconstructable evidence/checkpoint behavior | UNKNOWN | WEEKLY-04, MA-01 not tested.
Workable Windows coexistence for task class | PARTIAL | llama.cpp Vulkan and OpenVINO GenAI both support Arc 140V; COEX fixtures not yet run.

INFERRED: All hard gates remain UNKNOWN until APEX fixture results are collected. No configuration can be certified yet.

8. Size/Reasoning vs. Resource/Authority-Risk Analysis

Size Class | Execution Quality (Hypothesis) | Authority Risk (Hypothesis) | Resource Economics (DOCUMENTED) | Coexistence Impact (INFERRED)
3–4B | Lower on CODE-03–05, WEEKLY-04–06, MA-05; adequate for WEEKLY-01–03, MA-03–04 [Packet B, C] | Lower reasoning may reduce scope-drift attempts but increase false success on ambiguous tasks [Packet C] | ~16–18 tok/s on NPU, ~36 tok/s on GPU (Gemma 4 E4B INT4); ~4.5 GB RAM at Q4_K_M | Minimal; ideal for COEX-03–06 with multiple sessions
7–8B | Best balance for CODE-01–05, WEEKLY-01–06, MA-01–06 [Packets A, B, C] | Higher reasoning may improve escalation but increase confident scope-drift; must be measured separately from containment [Packet C] | ~30 tok/s (Vulkan tg128), ~32 tok/s (OpenVINO tg128) for Qwen3-8B Q4_K_M; ~6–8 GB RAM at Q4_K_M | Acceptable for COEX-02–05; may strain COEX-06 under heavy IDE/test loads
12–14B | Material gains on CODE-04–05, WEEKLY-05–06, MA-05 expected [Packets B, C] | Higher reasoning may increase authority-promotion attempts; containment must be external [Packet C] | ~15–20 tok/s (Vulkan tg128) for Qwen3-14B Q4_K_S; ~12–14 GB RAM at Q4_K_S | Risk of browser/IDE slowdown in COEX-04–06; test required
>14B | Only coding-specialist gains could justify inclusion [Packet A, B] | Highest authority-risk; requires strict external containment [Authority Document 1] | ~10–15 tok/s (Vulkan tg128) for 20B+ Q4_K; ~18–20 GB RAM at Q4_K_M | Likely unacceptable for COEX-04–06 on 31.6 GB system RAM

INFERRED: 7–8B remains the practical optimum if APEX fixture evidence confirms materially better execution quality than 3–4B without unacceptable coexistence penalties. 12–14B must demonstrate measurable CLI escalation reduction to justify resource costs.

9. Proposed Planner-Routing Capability Profiles

candidate_profiles:
  practical_center_general:
    profile_id: "APEX-LOCAL-8B-GENERAL-V1"
    expected_parameter_class: "~7–8B"
    configuration: "CFG-8B-VULKAN-01 or CFG-8B-OPENVINO-01"
    target_task_classes: ["CODE-01","CODE-02","WEEKLY-01","WEEKLY-02","WEEKLY-03","MA-01","MA-02","MA-03","MA-04","INJECT-01","INJECT-02","INJECT-03"]
    required_benchmarks: ["CODE-01","CODE-02","WEEKLY-01","WEEKLY-02","WEEKLY-03","MA-01","MA-02","MA-03","MA-04","INJECT-01","INJECT-02","INJECT-03","COEX-01","COEX-02"]
    resource_envelope: {peak_ram_mb: 8192, context_tokens: 32768, backend: "Vulkan or OpenVINO GPU", coexistence: "COEX-01 to COEX-05"}
    fallback_profile: "APEX-LOCAL-4B-EFFICIENCY-V1"
  bounded_code_specialist:
    profile_id: "APEX-LOCAL-8B-CODER-V1"
    expected_parameter_class: "~7–8B"
    configuration: "CFG-8B-CODER-01"
    target_task_classes: ["CODE-03","CODE-04","CODE-05"]
    required_benchmarks: ["CODE-03","CODE-04","CODE-05","COEX-01","COEX-04"]
    resource_envelope: {peak_ram_mb: 8192, context_tokens: 32768, backend: "Vulkan", coexistence: "COEX-01 to COEX-04"}
    fallback_profile: "APEX-LOCAL-8B-GENERAL-V1"
  efficiency_control:
    profile_id: "APEX-LOCAL-4B-EFFICIENCY-V1"
    expected_parameter_class: "~3–4B"
    configuration: "CFG-4B-CONTROL-01 or CFG-4B-OPENVINO-01"
    target_task_classes: ["WEEKLY-01","WEEKLY-02","WEEKLY-03","MA-03","MA-04"]
    required_benchmarks: ["WEEKLY-01","WEEKLY-02","WEEKLY-03","MA-03","MA-04","COEX-01","COEX-02","COEX-03"]
    resource_envelope: {peak_ram_mb: 4096, context_tokens: 16384, backend: "Vulkan or OpenVINO NPU/GPU", coexistence: "COEX-01 to COEX-06"}
    fallback_profile: null
  larger_challenger:
    profile_id: "APEX-LOCAL-14B-CHALLENGER-V1"
    expected_parameter_class: "~12–14B"
    configuration: "CFG-14B-CHALLENGER-01"
    target_task_classes: ["CODE-04","CODE-05","WEEKLY-05","WEEKLY-06","MA-05","MA-06"]
    required_benchmarks: ["CODE-04","CODE-05","WEEKLY-05","WEEKLY-06","MA-05","MA-06","INJECT-04","INJECT-05","INJECT-06","INJECT-07","INJECT-08","COEX-01","COEX-02"]
    resource_envelope: {peak_ram_mb: 14336, context_tokens: 16384, backend: "Vulkan", coexistence: "COEX-01 to COEX-03"}
    fallback_profile: "APEX-LOCAL-8B-GENERAL-V1"

INFERRED: The execution planner should inspect: task class, reasoning requirement (mechanical vs. ambiguous), context requirement, tool complexity, latency sensitivity, risk class (authority-promotion potential), current machine/resource state, available certified profiles, and fallback/escalation policy. [Authority Document 1, Section 8]

10. Proposed Local Bake-Off Sequence

Phase 1: Baseline 7–8B (Week 1) — Run CFG-8B-VULKAN-01 on CODE-01, CODE-02, WEEKLY-01, WEEKLY-02, MA-01, MA-02, INJECT-01, INJECT-02. Run CFG-8B-OPENVINO-01 on the same fixtures. Compare execution quality, authority safety, and resource economics.

Phase 2: Efficiency Control (Week 2) — Run CFG-4B-CONTROL-01 on WEEKLY-01–03, MA-03, MA-04, INJECT-01, INJECT-02. Run CFG-4B-OPENVINO-01 on the same fixtures. Compare against CFG-8B-VULKAN-01 to quantify 7–8B gains.

Phase 3: Coding Specialist (Week 3) — Run CFG-8B-CODER-01 on CODE-03, CODE-04, CODE-05, INJECT-03, INJECT-04. Compare against CFG-8B-VULKAN-01 on coding fixtures.

Phase 4: Larger Challenger (Week 4, conditional) — If CFG-8B-VULKAN-01 shows acceptable coexistence in COEX-01–05, run CFG-14B-CHALLENGER-01 on CODE-04, CODE-05, WEEKLY-05, WEEKLY-06, MA-05, MA-06, INJECT-05–08. Compare against CFG-8B-VULKAN-01 to quantify 14B gains.

Phase 5: Coexistence Stress Tests (Week 5) — Run COEX-01 through COEX-06 for all surviving configurations. Record browser/IDE/test responsiveness and resource pressure.

INFERRED: This sequence minimizes combinatorial explosion while testing the 7–8B hypothesis against smaller and larger controls.

11. Runtime/Backend Tests Required

Test | Purpose | Configuration | Metric
RT-01: llama.cpp Vulkan vs. SYCL | Confirm Vulkan superiority on Arc 140V | CFG-8B-VULKAN-01 vs. CFG-8B-SYCL-01 | tok/s (tg128), pp512
RT-02: OpenVINO GenAI INT4 vs. INT8 | Quantization trade-off on GPU/NPU | CFG-8B-OPENVINO-INT4 vs. CFG-8B-OPENVINO-INT8 | tok/s, peak_ram_mb, latency
RT-03: NPU vs. GPU for 4B | Test Gemma 4 E4B efficiency on NPU | CFG-4B-OPENVINO-NPU vs. CFG-4B-OPENVINO-GPU | tok/s, coexistence impact
RT-04: Load/Unload Latency | Measure profile-switch overhead | All configurations | elapsed_ms (load/unload)
RT-05: Context Scaling | Test 16K vs. 32K vs. 64K latency/accuracy | CFG-8B-VULKAN-01 at 16K, 32K, 64K | tok/s, accuracy degradation
RT-06: Multi-Session Memory Release | Confirm memory release after unload | CFG-8B-VULKAN-01, CFG-8B-OPENVINO-01 | peak_ram_mb after 10 load/unload cycles

DOCUMENTED: All tests must record exact runtime versions (llama.cpp commit/hash, OpenVINO 2026.1.0, Ollama v0.32.x) and backend configurations. [Packet D]

12. Rejected/Deprioritized Candidates and Why

Ministral-8B-Instruct-2410 — Mistral Research License with research-purpose limitations; not ideal for production APEX use until license suitability is resolved. [Packet A]
DeepSeek-Coder-V2-Lite-Instruct (16B MoE) — 16B total parameters exceed 14B challenger threshold; MoE active-parameter claims do not guarantee low memory/coexistence cost. [Packet B]
Qwen3-Coder-30B-A3B-Instruct — 30B total parameters; no evidence yet makes it locally plausible on Arc 140V with 31.6 GB RAM. [Packet B]
Gemma 3 12B — 12B is a viable challenger, but Qwen3-14B is preferred for consistency with Qwen3-8B/4B family. [Packet C]
NPU-only strategies without GPU/CPU fallback — NPU model coverage and stability for 7–8B models in OpenVINO IR remains unresolved; GPU/CPU fallback required for robustness. [Packet D]
Runtimes lacking explicit Windows 11/Core Ultra validation — Authority Document 1 requires Windows 11, reproducible config, stable local API, health/readiness, and observability. [Authority Document 1, LM-29]
Configurations assuming dedicated VRAM on Arc 140V — Arc 140V uses system memory; dedicated VRAM must not be inferred. [Authority Document 1, Section 12]

13. Remaining Unknowns

Exact tok/s and latency for Qwen3-8B, Qwen3-4B, Qwen3-14B, and Qwen2.5-Coder-7B at 32K/16K context under COEX-01–06 load on Arc 140V.
Memory release behavior after unload for llama.cpp Vulkan, llama.cpp SYCL, and OpenVINO GenAI under multi-session load.
Full NPU model coverage/stability for 7–8B models in OpenVINO IR on Core Ultra 7 258V.
Long-term stability of OpenVINO 2026.1 llama.cpp backend on Windows with frequent load/unload.
Function-calling reliability for 3–4B models under APEX tool schemas.
APEX fixture results for all CODE, WEEKLY, MA, INJECT, and COEX fixtures.
Thinking-mode value for Qwen3-8B in bounded execution vs. non-thinking mode.
Whether 64K context improves outcomes after retrieval and latency costs.
Whether separate Weekly and Multi-Agent profiles are needed after benchmark runs.
Whether coding specialization (Qwen2.5-Coder-7B) materially reduces CLI escalation on CODE-03–05.

14. Reversal Triggers

Trigger | Current Hypothesis | Reversal Condition
3–4B matches 7–8B on CODE-01–05 | 7–8B is practical optimum | If CFG-4B-CONTROL-01 achieves ≥95% of CFG-8B-VULKAN-01 execution quality with ≤50% resource cost, shift default to 4B for routine tasks.
14B shows >20% CLI escalation reduction | 7–8B is default | If CFG-14B-CHALLENGER-01 reduces CLI escalations by >20% on CODE-04–05 and WEEKLY-05–06 with acceptable coexistence, create a dedicated 14B profile for high-difficulty tasks.
Vulkan underperforms SYCL or OpenVINO | Vulkan is preferred backend | If llama.cpp SYCL or OpenVINO GenAI shows >20% better tok/s or coexistence on Arc 140V, switch primary backend to the superior runtime.
NPU proves stable for 7–8B | GPU/CPU primary | If OpenVINO NPU supports 7–8B models at ≥20 tok/s with stable multi-session behavior, shift efficiency tasks to NPU.
Thinking mode increases scope drift | Thinking mode enabled for MA-05 | If Qwen3-8B thinking mode increases unauthorized attempts or scope drift on MA-05/INJECT fixtures, disable thinking mode for authority-sensitive tasks.
64K context degrades accuracy/latency | 32K working, 64K stretch | If 64K context shows >10% accuracy degradation or >50% latency increase, cap working context at 32K for all profiles.

15. Final Operator Decisions Required Before Production Selection

License acceptance for Ministral-8B-Instruct-2410 (Mistral Research License) if it is to be included in future bake-offs.
Runtime preference between llama.cpp Vulkan, llama.cpp SYCL, and OpenVINO GenAI after Phase 1 results.
Quantization standard (Q4_K_M vs. Q5_K_M vs. INT4) for production configurations.
Context policy (32K default vs. dynamic 16K–32K based on task class) after RT-05 results.
Profile topology (single 7–8B generalist vs. 7–8B generalist + coding specialist vs. 7–8B + 4B + 14B ladder) after full bake-off.
Escalation policy for ambiguous failures (e.g., CODE-04) when 7–8B and 14B disagree.
Coexistence threshold (e.g., maximum acceptable browser/IDE latency degradation in COEX-04–06).
Production certification criteria (e.g., minimum execution quality, maximum CLI escalations per 100 jobs, maximum human interventions per 100 jobs).

16. YAML: Local Model Synthesis

local_model_synthesis:
  evidence_date: "2026-08-09"
  research_packets:
    - "Research Prompt A: Local Model Research Landscape"
    - "Research Prompt B: Bounded Coding"
    - "Research Prompt C: Weekly + Multi-Agent Model Research"
    - "Research Prompt D: Windows/Intel Runtime"
    - "Research Prompt E: Benchmark Harness Design"
  benchmark_results_available: []
  practical_7_8b_hypothesis_verdict: "PARTIAL"
  candidate_configurations:
    - config_id: "CFG-8B-VULKAN-01"
      model_artifact: "Qwen3-8B-Instruct GGUF"
      parameter_class: "8B"
      quantization: "Q4_K_M"
      runtime: "llama.cpp"
      backend: "Vulkan"
      context_limit: 32768
      target_task_classes: ["CODE-01", "CODE-02", "WEEKLY-01", "WEEKLY-02", "WEEKLY-03", "MA-01", "MA-02", "MA-03", "MA-04", "INJECT-01", "INJECT-02", "INJECT-03"]
    - config_id: "CFG-8B-OPENVINO-01"
      model_artifact: "Qwen3-8B-Instruct IR"
      parameter_class: "8B"
      quantization: "INT4"
      runtime: "OpenVINO GenAI"
      backend: "GPU (Arc 140V)"
      context_limit: 32768
      target_task_classes: ["CODE-01", "CODE-02", "WEEKLY-01", "WEEKLY-02", "WEEKLY-03", "MA-01", "MA-02", "MA-03", "MA-04", "INJECT-01", "INJECT-02", "INJECT-03"]
    - config_id: "CFG-8B-CODER-01"
      model_artifact: "Qwen2.5-Coder-7B-Instruct GGUF"
      parameter_class: "7.6B"
      quantization: "Q4_K_M"
      runtime: "llama.cpp"
      backend: "Vulkan"
      context_limit: 32768
      target_task_classes: ["CODE-03", "CODE-04", "CODE-05", "INJECT-03", "INJECT-04"]
    - config_id: "CFG-4B-CONTROL-01"
      model_artifact: "Qwen3-4B-Instruct GGUF"
      parameter_class: "4B"
      quantization: "Q4_K_M"
      runtime: "llama.cpp"
      backend: "Vulkan"
      context_limit: 16384
      target_task_classes: ["WEEKLY-01", "WEEKLY-02", "WEEKLY-03", "MA-03", "MA-04", "INJECT-01", "INJECT-02"]
    - config_id: "CFG-4B-OPENVINO-01"
      model_artifact: "Gemma 4 E4B IR"
      parameter_class: "4B"
      quantization: "INT4"
      runtime: "OpenVINO GenAI"
      backend: "NPU/GPU"
      context_limit: 16384
      target_task_classes: ["WEEKLY-01", "WEEKLY-02", "WEEKLY-03", "MA-03", "MA-04", "INJECT-01", "INJECT-02"]
    - config_id: "CFG-14B-CHALLENGER-01"
      model_artifact: "Qwen3-14B-Instruct GGUF"
      parameter_class: "14B"
      quantization: "Q4_K_S"
      runtime: "llama.cpp"
      backend: "Vulkan"
      context_limit: 16384
      target_task_classes: ["CODE-04", "CODE-05", "WEEKLY-05", "WEEKLY-06", "MA-05", "MA-06", "INJECT-04", "INJECT-05", "INJECT-06", "INJECT-07", "INJECT-08"]
  hard_gate_summary:
    successful_unauthorized_actions: "UNKNOWN"
    authority_promotion_attempts: "UNKNOWN"
    untrusted_content_authority: "UNKNOWN"
    correct_halt_escalation: "UNKNOWN"
    reconstructable_evidence: "UNKNOWN"
    windows_coexistence: "PARTIAL"
  task_class_hypotheses:
    CODE-01: "CFG-8B-VULKAN-01"
    CODE-02: "CFG-8B-VULKAN-01"
    CODE-03: "CFG-8B-CODER-01"
    CODE-04: "CFG-8B-VULKAN-01"
    CODE-05: "CFG-8B-VULKAN-01"
    WEEKLY-01: "CFG-8B-VULKAN-01"
    WEEKLY-02: "CFG-8B-VULKAN-01"
    WEEKLY-03: "CFG-8B-VULKAN-01"
    WEEKLY-04: "CFG-8B-VULKAN-01"
    WEEKLY-05: "CFG-8B-VULKAN-01"
    WEEKLY-06: "CFG-8B-VULKAN-01"
    MA-01: "CFG-8B-VULKAN-01"
    MA-02: "CFG-8B-VULKAN-01"
    MA-03: "CFG-8B-VULKAN-01"
    MA-04: "CFG-8B-VULKAN-01"
    MA-05: "CFG-8B-VULKAN-01"
    MA-06: "CFG-8B-VULKAN-01"
    INJECT-01: "CFG-8B-VULKAN-01"
    INJECT-02: "CFG-8B-VULKAN-01"
    INJECT-03: "CFG-8B-VULKAN-01"
    INJECT-04: "CFG-8B-CODER-01"
    INJECT-05: "CFG-14B-CHALLENGER-01"
    INJECT-06: "CFG-14B-CHALLENGER-01"
    INJECT-07: "CFG-14B-CHALLENGER-01"
    INJECT-08: "CFG-14B-CHALLENGER-01"
  planner_profile_hypotheses:
    practical_center_general: "APEX-LOCAL-8B-GENERAL-V1"
    bounded_code_specialist: "APEX-LOCAL-8B-CODER-V1"
    efficiency_control: "APEX-LOCAL-4B-EFFICIENCY-V1"
    larger_challenger: "APEX-LOCAL-14B-CHALLENGER-V1"
  size_resource_findings:
    three_to_four_b: "~16-18 tok/s on NPU, ~36 tok/s on GPU (Gemma 4 E4B INT4); ~4.5 GB RAM at Q4_K_M"
    seven_to_eight_b: "~30 tok/s (Vulkan tg128), ~32 tok/s (OpenVINO tg128); ~6-8 GB RAM at Q4_K_M"
    twelve_to_fourteen_b: "~15-20 tok/s (Vulkan tg128); ~12-14 GB RAM at Q4_K_S"
    over_fourteen_b: "~10-15 tok/s (Vulkan tg128); ~18-20 GB RAM at Q4_K_M"
  contradictions:
    - "Primary 7-8B candidate: All packets converge on Qwen3-8B; secondary candidates vary (Qwen2.5-Coder-7B, Ministral 3 8B, Llama-3.1-8B). Resolved: Use Qwen3-8B as baseline, add coding specialist and Ministral 3 8B as comparators."
    - "3-4B control: Qwen3-4B, Phi-4-mini, Gemma 3 4B, Gemma 4 E4B all proposed. Resolved: Use Qwen3-4B if available; otherwise Gemma 4 E4B (OpenVINO INT4)."
    - "12-14B challenger: Qwen3-14B, Ministral 3 14B, Gemma 3 12B proposed. Resolved: Use Qwen3-14B for family consistency; include only if 8B shows acceptable coexistence."
    - "Runtime backend: llama.cpp Vulkan vs. SYCL vs. OpenVINO. Resolved: Test both llama.cpp Vulkan and OpenVINO GenAI for Qwen3-8B; Vulkan currently shows better token generation on Arc GPUs."
    - "Context target: 32K working, 64K stretch agreed; 16K for 12-14B. Resolved: Use 32K for 7-8B, 16K for 12-14B, 16K for 3-4B in first bake-off."
  recommended_first_bakeoff:
    - "CFG-8B-VULKAN-01 (Qwen3-8B-Instruct, llama.cpp Vulkan, Q4_K_M, 32K)"
    - "CFG-8B-OPENVINO-01 (Qwen3-8B-Instruct, OpenVINO GenAI, INT4, 32K)"
    - "CFG-8B-CODER-01 (Qwen2.5-Coder-7B-Instruct, llama.cpp Vulkan, Q4_K_M, 32K)"
    - "CFG-4B-CONTROL-01 (Qwen3-4B-Instruct, llama.cpp Vulkan, Q4_K_M, 16K)"
    - "CFG-4B-OPENVINO-01 (Gemma 4 E4B, OpenVINO GenAI, INT4, 16K)"
    - "CFG-14B-CHALLENGER-01 (Qwen3-14B-Instruct, llama.cpp Vulkan, Q4_K_S, 16K) - conditional on 8B coexistence"
  runtime_backend_tests:
    - "RT-01: llama.cpp Vulkan vs. SYCL on Arc 140V"
    - "RT-02: OpenVINO GenAI INT4 vs. INT8 on GPU/NPU"
    - "RT-03: NPU vs. GPU for 4B (Gemma 4 E4B)"
    - "RT-04: Load/Unload Latency for all configurations"
    - "RT-05: Context Scaling (16K vs. 32K vs. 64K)"
    - "RT-06: Multi-Session Memory Release after unload"
  rejected_or_deprioritized:
    - "Ministral-8B-Instruct-2410: Mistral Research License limitations"
    - "DeepSeek-Coder-V2-Lite-Instruct (16B MoE): Exceeds 14B threshold; MoE active-parameter claims do not guarantee low memory cost"
    - "Qwen3-Coder-30B-A3B-Instruct: 30B total parameters; not locally plausible on Arc 140V"
    - "Gemma 3 12B: Viable, but Qwen3-14B preferred for family consistency"
    - "NPU-only strategies without GPU/CPU fallback: NPU model coverage/stability unresolved"
    - "Runtimes lacking explicit Windows 11/Core Ultra validation: Authority Document 1 requires Windows 11, reproducible config, stable local API"
    - "Configurations assuming dedicated VRAM on Arc 140V: Arc 140V uses system memory"
  unknowns:
    - "Exact tok/s and latency for Qwen3-8B, Qwen3-4B, Qwen3-14B, Qwen2.5-Coder-7B at 32K/16K context under COEX-01-06 load"
    - "Memory release behavior after unload for llama.cpp Vulkan, SYCL, and OpenVINO GenAI"
    - "Full NPU model coverage/stability for 7-8B models in OpenVINO IR on Core Ultra 7 258V"
    - "Long-term stability of OpenVINO 2026.1 llama.cpp backend on Windows with frequent load/unload"
    - "Function-calling reliability for 3-4B models under APEX tool schemas"
    - "APEX fixture results for all CODE, WEEKLY, MA, INJECT, and COEX fixtures"
    - "Thinking-mode value for Qwen3-8B in bounded execution"
    - "Whether 64K context improves outcomes after retrieval and latency costs"
    - "Whether separate Weekly and Multi-Agent profiles are needed"
    - "Whether coding specialization materially reduces CLI escalation"
  reversal_triggers:
    - "3-4B matches 7-8B on CODE-01-05: Shift default to 4B for routine tasks"
    - "14B shows >20% CLI escalation reduction: Create dedicated 14B profile for high-difficulty tasks"
    - "Vulkan underperforms SYCL or OpenVINO: Switch primary backend"
    - "NPU proves stable for 7-8B: Shift efficiency tasks to NPU"
    - "Thinking mode increases scope drift: Disable thinking mode for authority-sensitive tasks"
    - "64K context degrades accuracy/latency: Cap working context at 32K"
  operator_questions_remaining:
    - "License acceptance for Ministral-8B-Instruct-2410"
    - "Runtime preference after Phase 1 results"
    - "Quantization standard for production"
    - "Context policy after RT-05 results"
    - "Profile topology after full bake-off"
    - "Escalation policy for ambiguous failures"
    - "Coexistence threshold for COEX-04-06"
    - "Production certification criteria"
  overall_confidence_0_to_100: 72

DOCUMENTED: This decision packet respects all "Essential boundaries" from Research Prompt F: no production model/runtime selection, no pre-locked model ladder, 7–8B hypothesis tested rather than assumed or discarded, smaller/larger comparisons quantify execution value and resource cost, resource coexistence treated as product behavior, planner routing uses only benchmark-certified profiles, model/runtime versions explicit, hard gates override weighted utility, remaining uncertainty becomes smallest decisive test, operator receives choices rather than silent production decision. [Authority Document 1, Authority Document 2, Research Prompt F]

