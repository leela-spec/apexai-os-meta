---
title: "Leela Core Interaction Development — Evidence Worklog"
document_role: iterative_planning_checkpoint
created: 2026-08-16
updated: 2026-08-16
status: active
project: leela-core-interaction-development
source_of_truth_rule: reread_this_worklog_and_plan_packet_before_each_next_planning_stage
---

# Leela Core Interaction Development — Evidence Worklog

## Operating Rule

This file is durable intermediate context for iterative planning. Before continuing a new workstep, read:

1. `apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-core-interaction-development.md`
2. this worklog
3. the specific current Leela repository sources needed for that workstep

Do not reconstruct accepted findings from chat memory.

No canonical `apex-meta/epics/` or task state is mutated by this worklog.

---

## Workstep 1 — Home evidence correction

Status: completed planning evidence pass.

Persisted in main plan packet commit `bbe99405719debc71f9c803285e5fefaed0e83ed`.

Core finding:

- Home is not greenfield.
- `SCR_Home_Today` is the operative screen.
- locked decision: Home is a non-owning composition screen, not a feature/domain owner.
- current runtime has substantial UI but still contains mock/legacy data and recommendation wiring.
- project start changed from "define/build Home" to audit -> runtime verification -> repair selected seams -> owner-backed integration.

---

## Workstep 2 — Skill Tree evidence pass

Status: checkpoint saved; further route/runtime reconciliation follows.

### Runtime repository inspected

Repository: `leela-spec/Leela-Cloud-2026`, branch `master`.

Inspected:

- `lib/features/skill_tree/s_c_r_skill_cluster.dart`
- `lib/features/skill_tree/spatial_repository.dart`
- `lib/features/skill_tree/spatial_adapter.dart`
- `lib/features/skill_tree/skill_cluster_controller.dart`
- directory `lib/features/skill_tree/`

### Current SSOT inspected

- `docs/ssot/features/skill-tree/spec.md`
- `docs/ssot/features/skill-tree/materialization.csv`

### Confirmed runtime structure

The current bounded spatial Skill Tree is already substantial:

- `SCRSkillCluster` route `/skill-cluster` exists.
- bounded spatial cluster layout/view exist.
- hierarchy supports root focus, children, lineage/breadcrumbs, paging, drill-down, and selection.
- long-press can select Epic/Block/Chunk granularity.
- confirmed selection is converted into the existing canonical `ScopeSelection` model.
- confirmation writes the scope into `GS_Spark` and currently navigates onward to a harmonized Path screen.
- `SpatialRepository` reads `v_skill_tree_node_list` through `LeelaReadRepository` and merges `v_skill_tree_block_rollup`, with fixture fallback.
- `SpatialAdapter` performs pure row -> typed node projection and deterministic tree helpers.

### Current Skill Tree ownership from SSOT

Skill Tree owns:

- structural discovery over Life > Epic > Block > Chunk;
- structural lineage/breadcrumbs;
- deterministic node ordering;
- visual rollups and structural visual flags;
- explicit scope confirmation;
- `ScopeSelection` handoff.

Skill Tree does not own:

- progression/mastery/scoring;
- Algorithm ranking or XP/TP/BP calculation;
- Stats aggregation;
- Content Chunk metadata, prerequisites, or durable relationship edges;
- Path demand/priority;
- Sequencing structure;
- Rhythm temporal placement.

Confirmed boundary: an abstract Epic/Block scope is allowed. Skill Tree must not resolve it into executable Chunks as authoritative execution structure; downstream Algorithm resolution owns that step and must stay within the confirmed scope boundary.

### Important existing implementation status

The SSOT/materialization already marks the bounded spatial renderer as conforming/current and the old indented list surface as `to_change`:

- `BoundedClusterView` is the conforming spatial renderer.
- `/skill-cluster` is registered.
- legacy `lib/components/w_g_t_s_t_tree_view.dart` remains an indented recursive ListView.
- SSOT says the legacy list should be accessibility/debug fallback, but it is currently still effectively primary and therefore needs routing/surface disposition work.

### Concrete debts already identified by current SSOT

1. `GS_Spark.g_scope` is seeded with a hard-coded `ScopeSelection` that the user never confirmed (`userConfirmed:false` prevents it being confirmed truth, but the state is still misleading).
2. `ScopeSelection.breadcrumbLabels` contains labels only rather than typed node references, weakening lineage navigation/identity.
3. legacy `mastered` maturity mapping is drift evidence and is mandated for retirement; Skill Tree must not infer mastery from completion.
4. `status` and `progress` are fixture-only extensions until a live backend provides them.
5. `hasSuccessor` is provisional visual-only evidence and must never become a hard gate; fixture count mismatches remain deferred.
6. Content-owned durable creator relationships/prerequisites are still incomplete and must not be invented inside Skill Tree.
7. downstream `ResolvedScope.resolvedChunkIds` remains a lossy flat set and is itself tracked as `to_change`; Skill Tree must not treat it as execution authority.

### Planning consequence

The earlier Task 7 wording "audit existing Skill Tree" remains correct, but evidence now strongly suggests that the next implementation project should not be "build spatial Skill Tree". More likely sequence:

- reconcile which route/surface is actually primary (`/skill-tree` vs `/skill-cluster`);
- verify bounded cluster runtime visually/behaviorally;
- promote bounded cluster to intended primary spatial surface while preserving legacy list as fallback if still required;
- remove or quarantine known drift (`mastered`, hard-coded scope, misleading fixture-only state);
- validate the `ScopeSelection` handoff and Home entry/navigation seam;
- only then define the smallest Home -> Skill Tree -> downstream scope vertical slice.

### Next workstep

Read current router and legacy Skill Tree surface/state files to establish actual runtime entry points and determine the exact surface migration/disposition. Then update this worklog and the main Apex Plan packet before moving to Home -> Skill Tree slice definition.
