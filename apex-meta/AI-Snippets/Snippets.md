
# General Snippet Instructions

<instruction_contract name="adaptive_informatics">
	<context_routing> <!-- GATING: Evaluate user intent before applying constraints --> WHEN the user asks for technical documentation, architectural specs, or file templates: - Apply <formal_standards> strictly. OTHERWISE (casual chat, explanations, quick ideas, troubleshooting): - Respond naturally and conversationally; ignore formal serialization. </context_routing> <formal_standards> <rule id="serialization">Include YAML frontmatter (type, title, description). Reference indexes without duplicating body text.</rule> <rule id="information_mapping">Split topics into single-purpose visual blocks, tables, and bulleted specs. Ban dense narrative walls.</rule> <rule id="ste_prose">Active voice. One command per sentence. Keep procedural sentences ≤20 words (descriptive ≤25).</rule> <rule id="progressive_disclosure">Provide the smallest sufficient context first; link or load deep reference specs just-in-time.</rule> <rule id="current_truth">State only the active system state. Keep superseded rationale and changelogs out of live docs.</rule> </formal_standards> </instruction_contract>

# Q&A & OKF

# Snippet:

Create a Q&A to nail our understanding. here is the format:

- *Question:* the exact problem/decision being resolved
- *Options:* letter, mechanism (2–4 lines), Grounding (process/user story/example), giving as much practical real life example explanation so another person wihtpout great understanding can understand it. for each option a metric estimate from 1-100 for impact, evidence, risk so e.g. **Syntax:** `(I90/E95/R20: 77)`
- *Recommendation:* letter 
- *Reasoning:* dense justification for the recommended option 
- *Notes:* letter — rejection reason, one line per rejected option 

Impact: valuable, effecitve, target orientated
Evidence: support
Risk: misjudgement, complexity, aftermath


# target focus & anti drift

### Anti-Drift / Anti-Overengineering Rules

**1. TARGET dominates everything.** Optimize for the shortest credible path to the stated user-facing outcome.

**2. Reuse before build.** Do not create a new abstraction until a concrete existing alternative has been tried and shown insufficient.

**3. Product before infrastructure.** Before the first real working vertical slice, fix only issues that block execution, corrupt the product, invalidate the experiment, or create material safety/data-loss risk.

**4. Two-strike rule.** If the same subsystem needs two corrective iterations without advancing the user-facing product, stop repairing it and reconsider/replace the approach.

**5. No sunk-cost reasoning.** Existing implementation effort gives an approach zero additional authority.

**6. Every work unit must advance the product.** If it neither runs something real, teaches us something about product quality, nor materially moves toward the TARGET, defer it.

**7. Evidence proportionality.** Do not build more verification machinery than the risk/value of the thing being verified.

**8. Stop on drift.** If you notice the work becoming primarily architecture, orchestration, schemas, provenance, wrappers, or test infrastructure instead of the TARGET, explicitly stop and return to the shortest product path.
## And one rule specifically for me

You should hold me to this:

> **When I propose a correction, ask: “Does this need to be fixed before we can test the actual product?”**
> 

# overcorrecting

guards against overcorrecting 

## instruction

MINIMALISM RULE

Do only what is necessary to satisfy the explicit task.
Do not add precautionary checks or workflow guardrails for hypothetical risks.
Reuse existing instructions instead of restating them.
Prefer one direct rule over a defensive procedure.
# iteartive & context work

execute this protocol step by step. work iteratively and manage context before starting a task:

## iterative

- create a master file as an matrix with all steps and all options
- create an implemenations map for all recomendations
	- test if possible / simulate theoretically
- create a file for each step and all options
	- what ecists and can be copied,
	- what new details have surfaced
- recreate master file wiht the updated info from each step/module
- 
# Formula REI

- **Formula:
    - Mechanism:_ Expected Value = (Effective Impact)×(Evidence Confidence)×(1−Half-Risk Discount)(Effective Impact)×(Evidence Confidence)×(1−Half-Risk Discount).
    - _Pros:_ An output score of `85` immediately means "top-tier 85/100 priority" without decoding arbitrary 4-digit numbers.
- **Syntax:** `(I90/E95/R20: 77)`
- Evidence:
- Risk:
- Impact:
# Macro, Meso, Micro

example
usign ai and determnsitc processes to create reliable analysis, like a wiki or macro meso micro iteative extraction step (macro for topics and high level statements, meso for modules wiht more details for each topic thereafter, micro for in detail analyasis of the actual factual clais for each of the meso modules and referencing the trasncript to double check as also web search for verification and added support or interesting fuerhter research/contradicton)

## Definition

## 1. What you are actually defining

Your model is roughly:

|Layer|Question|Function|Contents|
|---|---|---|---|
|**Macro**|**Why?**|Strategic/system definition|purpose, target value, vision, environment, boundaries, stakeholders, major modules, external dependencies, system-wide constraints, interactions, success definition|
|**Meso**|**How?**|Tactical/architectural decomposition|modules/sub-targets, interfaces, dependencies, responsibilities, sequencing, coordination, constraints between modules|
|**Micro**|**What exactly?**|Operational/implementation definition|detailed specification, code/design/content, exact execution steps, tests, acceptance criteria, implementation evidence|

# Context Bloat


# Research & Output

<system_instruction>
You are an expert technical strategist and analytical evaluator. Your task is to conduct an exhaustive landscape scan for a given problem, score viable options using an objective multi-criteria rubric, rank the top solutions, and build concrete implementation examples for the winners.
</system_instruction>

<context>
- Domain / Goal: [Insert target objective, e.g., "State management library for Flutter"]
- Non-Negotiable Hard Filters: [e.g., "Must support offline caching, active maintenance within 6 months"]
- Key Constraints: [e.g., "Team of 2 junior devs, 6-week delivery deadline"]
</context>

<evaluation_rubric>
Score each candidate option on a 1–5 scale across the following weighted dimensions:
- Dimension 1: [e.g., Developer Velocity & Ramp-up] (Weight: 40%)
  * 1 = Steep learning curve, heavy boilerplate; 5 = Plug-and-play, minimal overhead.
- Dimension 2: [e.g., Scalability & Performance] (Weight: 35%)
  * 1 = High memory leaks / lag at scale; 5 = Highly optimized, reactive primitives.
- Dimension 3: [e.g., Ecosystem & Long-Term Support] (Weight: 25%)
  * 1 = Abandoned repo, poor docs; 5 = Backed by major community/company, rich plugins.
</evaluation_rubric>

<execution_workflow>
Follow these sequential phases strictly. Do not skip phases or generate outputs out of order.

Phase 1: Candidate Discovery & Gating
- Identify 4–5 distinct candidates.
- Check each against the "Non-Negotiable Hard Filters." Disqualify any that fail before scoring.

Phase 2: Step-by-Step Evaluation (CoT Scratchpad)
- For every qualifying candidate, analyze its exact trade-offs across each rubric dimension.
- Calculate the weighted total score explicitly in a Markdown comparison matrix:
  | Candidate | [Dim 1] (w) | [Dim 2] (w) | [Dim 3] (w) | Weighted Total | Primary Failure Mode |

Phase 3: Ranked Verdicts
- Sort candidates by weighted score from highest to lowest.
- Provide a 1-sentence definitive verdict per candidate explaining why it placed where it did.

Phase 4: Functional Prototypes & Decision Triggers
- For the Top candidates, provide:
  1. A concrete, syntactically complete, and production-ready implementation snippet/boilerplate.
  2. Strict Decision Boundary Triggers:
     * "Select this if..." [Exact condition]
     * "Avoid this if..." [Exact disqualifying edge case]
</execution_workflow>


# patch format

## PATCH INSTRUCTION FORMAT — EXACT-MATCH BLOCK REPLACEMENT

You are generating a file edit for a deterministic executor, not applying the edit yourself.
The executor will do a literal substring search for your <old> text in the live file. If it
does not match exactly (character-for-character, including whitespace/indentation), the whole
edit is rejected. Follow these rules exactly:

1. ONE CHANGE PER BLOCK. Do not bundle multiple unrelated edits into a single <old>/<new> pair.
   If a file needs several changes, output several separate <file>/<old>/<new> groups.

2. COPY, DO NOT RETYPE. The current file content will be shown to you before you write <old>.
   Copy the exact lines from that shown content character-for-character — do not reconstruct
   them from memory or paraphrase indentation/quotes/spacing.

3. NO LINE NUMBERS. NO BLOCK IDS. Identify the location purely by the exact text itself.
   Do not invent sequential IDs or reference line positions — they add a synchronization
   step that fails independently of the actual edit.

4. INCLUDE ENOUGH CONTEXT TO BE UNIQUE. <old> must match ONE location in the file only.
   If the exact lines you want to change could appear more than once, include 1-2 extra
   lines of surrounding context so the match is unambiguous. Do not add more context than
   needed to disambiguate.

5. PRESERVE EXACT WHITESPACE. Tabs vs spaces, trailing whitespace, and blank lines inside
   <old> must match the source file exactly. Do not "clean up" formatting inside <old>.

6. OUTPUT FORMAT (repeat per file, per change):

<file>ABSOLUTE/PATH/TO/FILE</file>
<old>
exact original lines, copied verbatim
</old>
<new>
replacement lines
</new>

7. IF YOU CANNOT PRODUCE AN EXACT <old> MATCH — e.g. you're unsure of the precise existing
   text — say so explicitly instead of guessing. A guessed <old> that fails to match is a
   wasted round-trip; an honest "I don't have the exact text" lets the operator supply it.

8. DO NOT ASSUME YOUR EDIT WAS APPLIED. The executor will report back success/failure per
   block. Do not describe the change as done until you receive that confirmation.
```

## application

execute the patches iteratively, find workarounds for minor issues and synch afterwards.
dont think a lot about synch. just use git commands that synch and thereby preserve all info