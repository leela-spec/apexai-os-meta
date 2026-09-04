---
type: Handover
title: Universal AI Interaction Instruction System — Orchestrator Handover
description: Research-first launcher to turn the operator's AI Snippets into a modular, portable, progressively disclosed instruction system, then generate one bounded authoring handover per validated behavior module.
status: research_handover_no_live_instruction_changes_authorized
created: 2026-09-04
repository: leela-spec/apexai-os-meta
branch: main
---

# Universal AI Interaction Instruction System — Orchestrator Handover

## 0. Mission

Act as the **research and architecture orchestrator** for a universal AI interaction instruction system.

The operator wants one portable way to tell any capable AI **how to work with him**, without forcing every session to load a large rulebook.

The desired architecture is:

```text
very short, self-sufficient instruction snippets
        ↓ only when relevant
focused method / Skill / reference file
        ↓ only when necessary
examples, mistakes, evidence, research, evals
```

Do **not** begin by rewriting `AGENTS.md`, `CLAUDE.md`, client-specific instruction files, or existing Skills.

Do **not** assume the current snippets are best practice.

First research the general architecture and vocabulary. Then modularize the behavior domains. Then create a separate bounded handover for another AI to research and author each selected module.

The primary result of this run is **the architecture decision + module map + child handovers**, not the final global instruction set.

---

# 1. Core operator intent

Preserve these requirements:

1. **Portable semantics:** the behavioral guidance should remain understandable across different AI systems, not only Claude or one coding agent.
2. **Known vocabulary before invented vocabulary:** use established concepts, standards, research terms, and common agent patterns wherever they fit.
3. **Tiny always-on surface:** each universal instruction must be short enough to live in a root agent/custom-instruction surface without causing context bloat.
4. **Self-sufficient snippets:** the short text should already communicate the essential behavior. The linked file adds sophistication; it must not be required to understand the basic rule.
5. **Progressive disclosure:** load deeper files only when the task or failure mode actually needs them.
6. **One owner per concept:** avoid duplicating the same method across snippets, agent files, Skills, and knowledge files.
7. **Adaptive rigor:** simple requests should stay simple. Complex requests may trigger a deeper method.
8. **Target before process:** procedures exist to improve the requested outcome, not to satisfy artificial workflow checkmarks.
9. **Research before canonization:** current `Snippets.md` content is source material/operator preference, not validated doctrine.
10. **Modular research:** after the shared architecture is selected, each behavior domain gets its own narrow research-and-authoring handover.

---

# 2. Current repository sources — read only what is needed

## Required starting sources

### A. Operator snippet collection

`apex-meta/AI-Snippets/Snippets.md`

Treat it as **operator-authored candidate behavior**, not authority.

It currently contains rough modules for:

- Q&A / decision clarification;
- target focus / anti-drift / anti-overengineering;
- minimalism / avoiding overcorrection;
- iterative and context work;
- REI impact/evidence/risk scoring;
- Macro–Meso–Micro;
- context bloat;
- research and output evaluation;
- exact-match patch format and patch application behavior.

The operator also supplied an uploaded working copy with an `adaptive_informatics` snippet. Compare it to the repository file if relevant; do not silently merge differences.

### B. Canonical Informatics architecture

Start at:

`apex-meta/informatics/index.md`

Then use only needed parts of:

`apex-meta/informatics/standard.md`

The current design already defines this progressive-disclosure hierarchy:

```text
small always-on control
  → scoped instructions
    → task-triggered Skills
      → indexed knowledge
        → evidence / raw / history (JIT only)
```

Do not invent a competing information architecture unless research demonstrates a material deficiency.

### C. Existing MMM candidate module

`apex-meta/informatics/MMM/index.md`
`apex-meta/informatics/MMM/working-method.md`
`apex-meta/informatics/MMM/established-concepts.md`

MMM is already a candidate **working/reasoning orientation**, separate from Plan-Sync-Session and state management.

Current shorthand:

```text
Macro → Meso → Micro → Meso → Macro
```

Current established basis:

- hierarchical systems engineering;
- V-model / Vee;
- requirements decomposition / flowdown;
- integration;
- verification;
- validation;
- recursive decomposition;
- progressive / just-in-time context.

Do not create a second MMM definition. Evaluate and refine the existing candidate only if evidence warrants it.

### D. Anti-overengineering source-path mismatch

The operator referenced:

`apex-meta/AI-Snippets/SnippetDocs/AnitOverEng.md`

At handover creation time, this path was not found on `main`, and the visible `apex-meta/AI-Snippets/` directory did not contain `SnippetDocs/`.

Do not treat this as a blocker. Search by filename/content. If still absent, use the anti-overengineering material in `Snippets.md` as the current source and record the path mismatch.

---

# 3. Preliminary external architecture findings — hypotheses to verify

These are starting points, not locked decisions.

## 3.1 AGENTS.md — portable root instruction surface for coding agents

`AGENTS.md` is now an open, cross-agent format intended as a predictable "README for agents". It supports root and nested instruction scoping across a broad coding-agent ecosystem.

Starting source:

- https://agents.md/

**Usefulness:** strong candidate for the *runtime adapter / always-on instruction surface* in repositories.

**Limit:** it is primarily a coding-agent/repository convention, not a universal format for every conversational AI. Therefore distinguish **portable semantic content** from **runtime-specific delivery adapters**.

## 3.2 Agent Skills — progressive disclosure and reusable procedures

Agent Skills are an open standard for folders containing a concise `SKILL.md` plus focused references/assets. The architecture explicitly uses progressive disclosure:

1. small metadata/description;
2. full Skill body when relevant;
3. additional referenced files only when needed.

Starting sources:

- https://agentskills.io/specification
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

**Usefulness:** strong candidate for how deeper behavior methods should be packaged when a runtime supports Skills or filesystem references.

**Limit:** not every AI product natively resolves Agent Skills. The canonical instruction content must still be portable as ordinary text/Markdown.

## 3.3 Context engineering — smallest high-signal context

Anthropic's current context-engineering guidance explicitly treats context as a finite resource and recommends the smallest high-signal token set, just-in-time retrieval, compaction, structured notes/memory, and context isolation where appropriate.

Starting source:

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**Usefulness:** likely external basis for the operator's context-management/context-bloat module.

## 3.4 Building Effective Agents — complexity should earn itself

Anthropic distinguishes fixed **workflows** from model-directed **agents**, recommends the simplest solution that works, and documents reusable patterns:

- direct/single-call solutions;
- prompt chaining;
- routing;
- parallelization;
- orchestrator-workers;
- evaluator-optimizer;
- agent loops.

Starting source:

- https://www.anthropic.com/engineering/building-effective-agents

**Usefulness:** strong candidate basis for adaptive workflow/complexity routing and for anti-overengineering.

## 3.5 GitHub Spec Kit — specification/clarification/planning as explicit artifacts

GitHub Spec Kit currently exposes an agentic specification-driven flow including:

```text
constitution → specify → clarify → plan → checklist → tasks → analyze → implement → converge
```

It also supports scoped implementation for large work and a "spec-of-specs" pattern when one feature would exceed a manageable context.

Starting sources:

- https://github.com/github/spec-kit
- https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md
- https://github.com/github/spec-kit/blob/main/docs/concepts/spec-of-specs.md

**Usefulness:** useful research input for understanding recap, requirements clarification, complexity scaling, specification consistency, output contracts, and convergence.

**Limit:** it is a software-development system. Do not blindly generalize its full artifact workflow to ordinary AI interaction.

---

# 4. Architecture question to solve first

Before authoring any behavior module, determine the best universal layering model.

Evaluate at least these candidates:

## Candidate A — root snippets + reference Markdown

```text
portable instruction paragraph
→ linked focused Markdown method
→ linked evidence/examples
```

Pros: works almost everywhere.

Risk: weak automatic discovery in runtimes without filesystem conventions.

## Candidate B — AGENTS/custom instruction adapter + Agent Skills

```text
runtime root instruction
→ skill trigger/description
→ SKILL.md
→ references/
```

Pros: established progressive-disclosure pattern.

Risk: runtime support varies; repository-oriented.

## Candidate C — canonical portable behavior bundle + thin runtime adapters

```text
canonical behavior modules
        ↓
short portable snippets
        ↓
adapters: AGENTS.md / CLAUDE.md / system prompt / custom instructions / Skills
```

Pros: separates semantic authority from tool-specific delivery.

Risk: needs clean ownership/routing to avoid adapter drift.

Do not select a candidate by intuition. Research current cross-agent support and test the model against the operator's "any AI" requirement.

---

# 5. Provisional behavior-module map

Treat this as a research backlog, not final taxonomy. Merge, split, rename, or reject modules when established vocabulary suggests a cleaner structure.

| ID | Working module | Operator need | Existing candidate vocabulary / research anchors | Current source |
|---|---|---|---|---|
| M01 | **Understanding & Intent Alignment** | Before nontrivial execution, show what the AI understood and where it will go. | requirements elicitation, specification, clarification, backbrief/brief-back, task contract, closed-loop communication, Spec Kit `specify`/`clarify` | operator prompt |
| M02 | **Iterative Hierarchical Realization (MMM)** | Top-down purpose→architecture→detail, then bottom-up verification/validation; recurse when needed. | hierarchical systems engineering, V-model/Vee, requirements flowdown, verification, validation, recursive decomposition | `informatics/MMM/` |
| M03 | **Context Management** | Avoid bloat; load only relevant material; preserve long-horizon coherence. | context engineering, progressive disclosure, JIT retrieval, compaction, structured notes/memory, context isolation | Informatics + operator prompt |
| M04 | **Workflow & Complexity Routing** | Use a direct path for easy tasks and stronger iterative workflows only when complexity warrants them. | workflow vs agent, prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer | `Snippets.md` + Anthropic patterns |
| M05 | **Reasoning, Review & Verification** | Improve decision quality without demanding opaque or excessive internal reasoning. | plan-act-observe, evaluator-optimizer, reflection/self-review, verification, test/evidence loops | operator prompt |
| M06 | **Q&A / Decision Elicitation** | Nail understanding and material choices through structured questions/options/recommendations. | requirements elicitation, trade study, MCDA/decision matrix, ADR/RFC decision records, uncertainty/risk communication | `Snippets.md` |
| M07 | **Target / Value / Anti-Drift / Anti-Overengineering** | Keep work tied to the actual outcome; resist infrastructure/process drift and overcorrection. | simplicity-first, YAGNI, KISS, Lean value, vertical slices, tracer bullets, evidence proportionality | `Snippets.md` |
| M08 | **Research & Evidence Discipline** | Use authoritative, current, sufficient evidence; distinguish evidence from inference. | evidence hierarchy, source authority, triangulation, provenance, confidence/uncertainty, freshness | `Snippets.md` research section + Informatics |
| M09 | **Output / Deliverable Contract** | Make the requested deliverable, format, rough content structure, acceptance criteria, and dependencies explicit. | output contracts, Definition of Done, acceptance criteria, specification artifacts, structured outputs | operator prompt |
| M10 | **Change / Patch Execution** | Safe deterministic file-edit format where exact mutation matters. | patch/diff workflows, exact-match transforms, transaction-like validation | `Snippets.md` |

### Important scope note

M10 is probably **not universal interaction behavior**. It may remain a task-specific execution Skill. The orchestrator must classify which topics belong in the universal behavioral layer versus domain/task procedures.

---

# 6. Required discovery: what is missing?

The operator explicitly asked what else makes agents work efficiently.

Research whether a universal interaction set materially benefits from additional independent modules such as:

- ambiguity thresholds / when to ask versus infer;
- source and authority resolution;
- permissions / irreversible-action confirmation;
- error recovery and stop conditions;
- communication cadence / progress updates;
- evaluation / success measurement;
- state and handoff continuity across sessions;
- tool-use discipline;
- disagreement / challenge behavior;
- uncertainty calibration;
- prioritization / dependency ordering;
- parallel versus sequential work;
- memory/personal-preference handling.

Do **not** add a module merely because literature names it. Include it only when it addresses a recurring operator/agent failure mode that is not already owned elsewhere.

---

# 7. Special research requirement — Understanding Recap

This is a high-priority module.

The operator wants a nontrivial prompt to produce a concise structured recap **before execution**, roughly covering:

```text
Target / intended outcome
Inputs / guidance / evidence
Scope / non-scope
Subtargets / subproblems
Sources / files / systems to use
Dependencies / interconnections
Proposed iterative process
Expected output format
Rough output/content structure
Material assumptions / ambiguities
First active step
```

Research whether this maps best to one or more established concepts such as:

- requirements elicitation;
- task specification;
- briefing/backbriefing;
- closed-loop communication;
- implementation plan preview;
- acceptance-contract confirmation;
- Spec Kit `specify` + `clarify` + `plan`;
- another well-supported human-AI interaction pattern.

### Constraints

- Do not force the recap on trivial/obvious requests.
- Do not make it a permission gate by default.
- Do not expand it into a full plan when a 5–10 line recap is sufficient.
- It should expose **understanding and intended execution**, not hidden chain-of-thought.
- It should make misunderstandings cheap to catch before expensive work begins.

---

# 8. Special research requirement — reasoning

The current `Snippets.md` research template explicitly requests a "CoT Scratchpad".

Do **not** automatically preserve this.

Research robust, inspectable alternatives that work across AI products:

- concise plan;
- assumptions;
- evidence;
- decision rationale;
- intermediate artifacts;
- verification criteria;
- critique/evaluation pass;
- confidence/uncertainty.

The target is **better reasoning performance and auditability**, not access to private hidden reasoning tokens.

Determine what belongs in the user-visible contract and what should remain implementation-internal.

---

# 9. Special research requirement — Q&A and REI

Current operator Q&A preference:

```text
Question
Options
Grounding / practical example
Impact / Evidence / Risk estimates
Recommendation
Reasoning
Rejection notes
```

Current score syntax:

```text
(I90/E95/R20: 77)
```

Treat both the format and the REI formula as **candidate local mechanisms**.

Research established equivalents first:

- trade studies;
- multi-criteria decision analysis (MCDA);
- weighted decision matrices;
- risk-adjusted prioritization;
- confidence/evidence scoring;
- ADR/RFC-style decision recording;
- requirements elicitation question patterns.

Determine whether REI has enough value to retain, should be mathematically corrected, should be renamed as a local heuristic, or should be replaced by a more established method.

Do not imply pseudo-precision when scores are subjective.

---

# 10. Special research requirement — target/value/anti-overengineering

Preserve the operator's core intent:

> Optimize for the shortest credible path to the actual user-facing target. Process, architecture, checks, schemas, provenance, wrappers, and infrastructure must justify themselves through value, risk reduction, or necessary evidence.

Research established language that makes this immediately legible to agents, including where appropriate:

- simplicity-first;
- YAGNI;
- KISS;
- Lean value / waste;
- vertical slicing;
- tracer-bullet / walking-skeleton approaches;
- Theory of Constraints / bottleneck focus;
- evidence proportionality / risk-based assurance.

Retain the operator-specific challenge rule if it remains useful:

> When the operator proposes a correction, ask whether it must be fixed before the actual target can be tested.

But test whether this belongs in the universal snippet, a deeper operator-preference reference, or only particular product-building contexts.

---

# 11. Child-handover contract

After the architecture and module map are approved by evidence, create **one handover per selected module** for fresh AI contexts.

Each child handover must be bounded to one module and include:

## A. Purpose

One sentence describing the behavior being standardized.

## B. Operator intent

Only the relevant preferences and examples for that module.

## C. Existing repo sources

List only files needed for that module.

## D. Research questions

What external vocabulary/methods/standards must be compared.

## E. Source policy

- Prefer official/current sources and primary research.
- Distinguish formal standards, established methods, vendor practice, empirical research, and local recommendation.
- Do not elevate an Apex-local term into an industry standard.

## F. Required outputs

Every module AI should produce, at minimum:

1. **Established-concept map** — operator intent → known terminology/methods.
2. **Candidate comparison** — 2–5 viable formulations, with trade-offs.
3. **Recommended short snippet** — usually 1–4 sentences, self-sufficient.
4. **Trigger/depth rule** — when deeper guidance should be loaded.
5. **Focused explanation/method file** — concise; no encyclopedia.
6. **Failure modes / mistakes** — recurrent misunderstandings the instruction guards against.
7. **Examples** — simple, medium, and complex where relevant.
8. **Evaluation prompts** — test whether the instruction improves behavior and whether it causes over-processing.
9. **Dependencies/overlap** — explicit boundaries with other modules.
10. **Integration proposal** — where canonical content should live and which adapters should only point to it.

## G. No live propagation

Do not patch root agent instructions from the child module run.

First test the module independently. Integration happens only after cross-module synthesis.

---

# 12. Required orchestrator outputs

Create a dedicated result folder such as:

`apex-meta/handoff/universal-ai-instruction-system/`

Use the current Informatics rules for structure, but do not overproduce artifacts.

Minimum outputs:

## 12.1 `00-ARCHITECTURE-DECISION.md`

Answer:

- What is the canonical semantic layer?
- What is the always-on layer?
- What is the deeper method layer?
- How do runtime adapters work?
- How does this remain portable beyond coding agents?
- How does progressive disclosure work when the AI cannot directly read linked files?

## 12.2 `01-MODULE-MAP.md`

For every candidate module:

```text
name
purpose
universal vs task-specific
established vocabulary
current owner/source
proposed canonical owner
trigger
likely snippet size
deeper reference need
dependencies
overlap/conflict
status: keep / merge / split / reject / research
```

## 12.3 `02-GLOBAL-SNIPPET-GRAMMAR.md`

Research and propose a consistent form for short instructions.

Do not force XML/YAML unless evidence shows it materially helps portability.

A candidate structure to test, not assume:

```text
[Behavior name]
Core rule in 1–3 direct sentences.
If <condition requiring sophistication>, use <canonical method/reference>.
```

## 12.4 `03-EVALUATION-PLAN.md`

Design cross-model tests for:

- simple request: no unnecessary ceremony;
- ambiguous request: correct understanding recap/clarification;
- medium multi-part task: appropriate decomposition;
- large context-heavy task: JIT context and bounded iteration;
- research request: evidence/freshness/source quality;
- product task: target/value dominates process;
- decision request: useful Q&A without pseudo-precision;
- conflicting instructions: correct authority/routing;
- failure recovery: no runaway framework-building.

## 12.5 `handoffs/`

One child handover per selected module.

Do not let child handovers preload the whole universal-instruction program. Give each one only:

- module mission;
- relevant operator intent;
- relevant repository files;
- shared architecture decision;
- specific research/output contract.

---

# 13. Research quality rules

1. **Do not search for a single magical framework.** The final system may legitimately compose several established concepts.
2. **Do not create new jargon when an established term works.**
3. **Do not claim universality from one vendor's implementation.**
4. **Do not confuse delivery format with behavioral method.** `AGENTS.md` and Agent Skills are delivery mechanisms; MMM, context engineering, and decision methods are behavioral concepts.
5. **Do not let an instruction module duplicate Informatics.** Informatics owns information architecture/serialization/context routing conventions.
6. **Do not let MMM become project management.** MMM owns hierarchical reasoning/realization, not durable task-state mutation.
7. **Do not let workflow selection become mandatory ceremony.** Complexity must justify extra steps.
8. **Do not preserve current snippets merely because they exist.** Treat them as operator requirements/examples to be translated into better-supported language.
9. **Do not require hidden chain-of-thought.** Prefer observable plans, rationale, evidence, artifacts, and checks.
10. **Test instruction interference.** A individually sensible rule can degrade performance when combined with nine others.

---

# 14. Current working hypothesis

The likely target architecture is:

```text
CANONICAL PORTABLE BEHAVIOR MODULES
│
├── Informatics                 [existing]
├── Understanding / Preflight   [research]
├── MMM                         [existing candidate]
├── Context Engineering         [research]
├── Workflow Selection          [research]
├── Reasoning / Verification    [research]
├── Q&A / Decision Elicitation  [research]
├── Target / Anti-Drift         [research]
├── Research / Evidence         [research]
└── Output Contract             [research]

        ↓ each exports

VERY SHORT SELF-SUFFICIENT SNIPPET
        ↓ when needed
FOCUSED METHOD / SKILL / REFERENCE
        ↓ when needed
EXAMPLES / FAILURES / EVIDENCE / EVALS

        ↓ delivered through thin adapters

AGENTS.md | CLAUDE.md | custom instructions | system prompt | Agent Skills | other runtime adapters
```

This is a **hypothesis to validate**, not permission to implement it as-is.

---

# 15. Preliminary acceptance criteria

The eventual system should pass all of these:

- A new AI can understand the essential operator behavior from the short snippets alone.
- A simple request does not trigger a process-heavy workflow.
- A complex task can discover deeper guidance without preloading unrelated modules.
- The same semantic rule is not duplicated across multiple canonical files.
- Established vocabulary explains most concepts without Apex-specific interpretation.
- Runtime-specific adapters do not become independent policy owners.
- The Understanding Recap catches meaningful misunderstandings before execution without becoming a default approval gate.
- MMM remains a lightweight reasoning/realization method, not a project-state framework.
- Context-management behavior demonstrably reduces irrelevant loading and context pollution.
- Anti-overengineering guidance stops process/infrastructure drift without suppressing necessary architecture or safety work.
- Q&A improves decisions without inventing false numerical certainty.
- Research behavior distinguishes evidence, inference, uncertainty, and freshness.
- Combined instructions remain short enough for practical always-on use.

---

# 16. Stop condition for this orchestrator run

Stop after all of the following exist:

1. evidence-backed general architecture decision;
2. validated module taxonomy;
3. proposed short-snippet grammar;
4. cross-module evaluation plan;
5. one bounded handover for every selected module.

Do **not** author the final universal `AGENTS.md` / system prompt.

Do **not** propagate snippets globally.

Do **not** redesign Plan-Sync-Session or orchestration topology.

Those are downstream integration decisions after the modules have been independently researched and tested.
