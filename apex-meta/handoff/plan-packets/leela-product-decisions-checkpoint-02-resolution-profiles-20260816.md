---
title: "Leela Product Decisions Checkpoint 02 — Resolution Profiles"
document_role: iterative_decision_evidence_checkpoint
created: 2026-08-16
status: evidence_narrowed_operator_choice_remains
project: leela-product-decisions
qa_ids: [QA-02, QA-11]
canonical_mutation_performed: false
---

# QA-02 / QA-11 — Resolution Profile Decision Cluster

## Evidence read

- current `OPEN_QUESTIONS.md`
- current decision registry/index
- `docs/ssot/features/algorithm/spec.md`
- `docs/ssot/features/sequencing/spec.md`
- `lib/features/sequencing/domain/resolution_context.dart`
- current Leela Core Interaction plan/checkpoints in Apex repo

## What is already defined

Current Algorithm SSOT contains a **provisional** `SEQ-RES-001` profile split:

- every resolution has exactly one profile;
- `path_bound` requires a frozen `PathDemandSnapshot` and matching demand line;
- `path_bound` takes the ST-034 priority factor from Path's integer priority 1–10;
- `ad_hoc` must not fabricate Path demand or Path priority;
- `ad_hoc` uses a versioned explicit policy factor;
- proposed `adHocPriorityFactor = 1.00` is neutral and remains blocked pending operator ratification.

Therefore the conceptual split itself is already substantially specified. Do not redesign it from scratch.

## What QA-02 actually still asks

The unresolved choice is **entry-flow mapping**.

The repository documents multiple entry sources (Home Next Best/current-window request, manual selection, Path-bound demand, Rhythm, etc.) but does not authoritatively say which of those run as `path_bound` and which run as `ad_hoc`.

This matters immediately because the first Leela vertical slice begins from Home -> Skill Tree confirmed scope.

## What QA-11 actually still asks

QA-11 is narrower than the profile concept:

- ratify the profile split as current policy;
- decide the ad-hoc priority factor, with `1.00` proposed as neutral.

Evidence strongly constrains the safe options because ad-hoc may not invent a Path priority.

## Runtime state

Packet 09 (2026-08-15) implemented `ResolutionRequest` / `ResolutionContext`, but the current runtime request:

- has no `resolutionProfile` field;
- carries no confirmed `ScopeSelection`;
- requires `pathDemandSnapshotId` and revision;
- therefore structurally behaves as Path-required even though current Algorithm SSOT describes Path demand as optional for current-window resolution.

This is an implementation/contract mismatch, not evidence that every flow should be path-bound.

## Decision packet to prepare for operator

### Decision A — Entry-flow mapping (QA-02)

User-facing question:

> When you ask Leela for an action from Home/Skill Tree, should Leela use your Path priorities whenever the selected scope has matching active Path demand, and otherwise treat the request as ad-hoc — or should Home/Skill Tree requests follow a different fixed profile rule?

Evidence-bounded versions:

#### A1 — Demand-sensitive profile selection — recommended candidate

- if confirmed scope has a matching current Path demand line -> `path_bound`;
- if there is no matching Path demand -> `ad_hoc`;
- manual/Home origin itself does not determine the profile; presence of valid Path demand does.

Consequence:

- Home can still surface planned work naturally when Path has demand;
- exploratory/manual scope does not require inventing Path data;
- aligns with the existing owner rule that Path priority exists only when Path actually owns a matching demand line.

#### A2 — Home/Skill Tree always ad-hoc unless explicitly launched from Path

- explicit Path-origin flow -> `path_bound`;
- Home/Skill Tree/other manual origin -> `ad_hoc` even when matching Path demand exists.

Consequence:

- very simple entry semantics;
- but planned Path priority is ignored merely because the user entered from Home rather than Path.

#### A3 — Home/Skill Tree always path-bound

- current-window Home requests require Path demand;
- absence of matching Path demand is an explicit failure or requires user to add Path demand first.

Consequence:

- strongest planning discipline;
- incompatible with the product idea of useful recommendations when Path is sparse unless another pool/fallback rule takes over;
- would make the provisional `ad_hoc` profile irrelevant to the primary Home flow.

Recommendation basis: A1 best preserves owner semantics while allowing Home to serve both planned and exploratory requests. This is a recommendation only, not a resolved QA answer.

### Decision B — Ad-hoc priority factor (QA-11)

User-facing question:

> When a request is genuinely outside Path demand, should it receive a neutral priority factor, be deliberately penalized relative to planned work, or receive a boost?

Versions:

- **B1 neutral 1.00 — recommended candidate:** ad-hoc neither gains nor loses XP merely for lacking Path demand.
- **B2 below 1.00:** planned Path work is structurally favored; creates a built-in planning bias.
- **B3 above 1.00:** spontaneous/ad-hoc work is structurally favored; creates an exploration bias.

Recommendation basis: B1 is the only option that does not introduce a new product preference not already evidenced elsewhere. It is still operator-owned and must not be silently ratified.

## Downstream artifacts affected after operator answer

- `docs/ssot/decisions/OPEN_QUESTIONS.md` QA-02 / QA-11
- decision registry/index
- Algorithm `SEQ-RES-001`
- `docs/ssot/features/algorithm/spec.md`
- `lib/features/sequencing/domain/resolution_context.dart`
- associated context schemas/tests/materialization
- Leela Core Interaction Task 6/7 contract reconciliation

## Planning disposition

```yaml
qa_disposition:
  QA-02:
    classification: evidence_can_narrow_but_operator_choice_remains
    recommended_candidate: A1_demand_sensitive_profile_selection
    blocks:
      - final_resolution_context_shape_for_home_skilltree_slice
  QA-11:
    classification: genuinely_operator_owned_policy_value
    recommended_candidate: B1_neutral_1_00
    blocks:
      - complete_ad_hoc_resolution_policy
```

## Next workstep

Evidence-sweep QA-100 Home override persistence separately. Do not merge it with QA-131 unless repository evidence proves they are the same state boundary.
