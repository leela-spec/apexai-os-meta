---
type: Audit
title: Universal AI Instruction System — AI-Native Retroactive Audit A01–A05
description: Retroactive audit of A01–A05 against current OpenAI/ChatGPT/Codex guidance and independent mature-agent guidance, with concrete patch proposals.
status: AUDIT_COMPLETE_PATCHES_PROPOSED
updated: 2026-09-07
---

# AI-Native Retroactive Audit — A01–A05

## 1. Why this audit exists

The first five module-deepening runs used current agent-system sources, but their research presentation and reasoning order over-weighted older external disciplines such as systems engineering and project management. That is the wrong priority for an instruction system whose direct target is modern AI-agent behavior.

The corrected evidence order is:

1. **Current OpenAI / ChatGPT / Codex model and product guidance** — direct evidence for the primary target runtime and current model behavior.
2. **Independent mature agent systems** — Anthropic Claude/Claude Code, GitHub Copilot, Gemini CLI, Kiro, Cursor, Windsurf, Agent Skills where they add distinct evidence.
3. **Observed/empirical production-agent experience** — documented results from real agent deployments and evaluations.
4. **Established external disciplines** — systems engineering, requirements engineering, Lean, project management, decision analysis, incident management, etc., used to supply durable concepts, failure modes, and vocabulary.
5. **Local synthesis** — only what the preceding layers do not already establish.

External disciplines remain useful. They must not dominate or override current measured AI behavior.

## 2. Strongest current AI-native findings

### OpenAI / ChatGPT / Codex

Current primary guidance checked 2026-09-07 establishes several load-bearing principles for this program:

- **Outcome first:** ChatGPT prompting guidance says to start with the result, not a detailed process; add context/output/boundaries only when they change the result.
- **Lean persistent instructions:** GPT-5.6 guidance reports better coding-agent eval performance from leaner system prompts and explicitly recommends stating each instruction once.
- **Intent inference has improved:** GPT-5.6 can infer the user's underlying goal and intended level of work from context; prompts should provide hard constraints, approval boundaries, success criteria, and specify when ambiguity should trigger a question rather than prescribing every step.
- **Autonomy boundaries should be positive and compact:** current GPT-5.6 guidance recommends allowing in-scope local edits and relevant non-destructive validation without asking, while requiring confirmation for external, destructive, costly, or materially scope-expanding actions.
- **Boundaries should prevent real problems, not control every step:** current ChatGPT guidance recommends focusing on the one or two boundaries that matter most.
- **Planning is conditional:** OpenAI's Codex guidance recommends planning for larger changes; small well-scoped work can execute directly.
- **Context is scarce:** OpenAI's Harness Engineering report says the monolithic `AGENTS.md` approach failed; their working pattern is a short map plus structured deeper sources of truth.
- **Reuse is an explicit current platform pattern:** ChatGPT/Codex customization guidance says to install an existing plugin first when a reusable workflow already exists, then create a Skill only when needed.
- **Evaluation, not theoretical completeness, is the final judge:** current model guidance repeatedly recommends testing prompt/model/config changes on representative tasks rather than assuming more rules, more reasoning, or more process is better.

### Independent mature-agent convergence

- **Anthropic:** current prompting guidance favors clear desired behavior, relevant context, examples where they fix measured gaps, and explicit default-to-action behavior when proactive execution is desired. It also warns that newer models may over-trigger on legacy anti-laziness scaffolding and that prompts should be retuned rather than accumulated indefinitely.
- **GitHub Copilot:** current guidance says persistent instructions should be short, specific, and grounded in observed agent behavior, not generic best-practice prose. It separately emphasizes lean context, clear task definition, relevant context, and a stopping condition.
- **Gemini CLI:** Plan Mode is a distinct read-only mode for complex changes; subagents are specialized/context-isolating tools, not mandatory ceremony. Hierarchical `GEMINI.md` gives specific context just in time.
- **Agent Skills:** both current OpenAI and Anthropic implementations use progressive disclosure: lightweight metadata is visible first; full workflow instructions are loaded only when the task matches.

## 3. Program-level audit result

### Finding P0 — research order is wrong

**Severity:** HIGH  
**Status:** PATCH REQUIRED BEFORE A06

The current handover structurally asks the researcher to establish an underlying external discipline before researching mature agent implementations. That ordering invites exactly the observed failure: NASA/PMI become the conceptual center and AI guidance becomes supporting evidence.

**Required correction:** reverse the order. Current OpenAI/ChatGPT/Codex guidance must be researched first, followed by independent agent-system convergence; external disciplines come third.

### Finding P1 — final synthesis must aggressively defend context budget

**Severity:** HIGH  
**Status:** PROGRAM EVALUATION REQUIREMENT

OpenAI's current guidance gives direct empirical support for leaner system prompts, and Harness Engineering documents failure of a large monolithic `AGENTS.md`. Therefore an individually reasonable module does **not** automatically deserve permanent always-on presence.

At final synthesis:

- require behavioral evidence for each always-on rule;
- merge overlapping modules where one compact rule preserves behavior;
- delete rules that current models already perform reliably without prompting unless they correct an observed recurring failure;
- keep deeper procedures behind Skills/references/JIT routing;
- compare the full XML constitution against a smaller control prompt on representative tasks.

## 4. Module verdicts

| Module | Verdict | Change level | AI-native reason |
|---|---|---:|---|
| A01 `<target>` | **PATCH** | Medium | Correct behavior, but current wording is broader/more abstract than current outcome-first + success/stopping guidance and overlaps A04 on effort/depth. |
| A02 `<scope>` | **REDESIGN** | High | Current wording is primarily restrictive. Current GPT-5.6 guidance supports a compact positive autonomy/approval policy: safe in-scope local action without asking; explicit stop points for destructive/external/costly/scope-expanding actions. |
| A03 `<reuse>` | **PATCH** | Low/Medium | Strongly supported by current ChatGPT/Codex plugin/Skill architecture, but current wording can imply mandatory external searching. External evaluation should be conditional on likely relevance. |
| A04 `<workflow>` | **KEEP** | None | Strong match to current Codex/Claude/Gemini conditional planning and cleanly-independent delegation guidance. |
| A05 `<intent>` | **PATCH** | Medium | Semantics are strong, but current OpenAI/Anthropic guidance supports more explicit intent inference/default-to-action and a smaller missing-decision question instead of generic elicitation framing. |

## 5. Proposed semantic patches

These are **proposals, not yet applied to the live pilot**. Apply them together only after review so the module result records and pilot stay synchronized.

### A01 — proposed patch

#### Current

```xml
<target principles="intent-preservation,outcome-orientation,validation,anti-proxy-optimization,proportional-rigor">
  Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; use the depth, rigor, completeness, and effort the outcome actually requires.
</target>
```

#### Proposed

```xml
<target principles="outcome-first,success-criteria,validation,stopping-condition,anti-proxy-optimization">
  Realize the intended useful result, not merely a named artifact or check. Treat tests, schemas, metrics, and other acceptance signals as evidence; continue until the result is substantively satisfied, then stop.
</target>
```

#### Why

- Directly matches current OpenAI outcome-first prompting and explicit stopping-condition guidance.
- Preserves the operator's critical anti-checkmark / anti-proxy requirement.
- Removes `depth, rigor, completeness, effort` from the root sentence because A04 already decides workflow depth and later A08 will govern evidence strength.
- Adds an explicit stop condition so “substantive” does not become permission for endless extra work.

**Confidence:** HIGH that the semantics should tighten; MEDIUM-HIGH on exact wording pending cross-agent eval.

### A02 — proposed redesign

#### Current

```xml
<scope principles="scope-control,non-goals,change-control">
  Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
</scope>
```

#### Proposed

```xml
<scope principles="authorization-mode,autonomy-boundaries,non-goals">
  Match action to the request: analysis/review/planning does not authorize implementation; change/build/fix requests authorize in-scope local changes and relevant non-destructive validation without asking. Keep incidental improvements separate and confirm before destructive, external, costly, or materially scope-expanding actions.
</scope>
```

#### Why

This is the largest correction in the audit.

The current module answers mostly “what should the agent avoid?” Current GPT-5.6 guidance instead gives a compact **positive autonomy policy**:

- infer the action level from the request;
- continue safe in-scope work without unnecessary pauses;
- distinguish analysis-only from implementation authorization;
- reserve explicit confirmation for materially riskier boundary crossings.

This makes A02 useful even when nothing goes wrong. It tells the agent what it **may autonomously do**, not only what it may not do.

The explicit incidental-improvement boundary retains the useful anti-scope-creep behavior from the current module.

**Confidence:** HIGH. This is the strongest patch recommendation from the audit.

### A03 — proposed patch

#### Current

```xml
<reuse principles="make-buy-reuse,fitness-for-use">
  Before building nontrivial custom capability, check suitable existing project assets and established external solutions. Reuse or adapt a fit-for-purpose option when it meets the target and constraints; build new only when a demonstrated gap or better overall trade-off justifies it.
</reuse>
```

#### Proposed

```xml
<reuse principles="reuse-before-build,fitness-for-use">
  Before creating nontrivial custom capability, inspect existing project assets first and, when an established external solution is plausibly relevant, evaluate it before building. Reuse or adapt a fit-for-purpose option when it meets the target and constraints; build new when the gap or overall trade-off justifies it.
</reuse>
```

#### Why

- Current ChatGPT/Codex customization guidance explicitly recommends installing an existing plugin first when a reusable workflow already exists, otherwise creating a Skill.
- `project assets first` remains correct and token-efficient.
- Making external evaluation conditional avoids turning A03 into a compulsory market scan for every nontrivial change.
- `reuse-before-build` is more immediately legible to an AI agent than the older discipline label `make-buy-reuse`; the deeper README can retain make/buy/reuse as conceptual grounding.

**Confidence:** MEDIUM-HIGH. Behavior is already good; this is mostly trigger precision and AI-native framing.

### A04 — no patch

Current:

```xml
<workflow principles="process-tailoring,progressive-elaboration,risk-informed-planning">
  Tailor execution depth to task complexity, uncertainty, coupling, and consequence. Execute clear low-risk work directly; when those factors warrant it, plan, decompose, delegate independent work, and review proportionately, adapting as new evidence changes the task.
</workflow>
```

**Decision:** KEEP.

Reasons:

- OpenAI: planning for larger changes; direct work remains appropriate for well-scoped tasks.
- GPT-5.6 multi-agent: parallelization is beneficial when complex work divides cleanly into independent workstreams.
- Gemini CLI: Plan Mode exists specifically as a separate research/design mode for complex changes.
- Anthropic: current agent guidance similarly treats planning/delegation as task-dependent and warns against legacy scaffolding over-triggering on newer models.

The existing wording already captures this well and does not need AI-fashion vocabulary inserted merely for appearance.

**Confidence:** HIGH.

### A05 — proposed patch

#### Current

```xml
<intent principles="requirements-elicitation,requirements-validation,closed-loop-communication">
  Resolve ambiguity from available evidence before asking. Make routine, reversible judgment calls autonomously; clarify or check back only when unresolved ambiguity could materially change the intended outcome, scope, governing constraints, or a consequential choice.
</intent>
```

#### Proposed

```xml
<intent principles="intent-inference,default-to-action,targeted-clarification">
  Infer intent from the request, prior context, and readily available task evidence. Make reasonable low-risk or reversible choices and continue; ask only for the smallest missing decision when unresolved ambiguity could materially change the outcome, authorization boundary, or a consequential action.
</intent>
```

#### Why

- GPT-5.6 explicitly says it can infer underlying goals and intended level of work from context and should be told when important ambiguity warrants a question.
- GPT-5.6 autonomy guidance warns that repeated “ask first” language can create unnecessary approval requests.
- Anthropic's current proactive-action guidance similarly says to infer useful action and use tools to discover missing details instead of guessing or immediately asking.
- `readily available task evidence` reduces the risk that “resolve from available evidence” becomes an exhaustive repository/search expedition; A06 will own context retrieval depth.
- `smallest missing decision` makes clarification information-dense and anti-ceremonial.

**Confidence:** HIGH on behavioral direction; MEDIUM-HIGH on exact principle labels.

## 6. Interaction after proposed patches

The five modules would then have cleaner positive roles:

```text
A01 target   -> what useful result counts as success, and when to stop
A02 scope    -> what action level is authorized; safe autonomy vs boundary crossings
A03 reuse    -> obtain existing capability before custom construction when relevant
A04 workflow -> scale planning/delegation/review to task shape and consequence
A05 intent   -> infer intent; ask only for a material missing decision
```

This is materially better than five adjacent “be careful” constraints.

## 7. Required patch to the research method before A06

The module-deepening program should use this research order for every remaining module:

### A. Current AI-native guidance first

Research current primary guidance for the actual target runtimes, beginning with OpenAI/ChatGPT/Codex. Extract current model behavior, prompting recommendations, instruction/context architecture, approval/autonomy patterns, Skills/plugins/tool patterns, and measured failure modes relevant to the module.

### B. Cross-agent convergence

Check at least two independent mature systems when relevant (for example Anthropic Claude/Claude Code, GitHub Copilot, Gemini CLI, Kiro, Cursor, Windsurf). Distinguish genuine convergence from vendor-specific product mechanics.

### C. Established external discipline

Only after the AI-native evidence is understood, use established disciplines to supply durable concepts, vocabulary, trade-off methods, or failure modes. Do not let an older discipline override current measured model behavior merely because its terminology is more formal.

### D. Compare alternatives and test wording

Evaluate competing designs against:

- current AI behavior;
- portability across agents;
- context/token cost;
- activation reliability;
- risk of over-triggering/under-triggering;
- overlap with neighboring modules;
- representative scenario evals.

The existing XML remains a hypothesis, not an authority.

## 8. Sources — AI-native primary layer

Checked 2026-09-07.

### OpenAI / ChatGPT / Codex

1. OpenAI — GPT-5.6 Model Guidance  
   https://developers.openai.com/api/docs/guides/latest-model
2. ChatGPT Learn — Prompting (Chat, ChatGPT Work, Codex)  
   https://learn.chatgpt.com/docs/prompting
3. OpenAI — Harness engineering: leveraging Codex in an agent-first world  
   https://openai.com/index/harness-engineering/
4. OpenAI — How OpenAI uses Codex  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/
5. ChatGPT Learn — Customization overview / Skills, plugins, MCP, subagents  
   https://learn.chatgpt.com/docs/customization/overview
6. ChatGPT Learn — Build Skills  
   https://learn.chatgpt.com/docs/build-skills
7. OpenAI Academy — Codex for Faculty and Researchers Follow Along Guide (2026-06-09)  
   https://academy.openai.com/public/clubs/higher-education-05x4z/resources/codex-for-faculty-and-researchers-follow-along-guide-2026-06-09

### Independent mature agents

8. Anthropic — Prompting best practices  
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
9. Anthropic — Agent Skills overview  
   https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
10. GitHub — Optimizing AI usage to maximize efficiency and reduce cost  
    https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
11. Google Gemini CLI — Plan Mode  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md
12. Google Gemini CLI — Subagents  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
13. Google Gemini CLI — GEMINI.md hierarchical context  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md

## 9. Secondary discipline layer

The NASA/PMI/INCOSE/AHRQ material already collected remains valid as **secondary** evidence for durable concepts such as validation, scope control, enabling work, process tailoring, requirements clarity, and closed-loop communication.

The audit does **not** conclude that those sources were wrong. The error was giving them the wrong epistemic priority for an AI-agent instruction system.

## 10. Application plan

Before A06:

1. Patch the module-deepening handover and live README research standard to make the AI-native-first hierarchy authoritative.
2. Review the proposed A01/A02/A03/A05 XML replacements as one coherent patch set.
3. If accepted, update each affected module README with an `AI-native audit amendment`, update its final XML/control wording, and patch the pilot in the same commit so no source of truth disagrees.
4. Leave A04 unchanged.
5. Do not advance the module status table; A06 remains `NEXT` until the retroactive patch decision is settled.
6. Continue A06 only under the corrected research order.

## 11. Audit conclusion

The first five modules are **not invalid**, but the audit found that the current system is too influenced by general governance/engineering language and not yet optimized enough for current frontier-agent behavior.

The most important corrective direction is:

> **Outcome + autonomy + selective boundaries + reuse + adaptive workflow + targeted clarification.**

Not:

> **More constraints, more formal process, or more requirements language.**

The final constitution should earn every always-on token through measured behavioral value.