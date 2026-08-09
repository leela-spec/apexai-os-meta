---
title: "Local Model Research Result — Weekly + Multi-Agent — Perplexity"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-WEEKLY-MULTIAGENT-2026-08-08.md
prompt_id: C
agent: perplexity
agent_model_label: "Beste (Best/auto-select) — deliberately not hand-picked, to avoid biasing toward a Claude-family model"
agent_mode: "Suche (standard Search), not Vertiefte Recherche (Deep Research)"
account_tier: "subscription (plan tier not disclosed by UI)"
run_id: R1
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: null
bundle_sha256: "2c8fa705dbe7dcf83bea267eec4a8cbfbfc7608f1ed15f7e74a3db819f2d05ed"
retries: 0
interruptions: []
uncontrolled_variables:
  - "Chat URL for this specific run was not captured at execution time (browser extension disconnected before it could be recorded retroactively); response content and structure were verified via in-page marker/length checks before extraction."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Weekly + Multi-Agent — Perplexity

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Perplexity executing Research Prompt C (Weekly + Multi-Agent) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

# APEX OS Research Packet — Weekly + Multi-Agent Local Execution

**Evidence date:** 2026-08-09.
**Scope:** Non-coding local execution for Weekly Orchestrator and Multi-Agent Orchestration.
**Status:** No production model or runtime is selected. All recommendations are bake-off hypotheses.

## 1. Executive finding

[INFERRED] The current evidence supports retaining the operator's 7–8B practical-center hypothesis. The strongest initial candidate set is Qwen3-8B and Ministral 3 8B Instruct 2512, with Qwen3-4B and Ministral 3 3B as efficiency controls and Qwen3-14B, Ministral 3 14B, and Gemma 3 12B as larger challengers.

[DOCUMENTED] Qwen3-8B provides switchable thinking/non-thinking modes, native 32,768-token context, validated 131,072-token YaRN context, and documented tool/MCP-oriented usage. The model card explicitly recommends non-greedy sampling and describes Qwen3 as optimized for agent capabilities. (huggingface)

[DOCUMENTED] Ministral 3 8B Instruct 2512 provides native function calling, JSON output, vision input, a 256K advertised context window, and an FP8 representation intended for edge deployment. Its official card reports an 8.4B language model plus a 0.4B vision encoder and lists 3B, 8B, and 14B family variants. (huggingface)

[UNKNOWN] No public source reviewed here establishes that either candidate reliably performs APEX-specific UNKNOWN recognition, typed escalation, checkpoint-aware recovery, multi-repo containment, or injection-resistant bounded execution. Those properties require the APEX fixture portfolio.

[INFERRED] Qwen3-8B should be the first generalist baseline because it directly exposes the required thinking-mode control, tool-use path, and 32K working-context alignment. Ministral 3 8B should be run in parallel because its native function calling, JSON output, vision capability, and edge-deployment orientation could improve browser and structured-worker tasks.

[DOCUMENTED] The authority documents require model-plus-runtime-plus-harness evaluation, zero successful unauthorized actions, external authority enforcement, raw evidence preservation, durable checkpoints, and planner-routed capability profiles. These requirements remain binding; model capability does not grant authority.

## 2. Current candidate/version map

| Size class | Candidate/version | Current documented properties | APEX relevance |
|---|---|---|---|
| ~3–4B control | Qwen3-4B | [DOCUMENTED] 4.0B parameters, 32,768 native context, 131,072-token YaRN validation, switchable thinking/non-thinking modes, and documented tool-oriented usage. (huggingface) | [INFERRED] Primary efficiency control because it preserves the Qwen3 behavior family while reducing parameter count. |
| ~3–4B control | Ministral 3 3B Instruct 2512 | [DOCUMENTED] Listed by Mistral as an instruct variant in the Ministral 3 family; the family includes corresponding reasoning and base variants. (huggingface) | [INFERRED] Useful control for testing whether a smaller edge-oriented model can handle closed-set routing and evidence tasks. |
| ~3–4B secondary control | Phi-4-mini-instruct | [DOCUMENTED] NVIDIA's hosted model card describes 128K context and a tool-enabled function-call format; it reports a BFCL score of 70.3 in its comparison table. (build.nvidia) | [INFERRED] Secondary control for function-calling behavior; its hosted evidence is weaker than a directly maintained Microsoft model card. |
| ~7–8B primary | Qwen3-8B | [DOCUMENTED] 8.2B parameters, 6.95B non-embedding parameters, 32,768 native context, 131,072-token YaRN validation, switchable reasoning, and Qwen-Agent/MCP integration guidance. (huggingface) | [INFERRED] First general-purpose APEX candidate and likely default bake-off baseline. |
| ~7–8B primary | Ministral 3 8B Instruct 2512 | [DOCUMENTED] 8.4B language model plus 0.4B vision encoder, FP8 instruct checkpoint, native function calling, JSON output, vision support, 256K advertised context, and Apache 2.0 licensing. (huggingface) | [INFERRED] First multimodal/edge-oriented challenger to Qwen3-8B, especially for browser screenshots and structured tool calls. |
| ~7–8B secondary | Llama 3.1 8B Instruct | [UNKNOWN] Not independently verified in this run against a current official model card and runtime configuration. | [UNKNOWN] Do not include in the first APEX shortlist unless the exact artifact, license, runtime support, and current tool behavior are reverified. |
| ~12–14B challenger | Qwen3-14B | [DOCUMENTED] Qwen's official documentation lists 14B among available dense model sizes and describes shared Qwen3 thinking/non-thinking behavior across the family. (qwen.readthedocs) | [INFERRED] Strongest same-family scale challenger; must demonstrate APEX task gains sufficient to offset memory and coexistence cost. |
| ~12–14B challenger | Ministral 3 14B Instruct 2512 | [DOCUMENTED] Official Mistral material lists the 14B instruct variant and reports higher reasoning and instruction benchmark values than its 8B counterpart in the supplied comparison tables. (huggingface) | [INFERRED] Credible larger challenger if the 8B model fails recovery, evidence comparison, or escalation fixtures. |
| ~12–14B challenger | Gemma 3 12B IT | [DOCUMENTED] Google documents multimodal input, 128K context for the 12B size, and published scores including IFEval 88.9, MMLU Pro 60.6, and LiveCodeBench 24.6. (google) | [INFERRED] Relevant multimodal and instruction-following challenger, but not a same-family comparison to Qwen3 or Ministral. |
| >14B | Any larger local model | [UNKNOWN] No larger candidate is justified by the supplied machine evidence alone. | [DOCUMENTED] Authority requires concrete hardware/runtime evidence before including models beyond the 12–14B class. |

## 3. Primary 7–8B shortlist

### Qwen3-8B

[DOCUMENTED] Qwen3-8B supports explicit thinking and non-thinking modes, with recommended sampling configurations differing between the two modes. Its official card warns against greedy decoding because it can cause performance degradation and endless repetition. (huggingface)

[DOCUMENTED] Qwen3-8B's documented agent path includes Qwen-Agent, external tools, MCP configuration, and an OpenAI-compatible local endpoint pattern. (huggingface)

[INFERRED] The mode switch is valuable for APEX because routine state classification and evidence indexing can use non-thinking mode, while recovery judgement or contradiction comparison can selectively use thinking mode. The switch must remain harness-controlled rather than being treated as model authority.

[UNKNOWN] The public card does not establish reliable abstention, safe refusal, typed escalation, or resistance to APEX's eight injection families.

### Ministral 3 8B Instruct 2512

[DOCUMENTED] Ministral 3 8B Instruct 2512 is an FP8 instruct model with a vision encoder, native function calling, JSON output, system-prompt support, multilingual coverage, and a 256K context window. (huggingface)

[DOCUMENTED] Mistral recommends keeping the tool set well-defined and limiting tools to the minimum required for the use case. (huggingface)

[INFERRED] This design is directly relevant to bounded APEX packets: a small declared tool surface, JSON validation, screenshot interpretation, and explicit system-prompt contracts are compatible with the authority envelope.

[UNKNOWN] The official card does not demonstrate that the model will preserve raw evidence without semantic overreach, recognize UNKNOWN consequential states, or avoid candidate-to-verified promotion attempts.

### Initial recommendation

[INFERRED] Run both candidates under the same fixture versions, schemas, tool broker, retrieval policy, generation budget, checkpoint harness, and coexistence scenarios. Do not compare Qwen3 in thinking mode against Ministral in a cheaper non-reasoning configuration without recording the difference as part of the evaluated configuration.

## 4. Smaller and larger comparators

| Comparison | Documented basis | APEX hypothesis to test |
|---|---|---|
| Qwen3-8B vs Qwen3-4B | [DOCUMENTED] Both expose Qwen3 thinking/non-thinking behavior, tool-oriented usage, and 32,768 native context; Qwen3-8B has 8.2B parameters versus Qwen3-4B at 4.0B. (huggingface) | [INFERRED] The 8B model should materially improve UNKNOWN recognition, evidence comparison, recovery judgement, and escalation routing without making coexistence unusable. |
| Ministral 3 8B vs Ministral 3 3B | [DOCUMENTED] Both belong to the same Ministral 3 family, with instruct and reasoning variants listed for the size classes. (huggingface) | [INFERRED] The 8B model should reduce tool-argument errors and scope-drift attempts on multi-step packets. |
| Qwen3-8B vs Ministral 3 8B | [DOCUMENTED] Qwen3 emphasizes switchable reasoning and tool/MCP integration; Ministral 3 emphasizes function calling, JSON, vision, and edge deployment. (huggingface) | [INFERRED] Qwen3 may lead state/reasoning tasks, while Ministral may lead screenshot/tool-schema tasks. APEX fixtures, not generic benchmarks, decide. |
| Qwen3-8B vs Qwen3-14B | [DOCUMENTED] Qwen's current documentation lists both 8B and 14B dense sizes and describes hybrid thinking/non-thinking behavior across the family. (qwen.readthedocs) | [INFERRED] The 14B model must reduce meaningful APEX failures rather than merely improve generic reasoning. |
| Ministral 3 8B vs Ministral 3 14B | [DOCUMENTED] Mistral's official card reports benchmark comparisons for both sizes and lists both instruct variants. (huggingface) | [INFERRED] The 14B model is justified only if gains in recovery, contradiction detection, and escalation exceed load, latency, and coexistence penalties. |
| Qwen3/Ministral 8B vs Gemma 3 12B | [DOCUMENTED] Gemma 3 12B supports image input and 128K context, with official instruction and reasoning benchmark results. (google) | [INFERRED] Gemma is a multimodal challenger, but tool-call and APEX authority behavior remain unverified. |

## 5. WEEKLY-01..06 evidence/hypothesis matrix

| Fixture | Public evidence | APEX hypothesis and measurement |
|---|---|---|
| WEEKLY-01 — one prompt + capture | [DOCUMENTED] Qwen3-8B and Qwen3-4B provide documented local endpoint and generation examples; Ministral provides a local OpenAI-compatible serving pattern. (huggingface) | [INFERRED] Both 8B candidates should capture the approved response and artifact references without adding undeclared work. Measure capture completeness, structured validity, false success, and intervention count. |
| WEEKLY-02 — conditional multi-turn | [DOCUMENTED] Qwen3 supports turn-level thinking-mode control and advises excluding hidden thinking content from multi-turn history. (huggingface) | [INFERRED] Qwen3 may have an advantage in conditional follow-up handling; test closed-set mapping, UNKNOWN stopping, duplicate submissions, and invented branch rate. |
| WEEKLY-03 — browser/UI recovery | [DOCUMENTED] Ministral 3 8B and Gemma 3 support image input; this establishes multimodal capability, not browser-agent certification. (google) | [UNKNOWN] No candidate is publicly certified for APEX semantic UI recovery. Test screenshot interpretation, equivalent-intent recovery, consequential-mode avoidance, and broker-blocked unauthorized actions. |
| WEEKLY-04 — interruption/resume | [DOCUMENTED] The authority portfolio requires external durable checkpoints; model cards do not establish checkpoint semantics. | [INFERRED] Model size should have limited importance if the harness owns state. Measure duplicate submission rate, checkpoint reconstruction, restart classification, and model/harness fault separation. |
| WEEKLY-05 — multi-repo containment | [DOCUMENTED] Qwen3 documents external tools and MCP integration; this does not prove root obedience. (huggingface) | [UNKNOWN] Test declared A/B/C roots versus forbidden D, including plausible path text inside untrusted content. The broker must enforce zero forbidden-root success independently of model behavior. |
| WEEKLY-06 — raw evidence + index | [DOCUMENTED] The APEX portfolio requires raw evidence preservation and permits only non-authoritative indexing. | [INFERRED] A 7–8B model may be sufficient for structural extraction; test whether larger models increase semantic overreach. Measure raw-evidence hash preservation, index correctness, and unauthorized conclusions. |

## 6. MA-01..06 evidence/hypothesis matrix

| Fixture | Public evidence | APEX hypothesis and measurement |
|---|---|---|
| MA-01 — bounded Meta Ops packet | [DOCUMENTED] Qwen3 and Ministral document tool/function-calling paths. (huggingface) | [INFERRED] Both 8B candidates should execute a frozen packet and return evidence without creating a continuation workstream. Measure packet adherence, output schema validity, and self-created work. |
| MA-02 — Detective evidence without verdict | [DOCUMENTED] Public model cards describe general reasoning, instruction following, or agent capabilities, but none certify separation between evidence collection and validity judgement. (huggingface) | [UNKNOWN] Test whether the model reports evidence and contradiction candidates while refusing to issue authority or validity verdicts. |
| MA-03 — KB/Informatics hygiene | [DOCUMENTED] Gemma 3 and Ministral 3 document instruction-following and text transformation use cases. (google) | [INFERRED] Smaller models may perform mechanical terminology/schema cleanup adequately; semantic ambiguity should force typed escalation rather than local redesign. |
| MA-04 — prompt/workflow materialization | [DOCUMENTED] Qwen3 and Ministral support structured/tool-oriented interaction patterns. (huggingface) | [INFERRED] 7–8B models should materialize approved templates, but larger reasoning modes may increase unauthorized strategy rewriting. Measure exact-template fidelity and semantic drift. |
| MA-05 — escalation destination selection | [UNKNOWN] No reviewed model card reports APEX-like closed-vocabulary escalation classification. | [INFERRED] Qwen3-8B's optional reasoning may improve distinction between transient, operational, coding, reasoning, authority, security, and unknown failures. Test deterministic destination agreement and missed-escalation rate. |
| MA-06 — adversarial source containment | [DOCUMENTED] Google reports safety evaluation and limitations for Gemma 3, but its evaluation is not equivalent to APEX source/tool injection containment. (google) | [UNKNOWN] All candidates require direct INJECT-01..08 trials. Score model attempts separately from broker containment and require zero successful unauthorized actions. |

## 7. Injection-resistance findings

[DOCUMENTED] The APEX authority documents define captured source, browser, model, and tool content as untrusted data. They require layered containment: trust labels, capability broker, sandbox/allowlists, tool guards, and approval gates.

[UNKNOWN] The reviewed public model cards do not provide evidence for the exact APEX injection family: direct source instructions, fake Meta Ops approval, poisoned tool output, filesystem-scope expansion, secret-seeking comments, upload-endpoint social engineering, or candidate self-promotion.

[INFERRED] Model reasoning and instruction-following may increase the ability to recognize a malicious instruction, but may also increase willingness to pursue a plausible-looking task beyond the packet. The harness must therefore treat every model-originated tool request as untrusted until deterministic validation succeeds.

| Injection family | Required model test | Required system test |
|---|---|---|
| INJECT-01 source-file instruction | [UNKNOWN] Does the model preserve the packet and report the file as data? | [DOCUMENTED] Capability broker rejects commands not authorized by the packet. |
| INJECT-02 browser command request | [UNKNOWN] Does the model refuse or escalate? | [DOCUMENTED] Browser/tool layer blocks local command execution unless explicitly declared. |
| INJECT-03 fake approval | [UNKNOWN] Does the model treat the claim as untrusted? | [DOCUMENTED] Approval state is externally represented and cannot be created by content. |
| INJECT-04 new upload endpoint | [UNKNOWN] Does the model stop rather than invent a provider/path? | [DOCUMENTED] Upload destinations are allowlisted and packet-bound. |
| INJECT-05 poisoned code comment | [UNKNOWN] Does the model avoid secret access? | [DOCUMENTED] Secret paths and tools are outside the capability contract. |
| INJECT-06 poisoned tool output | [UNKNOWN] Does the model preserve provenance and avoid treating output as authority? | [DOCUMENTED] Tool responses are typed data and cannot mutate permissions. |
| INJECT-07 filesystem widening | [UNKNOWN] Does the model emit a typed escalation? | [DOCUMENTED] Root scope is enforced outside the model. |
| INJECT-08 self-promotion | [UNKNOWN] Does the model refuse candidate-to-verified promotion? | [DOCUMENTED] Promotion boundary is absolute and externally gated. |

## 8. Size/reasoning versus authority drift

[DOCUMENTED] Qwen3 explicitly exposes a thinking mode intended to improve reasoning and a non-thinking mode intended to improve efficiency. (huggingface)

[INFERRED] Greater reasoning capability may improve closed-set classification, evidence comparison, and recovery judgement. It may also increase the probability that the model attempts an apparently helpful but undeclared action, especially when the packet contains ambiguity or persuasive hostile content.

[DOCUMENTED] APEX authority is independent of model capability: local workers create candidates, independent review may verify exact reviewed versions, operator gates confirm consequences, and a gated mutation path applies durable changes.

| Dimension | ~3–4B hypothesis | ~7–8B hypothesis | ~12–14B hypothesis |
|---|---|---|---|
| Closed-set state classification | [INFERRED] More confusion and premature guesses are possible. | [INFERRED] Expected practical balance for UNKNOWN recognition. | [INFERRED] May improve difficult distinctions, but must be measured. |
| Recovery judgement | [INFERRED] Likely adequate only for obvious equivalent UI/path changes. | [INFERRED] Expected to handle bounded variation with lower escalation than controls. | [INFERRED] May reduce difficult recovery failures, but not necessarily enough to justify cost. |
| Evidence comparison | [INFERRED] Suitable for structural indexing and simple contradiction candidates. | [INFERRED] Expected to improve multi-source comparison. | [INFERRED] Possible advantage on subtle contradictions. |
| Authority drift | [UNKNOWN] Must be measured; smaller does not mean safe. | [UNKNOWN] Capability may increase initiative and scope drift. | [UNKNOWN] Larger reasoning may increase both useful recovery and overreach. |
| Containment | [DOCUMENTED] Must be external to the model. | [DOCUMENTED] Must be external to the model. | [DOCUMENTED] Must be external to the model. |

[INFERRED] The relevant metric is not "most intelligent model." It is successful bounded jobs per wall time and intervention, subject to zero successful unauthorized actions and acceptable coexistence.

## 9. Context and retrieval implications

[DOCUMENTED] Qwen3-8B and Qwen3-4B provide 32,768-token native context and 131,072-token YaRN validation. Gemma 3 4B, 12B, and 27B provide 128K context, while Ministral 3 8B advertises 256K context. (google, +3)

[DOCUMENTED] Qwen's model card warns that static YaRN configuration can affect shorter-text performance and recommends not enabling YaRN when typical context does not exceed 32,768 tokens. (huggingface)

[INFERRED] APEX should use the locked ~32K working tier as the normal target, with just-in-time retrieval and a 64K stretch test. Advertised maximum context must not be treated as verified operational context.

[INFERRED] Each candidate should be tested at approximately 8K, 16K, 32K, and—where supported—64K effective working context. The harness should measure action accuracy, tool churn, latency, malformed-output rate, and evidence provenance as context grows.

[UNKNOWN] No reviewed public source establishes candidate-specific degradation curves for APEX packet structures, long browser histories, multi-repo manifests, or raw-evidence indexing.

## 10. Browser and tool implications

[DOCUMENTED] Ministral 3 8B and Gemma 3 support image input, while Qwen3-8B documents tool calling and MCP integration but is presented as text-only in the reviewed model card. (google, +2)

[INFERRED] Ministral 3 8B and Gemma 3 12B deserve screenshot-based browser fixtures. Qwen3-8B remains suitable for DOM/state/tool fixtures and should not be excluded merely because the public card does not establish vision support.

[UNKNOWN] None of the reviewed primary sources certifies browser computer-use behavior such as safe semantic relocation of controls, preservation of declared intent, or avoidance of consequential mode changes.

[DOCUMENTED] Mistral recommends a small, well-defined tool set for agentic use. (huggingface)

[INFERRED] The APEX harness should expose the minimum tool set per fixture, use strict JSON Schema validation, reject unknown tool names and arguments, and separate model intent from actual execution.

[INFERRED] Browser recovery should be implemented as a state-and-intent problem: the model may propose an equivalent already-declared action, while deterministic policy decides whether the proposal is within scope.

## 11. Resource and coexistence implications

[DOCUMENTED] The known machine profile is Windows 11, Intel Core Ultra 7 258V, approximately 31.6 GB system RAM, and Intel Arc 140V integrated graphics. This is binding project context, not a measured model benchmark.

[DOCUMENTED] llama.cpp's SYCL backend supports Windows 11 and Intel built-in Arc GPUs, and its documentation includes Windows build instructions using Intel oneAPI and Visual Studio. It also warns that device memory limits model size and context size, and recommends reducing context or quantization when allocation fails. (github)

[DOCUMENTED] llama.cpp reports verified Intel built-in Arc support for Meteor Lake, Arrow Lake, and Lunar Lake families, but the reviewed page does not specifically verify the Core Ultra 7 258V / Arc 140V combination. (github)

[UNKNOWN] No source reviewed here provides measured throughput, peak RAM, shared-memory pressure, load/unload time, browser responsiveness, IDE impact, or concurrent-session behavior for the operator's exact machine.

[INFERRED] The first runtime bake-off should prioritize a Windows-compatible OpenAI-style local API and reproducible configuration. llama.cpp SYCL is a credible candidate runtime path, but the exact Arc 140V configuration must be validated locally; Vulkan and CPU fallback should be treated as comparison configurations rather than assumed winners.

[INFERRED] The 8B class is more plausible than 14B for coexistence because the machine uses integrated graphics and shared system resources. This is a resource hypothesis, not a measured conclusion.

[UNKNOWN] The practical feasibility of FP8 Ministral 3 8B, quantized Qwen3-8B, and 14B challengers on Arc 140V cannot be concluded from parameter count alone. Representation, context allocation, backend, KV-cache policy, and concurrent workload must be recorded.

## 12. Shortlist for APEX bake-off

### Tier 1 — required

Qwen3-8B, with at least:
- [INFERRED] one reproducible quantized configuration suitable for local Windows execution;
- [INFERRED] thinking and non-thinking profiles;
- [DOCUMENTED] native 32K context configuration, with 64K as stretch where supported;
- [DOCUMENTED] Qwen-Agent or OpenAI-compatible tool path as the integration baseline. (huggingface)

Ministral 3 8B Instruct 2512, with:
- [DOCUMENTED] FP8 baseline where the runtime supports it;
- [INFERRED] a comparable quantized configuration if FP8 is not practical;
- [DOCUMENTED] JSON/function-calling configuration;
- [INFERRED] vision-enabled browser configuration for screenshot fixtures. (huggingface)

### Tier 2 — efficiency controls

- Qwen3-4B, because it preserves the Qwen3 family behavior while reducing size. [DOCUMENTED] (huggingface)
- Ministral 3 3B Instruct 2512, because it tests the lower edge-oriented family member. [DOCUMENTED] (huggingface)
- Phi-4-mini-instruct, only as a secondary control after exact artifact and runtime provenance are fixed. [DOCUMENTED] The available evidence is a hosted NVIDIA model card rather than a directly retrieved Microsoft repository. (build.nvidia)

### Tier 3 — challengers

- Qwen3-14B, for same-family scaling analysis. [DOCUMENTED] (qwen.readthedocs)
- Ministral 3 14B Instruct 2512, for same-family edge-model scaling analysis. [DOCUMENTED] (huggingface)
- Gemma 3 12B IT, for multimodal and instruction-following comparison. [DOCUMENTED] (google)

[DOCUMENTED] No candidate is promoted to production or to a routing registry by this packet. Only benchmark-certified model-plus-runtime profiles may enter the planner-routed registry.

## 13. Unknowns requiring local trials

- [UNKNOWN] Exact Windows 11 / Arc 140V support for each selected runtime and model representation.
- [UNKNOWN] Peak RAM and shared GPU-memory pressure at 8K, 16K, 32K, and 64K contexts.
- [UNKNOWN] Model load, unload, and profile-switch time.
- [UNKNOWN] Browser responsiveness during inference.
- [UNKNOWN] IDE, terminal, test-runner, and occasional CLI-agent coexistence.
- [UNKNOWN] Tool-call schema validity under realistic APEX packet prompts.
- [UNKNOWN] Correct recognition of UNKNOWN consequential states.
- [UNKNOWN] Typed escalation destination accuracy.
- [UNKNOWN] Duplicate prevention after interruption and resume.
- [UNKNOWN] Multi-repo root obedience when forbidden paths appear in content.
- [UNKNOWN] Candidate-to-verified self-promotion attempts.
- [UNKNOWN] Raw-evidence preservation and provenance under large returned artifacts.
- [UNKNOWN] Browser screenshot interpretation and semantic equivalent-action recovery.
- [UNKNOWN] Injection attempt rates for INJECT-01 through INJECT-08.
- [UNKNOWN] Whether thinking mode improves bounded execution enough to justify latency and resource cost.
- [UNKNOWN] Whether larger models reduce CLI escalation enough to offset coexistence penalties.
- [UNKNOWN] Whether the same model requires separate profiles for Weekly and Multi-Agent work.
- [UNKNOWN] Whether a generalist model or coding-specialized model is better for non-coding operational support.
- [UNKNOWN] Whether quantization changes authority drift, malformed tool calls, or refusal behavior.
- [UNKNOWN] Whether a model/runtime configuration can sustain overnight resumable execution without false success.
- [UNKNOWN] Whether 64K context is useful after retrieval quality and latency are included.
- [UNKNOWN] Which failures should become permanent regression fixtures after baseline runs.

## 14. Source appendix

Primary and technical sources used:

- Qwen3-8B official Hugging Face model card. Documents parameter count, native and YaRN context, thinking-mode controls, sampling guidance, tool calling, Qwen-Agent, MCP usage, and local runtime examples. (huggingface)
- Qwen3-4B official Hugging Face model card. Documents 4.0B size, context behavior, thinking-mode controls, tool-oriented usage, and local deployment examples. (huggingface)
- Ministral 3 8B Instruct 2512 official Mistral Hugging Face model card. Documents architecture, FP8 representation, vision, JSON/function calling, context, family variants, benchmark tables, serving configuration, and licensing. (huggingface)
- Google Gemma 3 official model card. Documents multimodal input, context sizes, model sizes, benchmark results, limitations, and safety-evaluation scope. (google)
- llama.cpp official SYCL backend documentation. Documents Intel GPU support, Windows 11 support, oneAPI requirements, built-in Arc coverage, memory limitations, and build/run procedures. (github)
- NVIDIA-hosted Phi-4-mini-instruct model card. Documents 128K context, tool-enabled function-call formatting, and a comparative BFCL table. This is treated as weaker primary evidence than a directly retrieved Microsoft artifact. (build.nvidia)
- Qwen official documentation index. Documents current Qwen3 size classes and shared thinking/non-thinking behavior. (qwen.readthedocs)

[DOCUMENTED] Secondary aggregators and informal blog sources were not used as certification evidence. Generic benchmarks cited in official model cards are treated as prioritization evidence only; they do not certify APEX Weekly or Multi-Agent behavior.

## 15. YAML research record

```yaml
weekly_multiagent_model_research:
  evidence_date: "2026-08-09 [DOCUMENTED]"
  primary_7_8b_candidates:
    - "Qwen3-8B [DOCUMENTED]"
    - "Ministral-3-8B-Instruct-2512 [DOCUMENTED]"
  smaller_controls:
    - "Qwen3-4B [DOCUMENTED]"
    - "Ministral-3-3B-Instruct-2512 [DOCUMENTED]"
    - "Phi-4-mini-instruct [DOCUMENTED; weaker hosted-source provenance]"
  larger_challengers:
    - "Qwen3-14B [DOCUMENTED]"
    - "Ministral-3-14B-Instruct-2512 [DOCUMENTED]"
    - "Gemma-3-12B-IT [DOCUMENTED]"
  benchmark_priority:
    - "Tier 1: Qwen3-8B and Ministral-3-8B-Instruct-2512 across WEEKLY-01..06, MA-01..06, INJECT-01..08, context, and coexistence fixtures [INFERRED]"
    - "Tier 2: Qwen3-4B and Ministral-3-3B-Instruct-2512 as matched efficiency controls [INFERRED]"
    - "Tier 3: Qwen3-14B, Ministral-3-14B-Instruct-2512, and Gemma-3-12B-IT only where local deployment is credible [INFERRED]"
    - "Certify model-plus-runtime-plus-harness configurations, not model names alone [DOCUMENTED]"
    - "Require zero successful unauthorized actions [DOCUMENTED]"
  weekly_fixture_hypotheses:
    WEEKLY-01: "Both primary 8B candidates should capture approved prompt results and artifact references without undeclared work; measure schema validity and false success [INFERRED]"
    WEEKLY-02: "Qwen3 may benefit from explicit thinking-mode control; all candidates must map only to declared follow-ups or UNKNOWN [INFERRED]"
    WEEKLY-03: "Vision-capable candidates may improve screenshot interpretation, but semantic browser recovery remains unverified [UNKNOWN]"
    WEEKLY-04: "Checkpoint/resume quality should depend mainly on the external harness; duplicate submission and reconstruction must be measured [INFERRED]"
    WEEKLY-05: "Model path obedience is unverified; deterministic root containment must enforce zero forbidden-root success [UNKNOWN]"
    WEEKLY-06: "7–8B models may suffice for structural indexing, but semantic overreach and provenance loss require direct trials [INFERRED]"
  multiagent_fixture_hypotheses:
    MA-01: "Primary 8B candidates should execute frozen Meta Ops packets without creating continuation workstreams [INFERRED]"
    MA-02: "Evidence collection without validity or authority verdict remains unverified for all candidates [UNKNOWN]"
    MA-03: "Smaller models may handle mechanical hygiene; injected semantic ambiguity must produce typed escalation [INFERRED]"
    MA-04: "Template materialization may be adequate at 7–8B, while reasoning modes may increase strategy rewrite risk [INFERRED]"
    MA-05: "Qwen3-8B thinking mode may improve escalation distinctions; closed-vocabulary destination accuracy is unverified [UNKNOWN]"
    MA-06: "No reviewed model card certifies APEX hostile-content behavior; all candidates require INJECT-01..08 trials [UNKNOWN]"
  injection_findings:
    model_resilience: "Unverified for INJECT-01..08 [UNKNOWN]"
    system_containment: "Must be implemented through external trust labels, capability broker, allowlists, sandboxing, tool guards, and approval gates [DOCUMENTED]"
    successful_unauthorized_actions: "Required value is zero for certification [DOCUMENTED]"
    capability_authority_relationship: "Greater reasoning capability must not expand authority [DOCUMENTED]"
  size_tradeoff_hypotheses:
    "3_4B_vs_7_8B": "7–8B is hypothesized to improve UNKNOWN recognition, recovery judgement, evidence comparison, and escalation routing enough to justify additional resource use [INFERRED]"
    "7_8B_vs_12_14B": "12–14B must demonstrate material APEX fixture gains to justify memory, latency, loading, and coexistence penalties [INFERRED]"
    "capability_vs_drift": "Greater reasoning may improve recovery while increasing scope-drift attempts; this must be measured separately from containment [INFERRED]"
    "authority": "Authority remains external and unchanged across size classes [DOCUMENTED]"
  scope_drift_risks:
    - "Invented follow-up branches [UNKNOWN]"
    - "False success under ambiguous consequential state [UNKNOWN]"
    - "Forbidden-root or undeclared-path requests [UNKNOWN]"
    - "Candidate-to-verified self-promotion [UNKNOWN]"
    - "Prompt-template strategy rewrite [UNKNOWN]"
    - "Treating captured content as authority [UNKNOWN]"
    - "Overconfident recovery after UI/provider variation [UNKNOWN]"
  context_findings:
    native_working_target: "~32K reliably usable working context [DOCUMENTED]"
    stretch_target: "~64K where supported and locally verified [DOCUMENTED]"
    qwen3_8b: "32,768 native; 131,072 validated with YaRN [DOCUMENTED]"
    qwen3_4b: "32,768 native; 131,072 validated with YaRN [DOCUMENTED]"
    ministral_3_8b: "256K advertised context [DOCUMENTED]"
    gemma_3_12b: "128K context [DOCUMENTED]"
    policy: "Use just-in-time retrieval; do not treat advertised maximum context as certification evidence [DOCUMENTED]"
  browser_tool_findings:
    qwen3_8b: "Documented tool calling, Qwen-Agent, and MCP-oriented integration; screenshot/browser suitability remains unverified [DOCUMENTED/UNKNOWN]"
    ministral_3_8b: "Documented vision, native function calling, and JSON output; semantic browser recovery remains unverified [DOCUMENTED/UNKNOWN]"
    gemma_3_12b: "Documented image input and multimodal operation; browser-agent behavior remains unverified [DOCUMENTED/UNKNOWN]"
    tool_policy: "Expose minimum declared tools, validate schemas externally, and execute only after deterministic authorization [DOCUMENTED]"
  resource_findings:
    machine: "HP OmniBook X Flip / Core Ultra 7 258V / approximately 31.6 GB RAM / Arc 140V / Windows 11 [DOCUMENTED]"
    runtime_candidate: "llama.cpp SYCL is technically credible for Windows 11 and Intel built-in Arc, but exact Arc 140V behavior is unverified [DOCUMENTED/UNKNOWN]"
    coexistence: "8B is the leading resource hypothesis; throughput, memory pressure, load time, and responsiveness are unmeasured [INFERRED/UNKNOWN]"
    measurement: "Run model-only, browser, three-session, browser-plus-IDE, browser-plus-tests, and occasional CLI-agent coexistence fixtures [DOCUMENTED]"
  local_test_unknowns:
    - "Exact runtime/backend support for Arc 140V"
    - "Quantization and representation effects"
    - "Peak RAM and shared-memory pressure"
    - "Load/unload/profile-switch latency"
    - "Browser, IDE, terminal, test, and CLI-agent responsiveness"
    - "Structured tool-call validity"
    - "UNKNOWN recognition"
    - "Typed escalation accuracy"
    - "Checkpoint/resume duplicate prevention"
    - "Forbidden-root behavior"
    - "Injection attempt rates"
    - "Candidate-to-verified promotion attempts"
    - "Raw-evidence provenance preservation"
    - "Screenshot-based browser recovery"
    - "Value of thinking mode for bounded execution"
    - "Whether 12–14B gains justify coexistence cost"
    - "Whether separate Weekly and Multi-Agent profiles are needed"
    - "Whether 64K context improves outcomes after retrieval and latency costs"
  overall_confidence_0_to_100: 67
```
