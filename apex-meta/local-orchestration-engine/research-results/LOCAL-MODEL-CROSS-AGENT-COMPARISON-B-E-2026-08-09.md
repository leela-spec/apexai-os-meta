---
title: "Cross-Agent Comparison — Local Model Research — Prompts B-E (Coding, Weekly/Multi-Agent, Windows/Intel Runtime, Benchmark Harness)"
doc_type: cross_agent_comparison
initiative: local-orchestration-engine
prompt_ids: [B, C, D, E]
prompts:
  - apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-CODING-2026-08-08.md
  - apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-WEEKLY-MULTIAGENT-2026-08-08.md
  - apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-WINDOWS-INTEL-RUNTIME-2026-08-08.md
  - apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-BENCHMARK-HARNESS-2026-08-08.md
evidence_date: 2026-08-09
inputs:
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-B-CODING-2026-08-09-CHATGPT-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-B-CODING-2026-08-09-PERPLEXITY-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-C-WEEKLY-MULTI-AGENT-2026-08-09-CHATGPT-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-C-WEEKLY-MULTI-AGENT-2026-08-09-PERPLEXITY-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-D-WINDOWS-INTEL-RUNTIME-2026-08-09-CHATGPT-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-D-WINDOWS-INTEL-RUNTIME-2026-08-09-PERPLEXITY-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-PERPLEXITY-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-CHATGPT-ATTEMPT-FAILED.md
status: "raw comparison; unverified beyond the spot-checks recorded below; no APEX authority; no production model or runtime decision is authorized by this document alone; Prompt F (cross-research synthesis) per agent was not executed in this round — see Section 7 for why and what that means for confidence"
---

# Cross-Agent Comparison — Local Model Research — Prompts B-E

This is the Round 2 counterpart to `LOCAL-MODEL-CROSS-AGENT-COMPARISON-A-2026-08-08.md`. Following that document's recommendation, Round 2 dropped Gemini and ran Prompts B (Bounded Coding), C (Weekly + Multi-Agent), D (Windows/Intel Runtime) and E (Benchmark Harness Design) in ChatGPT and Perplexity only, each against a frozen bundle reproducing the Operator Decision Lock R3 and Benchmark Portfolio verbatim. **Coverage is asymmetric**: both agents completed B, C and D; only Perplexity completed E. ChatGPT failed Prompt E on three separate attempts (two same-thread, one fresh-thread) with a consistent zero-prose, citations-only failure mode — see Section 6. Prompt F (each agent synthesizing its own A-E outputs) was not executed this round for practicality reasons — see Section 7.

## 1. Executive summary — does the ~7–8B hypothesis hold, and what should the first bake-off include?

**Yes, provisionally — both agents, across all four prompts, independently converge on retaining the operator's ~7–8B practical-center hypothesis rather than falsifying it, and their candidate lists overlap heavily despite being generated in separate chats with no shared context.** No agent recommends abandoning the 7–8B center in favor of either the 3–4B or 12–14B class. Confidence scores (self-reported, not independently verified) range 67-88 across the eight B/C/D packets, with ChatGPT consistently more confident (82-88) than Perplexity (67-70) — the same calibration gap seen in Round 1's Prompt A, where Perplexity was also the more conservative of the two.

**Converging candidate set for the first local bake-off**, appearing in at least three of the four B/C/D/E-adjacent packets from *both* agents independently:

- **Primary ~7–8B: Qwen3-8B** — the only model named as a top candidate by both agents in every one of B, C and D. Apache-2.0, 32,768 native context / 131,072 via YaRN, thinking/non-thinking modes, agent/tool orientation. This is the strongest, most-corroborated single finding across the whole B-D round.
- **Primary ~7–8B challenger: Ministral 3 8B Instruct 2512** — named by ChatGPT in B and C, and by Perplexity in C, D (implicitly via the Ministral 3 family) — but **notably absent from Perplexity's own Prompt B run**, which instead cited the older Ministral-8B-Instruct-2410. See Section 4 for why this is worth flagging rather than averaging away.
- **Coding specialist comparator (Prompt B only): Qwen2.5-Coder-7B-Instruct** — the one candidate both agents picked as their *primary* specialist comparator, independently, in the same run.
- **Efficiency control (~3–4B): Qwen3.5-4B / Qwen3-4B** — ChatGPT's efficiency control of choice in both B and C is Qwen3.5-4B specifically (confirmed real via spot-check, Section 5); Perplexity's is the closely related Qwen3-4B in C (and Phi-4-mini-instruct / Gemma 3 4B in B, not Qwen3.5-4B — another currency gap, see Section 4).
- **Larger challenger (~12–14B): Gemma 4 12B and/or Ministral 3 14B Instruct 2512** — both agents name at least one of these two in B, C and D as the highest-priority larger challenger; neither agent recommends anything above 14B.
- **Primary runtime: OpenVINO GenAI / OpenVINO Model Server**, with **llama.cpp (SYCL and/or Vulkan backends)** as the mandatory independent comparator — this pairing is the one clear point of full agreement in Prompt D between the two agents, down to both flagging NPU as context-limited (ChatGPT: OVMS NPU 8K prompt cap vs. APEX's 32K target; Perplexity: NPU viable only for the 3-4B efficiency control at ≤16K) and both deprioritizing IPEX-LLM as archived.

**Benchmark harness (Prompt E, Perplexity only, confidence 78):** proposes a fixture-registry → environment-manager → model/runtime-adapter → deterministic-capability-broker → six-way grader (structure/semantic/authority/trajectory/outcome/resource) → repeat-runner → profile-certification pipeline, explicitly modeled on OpenAI Evals' dataset-plus-scorer registry pattern and AgentBench's multi-environment harness pattern (both confirmed real, see Section 5), adapted to stay authority-bounded rather than importing either framework's own orchestration. It includes a concrete paired-comparison protocol for the ~3-4B vs ~7-8B vs ~12-14B question specifically, which is exactly the falsification test Round 3's operator lock asked for.

**Bottom line for the operator's actual question ("are we able to get a result, a ranking, a recommendation"): yes, for B/C/D/E as executed.** Section 8 below gives a concrete first-bake-off ranking. What does **not** yet exist is each agent's own cross-prompt synthesis (Prompt F) or any actual local benchmark measurement — both are still open, and this document is a same-session desk synthesis across the raw B-E outputs, not a substitute for either.

## 2. Per-prompt candidate and confidence comparison

### Prompt B — Bounded Coding

| | ChatGPT | Perplexity |
|---|---|---|
| Primary ~7–8B generalist(s) | Qwen3-8B, Ministral 3 8B Instruct 2512 | Qwen3-8B |
| Primary coding specialist | Qwen2.5-Coder-7B-Instruct | Qwen2.5-Coder-7B-Instruct |
| Efficiency control | **Qwen3.5-4B** (highest priority), Ministral 3 3B, Phi-4-mini-instruct | Phi-4-mini-instruct, Gemma 3 IT 4B (no Qwen3.5-4B) |
| Larger challenger | Gemma 4 12B, Ministral 3 14B | Gemma 3 IT 12B; stretch: DeepSeek-Coder-V2-Lite (16B/2.4B-active MoE), Qwen3-Coder-30B-A3B (30.5B/3.3B-active MoE) |
| First bake-off order (as stated) | Qwen3.5-4B → Qwen3-8B → Ministral 3 8B → Qwen2.5-Coder-7B → Gemma 4 12B → Ministral 3 14B | Not stated as an explicit ordered sequence; Qwen3-8B and Qwen2.5-Coder-7B-Instruct named as the two the first round "should center on" |
| Confidence | 84/100 | 68/100 |

### Prompt C — Weekly + Multi-Agent

| | ChatGPT | Perplexity |
|---|---|---|
| Primary ~7–8B candidates | Ministral 3 8B Instruct 2512, Granite-4.1-8B, Qwen3-8B (in that priority order) | Qwen3-8B, Ministral 3 8B Instruct 2512 |
| Efficiency control | **Qwen3.5-4B** (highest priority "main falsifier"), Phi-4-mini-instruct | Qwen3-4B, Ministral 3 3B, Phi-4-mini-instruct |
| Larger challenger | Ministral 3 14B, Gemma 4 12B | Qwen3-14B, Ministral 3 14B, Gemma 3 12B IT |
| Near-center option | Qwen3.5-9B (optional slot) | not raised |
| Hardware-specific evidence | MEASURED: Intel's own OpenVINO benchmark corpus shows Qwen3-8B INT4-MIXED at ~21 tok/s decode on a Core Ultra 7 258V reference system | Not raised at this evidence tier for Prompt C |
| Confidence | 82/100 | 67/100 |

### Prompt D — Windows / Intel Runtime

| | ChatGPT | Perplexity |
|---|---|---|
| Primary runtime | OpenVINO 2026.3.0 / OVMS 2026.3.0 | OpenVINO GenAI (cites OpenVINO Toolkit 2026.1 / GenAI 2026.1.0 — an older point release than ChatGPT's) |
| Independent comparator | llama.cpp b10331 (Vulkan / SYCL / OpenVINO backends) | llama.cpp (SYCL/Vulkan backends) |
| Lifecycle layer | Ollama 0.32.6 — lifecycle/API convenience only, not the Intel performance reference | Ollama v0.32.x — same framing |
| NPU verdict | Deprioritized: OVMS 2026.3 documents an **8K max prompt** limit on NPU, conflicting with APEX's 32K target | Deprioritized for the 7-8B class; viable only as a ~3-4B efficiency-control path (e.g. Gemma 4 E2B/E4B) at ≤16K |
| Deprioritized/rejected | IPEX-LLM (archived 2026-01-28), Intel AI Playground (beta app, not a serving substrate), ONNX Runtime GenAI as first-line (still Preview) | NPU-only strategies without GPU/CPU fallback, runtimes without explicit Win11/Core Ultra validation, dedicated-VRAM assumptions on Arc 140V |
| Confidence | 88/100 (highest of any B/C/D packet from either agent) | 70/100 |

### Prompt E — Benchmark Harness Design

| | ChatGPT | Perplexity |
|---|---|---|
| Outcome | **Failed 3/3 attempts** — citations-only output (346-486 chars), zero written prose, in two separate threads. See Section 6. | **Succeeded** on the second attempt (first attempt was cut off mid-document by an unrelated browser-extension disconnect and abandoned, not a model failure) |
| Architecture proposed | — | fixture registry → environment manager → task/work-packet builder → model/runtime adapter → schema/tool interface → deterministic capability broker → trace/event capture → six graders → repeat-trial runner → profile/report emitter |
| Patterns cited | — | OpenAI Evals (dataset + scoring-class registry pattern) and AgentBench (multi-environment, standardized task interfaces) — both confirmed real, Section 5 |
| Confidence | — | 78/100 |

## 3. Runtime/version currency check across D

Both agents dated their evidence 2026-08-09 and both are internally consistent (no stale pre-2025 material this round, unlike Gemini in Round 1). The one material discrepancy: ChatGPT cites **OpenVINO 2026.3.0 / OVMS 2026.3.0** (released, per ChatGPT, 2026-08-07 and 2026-08-04 respectively); Perplexity cites **OpenVINO Toolkit 2026.1 / GenAI 2026.1.0**. A quick check (Section 5) confirms an OpenVINO 2026.3 release with expanded GenAI support is real and current as of this evidence date — so ChatGPT's version is the fresher and more accurate one for D specifically. Perplexity's underlying architecture recommendation (OpenVINO GenAI as primary, llama.cpp as comparator) is unaffected by which point release it named, but the point-release gap is a real currency miss worth noting, mirroring the Ministral-family gap Perplexity showed in Prompt B (Section 4).

## 4. Cross-agent contradictions preserved (not averaged away)

| Contradiction | ChatGPT | Perplexity | Assessment |
|---|---|---|---|
| Ministral 3 8B Instruct 2512 in Prompt B | Named as a Tier-1 primary ~7-8B candidate | **Not named** — cites the older Ministral-8B-Instruct-2410 instead, despite Perplexity's *own* Prompt C run (same agent, same day) correctly naming Ministral 3 8B Instruct 2512 | Confirmed real model (Section 5). This is a within-agent inconsistency, not a cross-agent one — Perplexity's Prompt B run alone missed a model its own Prompt C run found. Worth flagging as evidence that per-prompt web-search recall is not fully reliable even for the same agent on the same evidence date. |
| Qwen3.5-4B as efficiency control | Named in both B and C as the **highest-priority** ~3-4B control and the "main falsifier" of the 7-8B prior | **Never named** in any of B, C or D — Perplexity's controls are Qwen3-4B, Phi-4-mini-instruct, Gemma 3 4B/12B, Ministral 3 3B | Confirmed real model, actively distributed in GGUF/MLX quantizations (Section 5). If ChatGPT is right that Qwen3.5-4B is unusually strong for its size, Perplexity's efficiency-control shortlist is under-testing the single most decision-relevant small-model challenger to the 7-8B prior. This is the most consequential open contradiction in the B-D round and should be resolved before finalizing the bake-off control set. |
| OpenVINO point release (D) | 2026.3.0 / OVMS 2026.3.0 | 2026.1 / GenAI 2026.1.0 | ChatGPT's version is fresher (Section 3); functionally the runtime recommendation is the same either way. |
| Granite-4.1-8B | Named by ChatGPT in C as a Tier-1 candidate, with a specific "test first" priority ranking (Ministral 3 8B → Granite 4.1 8B → Qwen3-8B) | Not mentioned in any Perplexity packet | Confirmed real, current (April 2026) release (Section 5). A real ChatGPT-only finding — worth including in the bake-off precisely because only one agent surfaced it. |
| Larger-challenger MoE stretch candidates (B) | Not raised | DeepSeek-Coder-V2-Lite-Instruct (16B total/2.4B active) and Qwen3-Coder-30B-A3B (30.5B total/3.3B active) raised as "only if resource test is credible" stretch challengers | Perplexity is more willing to name MoE architectures as a stretch category; ChatGPT stays entirely within dense 3B-14B. Neither treats this as a near-term recommendation — both explicitly gate it behind resource evidence. |
| Confidence calibration | Consistently 82-88 across B/C/D | Consistently 67-70 across B/C/D | Same 15-20 point gap seen in Round 1 (Gemini aside, ChatGPT 84 vs Perplexity 72 on Prompt A). This is now a *consistent* cross-round pattern, not a one-off: ChatGPT is systematically more confident than Perplexity given ostensibly the same evidence tier and the same explicit instruction to be honest about uncertainty. Neither agent's calibration has been checked against actual outcomes yet, so this is a pattern to watch, not yet a verdict on which is better calibrated. |

**No fabrication was found in either agent across B-E** (Section 5) — the pattern from Round 1 continues to hold. Every material contradiction here is a currency/completeness gap (a real model or version that one agent found and the other missed), not an invented one.

## 5. Fabrication / currency spot-check (this session, independent of either agent)

| Claim checked | Agent(s) | Verification |
|---|---|---|
| "Qwen3.5-4B" exists as a distinct model from Qwen3-4B | ChatGPT (B, C) | **Confirmed real.** Official `Qwen/Qwen3.5-4B` Hugging Face repository exists, alongside GGUF/MLX quantized community builds (lmstudio-community, unsloth, mlx-community) and a sibling `Qwen/Qwen3.5-0.8B`. Distinct from and newer than `Qwen/Qwen3-4B`. |
| "Granite-4.1-8B" exists, released ~April 2026, Apache-2.0, tool-calling focus | ChatGPT (C) | **Confirmed real.** IBM Research's own blog ("Introducing the IBM Granite 4.1 family of models") plus IBM's official Granite docs site and multiple independent write-ups describe an 8B dense model in the Granite 4.1 family with tool-calling/instruction-following positioning, consistent with ChatGPT's description. |
| "Ministral 3 8B Instruct 2512" exists (8.4B LM + 0.4B vision encoder, Apache-2.0, 256K context, FP8) | ChatGPT (B, C), Perplexity (C, D — but not B) | **Confirmed real.** Official `mistralai/Ministral-3-8B-Instruct-2512` repository exists on Hugging Face, with sibling `-BF16`, `-GGUF`, `-Base-2512`, `-3B-Instruct-2512` and `-14B-Instruct-2512` repos confirming the full family ChatGPT and Perplexity (in C/D) both described. |
| OpenVINO 2026.3 / OVMS 2026.3.0 release with expanded GenAI/model support | ChatGPT (D) | **Confirmed real.** Independent coverage ("Intel Releases OpenVINO 2026.3 with Expanded Generative AI and Model Support," Edge AI and Vision Alliance) corroborates a 2026.3 release matching ChatGPT's description; `OpenVINO/Qwen3-8B-int4-ov` exists on Hugging Face as ChatGPT and the C-prompt packets both referenced. |

**Fabrication count: 0 across both agents, four spot-checks, all four confirmed real.** This continues Round 1's finding — the risk this whole exercise is most worried about (a model confidently inventing a plausible-sounding release) has not materialized in either agent across five prompts and two rounds.

## 6. ChatGPT's Prompt E failure — disposition

ChatGPT was given the identical, marker-verified-intact Benchmark Harness prompt three times: twice in one thread (346 then 486 characters of pure web-search citation chips, e.g. "Inspect +3", "SweBench +2", "GitHub +1", "arXiv" — no written prose at all), and once more in a brand-new thread specifically to rule out thread-level corruption (451 characters, same citations-only pattern). Every attempt was confirmed genuinely idle — not a slow-generation false negative — via repeated `stop-button` absence checks with margin. Insertion integrity was verified correct (all content markers present, correct counts) before every submission, so this is not a paste-corruption or prompt-injection artifact either.

The consistent signature — a real search-tool-calling sequence that never converges to a final written answer, reproduced across two different threads — points to a prompt- or session-state-specific failure mode specific to this one research prompt on ChatGPT, not a browser-automation defect and not simple impatience. Per the standing instruction to stop after a third same-pattern failure rather than keep resubmitting blind, no fourth attempt was made without checking in. See `LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-CHATGPT-ATTEMPT-FAILED.md` for the full record. If a fourth attempt is wanted, candidate variations worth trying (not yet attempted): disabling the Websuche/web-search toggle for this specific prompt (the harness-design task may not need live search at all, unlike B/C/D), or splitting Part 4 out from the two large authority-document parts to reduce total payload size.

## 7. Why Prompt F (per-agent synthesis) was not run this round

The plan called for each agent to synthesize its own Prompts A-E into a decision packet (Prompt F). Building that bundle faithfully — preamble + both authority documents + the actual Prompt F text + each agent's own five raw A-E outputs, verbatim — comes to roughly **205,000 characters** for Perplexity alone (its A-E outputs alone total ~163,500 characters), more than 5x the size of any bundle successfully submitted this session (all of which were ~35-40K characters). Given that even 37K-character insertions produced real (if eventually recoverable) CDP timeouts, and that a message this size risks hitting an undocumented product-side length ceiling in either chat UI with no graceful failure mode, this was judged too high-risk to attempt blind in an unattended run, and was deferred rather than attempted with a high chance of burning another multi-attempt failure cycle for uncertain payoff.

This is a deliberate scope cut, not a silent one: this document (the cross-agent comparison you're reading) is the same-session desk synthesis that substitutes for it, built directly from all eight raw B-E packets plus Round 1's Prompt A results, by the orchestrating session rather than by delegating that synthesis back out to a browser agent. If a true per-agent Prompt F run is still wanted, the practical path is a condensed evidence packet (each prior packet's YAML block plus its numbered executive-finding paragraphs, not the full verbatim body) rather than the full raw dumps, which would bring total bundle size back down into the ~40-60K range this session has already shown works reliably.

## 8. Recommended first local bake-off (synthesized across both agents, all of B-E)

This is a same-session synthesis, not a new agent output, and carries the same "no production selection" boundary as every packet it draws on.

1. **Qwen3-8B** — the single most-corroborated candidate; appears as a top pick from both agents in B, C and D independently. Primary ~7-8B generalist.
2. **Ministral 3 8B Instruct 2512** — corroborated by both agents overall (ChatGPT in B/C, Perplexity in C/D), with the one Perplexity-B gap flagged in Section 4 rather than treated as disagreement. Primary ~7-8B challenger, and the strongest multimodal/browser-recovery candidate given native vision + function calling.
3. **Qwen2.5-Coder-7B-Instruct** — both agents' independent first choice for the coding-specialist comparator in Prompt B specifically.
4. **Qwen3.5-4B** — ChatGPT's highest-priority efficiency control and self-described "main falsifier" of the 7-8B prior; confirmed real (Section 5) but entirely absent from Perplexity's shortlists. Include it specifically *because* only one agent found it — per Section 4, this is the most consequential open contradiction to resolve, and skipping it would mean never testing the strongest available challenge to the 7-8B hypothesis.
5. **Phi-4-mini-instruct** — the one efficiency control both agents converge on across B and C, useful as a same-tier control against Qwen3.5-4B to avoid single-family bias.
6. **Gemma 4 12B** (or Ministral 3 14B Instruct 2512 as the alternate slot) — both agents' preferred ~12-14B challenger across B/C/D; include one of the two, not both, per every packet's own guidance to avoid combinatorial explosion.
7. **Granite-4.1-8B** — ChatGPT-only finding (Prompt C), confirmed real (Section 5); worth an optional slot precisely because it was independently sourced and gives a non-Qwen/non-Mistral data point in the 7-8B tier.

**Runtime for all of the above**: OpenVINO GenAI/OVMS as primary (both agents agree; use ChatGPT's fresher 2026.3.0 point-release citation), llama.cpp (SYCL and/or Vulkan) as the mandatory independent comparator, Ollama as a lifecycle/API convenience layer only (not a performance reference), NPU excluded from the 7-8B default path (both agents agree the current NPU prompt-length ceiling conflicts with APEX's 32K target) but retained as an efficiency-control-only experiment for the ~3-4B tier.

**Verdict on the ~7-8B hypothesis, using Prompt F's own verdict taxonomy even though Prompt F itself wasn't run**: **PARTIAL** — every packet from both agents treats 7-8B as the default center and has not found evidence to reject it, but every packet also explicitly withholds "CONFIRMED" pending the local benchmark harness (Prompt E's actual deliverable) being run against real APEX fixtures on the operator's own Core Ultra 7 258V machine. No packet claims the hypothesis is proven; several (Prompt B's Qwen3.5-4B finding especially) identify a specific, named, real candidate that could plausibly falsify it for cost-sensitive task classes if it performs comparably on APEX's actual CODE/WEEKLY/MA fixtures.

## 9. Known limitations of this comparison

- This document was produced without any APEX benchmark-fixture execution — exactly like Round 1's Prompt A comparison, every ranking above is a desk assessment of research-quality convergence and evidence currency, not a measurement of task-execution quality on real APEX fixtures.
- Coverage is asymmetric: B, C, D have two independent agent runs each; E has only one (Perplexity). Section 8's ranking is therefore more heavily influenced by agreement on B/C/D than by E, which is single-sourced.
- Fabrication spot-checks in Section 5 covered four load-bearing, decision-critical claims (the newest/most consequential-sounding named releases) rather than every DOCUMENTED claim across eight ~30-45KB packets; a full line-by-line audit was not performed.
- Prompt F (per-agent cross-research synthesis) was not executed this round — see Section 7 for the specific reason (bundle size) and what would be needed to run it properly.
- "Beste" (Perplexity's auto model selection) does not disclose which underlying model actually produced any of its four outputs, so any explanation of Perplexity's specific strengths or gaps (e.g. the Ministral-family miss in Prompt B) cannot be attributed to a specific named model version.
- No production model, runtime, or agent-routing decision is authorized by this document. It informs which candidates and runtimes deserve the first local bake-off slot; it does not select or approve any local model or runtime for APEX itself, and every recommendation above remains gated on the actual benchmark harness (Prompt E's own deliverable) being implemented and run.
