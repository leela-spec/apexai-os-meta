---
type: ExecutionHandover
title: Universal AI Instruction System — Module Deepening Handover
description: Reusable one-module-at-a-time research and design contract for refining the compact agent XML and its justified deeper method.
status: active_reusable_handover
updated: 2026-09-04
---

# Universal AI Instruction System — Module Deepening Handover

## Role

You are the independent research-and-design orchestrator for **one behavior module** of the Universal AI Instruction System.

Repository: `leela-spec/apexai-os-meta`
Branch: `main`
Program root: `apex-meta/handoff/universal-ai-instruction-system/`

Your job is not to redesign the whole instruction architecture. Your job is to take the one module currently marked `NEXT` in the live README, research it deeply, test its semantics and wording, decide the smallest correct deeper owner, update the pilot module if justified, persist the module result, advance the program status by one row, commit, and stop.

## Authority and startup

Read these live files first and in this order:

1. `apex-meta/handoff/universal-ai-instruction-system/README.md`
2. `apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
3. the operator-source material or supporting audit only when needed:
   - `apex-meta/handoff/universal-ai-instruction-system/07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md`
   - `apex-meta/AI-Snippets/Snippets.md`

The README is current truth for architecture, module identity, sequence, output shape, and stop conditions.

Do not reconstruct current state from older research files. Do not import an older module taxonomy when it conflicts with the live README.

## Fixed architecture — do not reopen by default

The program has already decided:

```text
small always-loaded agent contract
  -> compact embedded module
  -> conditional/path/semantic activation where relevant
  -> focused method or Agent Skill only when justified
  -> deeper references/examples/scripts/evidence JIT
```

The compact XML belongs **inside the always-loaded agent file**. A deeper reference or Skill is additional method support, not a replacement for the root rule.

XML is the current pilot representation, not a parser dependency and not a separate policy authority.

Each compact module uses the pattern:

```text
established concept name(s)
+ one short local semantic rule
+ optional trigger / deepen_when / ref
```

Do not install or propagate candidate modules into live runtime instruction files during this program.

## Execution mode

**One run = one module.**

1. Read `README.md`.
2. Select exactly the row marked `NEXT`.
3. Research and complete that module only.
4. Update the module's current block in `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` only if the evidence supports a change.
5. Write the module result under `module-deepening/<ID>-<slug>/`.
6. Mark the completed row `DONE` and the next queued row `NEXT` in `README.md`.
7. Commit the bounded result to `main`.
8. Stop.

Do not continue into the next module unless the operator explicitly overrides the one-module-per-run rule.

## Core research question

For the selected module answer:

> What is the best evidence-backed, token-efficient way to make an AI agent reliably exhibit this behavior, using established concepts and proven methods, while keeping the always-loaded rule tiny and loading deeper guidance only when necessary?

## Research requirements

### A. Establish the underlying discipline

Find the established concept(s) that genuinely match the target behavior.

Search outside prompt-engineering vocabulary when appropriate. Depending on the module this may include:

- requirements engineering;
- systems engineering;
- V-model / verification & validation;
- Lean / KISS / YAGNI / reuse practice;
- context engineering / progressive disclosure;
- decision analysis / trade studies / MCDA;
- evidence-based practice / provenance / uncertainty calibration;
- incident management / graceful degradation / escalation;
- technical communication / information design;
- source-of-truth / configuration-management practice.

Do not invent a local term when an established one already covers the behavior.

### B. Find existing proven agent implementations

Research how mature agent systems already express or operationalize the same behavior.

Prioritize current primary documentation and proven systems such as relevant parts of:

- AGENTS.md conventions;
- Agent Skills;
- Claude Code instructions/rules/Skills;
- OpenAI Codex/agent guidance where public;
- Cursor rules/Skills;
- Windsurf rules/Skills;
- Kiro steering/Skills;
- Gemini CLI context/rules;
- GitHub Copilot instructions;
- other mature frameworks only when they add distinct evidence.

The target is not a vendor feature survey. Extract the patterns that matter to this one module.

### C. Compare alternatives

Where more than one legitimate method exists, compare them.

For each viable alternative capture:

- mechanism;
- evidence/maturity;
- token/context cost;
- activation reliability;
- likely failure mode;
- portability across agents;
- whether it fits an always-on rule, Skill, scoped rule, reference, or no deeper artifact.

Reject alternatives explicitly when they are too vague, too heavy, too runtime-specific, or duplicate another module.

### D. Test the current pilot wording

Treat the current XML block as a hypothesis.

Ask:

- Does it name the right established concepts?
- Is the local rule precise enough to disambiguate those concepts?
- Is it too broad or too narrow?
- Could it create unwanted ceremony on simple tasks?
- Does it overlap another module?
- Does it need `when`, `deepen_when`, or `ref`?
- Does a referenced method actually need to exist?
- Can the wording be shorter without losing the behavior?
- Would equivalent compact Markdown behave as well or better?

Produce 2–4 materially different wording candidates before selecting the final one when there is a real wording trade-off. Do not manufacture variants that differ only cosmetically.

## Deeper-owner decision

Do not assume every module needs a Skill.

Choose exactly one primary deeper owner:

| Owner | Use when |
|---|---|
| **No deeper artifact** | the root semantic rule is sufficient and no reusable procedure is needed |
| **Focused reference** | the module mainly needs definitions, boundaries, examples, failure modes, or conceptual guidance |
| **Scoped rule** | applicability can be determined reliably by file/path/subsystem |
| **Agent Skill** | there is a reusable multi-step method/checklist with a recognizable semantic task trigger |

A Skill is preferred only when it provides useful executable method, not merely because Skills support progressive disclosure.

If `Agent Skill` wins, the candidate must follow current Agent Skills best practice:

- concise `name` and activation-oriented `description`;
- focused `SKILL.md` body;
- no duplicated root rule;
- references only when needed;
- references remain shallow and purposeful;
- procedure is usable without loading unrelated background;
- explicit stop/output behavior when the method needs it.

Keep any candidate Skill under the research module folder. Do **not** place it in runtime skill discovery paths yet.

## Required module result

Create:

`apex-meta/handoff/universal-ai-instruction-system/module-deepening/<ID>-<slug>/README.md`

This file is the single current result for that module and must contain:

### 1. Final decision

- module ID / XML tag;
- semantic purpose;
- final root XML block;
- equivalent compact Markdown control;
- selected deeper owner;
- selected established principles/methods.

### 2. Why this is the right method

Dense synthesis of the strongest external evidence and proven implementations.

Separate:

- underlying discipline evidence;
- agent-delivery/loading evidence;
- local inference/decision.

### 3. Semantic contract

Define:

- MUST behavior;
- MUST NOT behavior;
- activation condition if conditional;
- deepen condition if applicable;
- interaction with neighboring modules;
- common misinterpretations;
- known failure modes.

### 4. Deep method

Write the actual deeper guidance another agent would need when the module deepens.

Do not stop at an outline such as “create a Skill later.” If deeper guidance is justified, specify it now.

If the deeper owner is a Skill, additionally create:

`module-deepening/<ID>-<slug>/SKILL.md`

If a separate focused reference is genuinely necessary, create:

`module-deepening/<ID>-<slug>/REFERENCE.md`

Avoid both unless both have distinct jobs.

### 5. Scenario simulations

At minimum test:

1. simple/negative case;
2. clear positive case;
3. ambiguous case;
4. conflict/edge case;
5. the failure mode the module is meant to prevent.

For each record:

- scenario/input;
- current-pilot expected behavior;
- candidate expected behavior;
- observable success/failure criteria;
- whether deep guidance should activate;
- concise rationale.

Do not request or fabricate hidden chain-of-thought. Use observable behavior and concise decision rationale.

When practical, include one XML-vs-Markdown comparison scenario.

### 6. Alternatives rejected

List the important alternatives and why they lost.

### 7. Sources

Use current primary/authoritative sources. Include publication/update context where freshness matters.

## Wording acceptance criteria

The final root module should pass all applicable checks:

- **Self-sufficient:** an agent can act reasonably without opening the reference.
- **Small:** one behavior, typically one short semantic rule.
- **Established:** uses recognized concepts where they improve meaning.
- **Disambiguated:** principle names are not left to interpretation alone.
- **Non-ceremonial:** does not force a complex process onto simple work.
- **Non-duplicative:** does not restate another module's job.
- **Routable:** a deep trigger/reference is present only when it adds real value.
- **Portable:** does not depend on one vendor unless the behavior itself is vendor-specific.
- **Testable:** its effect can be observed in scenarios.

## Modification rules

During this run you may modify only:

- the selected module's research folder;
- the selected module block in `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` when evidence supports a change;
- the module status table in `README.md`.

Do not modify:

- live `AGENTS.md`;
- `.claude/CLAUDE.md`;
- `.hermes.md`;
- Cursor/Kiro/Windsurf live rules;
- installed runtime Skills;
- Plan-Sync-Session;
- unrelated modules in the pilot.

If research shows a neighboring module should change, record the dependency in the current module result. Do not edit the neighboring module in this run.

## Git / concurrency behavior

Work on `main` only.

Before committing, re-read the latest `main`. If it moved, preserve upstream changes and replay only this bounded module result. Never force-update `main`.

Commit message format:

`docs(agent-contract): deepen <ID> <module-name>`

## Stop condition

Stop immediately after:

- the one `NEXT` module is fully researched;
- its module result is written;
- any justified candidate Skill/reference is written;
- its pilot XML wording is updated if justified;
- README status advances exactly one module;
- the bounded commit is on `main`.

Report:

- module completed;
- final XML wording;
- deeper owner chosen;
- files created/updated;
- commit SHA;
- next module now marked `NEXT`.

Do not start the next module.