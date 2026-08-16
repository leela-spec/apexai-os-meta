---
title: "Leela Core Interaction Checkpoint 04 — Algorithm Resolution Seam"
document_role: iterative_planning_checkpoint
created: 2026-08-16
status: completed_evidence_pass
project: leela-core-interaction-development
predecessor: apex-meta/handoff/plan-packets/leela-core-interaction-checkpoint-03-home-skilltree-scope-slice-20260816.md
---

# Algorithm Resolution Seam Evidence

## Read-before-next-step rule

Read this checkpoint together with the main Leela plan packet and prior checkpoints before final task decomposition or implementation handoff.

## Evidence inspected

Repository `leela-spec/Leela-Cloud-2026`, branch `master`:

- `docs/ssot/features/algorithm/spec.md`
- `docs/ssot/features/algorithm/materialization.csv`
- `lib/features/sequencing/domain/`
- `lib/features/sequencing/domain/resolution_context.dart`
- prior Home/Skill Tree runtime evidence

## Important current implementation update

The Algorithm materialization ledger is newer than the initial Home evidence assumptions in one important place.

As of Packet 09 / 2026-08-15, the repository contains:

- `ResolutionRequest`
- `ResolutionContext`
- owner revision cross-validation
- deterministic context fingerprinting
- typed stale/malformed/version failures

Implementation path:

`lib/features/sequencing/domain/resolution_context.dart`

The materialization ledger explicitly records this as an implementation of the freeze/context portion of `ALG-B002`.

## What the current ResolutionContext actually contains

`ResolutionRequest` currently carries:

- request ID
- TemplateVersion ID
- PathDemandSnapshot ID + revision
- RhythmWeekSnapshot ID + revision
- schema version

`ResolutionContext` currently freezes:

- ResolutionRequest
- PathDemandSnapshot
- RhythmWeekSnapshot
- schema version
- SHA-256 fingerprint over those frozen inputs

It validates owner IDs/revisions and rejects stale/mismatched inputs.

## What is still absent from the current runtime context

Relative to the current Algorithm SSOT, the existing implementation does not yet include the full Home/Skill Tree request envelope:

- confirmed `ScopeSelection`
- explicit Epic/Block/Chunk narrowing in the request
- Home duration narrowing
- Home mode/Template/Sequence narrowing beyond TemplateVersion ID
- Content eligibility snapshot/reference
- privacy/permission/offline scope
- full policy/default provenance described by the SSOT

Therefore the existing `ResolutionContext` is a valuable foundation but not yet the complete current-window contract described in the current Algorithm spec.

## Materialization status of downstream Algorithm pieces

Current materialization states include:

- `DecisionTrace` runtime owner: `to_write`
- DecisionTrace schema/fixture/tests: `to_write`
- current-window default-window narrowing and guided-pool fallback tests: `to_write`
- eligibility engine: `to_write`
- Home integration with frozen Rhythm-aware context: `to_change`
- Algorithm context schema/fixture: still `to_write` in the older target ledger despite the newer Packet 09 runtime class

Repository search found no current runtime `ResolutionCandidate` class or `DecisionTrace` owner implementation.

Thus the first Leela slice must not assume a complete Algorithm engine already exists.

## Planning boundary

The first Home -> Skill Tree slice should integrate only up to a **valid fresh resolution request/context seam**, not attempt to deliver the entire Algorithm candidate/ranking engine as part of one task.

Evidence-supported decomposition:

### AR-1 — Extend/reconcile existing ResolutionRequest/Context for confirmed Skill Tree scope + Home narrowing

Goal:

- reuse the existing fingerprinted/revision-safe context implementation;
- add the current owner inputs needed by the Home/Skill Tree request boundary rather than create a parallel context model.

Must preserve:

- owner revision validation;
- deterministic fingerprint;
- typed stale/malformed/version failure;
- one authoritative `ScopeSelection` from Skill Tree;
- no scope widening.

Requires design/contract check before code because current SSOT describes more fields than Packet 09 currently implements.

### AR-2 — Build Home request adapter/orchestrator into ResolutionContext

Goal:

Convert:

- confirmed `ScopeSelection`
- current Home duration/mode narrowing
- current Rhythm snapshot
- available Path snapshot if path-bound
- selected/allowed TemplateVersion

into the existing/current ResolutionRequest/ResolutionContext family.

Home must not calculate rank, points, eligibility, or concrete Chunk binding.

### AR-3 — Keep candidate engine outside the first navigation/scope milestone

The following remain separate Algorithm implementation work:

- eligibility engine
- guided-pool fallback
- concrete Chunk binding
- point calculation
- deterministic candidate ranking
- `ResolutionCandidate`
- `NoFeasibleCandidate`
- `DecisionTrace`

They are required for a fully real Next Best Action, but they should not block proving the first Home -> Skill Tree -> confirmed scope -> frozen resolution-context vertical slice unless a contract requires them for interface validation.

## Revised smallest executable integration milestone

```yaml
milestone:
  name: home_to_skilltree_to_frozen_resolution_context
  proves:
    - Home opens canonical bounded Skill Tree
    - user discovers hierarchy and confirms one ScopeSelection
    - origin-aware navigation returns selection to Home request context
    - no hard-coded fake scope is treated as user truth
    - Home duration/mode narrowing is represented as request input rather than local ranking logic
    - a fresh fingerprinted ResolutionRequest/ResolutionContext is produced using current owner snapshots
    - scope identity is preserved without widening
    - stale/mismatched owner revisions fail explicitly
  does_not_require_yet:
    - complete candidate generation
    - TP/XP/BP calculation
    - candidate ranking
    - DecisionTrace rendering
    - SequenceInstance acceptance
    - Rhythm placement
```

## Critical integration risks

1. **Context-model drift:** Packet 09 implementation is narrower than the current Algorithm SSOT. Extending it incorrectly could create a second incompatible context family.
2. **Home authority creep:** Home must remain an adapter/presentation requester, not a resolver.
3. **Legacy GS_Spark coupling:** existing `GS_Spark.resolveSelection()` must not remain the authority once the new context seam is used.
4. **Fake defaults:** current hard-coded `g_scope` and `g_resolvedScope` can contaminate validation if not quarantined.
5. **Path optionality:** current `ResolutionRequest` requires a PathDemandSnapshot ID/revision, while Algorithm SSOT describes Path demand as optional in current-window resolution. This is a real contract mismatch requiring explicit reconciliation, not silent guessing.
6. **Scope missing from context:** current runtime ResolutionContext cannot yet prove which Skill Tree selection it resolved against.

## Next planning action

Update the main Apex Plan packet with the evidence-backed task decomposition from checkpoints 02–04. Preserve unresolved context-shape mismatches as review flags. Do not create canonical epic/task files yet; this remains Apex Plan proposal state.
