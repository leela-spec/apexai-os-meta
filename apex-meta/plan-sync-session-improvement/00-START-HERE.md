# Apex Plan / Sync / Session Improvement — Start Here

Status: **contract/eval/carrier spike complete; production skills not yet redesigned**
Date: 2026-08-16
Canonical folder: `apex-meta/plan-sync-session-improvement/`
Repository: `leela-spec/apexai-os-meta`
Branch: `main`

## Purpose

This folder is the durable project home for the Apex Plan / Sync / Session authorization and gate-improvement work.

It consolidates:

- the original redesign/validation handover;
- repository-grounded independent validation;
- pressure-test simulation and raw output;
- external production-pattern/web research;
- operator decisions;
- the minimal A1′ authorization contract draft;
- lifecycle/duration and regression eval criteria;
- an executable carrier spike across Plan / Weekly / Session with the Sync C1 boundary;
- the resulting compatibility map and remaining decision boundary.

Another AI should be able to resume from this folder without reconstructing design state from chat history.

## Current operator-validated direction

- **A1′ — commit-time action authorization:** reuse prior approval only when the exact pending durable action is still covered by an active witness whose basis, action class, target scope, constraints, lifecycle, and required evidence still match immediately before the durable effect.
- **B1 — external / irreversible actions remain action-specifically gated in the first rollout.**
- **C1 — preserve the current Apex Sync explicit authorization requirement for non-dry-run registry writes.**
- Deterministic authorization checks precede optional AI semantic review.
- AI semantic review may escalate; it cannot override a deterministic denial.
- No task-wide inherited `gate_mode` as the canonical authority primitive.
- Weekly Orchestrator G1-G5 remain intact.
- No new authorization service/registry/daemon or task schema unless later evidence proves a concrete missing capability.

See `06-operator-decisions-and-current-direction.md` for the decision ledger.

## Reading order

1. `01-original-validation-handover.okf.md` — original proposal and independent-validation mission.
2. `02-independent-validation-report.md` — repository-grounded validation and failure-mode analysis.
3. `03-gate-policy-simulation.py` — first reproducible design pressure-test.
4. `04-simulation-results.txt` — raw first simulation output.
5. `05-external-web-benchmark.md` — external validation against production frameworks, skill guidance, web-search patterns, and primary research.
6. `06-operator-decisions-and-current-direction.md` — operator decision ledger.
7. `07-source-and-history-index.md` — source paths, commits, branch history, and evidence map.
8. `08-authorization-policy-contract-draft.md` — small canonical A1′ contract draft.
9. `09-authorization-eval-matrix.md` — lifecycle/duration, safety, automation, and complexity eval criteria.
10. `10-carrier-spike.py` — executable non-production Plan/Weekly/Session/Sync carrier spike.
11. `11-carrier-spike-results.txt` — raw carrier-spike results.
12. `12-carrier-spike-verdict-and-compatibility-map.md` — implementation footprint, compatibility map, writer-boundary finding, and remaining decision.

## Core verified problem

The current Plan -> Session path can require two operator approvals for one unchanged semantic decision:

1. Apex Plan produces proposal state and obtains operator approval for handoff.
2. Apex Session creates an exact before/after mutation preview.
3. Current Session rules can require another explicit confirmation before deterministic canonicalization.

The W34 portfolio run reproduced this behavior in the real repository.

## Current engineering result

The carrier spike supports a much smaller solution than a new authorization subsystem.

### Existing carriers are sufficient

- **Plan:** extend the existing `operator_gate` with/reference the authorization witness when approval is granted.
- **Weekly:** reuse existing `operator_validation` and `authority.basis_digest`; add only authorization id/reference where reusable authority is actually passed.
- **Status Merge:** pass the confirmed reference/digest; do not own a second policy engine.
- **Session:** accept the reference and treat consequential mutation as confirmable by either fresh operator confirmation or a valid commit-time witness.
- **Sync:** no reusable-authorization change is needed for the core fix; C1 remains separate.
- **Canonical task records:** no authorization/gate field is needed.

### Executable spike result

- `17/17` expected policy outcomes;
- `0` unsafe allows;
- `0` overblocks;
- `0` repeated operator gates across 50 unchanged covered internal actions;
- `0` new task gate fields;
- `0` new global registries/services/daemons;
- `0` Sync reusable-authorization changes for the core fix.

This is a design-spike result, not a production safety proof.

## Important boundary discovered

Session's current mutation-gate rules say final mutation records are authoritative input to a later explicit file-application flow and do not themselves imply silent repo writes. Weekly wording meanwhile describes Session as validating/applying the confirmed mutation.

Current repository/package inspection did not identify a separately named file-application/writer component.

Therefore:

- do **not** invent a new writer subsystem;
- during implementation, identify/clarify the actual existing durable-write step;
- run the final A1′ validation immediately before that effect;
- if a distinct writer is later found, pass the witness and revalidate there.

See `12-carrier-spike-verdict-and-compatibility-map.md`.

## Remaining operator architecture decision before production skill edits

### P1 — canonical policy under Session references — **recommended**

Use:

`.claude/skills/apex-session/references/authorization-policy.md`

Plan and Weekly carry/reference the witness; Session owns the canonical mutation authorization contract. If later evidence proves multiple independent writers need the complete policy, share/move it then.

### P2 — shared Workflow & Processes reference

Create a shared policy location from the start. This is only preferable if multiple independent durable writers are actually demonstrated.

**Current recommendation: P1.** It keeps the solution local to the real mutation boundary and avoids creating a framework before it is needed.

For the writer boundary, the standing recommendation is W1: clarify the existing boundary, not W2: create a new writer/authorization subsystem.

## Likely minimum production edit surface if P1 is approved

1. `.claude/skills/apex-plan/SKILL.md`
2. `.claude/skills/apex-session/SKILL.md`
3. `.claude/skills/apex-session/references/mutation-gate-rules.md`
4. `.claude/skills/apex-session/references/authorization-policy.md` (new canonical reference)
5. `.claude/skills/weekly-orchestrator/references/handoff-schema.md`

Only if pass-through wording proves necessary:

- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/apex-status-merge/SKILL.md`

Expected no-change surfaces for the core fix:

- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/apex-plan/references/task-record-contract.md`

## Preservation rule

Research, simulations, and prior reports in this folder are evidence/history. Do not silently rewrite old conclusions. Add a superseding decision/report with explicit links, evidence, and operator confirmation when direction changes.
