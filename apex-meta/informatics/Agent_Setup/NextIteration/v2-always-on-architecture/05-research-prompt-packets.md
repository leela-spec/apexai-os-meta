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

---

## Packet 4 — What is the established term for this communication register?

```yaml
prompt_packet:
  id: RP-04-register-terminology
  prompt_task_type: terminology_identification
  workflow_stage: contract_wording
  process_stage: rule_authoring
  expected_output_type: named_term_with_definition_and_usage
  provider_target: provider_unspecified
  provider_rationale: Retrieval and terminology synthesis; no provider-specific capability needed.
  prompt_design_rationale: >
    The operator recalls a named concept for a specific writing register but not the name. The
    prompt describes the register behaviourally and asks for the established term, explicitly
    warning against inventing one or forcing a weak match.
  usage_tracking_tags: [wording, register, terminology]
  validation_status: valid
```

**Why this matters:** `<communication>` currently carries a descriptive placeholder. A named,
established register would be shorter and more reliably understood than a list of adjectives.

### Copy-paste prompt

> I am writing a style directive for an AI agent and need the **established term** for a specific
> communication register. I recall there is a recognised name for it but cannot retrieve it.
>
> **The register, described behaviourally:**
> - scientific and rational
> - neutral and unemotional
> - fact-oriented; claims are tied to evidence
> - no decorative prose, no filler, no flattery, no enthusiasm padding
> - high information density — maximum content per sentence
> - precise and questioning rather than agreeable
>
> **Find the term.** Check all of these families and say which, if any, actually fits:
> 1. Technical-writing and documentation standards (controlled languages, plain-language standards,
>    editorial register names).
> 2. Linguistics and register theory — formal names for this kind of writing.
> 3. Journalism and encyclopedic editorial standards.
> 4. Scientific and academic writing conventions.
> 5. AI and prompt-engineering vocabulary — named output styles, personas or modes, **including any
>    colour-coded scheme that labels AI communication styles.** The operator recalls seeing a
>    colour association and suspects it may be outdated; confirm whether such a scheme exists, name
>    it, and say whether it is current or superseded.
> 6. Personality and communication-style frameworks that use colour coding, and whether any maps to
>    this register.
>
> **Output contract.**
> - The single best-fitting established term, with its source and definition. If several fit
>   different facets, name each and say which facet it covers.
> - A short table: term, field of origin, what it captures, what it misses.
> - A verdict on the colour scheme specifically: does one exist for AI communication styles, what is
>   it called, is it current, and does it match the description above?
> - One directive sentence usable verbatim in an instruction file that invokes this register as
>   compactly as possible.
>
> **Validation criteria.**
> - **Do not invent a term.** If no established term covers this precisely, say so and give the
>   closest partial matches instead.
> - Distinguish terms with a formal standard behind them from informal community vocabulary.
> - Flag any term that carries unwanted connotations alongside the intended meaning.
> - Keep the usable sentence under 20 words.
>
> **Stop when** you have either a well-sourced term or a clear statement that none exists.

```yaml
prompt_failure_hints:
  - "Inventing a plausible-sounding term. The honest answer may be that no single term exists."
  - "Returning generic 'be concise and professional' advice instead of a named register."
  - "Ignoring question 5, which is the operator's actual recollection."
prompt_learning_hints:
  - "If no single term exists, the descriptive placeholder in <communication> stays and this closes."
  - "A colour scheme that turns out to be real and current may carry other useful style vocabulary."
```

---

## Packet 5 — Stopping self-authored acceptance criteria

```yaml
prompt_packet:
  id: RP-05-self-authored-criteria
  prompt_task_type: instruction_design_evidence_review
  expected_output_type: phrasing_recommendation_with_evidence
  provider_target: provider_unspecified
  prompt_design_rationale: >
    Asks which of three directive forms measurably works, rather than which sounds best, because
    the failure mode is specific and observable.
  usage_tracking_tags: [wording, target, acceptance-criteria]
  validation_status: valid
```

**Decides:** the `<target>` wording, currently provisional.

### Copy-paste prompt

> An AI coding agent is given a task with stated requirements. A recurring failure: the agent writes
> its own test, schema or checklist, that artifact passes, and the agent reports success — but the
> self-authored artifact was weak and never actually checked the stated requirement. The agent's own
> criteria silently replaced the operator's.
>
> **Find what measurably prevents this.** Compare at least these directive forms:
> 1. **Prohibition** — "never invent your own acceptance criteria."
> 2. **Positive validation duty** — "before reporting completion, check the result against each
>    stated requirement."
> 3. **Ordering rule** — "operator-stated criteria outrank anything you infer or author."
> 4. **Conflict rule** — "where your artifact and the stated requirement disagree, the requirement
>    wins."
> 5. Any form used in practice that is not on this list.
>
> Investigate: evidence on reward hacking and specification gaming in agents; whether models comply
> better with prohibitions or with positive duties; whether an explicit completion checklist against
> stated requirements measurably reduces false completion claims; and any published agent
> instruction set that solves this, quoted verbatim.
>
> **Output contract.** A recommendation naming which form or combination to use, with evidence. A
> comparison table: form, mechanism, evidence, failure mode. One directive usable verbatim, under 50
> words. An explicit note on whether combining forms helps or whether it just adds instruction count.
>
> **Validation criteria.** Distinguish measured results from advice. If the evidence is thin, say so
> rather than ranking on plausibility. Flag any form that could cause the opposite failure — an
> agent that refuses to write any test at all.
>
> **Stop when** you can name a form with evidence behind it, or state that none has been measured.

```yaml
prompt_failure_hints:
  - "Recommending all four forms. Instruction count has a cost; pick."
  - "Conflating this with general hallucination research - the failure is criteria substitution."
prompt_learning_hints:
  - "If positive duties beat prohibitions, several other rules in the contract should be reworded the same way."
```

---

## Packet 6 — Compact condition syntax

```yaml
prompt_packet:
  id: RP-06-condition-syntax
  prompt_task_type: format_efficiency_evaluation
  expected_output_type: syntax_recommendation_with_measurements
  provider_target: provider_unspecified
  prompt_design_rationale: >
    Reframed after measurement. The expensive part is the condition and pointer machinery, not the
    tag names, so the prompt asks about conditions specifically.
  usage_tracking_tags: [format, conditions, token-efficiency]
  validation_status: valid
```

**Decides:** `DEC-17` final form, and the serialization of the whole block.

**Scope correction:** this packet was briefly narrowed to conditions only, on the strength of a
measurement showing tag names cost just 7%. That measurement tested one narrow swap — unconditional
tags to bullets, same structure — and found 39 tokens. A **wholesale reformat is a different and
larger lever.** Measured locally on identical content across three gated rules:

| Serialization | Tokens | vs XML |
|---|---:|---:|
| XML tags + attributes | 221 | — |
| Bullets with `IF … →` prefix | 198 | **−10%** |
| Markdown table | 190 | **−14%** |

Extrapolated across the block that is roughly **190 tokens (12%)**, not 39. The packet is therefore
widened back to the full format question.

### Copy-paste prompt

> An always-loaded instruction file for an AI coding agent contains about twenty rules. Twelve are
> unconditional. Nine carry a machine-readable condition plus a file pointer, in this shape:
>
> ```
> <editing when="changing, moving or deleting a file that already exists"
>          ref="informatics/execution-modes.md"
>          deepen_when="the edit spans multiple blocks or goes to a deterministic executor">
> rule body
> </editing>
> ```
>
> Measured composition: rule bodies 73%, **attributes 20%**, tag names 7%. A local test on identical
> content found bullets ~10% cheaper than XML and a markdown table ~14% cheaper.
>
> **Find the most token-efficient serialization that does not degrade how reliably the agent applies
> the right rule.** Compare at minimum:
>
> 1. **Paired XML tags with attributes** (current).
> 2. **Bullets with an inline condition prefix** — `- IF <condition> → <file>: <rule>`.
> 3. **A markdown table** — columns for condition, pointer, rule.
> 4. **Abbreviated attributes** — `w=` / `r=` instead of `when=` / `ref=`.
> 5. **Headings per rule** with conditions in the body text.
> 6. **A hybrid** — unconditional rules as a bullet list, conditional rules as a table.
> 7. **Any serialization in production use** that none of the above captures.
>
> For each report: token cost; whether models reliably parse it; and crucially **whether any is
> known to degrade condition-matching accuracy or rule application**. A format that saves 14% and
> loses 10% of rule compliance is a bad trade — say so if the evidence supports it.
>
> Then answer three direct questions:
> - **Is a separate "go deeper" condition worth its tokens**, or does a file pointer alone carry
>   enough signal?
> - **Do tables degrade multi-sentence rule bodies?** Several rules here are three or four sentences,
>   and a long table cell is hard to scan.
> - **Does the right answer differ between the unconditional and conditional rules?** They have
>   different structural needs.
>
> **Output contract.** A ranked recommendation with token estimates. A table: form, tokens, parse
> reliability, evidence quality, failure mode. Direct verdicts on all three questions above. One
> rewritten example of the block above in the recommended form.
>
> **Validation criteria.** Do not recommend on aesthetics; cite measurement or label it unmeasured.
> Flag any form that buys tokens with ambiguity. Distinguish evidence about short prompts from
> evidence at twenty-rule scale — they are not the same regime. "No published measurement exists" is
> a valid finding.
>
> **Stop when** all three direct questions are answered.

```yaml
prompt_failure_hints:
  - "Returning generic XML-vs-markdown advice. The question is condition syntax at ~20 rules."
  - "Ignoring the direct question about the secondary depth condition."
prompt_learning_hints:
  - "A verdict against the depth condition saves ~99 tokens immediately."
```

---

## Packet 7 — What actually reduces over-building

```yaml
prompt_packet:
  id: RP-07-over-building
  prompt_task_type: intervention_effectiveness_review
  expected_output_type: intervention_recommendation
  provider_target: provider_unspecified
  prompt_design_rationale: >
    Asks which intervention point works, since the current design bets on a pre-action check and
    that bet is untested.
  usage_tracking_tags: [over-building, ceremony, intervention]
  validation_status: valid
```

**Decides:** `<new_machinery>`, and feeds `DEC-20`.

### Copy-paste prompt

> AI coding agents reliably over-build: they add scripts, tests, gates, schemas, wrappers and
> abstractions that were not asked for and do not advance the product. A documented case had an
> autonomous run spend almost its entire budget on process and verification work, then stop without
> delivering.
>
> **Find what measurably reduces this.** Compare intervention points:
> 1. **Pre-action check** — before adding machinery, confirm ordinary use does not already surface
>    the problem. *(the current design's bet)*
> 2. **Budget** — a cap on files, steps or tool calls.
> 3. **Post-hoc review** — a separate pass that flags unnecessary additions.
> 4. **Output contract** — specifying the deliverable so tightly that extras are visibly out of scope.
> 5. **Explicit permission gate** — agent must ask before adding machinery.
> 6. Anything in practice not listed.
>
> Also answer: is over-building better treated as a **scope** failure, a **reward/completion-signal**
> failure, or a **planning** failure? The framing determines where the fix belongs.
>
> **Output contract.** A ranked recommendation with evidence. A table: intervention, mechanism,
> evidence, failure mode, cost. A verdict on whether a pre-action check is the right point of
> intervention. One directive usable verbatim, under 40 words.
>
> **Validation criteria.** Distinguish measured interventions from proposed ones. Note any
> intervention that causes the opposite failure — an agent too timid to build what is genuinely
> needed. If the honest answer is that no instruction reliably fixes this and it needs a runtime
> mechanism, say so.
>
> **Stop when** the pre-action-check question has a verdict.

```yaml
prompt_failure_hints:
  - "Generic 'be concise' advice. The question is which intervention point measurably works."
prompt_learning_hints:
  - "If over-building is a completion-signal failure, the fix belongs with the target rule, not a separate gate."
  - "A finding that no instruction fixes it would be the strongest possible argument for a runtime mechanism."
```

---

## Packet 8 — How conditional depth signals actually work

```yaml
prompt_packet:
  id: RP-08-deepen-when-mechanics
  prompt_task_type: mechanism_explanation
  expected_output_type: mechanism_explanation_with_verdict
  provider_target: provider_unspecified
  prompt_design_rationale: >
    The operator asked directly how this works. Written as an explanation request first and an
    evaluation second, so the answer is usable without prior knowledge.
  usage_tracking_tags: [deepen-when, progressive-disclosure, mechanism]
  validation_status: valid
```

**Decides:** whether to keep `deepen_when`, worth **99 tokens** across six rules.

### Copy-paste prompt

> **Explain, then evaluate.** Assume no prior knowledge.
>
> An always-loaded instruction file for an AI coding agent carries rules in this shape:
>
> ```
> <authoring when="creating or editing a governed knowledge file"
>            ref="informatics/index.md"
>            deepen_when="you need the frontmatter contract, tier definitions or bundle layout">
> a short summary of the rules
> </authoring>
> ```
>
> Three signals: `when` says the rule applies; `ref` names a fuller file; `deepen_when` says the
> inline summary is insufficient and the file should be opened.
>
> **Part 1 — explain the mechanism in plain language.** There is no parser. The model reads these as
> text. So what actually happens when a model encounters `deepen_when`? Does it meaningfully change
> whether the model opens the file, or is it inert decoration? Explain how a model decides to use a
> tool to read a referenced file at all, and what in the surrounding text influences that.
>
> **Part 2 — evaluate.** Does a separate depth condition earn its tokens, given the file pointer is
> already present? Compare: all three signals; `when` + `ref` only; `when` + a single sentence inside
> the rule body saying when to read further; and `ref` alone.
>
> **Part 3 — failure modes.** What goes wrong? Opening the file every time regardless; never opening
> it; opening it for the wrong reason. Any measured rates.
>
> **Output contract.** A plain-language mechanism explanation a non-specialist can follow. A
> comparison table: variant, tokens, expected behaviour, evidence. A direct verdict: keep or drop,
> and why. If keeping, the most compact phrasing that preserves the effect.
>
> **Validation criteria.** Part 1 must be understandable without prompt-engineering background. Do
> not assume the attribute does something merely because it is named as if it does. Separate what is
> measured from what is plausible. If the honest answer is "no evidence either way, and it is
> probably weak," say that.
>
> **Stop when** Parts 1 and 2 are both answered.

```yaml
prompt_failure_hints:
  - "Jargon-heavy Part 1. The operator asked how it works because they do not know - explain plainly."
  - "Assuming the attribute works because of its name. It is text, not a parsed directive."
prompt_learning_hints:
  - "A verdict of 'inert' drops 99 tokens and applies to every attribute whose effect is assumed rather than measured."
  - "This generalises: any attribute in the contract may be decorative. deepen_when is the test case."
```

---

---

## Packet 9 — Every remaining token-efficiency lever

```yaml
prompt_packet:
  id: RP-09-efficiency-audit
  prompt_task_type: comprehensive_optimization_audit
  expected_output_type: ranked_lever_inventory
  provider_target: provider_unspecified
  prompt_design_rationale: >
    The other packets each test one lever. This one asks what the author has not thought of, because
    the local compression attempt recovered only 3% and the author may be out of ideas rather than
    out of slack.
  usage_tracking_tags: [token-efficiency, audit, levers]
  validation_status: valid
```

**Decides:** whether ~1,476 is genuinely the floor, or whether levers exist that were never
considered. **This is the packet that covers everything the other eight do not.**

### Copy-paste prompt

> An always-loaded instruction block for an AI coding agent measures **1,622 tokens** across about
> twenty rules. It is paid on every session regardless of task. The author wants it near 1,000 and
> has concluded that is impossible without deleting rules. **Challenge that conclusion. Find every
> lever they have not considered.**
>
> **What they have already tried or measured:**
>
> | Lever | Result |
> |---|---|
> | Aggressive rewording of the six largest rules | **−47 tokens (3%)** — wording appears to be at its floor |
> | Swapping XML tags for bullets on unconditional rules | −39 tokens (2.4%) |
> | Wholesale reformat to a markdown table | ~−190 tokens (12%), untested for comprehension cost |
> | Dropping the secondary depth condition from nine rules | −99 tokens |
> | Moving content into separately-gated files | Works, but only for content that is genuinely conditional |
>
> **Composition:** rule bodies 73%, condition and pointer attributes 20%, tag names 7%.
>
> **Find what is missing from that list.** Consider at least:
> 1. **Prompt caching** — if the block is cached across requests, does its token count still cost
>    what the author assumes? Does this change the entire premise of optimizing it?
> 2. **Rule merging** — can rules with adjacent meaning be combined without losing behaviour? Is
>    there evidence on whether fewer longer rules outperform more shorter ones, or the reverse?
> 3. **Relocation** — can instruction content live in tool descriptions, function schemas, or other
>    surfaces that are loaded anyway, instead of in the instruction block?
> 4. **Compression techniques** — telegraphic register, dropping articles, symbols for common words,
>    abbreviation schemes. Do these actually save tokens after tokenization, and do they cost
>    comprehension? Be specific: many "compression" tricks tokenize worse than plain English.
> 5. **Model-side features** — anything in current agent runtimes that handles this automatically
>    and makes manual optimization obsolete.
> 6. **Elimination by default** — are any of these rules things a current model already does
>    reliably without being told? A rule that restates default behaviour is pure cost.
> 7. **Anything else in production practice.**
>
> ### Search creatively — the list above is a floor, not a ceiling
>
> **There is no limit on where you look.** The seven items above are what one author happened to
> think of. Go wider. Any field that has solved "maximum meaning per character under a hard budget"
> is fair game, and most of them are not AI fields at all. Consider, and go beyond:
>
> - **Controlled natural languages** — Simplified Technical English, ASD-STE100, AECMA, and the
>   aviation and defence documentation standards behind them.
> - **Constrained-channel writing** — telegraphic style, telex and cablese, newspaper headline
>   grammar, radio and aviation phraseology, military message formats.
> - **Legal and regulatory drafting** — defined-term tables, incorporation by reference, numbered
>   clause schemes that avoid restating conditions.
> - **Information theory and compression** — what a shared vocabulary or dictionary buys, and
>   whether any of it survives tokenization.
> - **Code and config minification** — what transfers to natural language and what does not.
> - **Instructional design and checklist discipline** — aviation and surgical checklists are
>   extremely compressed instruction sets with measured compliance outcomes.
> - **Tokenizer-level tactics** — word choices that happen to tokenize cheaply, punctuation and
>   casing effects, whether common words cost less than synonyms.
> - **Anything else at all.** If you find a technique in a field nobody would expect, that is the
>   most valuable kind of finding here.
>
> ### But evidence gates adoption
>
> Creativity applies to **where you search**. It does not apply to what you claim. Classify every
> technique you surface into exactly one tier, and label it in the output:
>
> | Tier | Meaning | Usable? |
> |---|---|---|
> | **Proven** | A real standard, a published measurement, or documented production use with results | Recommend |
> | **Plausible** | Used somewhere real, but no measurement for this use case | Propose as a local test, never as a recommendation |
> | **Speculative** | Your own idea, or an untested extrapolation | List separately, clearly marked, never mixed in with the above |
>
> **Do not invent a technique and present it as established.** An idea of your own is welcome in the
> Speculative tier and worthless anywhere else. Equally, do not discard a genuinely proven technique
> because it comes from an unglamorous field — a 1950s telex convention with a measured track record
> outranks a 2026 blog post.
>
> **Then answer the central question directly: is ~1,000 tokens achievable for a twenty-rule
> always-on instruction block without deleting rules — and if not, what is the realistic floor?**
>
> **Output contract.** A ranked table: lever, **tier** (Proven / Plausible / Speculative), estimated
> saving, cost or risk, evidence link. A section titled "Not on the author's list" for anything
> genuinely new, with its source field named. A separate clearly-marked Speculative section. A direct
> verdict on the 1,000-token question with a realistic floor figure. A direct verdict on whether
> caching changes the premise.
>
> **Validation criteria.** Estimate savings in tokens, not vaguely. Flag any lever that trades
> tokens for correctness and say which way the trade goes. Every Proven-tier claim carries a source.
> **Point 6 matters most and is the easiest to skip** — identify specific rules in the categories
> listed that a current model likely follows by default. If the honest answer is that 1,622 is close
> to the floor and the author should accept it, say so plainly; that is a useful finding, not a
> failure.
>
> **Stop when** the 1,000-token question has a direct answer with a floor figure, and you have
> searched at least three fields outside AI and prompt engineering.

```yaml
prompt_failure_hints:
  - "Repeating levers already in the author's table. The value is in what is missing."
  - "Recommending compression tricks without checking how they tokenize - many make things worse."
  - "Skipping the caching question, which could invalidate the whole optimization premise."
prompt_learning_hints:
  - "If caching makes always-on token cost largely irrelevant, most of this work was optimizing the wrong variable."
  - "Rules that restate default model behaviour are the cheapest possible deletion - they cost tokens and buy nothing."
  - "A floor figure materially above 1,000 closes the question and lets the operator stop pushing on it."
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
