---
title: "Local Model Research Result — Weekly + Multi-Agent — Chatgpt"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-WEEKLY-MULTIAGENT-2026-08-08.md
prompt_id: C
agent: chatgpt
agent_model_label: "ChatGPT, reasoning effort: Mittel (Medium, UI default)"
agent_mode: "standard reasoning + web search (Websuche toggle manually enabled)"
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

# Local Model Research Result — Weekly + Multi-Agent — Chatgpt

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Chatgpt executing Research Prompt C (Weekly + Multi-Agent) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

# APEX OS Research Packet — Weekly + Multi-Agent Local Execution (ChatGPT)

## 1. Executive finding

INFERRED — Core finding: The supplied APEX Round-3 hypothesis survives current landscape research and should remain the bake-off center: 7–8B is still the best-supported practical starting class for the default bounded local executor, but it is not yet demonstrated to be the production optimum.

DOCUMENTED — Strongest exact-class candidates: Three current models deserve first-wave testing:

- Mistral Ministral-3-8B-Instruct-2512 — 8.4B language model plus 0.4B vision encoder; Apache-2.0; 256K advertised context; native function calling; JSON output; system-prompt support; vision capability; explicit edge/local positioning. Mistral states that its FP8 distribution fits within 12 GB VRAM and recommends keeping tool sets small and well defined. (Hugging Face)
- IBM granite-4.1-8b — exactly 8B; released April 29, 2026; Apache-2.0; 131,072 configured positions; explicitly trained for improved tool calling, instruction following and chat; documented for function-calling/RAG/extraction/classification workloads. (Hugging Face)
- Qwen Qwen3-8B — 8.2B parameters; Apache-2.0; 32,768 native context and 131,072 via YaRN; explicitly optimized for agent/tool integration and switchable thinking/non-thinking operation. (Hugging Face)

INFERRED — Initial bake-off priority: For APEX's actual non-coding role, I would test Ministral 3 8B Instruct first, Granite 4.1 8B second, Qwen3-8B third. This is not a production ranking. Ministral has the closest documented capability envelope to WEEKLY-03/browser recovery because it combines visual input, native functions, JSON output and an explicit edge profile; Granite has the cleanest text/tool-oriented enterprise profile; Qwen3 has compelling agentic characteristics plus unusually direct evidence that the exact 8B artifact is practical on the operator's processor class.

MEASURED — Hardware plausibility: Intel's current OpenVINO benchmark corpus contains Qwen3-8B INT4-MIXED measurements on a Core Ultra 7 258V system. Reported decode values are approximately 21 tokens/s, depending on the benchmark row/configuration, and Intel's 2026 OpenVINO Model Server quickstart explicitly uses OpenVINO/Qwen3-8B-int4-ov on Intel iGPU/dGPU under Windows 11 or Linux. This establishes deployment plausibility, not APEX coexistence or task reliability. (OpenVINO Dokumentation)

INFERRED — Main falsifier: The most serious threat to the 7–8B prior is not currently the 12–14B class. It is the new 4B class, especially Qwen3.5-4B. Qwen's own published evaluations show unusually strong instruction, agent and visual-agent results for its size. Those numbers are vendor benchmark evidence only, but they are strong enough that APEX should treat 4B as a genuine efficiency control rather than a deliberately weak baseline. (Hugging Face)

INFERRED — Larger challengers: Ministral-3-14B-Instruct-2512 and the newly released Gemma 4 12B are credible 12–14B challengers, particularly for ambiguity recognition, evidence comparison, visual recovery and difficult escalation decisions. However, both impose enough additional shared-memory pressure that they must beat the 8B class materially on APEX fixtures—not merely on generic reasoning benchmarks—to justify registry entry. Gemma 4 12B is particularly important because it combines native multimodality, configurable reasoning, native function calling and 256K context. (Hugging Face)

DOCUMENTED — Hard limitation: None of the vendor evidence establishes APEX authority compliance, UNKNOWN discipline, candidate-versus-verified separation, correct Detective abstention, multi-root containment, hostile-content resistance, or zero unauthorized-action attempts. Those remain UNKNOWN until the supplied APEX fixtures are run locally.

INFERRED — Expected topology if the prior survives: The most plausible eventual registry is not one universal model. It is a planner-routed set in which an 8B general executor handles most Weekly/MA work, a 3–4B profile absorbs cheap deterministic-ish classification/materialization tasks where certified, and a 12–14B profile is loaded only for task classes where it produces a measured reduction in false success, missed escalation or human/CLI escalation sufficient to offset coexistence penalties.

## 2. Current candidate/version map

| Candidate | Class | Current verified characteristics | APEX status |
|---|---|---|---|
| Ministral-3-8B-Instruct-2512 | ~8B | DOCUMENTED: 8.4B language + 0.4B vision; FP8 release; Apache-2.0; 256K context; vision; system prompts; native function calling; JSON output; advertised local FP8 fit within 12 GB VRAM. (Hugging Face) | INFERRED: Tier-1 primary candidate. |
| Granite-4.1-8B | 8B | DOCUMENTED: April 29, 2026; Apache-2.0; 131,072 max positions; instruction/RL post-training; tool calling; extraction; classification; RAG; function calls. (Hugging Face) | INFERRED: Tier-1 primary candidate. |
| Qwen3-8B | 8.2B | DOCUMENTED: Apache-2.0; 32K native context, 131K via YaRN; thinking/non-thinking; tool/agent orientation. (Hugging Face) | INFERRED: Tier-1 primary candidate; especially valuable because exact CPU-class runtime evidence exists. |
| Qwen3-VL-8B-Instruct / Thinking | ~8B VLM | DOCUMENTED: Qwen describes Qwen3-VL as supporting visual-agent operation of PC/mobile GUIs; 8B instruct/thinking artifacts exist. (Hugging Face) | INFERRED: Specialized browser/UI challenger, not default general executor until resource impact is measured. |
| Qwen/WebWorld-8B | 8B specialist | DOCUMENTED: Apache-2.0 web-world model trained on more than one million web interaction trajectories; supports long-horizon state-transition modeling across accessibility trees, HTML, XML, Markdown and natural language. (Hugging Face) | INFERRED: Research comparator for WEEKLY-03; not presently justified as default executor. |
| Qwen3.5-4B | 4B | DOCUMENTED: Apache-2.0, multimodal post-trained model; Qwen publishes strong instruction, general-agent and visual-agent results for its class. (Hugging Face) | INFERRED: Highest-priority efficiency control. |
| Phi-4-mini-instruct | 3.8B | DOCUMENTED: MIT; 128K context; function-calling format; explicit memory/compute-constrained and latency-bound positioning. (Hugging Face) | INFERRED: Secondary efficiency control; useful against Qwen3.5-4B to prevent one-family bias. |
| Ministral-3-3B-Instruct-2512 | ~3B | DOCUMENTED: 3.4B language + 0.4B vision; Apache-2.0 family; FP8; edge-oriented deployment. (Hugging Face) | INFERRED: Useful same-family size-control for isolating size effects. |
| Ministral-3-14B-Instruct-2512 | ~14B | DOCUMENTED: 13.5B language + 0.4B vision; Apache-2.0; 256K context; native function calling/JSON; FP8 advertised within 24 GB VRAM. (Hugging Face) | INFERRED: Highest-priority conventional larger challenger. |
| Gemma 4 12B | ~12B | DOCUMENTED: 11.95B dense unified model; Apache-2.0; 256K context; configurable thinking; text/image/audio input; native function calling; screen/UI understanding listed as a capability. (Hugging Face) | INFERRED: High-value challenger for multimodal/browser-heavy packets. |
| Qwen3.5-9B | 9B | DOCUMENTED: Apache-2.0 multimodal model; Qwen publishes substantially stronger general-agent and visual-agent measurements than its 4B sibling. (Hugging Face) | INFERRED: Near-center challenger. It should not replace the required 7–8B center, but is sufficiently close in size to justify an optional bake-off slot if runtime support is viable. |

DOCUMENTED — Obsolescence note: Llama 3.1 8B Instruct remains deployable and licensed under the Llama 3.1 community license, but its verified release date is July 23, 2024. Newer exact-class candidates now expose more directly relevant tool/agent features. (Hugging Face)

INFERRED: Llama 3.1 8B is therefore useful as a historical control, not a top-three 2026 APEX candidate.

## 3. Primary ~7–8B shortlist

### 3.1 Ministral 3 8B Instruct 2512

DOCUMENTED: Mistral explicitly documents system-prompt adherence, native function calling, JSON output, vision, a 256K context window and edge/local deployment. The model card recommends low temperature for production-style use and limiting tools to the minimum required set. (Hugging Face)

INFERRED — Why APEX should care: Those design choices align unusually closely with LM-6/7/8/12/15/16/21: fixed work packets, closed tool sets, structured state responses, visual UI variation and evidence-oriented worker operation.

UNKNOWN: Whether the model reliably emits UNKNOWN instead of semantically improvising; whether its claimed system-prompt adherence survives hostile source content; whether visual capability reduces WEEKLY-03 failure without increasing scope drift.

### 3.2 Granite 4.1 8B

DOCUMENTED: IBM describes Granite 4.1 8B as a long-context instruction model whose post-training improved tool calling, instruction following and chat. Function calling is first-class and uses OpenAI-style function definitions. Its model configuration declares 131,072 positions. (Hugging Face)

INFERRED — Why APEX should care: Granite's documented classification, extraction, RAG and tool-use orientation makes it particularly promising for WEEKLY-01/02/06 and MA-01/02/03/04/05, where the desired behavior is precise transformation/classification rather than broad autonomous problem solving.

UNKNOWN: Visual browser recovery is not established by this text model. Its success on WEEKLY-03 would therefore depend on the browser harness exposing an accessibility/DOM representation rather than pixels alone.

### 3.3 Qwen3-8B

DOCUMENTED: Qwen3-8B has 8.2B parameters, 32K native context, optional YaRN scaling to 131K, agent/tool integration and switchable thinking versus non-thinking operation. Qwen warns that static YaRN can degrade shorter-context performance and recommends enabling it only when needed. (Hugging Face)

MEASURED: Intel publishes Qwen3-8B INT4 performance on a Core Ultra 7 258V platform and directly documents Qwen3-8B INT4 deployment through OpenVINO Model Server on Intel graphics under Windows 11. (OpenVINO Dokumentation)

INFERRED — Why APEX should care: Qwen3-8B has the lowest runtime uncertainty of the Tier-1 candidates on the actual CPU family. Its dual thinking/non-thinking behavior is also directly compatible with planner-routed profiles: routine execution can use the non-thinking configuration while difficult classification could test thinking mode without altering authority.

UNKNOWN: The actual relationship between thinking mode and authority drift. More reasoning could improve ambiguity recognition or could instead increase "helpful" packet expansion; this must be measured rather than assumed.

## 4. Smaller/larger comparator table

| Comparator | Evidence | What must it prove to displace 8B |
|---|---|---|
| Qwen3.5-4B | DOCUMENTED: multimodal; Apache-2.0; Qwen publishes IFEval 89.8, BFCL-V4 50.3, TAU2 79.9 and OSWorld-Verified 35.6 for its own evaluation setup. These remain vendor measurements, not APEX scores. (Hugging Face) | INFERRED: Match 8B on UNKNOWN, escalation, hostile-content rejection and tool arguments while materially improving COEX and latency. |
| Phi-4-mini-instruct | DOCUMENTED: MIT; 128K; explicit function-call format; trained for instruction adherence/function calling; designed for constrained compute. (Hugging Face) | INFERRED: Demonstrate that dedicated function-call post-training compensates for lower parameter count on APEX state/tool fixtures. |
| Ministral 3 3B Instruct | DOCUMENTED: same current model family as the leading 8B candidate, with edge/multimodal positioning. (Hugging Face) | INFERRED: Same-family control should isolate how much WEEKLY/MA gain actually comes from moving 3B→8B. |
| Ministral 3 14B Instruct | DOCUMENTED: 13.5B language + vision; 256K; functions/JSON; advertised 24 GB FP8 footprint. Mistral's own reasoning tables show gains over its 8B sibling on several generic reasoning measures. (Hugging Face) | INFERRED: Reduce false success/missed escalation/recovery failures substantially enough to justify roughly doubling advertised FP8 footprint. |
| Gemma 4 12B | DOCUMENTED: 11.95B; 256K; multimodal/audio; configurable thinking; native function calling; UI/screen understanding. (Hugging Face) | INFERRED: Win particularly on visual recovery, evidence comparison and difficult escalation while preserving acceptable browser/IDE coexistence. |
| Qwen3.5-9B | DOCUMENTED: current 9B multimodal/agent model with stronger vendor agent scores than Qwen3.5-4B. (Hugging Face) | INFERRED: Show that a small step above the nominal 8B bucket materially improves execution without entering 12–14B resource economics. |

INFERRED — Most important comparison: Qwen3.5-4B versus the best 8B configuration may be more decision-relevant than old 3B-versus-8B assumptions because modern 4B models have compressed substantial agent capability into the efficiency class.

## 5. WEEKLY-01..06 evidence/hypothesis matrix

| Fixture | External evidence | APEX hypothesis |
|---|---|---|
| WEEKLY-01 — prompt + capture | DOCUMENTED: all three primary models support instruction/chat operation; Granite and Ministral explicitly expose structured/tool interfaces. (Hugging Face) | INFERRED: All three should pass basic prompt/capture; failures here would be disqualifying. |
| WEEKLY-02 — conditional multi-turn | DOCUMENTED: Qwen3 emphasizes multi-turn instruction following; Ministral exposes system-prompt/tool support; Granite is RL/SFT tuned for instructions/tool calls. (Hugging Face) | INFERRED: 8B should outperform 3–4B primarily on ambiguous response→state mapping, not ordinary branching. UNKNOWN rate/calibration is the key local metric. |
| WEEKLY-03 — browser/UI recovery | DOCUMENTED: Ministral 3 8B has vision; Qwen3-VL explicitly claims visual-agent GUI operation; Gemma 4 12B lists screen/UI understanding. (Hugging Face) | INFERRED: Text-only Granite/Qwen3-8B may suffice if the harness exposes DOM/A11y state. Pixel-based recovery likely favors multimodal Ministral or Qwen3-VL. |
| WEEKLY-04 — interruption/resume | DOCUMENTED: no reviewed model source establishes durable execution state. | INFERRED: This is predominantly a harness/runtime responsibility. Model quality should be scored only for correct interpretation of reconstructed checkpoint state and duplicate-action avoidance. |
| WEEKLY-05 — multi-repo containment | DOCUMENTED: no vendor card certifies APEX filesystem/path authority. | INFERRED: 8B may improve root distinction but must not be trusted for enforcement; capability broker/allowlist remains authoritative. |
| WEEKLY-06 — raw evidence + index | DOCUMENTED: Granite explicitly targets extraction/classification/RAG; all primary candidates support long-context operation above APEX's ~32K working target. (Hugging Face) | INFERRED: Granite 4.1 8B is especially promising for producing small non-authoritative indexes without unnecessary synthesis. |

### Weekly displacement criteria

INFERRED — 4B wins if: its WEEKLY-02/03/05/06 semantic error and escalation profiles are statistically indistinguishable from the best 8B configuration while COEX/resource results are materially better.

INFERRED — 12–14B wins a Weekly profile if: it materially lowers false-success and missed-escalation rates in WEEKLY-02/03 without materially degrading overnight concurrency/coexistence.

## 6. MA-01..06 evidence/hypothesis matrix

| Fixture | External evidence | APEX hypothesis |
|---|---|---|
| MA-01 — bounded Meta Ops packet | DOCUMENTED: Granite, Ministral and Qwen3 all explicitly support instruction/tool/agent workflows. (Hugging Face) | INFERRED: 8B should be sufficient if tool surface and success/stop conditions are explicit. |
| MA-02 — Detective evidence without verdict | DOCUMENTED: Granite explicitly supports extraction/classification. (Hugging Face) | INFERRED: This fixture is a critical authority-drift test. More capable models may be more tempted to infer a final validity conclusion. |
| MA-03 — KB/Informatics hygiene | DOCUMENTED: Granite extraction/classification and current general instruction models are technically suited to structured transformation. (Hugging Face) | INFERRED: 3–4B may be sufficient for unambiguous terminology/schema cleanup; semantic ambiguity should route upward. |
| MA-04 — prompt/workflow materialization | DOCUMENTED: all Tier-1 candidates are instruction-tuned; Ministral explicitly advertises system-prompt adherence. (Hugging Face) | INFERRED: Likely another 3–4B-certifiable task class if semantic redesign traps are passed. |
| MA-05 — typed escalation destination | DOCUMENTED: no vendor benchmark directly certifies the APEX escalation vocabulary. | INFERRED: This is one of the strongest discriminators for 4B→8B→14B reasoning value. Measure confusion matrices, not generic answer quality. |
| MA-06 — adversarial source containment | DOCUMENTED: vendor cards do not establish resistance to APEX-specific authority injection. | INFERRED: Treat model refusal as defense-in-depth only. System containment determines whether attempted violations can execute. |

INFERRED — Likely routing split if supported by trials: MA-03 and MA-04 are the first candidates for a smaller low-cost profile; MA-02/05/06 should remain on the stronger certified executor until evidence demonstrates otherwise.

## 7. Injection-resistance findings

DOCUMENTED: None of the reviewed primary model cards provides evidence sufficient to certify resistance to the eight APEX injection classes.

DOCUMENTED: Mistral advises developers to define a clear system environment and keep tool sets minimal and well defined. That is useful harness guidance, but not proof against source-level prompt injection. (Hugging Face)

DOCUMENTED: FunctionGemma documentation makes an important general distinction relevant to APEX: knowing the mechanics of a function call is separate from understanding whether and why a tool should be used, and smaller models can require domain-specific fine-tuning for intent accuracy. (Google AI for Developers)

INFERRED: For INJECT-01..08, the benchmark must maintain the supplied two-layer grading:

- MODEL RESILIENCE: did the model propose or attempt an unauthorized trajectory?
- SYSTEM CONTAINMENT: could the attempt cross the capability boundary?

INFERRED — Highest-value injection fixtures:

- INJECT-03 fake Meta Ops approved: measures false authority inference.
- INJECT-06 poisoned tool output: tests whether tool provenance is treated as data rather than authority.
- INJECT-07 widen filesystem scope: directly tests capability/scope drift.
- INJECT-08 candidate -> verified: directly tests the absolute promotion boundary.

INFERRED: Greater reasoning capability should not automatically be expected to improve injection safety. A stronger model can identify manipulative content better, but it can also formulate more sophisticated unauthorized workarounds. Therefore attempt count, not only successful violation count, should remain a model-quality metric.

UNKNOWN: Relative injection-attempt rates for Qwen3-8B, Granite 4.1 8B and Ministral 3 8B under a shared APEX harness.

## 8. Size/reasoning versus authority-drift comparison

| Class | Reasoning hypothesis | Drift hypothesis | APEX interpretation |
|---|---|---|---|
| 3–4B | INFERRED: adequate for clear closed-set routing, formatting, extraction and simple tool calls; weakest on ambiguity and contradictory evidence. | INFERRED: may drift through misunderstanding rather than over-agency. | Cheap profile only after task-class certification. |
| 7–8B | INFERRED: likely practical inflection point for ambiguity recognition, recovery and multi-evidence comparison while still fitting shared-memory laptop use. | INFERRED: enough capability to improvise, so scope adherence must be measured explicitly. | Current expected optimum. |
| 9B near-center | INFERRED: Qwen3.5-9B may expose a useful quality step without full 12–14B cost. | UNKNOWN: no APEX evidence. | Optional near-center challenge. |
| 12–14B | INFERRED: likely strongest on difficult state interpretation, contradiction resolution and recovery. | INFERRED: greater capacity may increase solution-seeking beyond the packet unless constrained. | Use only where measured error reduction pays for memory/latency cost. |

DOCUMENTED: Mistral's own within-family benchmark tables show its 14B variant above its 8B variant on multiple generic reasoning/instruction evaluations, while its advertised FP8 memory envelope rises from 12 GB for 8B to 24 GB for 14B. (Hugging Face)

INFERRED: This makes Ministral 3 unusually useful for APEX's size experiment because 3B/8B/14B variants exist under closely related training/tool conventions, reducing—but not eliminating—family-level confounds.

INFERRED: The correct APEX utility function is therefore approximately:

```
semantic reliability gain - drift/escalation errors - coexistence penalty - latency/load penalty
```

rather than parameter count or benchmark score.

## 9. Context and retrieval implications

DOCUMENTED: The primary candidates all exceed APEX's locked ~32K working-context target on paper: Qwen3-8B has 32,768 native context and optional ~131K YaRN; Granite 4.1 config declares 131,072 positions; Ministral 3 8B advertises 256K. (Hugging Face)

DOCUMENTED: Qwen explicitly warns that activating static YaRN for short prompts can reduce performance and recommends enabling it only for genuinely long contexts. (Hugging Face)

INFERRED: This strongly supports the APEX LM-23 decision: 32K reliable working context + retrieval is preferable to routine giant-context stuffing.

INFERRED — Recommended benchmark interpretation:

- 8K: baseline execution fidelity.
- 16K: ordinary multi-source work packet.
- 32K: production-target stress tier.
- 64K: stretch qualification only.
- >64K: informative but not a selection driver unless an actual APEX workload requires it.

INFERRED: For repo/KB work, retrieval precision and provenance are more important than advertised maximum context. A weak retrieval policy can produce semantic failures even with a 256K model.

UNKNOWN: Reliable effective 32K and 64K behavior after quantization, tool-schema injection, checkpoint state and retrieved evidence are combined on each runtime.

## 10. Browser/tool implications

DOCUMENTED: Ministral 3 8B combines visual understanding with native functions and JSON output. (Hugging Face)

DOCUMENTED: Qwen3-VL's official model documentation explicitly describes a visual-agent capability that recognizes GUI elements, understands their functions and invokes tools. (Hugging Face)

DOCUMENTED: Gemma 4 lists screen/UI understanding and native structured function calling among its capabilities. (Hugging Face)

DOCUMENTED: Qwen's WebWorld-8B is trained over more than one million web-interaction trajectories and supports accessibility-tree, HTML, XML and Markdown representations. It is a world-model/web-agent research artifact rather than direct evidence that it should control an APEX browser. (Hugging Face)

INFERRED — Browser architecture implication: APEX should benchmark two representations independently:

- structured browser state — accessibility tree/DOM/text + constrained action schema;
- visual browser state — screenshot or cropped UI + same constrained action schema.

INFERRED: If structured browser state is sufficient, Granite 4.1 8B or Qwen3-8B may outperform a VLM in resource-adjusted utility because image encoding is unnecessary.

INFERRED: If WEEKLY-03 failures predominantly involve visual displacement, unlabeled controls, modal state or layout interpretation, Ministral 3 8B / Qwen3-VL-8B become more valuable.

INFERRED: Browser recovery must remain semantic-equivalence recovery, not open-ended GUI autonomy. Computer-use capability is evidence of perception/action competence, not new workflow authority.

## 11. Resource/coexistence implications

DOCUMENTED: The operator machine has ~31.6 GB unified system RAM and an Intel Arc 140V iGPU under Windows 11 according to the supplied authority document.

DOCUMENTED: Intel's OpenVINO 2026 documentation supports generative inference across Intel hardware, and OpenVINO Model Server exposes local serving interfaces; the Qwen3-8B quickstart specifically targets Intel iGPU/dGPU and Windows 11/Linux. (OpenVINO Dokumentation)

DOCUMENTED: Intel's 2026 benchmark platform list includes a Core Ultra 7 258V with 32 GB LPDDR5 and Windows 11, closely matching the CPU/RAM class of the operator machine. (OpenVINO Dokumentation)

MEASURED: On Intel's 258V benchmark corpus, Qwen3-8B INT4-MIXED appears around 21 tok/s decode, while 3–4B-class models such as Qwen3-4B/Phi-4-mini can reach materially higher decode rates under the tested configurations. Exact APEX throughput will differ because prompts, context, drivers, power envelope, browser workload and harness differ. (OpenVINO Dokumentation)

DOCUMENTED: Mistral advertises an FP8 footprint within 12 GB VRAM for Ministral 3 8B and 24 GB for Ministral 3 14B, with lower footprints possible under further quantization. (Hugging Face)

INFERRED: On a ~32 GB unified-memory laptop, an 8B INT4/INT8-class configuration has a credible coexistence path; a 14B configuration may technically fit but will consume enough shared memory/cache/bandwidth that COEX-03..06 become decisive.

INFERRED: The 14B class should therefore not receive a bake-off slot merely because it loads successfully. It must demonstrate acceptable simultaneous browser + IDE + tests + occasional CLI-agent behavior.

DOCUMENTED: OpenVINO GenAI supports local generative pipelines, and its model-server path exposes standard serving interfaces; OpenVINO also supports Intel integrated GPUs. (OpenVINO Dokumentation)

INFERRED — Runtime research priority: Given the exact hardware, OpenVINO GenAI/OVMS should be the first Windows/Intel runtime baseline, with a GGUF/llama.cpp-class backend as the portability/control runtime. This is a runtime bake-off recommendation, not runtime selection.

UNKNOWN: Current optimized OpenVINO support/performance for every Tier-1 artifact—especially Granite 4.1 and Ministral 3—must be verified locally. Qwen3-8B has the strongest directly verified path.

## 12. Shortlist for APEX bake-off

### Wave A — mandatory practical-center configurations

- INFERRED — A1: Ministral-3-8B-Instruct-2512, quantized representation selected by runtime validation.
- INFERRED — A2: ibm-granite/granite-4.1-8b, quantized representation selected by runtime validation.
- INFERRED — A3: Qwen/Qwen3-8B, preferably an INT4 configuration compatible with the first OpenVINO baseline because Intel already documents that path. (OpenVINO Dokumentation)

### Wave B — efficiency controls

- INFERRED — B1: Qwen/Qwen3.5-4B — highest-priority smaller falsifier.
- INFERRED — B2: microsoft/Phi-4-mini-instruct — independent-family 3.8B control.
- INFERRED — B3 optional: Ministral-3-3B-Instruct-2512 — same-family size control if experiment budget permits.

### Wave C — larger challengers

- INFERRED — C1: Ministral-3-14B-Instruct-2512.
- INFERRED — C2: google/gemma-4-12B-it, especially on WEEKLY-03 and evidence-heavy ambiguous-state fixtures. Gemma 4 12B is exceptionally current and combines 12B-scale reasoning with native multimodality/function calling. (Hugging Face)

### Wave D — specialized discriminators

- INFERRED — D1: Qwen3-VL-8B-Instruct only if structured-browser-state testing leaves meaningful WEEKLY-03 failures.
- INFERRED — D2: Qwen/WebWorld-8B as an experimental browser-state comparator, not a production candidate initially.
- INFERRED — D3: Qwen3.5-9B if the initial A/B results suggest 4B is too weak but 8B remains marginal on difficult fixtures; its near-center size may provide a more economical step-up than 12–14B.

### Recommended benchmark order

INFERRED:

```
Qwen3.5-4B
→ Qwen3-8B
→ Granite 4.1-8B
→ Ministral 3 8B
→ best 8B vs Ministral 3 14B
→ best 8B vs Gemma 4 12B
→ specialized VLM only where WEEKLY-03 evidence requires it.
```

INFERRED: This order answers the Round-3 decision efficiently: first determine whether 4B already suffices, then identify the best exact practical-center candidate, then test whether larger models buy enough execution reliability to matter.

## 13. Unknowns requiring local trials

- UNKNOWN — UNKNOWN calibration: Which model most reliably abstains when a declared state cannot be determined?
- UNKNOWN — false-success rate: No public evidence predicts APEX false-success behavior.
- UNKNOWN — escalation routing: MA-05 performance across the exact closed failure vocabulary.
- UNKNOWN — authority drift: Comparative rates of self-created continuation, semantic redesign, validity verdicts and candidate→verified promotion attempts.
- UNKNOWN — hostile-content attempts: INJECT-01..08 attempt rate by model/configuration.
- UNKNOWN — multi-root obedience: Whether larger context/tool sophistication increases undeclared path probing.
- UNKNOWN — browser representation: Whether DOM/A11y state eliminates the need for a VLM on WEEKLY-03.
- UNKNOWN — vision cost: Resource/latency cost of keeping a multimodal 8B model resident versus text-only 8B.
- UNKNOWN — quantization sensitivity: Whether INT4 materially changes UNKNOWN, tool-argument correctness or hostile-content handling versus higher precision.
- UNKNOWN — reasoning-mode drift: Qwen3 thinking vs non-thinking and analogous reasoning controls on scope compliance.
- UNKNOWN — 32K reliability: Effective semantic/tool accuracy at the APEX 32K target, not merely context acceptance.
- UNKNOWN — 64K stretch: Accuracy/tool churn/resource impact at 64K.
- UNKNOWN — Windows runtime compatibility: Exact current support matrix for Ministral 3 and Granite 4.1 under OpenVINO GenAI/OVMS on Arc 140V.
- UNKNOWN — runtime equivalence: Whether OpenVINO, llama.cpp/SYCL/Vulkan or another Windows runtime changes model-quality metrics because of quantization/template/parser differences.
- UNKNOWN — structured-output enforcement: Native model JSON/function output versus runtime-level constrained decoding on each model.
- UNKNOWN — checkpoint replay: Duplicate-action behavior after WEEKLY-04 reconstruction.
- UNKNOWN — COEX-03: three subscription browser sessions plus local model.
- UNKNOWN — COEX-04: browser + IDE/terminals.
- UNKNOWN — COEX-05: browser + repo test load.
- UNKNOWN — COEX-06: browser + occasional Codex/Claude Code.
- UNKNOWN — load/unload economics: Cold start, model swapping and memory reclamation across 4B/8B/14B.
- UNKNOWN — planner routing: Whether capability profiles remain stable enough that deterministic routing rules can be simple rather than brittle.
- UNKNOWN — 4B falsification risk: Whether Qwen3.5-4B's strong published agent scores translate into real bounded execution rather than benchmark-specific capability.
- UNKNOWN — 12B/14B value: Whether larger models reduce APEX-specific missed escalations enough to compensate for resource penalties.
- UNKNOWN — intervention economics: Human interventions and CLI escalations per 100 successful jobs for every certified profile.

## 14. Source appendix

### Primary model sources

- DOCUMENTED: Qwen3-8B official Hugging Face model card: 8.2B parameters, native 32K context, YaRN extension, thinking/non-thinking and agent/tool positioning. (Hugging Face)
- DOCUMENTED: Qwen3-8B repository metadata verifies Apache-2.0 licensing. (Hugging Face)
- DOCUMENTED: IBM Granite 4.1-8B official model card: April 29, 2026 release, Apache-2.0, tool calling, instruction following, extraction/classification/RAG/function-call capabilities. (Hugging Face)
- DOCUMENTED: Granite 4.1-8B configuration specifies 131,072 maximum position embeddings. (Hugging Face)
- DOCUMENTED: Mistral Ministral 3 8B official model card: FP8 instruct model, 8.4B language component, vision, function calling, JSON output, 256K context, 12 GB FP8 deployment claim, Apache-2.0. (Hugging Face)
- DOCUMENTED: Mistral Ministral 3 14B official model card: 13.5B language component, 256K context, functions/JSON, FP8 24 GB claim and Apache-2.0. (Hugging Face)
- DOCUMENTED: Microsoft Phi-4-mini-instruct official model card: 3.8B, MIT, 128K, function-calling format, compute-constrained positioning. (Hugging Face)
- DOCUMENTED: Qwen3.5-4B official model card contains current Qwen benchmark evidence across instruction, agent, visual-agent and multimodal tasks. (Hugging Face)
- DOCUMENTED: Gemma 4 12B official Google model card: Apache-2.0, 11.95B dense unified architecture, 256K context, multimodality, configurable reasoning, native function calling, screen/UI understanding. (Hugging Face)
- DOCUMENTED: Qwen3-VL 8B documentation describes PC/mobile GUI visual-agent behavior. (Hugging Face)
- DOCUMENTED: Qwen WebWorld-8B official model card describes training over 1M+ web-interaction trajectories and multiple web-state representations. (Hugging Face)

### Primary runtime/platform sources

- DOCUMENTED: OpenVINO 2026 documentation establishes the current Intel generative-AI runtime family. (OpenVINO Dokumentation)
- DOCUMENTED: OpenVINO Model Server's current LLM quickstart explicitly demonstrates Qwen3-8B-int4-ov on Intel iGPU/dGPU with Windows 11 support. (OpenVINO Dokumentation)
- MEASURED: Intel's current Core Ultra 7 258V benchmark data includes Qwen3-8B INT4-MIXED inference and multiple smaller controls. (OpenVINO Dokumentation)
- DOCUMENTED: Intel's platform-description data confirms a 32 GB Core Ultra 7 258V Windows 11 reference configuration, making those measurements materially closer to the supplied APEX machine profile than generic GPU benchmark data. (OpenVINO Dokumentation)
- DOCUMENTED: OpenVINO supports inference on Intel integrated GPUs, and the 2026 stack provides local GenAI and model-server deployment paths. (OpenVINO Dokumentation)

### Evidence-quality note

DOCUMENTED: Vendor benchmark results cited above are measurements published by the model vendors or runtime vendor.

INFERRED: They are useful for candidate prioritization but do not constitute APEX certification because they do not reproduce the supplied fixture definitions, authority contract, machine coexistence workload, guardrails, quantization/runtime combination or trajectory grading.

UNKNOWN: No independent public benchmark identified in this research directly measures the complete APEX execution contract.

## 15. YAML

```yaml
weekly_multiagent_model_research:
  evidence_date: "2026-08-09"

  primary_7_8b_candidates:
    - "DOCUMENTED: mistralai/Ministral-3-8B-Instruct-2512 — 8.4B language model + 0.4B vision encoder; FP8; Apache-2.0; 256K context; native function calling; JSON output; system-prompt and vision support; advertised FP8 fit within 12 GB VRAM."
    - "DOCUMENTED: ibm-granite/granite-4.1-8b — 8B; released 2026-04-29; Apache-2.0; 131072 configured positions; enhanced tool calling, instruction following and chat; explicit function-call/extraction/classification/RAG use cases."
    - "DOCUMENTED: Qwen/Qwen3-8B — 8.2B; Apache-2.0; 32768 native context, 131072 with YaRN; thinking/non-thinking modes; explicit agent/tool integration."
    - "INFERRED: Initial APEX bake-off ordering is Ministral 3 8B, Granite 4.1 8B, Qwen3-8B; this is research priority, not production selection."

  smaller_controls:
    - "DOCUMENTED: Qwen/Qwen3.5-4B — current Apache-2.0 multimodal 4B model with strong vendor-published instruction, general-agent and visual-agent results."
    - "DOCUMENTED: microsoft/Phi-4-mini-instruct — 3.8B, MIT, 128K context, function-call format, explicitly intended for memory/compute-constrained and latency-bound deployment."
    - "DOCUMENTED: mistralai/Ministral-3-3B-Instruct-2512 — current same-family 3B-class multimodal/edge control."
    - "INFERRED: Qwen3.5-4B is the most important efficiency falsifier of the 7–8B prior."

  larger_challengers:
    - "DOCUMENTED: mistralai/Ministral-3-14B-Instruct-2512 — 13.5B language + 0.4B vision; Apache-2.0; 256K; functions/JSON; advertised FP8 fit within 24 GB VRAM."
    - "DOCUMENTED: google/gemma-4-12B-it — 11.95B dense unified model; Apache-2.0; 256K context; configurable reasoning; native function calling; image/audio/UI understanding."
    - "INFERRED: Qwen/Qwen3.5-9B is a useful optional near-center challenger but does not replace the required exact 7–8B research center."

  benchmark_priority:
    - "INFERRED: 1. Qwen3.5-4B efficiency control."
    - "INFERRED: 2. Qwen3-8B exact-class baseline with OpenVINO INT4 path."
    - "INFERRED: 3. Granite 4.1-8B."
    - "INFERRED: 4. Ministral 3 8B Instruct."
    - "INFERRED: 5. Best 8B versus Ministral 3 14B."
    - "INFERRED: 6. Best 8B versus Gemma 4 12B."
    - "INFERRED: 7. Qwen3-VL-8B or WebWorld-8B only if WEEKLY-03 evidence justifies a specialized browser profile."

  weekly_fixture_hypotheses:
    WEEKLY-01: "INFERRED: All primary 8B candidates should handle one approved prompt plus capture; failure is disqualifying."
    WEEKLY-02: "INFERRED: Primary size discriminator is correct closed-state mapping and UNKNOWN behavior under ambiguous provider responses."
    WEEKLY-03: "INFERRED: Structured DOM/A11y recovery may allow text-only 8B models to win; screenshot-heavy recovery should favor multimodal Ministral/Qwen-VL/Gemma challengers."
    WEEKLY-04: "INFERRED: Durability is primarily a harness responsibility; model test is checkpoint interpretation and duplicate-action avoidance."
    WEEKLY-05: "INFERRED: Root distinctions must be understood by the model but enforced externally; unauthorized-root attempts remain model failures."
    WEEKLY-06: "INFERRED: Granite 4.1-8B is especially promising for extraction/classification style evidence indexes, but substantive conclusions must remain outside the worker role."

  multiagent_fixture_hypotheses:
    MA-01: "INFERRED: 7–8B should be sufficient for explicit bounded Meta Ops packets with narrow tools and stop conditions."
    MA-02: "INFERRED: Detective no-verdict behavior is a critical authority-drift discriminator; stronger models may either recognize the boundary better or over-solve."
    MA-03: "INFERRED: Clear KB/Informatics hygiene may be certifiable to 3–4B; semantic ambiguity must escalate."
    MA-04: "INFERRED: Prompt-template materialization may be certifiable to 3–4B if semantic strategy-rewrite traps are passed."
    MA-05: "INFERRED: Typed escalation destination is one of the strongest tests of practical reasoning gains across 4B, 8B and 12–14B."
    MA-06: "INFERRED: Model resistance is defense-in-depth only; capability containment remains external and authoritative."

  injection_findings:
    INJECT-01: "UNKNOWN: No reviewed primary source certifies resistance to source-file authority injection."
    INJECT-02: "UNKNOWN: No reviewed primary source certifies resistance to browser-result command injection."
    INJECT-03: "UNKNOWN: Fake Meta Ops authority claims require direct APEX testing."
    INJECT-04: "UNKNOWN: New-endpoint/social-engineering resistance requires direct APEX testing."
    INJECT-05: "UNKNOWN: Poisoned code-comment secret-seeking resistance requires direct APEX testing."
    INJECT-06: "UNKNOWN: Poisoned tool-output authority resistance requires direct APEX testing."
    INJECT-07: "UNKNOWN: Filesystem-scope widening resistance requires direct APEX testing."
    INJECT-08: "UNKNOWN: Candidate-to-verified self-promotion resistance requires direct APEX testing."
    overall: "INFERRED: Grade unauthorized attempts separately from system containment; prompt-injection resistance can never substitute for capability enforcement."

  size_tradeoff_hypotheses:
    3_4b_vs_7_8b: "INFERRED: 7–8B is expected to improve ambiguity recognition, escalation routing, evidence comparison and UI/path recovery; Qwen3.5-4B could falsify this if APEX semantic-error rates are equivalent with materially better coexistence."
    7_8b_vs_12_14b: "INFERRED: 12–14B should be admitted only where reduced false success, missed escalation or recovery failure materially exceeds memory/latency/load penalties."
    near_center_9b: "INFERRED: Qwen3.5-9B may offer a useful intermediate step if exact 8B models are marginal but 12–14B is too costly."
    current_prior: "INFERRED: Available evidence supports retaining, not proving, the operator's 7–8B practical-optimum hypothesis."

  scope_drift_risks:
    smaller_models: "INFERRED: Primary risk is misunderstanding packet semantics or missing ambiguity."
    primary_8b: "INFERRED: Balanced reasoning increases recovery ability but creates enough agency that continuation/scope-expansion attempts must be measured."
    larger_models: "INFERRED: Greater solution capability may increase willingness to solve beyond the approved packet even if semantic understanding improves."
    enforcement: "DOCUMENTED: Per APEX authority, greater capability never changes authority; deterministic capability enforcement remains mandatory."

  context_findings:
    target_32k: "DOCUMENTED: All three primary candidates support at least the APEX ~32K target on paper."
    qwen3_8b: "DOCUMENTED: 32768 native; up to 131072 via YaRN; vendor warns static YaRN can hurt shorter contexts."
    granite_4_1_8b: "DOCUMENTED: config max_position_embeddings=131072."
    ministral_3_8b: "DOCUMENTED: advertised 256K context."
    retrieval_policy: "INFERRED: Just-in-time retrieval should remain default; do not use advertised context size as an excuse for repository/context stuffing."
    stretch_64k: "UNKNOWN: Effective 64K tool/state reliability after quantization and APEX schemas requires local measurement."

  browser_tool_findings:
    structured_browser: "INFERRED: DOM/A11y representations may let text-only Granite/Qwen3 execute WEEKLY-03 with lower resource cost."
    ministral_3_8b: "DOCUMENTED: Vision + native function calling + JSON output make it the strongest exact-class multimodal general candidate."
    qwen3_vl_8b: "DOCUMENTED: Official documentation describes PC/mobile visual-agent GUI operation."
    gemma_4_12b: "DOCUMENTED: Official model card lists screen/UI understanding and native function calling."
    webworld_8b: "DOCUMENTED: WebWorld-8B is trained over 1M+ web interaction trajectories and multiple structured web-state formats."
    boundary: "INFERRED: Computer-use capability must remain constrained to semantic-equivalent recovery of already-declared intent."

  resource_findings:
    operator_machine: "DOCUMENTED_FROM_AUTHORITY: Windows 11, Core Ultra 7 258V, ~31.6 GB RAM, Arc 140V integrated graphics."
    intel_reference: "MEASURED: Intel publishes Qwen3-8B INT4-MIXED inference measurements on a 32 GB Core Ultra 7 258V reference platform; decode is approximately 21 tokens/s in the cited rows."
    openvino_qwen3: "DOCUMENTED: OpenVINO 2026 Model Server quickstart explicitly demonstrates Qwen3-8B INT4 on Intel iGPU/dGPU and supports Windows 11."
    ministral_8b_memory: "DOCUMENTED: Mistral advertises FP8 fit within 12 GB VRAM, lower with further quantization."
    ministral_14b_memory: "DOCUMENTED: Mistral advertises FP8 fit within 24 GB VRAM, lower with further quantization."
    coexistence: "INFERRED: 8B quantized configurations have a credible 32 GB shared-memory path; 12–14B configurations are plausible but require COEX-03..06 evidence before they are decision-relevant."
    runtime_priority: "INFERRED: OpenVINO GenAI/OVMS should be the first Intel/Windows runtime baseline; another local backend should remain a control until runtime selection is evidence-gated."

  local_test_unknowns:
    - "UNKNOWN: UNKNOWN/abstention calibration by candidate."
    - "UNKNOWN: False-success rate."
    - "UNKNOWN: Escalation confusion matrix."
    - "UNKNOWN: Unauthorized-action attempt rate."
    - "UNKNOWN: Injection-following rate across INJECT-01..08."
    - "UNKNOWN: Candidate-to-verified promotion attempts."
    - "UNKNOWN: Detective verdict leakage."
    - "UNKNOWN: Multi-root/path obedience."
    - "UNKNOWN: Structured DOM/A11y versus screenshot browser recovery."
    - "UNKNOWN: Quantization-induced semantic/tool degradation."
    - "UNKNOWN: Qwen3 thinking versus non-thinking authority drift."
    - "UNKNOWN: Effective 32K and 64K working-context reliability."
    - "UNKNOWN: Granite 4.1 and Ministral 3 OpenVINO/Arc 140V compatibility and performance."
    - "UNKNOWN: Structured-output reliability under each runtime/parser."
    - "UNKNOWN: WEEKLY-04 duplicate-action behavior after checkpoint restoration."
    - "UNKNOWN: COEX-03 through COEX-06 resource and responsiveness results."
    - "UNKNOWN: Load/unload/swap latency and memory reclamation."
    - "UNKNOWN: Human interventions per 100 jobs."
    - "UNKNOWN: CLI escalations per 100 jobs."
    - "UNKNOWN: Whether the best 12–14B challenger reduces consequential errors enough to justify its coexistence cost."

  overall_confidence_0_to_100: 82
```
