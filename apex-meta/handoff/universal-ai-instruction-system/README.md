---
type: ProgramIndex
title: Universal AI Instruction System — Current Truth
description: Live continuation map for module-by-module research, wording, simulation, and deeper-method design of the compact agent contract.
status: module_deepening_active
updated: 2026-09-07
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
- **Remaining module research is AI-native first:** research current OpenAI / ChatGPT / Codex model and product guidance first when relevant, then independent mature-agent convergence, then established external disciplines for durable concepts. Formal older methodology must not outrank current measured agent behavior merely because its vocabulary is more established.
- A01 `<target>` owns both **intent-preserving realization and substantive completion validation**. Files, tests, checklists, schemas, and metrics are evidence of success, not substitutes for the requested useful outcome. The former standalone A09 `<verification>` module is merged into A01 and removed from the universal module set.
- A03 `<reuse>` owns **battle-proven reuse and minimal adaptation before invention**. Prefer established solutions in their proven form, preserve their tested architecture where fit, and restrict custom work to verified gaps or unavoidable project-specific adaptation surfaces. Researching an existing system merely as inspiration for a new local imitation does not satisfy A03.
- A13 `<grounding>` owns **external grounding and real-world verification**. When a material decision depends on real-world facts, capabilities, methods, integrations, standards, maturity, or reliability, model reasoning alone is insufficient: verify against sufficiently current authoritative external evidence and, where feasible, direct observed behavior or tests. A08 governs the quality of evidence; C02 governs deeper research methodology.
- Proven elsewhere does not automatically mean fit here. Reused systems and components must still be validated against the actual target, constraints, and operating environment.
- Do not install or propagate candidate Skills or rewrite live root agent instructions during this module-deepening program.
- Do not reopen the overall architecture unless new evidence directly falsifies a locked decision.

## Active files

Use these as the live continuation surface:

1. `README.md` — current truth, module status, locked decisions.
2. `09-MODULE-DEEPENING-HANDOVER.md` — reusable execution contract for a fresh chat, including the authoritative AI-native-first evidence order.
3. `10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md` — retroactive audit of completed A01-A05 plus pending semantic patch proposals. Its proposed wording is not live until explicitly applied.
4. `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` — current non-active XML pilot whose individual module wording is refined by this program.
5. `07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md` — supporting audit/evidence when a module needs prior repo findings.
6. `apex-meta/AI-Snippets/Snippets.md` — operator-originated source ideas when provenance is needed.

Other files in this research folder are background evidence, not active execution instructions. Do not import older taxonomies or superseded wording into new module results.

## Current module set

Each fresh run handles exactly one module: the row marked `NEXT`.

| ID | XML tag | Current role | Status |
|---|---|---|---|
| A01 | `<target>` | Intent-Preserving Target Realization & Validation | **DONE** |
| A02 | `<scope>` | Scope & Non-goals | **DONE** |
| A03 | `<reuse>` | Battle-Proven Reuse & Minimal Adaptation Before Invention | **DONE** |
| A04 | `<workflow>` | Complexity-Adaptive Workflow | **DONE** |
| A05 | `<intent>` | Intent Alignment / Clarification Threshold | **DONE** |
| A06 | `<context>` | Context Engineering / Progressive Disclosure | **DONE** |
| A07 | `<realization>` | Hierarchical Realization & Verification/Validation | **DONE** |
| A08 | `<evidence>` | Evidence & Uncertainty Discipline | **DONE** |
| A10 | `<recovery>` | Error Recovery & Escalation | **DONE** |
| A11 | `<current_truth>` | Current-Truth / Single-Source Discipline | **DONE** |
| A12 | `<communication>` | Communication Economy | **NEXT** |
| A13 | `<grounding>` | External Grounding & Real-World Verification | QUEUED |
| C01 | `<decision>` | Conditional Decision / Trade-off Discipline | QUEUED |
| C02 | `<research>` | Conditional Research Discipline | QUEUED |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | QUEUED |

`A*` modules are candidates for the always-on universal constitution. `C*` modules remain embedded conditional modules: their trigger is visible, but their deeper method is activated only when relevant.

## Required result for each module

A module is not complete merely because its XML sentence sounds good. A completed module must establish:

1. **Current AI-native grounding** — what current OpenAI / ChatGPT / Codex guidance says about the behavior when relevant, including model-specific changes, measured findings, and current prompt/context/autonomy patterns.
2. **Independent agent convergence** — how other mature agent systems express or operationalize the behavior, separating genuine convergence from vendor-specific mechanics.
3. **Established external grounding** — the durable concepts, methods, vocabulary, or failure modes from older disciplines that still add value after the AI-native evidence is understood.
4. **Semantic boundary** — what the module means, when it applies, when it must not apply, and its failure modes.
5. **Root wording** — the final compact XML block for the current pilot, plus a compact Markdown equivalent used as a control.
6. **Deepening decision/method** — Skill vs reference vs scoped rule vs no deeper artifact, with evidence-based rationale; if deeper guidance is justified, write the actual candidate method content, not merely an outline.
7. **Scenario evaluation** — run bounded simulations covering correct activation, non-activation, ambiguity, conflict/edge cases, and a known failure mode.
8. **Evidence record** — current primary/authoritative AI sources first, independent agent sources second, external-discipline sources third, plus important uncertainty.

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

Research in this order:

1. **Current AI-native primary evidence first.** Start with current OpenAI / ChatGPT / Codex model and product guidance when relevant to the module. Capture model-behavior changes, prompting/instruction guidance, autonomy/approval boundaries, context architecture, Skills/plugins/subagents/tool patterns, production-agent experience, and measured evaluation findings that materially bear on the behavior.
2. **Cross-agent convergence second.** Check at least two independent mature agent systems when practical (for example Claude/Claude Code, GitHub Copilot, Gemini CLI, Kiro, Cursor, Windsurf). Distinguish portable behavioral convergence from vendor-specific product mechanics.
3. **Established external disciplines third.** Use systems engineering, requirements engineering, Lean, project management, V&V, decision analysis, incident management, or other mature fields only after the current AI evidence is understood. Use them for durable vocabulary, methods, and failure modes; do not let formality override current measured model behavior.
4. **Local synthesis last.** Invent local methodology only where the preceding evidence leaves a genuine gap.

Additional requirements:

- Treat current model behavior as time-sensitive. Verify current official primary guidance rather than carrying forward prompt scaffolding designed for older models.
- Prefer documented production experience, measured evaluations, and observed failure modes over generic prompting folklore.
- Find established vocabulary where it improves precision, but do not optimize the module around terminology alone.
- Compare multiple viable methods where real alternatives exist.
- Defend the always-on context budget: every root instruction must earn its token cost through material behavioral value.
- Treat the existing XML wording as a hypothesis to test, not wording to defend.
- Explicitly test whether a rule over-triggers, creates unnecessary approvals/ceremony, duplicates current model capability, or suppresses useful autonomy.
- Do not request or record hidden chain-of-thought. Use concise observable rationale, comparison tables, and scenario traces instead.

### Research-profile alternatives retained for evaluation

The AI-native-first order above is the **current default candidate**, not proof that evidence order itself should never be tested. Preserve the prior discipline-first style as an explicit comparator rather than silently deleting it from the program's conceptual history.

#### Profile A — AI-native-first

```text
current OpenAI / ChatGPT / Codex evidence
  -> independent mature-agent convergence
  -> established external discipline
  -> local synthesis
```

Use when the immediate question is how current agents should actually behave, especially where model capabilities, prompt sensitivity, context architecture, autonomy, tool use, Skills/plugins, or over-triggering may have changed recently.

#### Profile B — discipline-first comparator

```text
established external discipline / vocabulary
  -> mature agent implementations
  -> current AI-specific adaptation
  -> local synthesis
```

Retain as a comparison profile when durable domain methodology may reveal requirements, failure modes, or trade-offs that product guidance under-specifies. Do **not** treat formality or age as evidence that Profile B is superior.

#### Comparison rule

When evidence-order itself is under evaluation, run the same module/scenarios under both profiles and compare resulting behavior, wording, context cost, omissions, over-triggering, and portability. Do not silently blend the profiles and then attribute the result to either one.

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

That synthesis must explicitly defend the **always-on context budget**: an individually reasonable module does not automatically deserve permanent inclusion. Test merges/deletions, compare the full constitution with a smaller control prompt on representative tasks, and retain only rules whose observed behavioral value justifies their persistent token/context cost.
