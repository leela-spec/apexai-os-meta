# Project Routing

## Companion-authority note

This file is a companion routing guide. It preserves readable examples and handoff checklists.

Governing routing, delegation, state, and handoff rules live in `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`. Project entry and interface-first control requirements live in `managed/rules/PROJECT_INTERFACE_CONTRACT.md`. This file does not define runtime routing law.

## What this file explains

- quick keep-local versus delegate examples
- scenario shortcuts for bounded specialist routing
- the minimum checklist that makes a handoff reviewable

- **Compatibility note:** these examples remain useful while authority lives in managed canon and managed contract surfaces.

## Scenario examples

### Keep work local when

- the task is simple, quick, or conversational
- personal context is needed
- the task needs real-time user interaction
- the task is security-sensitive
- the task requires user approval

### Delegate to a specialist when

- deep focus is needed for a clearly bounded task
- the work is mostly self-contained
- success criteria can be stated explicitly
- parallel help would keep the main assistant responsive
- budgets and return format can be named up front

## Quick reference

| Scenario | Example routing |
|---|---|
| "Research X for me" | Delegate to a bounded research specialist |
| "Build this feature" | Keep local if small; delegate if the coding task is clearly bounded and non-trivial |
| "What do you think about..." | Keep local |
| "Fix this bug" | Keep local if small; delegate if complexity or surface area is high |
| "Draft an email" | Keep local |
| "Analyze this dataset" | Delegate when the analysis is bounded and self-contained |
| "Review this PR" | Keep local or delegate based on size, risk, and boundedness |

## Handoff checklist

Before delegating:

- [ ] Task is clearly defined
- [ ] Success criteria are explicit
- [ ] Context needed is documented
- [ ] Return format is specified
- [ ] Time or compute budget is set
- [ ] Model or cost tier is specified if relevant

When a specialist returns:

- [ ] Verify completeness
- [ ] Check against acceptance criteria
- [ ] Integrate the result into current context
- [ ] Report back in the main assistant's voice
- [ ] Do not forward raw output as a substitute for review

## Pointers to managed canon and contract

- `managed/rules/AGENT_SWARM_INTERACTION_CANON.md` — governing routing, delegation, state, and handoff law
- `managed/rules/PROJECT_INTERFACE_CONTRACT.md` — project-entry and interface-first control boundary

## Named first-iteration routing examples

| Request shape | Primary owner | Typical validators or downstream handoffs |
|---|---|---|
| new operator request with constraint uncertainty | `alfred` | hand off to `meta_ops`; pull `meta_strategy` or `meta_detective` only when needed |
| multi-step implementation or research packet | `meta_ops` | activate the minimum specialist set; verify with `meta_detective` for T2+ durable change |
| strategic choice or path comparison | `meta_strategy` | challenge with `meta_detective`; route accepted path back to `meta_ops` |
| source placement or candidate KB landing | `special_ops__knowledge_bank` | validate structural fit with `special_ops__informatics_design` |
| structure, terminology, decomposition, or retrieval-shape issue | `special_ops__informatics_design` | validate hygiene impact with `special_ops__hygiene_clean` |
| reusable workflow or prompt pattern need | `special_ops__prompts_workflows` | verify fit with `meta_ops`; involve `meta_detective` for high-impact cases |
| model/tool/path selection question | `special_ops__ai_handling_routing` | validate risk posture with `meta_detective`; keep config manual-review only |
| stale pointers, missing surfaces, continuity risk, or backlog cleanup | `special_ops__hygiene_clean` | escalate to `meta_detective` when plausibility, authority, or T3/T4 risk appears |

Default rule: start with the smallest bounded activation set that can do the job legibly.
