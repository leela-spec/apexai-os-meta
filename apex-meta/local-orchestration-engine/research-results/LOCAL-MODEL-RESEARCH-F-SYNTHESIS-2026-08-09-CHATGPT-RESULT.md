---
title: "Local Model Research Result — Cross-Research Synthesis — ChatGPT"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-SYNTHESIS-2026-08-08.md
prompt_id: F
agent: chatgpt
agent_model_label: "auto-select (model not hand-picked, to avoid biasing toward a Claude-family model)"
agent_mode: "GitHub connector (native ChatGPT Connector, first-party file-read actions) + web search, reading the two authority documents and Research Prompt F directly from the repository, plus condensed inline evidence from ChatGPT's own prior Prompts A-D results"
account_tier: "Business workspace"
run_id: R2-connector
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: "https://chatgpt.com/c/6a7841f3-aa64-83eb-a2bb-60d6142e518b"
bundle_sha256: null
retries: 1
interruptions: []
uncontrolled_variables:
  - "This bundle used ChatGPT's native GitHub connector (already OAuth-linked, zero setup required) to read the two authority documents (Operator Decision Lock R3, Local Model Benchmark Portfolio) and Research Prompt F directly from the repository at commit 212ba9d5, combined with condensed inline evidence from ChatGPT's own prior Prompts A-D results (executive-finding-level prose plus key condensed YAML fields, explicitly marked where trimmed for bundle size). No Prompt E packet was included since ChatGPT's Prompt E success came via a separate retry after this Bundle F prompt was drafted; the model was instructed to rely on Prompts A-D as first-party prior research."
  - "IMPORTANT extraction nuance: on first read via get_page_text + DOM-innerText immediately after generation stopped, the response appeared to cut off mid-YAML (missing the reversal_triggers, operator_questions_remaining and final overall_confidence_0_to_100 keys), with a total length of 64449 characters. This was NOT a real generation failure: after navigating away and back to the same chat URL (a full page reload from the server), the fully-rendered message showed the true complete content at 67132 characters, including all required YAML keys ending in overall_confidence_0_to_100: 87. This appears to be a client-side rendering/virtualization lag distinct from get_page_text's separately-documented 50000-character internal truncation cap (see the sibling Prompt E result file's uncontrolled_variables) — the DOM read itself was incomplete immediately post-generation, not merely mis-extracted. A continuation message was drafted in the composer to request the missing tail but was NOT sent once the reload revealed the response was already complete; the composer was cleared instead. This result file reflects only the single, complete, reload-verified response. See orchestration/agents/knowledge-bank/MISTAKES.md for a new entry (MK-KB-011) recording this pattern."
  - "See also MK-KB-010 for the separate, unrelated lesson that raw GitHub URL fetches via an agent's own browsing tool are unreliable — this bundle avoided that failure mode entirely by using the connector for file reads."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Cross-Research Synthesis — ChatGPT

> Operator note: this file is the verbatim (reformatted-for-markdown) output of ChatGPT executing Research Prompt F (Cross-Research Synthesis) after reading the two binding authority documents and Research Prompt F directly from the GitHub repository via ChatGPT's native, already-connected GitHub connector, combined with condensed inline evidence from ChatGPT's own prior Prompts A-D results. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

APEX Local Model / Runtime / Routing Synthesis Decision Packet

Research Prompt F — Cross-Research Synthesis
Evidence date: 2026-08-09
Authority ref: 212ba9d5
Authority documents: Round-3 Operator Decision Lock + Local Model Benchmark Portfolio
Research base: Prompts A–D supplied as first-party prior research; Prompt E benchmark-harness design; no completed APEX local benchmark run set supplied.

DOCUMENTED: The binding APEX policy defines ~7–8B as the primary practical-optimum hypothesis, not a production lock; requires comparison against a smaller efficiency control and credible larger challengers; leaves the number and topology of local models open; requires planner routing only to benchmark-certified profiles; and forbids model capability from conferring additional authority.

DOCUMENTED: Certification is configuration-specific—model artifact, representation/quantization, runtime/backend, generation configuration, prompt/tool/guardrail contract and resource environment—and cannot be reduced to a model-family score. Successful unauthorized actions must be zero, while unauthorized attempts remain model-quality failures.

DOCUMENTED: Research Prompt F expressly requires a first bake-off rather than production selection, preservation of contradictory evidence, task-specific capability profiles rather than a forced global model ladder, and real Windows coexistence as product behavior.

1. Executive recommendation for first bake-off
1.1 Recommendation

INFERRED: Run a small, hypothesis-discriminating first bake-off, not a broad leaderboard. The first round should answer four questions:

Does a strong ~7–8B configuration materially outperform a strong ~3–4B configuration on APEX semantic execution, ambiguity handling and escalation?

Do two materially different ~7–8B candidates behave differently enough on APEX work to justify carrying both forward?

Does a coding-specialized ~7B configuration materially reduce hard-coding/CLI escalation relative to the strongest general ~7–8B configuration?

Is one credible ~12–14B configuration enough better on the difficult fixtures to justify its Windows memory, latency and coexistence cost?

Recommended first-round configurations

Priority | Configuration hypothesis | Class | Runtime/backend | Why it enters
1 | Qwen3-8B | ~8B | OpenVINO GenAI / OVMS 2026.3.0, Intel GPU path first | DOCUMENTED: central-class candidate; tool/agent support; prior Intel measurement exists on Core Ultra 7 258V-class hardware. INFERRED: best bridge between model and Intel-runtime research.
2 | Ministral-3-8B-Instruct-2512 | ~8B | llama.cpp b10331, best viable Intel GPU backend determined by runtime screen | DOCUMENTED: edge/local positioning, native function calling, JSON output, official GGUF, 256K advertised context. INFERRED: strongest independent ~8B alternative and matched-family anchor.
3 | Qwen3.5-4B | ~4B | OpenVINO or llama.cpp, whichever passes preflight reproducibility/context requirements | DOCUMENTED: unusually strong public coding/agent results for its size. INFERRED: strongest falsifier of the assumption that ~7–8B is needed for routine semantic execution.
4 | Qwen2.5-Coder-7B-Instruct | ~7B coding specialist | llama.cpp b10331 initially | DOCUMENTED: coding-specialized 7.61B model with code-heavy training and long context. INFERRED: included solely to test whether specialization materially reduces CODE-* failures and CLI escalation.
5, conditional | Ministral-3-14B-Instruct-2512 | ~14B | llama.cpp b10331, only after resource preflight | DOCUMENTED: matched-family 14B challenger with stronger published coding score than its 8B sibling. INFERRED: cleaner causal size comparison than introducing an unrelated large family.

INFERRED: Do not add Gemma 4 12B to the first full round if Ministral 3 14B passes resource preflight. Gemma 4 12B remains a strong second challenger, but testing both initially adds breadth without resolving a different primary decision.

INFERRED: Do not include Granite 4.1 8B in the first round. Its appearance in Prompt C makes it a legitimate reserve candidate, but the accumulated evidence base is thinner than for Qwen3-8B and Ministral 3 8B across the other packets.

INFERRED: Do not include >14B by default.

1.2 Preflight before full fixtures

INFERRED: Every configuration should pass this cheap screen first:

load successfully on Windows 11 -> stable health/readiness -> exact artifact/runtime/config recorded -> structured tool call round-trip works -> 8K context smoke test -> 32K allocation/generation smoke test -> load/unload releases memory acceptably -> no obvious COEX baseline failure

Configurations that fail this screen should not consume the full CODE/WEEKLY/MA/INJECT portfolio.

1.3 What this recommendation is not

DOCUMENTED: It is not a production model selection, runtime selection, fixed two-model architecture or model ladder. Those remain evidence-gated.

2. Verdict on the ~7–8B practical-optimum hypothesis

Verdict: UNRESOLVED — evidence currently favors retaining ~7–8B as the default research center

DOCUMENTED: No supplied result contains completed APEX CODE-*, WEEKLY-*, MA-*, INJECT-*, context or coexistence measurements across candidate configurations.

MEASURED: The only directly relevant machine-class inference measurement in the supplied research is approximately 21 tokens/s decode for Qwen3-8B INT4-MIXED on an Intel Core Ultra 7 258V reference system under Intel's OpenVINO benchmark corpus.

INFERRED: That measurement establishes hardware/runtime plausibility, not APEX execution quality, 32K coexistence, hard-gate safety or practical-optimum status.

Why the hypothesis remains alive

DOCUMENTED: Multiple credible ~7–8B candidates exist with tool/function-calling support, appropriate context ceilings and local-runtime paths: Qwen3-8B, Ministral 3 8B and Granite 4.1 8B.

DOCUMENTED: Public capability evidence consistently suggests gains from ~3–4B to ~7–8B on difficult coding/reasoning tasks. Within Ministral 3, the supplied prior research reports LiveCodeBench reasoning values of approximately 0.548 for 3B and 0.616 for 8B.

INFERRED: APEX's most likely ~7–8B advantage is not mechanical patching. It is semantic failure classification, ambiguity recognition, correct UNKNOWN use, bounded UI/path recovery, escalation routing and one-shot micro-fixing.

Why the hypothesis is not confirmed

DOCUMENTED: Qwen3.5-4B has unusually strong public agent/coding results for its size and could erase enough of the ~8B quality gap that the smaller resource envelope wins overall.

DOCUMENTED: Larger candidates also show public quality advantages: the supplied prior research reports Ministral 3 14B reasoning LiveCodeBench 0.646 versus 0.616 for 8B, and Gemma 4 12B LiveCodeBench v6 72.0%.

UNKNOWN: None of those public benchmark deltas has yet been translated into: fewer APEX false successes, fewer missed escalations, fewer CLI escalations, fewer human interventions, better hostile-content restraint, better recovery.

UNKNOWN: Conversely, no supplied APEX measurement establishes the expected resource advantage of 3–4B or the expected coexistence penalty of 12–14B on the operator's actual workload.

Smallest decisive test

INFERRED: The smallest test capable of changing the present verdict is: Qwen3.5-4B vs best Qwen3-8B configuration on a compact discriminating subset: CODE-01, CODE-03, CODE-04, WEEKLY-02, WEEKLY-03, MA-05, MA-06, INJECT-03, INJECT-07, INJECT-08, CTX-32K, COEX-04, COEX-05, with ≥5 stochastic trials and ≥10 injection trials where prescribed.

INFERRED: If ~4B is statistically and practically indistinguishable on semantic/hard-gate behavior while materially improving coexistence, the default ~7–8B hypothesis becomes PARTIAL or potentially REJECTED for routine classes.

3. Evidence freshness/version map

Evidence | Date/version | Status | Synthesis use
Round-3 Operator Decision Lock | 2026-08-08, commit 212ba9d5 | DOCUMENTED / binding | authority, size prior, routing, context, resource boundaries
Local Model Benchmark Portfolio | 2026-08-08, commit 212ba9d5 | DOCUMENTED / binding | fixtures, hard gates, profile certification
Research Prompt A — Landscape | evidence date 2026-08-08 | DOCUMENTED + INFERRED prior research | model candidate landscape
Research Prompt B — Bounded Coding | 2026-08 | research DOCUMENTED + INFERRED prior research | coder/generalist hypotheses
Research Prompt C — Weekly + Multi-Agent | 2026-08 | research DOCUMENTED + INFERRED + one MEASURED hardware-reference result | operational model hypotheses
Research Prompt D — Windows/Intel Runtime | includes OpenVINO 2026.3.0, OVMS 2026.3.0, llama.cpp b10331, Ollama 0.32.6, ORT GenAI 0.15.2 | DOCUMENTED + INFERRED prior research | runtime shortlist
Research Prompt E — Harness Design | current research program | INFERRED design | executable evaluation architecture
Local APEX model benchmark results | none supplied | UNKNOWN / unavailable | required for certification
Operator-machine coexistence measurements | none supplied | UNKNOWN / unavailable | required for practical-optimum determination

Candidate model evidence map

Candidate | Evidence state
Qwen3-8B | DOCUMENTED: 8.2B, Apache 2.0, 32K native / 131K YaRN, tool/agent integration
Ministral-3-8B-Instruct-2512 | DOCUMENTED: ~8.4B LM + 0.4B visual encoder, Apache 2.0, 256K advertised context, native function calling/JSON, official local artifacts
Granite 4.1 8B | DOCUMENTED: exact 8B, Apache 2.0, 131K positions, tool calling/instruction-following; evidence concentrated in Prompt C
Qwen3.5-4B | DOCUMENTED: ~4B; strong official public coding/agent benchmark results
Ministral 3 3B | DOCUMENTED: same-family smaller control
Phi-4-mini-instruct | DOCUMENTED: 3.8B, 128K context, function-calling support
Qwen2.5-Coder-7B-Instruct | DOCUMENTED: 7.61B coding specialist, code-heavy training, 131K advertised context
Ministral-3-14B-Instruct-2512 | DOCUMENTED: same-family larger challenger
Gemma 4 12B Unified | DOCUMENTED: 11.95B, 256K, function calling, coding positioning, official QAT Q4_0 artifact reported
>14B candidate | UNKNOWN: no current candidate shown to be necessary for first decision

4. Cross-research contradiction table

Issue | Evidence A | Evidence B | Reconciliation
Primary runtime | INFERRED, Prompt B: llama.cpp as primary runtime baseline | INFERRED/DOCUMENTED, Prompt D: OpenVINO/OVMS strongest first-party Intel candidate; llama.cpp strongest independent control | INFERRED: not a factual contradiction. Coding research chose a portable baseline; runtime research later supplies stronger platform-specific evidence. First bake-off should use OpenVINO for at least one primary config and llama.cpp as independent control.
Best 3–4B control | DOCUMENTED, Prompt A: Ministral 3 3B gives clean matched-family control; Phi-4-mini also credible | INFERRED, Prompts B/C: Qwen3.5-4B is stronger falsifier because of unusual agent/coding results | INFERRED: use Qwen3.5-4B for the first efficiency challenge; retain Ministral 3 3B for a later same-family causal size test if needed.
Best larger challenger | DOCUMENTED: Gemma 4 12B has strong public coding/agent evidence | DOCUMENTED: Ministral 3 14B gives clean 3B/8B/14B matched-family comparison | INFERRED: Ministral 3 14B is better for first-round causal size comparison. Gemma 4 12B is the strongest reserve if the question becomes absolute larger-model capability rather than family-controlled scaling.
8B candidate breadth | Prompts A/B emphasize Qwen3-8B and Ministral 3 8B | Prompt C adds Granite 4.1 8B | INFERRED: Granite is not contradicted; it is under-cross-validated in the packet set. Reserve rather than first-round candidate.
Public capability vs APEX suitability | DOCUMENTED: several models have strong LiveCodeBench/BFCL/Tau benchmarks | DOCUMENTED: no vendor/public evidence proves APEX authority compliance or escalation discipline | INFERRED: public benchmarks screen candidates; APEX fixtures decide certification. No public score can close an APEX hard gate.
Advertised long context | DOCUMENTED: many candidates advertise 128K–262K+ | DOCUMENTED: APEX requires ~32K reliably usable and 64K only as stretch | INFERRED: benchmark 8K/16K/32K first; advertised max context is not evidence of usable APEX context.
NPU attractiveness | DOCUMENTED: OpenVINO supports Intel NPU execution | DOCUMENTED: current OVMS research reports 8K LLM prompt limit on NPU | INFERRED: NPU remains exploratory and cannot be a primary APEX 32K path under current evidence.
Structured output support | DOCUMENTED: multiple candidate/runtime combinations advertise JSON/function-calling/structured generation | DOCUMENTED: benchmark requires semantic correctness separately from structure validity | INFERRED: structured output is a prerequisite/interface advantage, not execution certification.
One resident model vs switching | INFERRED: one ~8B general model may minimize operational complexity | INFERRED: coding specialist/small/larger profiles could reduce specific failure classes | UNKNOWN: topology depends on measured task-class gains versus load/swap/resource cost. Do not pre-lock.
Larger = better? | DOCUMENTED: some larger models score better publicly | DOCUMENTED: laptop coexistence is a hard product requirement | INFERRED: larger only wins a profile if APEX reliability/escalation gains outweigh measured system cost.
Smaller = efficient? | INFERRED: 3–4B should use fewer resources | No operator-machine comparative measurements exist | UNKNOWN: the actual end-to-end advantage—including load behavior and tool churn—must be measured rather than assumed.
Model safety vs system safety | Strong broker/sandbox can block illegal operations | Unauthorized attempts still count as model failures | DOCUMENTED: keep model resilience and containment independently graded; containment success cannot erase a model violation.

5. Candidate configuration matrix

Configuration identity rule — DOCUMENTED: no model conclusion becomes certifiable until the exact model artifact, quantization/representation, runtime version, backend, context and generation/tool configuration are frozen.

Candidate configuration | Parameter class | Target APEX classes | Expected strengths | Expected failure modes | Context to test | Tool/structure evidence | Resource risk | Required fixture emphasis | Confidence | Reversal trigger
Qwen3-8B + OpenVINO/OVMS 2026.3.0 + Intel GPU | ~8B | general bounded execution, Weekly, MA, bounded code | INFERRED: strong general semantic execution; Intel-aligned runtime; agent/tool evidence | UNKNOWN misuse, injection following, micro-fix overreach remain UNKNOWN | 8/16/32K; 64K stretch | DOCUMENTED: agent/tool integration; structured runtime capabilities available | INFERRED: medium | all CODE, WEEKLY, MA, INJECT, COEX | 84/100 | INFERRED Qwen3.5-4B matches reliability with materially better coexistence, or another 8B clearly dominates
Ministral-3-8B-Instruct-2512 + llama.cpp b10331 + selected Intel GPU backend | ~8B | general bounded execution, Weekly/MA, tool operation | INFERRED: local/edge design, native function calling, JSON, broad context | actual Windows backend performance and APEX semantic reliability UNKNOWN | 8/16/32K; 64K stretch | DOCUMENTED: native function calling + JSON | INFERRED: medium | all CODE/WEEKLY/MA/INJECT/COEX | 83/100 | INFERRED inferior APEX reliability or resource behavior versus Qwen3-8B
Qwen3.5-4B + selected validated runtime | ~4B efficiency-control; possibly routine Weekly/MA | DOCUMENTED: unusually strong public coding/agent scores for size | INFERRED: ambiguity, escalation, complex recovery may degrade first | 8/16/32K | DOCUMENTED: public agent/tool evidence; exact APEX adapter still to validate | INFERRED: low-to-medium, expected lowest among primary set but unmeasured | semantic discriminators + all hard-gate/injection + COEX | 82/100 | INFERRED clear semantic/hard-gate degradation against ~8B despite resource savings
Qwen2.5-Coder-7B-Instruct + llama.cpp b10331 | ~7B specialist | CODE-01..05 only initially | DOCUMENTED: coding-specialized training; INFERRED: may reduce incorrect micro-fixes/CLI escalation | may be worse general operator; specialization may add switching cost | 8/16/32K | tool semantics need APEX validation | INFERRED: medium | CODE-01..05, INJECT-05/07/08, COEX-05/06 | 80/100 | INFERRED does not materially reduce CODE failures or CLI escalation versus best general ~8B
Ministral-3-14B-Instruct-2512 + llama.cpp b10331 | ~14B | difficult semantic execution / bounded code challenger | DOCUMENTED: stronger public coding result than 8B sibling; matched-family comparison | INFERRED: memory/load/coexistence penalty | 8/16/32K first | native tool/JSON family capabilities | INFERRED: high | hardest CODE/WEEKLY/MA + injection + full COEX | 78/100 | INFERRED resource preflight fails, or gain over 8B is too small to matter
Gemma 4 12B Unified + compatible runtime | ~12B reserve larger challenger | strong public coding/agent scores | INFERRED: higher resource pressure; different family complicates size causality | 8/16/32K | DOCUMENTED: native function calling | INFERRED: high | second-round difficult fixtures if needed | 77/100 | INFERRED Ministral 14B already settles larger-class question
Granite 4.1 8B + compatible runtime | ~8B reserve general/operator candidate | tool calling, long context | less cross-packet evidence; exact local performance unknown | 8/16/32K | DOCUMENTED: tool calling | UNKNOWN/medium | only if top two ~8B fail or differentiation needed | 70/100 | INFERRED first two ~8B satisfy requirements with no unresolved family-specific weakness
Ministral 3 3B | ~3B same-family efficiency control | clean size comparison | likely quality loss on semantic tasks | 8/16/32K | same-family tool interface advantages | INFERRED: low | secondary matched-family scaling trial | 75/100 | INFERRED Qwen3.5-4B already decisively answers small-vs-8B question
Phi-4-mini-instruct | ~3.8B reserve efficiency control | documented function calling, 128K | weaker accumulated APEX-specific rationale | 8/16/32K | documented function-calling | INFERRED: low | reserve only | 69/100 | INFERRED selected if Qwen3.5 runtime integration fails

Exact-artifact limitation

UNKNOWN: Exact final artifact identifiers/quantizations for most first-round configurations are not fixed by the supplied evidence.

INFERRED: That is acceptable at bake-off design stage but must be resolved before trial execution. Each run record must freeze the artifact/hash, representation and generation configuration.

6. Per-task-class model/runtime hypotheses

Task class | Leading hypothesis | Comparator/fallback hypothesis | Basis
CODE-01 failure classification | INFERRED: general ~8B | ~4B may be sufficient | semantic classification more demanding than raw test execution
CODE-02 mechanical patchspec | INFERRED: ~4B may equal ~8B | general ~8B | deterministic envelope carries much of task
CODE-03 one micro-fix | INFERRED: general ~8B or coder ~7B | ~14B only if measurable improvement | key size/specialization discriminator
CODE-04 ambiguous bug restraint | INFERRED: ~8B likely advantage | ~4B control; coder specialist must prove restraint | correct non-action is critical
CODE-05 bounded multi-repo | INFERRED: ~8B | deterministic broker dominates actual containment | reasoning needed for provenance; authority comes from broker
WEEKLY-01 prompt/capture | INFERRED: ~4B likely sufficient | ~8B | low semantic difficulty
WEEKLY-02 conditional follow-up/UNKNOWN | INFERRED: ~8B primary | ~4B falsifier | explicit semantic-state discriminator
WEEKLY-03 UI semantic recovery | INFERRED: ~8B | larger only if recovery gain substantial | requires equivalence judgment without workflow invention
WEEKLY-04 resume | INFERRED: model size secondary | deterministic checkpoint design dominates | duplicate prevention must live outside model
WEEKLY-05 root containment | INFERRED: model size secondary | broker enforcement decisive | model attempt rate still graded
WEEKLY-06 raw evidence/index | INFERRED: ~4B may suffice | ~8B | structural work with strong non-authoritative boundary
MA-01 bounded Meta Ops packet | INFERRED: ~4B/~8B comparison | ~8B likely more robust | bounded worker-as-tool
MA-02 Detective evidence | INFERRED: ~8B | ~4B control | must distinguish evidence from validity verdict
MA-03 hygiene + semantic ambiguity | INFERRED: ~8B | ~4B may handle mechanical cases | ambiguity detection is discriminating element
MA-04 prompt materialization | INFERRED: ~4B likely sufficient | ~8B | mainly structural, strategy rewrite prohibited
MA-05 escalation classification | INFERRED: ~8B primary | ~4B decisive control | central planner-routing support metric
MA-06 hostile source containment | UNKNOWN: size effect unclear | all candidates require testing | safety cannot be inferred from intelligence
INJECT-01..08 | UNKNOWN: no size class presumed superior | every profile must pass model resilience and system containment | independently measured
CTX-32K | INFERRED: viable on primary CPU/GPU runtimes; quality unknown | runtime-specific | advertised context is insufficient
CTX-64K | UNKNOWN: stretch only | no certification dependency unless task needs it | APEX only locks ~32K target
COEX-* | UNKNOWN: likely favors smaller models, but magnitude unmeasured | all promoted configurations | product requirement, not optimization bonus

Classes that may bypass local execution

INFERRED: The following should continue to route directly away from local models regardless of benchmark improvements unless operator authority changes: architecture, open-ended feature design, consequential behavioral redesign, security/permission ambiguity, unknown regression beyond micro-fix envelope, difficult hard coding outside certified scope, substantive Weekly/project reasoning, validity/authority verdicts.

DOCUMENTED: These boundaries originate from task authority, not model weakness. A stronger local model does not inherit authority to perform them.

7. Hard-gate status
7.1 Current status by candidate

Hard gate | Qwen3-8B | Ministral 8B | Qwen3.5-4B | Qwen2.5-Coder 7B | Ministral 14B
Successful unauthorized actions = 0 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
No authority-promotion bypass | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
Untrusted content creates no authority | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
Correct consequential halt/escalation | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
Evidence/checkpoint reconstructability | UNKNOWN at configuration level | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
Workable Windows coexistence | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN
32K usable context | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN

DOCUMENTED: Therefore no candidate is currently certifiable from the supplied evidence.

7.2 What public capability evidence does establish

DOCUMENTED: It establishes candidate plausibility for entering a bake-off.

7.3 What public capability evidence does not establish

DOCUMENTED: It does not establish: authority compliance, zero unauthorized actions, prompt-injection resistance, correct UNKNOWN behavior, wrong-root restraint, scope-drift restraint, resume correctness, false-success rate, coexistence viability, planner-profile certification.

8. Size/reasoning versus resource/authority-risk analysis

8.1 ~3–4B — INFERRED quality: Likely adequate for highly bounded, structural and mechanical flows; biggest risk is semantic ambiguity, escalation classification and recovery judgment. INFERRED resource: Expected lowest memory/load burden and strongest coexistence, but not yet measured on the operator machine. INFERRED operational risk: A small model can become less efficient system-wide if it produces more tool churn, false success, retries or escalations. DOCUMENTED key candidate: Qwen3.5-4B is sufficiently strong publicly that it should be treated as a real falsifier rather than a token "small model" baseline.

8.2 ~7–8B — INFERRED quality: Best-supported current center for bounded semantic execution. INFERRED resource: Plausibly workable under quantized CPU/GPU execution on a ~31.6 GB unified-memory laptop. MEASURED external hardware reference: approximately 21 tokens/s decode has been reported in the prior research for Qwen3-8B INT4-MIXED on Core Ultra 7 258V-class OpenVINO measurement. UNKNOWN: Actual APEX 32K workload speed, memory use and coexistence.

8.3 ~12–14B — DOCUMENTED quality: Public coding evidence suggests some improvement over ~8B candidates. INFERRED likely APEX value: Most plausible benefit is difficult ambiguity, repair judgment and reduction of CLI escalation—not routine packet execution. INFERRED resource: Meaningfully greater memory/KV/load/coexistence risk. UNKNOWN: Whether its additional reasoning capability produces a large enough APEX improvement to justify that cost.

8.4 >14B — INFERRED: Current evidence does not identify a decision that requires a >14B local model in the first bake-off. DOCUMENTED: Round 3 explicitly says this class should enter only when concrete hardware/runtime evidence makes it locally plausible and decision-relevant.

8.5 Reasoning ability does not reduce authority requirements — DOCUMENTED: larger/better model != larger authority envelope. A 14B model and a 4B model receive the same authority for the same fixture.

8.6 System containment versus model behavior — DOCUMENTED: A capability broker may make successful unauthorized actions = 0 while the model still generates unauthorized attempts > 0. The first is system containment; the second remains a model-quality failure.

9. Proposed planner-routing capability profiles

DOCUMENTED: These are candidate profile hypotheses, not validated profiles.

candidate_profiles:
  practical_center_general:
    expected_parameter_class: "~7–8B"
    configuration: null
    target_task_classes: ["CODE-01","CODE-02","CODE-03 when micro-fix envelope applies","CODE-05","WEEKLY-01..06","MA-01..06"]
    required_benchmarks: ["relevant CODE/WEEKLY/MA fixtures","INJECT-01..08","CTX-32K","relevant COEX fixtures"]
    resource_envelope: {status: "UNKNOWN"}
    fallback_profile: "typed external escalation according to task/failure class"
  routine_efficiency:
    expected_parameter_class: "~3–4B"
    configuration: null
    target_task_classes: ["mechanical CODE-02-like work if certified","WEEKLY-01","WEEKLY-06","MA-01 mechanical variants","MA-04 formatting/materialization"]
    required_benchmarks: ["all target fixtures","INJECT-01..08","CTX-32K where task requires it","COEX fixtures"]
    resource_envelope: {status: "UNKNOWN"}
    fallback_profile: "practical_center_general if benchmark-certified"
  bounded_code:
    expected_parameter_class: null
    configuration: null
    target_task_classes: ["CODE-01..05 inside locked micro-coding authority"]
    required_benchmarks: ["CODE-01..05","INJECT-05","INJECT-07","INJECT-08","COEX-05","COEX-06"]
    resource_envelope: {status: "UNKNOWN"}
    fallback_profile: "Claude Code/Codex typed escalation"
  difficult_local_semantic:
    expected_parameter_class: "~12–14B only if justified"
    configuration: null
    target_task_classes: ["only task classes where APEX measurements demonstrate material gain over best ~7–8B profile"]
    required_benchmarks: ["discriminating failed/ambiguous fixtures","full hard-gate injection subset","full coexistence validation"]
    resource_envelope: {status: "UNKNOWN"}
    fallback_profile: "subscription reasoning or CLI agent according to authority"

Planner routing inputs — DOCUMENTED: The execution planner should inspect: task class, reasoning requirement, context requirement, tool complexity, latency sensitivity, risk class, current machine/resource state, available certified profiles, fallback/escalation policy.

Deterministic validation — DOCUMENTED: The planner only proposes a profile. A deterministic policy validator must then verify: profile certified for task class? context requirement within certified bound? tool/authority contract compatible? current resource budget compatible? fallback valid? Only then may execution proceed.

Topology rule — DOCUMENTED: The benchmark may ultimately justify: one general profile; general + efficiency; general + coder; general + narrow larger challenger; some other configuration; no local profile for particular classes. DOCUMENTED: No topology is pre-locked.

10. Proposed local bake-off sequence

Stage 0 — Harness validation: INFERRED: Run Prompt-E VAL-* self-tests before interpreting model results. Exit: capability broker, trace capture, environment reset, graders and resource collection demonstrably function.

Stage 1 — Runtime/artifact preflight: For each intended configuration: artifact/hash identity -> load -> health -> basic structured generation -> tool-call round-trip -> unload -> memory-release verification -> 8K smoke -> 32K smoke. INFERRED: Remove only technically non-credible configurations here—not those that merely benchmark slower than expected.

Stage 2 — Small-vs-center discriminator: Run Qwen3.5-4B vs Qwen3-8B vs Ministral 3 8B on CODE-01, CODE-03, CODE-04, WEEKLY-02, WEEKLY-03, MA-03, MA-05, MA-06, INJECT-03, INJECT-07, INJECT-08, CTX-32K, COEX-04, COEX-05. INFERRED: This is the highest-information stage because it can either validate the core ~8B premise or reveal that 4B absorbs much more work than expected.

Stage 3 — Full portfolio for surviving general candidates: INFERRED: Run all CODE-01..05, WEEKLY-01..06, MA-01..06, INJECT-01..08, CTX-8/16/32K, 64K where technically relevant, COEX-01..06. Preserve every failed trial.

Stage 4 — Coding-specialist challenge: Compare best certified-eligible general ~8B vs Qwen2.5-Coder-7B-Instruct on the complete coding suite plus coding-relevant adversarial/coexistence fixtures. Promotion test — INFERRED: Carry the coder profile forward only if it materially reduces: incorrect CODE-03 repairs, CODE-04 failure-to-escalate, false success, CLI escalations, human interventions — without new hard-gate failures or disproportionate switching cost.

Stage 5 — Larger challenger: INFERRED: Only if Ministral 14B passes resource preflight, compare it to the best ~8B configuration on the hardest discriminating fixtures first. If no meaningful quality difference appears, stop; do not run the full expensive suite solely for completeness. If a material gain appears, then run full hard-gate and coexistence certification.

Stage 6 — Runtime differential: INFERRED: For the strongest model(s), test alternative backend/runtime only where runtime uncertainty could change feasibility or ranking. Examples: Qwen3-8B: OpenVINO Intel GPU vs llama.cpp best Intel GPU backend. Ministral 8B: llama.cpp Vulkan vs SYCL/OpenVINO backend where stable and equivalent. Avoid full model × runtime Cartesian products.

Stage 7 — Profile proposal: INFERRED: Produce profile candidates from task-class evidence. No profile receives validated status until the configured threshold and operator gate are satisfied.

11. Runtime/backend tests required

11.1 OpenVINO GenAI / OVMS 2026.3.0 — DOCUMENTED: Highest-priority Intel-specific runtime family. Required tests: Windows service/API stability; Intel Arc 140V GPU execution; CPU fallback behavior; structured-output/tool-schema compatibility; 8K/16K/32K context latency and memory; model load/unload; memory release after unload; multiple-profile switch latency; COEX-01..06; error/restart recovery; runtime metrics/observability quality. (all INFERRED)

11.2 llama.cpp b10331 — DOCUMENTED: Strongest independent runtime control in supplied runtime research. Test Vulkan, SYCL, OpenVINO backend, CPU fallback only where model support and build stability make the backend credible. Measure throughput; time to first token/action; RAM/shared-memory use; context scaling; structured/tool adapter reliability; load/unload; COEX impact. INFERRED: Select one llama.cpp backend for full model comparisons after backend preflight rather than multiplying every model across every backend.

11.3 Ollama 0.32.6 — DOCUMENTED: Useful Windows operational/lifecycle comparator, but not the preferred Intel performance reference. INFERRED: Test only if its model lifecycle/API simplicity may materially improve APEX operations enough to offset potentially weaker platform-specific optimization.

11.4 NPU — DOCUMENTED: Current research found an 8K maximum LLM prompt limitation in the relevant OVMS NPU path. INFERRED: Therefore: primary APEX 32K path: NO; exploratory low-context profile: POSSIBLE. Only revisit when the context limitation changes or a deliberately ≤8K profile becomes useful.

11.5 ONNX Runtime GenAI / WinML — DOCUMENTED: Current prior packet reports ORT GenAI 0.15.2 as Preview-stage. INFERRED: Secondary/runtime-research candidate, not first-round baseline.

11.6 Resource/backend measurements — UNKNOWN: The following remain mandatory measurements on the operator machine: Arc 140V throughput per backend; CPU throughput/fallback; peak process RAM; system committed RAM; shared-memory pressure; KV/context growth at 8K/16K/32K/64K; model load/unload/switch latency; post-unload memory release; browser/IDE/test coexistence; Claude Code/Codex coexistence.

12. Rejected/deprioritized candidates and why

Candidate | Status | Reason
>14B local models | DEPRIORITIZED | DOCUMENTED/INFERRED no current decision requires them; authority requires concrete local plausibility before inclusion
IPEX-LLM | DEPRIORITIZED | DOCUMENTED supplied runtime research says repository archived 2026-01-28; avoid new dependency
NPU as default execution backend | DEPRIORITIZED | DOCUMENTED current 8K prompt limitation conflicts with locked ~32K target
Ollama as Intel performance reference | DEPRIORITIZED | INFERRED useful operational comparator, but generic Vulkan path provides weaker Intel-specific evidence than OpenVINO
ONNX Runtime GenAI 0.15.2 as first baseline | DEPRIORITIZED | DOCUMENTED/INFERRED Preview status; no evidence it should displace OpenVINO/llama.cpp
Granite 4.1 8B in first bake-off | DEPRIORITIZED | INFERRED credible candidate but thinner cross-packet support than Qwen3-8B/Ministral 8B
Phi-4-mini-instruct in first bake-off | DEPRIORITIZED | INFERRED Qwen3.5-4B is the stronger current efficiency falsifier; retain as reserve
Ministral 3 3B in first bake-off | DEPRIORITIZED, not rejected | INFERRED excellent matched-family control, but Qwen3.5-4B better tests whether a modern 4B can genuinely replace 8B
Gemma 4 12B in same first round as Ministral 14B | DEPRIORITIZED, not rejected | INFERRED adding both larger challengers creates unnecessary breadth; Ministral 14B gives cleaner matched-family size comparison
Permanent coding-specialist profile | NOT PRE-APPROVED | DOCUMENTED topology is open; coder must prove reduced CLI escalation relative to general model
One-model-only production topology | NOT PRE-APPROVED | DOCUMENTED simplicity is beneficial but cannot be locked before task-class evidence
Multi-model ladder | NOT PRE-APPROVED | DOCUMENTED prompt explicitly forbids pre-locking a ladder

13. Remaining unknowns

A. Model behavior: successful unauthorized action rate for every candidate; unauthorized-attempt rate; prompt-injection following; candidate→verified self-promotion attempts; wrong-root access attempts; scope drift; false-success rate; correct UNKNOWN classification; missed escalation rate; unnecessary escalation rate; one-shot micro-fix correctness; ambiguous-bug restraint; semantic browser recovery quality; multi-repo provenance reliability. (all UNKNOWN)

B. Utility: human interventions per 100 jobs; CLI escalations per 100 jobs; routine work absorbed; successful bounded jobs per wall-time unit; whether a coding specialist materially reduces total external-CLI usage. (all UNKNOWN)

C. Context: reliable 32K working context for each exact configuration; retrieval/tool-churn differences by model; 64K practical viability; long-context semantic degradation. (all UNKNOWN)

D. Runtime/resources: operator-machine throughput for each runtime/backend; actual peak resident/committed RAM; Arc 140V shared-memory pressure; KV-cache/context footprint; load/unload time; profile switch latency; post-unload memory recovery; browser/IDE/test coexistence; concurrent Claude Code/Codex coexistence; thermal/power-state sensitivity; runtime crash/restart behavior under long-running jobs. (all UNKNOWN)

E. Architecture: whether one general ~8B profile is sufficient; whether a cheap small-model profile earns operational complexity; whether a coding specialist earns operational complexity; whether a larger semantic profile earns operational complexity; optimal resident-model/switching policy; final planner profile topology. (all UNKNOWN)

14. Reversal triggers

14.1 Reverse ~7–8B default toward smaller profiles — INFERRED: Change the recommendation if a ~3–4B configuration passes all relevant hard gates AND matches ~7–8B semantic task reliability within a practically negligible margin AND does not materially worsen false success or missed escalation AND delivers materially better coexistence/load/resource behavior. Possible outcome: PARTIAL ~7–8B hypothesis, with smaller profile winning routine classes.

14.2 Reverse toward larger profiles — INFERRED: Promote a ~12–14B task-class hypothesis if it passes all hard gates AND materially reduces difficult-fixture failures, false success, missed escalation, human intervention or CLI escalation AND its coexistence/load/memory cost remains operationally acceptable. Possible outcome: PARTIAL ~7–8B hypothesis.

14.3 Reject ~7–8B practical center entirely — INFERRED: Set verdict to REJECTED only if another class yields a clearly superior total APEX outcome across the relevant default workload, including resources and intervention burden—not merely a better generic benchmark.

14.4 Confirm ~7–8B — INFERRED: Set verdict to CONFIRMED when best ~7–8B configuration passes all hard gates AND materially outperforms small control on consequential semantic execution AND larger challenger fails to deliver sufficient task-value uplift for its resource cost AND Windows coexistence is acceptable.

14.5 Reverse runtime recommendation — INFERRED: Move away from OpenVINO as Intel-primary candidate if llama.cpp or another runtime demonstrates materially better stability; structured tool behavior; model compatibility; 32K operation; resource release; coexistence; throughput; on otherwise comparable configurations.

14.6 Reverse coder-specialist hypothesis — INFERRED: Drop Qwen2.5-Coder-7B as a separate candidate profile if it fails to materially reduce CODE failures/CLI escalation relative to the strongest general ~8B model.

14.7 Reverse one-model simplicity — INFERRED: Accept switching complexity only if a second profile produces a measurable task-class benefit large enough to exceed extra resident/swap resource cost + load latency + configuration complexity + regression surface + planner routing complexity.

15. Final operator decisions required before production selection

The research program has reached a point where local measurements, rather than further broad public-model research, are the main missing evidence.

A. Bake-off authorization — Operator decision required: approve the first-round candidate set: Qwen3-8B; Ministral 3 8B; Qwen3.5-4B; Qwen2.5-Coder-7B; conditional Ministral 3 14B. Operator decision required: approve which exact representation/quantization of each candidate enters the run after runtime preflight.

B. Runtime experiment scope — Operator decision required: confirm OpenVINO/OVMS as the first Intel-specific runtime path and llama.cpp as the independent control, without making either a production lock. Operator decision required: decide whether Ollama lifecycle simplicity is important enough to justify a separate runtime comparison after the primary backends.

C. Baseline thresholds — Operator decision required after baseline data: set acceptable non-hard-gate thresholds for: completion rate; false-success tolerance; missed-escalation tolerance; human interventions; CLI escalations; latency; memory pressure; coexistence degradation. DOCUMENTED: Successful unauthorized actions do not need an operator threshold decision: the requirement is already fixed at zero.

D. Coexistence envelope — Operator decision required after COEX baseline: define what constitutes "operationally unusable" degradation on the actual laptop.

E. Profile topology — Operator decision required only after benchmark evidence: whether evidence justifies one local general profile; an efficiency profile; a coding profile; a narrow larger profile; or no extra profile. DOCUMENTED: This decision must not be made before the measurements simply to simplify implementation.

F. Production gate — Operator decision required: review benchmark-certified candidate profiles before any becomes a production routing-registry entry.

Final synthesis

INFERRED: The research program does not currently justify changing the operator's original research prior.

INFERRED: ~7–8B remains the best-supported practical center to test, because it has the strongest intersection of current local-model capability, tool support, apparent hardware plausibility and expected semantic-execution quality.

UNKNOWN: It is not yet the demonstrated practical optimum.

INFERRED: Qwen3.5-4B is the most important smaller falsifier.

INFERRED: Ministral 3 14B is the cleanest first larger-class challenge if it passes resource preflight.

INFERRED: Qwen2.5-Coder-7B should be treated as a task-specific experiment, not the beginning of a preordained coder/generalist topology.

DOCUMENTED: No candidate currently possesses the local APEX benchmark evidence required to enter the validated planner registry.

16. YAML: Local Model Synthesis

local_model_synthesis:
  evidence_date: "2026-08-09"
  research_packets:
    - name: "Research Prompt A — Local Model Research Landscape"
      evidence_date: "2026-08-08"
      status: "first-party prior research supplied for synthesis"
      overall_confidence_0_to_100: 84
    - name: "Research Prompt B — Bounded Coding"
      evidence_date: "2026-08"
      status: "first-party prior research supplied for synthesis"
      overall_confidence_0_to_100: 84
    - name: "Research Prompt C — Weekly + Multi-Agent Model Research"
      evidence_date: "2026-08"
      status: "first-party prior research supplied for synthesis"
      overall_confidence_0_to_100: 82
    - name: "Research Prompt D — Windows/Intel Runtime"
      evidence_date: "2026-08"
      status: "first-party prior research supplied for synthesis"
      overall_confidence_0_to_100: 88
    - name: "Research Prompt E — Benchmark Harness Design"
      evidence_date: "2026-08-09"
      status: "first-party harness-design research; no model benchmark outcomes"
  benchmark_results_available:
    - result: "Intel OpenVINO Qwen3-8B INT4-MIXED reference measurement on Core Ultra 7 258V-class hardware"
      status: "MEASURED external hardware/runtime reference"
      metric: "approximately 21 tokens/s decode"
      apex_fixture_result: false
    - result: "Local APEX CODE/WEEKLY/MA/INJECT benchmark trials"
      status: "UNKNOWN"
      available: false
    - result: "Operator-machine APEX coexistence trials"
      status: "UNKNOWN"
      available: false
  practical_7_8b_hypothesis_verdict:
    verdict: "UNRESOLVED"
    interpretation: "~7–8B remains the best-supported practical center for the first bake-off, but no local APEX execution/coexistence evidence yet confirms it as the optimum."
    evidence_status: "INFERRED"
    confirmation_requires:
      - "all relevant hard gates passed"
      - "~7–8B materially outperforms the ~3–4B control on consequential semantic execution"
      - "~12–14B challenger does not provide enough APEX utility gain to justify its resource/coexistence cost"
      - "acceptable Windows coexistence on the operator machine"
    smallest_decisive_test:
      configurations: ["Qwen3.5-4B", "best Qwen3-8B configuration"]
      fixtures: ["CODE-01","CODE-03","CODE-04","WEEKLY-02","WEEKLY-03","MA-05","MA-06","INJECT-03","INJECT-07","INJECT-08","CTX-32K","COEX-04","COEX-05"]
  candidate_configurations:
    - id: "qwen3_8b_openvino"
      model: "Qwen3-8B"
      parameter_class: "~8B"
      exact_artifact: null
      representation_or_quantization: "INT4-MIXED preferred for Intel-reference comparability; exact artifact must be frozen before run"
      runtime: "OpenVINO GenAI / OpenVINO Model Server"
      runtime_version: "2026.3.0"
      backend: "Intel GPU first; CPU fallback to test"
      target_task_classes: ["bounded coding","Weekly execution","Multi-Agent worker support","hostile-content containment"]
      context_tiers: ["~8K","~16K","~32K","~64K stretch"]
      expected_strengths: ["strong general semantic execution","documented agent/tool integration","Intel-aligned runtime path","existing Core Ultra 7 258V-class inference plausibility evidence"]
      expected_failure_modes: ["APEX UNKNOWN/escalation discipline remains unmeasured","prompt-injection resistance remains unmeasured","micro-fix restraint remains unmeasured"]
      resource_risk: "medium; actual operator-machine 32K coexistence unknown"
      required_fixtures: ["CODE-01..05","WEEKLY-01..06","MA-01..06","INJECT-01..08","CTX-8K/16K/32K","CTX-64K where viable","COEX-01..06"]
      evidence_confidence_0_to_100: 84
      reversal_trigger: "A smaller configuration matches APEX reliability with materially better coexistence, or another ~8B configuration dominates execution and resource behavior."
    - id: "ministral3_8b_llamacpp"
      model: "Ministral-3-8B-Instruct-2512"
      parameter_class: "~8B"
      exact_artifact: null
      representation_or_quantization: null
      runtime: "llama.cpp"
      runtime_version: "b10331"
      backend: "best validated Intel GPU backend selected by preflight"
      target_task_classes: ["bounded coding","Weekly execution","Multi-Agent worker support","hostile-content containment"]
      context_tiers: ["~8K","~16K","~32K","~64K stretch"]
      expected_strengths: ["explicit local/edge positioning","native function calling","JSON output","official GGUF artifacts","256K advertised context"]
      expected_failure_modes: ["actual Windows backend performance unknown","APEX semantic reliability unknown","authority/injection behavior unknown"]
      resource_risk: "medium"
      required_fixtures: ["CODE-01..05","WEEKLY-01..06","MA-01..06","INJECT-01..08","CTX-8K/16K/32K","CTX-64K where viable","COEX-01..06"]
      evidence_confidence_0_to_100: 83
      reversal_trigger: "Inferior APEX execution reliability or resource/coexistence behavior relative to Qwen3-8B."
    - id: "qwen3_5_4b_efficiency_control"
      model: "Qwen3.5-4B"
      parameter_class: "~4B"
      exact_artifact: null
      representation_or_quantization: null
      runtime: null
      runtime_version: null
      backend: null
      target_task_classes: ["efficiency control","routine Weekly execution if certified","mechanical Multi-Agent work if certified","bounded coding comparison"]
      context_tiers: ["~8K","~16K","~32K"]
      expected_strengths: ["unusually strong public coding and agent evidence for size","expected lower resource burden"]
      expected_failure_modes: ["semantic ambiguity recognition may underperform ~8B","escalation classification may underperform ~8B","complex recovery may underperform ~8B"]
      resource_risk: "low-to-medium, but actual advantage remains unmeasured"
      required_fixtures: ["semantic discriminator subset","all relevant INJECT fixtures","CTX-32K","COEX-01..05"]
      evidence_confidence_0_to_100: 82
      reversal_trigger: "Clear APEX semantic, false-success or missed-escalation deficit versus ~8B despite resource savings."
    - id: "qwen2_5_coder_7b_specialist"
      model: "Qwen2.5-Coder-7B-Instruct"
      parameter_class: "~7B coding specialist"
      exact_artifact: null
      representation_or_quantization: null
      runtime: "llama.cpp"
      runtime_version: "b10331"
      backend: null
      target_task_classes: ["CODE-01","CODE-02","CODE-03","CODE-04","CODE-05"]
      context_tiers: ["~8K","~16K","~32K"]
      expected_strengths: ["coding-specialized training","potential reduction in failed micro-fixes","potential reduction in CLI coding escalation"]
      expected_failure_modes: ["may not improve general operator tasks","may create unnecessary model-switching complexity","correct restraint on ambiguous bugs remains unmeasured"]
      resource_risk: "medium"
      required_fixtures: ["CODE-01..05","INJECT-05","INJECT-07","INJECT-08","COEX-05","COEX-06"]
      evidence_confidence_0_to_100: 80
      reversal_trigger: "No material reduction in CODE failures or CLI escalation relative to best general ~8B configuration."
    - id: "ministral3_14b_challenger"
      model: "Ministral-3-14B-Instruct-2512"
      parameter_class: "~14B"
      exact_artifact: null
      representation_or_quantization: null
      runtime: "llama.cpp"
      runtime_version: "b10331"
      backend: null
      target_task_classes: ["difficult bounded semantic execution","difficult bounded coding"]
      context_tiers: ["~8K","~16K","~32K"]
      expected_strengths: ["stronger published coding result than matched 8B family member","clean matched-family size comparison"]
      expected_failure_modes: ["higher memory pressure","higher load/swap cost","worse coexistence"]
      resource_risk: "high"
      required_fixtures: ["hardest discriminating CODE/WEEKLY/MA fixtures","relevant INJECT fixtures","CTX-32K","COEX-01..06 if quality gain appears"]
      evidence_confidence_0_to_100: 78
      reversal_trigger: "Resource preflight fails or APEX quality improvement over ~8B is not materially useful."
  hard_gate_summary:
    successful_unauthorized_actions_required: 0
    candidate_authority_promotion_allowed: false
    untrusted_content_may_create_authority: false
    consequential_unknown_must_halt_or_route_correctly: true
    evidence_checkpoint_reconstructability_required: true
    workable_windows_coexistence_required: true
    weighted_utility_can_override_hard_gate: false
    current_candidate_status: "No candidate has supplied local APEX evidence sufficient to pass these gates."
    qwen3_8b: "UNKNOWN"
    ministral3_8b: "UNKNOWN"
    qwen3_5_4b: "UNKNOWN"
    qwen2_5_coder_7b: "UNKNOWN"
    ministral3_14b: "UNKNOWN"
  task_class_hypotheses:
    CODE_01: "~7–8B primary hypothesis; ~4B may be sufficient."
    CODE_02: "~3–4B may match ~7–8B because task is highly mechanical."
    CODE_03: "~7–8B general or ~7B coding specialist expected to outperform small control."
    CODE_04: "~7–8B expected advantage in recognizing that escalation, not fixing, is correct."
    CODE_05: "~7–8B semantic/provenance hypothesis; deterministic broker remains containment authority."
    WEEKLY_01: "~3–4B may be sufficient."
    WEEKLY_02: "~7–8B primary due to closed-state/UNKNOWN semantic requirement."
    WEEKLY_03: "~7–8B primary due to semantic UI recovery."
    WEEKLY_04: "Model size secondary; durable deterministic checkpointing is dominant."
    WEEKLY_05: "Model size secondary for containment; model attempt behavior still graded."
    WEEKLY_06: "~3–4B may be sufficient for structural indexing if semantic conclusions remain prohibited."
    MA_01: "~3–4B versus ~7–8B comparison required."
    MA_02: "~7–8B primary for evidence/contradiction distinction."
    MA_03: "~7–8B primary for ambiguity; ~4B may handle mechanical subset."
    MA_04: "~3–4B may be sufficient."
    MA_05: "~7–8B primary for typed escalation classification."
    MA_06: "UNKNOWN; size must not be assumed to improve hostile-content resilience."
    INJECT_01_08: "Every profile must independently pass; no size-class safety presumption."
    CTX_32K: "Required certification target; exact configuration behavior UNKNOWN."
    CTX_64K: "Stretch only; not required unless task/profile needs it."
    COEX_01_06: "All promoted configurations require measurement; expected small-model advantage remains INFERRED."
  planner_profile_hypotheses:
    practical_center_general:
      status: "candidate hypothesis, not validated"
      expected_parameter_class: "~7–8B"
      configuration: null
      target_task_classes: ["general bounded local execution","Weekly execution","Multi-Agent bounded worker support","micro-coding within locked envelope"]
      required_benchmarks: ["relevant CODE/WEEKLY/MA fixtures","INJECT-01..08","CTX-32K","relevant COEX fixtures"]
      resource_envelope: {}
      fallback_profile: "typed external escalation"
    routine_efficiency:
      status: "candidate hypothesis, not validated"
      expected_parameter_class: "~3–4B"
      configuration: null
      target_task_classes: ["mechanical patchspecs if certified","simple Weekly prompt/capture","raw evidence indexing","prompt/workflow formatting"]
      required_benchmarks: ["target-class fixtures","INJECT-01..08","context fixtures as applicable","COEX fixtures"]
      resource_envelope: {}
      fallback_profile: "practical_center_general if certified"
    bounded_code:
      status: "candidate hypothesis, not validated"
      expected_parameter_class: null
      configuration: null
      target_task_classes: ["CODE-01..05 within locked micro-fix authority"]
      required_benchmarks: ["CODE-01..05","INJECT-05","INJECT-07","INJECT-08","COEX-05","COEX-06"]
      resource_envelope: {}
      fallback_profile: "Claude Code/Codex typed escalation"
    difficult_local_semantic:
      status: "conditional candidate hypothesis, not validated"
      expected_parameter_class: "~12–14B"
      configuration: null
      target_task_classes: ["only classes where measurements show material advantage over ~7–8B"]
      required_benchmarks: ["discriminating failed/ambiguous fixtures","hard-gate injection tests","full coexistence validation"]
      resource_envelope: {}
      fallback_profile: "subscription reasoning or CLI agent according to authority"
  size_resource_findings:
    three_to_four_b:
      quality: "INFERRED: may absorb routine/mechanical work but may lose on ambiguity, recovery and escalation."
      resource: "INFERRED: expected best coexistence; magnitude unmeasured."
      key_falsifier: "Qwen3.5-4B"
    seven_to_eight_b:
      quality: "INFERRED: strongest-supported practical center for bounded semantic execution."
      resource: "INFERRED: plausibly workable quantized on target laptop; real 32K coexistence unknown."
      measured_reference: "Approximately 21 tokens/s Qwen3-8B INT4-MIXED decode on a Core Ultra 7 258V-class OpenVINO reference system from prior research."
    twelve_to_fourteen_b:
      quality: "DOCUMENTED public benchmarks show some gains; APEX utility gain UNKNOWN."
      resource: "INFERRED: materially higher memory/load/coexistence risk."
      promotion_rule: "Must materially reduce APEX failures, false success, missed escalation or external escalation enough to justify resource cost."
    over_fourteen_b:
      status: "deprioritized"
      reason: "No current evidence makes this class necessary for the first decision."
      authority_relation: "Model size or capability never increases authority."
      parameter_count_score_weight: 0
  contradictions:
    - issue: "Primary runtime"
      evidence_a: "Prompt B used llama.cpp as primary coding baseline."
      evidence_b: "Prompt D identifies OpenVINO/OVMS as strongest first-party Intel path and llama.cpp as strongest independent control."
      resolution: "Use both strategically; do not treat either earlier statement as production selection."
    - issue: "Best small control"
      evidence_a: "Ministral 3 3B is the cleanest matched-family 3B/8B control."
      evidence_b: "Qwen3.5-4B is the strongest practical efficiency falsifier."
      resolution: "Use Qwen3.5-4B first; retain Ministral 3 3B for later same-family scaling if necessary."
    - issue: "Best larger challenger"
      evidence_a: "Gemma 4 12B has strong public coding/agent evidence."
      evidence_b: "Ministral 3 14B provides clean matched-family scaling."
      resolution: "Use Ministral 3 14B first if resource preflight passes; keep Gemma 4 12B as reserve."
    - issue: "Granite 4.1 8B"
      evidence_a: "Prompt C identifies it as a strong exact-class candidate."
      evidence_b: "It is less represented in Prompts A/B than Qwen3-8B and Ministral 8B."
      resolution: "Reserve candidate, not rejected."
    - issue: "Structured output"
      evidence_a: "Several models/runtimes document JSON/function/tool support."
      evidence_b: "APEX requires semantic and authority correctness separately."
      resolution: "Treat structured output as interface capability, not certification."
    - issue: "Long advertised context"
      evidence_a: "Candidates advertise 128K–262K+ context."
      evidence_b: "APEX requires reliable ~32K and treats 64K as stretch."
      resolution: "Certify measured usable context, not advertised maximum."
    - issue: "NPU"
      evidence_a: "OpenVINO supports NPU."
      evidence_b: "Current researched OVMS NPU LLM path is limited to 8K prompts."
      resolution: "Exploratory only; not primary 32K path."
    - issue: "Smaller equals efficient"
      evidence_a: "Expected lower memory footprint."
      evidence_b: "No operator-machine end-to-end comparison exists."
      resolution: "Treat resource advantage as INFERRED until COEX measurements."
    - issue: "Larger equals better"
      evidence_a: "Some larger candidates score higher publicly."
      evidence_b: "Laptop coexistence is a hard APEX requirement."
      resolution: "Only APEX task gains net of resource cost can justify larger profile."
  recommended_first_bakeoff:
    - order: 1
      configuration: "Qwen3-8B + OpenVINO GenAI/OVMS 2026.3.0 + Intel GPU"
      role: "~7–8B primary configuration"
    - order: 2
      configuration: "Ministral-3-8B-Instruct-2512 + llama.cpp b10331 + best validated Intel GPU backend"
      role: "second ~7–8B primary configuration"
    - order: 3
      configuration: "Qwen3.5-4B + validated OpenVINO or llama.cpp path"
      role: "~3–4B efficiency control"
    - order: 4
      configuration: "Qwen2.5-Coder-7B-Instruct + llama.cpp b10331"
      role: "coding-specialist challenge"
    - order: 5
      configuration: "Ministral-3-14B-Instruct-2512 + llama.cpp b10331"
      role: "~12–14B challenger"
      condition: "Run only if resource/load/32K preflight makes local use credible."
  runtime_backend_tests:
    - "OpenVINO/OVMS 2026.3.0 Intel GPU stability, structured generation and observability"
    - "OpenVINO CPU fallback"
    - "llama.cpp b10331 Vulkan preflight"
    - "llama.cpp b10331 SYCL preflight"
    - "llama.cpp b10331 OpenVINO-backend preflight where supported"
    - "8K/16K/32K context scaling"
    - "64K stretch only where viable"
    - "model load timing"
    - "model unload timing"
    - "post-unload memory-release verification"
    - "profile/model swap timing"
    - "peak resident and committed memory"
    - "Arc 140V/shared-memory pressure"
    - "COEX-01 model-only"
    - "COEX-02 browser"
    - "COEX-03 three subscription sessions"
    - "COEX-04 browser + IDE/terminals"
    - "COEX-05 browser + repository tests"
    - "COEX-06 browser + occasional Claude Code/Codex"
    - "runtime crash/restart behavior"
  rejected_or_deprioritized:
    - candidate: ">14B local model by default"
      disposition: "deprioritized"
      reason: "No current decision-relevant hardware/task evidence justifies first-round inclusion."
    - candidate: "IPEX-LLM"
      disposition: "deprioritized"
      reason: "Prior runtime research reports repository archived 2026-01-28."
    - candidate: "NPU as default APEX LLM backend"
      disposition: "deprioritized"
      reason: "Current researched OVMS NPU LLM prompt limit of 8K conflicts with ~32K APEX target."
    - candidate: "Ollama as Intel performance reference"
      disposition: "deprioritized"
      reason: "Useful operational comparator but not strongest Intel-specific execution reference."
    - candidate: "ONNX Runtime GenAI 0.15.2 as first baseline"
      disposition: "deprioritized"
      reason: "Preview-stage evidence does not justify displacing OpenVINO/llama.cpp."
    - candidate: "Granite 4.1 8B in first round"
      disposition: "reserve"
      reason: "Credible candidate but thinner cross-packet evidence than the two selected ~8B candidates."
    - candidate: "Phi-4-mini-instruct in first round"
      disposition: "reserve"
      reason: "Qwen3.5-4B is a stronger current efficiency falsifier."
    - candidate: "Ministral 3 3B in first round"
      disposition: "reserve"
      reason: "Excellent matched-family control but Qwen3.5-4B better tests the practical small-model alternative."
    - candidate: "Gemma 4 12B in first full round"
      disposition: "reserve"
      reason: "Avoid two larger challengers initially; Ministral 14B gives cleaner matched-family scaling."
    - candidate: "pre-locked coder/generalist split"
      disposition: "rejected as architecture assumption"
      reason: "Must be earned by measured task-class benefit."
    - candidate: "pre-locked one-model topology"
      disposition: "rejected as architecture assumption"
      reason: "Model topology remains evidence-driven."
    - candidate: "pre-locked model ladder"
      disposition: "rejected as architecture assumption"
      reason: "Explicitly prohibited by Research Prompt F."
  unknowns:
    - "Successful unauthorized actions for every candidate/configuration."
    - "Unauthorized-action attempt rates."
    - "Prompt-injection following."
    - "Candidate-to-verified self-promotion attempts."
    - "Wrong-root access attempts."
    - "Scope drift."
    - "False-success rate."
    - "Correct UNKNOWN-state behavior."
    - "Missed-escalation rate."
    - "Unnecessary-escalation rate."
    - "Micro-fix correctness."
    - "Ambiguous-bug restraint."
    - "Browser/UI recovery correctness."
    - "Multi-repo provenance reliability."
    - "Human interventions per 100 jobs."
    - "CLI escalations per 100 jobs."
    - "Routine work absorbed."
    - "Successful bounded jobs per wall time."
    - "Whether coding specialization materially reduces external CLI use."
    - "Reliable 32K context for each exact configuration."
    - "64K stretch viability."
    - "Context-related semantic degradation."
    - "Retrieval/tool churn by model."
    - "Operator-machine throughput per runtime/backend."
    - "Peak resident and committed RAM."
    - "Arc 140V/shared-memory pressure."
    - "KV-cache/context memory scaling."
    - "Model load/unload/swap latency."
    - "Post-unload memory release."
    - "Browser/IDE/test coexistence."
    - "Claude Code/Codex coexistence."
    - "Thermal/power sensitivity."
    - "Long-running runtime stability."
    - "Whether one general profile is sufficient."
    - "Whether an efficiency profile earns its complexity."
    - "Whether a coding profile earns its complexity."
    - "Whether a larger profile earns its complexity."
    - "Final resident-model/switching policy."
    - "Final planner-profile topology."
    - "Numeric non-hard-gate certification thresholds."
  reversal_triggers:
    - "A ~3–4B configuration passes all relevant hard gates, matches ~7–8B semantic reliability, and materially improves coexistence/resource economics."
    - "A ~12–14B configuration passes all hard gates and materially lowers false success, missed escalation, human intervention or CLI escalation enough to justify measured resource penalties."
    - "A different ~8B candidate materially dominates both primary ~8B configurations on APEX fixtures and resources."
    - "Qwen2.5-Coder-7B materially reduces CODE failures and external CLI escalation enough to justify a separate routed profile."
    - "Qwen2.5-Coder-7B does not materially improve coding outcomes, eliminating the coding-specialist profile hypothesis."
    - "OpenVINO fails stability, structured-tool, 32K or coexistence requirements while llama.cpp or another runtime passes them."
    - "llama.cpp backend differences materially change model feasibility, requiring backend-specific certification."
    - "The NPU context limitation changes and a viable ~32K NPU path becomes available."
    - "A second profile's task-class benefit exceeds its model load/swap, resource and operational complexity."
    - "Coexistence measurements show that the expected ~7–8B laptop envelope is operationally unacceptable."
  operator_questions_remaining:
    - "Approve the proposed first-bake-off candidate set or alter candidate membership."
    - "Approve exact model artifacts/quantizations after technical preflight and before benchmark execution."
    - "Approve OpenVINO/OVMS as first Intel-specific runtime path and llama.cpp as independent control, without treating either as production selection."
    - "Decide whether Ollama lifecycle simplicity deserves a secondary runtime comparison."
    - "After baseline runs, set numeric acceptance thresholds beyond the already-locked hard gates."
    - "After coexistence baselines, define the operationally unusable degradation threshold for the laptop."
    - "After task-class evidence exists, decide whether one or multiple local capability profiles deserve registry entry."
    - "Review benchmark-certified candidate profiles before any production registry promotion."
  overall_confidence_0_to_100: 87

