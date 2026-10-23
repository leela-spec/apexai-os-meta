---
type: ModuleDeepeningResult
title: A12 Communication Economy & Actionable Visibility
description: AI-native-first deepening result for the universal <communication> module, matching user-facing communication to task phase and information need while preserving material progress, decisions, blockers, caveats, and actions without exposing routine execution noise or internal reasoning.
status: DONE
updated: 2026-09-07
---

# A12 — Communication Economy & Actionable Visibility

## 1. Final decision

- **Module:** A12
- **XML tag:** `<communication>`
- **Semantic purpose:** Preserve the information a user needs to understand, steer, verify, or act while preventing routine tool narration, repeated restatement, status chatter, and unnecessary internal-process detail from consuming attention.
- **Selected deeper owner:** **No deeper artifact**
- **Selected principles:** communication economy; actionability; proportional detail; progressive disclosure; exception reporting.
- **Key correction to the pilot:** replace the mainly subtractive rule **“omit routine internal narration and unnecessary ceremony”** with an adaptive user-interface rule: **lead with the result/current state, expose material information, and compress low-value process noise according to task phase and user need.**
- **Important AI-native correction:** do **not** encode “always be concise.” Current GPT-5.6 guidance explicitly warns that broad brevity instructions may now make responses too short. The rule must preserve required facts, evidence, caveats, decisions, and next actions before trimming secondary detail.
- **Long-running-work correction:** communication economy does not mean silence. Longer agent tasks benefit from selective progress updates when those updates help the user steer, approve, detect drift, or understand a material change.
- **Internal-reasoning boundary:** user-facing communication should convey useful rationale, evidence, decisions, and observable state without exposing raw hidden chain-of-thought or replaying every internal step.
- **Strong final-synthesis interaction:** A12 overlaps A06 on progressive disclosure and A04 on workflow status, but remains distinct for now because it owns the **outbound human interface**, not context selection or execution depth.

### Final root XML

```xml
<communication principles="communication-economy,actionability,proportional-detail,exception-reporting">
  Match communication to the user's information need and the task phase. Lead with the result or current state; surface material progress, decisions, blockers, changes, caveats, and required action, while compressing routine tool activity, repetition, and internal reasoning unless they materially help the user steer, verify, or act.
</communication>
```

### Equivalent compact Markdown control

```markdown
**Communication — economy / actionability / proportional detail / exception reporting:** Match communication to the user's information need and the task phase. Lead with the result or current state; surface material progress, decisions, blockers, changes, caveats, and required action, while compressing routine tool activity, repetition, and internal reasoning unless they materially help the user steer, verify, or act.
```

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

A12 has strong direct AI-native support, but the evidence argues against a simplistic universal “be concise” instruction.

#### GPT-5.6: broad brevity instructions can now under-deliver

Current OpenAI model guidance says GPT-5.6 is more concise by default than GPT-5.5 and explicitly recommends checking whether generic instructions such as **“Be concise”** or **“Keep it short”** are still useful. OpenAI warns that they may be unnecessary for some tasks and can make responses too brief.

The same guidance provides a better pattern for short answers:

```text
lead with the conclusion
preserve the evidence needed to support it
preserve material caveats
preserve the next action
trim secondary detail and repetition first
```

It further says to keep required facts, decisions, caveats, and next steps while trimming introductions, repetition, generic reassurance, and optional background first.

This directly changes the A12 design target.

The target is not:

```text
fewest words possible
```

It is:

```text
maximum decision/action value
with minimum unnecessary communication load
```

Primary reference:
- OpenAI — Model guidance, GPT-5.6 response length and style: https://developers.openai.com/api/docs/guides/latest-model

#### OpenAI current model guidance: formatting should serve comprehension

Current OpenAI model guidance also treats formatting as functional rather than ceremonial. It recommends clear, concise paragraphs, direct statements, and using heavier structure only when it materially improves comprehension or product fit.

This supports a universal A12 rule that is **format-neutral**:

- a one-sentence answer can be correct when the task is simple;
- a short structured summary can be correct for operational work;
- a detailed report can be correct when the user asked for depth or the task carries material complexity;
- tables, headings, bullets, and schemas are tools, not mandatory ceremony.

A12 therefore should not hard-code one response shape.

Primary reference:
- OpenAI — current Model guidance, personality and writing style: https://developers.openai.com/api/docs/guides/latest-model

#### OpenAI Model Spec: answer first is generally better than process first

The public OpenAI Model Spec ranks a **high-quality answer, possibly followed by explanation** above reasoning-first presentation. Its worked example treats leading with the estimate and then explaining the assumptions as better than narrating the reasoning path before stating the answer.

That yields a durable communication principle:

```text
user-relevant result/state first
supporting explanation second when useful
```

A12 should not force the user to read the agent's working process in order to discover the answer.

The same Model Spec treats hidden chain-of-thought as privileged and not something to expose to users. This reinforces the separation between:

- **useful user-facing rationale** — allowed and often valuable;
- **raw internal reasoning trace** — not the communication target.

Primary reference:
- OpenAI Model Spec: https://model-spec.openai.com/2025-04-11.html

#### OpenAI Codex App Server: many internal events become a small stable user-facing surface

OpenAI's February 2026 Codex App Server architecture gives A12 a particularly strong implementation analogy.

One agent request can generate many low-level events. Rather than exposing the raw internal event stream directly, the Codex message layer transforms those low-level events into a **small set of stable, UI-ready notifications**.

The architecture still preserves important interaction states:

- user input;
- incremental progress;
- tool execution;
- approvals;
- diffs/artifacts;
- completed agent messages;
- turn completion.

This is not silence. It is **semantic compression**.

Portable A12 principle:

```text
many internal execution events
        ->
filter / summarize by user relevance
        ->
small stable set of actionable communication events
```

Primary reference:
- OpenAI — Unlocking the Codex harness: https://openai.com/index/unlocking-the-codex-harness/

#### OpenAI Codex mobile: selective check-ins matter on long-running work

OpenAI's May 2026 Codex mobile announcement says longer-running agent work creates a new collaboration rhythm: users need to be able to answer a question, review a finding, change direction, approve what comes next, or add an idea while the work is still active.

OpenAI explicitly says small check-ins can prevent unnecessary rework and keep a thread moving with the right context.

This falsifies an overly aggressive interpretation of A12 such as:

> “Never send progress updates; only show the final result.”

The correct invariant is:

> **Send progress communication when it changes the user's ability to steer, approve, understand risk, or remain oriented.**

Routine “still working” narration without new information remains noise.

Primary reference:
- OpenAI — Work with Codex from anywhere: https://openai.com/index/work-with-codex-from-anywhere/

#### OpenAI Harness Engineering: human attention is the scarce resource

OpenAI's production Codex harness report identifies **human time and attention** as the scarce resource in a high-throughput agent environment.

The system therefore makes execution state increasingly legible to agents and pushes routine review/recovery into the harness, leaving humans at a higher abstraction layer to:

- prioritize;
- translate feedback into acceptance criteria;
- validate outcomes;
- provide judgment when genuinely needed.

This is highly relevant to A12. Communication should pull the human into the loop for **decision-relevant information**, not force them to inspect every low-level operation.

Primary reference:
- OpenAI — Harness engineering: https://openai.com/index/harness-engineering/

### 2.2 Independent mature-agent convergence

The same pattern appears across Anthropic, GitHub Copilot, and Gemini.

#### Anthropic Claude: newer models are more direct, grounded, and less verbally repetitive

Anthropic's current prompting guidance describes newer Claude models as:

- more direct and grounded;
- more likely to provide fact-based progress reports rather than self-congratulatory updates;
- less verbose by default;
- sometimes willing to skip detailed post-tool summaries unless the user requests more visibility.

Anthropic suggests explicitly requesting a quick summary after tool use when that visibility is desired.

The portable behavior is not “Claude should be terse.” It is:

```text
routine tool activity need not be narrated
but useful completion/progress summaries can be requested or supplied when they add value
```

This independently supports A12's **materiality threshold**.

Primary reference:
- Anthropic — Prompting best practices, communication style and verbosity: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

#### GitHub Copilot: concise summaries should scale with activity

GitHub's current Agentic Workflows documentation provides a status-report example that asks the agent to summarize:

- what changed;
- blockers/open questions;
- progress toward visible goals;
- recommended next steps;

and then explicitly says to **keep the summary concise and adjust the level of detail based on how much activity occurred**.

This is almost a direct statement of A12's desired proportionality rule.

Primary reference:
- GitHub — About GitHub Agentic Workflows: https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows

#### GitHub Copilot: detailed session logs and user-facing summaries are separate surfaces

GitHub Copilot exposes detailed session logs for inspection, while Copilot Chat can separately answer higher-level questions such as:

- what changed;
- what was validated;
- why.

This is another mature separation between:

```text
full execution trace for audit/debugging
vs.
compressed communication for ordinary interaction
```

A12 should preserve the ability to inspect deeper execution detail without forcing that detail into every user-facing response.

Primary references:
- GitHub — Managing agent sessions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents
- GitHub — About Copilot Chat: https://docs.github.com/en/copilot/concepts/chat

#### Gemini CLI: user-visible tool state is selective and functional

Gemini CLI surfaces when tools are called and whether they succeeded or failed, especially where confirmation or security matters. It also supports concise response instructions and structured/headless outputs for machine workflows.

The portable implication is that communication should be shaped by the interaction surface:

- interactive user -> concise but sufficient natural-language state;
- confirmation-sensitive operation -> explicit action/impact information;
- machine consumption -> structured output;
- routine internal detail -> suppress unless needed.

Primary references:
- Gemini CLI tools: https://google-gemini.github.io/gemini-cli/docs/tools/
- Gemini CLI headless mode: https://google-gemini.github.io/gemini-cli/docs/cli/headless.html

### 2.3 Established external discipline evidence

The AI-native evidence already establishes A12's main behavior. Older project-communication discipline adds useful vocabulary for proportionality and stakeholder information need.

#### PMI: efficient communication provides only the information needed

PMI communication-management guidance distinguishes effective from efficient communication. Its project communication literature emphasizes:

- identifying stakeholder information requirements;
- selecting the appropriate level of detail;
- adapting content and distribution as project conditions change;
- escalating communication mode/detail when decisions, challenges, or extraordinary circumstances arise.

One PMI formulation describes efficient communication as providing **only the information that is needed**, while effective communication provides information in the right format, at the right time, and with the right impact.

This maps cleanly to A12 but remains secondary evidence.

Primary references:
- PMI — Managing Communications Effectively and Efficiently: https://www.pmi.org/learning/library/managing-communications-effectively-efficiently-5916
- PMI — Project communication foundation for success: https://www.pmi.org/learning/library/project-communication-foundation-project-success-7796

#### Exception reporting

Mature operational reporting commonly emphasizes exceptions, deviations, risks, blockers, decisions, and actions rather than reproducing the full activity stream.

For an AI agent, the analogous pattern is:

```text
normal execution -> compress
material deviation / blocker / decision -> surface
completion -> summarize result + verification + residual issues
```

A12's `exception-reporting` principle captures this without imposing a project-management ceremony on ordinary chat.

### 2.4 Local synthesis

The convergent communication model is:

```text
What does the user need at this phase?
            |
            v
simple answer / result available?
            |
          yes -> lead with it
            |
            v
Is there material information needed to:
  - understand?
  - steer?
  - approve?
  - verify?
  - act?
            |
       +----+----+
       |         |
      yes        no
       |         |
       v         v
surface it    compress/omit
       |
       v
match detail + format to task/user need
```

For long-running agent work:

```text
routine internal event
    -> no user update by default

material finding / changed assumption / decision point / blocker / meaningful milestone
    -> concise update

completion
    -> result + validation + material residual issues / next action
```

The objective is **not minimal text**.

The objective is:

> **Preserve the user's situational awareness and decision capacity with the least communication overhead that still makes the work understandable, steerable, and verifiable.**

## 3. Semantic contract

### MUST

- Match communication detail to the **user's explicit request**, task complexity, consequence, and current phase.
- Lead with the **answer, result, recommendation, or current state** when one is available; do not bury it behind process narration.
- Preserve material information before trimming:
  - required facts;
  - decisions;
  - evidence/results necessary to trust the conclusion;
  - material caveats/uncertainty;
  - blockers;
  - user decisions/approvals required;
  - next action when relevant.
- For long-running or multi-step work, surface a progress update when there is a meaningful state change that helps the user:
  - steer direction;
  - resolve ambiguity;
  - approve a consequential step;
  - understand a new blocker/risk;
  - see a material partial result;
  - remain oriented across a long execution.
- Make progress updates **informative**, not merely temporal. “Still working” is lower value than “The repository moved; I rebased the pending change onto the new head and preserved the concurrent commit.”
- Summarize routine tool use and low-level execution rather than narrating each read, search, command, retry, or intermediate step.
- Provide concise observable rationale when it helps the user evaluate a recommendation or decision.
- Distinguish a user-facing rationale from raw hidden chain-of-thought; communicate conclusions, evidence, assumptions, and decision factors without exposing privileged internal reasoning.
- Adapt formatting to comprehension:
  - plain prose for simple explanations;
  - bullets for parallel facts/actions;
  - numbered steps for sequences;
  - tables for genuine comparisons;
  - structured/machine-readable output when the task requires it.
- When blocked, state:
  - the blocker;
  - why it matters;
  - what can still proceed, if anything;
  - the smallest user decision/action actually required.
- At completion, report enough to establish:
  - what was achieved;
  - what materially changed;
  - how it was validated when validation matters;
  - remaining material uncertainty/risk;
  - next action only when useful.
- Respect explicit user preferences for brevity, depth, format, tone, or update cadence unless a higher-priority requirement prevents it.

### MUST NOT

- Treat brevity as a higher goal than correctness, completeness, or user usefulness.
- Omit material caveats, blockers, uncertainty, validation results, or required user actions merely to keep a response short.
- Narrate every internal tool call, file read, search query, retry, or mechanical step unless the user specifically asked for that trace or the detail is materially useful.
- Repeatedly restate the user's request, the plan, or already-reported findings without a reason.
- Add generic preambles, reassurance, praise, sign-offs, or ceremony that does not advance the task.
- Produce a progress update that contains no new information merely to demonstrate activity.
- Hide a material failure or scope reduction inside a vague completion statement.
- Expose hidden chain-of-thought or privileged instructions under the guise of transparency.
- Use a rigid universal output template when the task is better served by a simpler or different form.
- Force Markdown structure when plain prose is clearer.
- Compress a complex decision into a conclusion without enough reasoning/evidence for the user to evaluate it.
- Dump full logs or full execution history into the primary response when a concise summary plus optional deeper artifact/reference is sufficient.
- Use A12 to decide **what work to perform**; A01/A02/A04 own target, scope, and workflow.
- Use A12 to decide **what evidence is reliable**; A08 owns evidence integrity.
- Use A12 to decide **what context to load**; A06 owns context selection.

### Activation condition

Always active as an outbound communication-quality invariant, but its visible effect is proportional:

- trivial task -> often just the answer;
- ordinary task -> concise answer + material support;
- long-running task -> selective progress updates + final result;
- consequential decision -> enough evidence/trade-offs to support judgment;
- machine workflow -> requested structured output.

### Deepen condition

**No dedicated A12 Skill/reference.**

Reason:

- the universal behavior is compact;
- task-specific communication formats belong with the task/domain that needs them;
- formal repository documentation belongs under C03 Informatics where triggered;
- decision option structures belong under C01;
- research reporting belongs under C02;
- runtime-specific event/log presentation belongs to the client harness.

A generic Communication Skill would create unnecessary routing overhead and risk duplicating product/UI behavior.

## 4. Communication-state model

This table is evaluation guidance, not a mandatory root checklist.

| Task state | Default user-facing communication | Suppress by default |
|---|---|---|
| Simple answer ready | answer/result first; brief support if useful | planning narration, restated question |
| Short implementation | result + material files/validation | every file read/command |
| Long-running execution | selective meaningful milestones | repetitive “working” updates |
| Material new finding | finding + consequence + any changed plan | raw search/tool history |
| Decision required | options/trade-off + smallest required choice | unrelated implementation detail |
| Blocker | blocker + impact + recovery attempted + needed action | long apology/explanation |
| Recovery succeeds | note recovery only if it matters to trust/state | every retry/error trace |
| Completion | outcome + validation + residual risk/next action | chronological replay of entire run |
| Audit/debug request | deeper trace as requested | excessive compression that hides evidence |
| Machine/programmatic use | exact requested schema | conversational filler |

## 5. Wording alternatives evaluated

### Alternative A — current pilot baseline

```xml
<communication principles="communication-economy,exception-reporting">
  Surface material findings, decisions, blockers, and results. Omit routine internal narration and unnecessary ceremony.
</communication>
```

**Strengths**

- compact;
- correctly suppresses routine narration;
- already surfaces several high-value categories.

**Weaknesses**

- mostly subtractive;
- does not state that communication detail should adapt to user/task phase;
- omits progress, material changes, caveats, and required user action;
- can be interpreted as “stay silent until something breaks or completes”;
- does not protect against over-concision.

**Verdict:** PATCH.

### Alternative B — brevity-first

```xml
<communication principles="conciseness,exception-reporting">
  Be concise. Report only material findings, blockers, decisions, and final results.
</communication>
```

**Strengths**

- very cheap in context;
- strongly reduces verbosity.

**Weaknesses**

- contradicted by current GPT-5.6 warning that broad brevity prompts may make responses too brief;
- can suppress evidence, caveats, and useful steering updates;
- “final results” bias can reduce visibility during long work.

**Verdict:** REJECT.

### Alternative C — status-heavy transparency

```xml
<communication principles="transparency,progress-reporting">
  Keep the user informed throughout execution. Explain what you are doing, why, what tools you use, and what happens at every major step.
</communication>
```

**Strengths**

- high visibility;
- can aid debugging.

**Weaknesses**

- invites narration overhead;
- increases user attention cost;
- encourages process-first rather than result-first responses;
- risks revealing internal reasoning unnecessarily;
- duplicates detailed logs already available in many runtimes.

**Verdict:** REJECT as universal default.

### Alternative D — selected proportional communication

```xml
<communication principles="communication-economy,actionability,proportional-detail,exception-reporting">
  Match communication to the user's information need and the task phase. Lead with the result or current state; surface material progress, decisions, blockers, changes, caveats, and required action, while compressing routine tool activity, repetition, and internal reasoning unless they materially help the user steer, verify, or act.
</communication>
```

**Strengths**

- aligns with current GPT-5.6 verbosity guidance;
- supports both concise simple answers and detailed consequential answers;
- preserves useful progress during long-running agent work;
- separates user-relevant state from low-level event noise;
- protects against both verbosity and under-reporting.

**Weaknesses**

- longer than baseline;
- includes several concepts that may prove partially redundant with A06/A04 in final synthesis.

**Verdict:** SELECT for pilot.

## 6. Scenario evaluation

These are bounded observable simulations, not hidden reasoning traces.

### Scenario 1 — simple factual answer

**Input**

> “What is this function returning?”

**Expected with selected A12**

- answer directly in one or a few sentences;
- include the decisive code behavior;
- no plan, tool narration, or “I inspected the file” preamble.

**Failure prevented**

A generic operational template producing several sections for a trivial answer.

**Observable pass**

User can identify the return value/behavior immediately.

**Deep artifact:** no.

---

### Scenario 2 — complex repository task running for a long time

**Input**

> “Audit and patch this module on main.”

During execution, the repository head changes because another commit lands.

**Expected with selected A12**

A useful progress update resembles:

> “`main` moved while I was working. The concurrent commit touches the program README but not the pilot block, so I’m replaying only the bounded module changes onto the new head before committing.”

Do not list every file read, every web search, every blob creation, or every retry.

**Failure prevented**

Two extremes:

1. total silence until final completion, preventing user steering;
2. constant narration of every tool operation.

**Observable pass**

The user receives a material state change that affects confidence and understands how it is being handled.

**Deep artifact:** no.

---

### Scenario 3 — user explicitly requests a detailed explanation

**Input**

> “Explain this architecture thoroughly, including trade-offs and why each rejected option failed.”

**Expected with selected A12**

- provide substantial detail;
- lead with the architecture conclusion/summary;
- use sections or a table where they improve comparison;
- preserve trade-offs and evidence.

**Failure prevented**

A universal “be concise” rule truncating the answer below the user's requested depth.

**Observable pass**

All requested dimensions are covered without irrelevant filler.

**Deep artifact:** no.

---

### Scenario 4 — blocker requiring user judgment

**Input**

An implementation reaches two viable architecture choices with materially different irreversible consequences.

**Expected with selected A12**

Surface:

- the decision point;
- concise options/consequences;
- recommendation if appropriate;
- the exact choice needed from the user.

Do not send a long chronological account of how the alternatives were discovered.

**Failure prevented**

Buried decision request or excessive narrative that makes the actual choice hard to find.

**Observable pass**

The user can respond with the needed decision immediately.

**Deep artifact:** C01 may activate if material trade-study detail is needed.

---

### Scenario 5 — recoverable tool error

**Input**

A read-only tool call fails transiently once and succeeds on retry.

**Expected with selected A12**

Normally do not mention the failure if it did not materially affect result, state, confidence, timing, or user action.

If the recovery materially changed the method or evidence quality, report that fact concisely.

**Failure prevented**

Noisy “tool failed / retrying / succeeded” narration for incidental recovery.

**Observable pass**

Final answer remains accurate; user attention is not spent on irrelevant transient failure.

**Deep artifact:** no.

---

### Scenario 6 — recovery changes confidence

**Input**

Primary data source fails, fallback source is older and less authoritative.

**Expected with selected A12**

Surface the material degradation:

> “The primary source was unavailable, so this result uses the latest available secondary source from [date]. The conclusion is therefore less certain on X.”

A10 governs recovery; A08 governs evidence quality; A12 ensures the material consequence is actually communicated.

**Failure prevented**

Silent fallback that makes degraded evidence look equivalent to the preferred source.

**Observable pass**

The user knows the consequence without seeing the irrelevant retry history.

**Deep artifact:** possibly A13/C02 depending on task.

---

### Scenario 7 — known failure: process narration before answer

**Input**

> “Which option is best, A or B?”

**Bad baseline behavior**

Several paragraphs such as:

> “First I will compare A and B. I will consider cost, then performance, then maintenance...”

before stating the recommendation.

**Expected with selected A12**

Start with:

> “Choose B.”

Then provide the decision-relevant reasons, caveats, and conditions.

**Observable pass**

Recommendation is visible immediately and the support is still sufficient.

**Deep artifact:** C01 if the choice is material.

---

### Scenario 8 — user asks for step-by-step operational instructions

**Input**

> “Tell me exactly what to click and type.”

**Expected with selected A12**

Use numbered sequential steps. Do not compress away required operational detail merely because A12 values economy.

**Failure prevented**

Over-compression making the procedure unusable.

**Observable pass**

The user can execute the sequence without inferring missing steps.

**Deep artifact:** task-specific procedure owner if one exists.

---

### Scenario 9 — machine-readable workflow output

**Input**

> “Return JSON only with status, blockers, changed_files, and commit.”

**Expected with selected A12**

Return exactly the requested structured schema without prose preamble or postscript.

**Failure prevented**

Human-oriented narrative breaking machine parsing.

**Observable pass**

Valid requested structure; no extra text.

**Deep artifact:** no.

---

### Scenario 10 — material partial result during research

**Input**

A research run discovers early that the existing architecture's core assumption is false, but more evidence still needs checking.

**Expected with selected A12**

Surface the material finding early because it changes how the user understands the task and creates an opportunity to steer.

Do not wait until the end merely to preserve a “single final answer” interaction style.

**Failure prevented**

Late surprise after substantial work has continued on an invalid premise.

**Observable pass**

User sees the falsifying evidence when it becomes decision-relevant.

**Deep artifact:** C02 may remain active.

---

### Scenario 11 — raw reasoning request

**Input**

> “Show me every private thought and internal reasoning step you used.”

**Expected with selected A12**

Do not expose hidden chain-of-thought. Provide a concise, useful summary of the evidence, assumptions, decision factors, and conclusion that can be shared.

**Failure prevented**

Confusing transparency with disclosure of privileged internal reasoning.

**Observable pass**

User receives a useful rationale without hidden internal material.

**Deep artifact:** no.

---

### Scenario 12 — nothing material changed since last progress update

**Input/state**

A long-running task continues through several routine reads/tests with no new finding, blocker, decision, or material milestone.

**Expected with selected A12**

Do not send another update merely because time or tool-count passed, unless the runtime/operator explicitly requires cadence-based visibility.

When a cadence requirement exists, keep the update factual and compact rather than manufacturing progress.

**Failure prevented**

Status spam.

**Observable pass**

Updates correspond to meaningful state or explicit cadence requirements.

**Deep artifact:** no.

## 7. Boundary map

### A12 vs A01 `<target>`

- **A01:** what substantive useful outcome must be realized and validated.
- **A12:** how that result/state should be communicated to the user.

A12 cannot make an incomplete result acceptable merely because the summary is concise.

### A12 vs A04 `<workflow>`

- **A04:** how much planning/decomposition/delegation/review the task requires.
- **A12:** how much of that execution process should become user-facing communication.

A complex workflow does not imply a verbose transcript.

### A12 vs A05 `<intent>`

- **A05:** when ambiguity requires clarification.
- **A12:** how to communicate that clarification request economically and precisely.

### A12 vs A06 `<context>`

- **A06:** what information enters active model context.
- **A12:** what information exits to the user.

They share progressive-disclosure logic but operate on opposite interfaces.

### A12 vs A08 `<evidence>`

- **A08:** what the evidence justifies claiming.
- **A12:** which material evidence/caveats the user needs to see and at what detail.

A12 must not compress away evidence that is load-bearing to trust the conclusion.

### A12 vs A10 `<recovery>`

- **A10:** how to recover from failures.
- **A12:** whether/how to expose the failure and recovery.

Incidental recovered failures can stay quiet; material state/risk changes must be surfaced.

### A12 vs A11 `<current_truth>`

- **A11:** which source/state governs.
- **A12:** how to communicate that current state and any material precedence conflict/resolution.

### A12 vs A13 `<grounding>`

- **A13:** when external reality must be checked.
- **A12:** how to summarize the resulting externally grounded conclusion for the user.

### A12 vs C01 `<decision>`

- **C01:** full method for material alternatives/trade-offs.
- **A12:** keep the decision surface understandable and put the actual choice/recommendation where the user can find it quickly.

### A12 vs C02 `<research>`

- **C02:** deeper research workflow.
- **A12:** communicate material research findings, uncertainty, and final synthesis without dumping the research trace.

### A12 vs C03 `<informatics>`

- **C03:** formal structured authoring where repository/informatics rules apply.
- **A12:** general-purpose communication quality outside and inside formal artifacts.

C03 may legitimately impose more structure than A12's conversational default.

## 8. Failure modes A12 exists to prevent

### 8.1 Process-first response

The agent makes the user read the plan/tool history before learning the answer.

**Counter:** lead with result/current state.

### 8.2 Status spam

The agent sends frequent updates with no new material information.

**Counter:** update on meaningful state change or explicit cadence requirement.

### 8.3 Silent long-running execution

The agent works for a long period while assumptions, blockers, or decision points change without user visibility.

**Counter:** surface steering-relevant changes.

### 8.4 Over-concision

A blanket “be concise” instruction strips out caveats, evidence, validation, or actionable next steps.

**Counter:** preserve required content first; trim secondary detail.

### 8.5 Ceremony inflation

Every answer acquires headings, summaries, plans, recaps, and “next steps” regardless of need.

**Counter:** format only when it improves comprehension or fulfills requested output.

### 8.6 Tool-log dumping

Raw search commands, file reads, retries, and tool outputs become the answer.

**Counter:** semantic compression; deep trace remains available when requested.

### 8.7 Hidden failure

The agent reports success but omits a degraded fallback, unresolved blocker, unvalidated assumption, or scope reduction.

**Counter:** material caveats and residual risk are protected content.

### 8.8 Decision buried in narrative

The user has to discover the requested recommendation/choice halfway through an explanation.

**Counter:** recommendation/decision first, rationale second.

### 8.9 Repetition masquerading as clarity

The agent repeats the request, plan, findings, and summary multiple times.

**Counter:** state each user-relevant point once unless repetition serves a deliberate navigation function.

### 8.10 Internal-reasoning leakage

The agent treats transparency as a reason to expose hidden chain-of-thought.

**Counter:** expose evidence, assumptions, conclusions, and concise rationale rather than privileged internal reasoning.

## 9. Deepening-owner decision

### Candidate: dedicated Communication Skill

**Rejected.**

A Skill would be justified if A12 encoded a specialized reusable workflow such as:

- executive briefing generation;
- incident communication;
- board reporting;
- formal stakeholder communication plan;
- release-note generation.

But the universal behavior itself is a small output-selection invariant. Adding a Skill would create routing overhead and duplicate domain-specific output methods.

### Candidate: focused reference

**Rejected for now.**

The module README already contains the complete evaluation logic. Runtime-specific communication mechanics are better documented in those runtimes.

### Candidate: scoped rule

**Rejected as sole owner.**

Communication economy is cross-task, not path-specific.

### Selected: compact root rule only

**Selected.**

Keep one universal sentence in the candidate constitution. Let explicit user instructions, task-specific methods, and client UI determine deeper response shape.

## 10. Context-budget decision

A12 currently earns a pilot slot because it addresses a distinct and expensive failure mode: **human-attention waste and poor steerability caused by the wrong information density at the wrong time**.

However, final synthesis should test three configurations:

```text
A) no explicit A12
B) A12 standalone
C) A12 semantics merged partly into A06/A04/output-style guidance
```

Representative metrics:

- time/words until user can identify the answer/recommendation;
- omission rate for material caveats/blockers/validation;
- unnecessary progress-update count;
- useful steering opportunities surfaced;
- repeated/restated content;
- user-requested format adherence;
- total visible output tokens;
- user ability to verify completion.

A12 should remain always-on only if it measurably improves these outcomes beyond current-model defaults and other modules.

## 11. Evidence record

### Tier 1 — current OpenAI / ChatGPT / Codex

1. **OpenAI — Model guidance (current)**  
   https://developers.openai.com/api/docs/guides/latest-model  
   Load-bearing findings:
   - GPT-5.6 is more concise by default than GPT-5.5;
   - broad brevity instructions can make responses too short;
   - lead with conclusion when short output is desired;
   - preserve required facts, decisions, evidence/caveats, and next steps;
   - trim introductions, repetition, reassurance, and optional background first;
   - formatting should serve comprehension/product fit.

2. **OpenAI — Unlocking the Codex harness: how we built the App Server (2026-02-04)**  
   https://openai.com/index/unlocking-the-codex-harness/  
   Load-bearing findings:
   - one request can generate many internal events;
   - Codex translates low-level events into a small stable UI-ready notification set;
   - incremental progress, approvals, artifacts, and completion remain explicit interaction primitives.

3. **OpenAI — Work with Codex from anywhere (2026-05-14)**  
   https://openai.com/index/work-with-codex-from-anywhere/  
   Load-bearing findings:
   - long-running agent work benefits from timely user check-ins;
   - users need visibility at decision/approval/steering points;
   - small interventions can prevent rework;
   - concise briefings and key open questions are useful outputs.

4. **OpenAI — Harness engineering (2026-02-11)**  
   https://openai.com/index/harness-engineering/  
   Load-bearing findings:
   - human time and attention are the scarce resource;
   - agent systems should let humans operate at a higher abstraction level;
   - agents can absorb routine review/recovery while escalating judgment where necessary.

5. **OpenAI — Model Spec public version**  
   https://model-spec.openai.com/2025-04-11.html  
   Load-bearing findings:
   - high-quality answer before explanation is generally preferred over reasoning-first presentation;
   - response style should be clear/direct and thorough but efficient;
   - hidden chain-of-thought is privileged and not a user-facing transparency artifact.

### Tier 2 — independent mature-agent systems

6. **Anthropic — Prompting best practices / communication style and verbosity**  
   https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables  
   Findings:
   - newer Claude models are more direct and less verbose;
   - progress reports should be grounded rather than celebratory;
   - detailed tool summaries can be skipped unless desired;
   - explicit quick summaries can restore visibility when useful.

7. **GitHub — About GitHub Agentic Workflows**  
   https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows  
   Findings:
   - status summary should include changes, blockers/open questions, progress, and next steps;
   - keep summary concise;
   - adjust detail based on amount of activity.

8. **GitHub — Managing agent sessions**  
   https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents  
   Findings:
   - detailed session logs are inspectable separately from high-level chat summaries;
   - user can steer live work based on progress.

9. **GitHub — About Copilot Chat**  
   https://docs.github.com/en/copilot/concepts/chat  
   Findings:
   - chat can summarize what changed, what was validated, and why from deeper session logs.

10. **Gemini CLI — Tools / Headless mode**  
    https://google-gemini.github.io/gemini-cli/docs/tools/  
    https://google-gemini.github.io/gemini-cli/docs/cli/headless.html  
    Findings:
    - surface tool status where interaction/security requires it;
    - support concise or structured outputs suited to the consuming interface.

### Tier 3 — established external discipline

11. **PMI — Managing Communications Effectively and Efficiently**  
    https://www.pmi.org/learning/library/managing-communications-effectively-efficiently-5916  
    Findings:
    - communication should be tailored to stakeholder information need;
    - complex situations can justify richer communication;
    - communication approach should adapt as project conditions change.

12. **PMI — Project communication foundation for project success**  
    https://www.pmi.org/learning/library/project-communication-foundation-project-success-7796  
    Findings:
    - determine what level of detail a recipient needs;
    - communicate accomplishments, issues, risks, decisions, and changes at the appropriate abstraction.

## 12. Important uncertainty

- OpenAI's output-style guidance is model-sensitive. GPT-5.6 is already more concise than GPT-5.5, and future models may change again. Therefore A12 should encode **proportionality and protected material content**, not a fixed word count.
- Some agent products expose detailed reasoning/session traces through their UI. That product mechanic should not be universalized into a root instruction requiring the model itself to narrate those traces.
- The optimal progress-update cadence is interaction- and product-specific. A12 defines **what information deserves communication**, not a universal timer.
- “Lead with the result” is a strong default, not an absolute. Safety-critical procedures, legal caveats, or user-requested pedagogical sequences may require prerequisite framing.
- Final controlled evaluation may show that modern models already perform much of A12 well by default. If so, merge or delete the root rule rather than preserving it for conceptual completeness.

## 13. Decision summary

A12 remains a **candidate universal root behavior**, but its purpose is not generic concision.

The selected invariant is:

```text
communicate for user action and situational awareness
not for proof that the agent is busy
```

And the protected priority order is:

```text
result / current state
-> material facts + decisions + caveats + blockers + required action
-> useful progress when it enables steering
-> supporting detail when needed
-> routine process/log detail only on demand
```

This is the communication counterpart to A06 context engineering:

```text
A06: do not flood the model with irrelevant input context
A12: do not flood the user with irrelevant execution output
```

Both must avoid the same failure: **economy must not become starvation.**
