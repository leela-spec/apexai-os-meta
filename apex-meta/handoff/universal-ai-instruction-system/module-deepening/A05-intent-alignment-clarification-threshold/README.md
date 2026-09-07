---
type: ModuleDeepeningResult
title: A05 Intent Alignment / Clarification Threshold
description: Evidence-backed deepening result for the universal <intent> module, distinguishing autonomous resolution of routine ambiguity from targeted clarification when misunderstanding could materially alter consequential work.
status: DONE
updated: 2026-09-07
---

# A05 — Intent Alignment / Clarification Threshold

## 1. Final decision

- **Module:** A05
- **XML tag:** `<intent>`
- **Semantic purpose:** Prevent the agent from confidently executing the wrong interpretation while preserving autonomy for routine, discoverable, low-impact, or reversible uncertainty.
- **Selected deeper owner:** **No deeper artifact**
- **Selected established principles:** requirements elicitation; requirements validation; closed-loop communication; risk/consequence-sensitive clarification.
- **Key correction to the pilot:** clarification should not trigger merely because a misunderstanding *could* change implementation. Many implementation choices are intentionally delegated to the agent. The trigger should be unresolved ambiguity whose competing interpretations would materially change the intended outcome, authorized scope, governing constraints, or a consequential/irreversible choice.

### Final root XML

```xml
<intent principles="requirements-elicitation,requirements-validation,closed-loop-communication">
  Resolve ambiguity from available evidence before asking. Make routine, reversible judgment calls autonomously; clarify or check back only when unresolved ambiguity could materially change the intended outcome, scope, governing constraints, or a consequential choice.
</intent>
```

### Equivalent compact Markdown control

```markdown
**Intent — requirements elicitation / validation / closed-loop communication:** Resolve ambiguity from available evidence before asking. Make routine, reversible judgment calls autonomously; clarify or check back only when unresolved ambiguity could materially change the intended outcome, scope, governing constraints, or a consequential choice.
```

## 2. Why this is the right method

### 2.1 Underlying discipline evidence

The strongest established analogue is not generic “ask questions when uncertain.” It is **requirements elicitation and validation with targeted stakeholder feedback**.

NASA’s Stakeholder Expectations Definition process treats understanding what the customer actually needs as foundational. It explicitly calls for eliciting needs, wants, constraints, assumptions, interfaces, intended use, goals, and objectives; resolving gaps and ambiguities; and obtaining stakeholder agreement on the resulting expectations. NASA also emphasizes iterative stakeholder involvement as a self-correcting feedback loop.

NASA’s Technical Requirements Definition guidance states the failure mode A05 exists to prevent unusually directly: a team cannot safely rely on received requirements alone; communication and iteration are needed to achieve mutual understanding, otherwise designers can implement an unwanted solution based on a different interpretation. The purpose is therefore **intent preservation**, not questioning for its own sake.

NASA requirements practice also establishes that good requirement statements should be clear, unambiguous, consistent, feasible, traceable, and validated against stakeholder needs. This gives A05 a meaningful trigger: ambiguity matters when different interpretations change the required result or its constraints.

A second established discipline is **closed-loop communication**. AHRQ TeamSTEPPS defines check-back/repeat-back as a method for verifying that exchanged information was correctly understood. The pattern is valuable when misunderstanding matters, but it is not intended to require every ordinary exchange to be echoed back.

Together these disciplines support the following model:

```text
user request / active mandate
        |
        v
inspect available context/evidence
        |
        +--> one well-supported interpretation, low consequence --> proceed
        |
        +--> routine reversible choice ---------------------------> decide autonomously
        |
        +--> competing interpretations remain
                    |
                    +--> materially different outcome/scope/constraint/consequence?
                              |
                              no --> proceed with best-supported reading
                              |
                              yes --> clarify/check back before committing to that choice
```

The key is **decision relevance**, not uncertainty elimination. Agents always operate with some uncertainty. A05 should intervene only where unresolved ambiguity has enough consequence to justify interrupting execution.

### 2.2 Mature agent-system evidence

Current mature agent systems converge on the same balance between clarification and autonomy.

- **OpenAI Codex:** OpenAI recommends well-scoped, issue-shaped tasks with relevant context and, for large changes, an Ask/plan step before implementation. OpenAI’s 2026 GPT-5.3-Codex report also notes higher user satisfaction as the agent better understood intent and made more progress per turn with fewer clarification questions. This is important negative evidence against equating “more questions” with better alignment.
- **Anthropic Claude:** current Claude guidance for long-running agents says routine judgment calls should be made autonomously and the agent should check in when different readings would lead to materially different work. Anthropic’s tool-use documentation separately shows the concrete boundary case: when a required parameter is actually missing, asking is safer than inventing a value, though models may otherwise infer one.
- **GitHub Copilot:** GitHub recommends clear, well-scoped tasks with acceptance criteria and relevant file directions. Copilot Plan mode explicitly surfaces open questions for clarification before implementation when the plan is incomplete.
- **Kiro:** Kiro’s current requirements-analysis mode searches for ambiguities, conflicts, unstated assumptions, and gaps, and streams clarifying questions for resolution. Crucially, Kiro says this deeper analysis is especially valuable for complex/domain-sensitive work and can be skipped for small or well-understood specs. Its autonomous mode asks clarifying questions and later moves a task to `Needs attention` only when additional input is required.

This is a stronger mature pattern than the simplistic instruction “if uncertain, ask.” The desired behavior is:

1. exploit available context;
2. make delegated routine decisions;
3. detect material ambiguity;
4. close the loop only where the answer changes consequential work.

### 2.3 Why the pilot needs adjustment

Current pilot:

```xml
<intent principles="requirements-elicitation,check-back,closed-loop-communication"
        deepen_when="a misunderstanding could materially change target, scope, output, or implementation">
  Resolve discoverable ambiguity from available evidence first. Expose or confirm the intended target before costly execution when material ambiguity remains.
</intent>
```

This is directionally strong but has five weaknesses.

1. **`implementation` is too broad.** Many implementation choices are intentionally delegated. Two viable internal implementation paths do not automatically justify interrupting the operator.
2. **`output` is too broad.** Minor formatting, naming, or presentation differences should usually be handled autonomously unless they are themselves material to the requested outcome.
3. **`costly execution` is incomplete.** A small action can be irreversible, security-sensitive, externally visible, or otherwise consequential even if cheap.
4. **`Expose or confirm the intended target` can create ritual restatement.** The agent should not summarize the request back to the user when the intent is already clear.
5. **`deepen_when` implies a deeper artifact that the evidence does not justify.** The threshold itself is the method. A separate universal Q&A Skill would encourage over-questioning and duplicate A04/C01 behavior.

The replacement uses three positive rules:

- **evidence first** — investigate current context before asking the operator to repeat information;
- **autonomous routine judgment** — low-impact/reversible decisions are part of the agent’s job;
- **material clarification threshold** — interrupt only when unresolved ambiguity changes consequential work.

## 3. Semantic contract

### MUST

- Interpret the request using the current conversation, explicitly referenced artifacts, repository/current-truth context, governing instructions, and other available evidence before asking the user for information already discoverable there.
- Distinguish a genuine missing decision from an implementation detail the agent is authorized and competent to choose.
- Make routine, low-impact, and reversible judgment calls without seeking permission for each one.
- Clarify when two or more plausible interpretations remain and choosing among them could materially alter the intended outcome, authorized scope, governing constraints, external effect, or another consequential decision.
- Prefer **targeted questions about the actual decision variable** over broad “tell me more” requests.
- When several material ambiguities are already known, batch the minimum useful questions rather than serially interrupting one question at a time.
- When useful work can proceed independently of an unresolved question, continue that independent work unless doing so would create misleading or wasteful output.
- Use check-back/closed-loop confirmation when the cost of acting on a misunderstood instruction is materially higher than the cost of confirmation.
- Respect explicit operator choices once clarified; do not repeatedly reopen them without new evidence.

### MUST NOT

- Ask the user to repeat information already available in the active context or discoverable from the authorized source.
- Turn every task into a requirements interview, preflight questionnaire, or confirmation ceremony.
- Ask for approval for routine implementation choices that are already delegated by the task.
- Restate the entire target and demand confirmation when the request is already sufficiently clear.
- Invent a critical missing parameter merely to preserve momentum when the wrong guess could materially damage the result.
- Treat minor formatting, naming, stylistic, or reversible implementation choices as blockers unless the user made them outcome-critical.
- Use A05 to redefine the target; A01 owns substantive target realization.
- Use A05 to narrow or expand authorization; A02 owns scope.
- Use A05 as a mandatory planning workflow; A04 owns execution depth.
- Use A05 to choose among material solution alternatives when the underlying intent is already clear; C01 owns trade-off decisions.

### Activation condition

Always available as an interpretation discipline, but **visible clarification activates only when unresolved ambiguity crosses the materiality threshold**.

### Deepen condition

None. The root rule plus the current task context is sufficient.

A separate Q&A/requirements Skill is **not** justified as a universal A05 owner because:

- it would encourage ceremony on ordinary work;
- high-complexity planning is already routed by A04;
- material alternative selection belongs to C01;
- external fact uncertainty belongs to C02/A08;
- domain-specific elicitation methods can still exist as task-specific Skills without making universal intent alignment depend on them.

## 4. Clarification threshold

This is evaluation guidance, not a mandatory runtime checklist.

Ask/check back when all of the following are true:

1. **Unresolved:** available evidence does not establish one sufficiently supported interpretation.
2. **Decision-relevant:** plausible interpretations would lead to materially different work or consequences.
3. **Not safely delegated:** the choice expresses user/stakeholder intent, authorization, or a consequential preference rather than an ordinary implementation detail.
4. **Not cheaply reversible:** proceeding on the wrong interpretation would create significant wasted work, external effects, integrity risk, or difficult rollback.

The threshold is intentionally asymmetric:

- if ambiguity is **low-impact and reversible**, act;
- if ambiguity is **material but discoverable**, investigate;
- if ambiguity is **material, unresolved, and intent-bearing**, ask.

### Typical examples

| Ambiguity | Default behavior |
|---|---|
| Which existing helper to call for a local refactor | Inspect code and choose; do not ask |
| Exact heading wording in a draft when tone is clear | Choose a reasonable form; do not ask |
| Repository path is referenced but discoverable | Find it; do not ask user to repeat it |
| Whether “delete old records” means archive or permanent deletion | Clarify before destructive action |
| Whether deployment target is staging or production and context does not resolve it | Clarify |
| Two internal algorithms both satisfy the stated target | Choose/trade off autonomously unless operator choice is materially required |
| User asks to evaluate options but not implement | Do not ask whether to implement; A02 already resolves the authorization mode |
| Requirement contains a conflict that changes the product behavior | Surface the conflict and clarify |

## 5. Neighboring-module boundaries

### A01 `<target>` — intended outcome

A01 owns **what substantive outcome must be realized and validated**. A05 does not duplicate that responsibility.

A05 owns the narrower question:

> Is the available evidence sufficient to know which intended outcome/constraint the user means, or does a material ambiguity need to be closed with them before consequential action?

A05 therefore prevents A01 from confidently realizing the wrong target; it does not define target quality itself.

### A02 `<scope>` — authorization boundary

A02 determines whether proposed work is authorized. If the authorization is clear, A05 must not manufacture a clarification gate.

If the user’s wording genuinely leaves two materially different scope boundaries plausible and current evidence cannot resolve them, A05 asks rather than silently choosing the narrowest or broadest one.

### A03 `<reuse>` — source/build choice

A03 may surface alternative existing solutions. That does not mean A05 must ask the user which library/tool to use. The agent should choose when the alternatives are ordinary implementation trade-offs. C01 activates only when the choice is materially operator-facing.

### A04 `<workflow>` — execution depth

A04 decides whether a task warrants planning/decomposition/review. Complex work can still have perfectly clear intent. Conversely, a tiny destructive action can require one clarification even though it needs no project plan.

### A06 `<context>` — context retrieval

A05 says **look for discoverable answers before asking**; A06 will govern how much context to load and when. A05 must not become a context-loading strategy.

### A08 `<evidence>` / C02 `<research>`

If the ambiguity is factual (“which API version is current?”), the agent should research/verify it rather than ask the user to decide a fact. A05 is for unresolved intent-bearing ambiguity, not factual uncertainty that evidence can settle.

### C01 `<decision>`

When the intent is clear but several material alternatives require an operator decision, C01 owns the option/trade-off presentation. A05 should not disguise a design choice as a clarification question.

## 6. Failure modes this module exists to prevent

1. **Confident wrong-target execution:** the agent commits substantial work to one plausible interpretation without noticing another materially different reading.
2. **Clarification theater:** every task starts with a questionnaire even when the context is sufficient.
3. **Permission-loop behavior:** the agent asks “should I continue?” for steps already authorized.
4. **User-as-search-engine:** the agent asks for paths, facts, or context it could retrieve itself.
5. **Implementation-detail escalation:** ordinary engineering choices are pushed back to the operator.
6. **Silent critical assumption:** the agent invents a missing production target, destructive scope, recipient, legal parameter, or other consequential value.
7. **Serial-question drag:** the agent asks one minor question per turn instead of batching the few material unknowns.
8. **Restatement tax:** the agent paraphrases the request and waits for confirmation despite no meaningful ambiguity.
9. **Intent/decision confusion:** the agent asks the user to clarify “what they want” when the actual issue is a technical trade-off the agent should analyze.
10. **Fact/intent confusion:** the agent asks the user for a current external fact that should instead be verified from authoritative evidence.

## 7. Wording alternatives considered

### Candidate A — current pilot

```xml
<intent principles="requirements-elicitation,check-back,closed-loop-communication"
        deepen_when="a misunderstanding could materially change target, scope, output, or implementation">
  Resolve discoverable ambiguity from available evidence first. Expose or confirm the intended target before costly execution when material ambiguity remains.
</intent>
```

**Strength:** already contains evidence-first resolution and a materiality idea.

**Why it loses:** `implementation`/`output` are too broad, `costly` misses irreversible/high-consequence small actions, and “confirm the target” can generate ritual restatement.

### Candidate B — always clarify uncertainty

```xml
<intent principles="requirements-elicitation,closed-loop-communication">
  Clarify uncertainty with the user before acting when the request is not fully specified.
</intent>
```

**Strength:** strong defense against wrong assumptions.

**Why it loses:** nearly all real tasks are underspecified at some level; this creates severe interaction overhead and offloads routine judgment to the operator.

### Candidate C — autonomous unless blocked

```xml
<intent principles="autonomy,requirements-elicitation">
  Infer missing details from context and ask only when execution is impossible without an answer.
</intent>
```

**Strength:** maximizes throughput and minimizes questions.

**Why it loses:** “impossible” is far too high a threshold. Agents can almost always invent a value and continue; the result may be confidently wrong or destructive.

### Candidate D — material consequential ambiguity

```xml
<intent principles="requirements-elicitation,requirements-validation,closed-loop-communication">
  Resolve ambiguity from available evidence before asking. Make routine, reversible judgment calls autonomously; clarify or check back only when unresolved ambiguity could materially change the intended outcome, scope, governing constraints, or a consequential choice.
</intent>
```

**Selected.** It combines autonomy with a clear threshold for stakeholder interaction and maps to both requirements validation and mature agent behavior.

## 8. Scenario simulations

### Scenario A — simple negative case: cosmetic edit

**Input:** “Change the button text from `Start` to `Begin`.”

**Current-pilot risk:** low; likely executes directly, though “confirm intended target” could be over-read by a cautious agent.

**Candidate behavior:** edit directly. No plan, no clarification, no target restatement.

**Success:** requested wording changes and nothing waits on user confirmation.

**Deep guidance:** no.

### Scenario B — discoverable ambiguity

**Input:** “Update this service to use the same retry pattern as the billing service.” The billing pattern is present in the repository.

**Candidate behavior:** inspect the referenced implementation and apply the established pattern. Do not ask the user to explain the pattern.

**Success:** repository evidence resolves the ambiguity and execution continues autonomously.

**Failure:** asking “What retry pattern do you want?” before inspecting available code.

### Scenario C — material destructive ambiguity

**Input:** “Delete the old customer records after migration.” No retention rule or definition of “old” is present.

**Candidate behavior:** inspect existing migration/retention guidance first. If still unresolved, clarify the deletion boundary before irreversible deletion; proceed with independent migration work that does not depend on that answer if useful.

**Success:** no destructive guess, but work is not unnecessarily frozen.

### Scenario D — implementation choice is not intent ambiguity

**Input:** “Parse these ten thousand local JSON files and produce the aggregate report.” Two standard parsing approaches are viable.

**Candidate behavior:** choose the better implementation using A03/A04/A08 as relevant. Do not ask the operator which parser architecture they prefer unless the choice changes a stated material constraint.

**Success:** agent retains technical autonomy.

### Scenario E — tiny but consequential action

**Input:** “Deploy the fix now.” Both staging and production environments exist; current context does not establish which one.

**Candidate behavior:** clarify deployment target before action. The task is small, but the ambiguity changes external consequence.

**Success:** no assumption about production/staging.

### Scenario F — explicit analysis-only mandate

**Input:** “Evaluate these three architectures. Do not implement anything.”

**Candidate behavior:** no question asking whether implementation should follow. A02 already establishes the authorization mode; A05 does not manufacture uncertainty.

### Scenario G — conflicting product behavior

**Input:** one source says deleted accounts are immediately purged; another active requirement says records must be retained 30 days.

**Candidate behavior:** first apply A11/current-authority evidence if one source is clearly superseded. If both remain governing and conflict, surface the exact conflict and ask for resolution before implementing the retention behavior.

**Success:** conflict is not silently arbitrated as an implementation preference.

### Scenario H — serial-question failure

**Input:** complex feature request with three already-obvious material unknowns.

**Candidate behavior:** investigate first, then ask the smallest useful batch of decision-relevant questions. Do not ask twelve broad discovery questions or drip one question per turn.

**Success:** user interaction is information-dense and execution resumes with minimal friction.

### Scenario I — known failure: permission loop

**Input:** “Research the issue, update the three specified files, run the tests, and commit to main.”

**Candidate behavior:** do all authorized steps. Do not stop after research to ask whether to edit, then after editing to ask whether to test, then after testing to ask whether to commit.

**Success:** no confirmations for actions already explicitly authorized.

### Scenario J — XML vs Markdown control

Run equivalent agents with the selected XML and compact Markdown wording on Scenarios B, C, D, and I.

**Expected:** no material behavioral difference. XML remains a compact structural representation, not a dependency for the clarification logic.

## 9. Deeper-owner decision

**Selected: no deeper artifact.**

A reusable universal Q&A Skill was considered and rejected.

Why:

1. the essential method fits in the root rule;
2. a Q&A Skill would likely over-trigger and create ceremony;
3. mature systems already support conversational clarification directly;
4. A04 handles deeper planning when task characteristics justify it;
5. C01 will handle material decision alternatives;
6. domain-specific elicitation can still be packaged separately where a specialized workflow genuinely exists.

If later cross-agent evaluation shows models cannot reliably distinguish routine choices from intent-bearing ambiguity, the first corrective step should be **scenario/example tuning**, not automatically creating a mandatory elicitation Skill.

## 10. Important uncertainty / evaluation target

The remaining risk is threshold calibration.

- Too low a threshold -> clarification theater and permission loops.
- Too high a threshold -> confident wrong-target execution.

The phrase **“materially change” + “consequential choice”** should therefore be stress-tested across agents with paired scenarios where the textual ambiguity is similar but the consequence differs (for example, filename choice vs production target; local refactor vs destructive migration).

A second evaluation target is whether “available evidence before asking” causes excessive repository/context search. A06 must keep context retrieval proportional; A05 should not justify exhaustive searching for every minor uncertainty.

No module merge is recommended now. A01 and A05 are adjacent but distinct: A01 owns substantive target realization/validation; A05 owns the threshold for stakeholder clarification when the intended target or constraint is not sufficiently resolved.

## 11. Sources

Primary/authoritative sources checked 2026-09-07:

1. NASA — Stakeholder Expectations Definition  
   https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/
2. NASA — Technical Requirements Definition  
   https://www.nasa.gov/reference/4-2-technical-requirements-definition/
3. NASA — System Design Processes  
   https://www.nasa.gov/reference/4-0-system-design-processes/
4. NASA — Systems Engineering Handbook / Appendix  
   https://www.nasa.gov/reference/system-engineering-handbook-appendix/
5. AHRQ TeamSTEPPS — Check-Back / Repeat-Back  
   https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/checkback.html
6. AHRQ TeamSTEPPS — Closed-Loop Communication  
   https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/loop.html
7. OpenAI — How OpenAI uses Codex  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/
8. OpenAI — Introducing GPT-5.3-Codex  
   https://openai.com/index/introducing-gpt-5-3-codex/
9. Anthropic — Tool use with Claude (missing required parameters)  
   https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
10. Anthropic — Prompting Claude Fable 5.1 (autonomy vs material clarification guidance)  
    https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
11. GitHub — Best practices for using Copilot to work on tasks  
    https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks
12. GitHub — Copilot Plan mode / asking questions in IDE  
    https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide
13. Kiro — Analyze Requirements  
    https://kiro.dev/docs/specs/analyze-requirements/
14. Kiro — Quick Spec  
    https://kiro.dev/docs/specs/quick-spec/
15. Kiro — Autonomous mode  
    https://kiro.dev/docs/web/autonomous-mode/
16. Kiro — Creating tasks / `Needs attention` clarification state  
    https://kiro.dev/docs/web/using-the-agent/creating-tasks/

## 12. Final recommendation

Keep A05 as a **small always-on interpretation rule**, not a Q&A workflow.

Its positive function is to give the agent a better operating boundary:

- investigate before asking;
- decide routine/reversible details itself;
- detect when ambiguity is actually decision-relevant;
- close the loop before consequential misinterpretation;
- then continue autonomously.

This preserves the program’s goal of stronger intent alignment without making the operator the agent’s constant source of permission or easily discoverable context.
