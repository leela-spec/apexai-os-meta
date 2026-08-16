---
title: "Leela Product Decisions Checkpoint 04 — Spatial Accessibility Fallback"
document_role: iterative_decision_evidence_checkpoint
created: 2026-08-16
status: narrowed_not_blocking_current_bounded_cluster
project: leela-product-decisions
qa_ids: [QA-138]
canonical_mutation_performed: false
---

# QA-138 — Must Every Spatial Surface Keep a Non-Spatial Accessible Fallback?

## Evidence read

- prior product-decisions checkpoints
- current QA-138 ledger text
- `docs/ssot/_sources/claims/P15/RUN-B-spatialplanfable-spatialchunks-skilltree.csv`
- `docs/ssot/architecture/design-system.md`
- `lib/features/skill_tree/bounded_cluster_view.dart`
- current Leela Core Skill Tree route/runtime checkpoints

## Important narrowing

The historical donor statement behind QA-138 was **not a universal rule for every spatial surface**.

Its exact context was **Option 2B, the free-pan/zoom Skill-Galaxy**:

- a free 2D surface has no natural reading order;
- therefore the donor proposed keeping `WGT_ST_TreeView` as a switchable accessible alternative;
- manual semantic traversal order would also be required.

The QA row generalized this into a broader question: whether *every* spatial surface must preserve a non-spatial fallback.

## Current canonical bounded cluster is materially different

`BoundedClusterView` is not an unbounded free canvas.

Current implementation already provides:

- bounded visible nodes;
- deterministic spatial layout input;
- explicit `FocusTraversalOrder` with numeric order;
- semantic labels on `LeelaCube` carrying node name, branch and lifecycle;
- captions inside the interactive target;
- reduced-motion support elsewhere in the design system.

Current design-system accessibility contract requires:

- keyboard/focus order follows reading and spatial lineage;
- state not encoded by color alone;
- reduced motion preserves state;
- bounded visible subsets;
- screen readers receive semantic level/name/branch/state/selection/actions.

It does **not** currently require a second non-spatial view for a bounded surface that can satisfy those requirements directly.

## Consequence for current Leela Core milestone

QA-138 should no longer be treated as a blocker to making `/skill-cluster` the primary Skill Tree surface.

Instead:

1. runtime/accessibility verification of the bounded cluster is required;
2. any concrete missing semantic fields/actions/focus problems must be repaired;
3. the legacy `/skill-tree` list should not remain primary merely because QA-138 exists;
4. retention of the legacy list as a supported accessibility fallback is a separate product/architecture choice after conformance is measured.

## What remains genuinely open

A broad policy decision still exists for **spatial surfaces that cannot provide a natural deterministic reading/focus order**.

User-facing question for later batch:

> When Leela uses a spatial surface that cannot itself provide a clean screen-reader/keyboard reading order, must it always provide a switchable structured/list alternative, or may it use another accessibility projection designed for that surface?

### A — Require a non-spatial alternative for any spatial surface that cannot satisfy accessibility directly — recommended principle

- bounded cluster may satisfy accessibility directly and need no duplicate list;
- free canvas/galaxy would require an accessible projection;
- projection does not have to be the legacy `WGT_ST_TreeView` implementation forever.

### B — Every spatial surface must always have a list/outline toggle

- simplest universal policy;
- creates duplicate UI and maintenance even where the primary surface already has deterministic semantics.

### C — No fallback requirement; accessibility only within the primary surface

- lowest maintenance;
- would make genuinely free spatial canvases difficult or impossible to use non-visually unless their interaction model is substantially constrained.

Recommendation basis: **A** expresses the actual accessibility requirement rather than preserving a historical widget implementation.

## Legacy list disposition for first milestone

```yaml
legacy_skill_tree_list:
  primary_route_status: should_not_remain_primary_due_to_QA_138
  deletion_authorized_now: false
  safe_first_milestone_action:
    - route normal Home/Discover use to bounded cluster after runtime verification
    - keep legacy list temporarily reachable only if needed for comparison/fallback
    - do not delete until bounded-cluster accessibility acceptance is verified
  later_decision:
    - archive/delete/replace legacy list after accessibility proof and QA-138 policy closure
```

## QA disposition

```yaml
qa_disposition:
  QA-138:
    classification: evidence_narrowed_broad_policy_choice_remains
    blocks:
      - future_free_canvas_accessibility_policy
      - final_deletion_of_legacy_fallback_without_replacement
    does_not_block:
      - bounded_cluster_primary_routing
      - Home_to_bounded_cluster_integration
      - Discover_to_bounded_cluster_integration
    recommended_principle: require_accessible_projection_when_primary_surface_cannot_satisfy_accessibility_directly
```

## Next workstep

Evidence-sweep QA-73 (`harmonization/` ownership). Determine whether current repository evolution has already split its responsibilities into named owners sufficiently that the question can be narrowed from "12th feature or archive?" to a concrete migration/namespace decision.
