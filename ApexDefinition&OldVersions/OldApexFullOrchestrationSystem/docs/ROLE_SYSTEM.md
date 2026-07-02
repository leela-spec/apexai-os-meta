# Role System

## Companion-authority note

This file is a companion guide. It explains everyday role heuristics and example handoffs.

Authoritative permissions, operational states, delegation rules, and handoff minimums live in `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`. This file does not define runtime authority.

## What this file explains

### Single-main default

- One primary assistant remains the default user-facing coordinator.
- Keep work local when the task is simple, personal, security-sensitive, approval-bound, or needs full context.
- Bring in specialists only when the work is clearly bounded and the main assistant needs to stay responsive.

### Specialist examples

- **Research specialist:** bounded research, information gathering, and synthesis.
- **Coding specialist:** complex coding tasks, larger refactors, testing, and documentation.
- **Cheap personas vs heavier orchestrators:** use cheap single-task helpers for formatting or narrowly scoped edits; use higher-judgment orchestration only when bounded decisions really require it.

### Conservative concurrency

- Default to one main active flow.
- Permit broader overlap only when validation evidence shows it is safe and non-drifting.

## Heuristics and examples

### Keep work local when

- the task is simple or quick
- personal context is central
- the user is in live conversation
- security-sensitive judgment is required
- user approval is required before action

### Delegate when

- deep focus is needed for an extended bounded task
- the work can be handed off cleanly with reduced context
- success criteria are explicit
- the main assistant needs to stay available for other work

### Example specialist framing

- **Research specialist:** receives the research question, required background, expected deliverable, and budget.
- **Coding specialist:** receives the task, files to touch, requirements, tests, and constraints.

## Handoff examples/templates

### Research handoff

```text
Research Task: [question]
Context Needed: [background]
Deliverable: [expected output]
Deadline: [when needed]
Budget: [token/compute limits]
```

### Coding handoff

```text
Task: [what to build]
Files to Modify: [paths]
Requirements: [acceptance criteria]
Test Cases: [how to verify]
Constraints: [what to avoid]
```

## Pointer to managed canon

Use `managed/rules/AGENT_SWARM_INTERACTION_CANON.md` for permission, state, delegation, and handoff law.

Use this file for quick companion guidance and readable examples only.

## Named first-iteration seed map

The current holding-layer companion map is:

| Named seed | Companion meaning |
|---|---|
| `alfred` | first user-facing intake, capacity, constraint, and route brief |
| `meta_ops` | central orchestration and specialist activation |
| `meta_strategy` | options, timing, and strategic recommendation |
| `meta_detective` | adversarial validation, drift challenge, and plausibility pressure |
| `special_ops__knowledge_bank` | placement, lifecycle, lane routing, and source coherence |
| `special_ops__informatics_design` | structure, taxonomy, terminology, and readability |
| `special_ops__prompts_workflows` | reusable prompt families and execution workflows |
| `special_ops__ai_handling_routing` | advisory model/tool routing posture |
| `special_ops__hygiene_clean` | structural QA, pointer integrity, and hygiene closure routing |

This map is explanatory only. Runtime behavior remains governed by the managed canons and protocols.
