---
type: ProgramIndex
title: Universal AI Instruction System — Current Truth
description: Live continuation map for module-by-module research, wording, simulation, and deeper-method design of the compact agent contract.
status: module_deepening_active
updated: 2026-09-04
---

# Universal AI Instruction System — Current Truth

## Mission

Create a small, token-efficient operating contract that can sit directly inside `AGENTS.md` or an equivalent always-loaded agent file. The contract names high-value principles, gives each one a short local behavioral rule, and loads deeper methods only when a task genuinely needs them.

The goal is **not** to invent a new agent framework. Reuse established agent-instruction and progressive-disclosure patterns, and reuse proven methods for each behavior module before creating custom methodology.

## Locked architecture

```text
always-loaded agent file
  -> compact embedded behavior modules
  -> conditional/path/semantic routing when relevant
  -> focused method or Agent Skill when justified
  -> deeper references/examples/scripts/evidence only when needed
```

Locked decisions:

- `AGENTS.md`-style root instructions are the preferred cross-agent carrier where supported.
- Compact XML inside the Markdown carrier is the current pilot representation. XML is prompt structure, not a parser-dependent or separate policy system.
- The XML module itself stays in the always-loaded agent file. A `ref` is a JIT pointer, not an import directive.
- Principle names alone are insufficient. Each module keeps: **established concept name(s) + one short local semantic rule + optional trigger/ref**.
- The always-loaded surface must remain small. Full procedures, examples, evidence, and edge cases do not belong in the root contract.
- A deeper module does **not automatically become a Skill**. Choose the smallest correct owner:
  - reusable procedure with a recognizable task trigger -> candidate Agent Skill;
  - conceptual guidance or explanation -> focused reference;
  - deterministic file/path relevance -> scoped rule;
  - no additional method needed -> no deeper artifact.
- A01 `<target>` owns both **intent-preserving realization and substantive completion validation**. Files, tests, checklists, schemas, and metrics are evidence of success, not substitutes for the requested useful outcome. The former standalone A09 `<verification>` module is merged into A01 and removed from the universal module set.
- Do not install or propagate candidate Skills or rewrite live root agent instructions during this module-deepening program.
- Do not reopen the overall architecture unless new evidence directly falsifies a locked decision.

## Active files

Use these as the live continuation surface:

1. `README.md` — current truth, module status, locked decisions.
2. `09-MODULE-DEEPENING-HANDOVER.md` — reusable execution contract for a fresh chat.
3. `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` — current non-active XML pilot whose individual module wording is refined by this program.
4. `07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md` — supporting audit/evidence when a module needs prior repo findings.
5. `apex-meta/AI-Snippets/Snippets.md` — operator-originated source ideas when provenance is needed.

Other files in this research folder are background evidence, not active execution instructions. Do not import older taxonomies or superseded wording into new module results.

## Current module set

Each fresh run handles exactly one module: the row marked `NEXT`.

| ID | XML tag | Current role | Status |
|---|---|---|---|
| A01 | `<target>` | Intent-Preserving Target Realization & Validation | **DONE** |
| A02 | `<scope>` | Scope & Non-goals | **NEXT** |
| A03 | `<reuse>` | Reuse Before Invention | QUEUED |
| A04 | `<workflow>` | Complexity-Adaptive Workflow | QUEUED |
| A05 | `<intent>` | Intent Alignment / Clarification Threshold | QUEUED |
| A06 | `<context>` | Context Engineering / Progressive Disclosure | QUEUED |
| A07 | `<realization>` | Hierarchical Realization & Verification/Validation | QUEUED |
| A08 | `<evidence>` | Evidence & Uncertainty Discipline | QUEUED |
| A10 | `<recovery>` | Error Recovery & Escalation | QUEUED |
| A11 | `<current_truth>` | Current-Truth / Single-Source Discipline | QUEUED |
| A12 | `<communication>` | Communication Economy | QUEUED |
| C01 | `<decision>` | Conditional Decision / Trade-off Discipline | QUEUED |
| C02 | `<research>` | Conditional Research Discipline | QUEUED |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | QUEUED |

`A*` modules are candidates for the always-on universal constitution. `C*` modules remain embedded conditional modules: their trigger is visible, but their deeper method is activated only when relevant.

## Required result for each module

A module is not complete merely because its XML sentence sounds good. A completed module must establish:

1. **Established grounding** — the recognized principles/methods that best match the intended behavior.
2. **Existing proven implementations** — how mature agent frameworks, standards, or established disciplines already express or operationalize the behavior.
3. **Semantic boundary** — what the module means, when it applies, when it must not apply, and its failure modes.
4. **Root wording** — the final compact XML block for the current pilot, plus a compact Markdown equivalent used as a control.
5. **Deepening decision** — Skill vs reference vs scoped rule vs no deeper artifact, with evidence-based rationale.
6. **Deep method** — if deeper guidance is justified, write the actual candidate method content, not merely an outline.
7. **Scenario evaluation** — run bounded simulations covering correct activation, non-activation, ambiguity, conflict/edge cases, and a known failure mode.
8. **Evidence record** — primary/authoritative sources and any important uncertainty.

## Module output shape

For each completed module create one compact result folder:

`module-deepening/<ID>-<slug>/`

Required:

- `README.md` — complete module decision, research synthesis, final wording, semantics, simulations, deepening-owner decision, and sources.

Only if the chosen deeper owner is an Agent Skill:

- `SKILL.md` — non-installed candidate Skill. Keep it in this research folder; do not copy it into `.agents/skills/`, `.claude/skills/`, or another runtime discovery path yet.

Only if a separate deeper reference materially improves clarity:

- `REFERENCE.md` — focused candidate reference. Do not create it if the module README already contains the complete useful method.

Avoid extra files unless they add execution value.

## Research standard per module

- Search current official/primary sources first.
- Find established vocabulary before inventing names.
- Compare multiple viable existing methods where the domain has alternatives.
- Prefer battle-tested frameworks and documented practices over custom prompt folklore.
- Distinguish agent-runtime best practice from the underlying discipline itself. Example: a module may use an Agent Skill for delivery while its method comes from systems engineering, requirements engineering, Lean, decision analysis, incident management, or another established field.
- Treat the existing XML wording as a hypothesis to test, not wording to defend.
- Do not request or record hidden chain-of-thought. Use concise observable rationale, comparison tables, and scenario traces instead.

## Evaluation standard per module

At minimum simulate:

1. **Simple / negative case** — module must not create unnecessary ceremony.
2. **Clear positive case** — module should change behavior in the intended way.
3. **Ambiguous case** — verify the trigger/boundary is understandable.
4. **Conflict / edge case** — verify interaction with target, scope, safety, authority, or another module.
5. **Known failure case** — test the failure mode this module exists to prevent.

Record:

- input scenario;
- expected behavior with the candidate module;
- expected behavior without it or with the current wording;
- observable success/failure criteria;
- concise rationale;
- whether the deep reference/Skill should activate.

When practical, compare XML wording with an equivalent compact Markdown form. The goal is behavioral evidence, not proving XML by preference.

## Completion rule for one run

A run is complete only when it has:

1. completed the research and module result for the single `NEXT` module;
2. updated only that module's block in `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` if the evidence supports a wording change;
3. written any justified non-installed candidate `SKILL.md` / `REFERENCE.md`;
4. updated this table: current module -> `DONE`, next queued module -> `NEXT`;
5. committed the bounded result to `main`;
6. stopped.

Do not continue into the next module in the same run by default. A fresh chat should re-read this README and execute the next `NEXT` row using the same handover.

## Program stop condition

After C03 is `DONE`, stop module research. The next phase is a separate cross-module synthesis and controlled agent evaluation before any live `AGENTS.md`, `CLAUDE.md`, Hermes, Cursor, Kiro, Windsurf, or Skill propagation.
