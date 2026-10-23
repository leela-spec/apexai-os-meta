---
type: Reference
id: RESULTS-09-efficiency-audit
title: Token-efficiency and architecture audit - Findings
description: Challenges the 1476-token floor with caching, external standards, scope routing, and additive savings boundaries.
status: current
tags: [research-result, efficiency, caching, rp-09]
---

# RP-09 - Every remaining token-efficiency lever

**Verdict (confidence: high on caching and published baseline measurements; low on any untested new absolute token floor):** **1,476 tokens is NOT a proven minimum; it is just the author's smallest measured XML wording/depth scenario.** A three-rule serialization test recorded **221 XML tokens versus 190 table tokens**; the author **extrapolated**, without rendering and counting the complete block, an approximately **190-token full-block saving (1,622 - 190 = ~1,432)**. This undermines the justification for calling 1,476 a hard floor, but **does not establish** a smaller rule-preserving full-block candidate. Conversely, **no evidence demonstrates that a safe ~1,000-token rendering of *all* current rules exists**. The most aggressive arithmetic using the author's non-overlap-unverified numbers is **1,622 - 190 - 99 - 47 = 1,286**, not ~1,000. The strongest intervention is to stop treating raw input token count as the sole objective: **stable-prefix prompt caching dramatically reduces repeated input-token price**, while instruction interference, task success, tool calls, and read behavior still matter. The answer is **no verified ~1,000-token candidate** and **no empirically justified theoretical floor**; the current **projected** table scenario is **~1,432** (only three rules directly measured), while the XML scenario is **1,476** under reported savings assumptions.

## Evidence

| Claim | Source link | Evidence type | Supports / undermines |
|---|---|---|---|
| GPT-5.6+ OpenAI prompt caching uses reusable prefix breakpoints; common models charge 1.25x for cache writes and 0.1x for reads; in the documented 10-request example, one write + nine reads cost **2.15** ordinary-input units versus **10** without caching. | [OpenAI prompt caching documentation](https://developers.openai.com/api/docs/guides/prompt-caching) | Vendor documented pricing/mechanics, not measured cost in this repo | Strongly undermines simplistic "1,622 tokens are fully re-billed each turn" premise |
| Cache hits require matching prefixes; model/tool/schema/effort or compaction changes can break reuse. Cached input still counts against token-per-minute rate limits. | [OpenAI diagnostics](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics); [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) | Vendor documentation | Undermines "cached means free" |
| Anthropic historically documents 5m and 1h caching with 1.25x/2x writes and 0.1x reads; applicability and pricing must be verified for the operator's actual Claude model/product. | [Anthropic caching pricing](https://docs.anthropic.com/en/docs/about-claude/pricing) | Vendor documentation | Supports the cross-provider premise, not a universal price |
| Gemini 2.5+ supports implicit caching and may impose **model-specific minimum prefixes** (2,048 or 4,096 tokens in cited variants); cache discounts are not automatic for a standalone 1,622-token user block. | [Google Gemini caching](https://ai.google.dev/gemini-api/docs/caching?lang=python) | Vendor documentation | Undermines cross-provider "this specific block is cached" without trace evidence |
| Rich structural claims about file size, position and split did not yield detectable adherence effects in the tested 1,650-session study; task complexity mattered more. | [McMillan 2026 factorial study](https://www.alphaxiv.org/abs/2605.10039) | Controlled coding-agent study | Undermines treating minimum token length or position as an automatic quality win |
| Context files increased cost >20% without generally improving completion; unnecessary instructions can induce work, not just input overhead. | [Gloaguen et al. 2026](https://arxiv.org/abs/2602.11988) | Controlled coding-agent benchmark | Supports optimizing total workflow and instructions' marginal value |
| ASD-STE100 uses a controlled dictionary and writing rules to reduce ambiguity. Its **goal is clarity**, not proven LLM-token minimization. | [Official ASD-STE100](https://www.asd-ste100.org/STE_faq.html) | Established non-AI technical-writing standard | Supports precision and uniform vocabulary; no quantitative token saving claim |
| OASIS DITA's `conref` and conditional processing allow one authored block to be reused and filtered at **processing time**. | [OASIS DITA `conref`](https://docs.oasis-open.org/dita/v1.2/os/spec/archSpec/conref.html); [DITA conditional processing](https://docs.oasis-open.org/dita/v1.1/CD02/archspec/behaviors.html) | Formal information-architecture standard | Supports build-time single-source ownership; runtime token benefit only if output is actually shorter |
| RFC 2119 standardizes the meanings of MUST/SHOULD/MAY, updated by RFC 8174. | [IETF RFC 2119](https://www.rfc-editor.org/info/rfc2119/) | Formal standards drafting | Supports economical unambiguous modality; zero measured LLM-token reduction |
| Surgical safety checklists correlate with better clinical outcomes in a before/after multicenter study (death 1.5% to 0.8%); **does not imply LLM prompt checklists have the same effect**. | [Haynes et al., NEJM 2009](https://www.nejm.org/doi/full/10.1056/NEJMsa0810119) | Controlled-process outcome study, nonrandomized | Supports concise observable-action reminders; no claim about tokens/LLMs |
| The author's own baseline is 1,622: 1,148 body + 319 attributes + 111 tags + about 44 wrapper/rounding; the **~190 full-table saving is an extrapolation from three rules**, and -47 wording/-99-depth are reported scenarios that require remeasurement and overlap checks. | [`09-contract-block-v0.5.md`, sections 2-4](09-contract-block-v0.5.md); [`05-research-prompt-packets.md`, RP-09](05-research-prompt-packets.md) | Direct repository measurements/claims; methods not independently replicated | Supports **conditional arithmetic**, not a unique floor |

## Ranked lever inventory

**Tier meaning:** *Proven* = technique/measurement has an actual source, **not necessarily a proven token saving on v0.5**; *Plausible* = real mechanism without a controlled v0.5 result; *Speculative* techniques are separately listed below. `TBD` means **not honestly quantifiable without the source-specific tokenizer/ablation**; it is not zero.

| Rank | Lever | Tier | Token saving estimate on 1,622 | Risk/condition | Source |
|---:|---|---|---|---|---|
| 1 | **Measure cache hit rate and optimize unchanged stable prefix** | Proven (vendor mechanism) | **0 tokens** removed; potentially large recurring **billing-equivalent** savings, not size savings | Depends on model, exact prefix, reuse frequency, provider TTL | [OpenAI caching](https://developers.openai.com/api/docs/guides/prompt-caching) |
| 2 | **Whole-block table instead of XML** (author's three-rule measurement, extrapolated to whole block) | Plausible **whole-block saving; measured three-rule slice** | **~190 projected** (non-additive to some formatting changes); ~1,432 projected output | Unmeasured readability, rule selection, failure response | [`05`, RP-09](05-research-prompt-packets.md) |
| 3 | **Drop `deepen_when`** if RP-08 finds it redundant | Proven **local size measurement only** | **99 reported/unreplicated**, yielding **1,523** hypothetically from baseline | May lose escalation threshold; requires B/C read traces | [`09`, section 4](09-contract-block-v0.5.md) |
| 4 | **Further wording pass** | Proven **local claimed measurement only** | **47 reported**; yields 1,575 individually | May shrink critical nuance; do not count twice if already applied | [`09`, section 4](09-contract-block-v0.5.md) |
| 5 | **13 unconditional named tags -> bullets** | Proven **local claimed measurement only** | **~39** individually | Operator decided clarity outweighs this; cannot add to the all-table transformation | [`09`, section 4](09-contract-block-v0.5.md) |
| 6 | **Replace model-judged content routing with native scoped rules / skills** | Proven (supported runtime) | **TBD**, often 0 always-on kernel tokens saved, but can save downstream reads | Tool/version specificity, activation miss risk | [Cursor](https://docs.cursor.com/context/rules-for-ai); [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills) |
| 7 | **Eliminate redundant default-behavior instructions only after task ablation** | Plausible | **0 verified; upper bound is the measured token size of selected rule bodies** | Defaults are model/task dependent; actual omission may hurt critical edge cases | [OpenAI GPT-6 Astra skill/prompt audit](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) |
| 8 | **Semantic rule grouping / common-condition factoring** | Plausible | **TBD** (0 verified) | Different triggers must not collapse into one broader trigger | [RFC 2119 defined modality](https://www.rfc-editor.org/info/rfc2119/); [DITA reuse](https://docs.oasis-open.org/dita/v1.2/os/spec/archSpec/conref.html) |
| 9 | **Compile universal/repo-specific source to target agent entrypoints** | Proven as content-reuse concept; plausible for this prompt | **0 at runtime** if identical text emitted; prevents duplication/drift | Build step/maintenance not justified for one repo | [OASIS conref](https://docs.oasis-open.org/dita/v1.2/os/spec/archSpec/conref.html) |
| 10 | **Controlled register, fewer synonyms and limited imperative vocabulary** | Proven as non-AI standard; plausible for model token savings | **TBD** | Terms may tokenize worse; model may lose necessary distinctions | [ASD-STE100](https://www.asd-ste100.org/STE_faq.html) |
| 11 | **Replace prose promises with an actual already-supported permission/hook check for a critical action** | Proven as supported mechanism | **TBD**, often no direct prompt saving if explanation still required | Costs engineering/harness configuration; not justified solely for compression | [Claude hooks](https://code.claude.com/docs/en/memory) |

## Not on the author's list - genuinely additional angles

1. **DITA-style compile-time profiling and transclusion (field: technical publishing / structured documentation).** Keep one authoritative rule block and produce a small target-specific projection, *not* three hand-authored replicas. Unlike a prompt-internal `when`, filtering happens before the model sees the text. **Proven content-publishing technique, unmeasured v0.5 savings**. [OASIS](https://docs.oasis-open.org/dita/v1.1/CD02/archspec/behaviors.html).
2. **Normative modality vocabulary (field: standards and legal drafting).** RFC 2119 defines precise MUST/SHOULD/MAY semantics, reducing repetitive descriptions of obligation. **Proven standard; token benefit unmeasured**; any added definitions can negate savings. [IETF](https://www.rfc-editor.org/info/rfc2119/).
3. **Checklist materiality and exception discipline (field: medicine / aviation human factors).** Put only decision-critical observable checks in routine workflows, instead of lengthy explanation of why every rule exists. The NEJM checklist paper offers *process-outcome* evidence, **not agent compliance evidence**; use only as a design analogy. [NEJM](https://www.nejm.org/doi/full/10.1056/NEJMsa0810119).
4. **Cache-hit diagnostics as a first-class cost denominator (field: distributed caching and performance engineering).** Count cache writes, cache reads, tool round-trips, and context misses; compare **cost per successful task**. This changes which 100-token savings are worth working on. [OpenAI diagnostics](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics).
5. **Distinguish source of truth from deployed text (field: compilers/configuration management).** A versioned source can emit AGENTS.md plus tool-specific adapters; no language model should decide inclusion when hard scope is known at build time. **Production practice analogue; no independent prompt-specific token reduction claimed**. [OASIS](https://docs.oasis-open.org/dita/v1.2/os/spec/archSpec/conref.html).

### Default-behavior elimination candidates (NOT findings of redundancy)

A modern coding agent **may** already do several tasks without an explicit clause. Strongest **test-only** candidates: `<communication>` (active voice, avoid filler); `<iterative>` (plan a complex task); `<recovery>` (recover from routine incidental failure); `<reuse>` (look for existing tools), and aspects of `<context>` (avoid indiscriminate bulk loads). By contrast, **do not presume** the operator-specific `<target>`, `<scope>`, `<surgical>`, `<ground>` with path-line evidence, or `<stop_repairing>` are defaults. The September 2026 OpenAI discussion explicitly warns that excessive historical scaffolding can hinder modern agents, but it does not validate omission of **any one of these specific rules**. [OpenAI](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Local ablations must score actual task outcomes; until then **all candidate deletions save 0 evidence-backed tokens**.

## Speculative - DO NOT RECOMMEND WITHOUT TOKENIZER AND COMPLIANCE TESTS

- **Shared short-code dictionary:** define `ED`, `DR`, `TR` once and reference them across multiple clauses. Might save bytes, but definitions + unusual tokenization can increase model tokens; 0 verified.
- **Telegraphic shorthand or domain-specific compact DSL:** remove articles and use punctuation-heavy abbreviations. English BPE tokenizers can assign multiple tokens to uncommon abbreviations. 0 verified.
- **Rule-body factoring across unrelated triggers:** compress overlapping text into one subrule; could erase exceptions or cause over-application. 0 verified.
- **Model-differential rule assignment:** serve different default subsets to different model releases. Requires version- and task-specific empirical evidence; 0 verified.

## Floor arithmetic and double-counting controls

| Scenario from reported measurements | Arithmetic | Result | What is actually warranted |
|---|---|---:|---|
| Current v0.5 measured candidate | - | **1,622** | Repo-reported baseline, not independently retokenized here |
| Wording only | 1,622 - 47 | **1,575** | Reported compression option; check whether 47 already applied |
| Drop all `deepen_when` only | 1,622 - 99 | **1,523** | Measured size, unvalidated behavior |
| Wording and depth (assume non-overlap) | 1,622 - 47 - 99 | **1,476** | The author's **scenario**, **not** a universal floor |
| Wholesale table alone | 1,622 - 190 | **~1,432** | Extrapolation from three-rule test, not an observed full-block candidate; undercuts asserted floor rationale |
| Table + depth + wording (unproven additive upper illustration) | 1,622 - 190 - 99 - 47 | **~1,286** | **DO NOT treat as measured**; transformations may overlap |
| Required further saving from illustrative 1,286 to 1,000 | 1,286 - 1,000 | **286** | No documented, rule-preserving 286-token lever identified |

**Recommended operational total: 1,622 until a behavior-preserving candidate wins the experiment.** If size pressure remains, evaluate ~1,432 table vs ~1,476 XML, then select by rule-following *and* cost per completed task. **Floor verdict: unknown**, with **projected** smaller whole-block serialization near ~1,432 (not yet rendered or validated) and a nonadditive 1,286 illustration. ~1,000 remains **unverified**, neither mathematically impossible nor evidence-backed.

## Prompt-caching verdict - is raw token count the right optimization variable?

**No, not by itself.** An always-loaded block is not necessarily charged full price each turn when the model reuses an unchanged prefix. OpenAI's vendor example gives 10 requests costing 2.15 uncached-input equivalents under one write + nine reads, a 78.5% reduction in that *specific pricing model*; it still costs money, occupies prompt context, consumes rate budget, can cause instruction interference, and may miss cache if the prefix or settings change. For a rare one-off request, caching may make little difference; for a high-hit repeated agent session, reducing 100 cached tokens can be less valuable than avoiding a single unnecessary tool call. **Measure usage, not assume.**

## Strongest case against the verdict

The author's 1,476 estimate may still be a sensible lower bound for the *chosen XML readability and semantics*, because the table can collapse per-rule identity, conditional scope and the clarity preference. Newer models can be more sensitive to terse abbreviations, so optimizing below a clear prose threshold risks regressions. Conversely, cache misses and bursty new sessions can make raw token cost dominate again. Neither side licenses the categorical claim that 1,000 is impossible or that token count does not matter at all.

## What I could not find

- The exact tokenizer, test harness, and raw side-by-side candidate strings that produced the repo's -47/-99/-190 figures; no independent token remeasurement was possible from the cited result-only measurements.
- A measured, correctness-preserving **1,000-token** rendering of the 22 blocks on the operator's actual model/tool stack.
- Evidence that terse symbolic/telegraphic writing lowers *model* token count while preserving clause-by-clause adherence for this content.
- Local cached/uncached usage data and cache hit rates for Codex, Claude Code, Gemini CLI, or their subscription/API routing in this repository.
- Evidence for treating the exact 47, 99 and 190 savings as simultaneously achievable: they may overlap.

## Consequence for the contract

- **Withdraw the claim that ~1,476 is an objective floor.** Keep it only as a named XML candidate.
- **Do not set a mandatory 1,000-token cap** or drop important rules solely to hit an unevidenced number.
- **Reframe success as accurate outcomes per total uncached/cached cost and agent actions.** This does not eliminate the need for readable, minimal always-on invariants.
- Carry to `RP-06`: test the table alongside XML and bullets, not only the 39-token unconditional-label swap. Carry to synthesis: **never add mutually exclusive formatting savings**.
