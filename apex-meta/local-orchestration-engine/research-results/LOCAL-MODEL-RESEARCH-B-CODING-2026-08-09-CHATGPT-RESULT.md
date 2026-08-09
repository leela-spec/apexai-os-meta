---
title: "Local Model Research Result — Coding — Chatgpt"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-CODING-2026-08-08.md
prompt_id: B
agent: chatgpt
agent_model_label: "ChatGPT, reasoning effort: Mittel (Medium, UI default)"
agent_mode: "standard reasoning + web search (Websuche toggle manually enabled)"
account_tier: "subscription (plan tier not disclosed by UI)"
run_id: R1
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: null
bundle_sha256: "c183a185110d6862a6d1a180ca2d67d54f6d2887190f286bc11f680823b5f22c"
retries: 0
interruptions: []
uncontrolled_variables:
  - "Chat URL for this specific run was not captured at execution time (browser extension disconnected before it could be recorded retroactively); response content and structure were verified via in-page marker/length checks before extraction."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Coding — Chatgpt

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Chatgpt executing Research Prompt B (Coding) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

APEX Local Model Research Packet — Bounded Coding Execution

Evidence date: 2026-08-09
Authority basis: Operator Decision Lock R3 + Local Model Benchmark Portfolio supplied verbatim in the research bundle.
Research boundary: No production model/runtime selection; bounded micro-coding only; main-only Git policy remains unchanged.

MEASURED: No APEX-machine benchmark was performed in this research run. All performance/resource conclusions requiring the HP OmniBook X Flip / Core Ultra 7 258V / Arc 140V / ~31.6 GB RAM are therefore hypotheses for the local bake-off, not measured facts.

1. Executive finding

DOCUMENTED: The strongest evidence supports keeping the operator's ~7–8B practical-center hypothesis alive. Two current generalist/agentic models deserve direct 7–8B testing: Qwen3-8B and Ministral 3 8B Instruct 2512. Qwen3-8B is an 8.2B dense model with native 32,768-token context, extension to 131,072 with YaRN, explicit thinking/non-thinking operation, agent/tool integration, Apache-2.0 weights and broad local-runtime support. Ministral 3 8B is an 8.4B language model plus a 0.4B vision encoder, Apache-2.0, explicitly edge/local-oriented, supports 256K context, native function calling and JSON output, and Mistral documents that its FP8 form fits in 12 GB VRAM. [Hugging Face]

DOCUMENTED: The strongest 7B-class coding-specialist control remains Qwen2.5-Coder-7B-Instruct, despite its older generation. It has 7.61B parameters, was continued-pretrained on 5.5T code-heavy tokens, was explicitly trained for code generation/reasoning/fixing, supports 131,072 tokens, and its technical report includes code generation, reasoning, editing and repair evaluations. [Hugging Face, arXiv]

INFERRED: Therefore, the primary APEX question is no longer simply generalist versus coder. It should be:

Can a newer agentically trained generalist such as Qwen3-8B or Ministral 3 8B match or beat Qwen2.5-Coder-7B on CODE-01..05 once scope adherence, correct escalation, tool calling and false-success behavior are scored alongside code correctness?

That is exactly the kind of distinction generic coding leaderboards do not resolve.

DOCUMENTED: There is meaningful evidence that a smaller model might falsify the 7–8B prior. Qwen3.5-4B is especially important: Qwen reports LiveCodeBench v6 55.8, BFCL-V4 50.3, and TAU2-Bench 79.9 in its official model card, while supporting explicit tool-call serving. Ministral 3 3B provides the cleanest same-family 3B-versus-8B control: Mistral reports LiveCodeBench 0.548 for the 3B reasoning variant versus 0.616 for 8B. [Hugging Face]

INFERRED: Qwen3.5-4B should therefore be the high-priority efficiency control, with Ministral 3 3B as the controlled same-family scaling comparison. Phi-4-mini-instruct remains useful as an independent 3.8B control because Microsoft explicitly trained it for instruction following and function calling and targets memory/compute-constrained deployments. [Hugging Face]

DOCUMENTED: The most decision-relevant larger challengers are Gemma 4 12B Unified and Ministral 3 14B. Google reports Gemma 4 12B at 72.0% LiveCodeBench v6 and 69.0% Tau2, with native function calling and 256K context. Mistral reports its 14B reasoning model at 0.646 LiveCodeBench, versus 0.616 for 8B and 0.548 for 3B. [Google AI for Developers]

INFERRED: Those documented gains are large enough to justify testing, but not large enough to justify preselecting a 12–14B model. APEX's bounded coding role rewards the point where additional reasoning stops reducing false fixes/missed escalations enough to compensate for extra model weight, KV cache, load time and lost laptop coexistence.

INFERRED: The recommended first bake-off is therefore:

Qwen3.5-4B -> Qwen3-8B -> Ministral 3 8B Instruct -> Qwen2.5-Coder-7B-Instruct -> Gemma 4 12B -> Ministral 3 14B

with the same APEX harness, guardrails, tool schema, context policy and quantization class wherever technically feasible.

UNKNOWN: It is not presently established from primary sources which of those configurations has the lowest missed-escalation rate, smallest unwanted-diff rate, best one-attempt micro-fix behavior, or best coexistence on the Core Ultra 7 258V. Those are local benchmark questions.

2. Current candidate/version table

- Qwen3-8B — ~8B generalist — Qwen/Qwen3-8B. DOCUMENTED: 8.2B parameters; 32,768 native context; 131,072 with YaRN; thinking/non-thinking; coding and agent/tool capabilities; supported by Ollama, LM Studio and llama.cpp. Apache-2.0. INFERRED: Primary 7–8B candidate.
- Ministral 3 8B Instruct 2512 — ~8B generalist/agentic — mistralai/Ministral-3-8B-Instruct-2512. DOCUMENTED: 8.4B LM + 0.4B vision encoder; 256K context; system-prompt adherence; native function calling and JSON; edge/local design; FP8 documented to fit within 12 GB VRAM. Apache-2.0. INFERRED: Primary 7–8B candidate.
- Qwen2.5-Coder-7B-Instruct — 7B code specialist — Qwen/Qwen2.5-Coder-7B-Instruct. DOCUMENTED: 7.61B; 131,072-token context; 5.5T continued-training tokens; code generation/reasoning/fixing focus; code-agent intent. DOCUMENTED: permissive/open-weight Qwen release; exact licence should be captured from the downloaded artifact during bake-off rather than inferred from family convention. INFERRED: Essential code-specialist comparator.
- Qwen3.5-4B — ~4B efficiency control — Qwen/Qwen3.5-4B. DOCUMENTED: 262K default context; tool-call parser support in official serving instructions; Qwen reports 55.8 LiveCodeBench v6 and 50.3 BFCL-V4. Apache-2.0 licence file. INFERRED: Highest-value small control.
- Ministral 3 3B Instruct/Reasoning 2512 — ~3B efficiency control — Ministral-3-3B-*-2512. DOCUMENTED: 256K; function calling and structured output; edge/local target; reasoning model scores 0.548 LiveCodeBench in Mistral evaluation. Apache-2.0. INFERRED: Best same-family scale-control for Ministral 8B.
- Phi-4-mini-instruct — 3.8B efficiency control — microsoft/Phi-4-mini-instruct. DOCUMENTED: 3.8B; 128K; instruction following; built-in function calling; explicitly targeted at memory/compute-constrained and latency-bound use. MIT. INFERRED: Secondary small control.
- Gemma 4 12B Unified — ~12B challenger — Gemma 4 12B instruction-tuned. DOCUMENTED: 11.95B; 256K; thinking; native function calling; coding; Google reports 72.0% LiveCodeBench v6 and 69.0% Tau2. Apache-2.0. INFERRED: Highest-priority 12B challenger.
- Ministral 3 14B — ~14B challenger — ministral-14b-2512 / corresponding weights. DOCUMENTED: 256K; structured outputs; function calling; local-deployment positioning; 0.646 LiveCodeBench for reasoning variant. Apache-2.0. INFERRED: Clean 8B→14B scaling challenger.
- Qwen3.5-9B — near-center challenger — Qwen/Qwen3.5-9B. DOCUMENTED: 9B; native 262,144 context; strong instruction/agent/coding results; official card reports LiveCodeBench v6 65.6 and BFCL-V4 66.1. DOCUMENTED: Open-weight Qwen artifact; exact downloaded licence should be recorded in bake-off config. INFERRED: Optional near-center probe because it is only modestly above the nominal 7–8B band.

INFERRED: Legacy candidates such as Llama 3.1 8B, CodeLlama 7B and Granite 8B Code do not need to occupy scarce first-round bake-off slots unless a runtime or regression-control reason emerges. Their historical value is outweighed by substantially newer 2025–2026 agentic/generalist models for this specific research question. IBM's Granite 8B Code remains relevant as historical evidence that an 8B coding-specialist form factor is practical, but not as the strongest current candidate. [IBM Research]

3. Primary ~7–8B generalist-versus-code-specialist comparison

Dimension | Qwen3-8B | Ministral 3 8B | Qwen2.5-Coder-7B
--- | --- | --- | ---
Coding specialization | DOCUMENTED: General model with improved coding/reasoning. | DOCUMENTED: General/agentic model; LiveCodeBench evidence exists. | DOCUMENTED: Explicit code-specific pretraining/post-training.
Tool/agent orientation | DOCUMENTED: Explicit external-tool/agent integration. | DOCUMENTED: Native function calling + JSON output. | DOCUMENTED: Intended as foundation for code agents, but its card gives weaker direct evidence for modern structured function-call protocols.
Exact patch ability | UNKNOWN: Must be APEX-tested. | UNKNOWN: Must be APEX-tested. | INFERRED: Strong prior from code editing/repair-specific training.
Test/log interpretation | INFERRED: General reasoning may benefit failure classification. | INFERRED: Agentic training is promising for tool/log loops. | INFERRED: Coding specialization is promising, but test interpretation is not equivalent to code-generation quality.
Correct escalation | UNKNOWN: No cited benchmark directly measures APEX-style restraint. | UNKNOWN: Same. | UNKNOWN: Same.
Scope discipline | UNKNOWN: Generic agent benchmarks cannot establish no-unwanted-diff behavior. | UNKNOWN: Same. | UNKNOWN: Same.
32K target | DOCUMENTED: Native 32,768. | DOCUMENTED: 256K advertised. | DOCUMENTED: 131K advertised.
Local footprint prior | INFERRED: 8B-class quantization should be plausible within 32 GB system RAM. | DOCUMENTED: FP8 version documented by Mistral as fitting in 12 GB VRAM. | INFERRED: Comparable 7B-class weight footprint; context/KV still requires testing.

Finding

INFERRED: Qwen2.5-Coder-7B should not be presumed superior simply because it is code-specialized. APEX's code role is unusually dominated by obedience:

inspect -> execute declared command -> classify -> minimally repair OR stop -> prove result

Modern generalists with strong tool protocols may outperform an older code specialist on this trajectory even if the specialist wins isolated code-generation tasks.

INFERRED: Conversely, Qwen2.5-Coder-7B could win CODE-02 and CODE-03 if code-specific training produces more accurate minimal patches and fewer syntactic/test failures. Its value is therefore as an essential specialization hypothesis test, not as an assumed coding default.

4. Smaller and larger comparator table

Configuration | Why test it | Evidence | Main falsification question
--- | --- | --- | ---
Qwen3.5-4B | Modern ~4B control with unusually strong documented agent/coding performance. | DOCUMENTED: LiveCodeBench v6 55.8; BFCL-V4 50.3; Tau2 79.9; official tool-call serving. | INFERRED: Does 8B materially reduce false repair/missed escalation enough to justify roughly double dense-model weight?
Ministral 3 3B | Clean architecture/training-family control for Ministral 8B/14B. | DOCUMENTED: LiveCodeBench reasoning 0.548 vs 0.616 at 8B and 0.646 at 14B. | INFERRED: Does the 8B step matter more for APEX than generic coding metrics suggest?
Phi-4-mini-instruct | Independent 3.8B function-calling control. | DOCUMENTED: 128K, function calling, improved instruction following, constrained-device use case. | INFERRED: Can careful harnessing let a compact model absorb CODE-01/02 without meaningful reliability loss?
Gemma 4 12B | Strong, newly released coding/reasoning/agent challenger. | DOCUMENTED: 72.0 LiveCodeBench v6, 69.0 Tau2, 256K, native function calling. | INFERRED: Does its quality gain actually lower APEX CLI escalation and false success enough to pay its memory cost?
Ministral 3 14B | Same-family 8→14B comparison. | DOCUMENTED: Mistral LiveCodeBench 0.616→0.646 from 8B→14B. | INFERRED: Is that incremental generic coding gain accompanied by a substantial CODE-03/04 reliability gain?
Qwen3.5-9B | Current Qwen generation immediately above practical-center band. | DOCUMENTED: 65.6 LiveCodeBench v6; 66.1 BFCL-V4; 262K native context. | INFERRED: Is the ~9B generation jump materially better than Qwen3-8B while retaining 8B-like coexistence?

Size conclusion

DOCUMENTED: Mistral's own same-family coding result increases from 0.548 → 0.616 → 0.646 across its 3B, 8B and 14B reasoning variants. The documented increment is substantially larger from 3B→8B than from 8B→14B.

INFERRED: That is directionally consistent with the operator's 7–8B optimum prior: the likely high-return capacity step is from the efficiency-control class to ~8B; the 8B→14B step may have diminishing marginal utility.

UNKNOWN: Whether this pattern carries over to APEX's escalation and scope-discipline metrics is unknown and must be falsified experimentally.

5. Evidence mapped to CODE-01..05

Fixture | Strongest prior | Weakest / key risk | Most uncertain
--- | --- | --- | ---
CODE-01 — test + failure classification | INFERRED: Qwen3-8B / Ministral 3 8B. Their general reasoning and agent/tool orientation should be advantageous when interpreting command output rather than merely generating code. Qwen explicitly documents external-tool expertise; Mistral documents native function calling/JSON. | INFERRED: Code-specialized models may over-index toward proposing fixes rather than classifying/halting. | UNKNOWN: Correct known-vs-unknown classification rate under APEX's closed taxonomy.
CODE-02 — exact mechanical patchspec | INFERRED: Qwen2.5-Coder-7B has the strongest specialization prior because its training/evaluations explicitly cover code editing/fixing. | INFERRED: Reasoning-heavy models may unnecessarily elaborate or refactor if harness constraints are weak. | UNKNOWN: Unwanted-diff rate by model under identical file allowlists.
CODE-03 — one tiny inferred fix | INFERRED: Qwen2.5-Coder-7B, Qwen3-8B and Gemma 4 12B are the highest-priority comparison. Gemma 4's official coding result gives the larger challenger a credible capability prior. | INFERRED: Small controls may correctly understand the defect yet make brittle patches or misread tests. | UNKNOWN: Whether 12B reduces failed first fixes enough to justify its resource penalty.
CODE-04 — ambiguous bug; escalation is success | INFERRED: This is likely the decisive APEX fixture. Generalist agentic models should be explicitly compared against coder specialists because the required action is non-coding restraint. | INFERRED: Higher coding skill can be actively harmful if it increases speculative repair. | UNKNOWN: No primary benchmark found measures APEX's exact "do not fix; type the escalation" behavior.
CODE-05 — bounded multi-repo operation | INFERRED: Ministral 3 8B and Qwen3-8B have the best prior from modern tool/agent design. | INFERRED: Any model can fail this through wrong-root selection even if its code is correct. | UNKNOWN: Root containment must be enforced and separately scored at model-attempt and system-containment layers.

Explicit cross-size hypotheses

INFERRED: ~7–8B versus ~3–4B: Expect 7–8B to show its largest advantage on CODE-01, CODE-03 and CODE-04—where semantic interpretation and restraint matter—rather than CODE-02, which is intentionally mechanical.

INFERRED: ~12–14B versus ~7–8B: Expect the larger class's greatest potential advantage on CODE-03/04. If it only improves raw patch success while leaving false-success and missed-escalation rates similar, it should not win the APEX role.

INFERRED: Code specialist versus generalist: Expect Qwen2.5-Coder-7B to be most competitive on CODE-02/03 and less clearly advantaged on CODE-01/04/05.

6. Scope/escalation-risk analysis

Failure mode | Research assessment
--- | ---
Editing undeclared files | UNKNOWN: No candidate is documented to satisfy APEX root/file authority semantically. This must be enforced externally and scored as a model-attempt failure if attempted.
Broad refactoring | INFERRED: More capable coding models may be more prone to technically sensible but unauthorized refactoring unless patch surface and diff validator are hard constrained.
Public API changes | UNKNOWN: Generic code benchmarks do not measure authorization awareness.
Repeated speculative repair | INFERRED: Thinking/reasoning modes increase the space of possible repairs; APEX's one-attempt rule must therefore be represented by deterministic execution state, not prompt prose alone.
Masked failing tests | INFERRED: Test outcome must be machine-derived. The model should never own the pass/fail truth value.
False success | INFERRED: Treat as a first-class failure independent of code correctness. A model claiming success against failed acceptance checks should fail certification.
Destructive Git command | INFERRED: Git permissions should be brokered at tool level; prompt adherence is insufficient.
Missed architecture escalation | UNKNOWN: This is likely the most discriminating model-quality metric in CODE-04.
Scope expansion after failure | INFERRED: The deterministic state machine should prevent a model from turning "test failed" into permission to inspect/write more roots.
Candidate → verified self-promotion | INFERRED: Must remain structurally unavailable to the local model.

INFERRED: The primary safety architecture should therefore evaluate two independent quantities, matching the authority documents:

Model resilience: did the model request or attempt an unauthorized action?

System containment: could the request actually execute?

A zero successful-unauthorized-action result produced only because the sandbox blocked a model that repeatedly attempted violations is not evidence of a good coding model.

7. Structured/tool-use findings

DOCUMENTED: Qwen3-8B explicitly advertises agent capabilities and precise integration with external tools, and its official model card documents deployment through OpenAI-compatible SGLang/vLLM endpoints plus broad local-runtime support.

DOCUMENTED: Ministral 3 8B directly advertises native function calling and JSON output, and Mistral's API model card exposes both structured outputs and function calling.

DOCUMENTED: Gemma 4 has native function calling; Google's documentation explicitly describes the model generating structured function-call objects that the developer parses and executes.

DOCUMENTED: Phi-4-mini-instruct contains an explicit tool-enabled function-calling format, and Microsoft describes better function calling as a post-training target.

DOCUMENTED: Qwen3.5-4B's official serving instructions show both SGLang and vLLM tool-call-parser configurations, making it unusually strong as a small tool-use control.

DOCUMENTED: llama.cpp currently exposes function-calling support and can enforce structured generation through its server/tooling stack; its documentation notes that native model templates are preferable to generic tool formatting because generic support can be less efficient.

DOCUMENTED: OpenVINO Model Server provides OpenAI-style agent serving and supports tool use/MCP integrations.

INFERRED: For APEX, native tool-call capability should be treated as a model-quality feature, but not a capability boundary. The harness should translate a valid schema proposal into deterministic authorization checks before executing any command.

INFERRED: The ideal benchmark interface is therefore:

model proposes typed action -> schema validator -> semantic validator -> capability broker -> execution -> machine result -> model

rather than allowing the model to emit free-form shell text directly.

8. Context requirements

8.1 32K production-target evidence

DOCUMENTED: Qwen3-8B supports 32,768 tokens natively, exactly matching LM-23's expected upper working tier. 131,072 is supported with YaRN rather than natively.

DOCUMENTED: Qwen2.5-Coder-7B-Instruct advertises a full 131,072-token context.

DOCUMENTED: Ministral 3 8B and 14B advertise 256K context.

DOCUMENTED: Gemma 4 12B supports 256K; its small E2B/E4B forms use 128K.

DOCUMENTED: Qwen3.5-4B/9B support 262,144 native context, although Qwen's serving instructions explicitly warn that inference memory varies with context and suggest reducing context on OOM.

8.2 What APEX should actually benchmark

INFERRED: Advertised maximum context is largely irrelevant to the first coding certification. The key gates are:

- 8K — INFERRED: Small patchspec/test loop baseline.
- 16K — INFERRED: Typical bounded repo-context + logs.
- 32K — INFERRED: Required serious certification tier.
- 64K — INFERRED: Stretch tier testing degradation and coexistence rather than maximum-advertised capacity.

INFERRED: CODE-05 should use just-in-time retrieval rather than whole-repository stuffing. A model that succeeds only when given a 128–256K repo dump should score worse economically than one that succeeds through bounded retrieval at 16–32K.

UNKNOWN: Reliable effective context under INT4/INT5 quantization, Arc 140V acceleration and simultaneous browser/IDE use is not established from model cards.

9. Windows/runtime/resource considerations

9.1 Runtime candidates

Runtime | Verified facts | APEX assessment
--- | --- | ---
llama.cpp / llama-server | DOCUMENTED: Current project provides OpenAI-style serving, function calling, GPU offload controls and structured-generation machinery; Qwen3's own model card lists llama.cpp as supported for local use. | INFERRED: Highest-priority portable runtime baseline because GGUF quantization, CPU/GPU split and explicit resource controls fit the laptop experiment.
Ollama | DOCUMENTED: Native Windows app and local API; current docs additionally provide Vulkan support on Windows/Linux. | INFERRED: Excellent operational baseline; less suitable as the only benchmark runtime because lower-level cache/offload/resource tuning needs explicit recording.
OpenVINO / OpenVINO GenAI / OVMS | DOCUMENTED: Intel-oriented CPU/GPU inference, local Model Server, agent/tool support; 2026 release notes include Qwen3.5/3.6 support and model-load/memory work. | INFERRED: Mandatory Intel-specific challenger because the machine is Lunar Lake/Core Ultra.
SGLang/vLLM | DOCUMENTED: Recommended by Qwen/Mistral for several current models and expose OpenAI APIs. | INFERRED: Useful correctness/reference runtime, but not first-choice Windows laptop runtime without local platform reconciliation.

9.2 Intel Arc 140V implications

DOCUMENTED: OpenVINO supports generative inference on Intel CPUs and GPUs, including integrated Intel graphics, and its current stack can expose language models through local serving.

DOCUMENTED: llama.cpp now has an OpenVINO backend intended to translate GGML graphs into OpenVINO graphs and exploit Intel hardware optimizations.

DOCUMENTED: Ollama exposes a Vulkan backend on Windows, giving another plausible route to the Arc 140V.

INFERRED: APEX should not decide among OpenVINO, llama.cpp-Vulkan/OpenVINO, and Ollama from theoretical hardware fit. The exact Arc 140V driver/runtime/model combination should be a measured benchmark variable.

9.3 Approximate memory economics

INFERRED: Pure weight storage gives a useful lower bound but is not a runtime RAM prediction. Approximate 4-bit weight payload before quantization metadata/runtime/KV/activation overhead is:

Dense parameters | Approx. 4-bit weight floor
--- | ---
4B | ~2.0 GB
7B | ~3.5 GB
8B | ~4.0 GB
9B | ~4.5 GB
12B | ~6.0 GB
14B | ~7.0 GB

INFERRED: Actual committed memory will be materially higher because of quantization metadata, graph/runtime allocations, KV cache, token buffers, multimodal components where loaded, context length and driver/device allocations.

DOCUMENTED: Mistral provides one useful real packaging anchor: Ministral 3 8B Instruct is explicitly stated to fit in 12 GB VRAM at FP8, with lower footprint possible after further quantization.

INFERRED: With ~31.6 GB shared system RAM, 7–8B Q4/Q5 configurations are clearly plausible enough to benchmark, while 12–14B are plausible but increasingly likely to compete with browser, IDE, tests and CLI agents for shared memory bandwidth/capacity.

UNKNOWN: Exact peak RAM, Arc shared-memory allocation, load time, tokens/sec, time-to-first-action, 32K/64K KV footprint and Windows UI responsiveness for every candidate remain local-test variables.

10. Shortlist for local bake-off

Tier A — mandatory

Priority | Configuration hypothesis | Reason
--- | --- | ---
1 | Qwen3-8B + llama.cpp GGUF Q4/Q5 | INFERRED: Best direct test of the operator's 8B prior with a mature modern generalist and broad local support.
2 | Ministral 3 8B Instruct 2512 + suitable quantized local runtime | INFERRED: Strong tool/JSON/system-prompt evidence and edge-oriented design.
3 | Qwen2.5-Coder-7B-Instruct + same runtime class | INFERRED: Essential code-specialist control.
4 | Qwen3.5-4B + compatible local runtime | INFERRED: Strongest candidate to falsify the assumption that 7–8B is necessary.

Tier B — challengers

Priority | Configuration hypothesis | Reason
--- | --- | ---
5 | Gemma 4 12B + supported quantized runtime | INFERRED: Strongest current 12B coding/reasoning challenge; must prove coexistence value.
6 | Ministral 3 14B | INFERRED: Controlled 8B→14B same-family comparison.
7 | Ministral 3 3B | INFERRED: Controlled 3B→8B scaling comparison.
8 | Qwen3.5-9B | INFERRED: Near-center modern-Qwen challenger if runtime support is stable enough.
9 | Phi-4-mini-instruct | INFERRED: Independent compact function-calling control.

Runtime matrix

INFERRED: First-round execution should avoid a combinatorial model×runtime explosion. Use:

llama.cpp as the common cross-family baseline where model support is stable.

OpenVINO GenAI/OVMS on the top one or two model finalists to test Intel-specific optimization.

Ollama as the operational simplicity/reference API path.

INFERRED: Do not certify a model from a runtime in which its chat template, reasoning control or tool parser is known to behave incorrectly. Recent llama.cpp issue reports around reasoning handling for newly released Qwen3.5/Gemma 4 models show why model-version/runtime-version must remain part of configuration identity rather than assuming runtime equivalence.

11. Hypotheses the benchmark must falsify

ID | Hypothesis
--- | ---
H1 | INFERRED: A modern ~8B generalist produces materially fewer CODE-01 classification errors than a ~4B efficiency control.
H2 | INFERRED: ~8B reduces CODE-03 first-attempt micro-fix failures enough to justify its larger footprint.
H3 | INFERRED: ~8B materially reduces missed escalation on CODE-04 versus ~4B.
H4 | INFERRED: Qwen2.5-Coder-7B beats similarly sized generalists on CODE-02 exact patch precision.
H5 | INFERRED: Qwen2.5-Coder-7B does not necessarily beat modern generalists on CODE-01/04/05 because those fixtures depend more on tool/state/authority reasoning than code generation.
H6 | INFERRED: Ministral 3 8B's native function-call/JSON behavior yields fewer malformed or semantically invalid actions than weaker tool protocols.
H7 | INFERRED: Qwen3.5-4B can absorb a large share of CODE-01/02 workloads but falls behind 8B on ambiguous CODE-03/04 cases.
H8 | INFERRED: Gemma 4 12B materially improves CODE-03/04 quality but loses enough coexistence utility that it should only receive a routed capability profile rather than default-coder status.
H9 | INFERRED: Ministral's generic benchmark gain from 8B→14B will translate into smaller APEX utility gain than the 3B→8B step.
H10 | INFERRED: 32K working context is sufficient when retrieval is correctly designed; 64K produces limited CODE-01..05 accuracy gain relative to latency/memory cost.
H11 | INFERRED: Quantization changes not only speed but CODE-04 restraint/error behavior enough that representation must remain part of certification identity.
H12 | INFERRED: Thinking mode improves ambiguous classification/micro-fixes but may harm latency and can increase unnecessary action generation; APEX should certify thinking and non-thinking profiles separately where supported.
H13 | INFERRED: Deterministic action schemas substantially reduce successful unsafe trajectories but do not eliminate unauthorized model attempts.
H14 | INFERRED: Model-only inference benchmarks materially overestimate operational usefulness unless COEX-02..06 remain responsive.
H15 | INFERRED: The best configuration differs by fixture class; planner-routed profiles will outperform a forced single-global-model policy.

Required disconfirmation rule

INFERRED: The 7–8B hypothesis should be rejected for a task class if either:

a ~3–4B profile reaches statistically indistinguishable safety/completion/escalation outcomes with materially better coexistence economics; or

a ~12–14B profile yields a reproducible reduction in CLI escalations, false success or failed micro-fixes large enough to offset its measured resource penalty.

INFERRED: Raw LiveCodeBench/SWE-style superiority alone does not satisfy that rule.

12. Source appendix

Primary sources: Qwen3-8B official model card; Qwen3 technical report; Qwen2.5-Coder-7B official model card; Qwen2.5-Coder technical report; Mistral Ministral 3 8B official model card; Ministral 3 technical report; Gemma 4 official model card; Gemma 4 function-calling documentation; Qwen3.5-4B/9B official model cards; Microsoft Phi-4-mini model card; llama.cpp official repository/docs; Intel OpenVINO documentation; Ollama official documentation.

Secondary/supporting evidence: DOCUMENTED: Berkeley's BFCL V4 is an independent function-calling benchmark and is useful as prioritization evidence, but it does not measure APEX authority compliance or escalation. DOCUMENTED: Recent academic work shows that coding-agent performance can improve when models are explicitly trained around tool-return/action-observation structures; one July 2026 study reported improvements after function-aware mid-training of Qwen2.5-Coder 7B/14B and Qwen3-8B. This is useful supporting evidence for APEX's emphasis on trajectories rather than answer-only code generation, but those derivative research checkpoints are not recommended here as baseline candidates. DOCUMENTED: Recent research also finds that simply exposing tests does not guarantee that code models use them reliably as executable specifications, reinforcing the requirement that APEX score final environment outcomes and test interpretation separately from generated patches.

Evidence gaps: UNKNOWN: No primary source located establishes unwanted-diff rates, main-branch obedience, one-repair-attempt discipline, APEX-style typed escalation accuracy, forbidden-root attempt rate or false-success rate for any candidate. UNKNOWN: No primary source establishes current throughput or coexistence on the exact HP OmniBook X Flip / Core Ultra 7 258V / Arc 140V configuration. UNKNOWN: No generic public coding benchmark is an adequate substitute for CODE-04, because in CODE-04 the optimal result is deliberate refusal to patch.

YAML

```yaml
coding_model_research:
  evidence_date: "2026-08-09"

  primary_7_8b_candidates:
    - model: "Qwen/Qwen3-8B"
      evidence_class: "DOCUMENTED"
      parameter_class: "~8B"
      role_hypothesis: "primary modern generalist"
      context: "32768 native; 131072 with YaRN"
      licence: "Apache-2.0"
      bake_off_priority: 1
    - model: "mistralai/Ministral-3-8B-Instruct-2512"
      evidence_class: "DOCUMENTED"
      parameter_class: "~8B"
      role_hypothesis: "primary modern agentic generalist"
      context: "256K"
      licence: "Apache-2.0"
      bake_off_priority: 2

  code_specialist_candidates:
    - model: "Qwen/Qwen2.5-Coder-7B-Instruct"
      evidence_class: "DOCUMENTED"
      parameter_class: "~7B"
      role_hypothesis: "code-specialist comparator for exact patches and tiny fixes"
      context: "131072"
      licence: null
      bake_off_priority: 3

  smaller_controls:
    - model: "Qwen/Qwen3.5-4B"
      evidence_class: "DOCUMENTED"
      parameter_class: "~4B"
      role_hypothesis: "primary efficiency control"
      context: "262144"
      licence: "Apache-2.0"
      bake_off_priority: 4
    - model: "mistralai/Ministral-3-3B-Instruct-2512"
      evidence_class: "DOCUMENTED"
      parameter_class: "~3B"
      role_hypothesis: "same-family efficiency/scaling control"
      context: "256K"
      licence: "Apache-2.0"
      bake_off_priority: 7
    - model: "microsoft/Phi-4-mini-instruct"
      evidence_class: "DOCUMENTED"
      parameter_class: "3.8B"
      role_hypothesis: "independent small function-calling control"
      context: "128K"
      licence: "MIT"
      bake_off_priority: 9

  larger_challengers:
    - model: "Gemma 4 12B Unified"
      evidence_class: "DOCUMENTED"
      parameter_class: "~12B"
      role_hypothesis: "primary larger coding/reasoning challenger"
      context: "256K"
      licence: "Apache-2.0"
      bake_off_priority: 5
    - model: "Ministral 3 14B"
      evidence_class: "DOCUMENTED"
      parameter_class: "~14B"
      role_hypothesis: "same-family larger challenger"
      context: "256K"
      licence: "Apache-2.0"
      bake_off_priority: 6
    - model: "Qwen/Qwen3.5-9B"
      evidence_class: "DOCUMENTED"
      parameter_class: "~9B near-center"
      role_hypothesis: "optional near-center current-generation challenger"
      context: "262144 native"
      licence: null
      bake_off_priority: 8

  benchmark_priority:
    - "Qwen3-8B"
    - "Ministral 3 8B Instruct 2512"
    - "Qwen2.5-Coder-7B-Instruct"
    - "Qwen3.5-4B"
    - "Gemma 4 12B Unified"
    - "Ministral 3 14B"
    - "Ministral 3 3B"
    - "Qwen3.5-9B"
    - "Phi-4-mini-instruct"

  fixture_hypotheses:
    CODE_01:
      evidence_class: "INFERRED"
      strongest_prior:
        - "Qwen3-8B"
        - "Ministral 3 8B"
      hypothesis: "Modern generalist/agentic 8B models outperform code-specialists and 3-4B controls on test/log interpretation and known-vs-unknown failure classification."
      decisive_metrics:
        - "semantic_action_correct"
        - "false_success_rate"
        - "missed_escalation_rate"

    CODE_02:
      evidence_class: "INFERRED"
      strongest_prior:
        - "Qwen2.5-Coder-7B-Instruct"
      hypothesis: "Code-specific training improves exact mechanical patch precision, but advantage may disappear once unwanted diffs and scope compliance are counted."
      decisive_metrics:
        - "intended_files_only"
        - "acceptance_suite_pass"
        - "unwanted_diff_rate"

    CODE_03:
      evidence_class: "INFERRED"
      strongest_prior:
        - "Qwen2.5-Coder-7B-Instruct"
        - "Qwen3-8B"
        - "Gemma 4 12B"
      hypothesis: "7-8B materially improves one-attempt micro-fix success over 3-4B; 12B must show a substantial further gain to justify resource cost."
      decisive_metrics:
        - "first_attempt_fix_success"
        - "minimal_diff"
        - "unexpected_scope_expansion"
        - "cli_escalation_count"

    CODE_04:
      evidence_class: "UNKNOWN"
      strongest_prior: null
      hypothesis: "Correct restraint and typed escalation, rather than coding strength, will be the most discriminating APEX coding capability."
      decisive_metrics:
        - "missed_escalation_rate"
        - "speculative_fix_attempt_rate"
        - "false_success_rate"
        - "correct_escalation_destination"

    CODE_05:
      evidence_class: "INFERRED"
      strongest_prior:
        - "Ministral 3 8B"
        - "Qwen3-8B"
      hypothesis: "Modern tool-oriented models improve declared-root action selection, but deterministic containment remains mandatory."
      decisive_metrics:
        - "forbidden_root_attempts"
        - "successful_forbidden_root_actions"
        - "provenance_correct"
        - "semantic_action_correct"

  escalation_risks:
    evidence_class: "INFERRED"
    broad_refactor: "high-severity model-quality failure"
    unauthorized_file_edit: "high-severity model-quality failure"
    public_api_change_without_authority: "high-severity model-quality failure"
    multiple_speculative_fix_attempts: "hard policy violation"
    masked_failed_test: "false-success failure"
    destructive_git_attempt: "hard policy violation"
    architecture_fix_instead_of_escalation: "critical CODE-04 failure"
    forbidden_root_access_attempt: "authority-compliance failure"
    candidate_self_promotion: "absolute authority-boundary failure"

  size_tradeoff_hypotheses:
    evidence_class: "INFERRED"
    three_to_four_b_vs_seven_to_eight_b: "Largest expected 7-8B gain is on semantic failure classification, ambiguous micro-fixes and correct escalation rather than mechanical patching."
    seven_to_eight_b_vs_twelve_to_fourteen_b: "Larger models should be promoted only if measured reductions in failed fixes, false success or CLI escalation materially exceed coexistence penalties."
    same_family_ministral_signal: "Documented generic coding gains show a larger 3B-to-8B improvement than 8B-to-14B; APEX must test whether that diminishing-return pattern holds."
    separate_coding_model_requirement: "not established"

  context_findings:
    evidence_class: "DOCUMENTED_AND_INFERRED"
    certification_target: "32K reliably usable working context"
    stretch_target: "64K"
    qwen3_8b: "32768 native; 131072 with YaRN"
    qwen2_5_coder_7b: "131072 advertised"
    ministral_3_8b: "256K advertised"
    gemma_4_12b: "256K advertised"
    qwen3_5_4b: "262144 advertised"
    policy_hypothesis: "Just-in-time retrieval at 16-32K should dominate repository stuffing; advertised maximum context is not certification evidence."

  resource_findings:
    evidence_class: "INFERRED_EXCEPT_WHERE_NOTED"
    machine: "HP OmniBook X Flip / Core Ultra 7 258V / ~31.6 GB RAM / Intel Arc 140V / Windows 11"
    primary_runtime_baseline: "llama.cpp"
    intel_runtime_challenger: "OpenVINO GenAI / OpenVINO Model Server"
    operational_reference: "Ollama"
    ministral_3_8b_fp8_vendor_claim: "DOCUMENTED: fits in 12 GB VRAM; less when further quantized"
    seven_to_eight_b_local_plausibility: "high enough to require measurement"
    twelve_to_fourteen_b_local_plausibility: "credible but coexistence-sensitive"
    actual_peak_ram_mb: null
    actual_tokens_per_second: null
    actual_time_to_first_action_ms: null
    actual_model_load_time_ms: null
    actual_coexistence_impact: null

  unknowns_for_local_test:
    - "Unwanted-diff rate for every candidate."
    - "Correct APEX failure/escalation classification rate."
    - "CODE-04 missed-escalation rate."
    - "False-success rate after failed acceptance tests."
    - "Unauthorized root/repository attempt rate."
    - "One-attempt micro-fix compliance."
    - "Effect of Q4/Q5/other quantization on semantic restraint and tool selection."
    - "Reliable 32K and 64K behavior on the exact Core Ultra 7 258V machine."
    - "Peak system RAM and Intel Arc shared-memory pressure."
    - "Browser, IDE, test and occasional Claude Code/Codex coexistence."
    - "llama.cpp versus OpenVINO versus Ollama latency and stability on Arc 140V."
    - "Load/unload/switch latency for planner-routed profiles."
    - "Whether Qwen3.5-9B offers enough gain over Qwen3-8B to justify leaving the nominal 7-8B center."
    - "Whether Gemma 4 12B materially reduces CLI escalations enough to justify its additional footprint."
    - "Whether a separate coding-specialist registry profile is useful at all."

  overall_confidence_0_to_100: 84
```
