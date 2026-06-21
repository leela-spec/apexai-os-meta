# Operator Gate

## Purpose

Use the operator gate to stop planning outputs from silently turning into mutation or sync claims.

The operator gate is required whenever the packet is ready for review, approval, or downstream delegation.

## Gate Outcomes

The gate may produce only these outcomes:

- ready for operator review
- needs operator clarification
- ready for downstream planning handoff
- deferred by operator choice

The gate does not authorize this skill to mutate state.

## Required Gate Checks

Before closing a planning packet, check the following:

### Boundary Check

Confirm that the packet remains planning-only and does not claim script execution, mutation, registry rebuild, blocker scan, stale detection, exact sync result, or session mutation.

### Intent Check

Confirm that the operator intent is represented accurately enough for review.

### Scope Check

Confirm that the packet distinguishes in-scope planning work from out-of-scope execution work.

### Dependency Check

Confirm that proposed `depends_on` relationships are explicit and justified.

### Status Check

Confirm that only the allowed status values are used.

### Priority and Urgency Check

Confirm that priority and urgency are presented as suggestions, not as final scheduling or execution decisions.

### Evidence Check

Confirm that substitute or missing evidence is labeled correctly.

If PM2-style task-contract reasoning used the accepted substitute pattern, preserve `CrewAI_task_py_SUBSTITUTE`.

## Recommended Gate Questions

Use these question types when needed:

- Is the planning scope correct?
- Are any proposed epics missing or merged incorrectly?
- Are the dependency proposals acceptable?
- Which blocked or deferred items should remain in the packet?
- Should any task candidate priority or urgency suggestion be adjusted?
- Is the packet ready for downstream sync review?

## Downstream Delegation Statements

Use concise boundary-preserving language.

Allowed examples:

- exact next-task computation is deferred to `apex-sync`
- state mutation and session continuity are deferred to `apex-session`

Not allowed:

- sync completed
- session updated
- handoff files written
- registry rebuilt

## Final Gate Output Shape

End with a short gate summary:

- `gate_status`
- `operator_confirmations_needed`
- `boundary_reminders`
- `downstream_delegate`

Keep this summary short and explicit.