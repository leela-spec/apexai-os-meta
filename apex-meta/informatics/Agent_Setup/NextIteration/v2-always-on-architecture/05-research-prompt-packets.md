---
type: Reference
id: V2-RESEARCH-PROMPTS-v1.0
title: Research Prompt Packets — Gating Efficacy, Vector Retrieval, Currency Check
description: Three provider-unspecified prompt packets built to the PromptEngineer contract, covering whether conditional instruction gating works, whether vector retrieval supersedes static dispatch, and where the current architecture reasoning is out of date.
status: candidate_not_active
tags: [prompts, research, prompt-packet, provider-unspecified]
---

# Research Prompt Packets

> **Prompts only — no research has been run.** Each packet is built to the contract in
> `.claude/skills/PromptEngineer/SKILL.md`: metadata outside the prompt body, one primary prompt
> per packet, explicit output contract, validation criteria, failure hints, learning hints.
>
> `provider_target: provider_unspecified` for all three, per operator decision. The prompt bodies
> carry no provider-specific phrasing and no source document names, so they are portable and
> runnable anywhere.

---

## Packet 1 — Does conditional instruction gating actually work?

```yaml
prompt_packet:
  id: RP-01-gating-efficacy
  prompt_task_type: literature_and_evidence_review
  workflow_stage: architecture_validation
  process_stage: pre_implementation_evidence_gathering
  expected_output_type: evidence_review_with_verdict
  provider_target: provider_unspecified
  provider_rationale: >
    Needs current web sources with citation discipline. No provider-specific capability is
    required beyond retrieval and careful synthesis.
  prompt_design_rationale: >
    Framed to find DISCONFIRMING evidence first, because the operator's architecture depends on
    gating working and the natural failure is motivated reasoning. Demands a verdict with an
    explicit confidence level rather than a survey.
  usage_tracking_tags: [architecture, gating, instruction-following, blocking-decision]
  validation_status: valid
```

**Why this matters:** the whole conditional-dispatch design assumes an agent honours an IF-clause.
Falsifies `DEC-16` and `DEC-M2` if the answer is no.

### Copy-paste prompt

> You are an evidence reviewer. I need to know whether a specific technique actually works before I
> build an architecture on it. **Find reasons it fails before you find reasons it works.**
>
> **The technique.** An always-loaded instruction file given to an AI coding agent contains
> conditional directives of roughly this shape:
>
> ```
> IF the task is editing an existing file THEN read reference/patching.md
> IF the task is comparing options THEN read reference/comparison.md
> Paths are just-in-time pointers. Do not expand them into context unless the condition matches.
> ```
>
> The intent is that the agent reads only the referenced file whose condition matches, and ignores
> the others — reducing how much instruction text occupies its context.
>
> **The question.** Does an agent actually honour such a condition, or does it ignore the gate and
> read whatever seems relevant, or read everything?
>
> **Investigate all of these:**
> 1. Published evidence on conditional or scoped instruction following — benchmarks measuring
>    whether models correctly apply a directive only under its stated condition, and whether they
>    over-apply it outside that condition.
> 2. Evidence on whether models respect negative or restrictive directives ("do not read X unless
>    Y") as reliably as positive ones. If there is an asymmetry, quantify it.
> 3. Whether conditional structure measurably changes behaviour compared to the same content
>    written as plain unconditional prose. This is the crux — if gating adds nothing over prose,
>    the structure is decorative.
> 4. Whether markup-delimited conditions (attribute-carrying tags) behave differently from plain
>    text IF/THEN sentences.
> 5. Reported failure modes: over-triggering, under-triggering, ignoring conditions entirely, or
>    speculatively loading referenced material regardless of the gate.
> 6. How instruction count and instruction interference affect all of the above — if adding
>    conditions increases total instruction count, does the interference cost outweigh the benefit?
>
> **Output contract.**
> - A one-paragraph verdict first: does this technique work, with a confidence level of high,
>   medium or low, and the single strongest piece of evidence behind that verdict.
> - An evidence table: each row a claim, its source with a link, the type of evidence
>   (controlled benchmark / production report / anecdote / vendor documentation), and whether it
>   supports or undermines the technique.
> - A section titled "Strongest case that this does not work" — argue it properly, do not
>   strawman it.
> - Known failure modes with any reported rates.
> - Concrete design guidance: if the technique works only under certain conditions, state them
>   precisely.
> - An explicit list of what you could not find evidence for.
>
> **Validation criteria.**
> - Every quantitative claim carries a source link. No unsourced numbers.
> - Vendor documentation is labelled as vendor documentation, never as independent evidence.
> - If the honest answer is "there is no good evidence either way," say exactly that rather than
>   assembling weak sources into a false verdict.
> - Distinguish evidence about *system prompts* from evidence about *tool-using agents that read
>   files*. They are different situations and conflating them invalidates the review.
>
> **Stop when** you have either found controlled evidence on question 3, or established that none
> exists and said so.

```yaml
prompt_failure_hints:
  - "A survey of prompt-engineering advice instead of evidence. Demand measurements."
  - "Conflating system-prompt instruction following with agentic file-reading behaviour."
  - "Treating vendor docs as independent evidence."
  - "Skipping question 3, which is the only one that isolates gating from content."
prompt_learning_hints:
  - "If question 3 has no published evidence, that result makes the local empirical test the only source — raise its priority."
  - "Any reported over-triggering rate feeds directly into the bloat-rate threshold in the test protocol."
```

---

## Packet 2 — Could vector retrieval replace static IF-dispatch?

```yaml
prompt_packet:
  id: RP-02-vector-retrieval-alternative
  prompt_task_type: architecture_option_evaluation
  workflow_stage: architecture_validation
  process_stage: alternative_assessment
  expected_output_type: comparative_assessment_with_recommendation
  provider_target: provider_unspecified
  provider_rationale: >
    Requires current production practice, not only published papers. Retrieval plus synthesis;
    no provider-specific capability needed.
  prompt_design_rationale: >
    Written to let the alternative win. The requester has already invested in static dispatch, so
    the prompt explicitly instructs the reviewer to make the strongest case for retrieval and to
    name what the incumbent does better only afterwards.
  usage_tracking_tags: [architecture, retrieval, rag, alternative-assessment]
  validation_status: valid
```

**Why this matters:** could supersede the entire dispatch design. The operator's concern — that the
current framing may be out of date — is the reason this packet is framed to favour the challenger.

### Copy-paste prompt

> You are evaluating an architectural alternative. The person asking has already built one
> approach and may be anchored on it. **Your job is to make the strongest possible case for the
> alternative**, then state honestly where the incumbent is still better.
>
> **The incumbent.** A set of instruction documents for AI coding agents. A small always-loaded
> file carries universal rules plus hand-written conditional pointers to larger detail files. The
> agent reads a detail file only when a condition matches. All routing is static and authored by
> hand.
>
> **The alternative.** Instruction content is chunked and embedded. At task time, relevant chunks
> are retrieved semantically and injected into context. No hand-authored conditions; relevance is
> computed.
>
> **Investigate:**
> 1. Is semantic retrieval over *instruction and policy* content — as opposed to over knowledge or
>    documentation — actually done in production in 2026? Name real systems if they exist.
> 2. How does retrieval handle rules that must apply **unconditionally**? A safety invariant that
>    is retrieved 95% of the time is not an invariant. Is there an established pattern for mixing
>    guaranteed content with retrieved content, and what is it called?
> 3. Measured retrieval quality on short imperative rules. Rules are terse, semantically similar to
>    one another, and lack the surrounding prose that retrieval usually relies on. Does retrieval
>    degrade on this content type specifically?
> 4. Operational cost: embedding infrastructure, index freshness when a rule is edited, latency,
>    and what happens when an edit and a retrieval race.
> 5. Hybrid designs: static invariants plus retrieved detail. Who does this, and what have they
>    reported?
> 6. Failure modes: retrieving a contradictory rule pair, missing the one rule that mattered,
>    retrieving stale content after an edit.
> 7. What the current state of the art actually is for agent instruction architecture in 2026 —
>    including any approach neither of the two above. Assume the asker's framing may be a year out
>    of date and correct it if so.
>
> **Output contract.**
> - Open with the strongest case for retrieval, stated as its advocate would state it.
> - Then a comparison table: dimension, static dispatch, retrieval, hybrid — covering guarantee of
>   application, token cost, authoring effort, maintenance under edits, failure mode, and
>   operational complexity.
> - A direct answer on the unconditional-rules problem. This is the decisive question; do not
>   leave it vague.
> - A recommendation with the conditions under which it flips to the other option.
> - A section titled "What the asker appears not to know" — any development, pattern, or tool
>   relevant here that their framing omits.
>
> **Validation criteria.**
> - Distinguish *knowledge* retrieval from *instruction* retrieval throughout. Most published work
>   is about the former; do not silently generalise it to the latter.
> - If instruction-RAG is rare in production, say so plainly rather than inferring from
>   knowledge-RAG that it must work.
> - Every production claim names a real system or is marked as inference.
> - State explicitly whether the asker's static approach is behind current practice, current with
>   it, or ahead of it.
>
> **Stop when** question 2 has a concrete answer, since it determines whether retrieval can carry
> safety invariants at all.

```yaml
prompt_failure_hints:
  - "Generalising from document-RAG to instruction-RAG without flagging the leap."
  - "Recommending retrieval without resolving the unconditional-invariant problem."
  - "Returning a neutral survey instead of a recommendation with flip conditions."
prompt_learning_hints:
  - "If retrieval cannot guarantee invariant application, hybrid is the only viable form and the always-on block survives regardless of this result."
  - "A named production instruction-RAG system would be the single most valuable finding here."
```

---

## Packet 3 — What is this architecture reasoning missing?

```yaml
prompt_packet:
  id: RP-03-currency-check
  prompt_task_type: adversarial_review
  workflow_stage: architecture_validation
  process_stage: assumption_audit
  expected_output_type: gap_and_staleness_report
  provider_target: provider_unspecified
  provider_rationale: >
    Needs current awareness and a willingness to contradict the submitted framing. No
    provider-specific capability required.
  prompt_design_rationale: >
    States the design's own assumptions up front as targets, rather than asking for a general
    review, so the reviewer attacks specific claims instead of commenting on style.
  usage_tracking_tags: [architecture, staleness-check, adversarial-review]
  validation_status: valid
```

**Why this matters:** the operator's direct concern — *"maybe you are not up to date and limited in
your view."* This packet exists to answer that rather than defend against it.

### Copy-paste prompt

> You are auditing an architecture design for stale assumptions. The author may be reasoning from
> outdated information. **Find what they are missing.** Do not comment on writing quality.
>
> **The design, stated as claims. Treat each as a target.**
>
> 1. Instruction content for an AI coding agent should be split into three tiers: always loaded;
>    loaded when a condition matches; opened only for a specific lookup.
> 2. An always-loaded instruction file should sit near 1,000 tokens. Longer files dilute attention.
> 3. Critical rules belong at the very start and very end of a file, because attention favours
>    beginning and end and neglects the middle.
> 4. A conditional branch only reduces token cost when it points at a separate file. A condition
>    pointing at a section of a file already being read saves nothing.
> 5. Restating the same rule across several files risks the copies drifting apart, and
>    contradiction between copies degrades compliance more than the token cost of redundancy.
> 6. Markup-delimited structure earns its token overhead only where a block needs a named,
>    attribute-carrying handle; plain markdown is cheaper everywhere else.
> 7. Hand-authored conditional routing is the right mechanism for deciding which instruction file
>    an agent loads.
>
> **For each claim:** is it current, outdated, oversimplified, or wrong? Cite evidence. Where a
> claim was true but has been superseded, say what superseded it and when.
>
> **Then tell them what they have not considered.** Specifically:
> - Developments in agent instruction architecture, context management, or memory from the last
>   twelve months that change any of the above.
> - Whether runtime features now handle any of this automatically, making manual design obsolete.
> - Whether caching behaviour changes the cost calculus — if an always-loaded block is cached,
>   does its token cost still matter the way the author assumes?
> - Any mechanism for conditional loading other than hand-authored rules or semantic retrieval.
> - Whether measuring cost in tokens is even the right frame, or whether something else now
>   dominates.
>
> **Output contract.**
> - A claim-by-claim verdict table: claim number, verdict, evidence with link, what replaced it if
>   superseded.
> - A section titled "Not considered" — the highest-value omissions, ranked by how much each would
>   change the design.
> - A section titled "Still correct" — which claims hold up, so the author knows what to keep.
> - One sentence: is this design broadly current, or materially behind?
>
> **Validation criteria.**
> - Attack the claims, not the presentation.
> - Date every "this changed" assertion.
> - If a claim is simply correct and current, say so — do not manufacture criticism to seem
>   thorough.
> - Separate things that are genuinely new from things the author could have known and missed.
>
> **Stop when** every numbered claim has a verdict and the "Not considered" section has at least
> three substantive entries, or you have established there are none.

```yaml
prompt_failure_hints:
  - "Generic 'consider also...' advice with no evidence or dates."
  - "Agreeing with all seven claims. If nothing is outdated, say so explicitly and explain why that is plausible."
  - "Reviewing the writing rather than the claims."
prompt_learning_hints:
  - "Claim 4 is the newest and least externally validated; a contradiction there invalidates the file-splitting decision."
  - "A finding on caching would change the cost model for every number in the design."
  - "Claim 7 overlaps packet 2 — compare the two answers for consistency before accepting either."
```

---

## Dispatch guidance

| | |
|---|---|
| **Order** | Run all three in parallel. They are independent, and packet 2 could invalidate the architecture that packet 1 tests — so neither should wait on the other. |
| **Relation to the empirical test** | [04-empirical-test-protocol.md](04-empirical-test-protocol.md) measures *this repository*. Packet 1 asks what is known generally. If they disagree, the local measurement wins for local decisions, and the disagreement itself is worth recording. |
| **On return** | Record findings as new files in this folder. Do not edit the decision register's Part A — add a Part G for research outcomes, so the original positions stay visible alongside what revised them. |

```yaml
prompt_quality_review:
  packets: 3
  one_primary_prompt_per_packet: true
  metadata_outside_prompt_body: true
  output_contract_explicit: true
  validation_criteria_explicit: true
  stop_conditions_present: true
  no_source_document_names_in_prompt_bodies: true
  no_unrequested_capture_blocks: true
  provider_target: provider_unspecified
  validation_status: valid
  operator_review_flags:
    - "Packet 2 may return 'instruction-RAG is not an established production pattern'. That is a valid and useful result, not a failed prompt."
    - "Packet 3 is written to invite contradiction of the current design. Expect it to disagree with positions recorded in 01-decision-register.md Part C."
```
