# Operator Decisions and Current Direction

Date: 2026-08-16
Status: **operator-validated design direction; contract/eval/carrier spike complete; production skill edits pending final architecture choice**

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

### D5 — Minimal contract / lifecycle eval / carrier spike requested

The operator asked to continue with the next engineering step while explicitly prioritizing a **simple, efficient, resilient, valuable, on-target design that guards against over-engineering**.

Requested work:

- draft a small canonical authorization-policy contract;
- define duration/lifecycle and regression eval metrics;
- spike whether Plan, Session, Weekly/Status Merge, and Sync can carry the witness without creating a large subsystem;
- save the work into the canonical project folder.

**Result:** completed in `08` through `12` of this folder.

### D6 — Carrier spike supports field extension, not a subsystem

The executable non-production carrier spike produced:

- `17/17` expected policy outcomes;
- `0` unsafe allows;
- `0` overblocks;
- `0` repeated operator gates across 50 unchanged covered internal actions;
- no task gate field;
- no global authorization registry;
- no new daemon/service;
- no reusable-authorization change to Sync for the core Plan -> Session fix.

The spike therefore supports this carrier shape:

- Plan reuses its existing `operator_gate` as the approval/witness container;
- Weekly reuses `operator_validation` and `authority.basis_digest`, adding only authorization id/reference when needed;
- Status Merge passes the confirmed reference/digest rather than owning another policy engine;
- Session accepts the witness reference and validates it at the durable-effect boundary;
- Sync remains under C1;
- canonical task records remain unchanged.

This is design evidence, not production authorization code.

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

## Lifecycle / duration position from the spike

No global authorization TTL is selected for v1.

Each witness has explicit lifecycle data:

- `issued_at`;
- optional `expires_at`;
- `status: active | revoked | expired`.

Rules:

- if `expires_at` exists, authorization is invalid at or after that timestamp;
- `expires_at: null` explicitly means no time expiry, but basis/action/scope/constraints/status checks still apply on every commit;
- revocation takes effect on the next attempted action;
- a changed basis invalidates the witness even if time validity remains;
- process/chat restart does not invalidate a durable witness if it can be reloaded and revalidated from repository evidence.

A global TTL should only be introduced later if real usage demonstrates a cross-workflow need.

## Existing durable-writer ambiguity discovered

Current Session mutation-gate rules say final mutation records are authoritative input to a later explicit file-application flow and do not imply silent repo writes. Weekly wording also describes Session as validating/applying confirmed mutation.

Inspection of the current `apex-session` package and repository search did **not** identify a separately named file-application/writer component.

This is treated as an existing contract ambiguity, not a reason to invent a new subsystem.

Standing recommendation:

- **W1 — clarify the existing writer boundary** and put the final A1′ validation immediately before the real durable effect;
- **do not choose W2 — create a new writer/authorization subsystem** without evidence that one is necessary.

## Remaining architecture choice requiring operator decision

### P1 — Session-owned canonical authorization reference — **recommended**

Create the production canonical policy at:

`.claude/skills/apex-session/references/authorization-policy.md`

Rationale:

- Session already owns confirmed mutation semantics and validation;
- Plan and Weekly only need to carry/reference the witness;
- this is the smallest local home for the policy;
- if multiple independent durable writers are later proven, the policy can be shared/moved then.

### P2 — shared Workflow & Processes policy

Place the policy in a shared Workflow & Processes reference immediately.

Potential benefit: neutral location if multiple independent writers need the complete algorithm.

Current downside: creates a shared abstraction before the repository demonstrates that need, increasing cognitive and maintenance surface for a small Plan -> Session fix.

**Recommendation: P1.**

P1/P2 has not yet been silently decided by the engineering spike; it is the next operator architecture choice before production skill edits.

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

### New authorization registry/service/daemon

Not justified by current evidence. The carrier spike shows the existing approved packet and existing Plan/Weekly/Session handoffs can carry the needed evidence.

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

The contract, eval matrix, and carrier spike are now complete.

Before production skill edits:

1. operator chooses P1 or P2;
2. implementation identifies/clarifies the actual durable writer boundary under W1;
3. edit only the minimum affected skill contracts consistently;
4. run the eval matrix against the implemented behavior;
5. save implementation evidence and any superseding decisions in this folder.

## No-loss rule

Future changes to these decisions must be recorded as a new superseding decision with:

- what changed;
- operator confirmation;
- evidence/reason;
- affected contracts;
- migration consequence.

Do not silently edit this history to make prior decisions appear different from what was actually validated.
