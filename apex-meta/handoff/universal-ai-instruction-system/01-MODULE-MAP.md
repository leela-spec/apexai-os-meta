---
type: ArchitectureMap
title: Universal AI Instruction System — Module Map
description: Validated research taxonomy separating universal interaction behaviors from existing system owners and task-specific procedures.
status: research_backlog_selected
created: 2026-09-04
---

# Universal AI Instruction System — Module Map

## Taxonomy decision

Research **eight universal behavior modules**.

Do not create independent modules for concerns already owned by Informatics, Plan-Sync-Session, authorization, or task-specific Skills.

The eight modules are a research decomposition. Cross-module synthesis MAY merge them after independent evaluation.

## Selected modules

| ID | Name | Purpose | Scope | Established vocabulary | Current owner/source | Proposed canonical owner | Trigger | Short surface | Deep reference | Dependencies | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M01 | Intent Alignment & Execution Preflight | Make misunderstandings cheap to catch before nontrivial execution. | Universal interaction behavior | requirements elicitation; task specification; closed-loop communication; check-back; clarification | `Agent_Setup/02-preflight-and-progressive-disclosure-design.md`; operator handover | New focused behavior module, reusing existing preflight research | Nontrivial work where scope, basis, dependencies, or deliverable could be misunderstood | 1–3 sentences | Yes | M04, M08 | **KEEP / RESEARCH** |
| M02 | Hierarchical Realization (MMM) | Preserve system intent through top-down realization and bottom-up V&V. | Universal working orientation | hierarchical decomposition; requirements flowdown; V-model/Vee; integration; verification; validation | `apex-meta/informatics/MMM/` | **Existing MMM bundle** | Work with dependent levels, architecture, or integration risk | Existing candidate ~2–4 sentences | Existing | M04, M08 | **KEEP EXISTING / VERIFY** |
| M03 | Context Management | Keep context high-signal and load deeper material just in time. | Universal interaction behavior | context engineering; progressive disclosure; JIT retrieval; compaction; context isolation | Informatics + operator context-bloat need | Focused behavior module that references Informatics | Long, multi-source, multi-module, or context-heavy work | 1–3 sentences | Yes | Informatics, M04 | **KEEP / RESEARCH** |
| M04 | Workflow & Complexity Routing | Scale process to observable task complexity without ceremony. | Universal interaction behavior | direct execution; prompt chaining; routing; parallelization; orchestrator-workers; evaluator-optimizer; bounded specification | `Agent_Setup/01-*`; `02-*`; Anthropic patterns | Focused working-method router | Every task, but direct route should disappear into normal execution | 1–3 sentences | Yes | M01, M02, M03 | **KEEP / RESEARCH** |
| M05 | Target, Value, Reuse & Anti-Drift | Keep work tied to the requested outcome and prefer proven reuse before invention. | Universal interaction behavior | outcome/value focus; YAGNI; KISS; Lean waste; vertical slice; tracer bullet; bottleneck focus; risk-based assurance | `AI-Snippets/Snippets.md` | Focused behavior module | When process, infrastructure, repairs, or custom design could displace the target | 2–4 sentences | Yes | M04 | **KEEP / RESEARCH** |
| M06 | Decision Elicitation & Trade Studies | Help the operator resolve material choices with grounded options and uncertainty. | Universal interaction behavior | trade study; decision analysis; MCDA; decision matrix; ADR/RFC; uncertainty communication | `AI-Snippets/Snippets.md` Q&A + REI | Focused behavior module | Material choice, trade-off, unresolved preference, or requested Q&A | 2–4 sentences | Yes | M07 | **KEEP / RESEARCH** |
| M07 | Research & Evidence Discipline | Use sufficient current evidence and distinguish source support from inference. | Universal interaction behavior | source authority; evidence hierarchy; provenance; triangulation; freshness; uncertainty calibration | `AI-Snippets/Snippets.md` research block | Focused behavior module | External/current/niche/uncertain claims or explicit research | 2–4 sentences | Yes | M06, M08 | **KEEP / RESEARCH** |
| M08 | Output & Deliverable Contract | Keep execution tied to the requested artifact, structure, acceptance, and definition of done. | Universal interaction behavior | output contract; acceptance criteria; Definition of Done; structured output; specification | operator handover + existing preflight research | Focused behavior module | When deliverable shape or acceptance is not obvious | 1–3 sentences | Yes | M01, M02 | **KEEP / RESEARCH** |

## Merge decisions

### Former M05 — Reasoning, Review & Verification

**MERGE. Do not create a standalone universal reasoning module.**

Route its useful concerns to existing owners:

| Concern | Owner |
|---|---|
| Visible task understanding / plan | M01 |
| Complexity-adaptive review loop | M04 |
| Unit/system verification and validation | M02 |
| Evidence for factual claims | M07 |
| Acceptance and final correctness | M08 |

Do not preserve the current `CoT Scratchpad` request as a universal instruction. Prefer observable plans, assumptions, evidence, decision rationale, intermediate artifacts, and verification results.

## Task-specific decision

### Former M10 — Change / Patch Execution

**REJECT from universal behavior.**

The exact-match `<file>/<old>/<new>` protocol is a deterministic mutation procedure. Keep it in a task-specific procedure or Skill when needed.

Reason: most AI tasks do not need literal block replacement semantics. Loading the rule globally adds context and can distort ordinary editing.

## Additional candidates reviewed

| Candidate concern | Decision | Owner / rationale |
|---|---|---|
| Ambiguity threshold: ask vs infer | **MERGE** | M01. Ask only for material unresolved ambiguity; read evidence first when possible. |
| Source / authority resolution | **MERGE** | M07 plus existing instruction-precedence rules. |
| Irreversible-action confirmation | **DO NOT DUPLICATE** | Existing authorization/mutation policy owns permission. |
| Error recovery and stop conditions | **MERGE** | M04 for workflow recovery; M05 for two-strike/drift stop behavior. |
| Progress-update cadence | **NOT A MODULE** | Runtime/product interaction preference. Keep adapters lightweight. |
| Evaluation / success measurement | **CROSS-CUTTING** | M08 acceptance + `03-EVALUATION-PLAN.md`; no second lifecycle. |
| Durable state / handoff continuity | **DO NOT DUPLICATE** | Plan-Sync-Session and existing state owners. |
| Tool-use discipline | **TASK/RUNTIME-SPECIFIC** | Tool contracts and Skills should govern concrete tools. |
| Disagreement / challenge behavior | **MERGE** | M05 challenges drift/custom invention; M06 challenges decision assumptions. |
| Uncertainty calibration | **MERGE** | M06 for decisions; M07 for factual/evidence uncertainty. |
| Dependency ordering | **MERGE** | M01 captures active dependencies; M04 chooses execution pattern. |
| Parallel vs sequential work | **MERGE** | M04. Use parallelism only when work is genuinely independent. |
| Memory / personal preference handling | **NOT A METHOD MODULE** | Runtime memory and explicit operator preferences remain delivery/state concerns. |

## Overlap boundaries

### M01 vs M04

- M01 answers: **What do we think the job is?**
- M04 answers: **How much process does this job need?**

M04 may activate M01 for Route 1+ work. Do not duplicate the preflight schema in both modules.

### M02 vs M04

- M04 selects the route.
- M02 supplies hierarchical realization when the selected route needs it.

Do not make every Route 1 task produce a full Macro/Meso/Micro hierarchy.

### M03 vs Informatics

- Informatics owns document/knowledge structure and instruction scoping.
- M03 owns agent behavior for managing finite working context.

M03 references Informatics. It does not restate the five-plane standard.

### M05 vs M04

- M04 prevents process disproportion.
- M05 prevents outcome drift and unsupported custom invention.

A direct task can still need M05 if the agent starts building an unnecessary abstraction.

### M06 vs M07

- M06 structures choices.
- M07 establishes what evidence can support claims about those choices.

Numeric scoring must not substitute for evidence.

### M01 vs M08

- M01 exposes the task understanding.
- M08 defines the deliverable and acceptance contract.

M01 may summarize M08 fields without becoming their durable owner.

## Existing source-path mismatch

The handover referenced:

`apex-meta/AI-Snippets/SnippetDocs/AnitOverEng.md`

Repository search did not find that path or file on `main` during this run.

Use the anti-overengineering rules in `apex-meta/AI-Snippets/Snippets.md` as the current source until the missing artifact is recovered.

## Research order

Run modules in this dependency-aware order:

```text
M04 Workflow Routing
  -> M01 Intent / Preflight
  -> M02 MMM verification against routing
  -> M03 Context Management
  -> M08 Deliverable Contract
  -> M05 Target / Reuse / Anti-Drift
  -> M07 Research / Evidence
  -> M06 Decision Elicitation
```

Independent child contexts should remain bounded. Cross-module synthesis happens only after all selected modules have evidence-backed recommendations.
