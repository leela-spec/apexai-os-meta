---
type: ContinuationHandover
title: Universal AI Instruction System — A13 + Full Program Continuation Handover
description: Cold-start handover for a fresh chat to execute A13 External Grounding & Real-World Verification and then continue the remaining Universal AI Instruction System program one module at a time without relying on prior conversation context.
status: active_continuation_handover
created: 2026-09-18
repository: leela-spec/apexai-os-meta
branch: main
continuation_base_observed: 42b560f6ea8bec185f8f7f2ea79e0d602a42d243
next_module_observed: A13
---

# Universal AI Instruction System — A13 + Full Program Continuation Handover

## 0. Operator intent

Continue the Universal AI Instruction System from the live repository state.

Immediate next task:

> Deepen **A13 `<grounding>` — External Grounding & Real-World Verification** using the same AI-native-first method used for A06–A12.

Then continue the remaining program **one module per run** until the live README says the module-deepening phase is complete.

This handover is intended to let a fresh chat continue without reconstructing the prior conversation.

Do **not** assume this file is current truth merely because it is detailed. On every fresh run, the live repository state wins.

---

# 1. Repository / branch / execution discipline

Repository:

`leela-spec/apexai-os-meta`

Branch:

`main`

Program root:

`apex-meta/handoff/universal-ai-instruction-system/`

Observed continuation base when this handover was written:

`42b560f6ea8bec185f8f7f2ea79e0d602a42d243`

## Hard Git rules

- work on **main only**;
- do not create branches;
- never force-push / force-update;
- re-read current `main` before writing;
- preserve unrelated concurrent work;
- if `main` moves during the run, replay only the bounded module changes onto the new head;
- prefer one atomic commit per module;
- verify the exact changed paths after commit;
- stop after the one module unless the operator explicitly authorizes continuation.

Preferred commit message:

`docs(agent-contract): deepen <ID> <module-name>`

---

# 2. Startup authority — read in this order

A fresh chat should read these files from live `main` before doing any module work:

1. `apex-meta/handoff/universal-ai-instruction-system/README.md`
   - current truth for module sequence, statuses, architecture, research order, completion rule, and stop condition.

2. `apex-meta/handoff/universal-ai-instruction-system/09-MODULE-DEEPENING-HANDOVER.md`
   - reusable one-module execution contract.

3. `apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md`
   - current non-active XML pilot whose module wording is being refined.

4. `apex-meta/handoff/universal-ai-instruction-system/14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md`
   - important newly added operational candidate for explicit input/source authority/process/output/source-coverage control.
   - **Do not automatically integrate it during A13.** Evaluate its implications where relevant and preserve it for later synthesis / operational integration.

5. `apex-meta/handoff/universal-ai-instruction-system/13-HUMAN-AI-COMPLEX-TASK-EXECUTION.md`
   - current operational companion for turning complex human requests into bounded execution packets.

6. Supporting material only when needed:
   - `10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md`
   - `10-UNIVERSAL-SHORT-RULE-COVERAGE-TODO.md`
   - `11-ONLINE-MODEL-PATCH-HANDOFF-DECISION.md`
   - `12-PENDING-ARCHITECTURE-PATCHES-AUTHORITY-MUTATION.md`
   - `07-TIER-A-COVERAGE-AND-LIVE-AGENT-AUDIT.md`
   - `apex-meta/AI-Snippets/Snippets.md`

Do not reconstruct live state from this handover or from memory when the repository can be read.

---

# 3. Locked architecture — do not reopen by default

The program currently uses:

```text
always-loaded agent file
  -> compact embedded behavior modules
  -> conditional/path/semantic routing when relevant
  -> focused method or Agent Skill when justified
  -> deeper references/examples/scripts/evidence only when needed
```

Locked principles:

- `AGENTS.md`-style root instructions are the preferred carrier where supported.
- XML is a compact prompt-structure candidate, not a parser dependency.
- The compact module remains visible in the always-loaded agent contract.
- Deeper guidance is loaded JIT only when genuinely useful.
- A deeper module does **not** automatically become a Skill.
- Each root module should use:
  - established concept name(s);
  - one short local semantic rule;
  - optional `when` / `deepen_when` / `ref` only where routing value exists.
- Always-loaded context must stay small.
- Every root rule must eventually defend its token/context cost.
- Do not install candidate Skills or propagate pilot wording into live runtime instruction files during module deepening.

---

# 4. Research order — mandatory

For every remaining module, use this order:

```text
1. current OpenAI / ChatGPT / Codex evidence
2. independent mature-agent convergence
3. established external discipline
4. local synthesis only for genuine gaps
```

## 4.1 Current AI-native primary evidence first

Research current official OpenAI / ChatGPT / Codex guidance when relevant.

Look for:

- current model behavior;
- prompting recommendations;
- model/tool limitations;
- search / grounding / browsing behavior;
- approval/autonomy patterns;
- context architecture;
- Skills / plugins / subagents;
- production-agent lessons;
- measured evaluations;
- known over-triggering / under-triggering / stale-prompt failure modes.

Treat model/product behavior as time-sensitive.

Do not rely on old prompting folklore when current official guidance can be checked.

## 4.2 Independent mature-agent convergence second

Check at least two when practical:

- Anthropic Claude / Claude Code;
- GitHub Copilot;
- Gemini / Gemini CLI;
- Kiro;
- Cursor;
- Windsurf;
- other mature systems only when materially relevant.

Separate:

- portable behavioral convergence;
- vendor-specific implementation mechanics.

## 4.3 External disciplines third

Use mature disciplines only after the AI-native behavior is understood.

Examples:

- systems engineering;
- requirements engineering;
- configuration management;
- verification / validation;
- evidence / provenance;
- incident management;
- decision analysis;
- HCI / information architecture;
- scientific method / reproducibility.

Do not let formal vocabulary override observed current agent behavior.

---

# 5. Current observed program state

At the time this handover was written, live `README.md` showed:

| ID | Module | State |
|---|---|---|
| A01 | `<target>` | DONE |
| A02 | `<scope>` | DONE |
| A03 | `<reuse>` | DONE |
| A04 | `<workflow>` | DONE |
| A05 | `<intent>` | DONE |
| A06 | `<context>` | DONE |
| A07 | `<realization>` | DONE |
| A08 | `<evidence>` | DONE |
| A10 | `<recovery>` | DONE |
| A11 | `<current_truth>` | DONE |
| A12 | `<communication>` | DONE |
| **A13** | **`<grounding>`** | **NEXT** |
| C01 | `<decision>` | QUEUED |
| C02 | `<research>` | QUEUED |
| C03 | `<informatics>` | QUEUED |

A09 was previously merged into A01 and removed as a standalone module.

There are also **pending / not-yet-canonical** areas referenced by the operational companion and TODOs:

- A14 authority / side-effect boundary candidate;
- C04 online/browser repository mutation handoff candidate;
- retry/replay/idempotency ownership;
- final source-governed execution contract integration decision.

Do **not** insert these into the active sequence unless the live README has been updated to do so.

---

# 6. Completed module outcomes that matter for boundaries

The next chat does not need to re-research these, but it must respect their ownership boundaries.

## A01 `<target>`

Owns:

- substantive intended outcome;
- anti-proxy optimization;
- success validation;
- tests/files/checklists are evidence, not substitutes for the result.

## A02 `<scope>`

Owns:

- authorized task boundaries;
- non-goals;
- avoiding adjacent drift.

## A03 `<reuse>`

Owns:

- proven reuse before invention;
- evaluating existing project/external capability before custom construction;
- adapting only verified gaps.

## A04 `<workflow>`

Owns:

- complexity-adaptive process depth;
- when to execute directly vs plan/decompose/review.

## A05 `<intent>`

Owns:

- intent inference;
- clarification threshold;
- make low-risk/reversible judgment calls rather than asking unnecessarily.

## A06 `<context>`

Final direction:

```xml
<context principles="context-engineering,progressive-disclosure,JIT-retrieval">
  Maintain a sufficient high-signal working context. Keep always-loaded guidance lean and navigable; load deeper instructions, sources, files, skills, or tools just in time for the specific decision or work step that needs them, rather than bulk-loading available context upfront.
</context>
```

Owns:

- progressive disclosure;
- JIT retrieval;
- sufficient—not minimal—high-signal context.

## A07 `<realization>`

Final direction:

```xml
<realization principles="hierarchical-decomposition,requirements-traceability,incremental-integration,verification,validation"
             ref="apex-meta/informatics/MMM/working-method.md"
             deepen_when="work has dependent parent/child levels where local work could diverge from the parent outcome">
  For multilevel work, keep lower-level work and interfaces traceable to the parent outcome. Realize bounded units, integrate upward, verify each level against its requirements, and validate assembled results against parent intent; revise the level disproven by evidence.
</realization>
```

Owns:

- hierarchical coherence;
- child→parent traceability;
- integration;
- local verification + parent validation.

It does **not** force a universal waterfall or V-model sequence.

## A08 `<evidence>`

Final direction:

```xml
<evidence principles="claim-evidence-traceability,source-authority,provenance,freshness,uncertainty-calibration">
  Keep material claims traceable to what actually supports them. Distinguish source or observation from inference or assumption; calibrate confidence to evidence quality and freshness, and qualify, omit, or mark unresolved claims when support is insufficient rather than guessing.
</evidence>
```

Owns:

- claim↔evidence integrity;
- provenance;
- source authority / freshness;
- evidence vs inference;
- uncertainty calibration.

Important boundary for A13:

> **A08 = what the evidence justifies saying.**
>
> **A13 = when external reality must be consulted at all.**

## A10 `<recovery>`

Final direction:

```xml
<recovery principles="feedback-driven-recovery,bounded-retries,replay-safety,graceful-degradation,stop-conditions">
  Treat recoverable failures as feedback: correct, retry, replan, or use a target-preserving fallback and continue. Bound retries and avoid unchanged or replay-unsafe repeats; escalate only when no credible authorized path remains or further action risks safety, state, or target integrity.
</recovery>
```

Owns:

- bounded recovery;
- replay safety;
- re-plan/fallback/stop.

## A11 `<current_truth>`

Final direction:

```xml
<current_truth principles="canonical-current-state,scope-aware-precedence,consistency,history-separation">
  Use the authoritative current source for each governed fact or decision. When active sources overlap, follow explicit precedence and the most specific applicable scope; do not synthesize contradictory guidance. Update or flag stale dependents, and keep superseded states as history rather than competing instructions.
</current_truth>
```

Owns:

- current project/instruction authority;
- scoped precedence;
- current vs historical state.

Important boundary for A13:

> A11 answers **which project/instruction state governs**.
>
> A13 answers **when external real-world evidence is required**.

## A12 `<communication>`

Final direction:

```xml
<communication principles="communication-economy,actionability,proportional-detail,exception-reporting">
  Match communication to the user's information need and the task phase. Lead with the result or current state; surface material progress, decisions, blockers, changes, caveats, and required action, while compressing routine tool activity, repetition, and internal reasoning unless they materially help the user steer, verify, or act.
</communication>
```

Owns:

- proportional user-facing visibility;
- useful progress;
- communication economy;
- result/current-state first.

It does **not** mean “always be brief.”

---

# 7. Important new candidate — Source-Governed Execution Contract

The operator identified a recurring failure:

> Even when explicit sources are provided, an AI may quietly prioritize unrelated material, generic model knowledge, or newly discovered sources.

A candidate operational solution now exists:

`14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md`

## Core structure

```text
TARGET
  ↓
INPUT
  ├── requested material
  └── SOURCE AUTHORITY
         ├── P0 governing / binding
         ├── P1 primary / authoritative
         ├── P2 supporting
         ├── P3 discovery only
         └── X excluded
  ↓
PROCESS / TRANSFORMATION
  ↓
EXPECTED OUTPUT
  ↓
EXECUTION
  ↓
SOURCE-COVERAGE + TARGET VALIDATION
```

## Why categorical tiers, not only 1–10 scores

A free-form `1–10` ranking creates false precision.

The candidate therefore prefers:

- categorical authority tier;
- explicit usage policy;
- optional numeric rank only as a secondary ordering aid.

Example usage policies:

- `must-use`;
- `verification-only`;
- `use-if-relevant`;
- `background-only`;
- `discovery-only`;
- `excluded`.

## Critical completion check

A required source must not merely be listed.

The executor must show whether and where it affected the result.

A polished output that silently ignores a `must-use` source is a task failure unless the omission is explicitly justified.

## Boundary

This is currently:

- a **candidate operational pattern**;
- **not** a new A-module;
- **not** integrated into the live pilot;
- **not** a reason to change A13's bounded module scope.

Later synthesis should decide whether/how to integrate it into:

`13-HUMAN-AI-COMPLEX-TASK-EXECUTION.md`

and whether any compact source-governance invariant belongs in the root contract.

---

# 8. Immediate task — execute A13 only

## 8.1 Current observed A13 pilot block

```xml
<grounding principles="external-grounding,source-authority,real-world-verification">
  When a material decision depends on real-world facts, capabilities, methods, integrations, standards, maturity, or reliability, do not rely on model reasoning alone. Verify against current authoritative external evidence and, when feasible, direct observed behavior or tests; expose unresolved uncertainty.
</grounding>
```

Treat this as a **hypothesis to test**, not wording to defend.

## 8.2 A13 semantic purpose

A13 should prevent the AI from canonizing real-world claims or consequential decisions from model reasoning alone when external reality materially matters.

Typical domains include:

- current software/product capabilities;
- integrations;
- standards;
- current APIs;
- laws/regulations;
- maturity/maintenance;
- performance/reliability claims;
- market/product availability;
- factual claims whose current external state matters;
- named systems whose behavior can be checked;
- “battle-proven” claims;
- existence/support/compatibility claims.

## 8.3 A13 does NOT own

Do not let A13 absorb neighboring modules.

### A08 owns

- source quality;
- provenance;
- freshness;
- claim strength;
- uncertainty calibration;
- evidence vs inference.

### C02 owns

- deeper research workflow;
- landscape scan;
- triangulation;
- candidate comparison;
- research procedure.

### A11 owns

- current project/repository/instruction authority;
- precedence among local governing artifacts.

### A03 owns

- reuse-before-build decision.

### A01 owns

- substantive target and final success.

### A04 owns

- whether a task needs structured planning/research depth.

### A12 owns

- how grounding results are communicated to the user.

The likely unique A13 question is:

> **When is model reasoning alone insufficient, requiring the agent to consult external reality before making a material claim or decision?**

---

# 9. A13 research agenda

The fresh chat should research these questions explicitly.

## Q1 — Trigger threshold

What is the smallest useful trigger for external grounding?

Potential dimensions:

- materiality;
- time sensitivity;
- external/niche knowledge;
- named current systems;
- uncertainty;
- consequential decisions;
- user explicitly asks to research/verify;
- claim depends on exact current capability/support.

Test whether the trigger should be:

- “material decision” only;
- “material claim or decision”;
- “current/external/niche facts”;
- or another evidence-backed formulation.

## Q2 — Model knowledge vs external reality

What does current OpenAI guidance say about when to:

- use web/search/deep research;
- rely on supplied sources;
- use tools;
- verify current facts;
- avoid guessing from latent knowledge?

Research **current** official OpenAI / ChatGPT / Codex guidance first.

Do not assume 2025/early-2026 behavior is still the best guidance.

## Q3 — Direct observation / tests

When should direct observed behavior or runtime tests outrank documentation?

Examples:

- official docs claim feature exists but current tool surface does not expose it;
- integration claims support but direct execution fails;
- product marketing claims capability but observed environment contradicts it.

A13 should probably require direct observation only **when feasible and material**, not universally.

## Q4 — Source authority interaction

Does A13 need `source-authority` in its principle list, or is that already sufficiently owned by A08/A11?

Test for duplication.

## Q5 — Freshness

How much should A13 say about “current” evidence versus leaving freshness entirely to A08?

Likely boundary:

- A13 decides **whether external grounding is needed**;
- A08 decides **whether the evidence used is current/strong enough**.

But test this rather than assuming it.

## Q6 — Cost / latency / over-triggering

A13 must not turn every task into web research.

Explicitly test:

- rewriting user-provided text;
- pure coding refactor with complete local context;
- simple arithmetic;
- creative writing;
- stable conceptual explanation;
- current product capability;
- legal/regulatory question;
- architecture choice depending on real products;
- “battle-proven” tool recommendation.

The rule should ground externally only when external reality is load-bearing.

## Q7 — User-provided sources

How should A13 interact with the new Source-Governed Execution Contract?

Important:

- if P0 sources are explicitly designated by the operator, do not silently replace them with external material;
- external research may be:
  - verification-only;
  - contradiction detection;
  - gap filling;
  - discovery-only;
  depending on the task contract.

Do **not** let “ground externally” become permission to override the user's specified source basis.

Record this interaction in A13's result, but do not automatically integrate candidate 14 into the pilot.

## Q8 — Merge candidate with A08

A08 and A13 should be tested as separate vs merged controls.

Compare:

```text
A08 only
A13 only
A08 + A13
possible merged evidence/grounding rule
```

Measure:

- hallucinated current capability claims;
- unnecessary web research;
- citation/source quality;
- uncertainty handling;
- context cost;
- portability.

Preserve them separately unless evidence supports a merge.

## Q9 — Deeper owner

Likely candidates:

1. no deeper artifact;
2. C02 as deeper method when research is triggered;
3. dedicated grounding reference;
4. dedicated Skill.

Do not create a Skill merely because grounding is important.

A Skill is justified only if there is a recognizable reusable task/workflow that materially benefits from deeper procedure.

---

# 10. A13 scenario suite

At minimum test these.

## Scenario 1 — negative/simple

User: rewrite a paragraph for clarity.

Expected:

- no web;
- no external verification ceremony;
- A13 visible effect ≈ zero.

## Scenario 2 — current product capability

User: “Does product X currently support Y?”

Expected:

- external grounding required;
- current authoritative source preferred;
- if actual tool/runtime can be observed, use observed behavior where material.

## Scenario 3 — battle-proven architecture recommendation

User: “Use only proven existing tools for this pipeline.”

Expected:

- external evidence required for maturity/support/capability claims;
- model familiarity alone is insufficient;
- A03 decides reuse behavior;
- A13 supplies reality grounding.

## Scenario 4 — user provides binding sources

User provides three P0/P1 sources and asks for synthesis.

Expected:

- use supplied source contract;
- external search does not silently displace P0 basis;
- additional grounding only according to task role.

## Scenario 5 — docs vs observed behavior conflict

Official docs say integration exists; actual connected tool surface lacks it.

Expected:

- record the contradiction;
- observed execution capability matters for actual workflow design;
- do not pretend capability exists in the active environment.

## Scenario 6 — stale model knowledge

Model “knows” an API or product behavior from training, but task depends on the current version.

Expected:

- verify externally.

## Scenario 7 — stable conceptual knowledge

User asks for a general conceptual explanation that is not time-sensitive and no current factual decision depends on it.

Expected:

- do not force external research merely because sources exist.

## Scenario 8 — unsupported real-world claim

No reliable external evidence can be found.

Expected:

- preserve unresolved uncertainty;
- do not fabricate;
- A08 controls claim strength.

## Scenario 9 — A08/A13 merge test

Same task under:

- A08 alone;
- A13 alone;
- A08 + A13.

Measure whether standalone A13 earns its persistent context cost.

## Scenario 10 — XML vs compact Markdown

Compare selected XML wording with equivalent Markdown.

Record whether XML materially changes behavior or only structure/readability.

---

# 11. A13 required deliverable

Create:

`apex-meta/handoff/universal-ai-instruction-system/module-deepening/A13-<slug>/README.md`

The README should include:

1. final decision;
2. final XML;
3. compact Markdown control;
4. current OpenAI / ChatGPT / Codex evidence;
5. independent mature-agent convergence;
6. established external grounding;
7. semantic MUST / MUST NOT;
8. activation threshold;
9. module boundaries;
10. alternatives considered;
11. scenario evaluation;
12. deeper-owner decision;
13. overlap/merge candidates;
14. source record;
15. uncertainties;
16. final-synthesis implications.

Do not create extra artifacts unless they have genuine execution value.

If the selected deeper owner is:

- Skill -> add non-installed candidate `SKILL.md`;
- focused reference -> add `REFERENCE.md`;
- otherwise -> no extra file.

---

# 12. A13 bounded modifications

During the A13 run, modify only:

1. new A13 module result folder;
2. A13 block inside `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` if evidence supports a wording change;
3. module status table in `README.md`:
   - A13 -> DONE;
   - C01 -> NEXT.

Do **not** in the same run:

- rewrite A08;
- rewrite A11;
- integrate candidate 14;
- change the complex-task execution guide;
- add A14/C04;
- alter live runtime AGENTS/CLAUDE/Hermes/Kiro/Cursor/Windsurf rules;
- continue into C01.

If A13 research reveals a needed neighboring change, record it in the A13 result as a dependency / final-synthesis item.

---

# 13. Per-module execution algorithm after A13

For every subsequent module:

```text
READ live README
  ↓
SELECT exactly NEXT
  ↓
READ current pilot block
  ↓
RESEARCH AI-native first
  ↓
CHECK independent agent convergence
  ↓
USE external discipline only if it adds durable value
  ↓
COMPARE viable alternatives
  ↓
TEST current wording as a hypothesis
  ↓
SIMULATE activation / non-activation / conflict / failure cases
  ↓
DECIDE smallest deeper owner
  ↓
WRITE one module result folder
  ↓
UPDATE only selected pilot block if justified
  ↓
ADVANCE status exactly one row
  ↓
COMMIT to main
  ↓
VERIFY exact changed paths
  ↓
STOP
```

---

# 14. Remaining program after A13

Assuming the live README still follows the observed sequence:

## C01 `<decision>`

Role:

- conditional decision / trade-off discipline.

Current candidate idea in pilot:

```xml
<decision when="the operator must choose among material alternatives or explicitly asks for options"
          principles="trade-study,MCDA,decision-record">
  Present distinct options, consequences, evidence, uncertainty, recommendation, and concise rejection reasons. Avoid false numerical precision.
</decision>
```

Research should determine:

- whether recommendation belongs here;
- how to avoid fake numerical scoring;
- when trade study is worth the overhead;
- how human decision gates interact with agent autonomy;
- whether MCDA belongs in root principle names.

## C02 `<research>`

Role:

- conditional deeper research discipline.

Current candidate idea:

```xml
<research when="the task depends on current, external, niche, contested, or comparative evidence"
          principles="landscape-scan,source-authority,triangulation">
  Research before canonizing a recommendation. Prefer primary or authoritative sources and distinguish verified facts from inference.
</research>
```

Important boundary:

- A13 = trigger for external grounding;
- A08 = evidence integrity;
- C02 = actual research method.

Candidate 14 may be highly relevant here because it introduces explicit source authority / use roles / source coverage.

Do not conflate source governance with generic research breadth.

## C03 `<informatics>`

Role:

- conditional formal repository knowledge / architecture authoring.

Current pilot already contains a scoped Informatics block with a JIT reference to:

`apex-meta/informatics/index.md`

Research should determine:

- how much belongs in the root conditional block;
- whether current canonical Informatics standards are actually useful across tasks;
- whether serialization/style details belong in root or deeper reference;
- how to avoid forcing formal documentation structure into ordinary tasks.

---

# 15. Program completion after C03

When C03 is DONE, stop module research.

Do **not** immediately propagate the full contract live.

Start a separate final-synthesis / controlled-evaluation phase.

## Required final synthesis

### 15.1 Context-budget defense

Every module must earn its always-on token cost.

Compare:

- full constitution;
- smaller control prompt;
- merged variants;
- deleted-module variants.

### 15.2 Merge/delete testing

Explicitly test overlaps such as:

- A01 + A04 vs A01 + A04 + A07;
- A08 vs A13 vs merged evidence/grounding;
- A06 vs A12 overlap;
- A02/A05/A14 authority interaction if A14 becomes canonical;
- C02 vs source-governed execution contract.

### 15.3 XML vs Markdown

Test whether XML improves:

- instruction separation;
- cross-agent portability;
- behavioral adherence;
- readability;
- token cost.

Do not keep XML merely by preference.

### 15.4 Cross-agent evaluation

Use representative tasks across at least several mature agents/runtimes when practical.

Measure:

- target adherence;
- source adherence;
- reuse-before-invention;
- unnecessary planning;
- hallucinated capabilities;
- external-grounding correctness;
- evidence traceability;
- recovery behavior;
- communication noise;
- token/context cost.

### 15.5 Resolve pending controls

Before propagation, resolve:

- `10-UNIVERSAL-SHORT-RULE-COVERAGE-TODO.md`;
- A14 authority candidate;
- C04 repository mutation candidate;
- retry/replay/idempotency ownership;
- source-governed execution contract integration;
- any module merge/delete candidates.

Each high-value control should end as:

- COVERED;
- MERGED;
- or REJECTED WITH EVIDENCE.

### 15.6 Operational companion integration

Decide how to integrate:

`14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md`

into:

`13-HUMAN-AI-COMPLEX-TASK-EXECUTION.md`

Recommended evaluation target:

For complex tasks, the orchestrator should be able to expose a compact preflight like:

```text
TARGET
- substantive intended outcome

INPUT / SOURCES
- P0 must-use: ...
- P1 authoritative: ...
- P2 supporting: ...
- P3 discovery-only: ...
- excluded: ...

PROCESS
- transformation / execution steps
- what external verification may and may not change

OUTPUT
- expected artifact / answer
- rough depth / sections / format

VALIDATION
- source coverage
- target success
- unresolved uncertainty
```

The goal is not more ceremony.

The goal is to prevent the AI from silently substituting its preferred sources or process for the operator's specified basis.

### 15.7 Live propagation requires a separate decision

Only after controlled evaluation should the operator decide whether to update live:

- `AGENTS.md`;
- CLAUDE guidance;
- Hermes;
- Cursor;
- Kiro;
- Windsurf;
- installed Skills;
- other runtime instruction surfaces.

Module deepening itself does not authorize propagation.

---

# 16. Quality principles for the entire continuation

The next chat must preserve these operating principles.

## Outcome over proxies

Do not optimize for:

- file count;
- checkboxes;
- passing a narrow test;
- “completed” labels;
- schema compliance alone.

Optimize for the requested useful result.

## Reuse before invention

Do not design another custom framework when a proven solution exists.

Research the proven solution and use it near its established form when fit.

## AI-native before formal-method theater

Do not foreground NASA, PMI, systems engineering, or other mature disciplines merely because they offer terminology.

First determine what current AI systems actually need.

Use older disciplines only where they add durable value.

## No artificial minimalism

“Lean” does not mean shallow.

Use enough rigor, sources, detail, and validation to realize the target.

## No process explosion

Do not add:

- unnecessary agents;
- matrices;
- gates;
- schemas;
- files;
- reviews;
- scoring systems

unless they reduce a material failure mode.

## Do not infer tool capabilities

Verify the actual execution surface.

A capability documented for a CLI/local agent/API does not imply the online/browser connector has it.

## No hidden source substitution

When the operator specifies source authority:

- respect it;
- do not let generic model knowledge or web research silently outrank it;
- expose conflicts;
- apply explicit source-use roles.

---

# 17. Fresh-chat launcher

The operator can start a new chat with:

```text
@GitHub

Execute:

apex-meta/handoff/universal-ai-instruction-system/15-A13-AND-PROGRAM-CONTINUATION-HANDOVER.md

Repository:
leela-spec/apexai-os-meta

Branch:
main only

Become the continuation orchestrator for the Universal AI Instruction System.

First re-read the live README and confirm the actual NEXT module. If A13 is still NEXT, execute A13 only according to the handover, including current OpenAI/ChatGPT/Codex web research first, independent mature-agent comparison second, external discipline grounding third, bounded scenario evaluation, pilot update only if justified, one module-result folder, one atomic main commit, exact diff verification, then stop.

If the live README has advanced since the handover was written, do not regress it. Follow the live NEXT row using the same one-module process.

Preserve the Source-Governed Execution Contract candidate as an explicit later synthesis / operational-integration item; do not silently absorb it into A13.
```

---

# 18. Stop condition for the next chat

For the immediate next run:

```text
A13 research complete
+ A13 result persisted
+ A13 pilot wording updated only if justified
+ README advanced A13 DONE -> C01 NEXT
+ bounded commit on current main
+ exact changed-path verification
= STOP
```

Do not continue into C01 in the same run unless the operator explicitly says to continue.

---

# 19. Core invariant

The whole program should preserve this:

```text
UNDERSTAND THE REAL TARGET
        ↓
ESTABLISH CURRENT AUTHORITY
        ↓
RESPECT SOURCE GOVERNANCE
        ↓
GROUND EXTERNAL REALITY WHEN MATERIAL
        ↓
REUSE WHAT IS PROVEN
        ↓
PLAN ONLY AS MUCH AS NEEDED
        ↓
LOAD ONLY RELEVANT CONTEXT
        ↓
REALIZE BOUNDED WORK
        ↓
VERIFY / VALIDATE AGAINST THE PARENT OUTCOME
        ↓
REPORT MATERIAL RESULT, EVIDENCE, UNCERTAINTY, AND REQUIRED ACTION
```

The purpose is not to create a perfect instruction document.

The purpose is to measurably reduce:

- target drift;
- source drift;
- hallucinated capabilities;
- custom reinvention;
- context bloat;
- over-processing;
- under-delivery;
- unsafe side effects;
- fake completion;
- and human confusion about what the AI is actually doing.
