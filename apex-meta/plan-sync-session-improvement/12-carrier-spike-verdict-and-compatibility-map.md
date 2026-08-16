# Authorization Carrier Spike — Verdict and Compatibility Map

Date: 2026-08-16
Status: **design spike complete; production skill edits not yet authorized by this document**
Decision basis: A1′ commit-time action authorization + B1 external/irreversible action gate + C1 protected Sync registry write

## Verdict

**The existing Apex contracts can carry commit-time authorization with small field extensions. A new authorization subsystem is not justified by the spike.**

The lowest-complexity path is:

1. keep the operator-approved packet as the durable authorization witness container;
2. carry only stable reference/id/digest information downstream;
3. reuse Weekly's existing `authority.basis_digest` and `operator_validation` fields;
4. let the actual durable-write boundary revalidate the witness immediately before the effect;
5. fall back to fresh operator confirmation whenever the witness is absent, stale, changed, expired, revoked, out of scope, or blocked by an existing hard safety rule.

The executable carrier spike produced:

- policy correctness: `17/17`;
- unsafe allows: `0`;
- overblocks: `0`;
- repeated operator gates across 50 unchanged covered internal actions: `0`;
- new task gate field required: `false`;
- new global authorization registry required: `false`;
- new daemon/service required: `false`;
- reusable-authorization changes required in Apex Sync: `0` for the core fix.

These are design-spike results, not a production safety proof.

## Compatibility map

| Contract | Existing carrier | Minimal extension | What must not change |
|---|---|---|---|
| Apex Plan | `operator_gate` and approved handoff state | On approval, freeze/reference an `authorization_witness` containing id, authority ref, basis digest, allowed actions, target scope, constraints, lifecycle | Plan remains proposal-only; no mutation ownership; no task `gate_mode` |
| Weekly Orchestrator / handoff | `operator_validation`, `authority.state`, `authority.basis_digest`, `verification_ref` | Add `authorization_id` and `authorization_ref` only when a confirmed packet is intended to confer reusable internal authority | G1-G5 semantics, review wiring, digest invalidation, fail/hold routing remain |
| Apex Status Merge | G5 proposal/confirmed packet routed to Session | Preserve/pass the existing authorization reference/digest; no independent authorization engine | Remains proposal/status-merge boundary, not canonical writer authority |
| Apex Session | `operator_validation`, before/after mutation preview, confirmed mutation record | Accept authorization id/ref/digest and allow `fresh operator confirmation OR valid commit-time witness` as the confirmation basis | source conflicts, duplicate risk, operator judgment, explicit manual overrides remain hard gates |
| Apex Sync | dry-run-first contract; explicit operator request for registry non-dry-run | **None for the core redesign** | C1 explicit registry write request remains |
| Canonical task record | task/status/priority/dates/dependencies/acceptance/DoD/notes/source | **None** | Do not add task-wide authorization or `gate_mode` |

## Why this is not a subsystem

The approved packet itself is the evidence container. `authorization_ref` points at that packet. The downstream packet carries a few scalar references, not a replicated policy document.

No new component is needed for:

- authority lookup;
- lifecycle storage;
- inheritance;
- authorization scheduling;
- authorization caching;
- operator decision storage;
- task policy fields.

A deterministic validation helper may be warranted later only if the production checks become error-prone to repeat as prose. That helper would be a local skill script/reference implementation, not a service.

## Important boundary found by the spike: physical durable writer is under-specified

The current Session mutation-gate rules state that final mutation records **do not imply silent repo writes** and are authoritative input to a later explicit file-application flow. At the same time, the Weekly orchestration wording describes Session as the actor that validates/applies confirmed mutation and produces a receipt.

Repository search and inspection of the current `apex-session` package did not identify a separately named `file-application` skill or writer contract. The current Session package contains the Session skill, four reference contracts, templates, package manifest, extraction report, and harmonization notes; no separately named application/writer component was found.

This is an existing contract ambiguity, not evidence that a new writer subsystem is needed.

### Required commit-boundary rule

A1′ must be checked immediately before the actual durable effect:

- **If Session is the effective writer** (including an immediate file-application step it owns), Session performs the final commit-time authorization check.
- **If a distinct downstream file-application actor exists**, Session passes the witness and that writer must revalidate it immediately before the repo write.
- **If no explicit writer contract currently exists**, implementation should clarify the existing Session/application boundary in the smallest possible contract edit. Do not create a new actor merely to host authorization validation.

## Recommended production policy location — operator decision still needed

### P1 — Session-owned canonical reference — **recommended**

Create one canonical policy reference at:

`.claude/skills/apex-session/references/authorization-policy.md`

Reasoning:

- Session currently owns confirmed mutation semantics and mutation validation;
- the authorization check exists primarily to decide whether a durable mutation requires a new operator decision;
- Plan and Weekly need only carrier instructions;
- keeping the policy near the mutation boundary minimizes cross-skill policy duplication.

If later discovery proves that multiple independent durable writers need the same full validator, move/share it then rather than predicting that need now.

### P2 — shared Workflow & Processes policy

Place the canonical policy in a shared Workflow & Processes reference from the start.

Potential advantage: neutral home if many writers consume it.

Cost/risk: creates a shared abstraction before the current repository demonstrates more than one actual durable writer, increasing discovery/context overhead and making the small Plan-to-Session fix look like a framework.

**Recommendation: P1 unless the unresolved physical-writer investigation reveals multiple independent writers.**

## Writer-boundary handling recommendation

### W1 — clarify the existing boundary — **recommended**

During production implementation, identify the exact current file-application step and state that commit-time authorization is revalidated there. If the step is implicit, clarify it inside the existing Session contract/reference.

### W2 — create a dedicated writer/authorization subsystem

Do not do this without new evidence. The carrier spike gives no requirement for it.

## Likely production edit surface if P1/W1 are approved

Minimum expected files:

1. `.claude/skills/apex-plan/SKILL.md`
   - small carrier/output change only.
2. `.claude/skills/apex-session/SKILL.md`
   - replace unconditional fresh confirmation with fresh confirmation **or** valid commit-time witness.
3. `.claude/skills/apex-session/references/mutation-gate-rules.md`
   - reference canonical authorization policy and clarify final write boundary.
4. `.claude/skills/apex-session/references/authorization-policy.md`
   - new canonical reference containing the compact contract/check order.
5. `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
   - add minimal authorization reference/id fields to the existing authority envelope.

Possible only if wording requires it:

- `.claude/skills/weekly-orchestrator/SKILL.md` — pass-through wording, not a second policy copy.
- `.claude/skills/apex-status-merge/SKILL.md` — pass-through wording only if its existing G5 handoff is otherwise ambiguous.

Expected no-change files for the core fix:

- `.claude/skills/apex-sync/SKILL.md`;
- `.claude/skills/apex-plan/references/task-record-contract.md`;
- `.claude/skills/apex-session/references/state-delta-and-entity-rules.md` unless a one-line cross-reference is needed.

## Production acceptance threshold

Do not call the redesign complete unless production skill changes preserve the spike's architectural properties:

- no duplicate approval for exact authorized serialization;
- zero silent authority expansion from task/parent inheritance;
- B1 external/irreversible actions still stop;
- C1 Sync registry write still stops without explicit request;
- changed/revoked/expired authorization fails closed;
- source conflict and duplicate identity risk override reusable authorization;
- approval survives process/chat restart only through durable repository evidence;
- the actual writer revalidates immediately before the durable effect;
- one canonical policy, not repeated policy prose across skills;
- no new global registry/service/daemon unless later empirical evidence demonstrates a missing capability.

## Current decision boundary

The spike supports the minimal architecture. Before production skill edits, the remaining material architecture choice is small:

- **P1 (recommended):** canonical policy under Session references;
- **P2:** shared Workflow & Processes reference.

For the physical writer, W1 is a contract-clarification recommendation rather than a request to invent a new component. If repository evidence later identifies a distinct writer, bind the final validation there.
