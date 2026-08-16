---
title: "Leela Core Interaction Checkpoint 03 — Home to Skill Tree Scope Slice"
document_role: iterative_planning_checkpoint
created: 2026-08-16
status: completed_evidence_pass
project: leela-core-interaction-development
predecessor: apex-meta/handoff/plan-packets/leela-core-interaction-checkpoint-02-skill-tree-routing-20260816.md
---

# Home -> Skill Tree -> Scope Resolution Vertical Slice

## Read-before-next-step rule

This checkpoint is durable context. Read it with the main plan packet and checkpoints 01/02 before deriving implementation tasks or moving to another Leela workstream.

## Evidence inspected

Repository `leela-spec/Leela-Cloud-2026`, branch `master`:

- `lib/models/scope_selection.dart`
- `lib/models/resolved_scope.dart`
- `lib/pages/s_c_r_picker_scope.dart`
- `lib/globals/g_s_spark.dart` (from prior Home evidence pass)
- `lib/features/skill_tree/skill_cluster_controller.dart`
- `lib/features/skill_tree/s_c_r_skill_cluster.dart`
- `docs/ssot/features/skill-tree/spec.md`
- `docs/ssot/features/algorithm/spec.md`
- `docs/ssot/features/sequencing/canon/10-meso/07-cross-feature-contracts.md`
- `docs/ssot/screens/home-today.md` (from prior Home evidence pass)

## Contract truth

### ScopeSelection

Current `ScopeSelection` is the canonical Skill Tree output contract. It carries:

- selectionId
- scopeType
- selected Epic IDs
- selected Block IDs
- selected Chunk IDs
- primaryLabel
- focusNodeId
- breadcrumbLabels
- selectionMode
- userConfirmed
- createdAtIso

Current known debt: breadcrumb lineage is label-only rather than typed node references/versioned lineage.

### Skill Tree ownership

Skill Tree owns structural discovery and explicit confirmed scope selection. An Epic/Block selection may remain abstract. It must not silently expand visible descendants into authoritative executable Chunks.

### Algorithm ownership

Algorithm consumes one confirmed `ScopeSelection` inside a frozen `ResolutionContext`. It owns eligibility-aware concrete Chunk binding, hard feasibility, TP/XP/BP calculation, candidate ranking, typed exclusions, and `DecisionTrace`.

Algorithm must stay inside the confirmed user scope and must not replace or widen it.

### Sequencing ownership

Sequencing owns executable structure and candidate/Instance representation. A resolved Chunk set is not canonical executable structure.

### Home ownership

Home is a non-owning presentation/composition surface. It may hold draft scope/duration request state and trigger fresh resolution, but may not calculate or resolve domain truth itself.

## Current runtime mismatch

### A. Home scope control is confirmation UI, not discovery

`SCRHomeToday.fn_openScopePicker()` opens `SCRPickerScope`.

`SCRPickerScope` reads `GS_Spark.g_scope` and `g_resolvedScope`.

If `g_scope == null`, it only displays:

> No scope selected — Pick a node from the SkillTree to start

It does not itself navigate into the current Skill Tree discovery surface.

### B. Picker resolution uses legacy Skill Tree plane

On confirmation, `SCRPickerScope` calls:

- `spark.confirmScopeSelection()`
- `spark.resolveSelection(skillTree.treeModel)`

That resolution path depends on legacy `GS_SkillTree.treeModel`, not the newer `SpatialRepository`/`SkillClusterController` architecture and not the current Algorithm `ResolutionContext` contract.

### C. Bounded Skill Tree produces canonical selection but forces Path navigation

`SkillClusterController.buildScopeSelection()` correctly builds `ScopeSelection` from the selected Epic/Block/Chunk + lineage.

`SCRSkillCluster._confirmSelection()` currently:

1. writes the selection into `GS_Spark`;
2. clears pending selection;
3. shows a snackbar;
4. pushes `HarmonizedPathScreen`.

This means the Skill Tree handoff semantics are coupled to one destination even though the cross-feature contract states that entry source affects navigation context, not domain semantics.

### D. GS_Spark starts with fake scope truth

`GS_Spark.g_scope` is currently seeded with a hard-coded German Music `ScopeSelection` where `userConfirmed=false`, and `g_resolvedScope` is also hard-coded.

Although not marked confirmed, this means Home/picker state does not represent a clean absence of user scope and creates ambiguity during first real integration.

### E. ResolvedScope is transitional debt

`ResolvedScope` stores a flat `resolvedChunkIds` set with default strategy `visible_chunk_descendants`.

Current SSOT explicitly treats this as downstream transitional/legacy debt: Algorithm must resolve lowest-level eligible content under frozen context, not simply all visible descendants, and the flat set must not become execution authority.

## Smallest evidence-supported vertical slice

The first real integrated slice should be limited to **scope discovery and request propagation**, not full end-to-end execution.

```yaml
vertical_slice:
  name: home_skilltree_confirmed_scope_to_fresh_resolution_request

  start:
    screen: SCR_Home_Today
    action: user opens Skill Tree / scope discovery from Home

  discovery:
    surface: bounded spatial Skill Tree
    canonical_runtime: SCRSkillCluster + SpatialRepository + SkillClusterController
    user_actions:
      - browse hierarchy
      - drill Epic -> Block -> Chunk
      - select Epic, Block, or Chunk
      - explicitly confirm selection

  handoff:
    contract: ScopeSelection
    requirements:
      - explicit user confirmation
      - preserve selected IDs
      - preserve focus/lineage context
      - no Skill Tree-owned resolution into executable chunks
      - no silent scope widening

  return_context:
    rule: >
      Preserve entry origin so Home-origin scope discovery can return to the
      Home request surface rather than forcing Path. Exact route/parameter
      mechanism remains an implementation decision; do not create a second
      ScopeSelection contract.

  home_state:
    rule: >
      Home renders the confirmed selection as request context and may combine
      it with explicit duration/mode narrowing. Home does not calculate candidates.

  resolution_boundary:
    owner: Algorithm
    target_contract: fresh fingerprinted ResolutionContext
    consumes:
      - confirmed ScopeSelection
      - Rhythm current-window snapshot/context
      - optional Path demand
      - Content eligibility
      - Sequencing grammar
      - explicit Home request narrowing
    produces:
      - ResolutionCandidate alternatives
      - or typed NoFeasibleCandidate
      - DecisionTrace

  out_of_scope_for_first_slice:
    - SequenceInstance acceptance
    - Rhythm placement mutation
    - Run execution
    - Stats realization
    - full replacement of every Home mock seam
    - complete backend migration of Skill Tree status/progress
```

## Implementation-task implications

### VS-1 — Make canonical spatial Skill Tree reachable from Home

- Home's Skill Tree open affordance must target the bounded cluster primary surface.
- remove placeholder `/st` behavior for this path.
- preserve origin/navigation context.

### VS-2 — Make Discover use the same primary Skill Tree destination

- Discover Learn should not continue to route normal users into the retired-primary legacy list.
- legacy list remains only if intentionally preserved as fallback/accessibility/debug surface.

### VS-3 — Decouple ScopeSelection confirmation from forced Path navigation

- `SCRSkillCluster` confirmation must emit/store the same canonical `ScopeSelection` regardless of entry source.
- navigation after confirmation must respect origin context without changing selection semantics.
- Home-origin selection should return to the Home request context instead of unconditionally pushing Path.

### VS-4 — Remove fake initial scope truth from the real path

- the integrated path must support `g_scope == null` as a valid clean state.
- hard-coded German Music scope/resolved scope must not be treated as current user state.
- fixtures may remain only where explicitly test/demo scoped.

### VS-5 — Retire Home picker's legacy resolution responsibility

- `SCRPickerScope` should not be the authoritative resolver over `GS_SkillTree.treeModel`.
- it may remain a review/confirmation presentation if useful, but concrete resolution belongs to Algorithm.
- do not promote `visible_chunk_descendants` as final resolution semantics.

### VS-6 — Establish fresh resolution-request seam

- confirmed Skill Tree selection + Home duration/mode narrowing triggers a fresh owner-safe resolution request/context.
- use current Algorithm contract as target semantics.
- exact runtime service/class implementation requires separate evidence from Algorithm materialization before coding.

### VS-7 — Validate first slice

Prove:

1. Home -> canonical Skill Tree works.
2. user can select at Epic/Block/Chunk granularity.
3. confirmation creates one canonical `ScopeSelection`.
4. Home-origin flow returns to Home context.
5. no fake initial scope is mistaken for user truth.
6. no legacy `GS_SkillTree.treeModel` resolution is required for the integrated path.
7. the next resolution step receives the confirmed scope without widening/mutating it.

## Dependency implication

The previous broad plan should be revised so that Skill Tree routing/scope integration precedes broad Home mock replacement. Not every Home seam is needed to validate the first Home -> Skill Tree slice.

Suggested qualitative dependency order:

- Home/Skill Tree audit evidence: complete planning input
- bounded Skill Tree runtime verification
- primary route/navigation reconciliation
- origin-aware canonical ScopeSelection handoff
- fake/legacy scope-state quarantine
- Algorithm resolution seam materialization audit
- first integrated slice validation
- only then broader Home owner-backed data replacement

Exact next-task computation remains Apex Sync scope after canonical records exist.

## Next evidence step

Inspect Algorithm materialization/current runtime symbols relevant to `ResolutionContext`, `ResolutionCandidate`, and Home integration. Determine whether the fresh resolution seam already exists in code or must be built. Save that evidence before finalizing the revised main Apex Plan packet.
