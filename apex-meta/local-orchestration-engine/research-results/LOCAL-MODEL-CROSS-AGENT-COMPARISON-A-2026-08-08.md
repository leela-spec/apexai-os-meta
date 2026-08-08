---
title: "Cross-Agent Comparison — Local Model Research — Prompt A (Landscape)"
doc_type: cross_agent_comparison
initiative: local-orchestration-engine
prompt_id: A
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08.md
evidence_date: 2026-08-08
inputs:
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-CHATGPT-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-GEMINI-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-PERPLEXITY-RESULT.md
bundle_sha256: "638c150c3503cf9ee2e802a1870db18c088b268fc4efb1712b770e62a3da7d10"
status: "raw comparison; unverified beyond the spot-checks recorded below; no APEX authority; no production model or agent-routing decision is authorized by this document alone"
---

# Cross-Agent Comparison — Local Model Research — Prompt A (Landscape)

Calibration round. Prompt A (Local Model Landscape) was executed identically — same frozen bundle, same `bundle_sha256` — in ChatGPT, Gemini, and Perplexity, each in a fresh chat outside any project/Gem/Space, with English output enforced and standard chat + web search intended (not Deep Research). This document scores the three outputs against the rubric defined in Section 8 of the execution plan and produces a routing recommendation for the remaining prompts (B–F).

## 1. Executive summary

ChatGPT and Perplexity both produced current, well-sourced, boundary-compliant research grounded in real 2025–2026 model releases (verified below). Gemini produced a boundary-compliant *structure* but built it on a stale, pre-2025 model set because its own runtime disclosed that live web search was unavailable for the session — a fact it stated plainly at the top of its answer, then somewhat undermined by still stamping the output `evidence_date: 2026-08-08` and a 85/100 confidence score. That internal inconsistency, not fabrication, is Gemini's defining flaw in this run.

No fabrication was found in any of the three outputs during spot-checking (Section 4). All three models existed as named, with materially correct parameter counts and context lengths, for both the current-generation candidates (ChatGPT, Perplexity) and the stale-generation candidates (Gemini) it cited.

Recommendation: promote ChatGPT and Perplexity as the primary research agents for the remaining prompts; use Gemini only after forcing genuinely live search (e.g., explicit grounding/search-tool invocation rather than relying on default chat behavior), and treat any Gemini output that does not explicitly confirm live search was used as suspect by default. See Section 6.

## 2. Boundary compliance matrix

Per the plan's seven explicit boundaries for Prompt A. Pass / Fail / Partial.

| Boundary | ChatGPT | Gemini | Perplexity |
|---|---|---|---|
| Did not select a production model | Pass — explicitly frames every candidate as a benchmark-priority hypothesis, never a selection | Pass — same framing used | Pass — explicit "not a production selection" language for Qwen3-8B |
| Treated 7–8B as hypothesis, not proven | Pass — "supports the operator's research design rather than falsifying it," explicitly not proven | Pass — "highly credible," but still labeled INFERRED/hypothesis throughout | Pass — "should be the first execution candidate, not a production selection" |
| Did not silently substitute a largest-model or maximum-reasoning objective | Pass — 12–14B and >14B candidates are explicitly gated behind demonstrated APEX failure-reduction, not treated as default upgrades | Pass — 12–14B explicitly framed as "marginal... likely not worth the latency/RAM cost" | Pass — same gating language ("must justify resource and coexistence cost") |
| Did not equate public benchmark strength with APEX execution reliability | Pass — repeatedly states vendor benchmarks are "prioritization evidence, never APEX certification" | Partial — matrix ratings (H/M/L) are presented with less explicit disclaiming of vendor-benchmark reliance, though still labeled INFERRED | Pass — explicit "Public coding benchmark results do not establish performance on APEX's micro-fix envelope" |
| Did not infer dedicated VRAM from integrated-GPU reporting | Pass — explicitly discusses KV cache/shared-memory contention rather than treating "VRAM" as a fixed budget | Fail — treats memory purely as flat GB estimates (e.g. "~6.5 GB", "~10.0 GB") without addressing Intel unified-memory/shared-reporting nuance | Pass — has a dedicated section stating "Intel integrated graphics uses system memory... dedicated VRAM must not be inferred from Windows reporting," citing Intel directly |
| Separated measured / documented / inferred / unknown | Pass — rigorous and consistent throughout, including an explicit statement that MEASURED does not apply anywhere in this run | Pass — labels are present and mostly correctly applied, though less rigorously between DOCUMENTED and INFERRED in a few places (e.g., speed/RAM figures marked INFERRED but stated with unwarranted precision) | Pass — rigorous, plus an added DEPRIORITIZED label not in the other two, used consistently |
| Preferred current primary sources | Pass — Dec 2025/2026 releases (Ministral 3, Gemma 4) sourced to official model cards/release announcements | **Fail** — sources are exclusively 2024-era (Llama 3.1 July 2024, Phi-3 April 2024, Mistral Nemo July 2024, Qwen2 June 2024); no current-generation model appears anywhere in the output | Pass — 2025–2026 Qwen3/Gemma 3/Devstral materials, explicitly dated where possible |

**Result: ChatGPT 7/7 pass. Perplexity 7/7 pass. Gemini 5/7 pass, 1 partial, 1 fail** — the VRAM-inference boundary and, most importantly, the current-primary-sources boundary. The sources failure is largely explained (not excused) by Gemini's disclosed inability to search live this session; see Section 5.

## 3. Deliverable completeness

Prompt A requires 16 numbered deliverables plus an 18-key YAML block.

| Agent | Deliverables present (of 16) | YAML keys present (of 18) | Notes |
|---|---|---|---|
| ChatGPT | 16/16, all substantive | 18/18, several nulled honestly (e.g. `reliability_at_32k: null`, `semantic_tool_correctness: null`) rather than padded | Most complete; source appendix (§15) separates model sources from runtime sources |
| Gemini | 16/16, all present but each is shorter/thinner | 18/18, mostly filled with confident-sounding INFERRED estimates rather than nulls (e.g. exact GB figures for every size class where ChatGPT/Perplexity leave the analogous fields as ranges or null) | Structurally complete but the least hedged output despite having the weakest evidence base — a mismatch worth flagging on its own |
| Perplexity | 16/16, all substantive, with a distinct "Follow-ups" and "90 sources" footer beyond the 16 required sections | 18/18, closest to ChatGPT in honest nulling of unknowns | Only agent to report an explicit source count and to distinguish DOCUMENTED from DOCUMENTED-with-unverified-date |

**Result: all three technically complete. ChatGPT and Perplexity score higher on honesty of incompleteness (nulling what's actually unknown); Gemini scores lower because its confident numeric fills (e.g., "~6.5 GB", "~10.0 GB", "~3.5 GB" memory estimates) read as more certain than its evidence (2024-era, non-live-search) supports.**

## 4. Evidence quality and fabrication check

Independent web-search spot-check performed against each agent's most load-bearing or least-familiar claims (results below reflect this session's own verification, not the agents' self-reported confidence):

| Claim checked | Agent(s) | Verification result |
|---|---|---|
| "Ministral 3" family exists (3B/8B/14B, Instruct + Reasoning variants, Apache 2.0, Dec 2, 2025 release) | ChatGPT, Perplexity (as Ministral-8B-Instruct-2410, an older sibling) | **Confirmed real.** Mistral's own site, AWS Bedrock, Hugging Face `transformers` docs, and an arXiv abstract all reference "Ministral 3" and "Mistral Large 3," consistent with a December 2025 release. |
| "Gemma 4 12B," released June 3, 2026, unified encoder-free architecture | ChatGPT, Perplexity (as Gemma 3, an older sibling) | **Confirmed real.** Google's own developer blog ("Introducing Gemma 4 12B: a unified, encoder-free multimodal model"), Google AI Gemma release notes, and multiple independent write-ups (Analytics Vidhya, GIGAZINE) confirm a June 2026 release matching the described architecture. |
| Qwen3-8B / Qwen3-14B exist with documented parameter counts and native/YaRN context lengths | ChatGPT, Perplexity | **Confirmed real.** Official Hugging Face repositories (`Qwen/Qwen3-8B`, `Qwen/Qwen3-14B`, plus GGUF/AWQ/FP8 variants) exist and match the cited size classes. |
| "Devstral Small 2 24B," Apache 2.0, coding-agent-focused, ~Dec 2025 | ChatGPT, Perplexity | **Confirmed real.** Mistral's own announcement ("Introducing: Devstral 2 and Mistral Vibe CLI"), Hugging Face (`mistralai/Devstral-Small-2-24B-Instruct-2512`), LM Studio and Unsloth documentation all corroborate. |
| Llama 3.1 8B / Qwen2 7B / Mistral v0.3 7B / Gemma 2 9B / Phi-3 family (Gemini's entire shortlist) | Gemini | **Confirmed real but stale** — these are genuine 2024-era models, not fabrications. The problem is currency, not existence: none of them reflects the "current landscape" the prompt asked for, and Gemini's own executive finding cites Llama 3.1/Qwen2 as if they were still the frontier 7–8B options, which they are not given the Ministral 3 / Qwen3 / Gemma 4 releases ChatGPT and Perplexity found. |

**Fabrication count: 0 across all three agents.** This is a materially positive finding — the calibration round's biggest risk (a model confidently inventing a plausible-sounding release) did not occur. Gemini's failure mode is staleness/self-disclosed search unavailability, which is a different and more containable problem than fabrication.

## 5. Cross-agent contradiction table

Contradictions are preserved, not averaged away, per the plan's explicit instruction. A contradiction where all three agree is flagged separately as a possible shared-training-bias signal.

| Claim | ChatGPT | Gemini | Perplexity | Verifiable? | Assessment |
|---|---|---|---|---|---|
| Best current 7–8B candidate | Ministral 3 8B Instruct (Dec 2025) | Llama 3.1 8B Instruct (Jul 2024) | Qwen3-8B (2025) | Yes — release dates are checkable | Gemini's pick is materially outdated; ChatGPT and Perplexity disagree with each other on family (Ministral vs Qwen) but both point to a real, current (2025) release — a genuine, useful disagreement to resolve empirically in the benchmark, not a red flag |
| Overall confidence score | 84/100 | 85/100 | 72/100 | No — self-reported, not independently checkable | Notable: Gemini's confidence (85) is the *highest* of the three despite having the weakest, staleset evidence base and a disclosed search outage — this is the single most concerning number in the whole calibration round, since it suggests confidence calibration did not account for the disclosed limitation |
| Best 3–4B efficiency control | Qwen3-4B-Instruct-2507 | Microsoft Phi-3 Mini 3.8B | Qwen3-4B | Yes | ChatGPT and Perplexity agree (same model, same family as their 8B picks); Gemini again lands on a 2024 model consistent with its stale evidence base |
| Best 12–14B challenger | Gemma 4 12B-it | Mistral Nemo 12B Instruct | Qwen3-14B | Yes | Same pattern: ChatGPT/Perplexity current, Gemini stale |
| Intel Arc 140V / unified memory treatment | Explicitly discusses KV-cache and shared-memory contention rather than fixed VRAM budgets | Reports flat GB estimates per size class without unified-memory caveats | Explicitly cites Intel's own statement that shared-memory GB is not a dedicated reservation | Yes — this is exactly the boundary the plan flagged as a sharp discriminator | Perplexity is most rigorous here; ChatGPT is adequate; Gemini is the weakest and is the only one that risks the "VRAM inference" boundary violation the plan warned about |
| Zero-shot agreement on "no APEX evidence exists yet" | Yes (MEASURED: none) | Implicit (frames everything as INFERRED) | Yes (explicit UNKNOWN sections) | N/A — this is unanimous agreement on an unverifiable-until-tested claim | Flagged per plan instructions: unanimous agreement here is *expected and correct*, not a bias signal, since it reflects the actual state of the world (no benchmark has run yet), not a shared training artifact |

## 6. Routing recommendation for prompts B–F

Based on this calibration round:

ChatGPT and Perplexity both cleared every boundary, cited verifiably current sources, showed zero fabrication, and used the MEASURED/DOCUMENTED/INFERRED/UNKNOWN taxonomy rigorously. Either is suitable to lead the remaining prompts (CODING, WEEKLY-MULTIAGENT, WINDOWS-INTEL-RUNTIME, BENCHMARK-HARNESS). Perplexity's edge is stronger sourcing discipline (explicit source counts, an added DEPRIORITIZED label, explicit Intel unified-memory sourcing) and slightly more conservative confidence calibration (72 vs. 84/85), which is arguably the more trustworthy posture for research whose entire point is to avoid overconfidence. ChatGPT's edge is a more decision-oriented executive framing and a cleaner separation of model sources from runtime sources in its appendix.

**Recommendation: run prompts B–E in both ChatGPT and Perplexity (continue the three-way design is not required for every remaining prompt given Gemini's result — see below), and use Perplexity as the tie-breaker/lead for WINDOWS-INTEL-RUNTIME specifically**, since that prompt is exactly where Gemini's unified-memory boundary weakness and Perplexity's unified-memory rigor matters most.

**Gemini should not be run again in its current configuration.** Its failure was not capability — Gemini 3.1 Pro is a current, capable model — but a session-level inability to search live, which it disclosed honestly but which the UI/output did not otherwise flag (the YAML still claimed a live `evidence_date`). Before including Gemini in Round 2, either (a) explicitly verify and force live grounding/search-tool invocation is active before submitting the bundle, and require the agent to state which of its outputs are search-grounded versus internal-baseline; or (b) escalate specifically Gemini to Deep Research mode, which is more likely to force actual retrieval. Do not rerun Gemini in plain standard chat mode without first confirming search is functioning — a repeat of this run would silently reproduce the same staleness.

## 7. Verdict: was standard mode sufficient?

**Partially.** For ChatGPT and Perplexity, standard chat + web search on was sufficient to produce current, well-sourced, boundary-compliant research — no evidence that Deep Research depth is needed for either of them on this prompt type. For Gemini, standard mode was insufficient, but not for a depth reason: the mode itself may not have been the failure — the disclosed unavailability of live search this session was. This should be retested (confirm search tool availability before the next Gemini run) before concluding Gemini requires Deep Research; it may simply have needed working search in standard mode.

**No change is recommended to ChatGPT's or Perplexity's mode for Round 2.** Gemini's mode/configuration needs to be fixed or replaced before its next run, per Section 6.

## 8. Known limitations of this comparison

- This document was produced without any APEX benchmark-fixture execution; every "current vs. stale" and "boundary pass/fail" judgment above is a desk assessment against real-world release records, not a measurement of task-execution quality.
- Fabrication spot-checks covered the load-bearing, decision-critical claims (headline models named in each executive finding) rather than every DOCUMENTED claim in all three ~35–45KB outputs; a full line-by-line audit was not performed.
- "Beste" (Perplexity's auto model selection) does not disclose which underlying model actually produced this output, so any future attempt to reproduce or explain Perplexity's specific strengths should account for that opacity.
- No production model, runtime, or agent-routing decision is authorized by this document. It informs which subscription AI to run for the remaining research prompts; it does not select or approve any local model or runtime for APEX itself.
