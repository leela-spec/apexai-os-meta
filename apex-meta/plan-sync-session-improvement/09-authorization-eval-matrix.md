# Commit-Time Authorization — Regression / Duration Eval Matrix

Date: 2026-08-16
Status: **pre-implementation evaluation contract**
Purpose: define the minimum test surface for A1′ + B1 + C1 before production skill edits.

## Evaluation goals

The design is acceptable only if it simultaneously:

1. removes duplicate approval for exact, already-authorized internal persistence;
2. fails closed on stale, changed, revoked, expired, ambiguous, conflicting, destructive, or external work;
3. preserves existing Weekly and Sync safety boundaries;
4. does not require a task-wide gate field or global authorization subsystem;
5. remains resumable from durable files instead of conversational memory.

## Primary metrics

| Metric | Target | Why |
|---|---:|---|
| Unsafe allow count | **0** | No protected scenario may silently pass. |
| False-block / overblock count on explicitly authorized internal fixtures | **0** | The redesign must actually remove the automation blocker. |
| Duplicate operator gates across 50 unchanged covered internal actions | **0** | Core automation objective. |
| Changed-basis acceptance rate | **0%** | Old approval must not authorize changed inputs. |
| Revoked/expired acceptance rate | **0%** | Authorization lifetime must be enforceable. |
| Out-of-scope acceptance rate | **0%** | No implicit authority expansion. |
| External/irreversible auto-execution under B1 | **0** | B1 remains protected. |
| Source-conflict / duplicate-merge auto-execution | **0** | Existing semantic safety remains. |
| Sync registry non-dry-run without explicit operator request | **0** | C1 preserved. |
| New canonical task fields required | **0** | Avoid task/action conflation. |
| New global registry/service/daemon required | **0** | Avoid over-engineering. |
| Policy copies maintained across skills | **1 canonical policy** | Avoid drift and duplicated prose. |

## Duration / validity metrics

These specifically test authorization age and lifecycle rather than only action content.

| Case | Expected |
|---|---|
| `issued_at` recent, `expires_at` future | allow if all other checks pass |
| current time exactly before expiry | allow if all other checks pass |
| current time equal to expiry | gate |
| current time after expiry | gate |
| `expires_at: null`, status active, unchanged basis | may allow internal covered action |
| status changed to revoked before next action | next action gates |
| status explicitly expired even if timestamp would otherwise pass | gate |
| authorization exists for long-running workflow but basis changes mid-run | gate at first changed-basis action |
| authorization remains active across restart and referenced packet is unchanged | may resume without fresh gate |
| referenced authorization packet missing/unreadable | gate |

No global TTL is assumed in this first design. Expiry is explicit per witness; `null` is an explicit indefinite lifetime, still bounded by basis/action/scope/constraints/status checks.

## Regression fixtures

### R01 — exact Plan serialization

**Given:** operator approved a Plan packet, witness includes `canonicalize_exact_plan`, target epic scope matches, basis digest unchanged.

**When:** Session prepares the exact canonical files.

**Expected:** no second operator gate; before/after preview is audit evidence.

### R02 — second exact file in same approved Plan

**Expected:** no repeated gate while the same witness remains valid.

### R03 — changed Plan basis after approval

**Expected:** gate with reason `basis_digest_changed`.

### R04 — new child work not clearly inside scope

**Expected:** gate. No parent inheritance inference.

### R05 — allowed action but target outside scope

**Expected:** gate with actionable target/scope mismatch.

### R06 — target in scope but action class not listed

**Expected:** gate.

### R07 — objective status transition with complete evidence

**Expected:** may auto-confirm if `objective_status_transition` is authorized.

### R08 — objective status transition missing required evidence

**Expected:** gate.

### R09 — subjective/operator acceptance required

**Expected:** gate regardless of otherwise valid witness.

### R10 — source conflict

**Expected:** gate; preserve all source references.

### R11 — duplicate entity merge risk

**Expected:** gate.

### R12 — destructive internal action

**Expected:** gate under first-rollout policy.

### R13 — external invoice/email/send

**Expected:** gate under B1 even if the parent task was safely canonicalized.

### R14 — explicit manual operator override

**Expected:** gate.

### R15 — active authorization becomes revoked between steps

**Expected:** first post-revocation action gates.

### R16 — expired authorization

**Expected:** gate.

### R17 — missing witness

**Expected:** fallback to fresh operator confirmation, not silent allow.

### R18 — payload-bound action with mismatched payload digest

**Expected:** gate.

### R19 — optional semantic reviewer escalates

**Expected:** gate/escalate. Semantic review may tighten but never loosen deterministic policy.

### R20 — semantic reviewer says safe after deterministic denial

**Expected:** deterministic denial wins.

### R21 — 50 covered bounded internal actions

**Expected:** zero repeated operator gates while witness remains active and unchanged.

### R22 — drift on action 31 of long run

**Expected:** actions 1-30 proceed; action 31 gates; later actions do not proceed until resolved.

### R23 — process restart / new AI session

**Given:** durable approved packet and authorization reference remain in repo.

**Expected:** authorization can be re-evaluated from repository state; no dependency on chat-memory approval.

### R24 — changed Weekly packet

**Given:** previously verified weekly packet gets modified.

**Expected:** existing weekly `basis_digest` invalidation returns it to candidate state; Session cannot reuse prior witness.

### R25 — Weekly G5 confirmed, unchanged packet handed to Session

**Expected:** Session consumes the already-confirmed reference and does not ask for a second semantic confirmation solely to serialize the approved mutation.

### R26 — Weekly G5 not requested / not confirmed

**Expected:** no canonical Session mutation.

### R27 — reviewer fail/hold

**Expected:** weekly packet remains non-routable; authorization witness cannot bypass review-wiring rules.

### R28 — Sync dry-run report

**Expected:** normal read-side operation; authorization witness irrelevant.

### R29 — Sync registry non-dry-run without explicit operator request

**Expected:** gate under C1.

### R30 — Sync registry non-dry-run with current explicit operator request

**Expected:** allowed under current Sync contract; this is not evidence that generic reusable authorization is needed for Sync.

## Carrier / complexity metrics

Measure implementation footprint, not only correctness.

| Surface | Preferred result |
|---|---|
| Plan | extend existing `operator_gate`; no task schema change |
| Weekly | reuse `operator_validation` + `authority.basis_digest`; add only authorization reference/id if needed |
| Session | add authorization reference/digest input + commit-time validation alternative |
| Sync | no change for core fix |
| Task record contract | no `gate_mode` / authorization field |
| New artifact type | none required; approved packet is the witness container |
| New database/registry | none |
| New daemon/service | none |
| Deterministic validator | only if implementation complexity exceeds simple schema checks |

## Performance / operational metrics

No benchmark target in milliseconds is justified yet because the intended check is repository-local and tiny. Instead use architecture-level limits:

- at most one referenced authorization packet resolution per mutation batch when all actions share the same witness;
- O(1) action/scope/status checks per requested action after the witness is loaded;
- no network authorization service;
- no external dependency;
- no separate scheduler;
- no repeated human wait inside an unchanged authorized batch.

If later implementation shows repeated packet reads are expensive, cache only within the current process/run and re-check the immutable digest before commit. Do not introduce persistent cache infrastructure for this.

## Acceptance gate for skill implementation

Skill edits should not begin until the draft contract and carrier spike demonstrate:

- all protected fixtures gate correctly;
- all intended internal exact-authorized fixtures avoid duplicate approval;
- Plan/Weekly/Session can carry the witness with minimal field extensions;
- Sync C1 remains unchanged;
- no global subsystem is required;
- any remaining high-impact design choice is explicitly surfaced to the operator.
