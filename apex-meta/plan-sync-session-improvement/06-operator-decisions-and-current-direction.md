# Operator Decisions and Current Direction

Date: 2026-08-16
Status: **operator-validated design direction; implementation not yet authorized by this file alone**

## Decision history

### D1 — Independent validation required before skill edits

**Operator direction:** do not blindly implement the original one-gate / risk-based authorization proposal. Independently inspect live Plan, Session, Sync, Weekly Orchestrator, mutation-gate, shared validation, and feedback-loop contracts; run simulations; surface failure modes; prefer the minimal architecture.

**Result:** completed. The double-gate diagnosis was reproduced from live contracts and from the real W34 portfolio canonicalization trace.

### D2 — A1 + B1 + C1 validated

The independent validation produced three operator decisions:

- **A1 — pinned action-scoped authorization** rather than task-wide inherited gate modes.
- **B1 — external / irreversible actions require an action-specific operator gate in the first rollout.**
- **C1 — preserve the current Apex Sync explicit authorization requirement for non-dry-run registry writes.**

**Operator response:** `validated`.

This means A1/B1/C1 are the accepted direction unless explicitly superseded later.

### D3 — External/web validation required because AI can hallucinate

After validating A1/B1/C1, the operator required another web/research pass and asked that Apex orient itself on working examples from the internet, including workflow design, web-search design, and skill-design best practices.

**Result:** completed against current primary/official sources and recent primary research.

### D4 — A1 refined to A1′

The external benchmark strengthened A1 but added a critical timing rule:

> **A1′ — commit-time action authorization:** a prior approval may be reused only if the exact pending durable action is still authorized immediately before the durable effect happens.

The validation found strong convergence across OpenAI Agents SDK HITL/tool guardrails, Claude Code permissions/hooks, LangGraph interrupts, Temporal durable workflows, GitHub protected environments, and recent commit-time-authorization research.

This is treated as a **refinement of the already validated A1**, not as a reversal of it.

## Current target policy

### A1′ — Commit-time action authorization

A reusable authorization should bind, at minimum:

```yaml
authorization:
  authorization_id: <stable-id>
  authority_ref: <operator decision or approved packet>
  basis_digest: <approved semantic/input basis>
  allowed_actions: []
  target_scope: []
  constraints: []
  issued_at: <timestamp>
  expires_at: <timestamp-or-null>
  status: active | revoked | expired
```

Where exact payload binding is necessary, add a payload/mutation digest rather than assuming the action class alone is sufficient.

### Commit-time check order

Preferred fixed order:

1. hard deny / explicit manual override;
2. authorization active and not expired/revoked;
3. approved basis digest still matches;
4. requested action class is authorized;
5. target resource/entity/file scope matches;
6. payload or mutation digest matches where binding is required;
7. deterministic constraints and required evidence pass;
8. no protected exception such as source conflict or duplicate identity merge;
9. optional AI semantic-delta review may escalate but is not the primary permission engine;
10. execute idempotently and write a durable receipt.

### B1 — External / irreversible actions

For the first rollout, external or irreversible actions remain explicitly action-gated unless the operator later adopts a narrower pre-authorization model.

Examples include sends, publishes, payments/trades, destructive deletions/migrations, or other effects whose consequences extend outside the bounded internal persistence operation.

Important distinction:

- it can be safe to **persist a task record describing a future external/manual action** under an existing authorization;
- that does **not** authorize performing the future external/manual action.

### C1 — Apex Sync registry writes

Keep the existing contract boundary:

- dry-run/read-side Sync computation can proceed under its normal invocation rules;
- `registry --dry-run false` remains a specifically protected write requiring the current explicit operator request unless a future operator decision changes that rule.

The Plan -> Session duplicate-confirmation fix must not silently broaden Sync authority.

## Rejected / not-selected alternatives

### Task-wide canonical `auto / exception_only / manual`

Not selected as the primary authority model because a single task can contain several operations with different risk:

- safe canonical serialization;
- deterministic analysis;
- a human product decision;
- an external irreversible action.

A task-wide inherited gate can accidentally transfer authority between these action classes.

`auto / exception_only / manual` may remain useful later as a **derived UI/presentation label**, but should not be the root authorization primitive without new evidence.

### Implicit parent-scope inheritance

Not selected when exact child coverage is ambiguous. Ambiguous scope must fail closed and request a bounded decision.

### AI-only semantic equivalence detector

Rejected as the primary authorization control. The local simulation showed that a false-negative semantic-delta detector can let an unauthorized semantic change pass.

Use deterministic scope/digest/action/evidence checks first. AI review may add an escalation signal.

## Preserved safeguards

The redesign must preserve:

- operator authority and explicit overrides;
- source references and source-conflict preservation;
- duplicate-entity safeguards;
- objective evidence requirements for automatic state transitions;
- Weekly Orchestrator G1-G5 semantic workflow gates;
- review disagreement/no-LLM-tiebreak rules;
- Sync's read-side authority boundary and explicit registry-write exception;
- failure evidence and mutation/action receipts;
- retry/resume safety and idempotency where a durable action may be replayed.

## Implementation boundary

The operator has validated the design direction, but the next engineering step should remain implementation preparation rather than immediately rewriting production skills.

Before skill edits:

1. create a small canonical authorization-policy draft;
2. create the regression/eval matrix;
3. map it onto existing fields and packet boundaries;
4. prove the minimum set of affected files;
5. bring any remaining high-impact architecture choice to the operator with concrete use cases and options.

## No-loss rule

Future changes to these decisions must be recorded as a new superseding decision with:

- what changed;
- operator confirmation;
- evidence/reason;
- affected contracts;
- migration consequence.

Do not silently edit this history to make prior decisions appear different from what was actually validated.
