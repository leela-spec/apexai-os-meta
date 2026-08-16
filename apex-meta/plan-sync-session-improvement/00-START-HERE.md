# Apex Plan / Sync / Session Improvement — Start Here

Status: **research and operator-validated design direction; production skills not yet redesigned**
Date: 2026-08-16
Canonical folder: `apex-meta/plan-sync-session-improvement/`
Repository: `leela-spec/apexai-os-meta`
Branch: `main`

## Purpose

This folder is the durable project home for the Apex Plan / Sync / Session authorization and gate-improvement work.

It consolidates the evidence that was previously split between:

- the original handover on `main`;
- the independent validation branch `validation/gate-policy-20260816`;
- the pressure-test simulator and its raw results;
- the external web / production-pattern benchmark;
- operator decisions made during the validation conversation.

The goal is that another AI can resume this work from repository truth without reconstructing decisions from chat history.

## Current operator-validated direction

The operator validated the independent recommendation and then requested a second external/web validation before implementation.

Current direction:

- **A1′ — commit-time action authorization**: reuse prior approval only for the exact action when authorization is still active and its approved basis, action class, target scope, constraints, and required evidence still match at the durability boundary.
- **B1 — external / irreversible actions remain action-specifically gated in the first rollout.**
- **C1 — preserve the current Apex Sync explicit authorization requirement for non-dry-run registry writes.**
- Deterministic authorization checks should precede any AI semantic-delta review.
- AI semantic review is secondary/escalatory, not the primary permission engine.
- Do not make task-wide inherited `auto / exception_only / manual` the canonical authority primitive.
- Do not remove Weekly Orchestrator G1-G5 as part of this change.
- Do not edit production skills until the small canonical authorization contract + compatibility/eval matrix has been drafted and reviewed.

See `06-operator-decisions-and-current-direction.md` for the decision ledger.

## Reading order

1. `01-original-validation-handover.okf.md` — original proposal and independent-validation mission.
2. `02-independent-validation-report.md` — repository-grounded validation and failure-mode analysis.
3. `03-gate-policy-simulation.py` — reproducible bounded design pressure-test.
4. `04-simulation-results.txt` — raw simulation output.
5. `05-external-web-benchmark.md` — second validation against production frameworks, official skill guidance, web-search patterns, and primary research.
6. `06-operator-decisions-and-current-direction.md` — authoritative conversation decision state and next boundary.
7. `07-source-and-history-index.md` — original paths, commits, branch history, and evidence map.

## Core verified problem

The current Plan -> Session path can require two operator approvals for one unchanged semantic decision:

1. Apex Plan produces proposal state and obtains operator approval for handoff.
2. Apex Session creates an exact before/after mutation preview.
3. Current Session rules can require another explicit confirmation before deterministic canonicalization.

The W34 portfolio run reproduced this behavior in the real repository.

## Core validated design principle

> **Operator authority should be bound to a concrete action and revalidated at commit time. Mechanical persistence of already-authorized meaning should not create a second semantic approval gate.**

A durable authorization witness should minimally bind:

- authorization identity / operator decision reference;
- approved basis digest;
- allowed action class(es);
- exact target scope;
- constraints / invariants;
- validity / revocation / expiry;
- payload or mutation digest when exact payload binding is required;
- required deterministic evidence;
- exception conditions.

Before any protected durable effect, the system should deterministically re-check that witness. A changed basis, unsupported action, scope expansion, conflict, duplicate merge, missing evidence, revoked authorization, or protected external action must fail closed into an actionable operator gate.

## Important non-decisions

The following are **not** approved merely because they appeared in an earlier proposal:

- generic automatic non-dry-run registry maintenance;
- implicit parent -> child authorization inheritance when coverage is ambiguous;
- blanket automatic `done` transitions without objective evidence;
- external irreversible actions under unrelated task approval;
- a new standalone authorization subsystem/package unless later evidence proves it necessary;
- broad skill rewrites unrelated to the minimum Plan/Session/Weekly compatibility change.

## Next safe work

Before modifying any production skill:

1. Draft the smallest canonical `authorization-policy` contract.
2. Draft 10-20 regression/eval fixtures covering the validated scenarios and external-pattern failure modes.
3. Map the proposed witness fields onto current Plan, Session, Weekly Orchestrator, Status Merge, and Sync fields.
4. Prefer reuse of existing `basis_digest`, packet references, operator-validation evidence, and mutation receipts.
5. Identify whether a deterministic validator script is justified; do not create one if the checks can remain simple schema/contract validation.
6. Present any remaining high-impact architecture choices to the operator with concrete workflows, consequences, and recommendation.
7. Only then edit the affected skills consistently.

## Preservation rule

Research and validation artifacts in this folder are evidence/history. Do not silently rewrite old conclusions after later changes. Add a superseding decision/report with explicit links and reasons instead.
