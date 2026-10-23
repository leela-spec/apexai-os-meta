---
type: design-research
status: decision_ready_not_applied
created: 2026-09-03
---

# Preflight and Progressive Disclosure Design

## 1. Pre-execution understanding contract

The operator wants the agent to expose what it thinks the job is before starting nontrivial execution. This should **not** become another heavyweight project artifact by default.

Recommended established framing: **execution preflight / understanding brief**.

This is intentionally a compact working contract, not a new canonical project state object and not a new approval primitive.

### Required fields for Route 1+

```yaml
execution_preflight:
  target:
    outcome: "What concrete result should exist when done?"
    deliverable: "What artifact/action/output will be produced?"

  basis:
    inputs: []
    sources_to_use: []

  scope:
    in_scope: []
    out_of_scope: []

  realization:
    decomposition: []
    dependencies: []
    implementation_sequence: []
    expected_output_structure: []

  uncertainty:
    material_ambiguities: []
    assumptions: []

  verification:
    acceptance_conditions: []
    validation_question: "Does the resulting system/output satisfy the intended outcome?"
```

### Behavioral rules

1. Show it before consequential execution on Route 1–3 work.
2. Keep it proportional; omit empty or obvious fields.
3. Do not ask the operator to approve merely because a preflight exists.
4. Existing authorization/mutation contracts decide when operator approval is actually required.
5. If a material ambiguity can be resolved from repository/source evidence, resolve it by reading rather than asking.
6. If the ambiguity changes intended outcome/scope and evidence cannot resolve it, surface it explicitly before implementation.
7. Do not persist the preflight as a durable file unless the selected route needs a durable specification/plan artifact or a handoff.

## 2. Why this is not another TASK-BRIEF schema

The preflight is a **presentation/working interface** into existing planning artifacts.

Mapping:

| Preflight field | Existing owner or eventual owner |
|---|---|
| outcome/scope/constraints | specification or `apex-plan` project capture |
| decomposition/dependencies | plan/tasks or `apex-plan` task proposals |
| exact dependency/ranking validation | `apex-sync` |
| mutation authorization | existing authorization + `apex-session` |
| acceptance conditions | task/spec records |
| verification evidence | implementation/test artifacts |
| final status/handoff | `apex-session` |

Therefore the preflight should not create its own IDs, statuses, registry entries, permission fields, or lifecycle state.

## 3. Progressive disclosure architecture

### Level 0 — always loaded

Keep global guidance extremely small. It should contain only the routing invariant:

> Execute simple bounded work directly. For nontrivial work, establish target/scope/basis/plan/acceptance before changing things, decompose top-down with traceability, and verify/validate bottom-up. Load the shared working-method guidance only when that structure is needed.

The existing `AGENTS.md` directness rule remains authoritative: simple tasks take the shortest correct path.

### Level 1 — shared method surface

One shared method entrypoint should define:

- route selection (Direct / Compact / Full / Recursive);
- compact preflight;
- canonical vocabulary;
- top-down flowdown + bottom-up V&V;
- convergence behavior;
- handoff to Plan-Sync-Session owners;
- links to deeper references.

Do not duplicate these rules into each specialist agent.

### Level 2 — references loaded only when needed

Suggested reference topics:

```text
working-method/
  SKILL.md or method.md
  references/
    complexity-routing.md
    requirements-flowdown-and-traceability.md
    verification-validation-convergence.md
    recursive-specification.md
    plan-sync-session-mapping.md
  evals/
    route-selection.yaml
    preflight-quality.yaml
    hierarchy-and-vv.yaml
```

If implementation uses a Skill package, keep `SKILL.md` small enough to decide route and start execution. Push examples, edge cases, and evaluation scenarios into references/evals.

## 4. Specialist-agent behavior

Specialist agents should add only domain-specific instructions.

Bad:

```text
security-reviewer.md
  - its own planning lifecycle
  - its own complexity classes
  - its own task hierarchy
  - its own completion semantics
```

Good:

```text
security-reviewer.md
  shared_method: working-method
  domain_additions:
    - threat modeling rules
    - security evidence requirements
    - domain-specific verification criteria
```

The shared method owns realization semantics; specialist agents own specialist judgment.

## 5. Candidate ultra-short global instructions

### Candidate A — recommended default

> **Work to the target.** Execute simple bounded tasks directly. For nontrivial work, establish target, scope, basis, dependencies, deliverable and acceptance before mutation; decompose top-down with traceability and verify/validate bottom-up. Load the shared working method only when needed.

Strengths: complete enough to route behavior; explicit anti-ceremony; ~40 words.

### Candidate B — most compact

> Execute bounded work directly. Otherwise clarify/specify before implementation, preserve parent-child traceability, and verify units upward until the final result is validated against intent. Load detailed method guidance on demand.

Strengths: very small. Weakness: less explicit about inputs/scope/dependencies.

### Candidate C — strongest anti-drift

> Keep execution tied to the requested deliverable. If the task is nontrivial, expose what you understood (basis, target, scope, decomposition, dependencies, output and acceptance) before changing things. Then realize top-down and verify/validate bottom-up using the shared method.

Strengths: strongest protection against misunderstanding. Weakness: slightly more ceremony implied unless paired with direct-task exception elsewhere.

**Recommendation:** A, while retaining existing `AGENTS.md` directness/scope rules.

## 6. Route-specific interaction behavior

| Route | Visible preflight | Durable spec artifacts | Operator gate introduced by method? |
|---|---|---|---|
| Direct | none | none | No |
| Compact | short preflight | only if existing Plan/Session workflow needs them | No |
| Full | explicit preflight + spec/plan/task artifacts | yes | Only where existing lifecycle/mutation gate requires it |
| Recursive | program/roadmap summary + current bounded slice | yes, hierarchical | Only where existing lifecycle/mutation gate requires it |

## 7. Preflight quality test

A preflight passes only if another capable agent could answer these questions without rereading the user's full conversation:

- What exactly will be produced?
- What inputs/evidence are authoritative?
- What is explicitly outside scope?
- What are the main pieces and dependencies?
- In what order will work happen?
- What would count as done/correct?
- What ambiguity could materially change the result?

It fails if it is mainly generic process prose, repeats repository policy without task application, or describes tooling rather than the requested deliverable.

## 8. Anti-overengineering constraints

The shared method must not:

- require a new file for every task;
- require a new operator confirmation for every preflight;
- create another project status vocabulary;
- create a competing task database;
- automatically activate Multi-Agent Orchestration;
- automatically activate Weekly Orchestrator;
- require web research on every task;
- require an independent reviewer on every task;
- force recursive decomposition because the output is large;
- turn simple Git/file operations into planning sessions.
