---
title: "Leela Core Interaction Checkpoint 02 — Skill Tree Route Reconciliation"
document_role: iterative_planning_checkpoint
created: 2026-08-16
status: completed_evidence_pass
project: leela-core-interaction-development
predecessor_worklog: apex-meta/handoff/plan-packets/leela-core-interaction-development-worklog-20260816.md
---

# Skill Tree Route Reconciliation

## Read-before-next-step rule

This checkpoint is durable planning context. Subsequent work must read it together with the main plan packet and prior worklog before deriving Home -> Skill Tree implementation tasks.

## Evidence inspected

Repository `leela-spec/Leela-Cloud-2026`, branch `master`:

- `lib/globals/router.dart`
- `lib/pages/s_c_r_skill_tree.dart`
- `lib/globals/g_s_skill_tree.dart`
- `lib/components/s_t_r3_tree_area_bound.dart`
- `lib/pages/s_c_r_discover_hub.dart`
- current Skill Tree SSOT/materialization from prior checkpoint

## Confirmed routing state

The router registers both surfaces:

- legacy `SCR_SkillTree.route` = `/skill-tree`
- bounded spatial `SCRSkillCluster.route` = `/skill-cluster`

`router.dart` explicitly comments that `BoundedClusterLayout` behind `SCRSkillCluster.route` is the canonical engine after retiring older spatial engines.

However, current user-facing Discover behavior still sends the Learn tile to `/skill-tree`.

Search for `SCRSkillCluster.route` returned only router/materialization references and no normal in-app navigation caller. Therefore the conforming bounded spatial surface is registered but effectively hidden from standard navigation.

## Legacy `/skill-tree` state

`SCR_SkillTree` remains a large Nowa-generated screen with substantial obsolete/prototype behavior:

- route `/skill-tree`;
- hard-coded stats/distribution/health values;
- search query placeholder;
- old tree model loaded through `GS_SkillTree`;
- `ST_R3TreeAreaBound` delegates to `WGT_ST_TreeView`, the recursive indented legacy renderer;
- chunk info text includes mastery-oriented wording (`"Explore this unit to master your skills"`), conflicting with current no-universal-mastery SSOT direction;
- several interactions remain placeholders/dialogs.

`GS_SkillTree` is a parallel legacy state plane:

- loads via `SupabaseService().q_skill_tree_nodes(epicId)`;
- builds a nested mutable tree model;
- owns expanded IDs, selected ID, breadcrumb labels, mock state, and `MockScopeSelection`;
- does not enforce the current deterministic sibling sort policy itself;
- coexists with the newer `SpatialRepository` + `SkillClusterController` + canonical `ScopeSelection` path.

This creates two parallel Skill Tree architectures:

1. legacy `/skill-tree`: `GS_SkillTree` -> nested maps -> `WGT_ST_TreeView`
2. current `/skill-cluster`: `SpatialRepository` -> `SpatialAdapter` -> `SpatialViewNode` -> `SkillClusterController` -> `BoundedClusterView` -> canonical `ScopeSelection`

The current SSOT/materialization already marks architecture 2 as conforming and architecture 1 as `to_change`/fallback-oriented.

## Home/Discover entry implication

Current Home is not yet a valid Skill Tree entry either:

- Home's feature-tab data uses placeholder routes such as `/st`;
- Home's `p_onOpenTab` callback is currently empty.

Thus there is currently no clean Home -> conforming Skill Tree path.

Discover is the clearest existing user-facing Skill Tree entry, but it points to the legacy surface.

## Planning conclusion

The next Leela implementation slice should not create another Skill Tree renderer or another state model.

The evidence-supported surface migration is:

1. make the bounded cluster the primary Skill Tree destination for normal navigation;
2. preserve the legacy list only as an explicit accessibility/debug fallback if current requirements still require it;
3. wire Home's Skill Tree feature-open affordance to the primary Skill Tree destination;
4. update Discover Learn to the same destination;
5. avoid migrating legacy `GS_SkillTree`/`MockScopeSelection` state into the new surface unless a current contract requires it;
6. validate bounded cluster visually and behaviorally before deleting/retiring fallback paths;
7. preserve canonical `ScopeSelection` output from `SkillClusterController`.

## Candidate task refinement

The old broad Task 7 `Audit existing Skill Tree implementation and current contracts` can now be considered planning-evidence complete and should be replaced in the implementation proposal by narrower tasks:

### ST-A — Verify bounded spatial Skill Tree runtime

- run `/skill-cluster` in supported runtime;
- check hierarchy, breadcrumbs, paging, drill-down, selection, long-press, confirmation, empty/error states, responsive behavior, reduced-motion behavior;
- identify visual/layout/runtime defects without creating new architecture.

### ST-B — Promote bounded cluster to primary Skill Tree navigation

- Home Skill Tree open affordance -> canonical Skill Tree destination;
- Discover Learn -> canonical Skill Tree destination;
- router/route naming reconciled without creating duplicate semantics;
- legacy `/skill-tree` explicitly retained as fallback or retired based on verified runtime need.

### ST-C — Retire/quarantine legacy Skill Tree state drift

- no user-facing path depends on hard-coded legacy stats/health/mastery semantics;
- hard-coded/mock `GS_SkillTree` state does not become canonical;
- legacy mastery wording and `mastered` visual mapping are quarantined/removed where the current slice touches them;
- fixture-only status/progress remain explicitly non-authoritative.

### ST-D — Validate canonical scope handoff

- Epic/Block/Chunk selection produces canonical `ScopeSelection`;
- no abstract selection is silently resolved by Skill Tree;
- Home/Algorithm downstream consumers can distinguish unconfirmed vs confirmed scope;
- hard-coded `GS_Spark.g_scope` seed does not masquerade as user intent.

## Next evidence step

Inspect current `ScopeSelection`, `ResolvedScope`, Home scope picker, and Algorithm/Sequencing cross-feature contracts to define the smallest real Home -> Skill Tree -> scope-resolution vertical slice. Persist that slice definition before updating the main Apex Plan packet.
