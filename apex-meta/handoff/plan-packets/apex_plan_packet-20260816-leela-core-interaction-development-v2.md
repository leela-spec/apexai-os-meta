---
okf: open-knowledge-format
okf_version: 1
title: "Apex Plan Packet — Leela Core Interaction Development v2"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
updated: 2026-08-16
status: operator_review_needed
planning_status: evidence_checked_consolidated_candidate
package: apex-plan
project: Leela
candidate_epic_slug: leela-core-interaction-development
target_week: 2026-W34
operator_gate: operator_review_needed
canonical_mutation_performed: false
supersedes:
  - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-core-interaction-development.md
source_checkpoints:
  - apex-meta/handoff/plan-packets/leela-core-interaction-development-worklog-20260816.md
  - apex-meta/handoff/plan-packets/leela-core-interaction-checkpoint-02-skill-tree-routing-20260816.md
  - apex-meta/handoff/plan-packets/leela-core-interaction-checkpoint-03-home-skilltree-scope-slice-20260816.md
  - apex-meta/handoff/plan-packets/leela-core-interaction-checkpoint-04-algorithm-resolution-seam-20260816.md
---

# Apex Plan Packet — Leela Core Interaction Development v2

## plan_packet_metadata

```yaml
plan_packet_metadata:
  package: apex-plan
  planning_status: evidence_checked_consolidated_candidate
  project: Leela
  candidate_epic_slug: leela-core-interaction-development
  target_week: 2026-W34
  source_summary:
    operator:
      - begin new development from Home, then Skill Tree
      - include data, materialization, spatial design and related foundations
      - target working versions rather than final production completeness
    durable_apex_sources:
      - original evidence-corrected plan packet
      - Skill Tree evidence worklog
      - Skill Tree route reconciliation checkpoint
      - Home -> Skill Tree scope vertical-slice checkpoint
      - Algorithm resolution-seam checkpoint
    leela_spec_repo: leela-spec/leela@main
    leela_runtime_repo: leela-spec/Leela-Cloud-2026@master
  canonical_mutation_performed: false
```

## project_capture_record

```yaml
project_capture_record:
  goal: >
    Establish the first real contract-correct Leela interaction flow by
    reusing the existing Home and bounded spatial Skill Tree implementations,
    making the canonical Skill Tree reachable from Home, preserving one
    confirmed ScopeSelection across the interaction boundary, and feeding that
    selection plus Home narrowing into the existing fingerprinted resolution
    context family without allowing Home or Skill Tree to assume Algorithm,
    Path, Rhythm, Content, Sequencing, or Stats authority.

  success_state:
    first_milestone:
      - Home is verified against the current screen contract in the running app
      - bounded spatial Skill Tree is verified in the running app
      - Home opens the canonical bounded Skill Tree instead of placeholder or legacy routing
      - Discover Learn opens the same primary Skill Tree surface
      - Epic/Block/Chunk selection yields one canonical confirmed ScopeSelection
      - Home-origin Skill Tree interaction can return to Home request context without forcing Path
      - fake initial scope/resolved-scope state does not masquerade as user truth
      - the integrated path does not depend on legacy GS_SkillTree.treeModel resolution
      - confirmed scope and Home narrowing can enter the existing ResolutionRequest/ResolutionContext family
      - scope identity is preserved without widening
      - stale/mismatched owner revisions fail explicitly

    later_follow_on:
      - owner-backed Home read models replace selected remaining mock seams
      - Algorithm candidate generation/eligibility/ranking/DecisionTrace become real
      - broader Home -> recommendation -> Sequencing execution flow becomes possible

  scope:
    in_scope:
      - Home runtime conformance verification
      - bounded spatial Skill Tree runtime verification
      - Home and Discover routing into the canonical Skill Tree surface
      - legacy Skill Tree fallback disposition
      - origin-aware ScopeSelection handoff
      - fake/legacy scope-state quarantine
      - retirement of Home picker's legacy resolver authority
      - reconciliation/extension of current ResolutionRequest/ResolutionContext for Skill Tree scope and Home narrowing
      - Home request adapter into frozen resolution context
      - first integrated vertical-slice validation
      - bounded cleanup of Skill Tree drift touched by this integration

    out_of_scope_for_first_milestone:
      - rebuilding Home from scratch
      - building another Skill Tree renderer
      - building another Skill Tree state model
      - complete backend migration of Skill Tree fixture-only status/progress
      - full Algorithm eligibility engine
      - full ResolutionCandidate implementation
      - full TP/XP/BP calculation and ranking
      - DecisionTrace implementation
      - SequenceInstance acceptance
      - Rhythm placement mutation
      - Run execution
      - Stats realization
      - broad Leela-wide product-decision closure
      - Leela project-management cleanup

  constraints:
    - Home is a non-owning presentation/composition screen
    - Skill Tree owns structural discovery and confirmed ScopeSelection only
    - Skill Tree may emit abstract Epic/Block scope and must not resolve visible descendants into execution authority
    - Algorithm resolves within confirmed scope and must not widen it
    - Sequencing owns executable structure
    - Path owns demand/priority
    - Rhythm owns temporal supply/placement
    - Content owns Chunk metadata/prerequisites/relationships
    - current repository evidence outranks older chat reconstruction
    - reuse current code/contracts before adding parallel abstractions
    - no invented deadlines

  source:
    - operator portfolio intake and clarifications 2026-08-16
    - current Home runtime and Home screen contract
    - current Skill Tree runtime, SSOT and materialization ledger
    - current Sequencing cross-feature contracts
    - current Algorithm SSOT and materialization ledger
    - Packet 09 ResolutionRequest/ResolutionContext runtime implementation from 2026-08-15

  review_flags:
    - operator_review_needed
    - resolution_context_contract_mismatch
    - path_optionality_mismatch
    - legacy_surface_disposition_requires_runtime_verification
```

## epic_record

```yaml
epic_record:
  slug: leela-core-interaction-development
  title: Leela Core Interaction Development
  goal: >
    Deliver a working evidence-backed Home -> Skill Tree -> confirmed scope ->
    frozen resolution-context vertical slice using the existing Leela
    architecture and ownership contracts.
  status: open
  priority: high
  due_date: null
  source:
    - operator 2026-08-16 portfolio direction
    - evidence checkpoints listed in plan_packet_metadata
  review_flags:
    - operator_review_needed
```

## proposed_task_records

### Task 1 — Verify Home runtime against current Home screen contract

```yaml
id: 1
title: Verify Home runtime against current Home screen contract
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - SCR_Home_Today is run in the supported local/simulator environment
  - visible layout and responsive behavior are checked
  - orb/feature preview behavior is checked
  - feature-tab interactions and open affordances are checked
  - TP/XP/BP presentation and interactions are checked
  - upcoming-event expansion/interaction is checked
  - recommendation carousel behavior is checked
  - scope and duration controls are checked
  - Pre-Run transition is checked
  - Sid/search/settings behavior is checked
  - loading/error/empty behavior is checked
  - runtime observations are compared to docs/ssot/screens/home-today.md
  - existing card/layout debt is recorded explicitly
definition_of_done:
  - an evidence-backed Home runtime conformance report exists
  - every observed gap is classified as keep, repair, mock/prototype debt, obsolete, or deferred
notes:
  - static code audit is already captured in the planning checkpoints; this task is runtime verification
source:
  - lib/pages/s_c_r_home_today.dart
  - lib/globals/g_s_data.dart
  - lib/globals/g_s_spark.dart
  - test/pages/s_c_r_home_today_lifecycle_test.dart
  - docs/ssot/screens/home-today.md
```

### Task 2 — Verify bounded spatial Skill Tree runtime

```yaml
id: 2
title: Verify bounded spatial Skill Tree runtime
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - /skill-cluster is run in the supported runtime
  - hierarchy/root focus is correct
  - deterministic child ordering is visually reflected
  - breadcrumbs/refocus work
  - bounded paging/swipe behavior works
  - Epic/Block/Chunk drill-down works
  - long-press/select-at-any-granularity works
  - pending selection tray works
  - confirmation produces the expected ScopeSelection
  - empty/error/retry states work
  - reduced-motion behavior is checked
  - responsive behavior is checked
  - fixture fallback behavior is understood
definition_of_done:
  - one bounded-cluster runtime conformance report exists
  - the surface is classified as ready for primary routing or blocked by explicit defects
notes:
  - do not redesign spatial layout unless runtime evidence proves a defect against current SSOT
source:
  - lib/features/skill_tree/s_c_r_skill_cluster.dart
  - lib/features/skill_tree/bounded_cluster_layout.dart
  - lib/features/skill_tree/bounded_cluster_view.dart
  - lib/features/skill_tree/skill_cluster_controller.dart
  - lib/features/skill_tree/spatial_repository.dart
  - docs/ssot/features/skill-tree/spec.md
  - docs/ssot/features/skill-tree/materialization.csv
```

### Task 3 — Promote bounded cluster to primary Skill Tree navigation

```yaml
id: 3
title: Promote bounded cluster to primary Skill Tree navigation
status: open
priority: high
due_date: null
depends_on: [1, 2]
blocked_by: []
acceptance_criteria:
  - Home Skill Tree open affordance reaches the bounded spatial Skill Tree
  - placeholder /st behavior is removed from the integrated Home path
  - Discover Learn reaches the same primary bounded spatial Skill Tree
  - router semantics do not create two competing primary Skill Tree destinations
  - legacy /skill-tree is explicitly retained as accessibility/debug fallback or retired based on Task 2 evidence
  - no user-facing route silently depends on obsolete mastery/stats mock semantics for the primary path
definition_of_done:
  - normal Home and Discover navigation share one primary Skill Tree surface
  - legacy surface status is explicit and documented
notes:
  - current evidence shows /skill-cluster is registered but effectively hidden while Discover routes to /skill-tree
source:
  - lib/globals/router.dart
  - lib/pages/s_c_r_home_today.dart
  - lib/pages/s_c_r_discover_hub.dart
  - lib/pages/s_c_r_skill_tree.dart
  - docs/ssot/features/skill-tree/materialization.csv
```

### Task 4 — Make canonical ScopeSelection handoff origin-aware

```yaml
id: 4
title: Make canonical ScopeSelection handoff origin-aware
status: open
priority: high
due_date: null
depends_on: [3]
blocked_by: []
acceptance_criteria:
  - SkillClusterController remains the producer of the same canonical ScopeSelection contract
  - Epic/Block/Chunk selection semantics remain identical across entry sources
  - explicit user confirmation remains required
  - Home-origin discovery can return to Home request context instead of forcing Path
  - Discover/standalone entry can preserve its intended navigation context without altering domain semantics
  - no second scope-selection DTO/state family is introduced
  - selected IDs and lineage/focus context survive the return boundary
definition_of_done:
  - one ScopeSelection contract works across Home and non-Home entry contexts
  - navigation origin changes only navigation behavior, not selection meaning
notes:
  - exact route/parameter mechanism is implementation detail; contract identity must remain stable
source:
  - lib/features/skill_tree/skill_cluster_controller.dart
  - lib/features/skill_tree/s_c_r_skill_cluster.dart
  - lib/models/scope_selection.dart
  - docs/ssot/features/sequencing/canon/10-meso/07-cross-feature-contracts.md
```

### Task 5 — Quarantine fake and legacy scope-resolution state

```yaml
id: 5
title: Quarantine fake and legacy scope-resolution state from the integrated path
status: open
priority: high
due_date: null
depends_on: [4]
blocked_by: []
acceptance_criteria:
  - null/no-scope is a valid clean initial state for the integrated Home path
  - hard-coded German Music g_scope is not treated as current user intent
  - hard-coded g_resolvedScope is not treated as current resolution truth
  - SCRPickerScope no longer acts as authoritative resolver over GS_SkillTree.treeModel for the integrated path
  - legacy visible_chunk_descendants resolution is not promoted as final Algorithm semantics
  - legacy GS_SkillTree/MockScopeSelection state is not copied into the bounded-cluster architecture
  - fixture/demo defaults remain explicitly scoped to tests/demo behavior only
definition_of_done:
  - integrated Home -> Skill Tree flow cannot succeed using fabricated scope or legacy resolver truth
  - one clear boundary exists between confirmed Skill Tree scope and downstream resolution
notes:
  - picker may remain as review/presentation UI if useful; it must not own concrete resolution
source:
  - lib/globals/g_s_spark.dart
  - lib/globals/g_s_skill_tree.dart
  - lib/pages/s_c_r_picker_scope.dart
  - lib/models/resolved_scope.dart
  - docs/ssot/features/skill-tree/materialization.csv
```

### Task 6 — Reconcile ResolutionRequest/ResolutionContext with current Home and Skill Tree contracts

```yaml
id: 6
title: Reconcile ResolutionRequest and ResolutionContext with current Home and Skill Tree contracts
status: open
priority: high
due_date: null
depends_on: [4]
blocked_by: []
acceptance_criteria:
  - existing Packet 09 ResolutionRequest/ResolutionContext implementation is reused rather than duplicated
  - confirmed ScopeSelection identity can be frozen into or referenced by the resolution context family
  - explicit Home duration/mode/request narrowing has a versioned/fingerprinted representation
  - owner revision/fingerprint validation remains intact
  - stale/mismatched owner inputs still fail explicitly
  - Path optionality mismatch is explicitly resolved against current Algorithm SSOT
  - current implementation and SSOT agree on required context inputs for the first milestone
  - no Home-local ranking/eligibility logic is introduced
definition_of_done:
  - an implementation-ready contract patch/design exists and is applied for the first milestone context
  - the context can prove which confirmed Skill Tree scope and Home narrowing it represents
notes:
  - current Packet 09 context freezes Template + Path + Rhythm but does not yet carry confirmed ScopeSelection or Home narrowing
  - current ResolutionRequest requires Path while Algorithm SSOT describes Path demand as optional in current-window resolution
source:
  - lib/features/sequencing/domain/resolution_context.dart
  - docs/ssot/features/algorithm/spec.md
  - docs/ssot/features/algorithm/materialization.csv
  - docs/ssot/features/sequencing/canon/10-meso/07-cross-feature-contracts.md
```

### Task 7 — Build Home request adapter into frozen resolution context

```yaml
id: 7
title: Build Home request adapter into frozen resolution context
status: open
priority: high
due_date: null
depends_on: [5, 6]
blocked_by: []
acceptance_criteria:
  - confirmed ScopeSelection is consumed without mutation or widening
  - Home duration/mode narrowing is represented as request input
  - current Rhythm snapshot/revision enters the context through the owner contract
  - Path snapshot is included only according to the reconciled contract
  - allowed TemplateVersion identity is preserved
  - resulting ResolutionRequest/ResolutionContext has deterministic fingerprint
  - Home remains a requester/presenter and performs no eligibility, scoring, ranking, or concrete Chunk binding
definition_of_done:
  - Home can create/request one fresh frozen resolution context from current owner inputs
  - legacy GS_Spark.resolveSelection(treeModel) is unnecessary for this path
notes:
  - candidate generation is deliberately outside this task
source:
  - lib/pages/s_c_r_home_today.dart
  - lib/globals/g_s_spark.dart
  - lib/features/sequencing/domain/resolution_context.dart
  - docs/ssot/screens/home-today.md
  - docs/ssot/features/algorithm/spec.md
```

### Task 8 — Validate Home -> Skill Tree -> frozen resolution-context vertical slice

```yaml
id: 8
title: Validate Home to Skill Tree to frozen resolution-context vertical slice
status: open
priority: high
due_date: null
depends_on: [3, 4, 5, 6, 7]
blocked_by: []
acceptance_criteria:
  - Home opens the canonical bounded Skill Tree
  - user can browse and select Epic/Block/Chunk
  - explicit confirmation creates one canonical ScopeSelection
  - Home-origin selection returns to Home request context
  - fake initial scope is not mistaken for user truth
  - integrated path does not depend on legacy GS_SkillTree.treeModel resolution
  - Home narrowing plus confirmed scope produces a fresh fingerprinted context
  - scope identity is preserved without widening
  - stale/mismatched owner revisions fail explicitly
  - remaining candidate-generation functionality is clearly marked as not yet implemented rather than silently mocked as real
definition_of_done:
  - one demonstrable first real integrated Leela interaction slice exists
  - its implemented and deferred boundaries are documented
notes:
  - this is the primary first milestone for the epic
source:
  - tasks 1 through 7 evidence and implementation
```

### Task 9 — Retire touched Skill Tree drift and legacy primary-surface assumptions

```yaml
id: 9
title: Retire touched Skill Tree drift and legacy primary-surface assumptions
status: open
priority: medium
due_date: null
depends_on: [2, 3]
blocked_by: []
acceptance_criteria:
  - primary user flow does not expose universal mastery semantics
  - touched legacy "mastered" mapping/writing is removed or quarantined according to current SSOT
  - hasSuccessor remains visual-only and cannot become a hard gate
  - fixture-only status/progress are not represented as authoritative backend truth
  - legacy list/state code retained for fallback is explicitly labeled and isolated
  - no Content-owned prerequisite/relationship truth is invented by Skill Tree
definition_of_done:
  - Skill Tree code touched by the first slice does not reintroduce known SSOT drift
notes:
  - broader Content relationship repair remains outside this epic's first milestone
source:
  - docs/ssot/features/skill-tree/spec.md
  - docs/ssot/features/skill-tree/materialization.csv
  - lib/features/skill_tree/spatial_adapter.dart
  - lib/pages/s_c_r_skill_tree.dart
```

### Task 10 — Continue broader owner-backed Home integration after first slice

```yaml
id: 10
title: Continue broader owner-backed Home integration after first slice
status: open
priority: medium
due_date: null
depends_on: [8]
blocked_by: []
acceptance_criteria:
  - next Home mock seam is selected from the runtime conformance report rather than assumed
  - selected seam consumes owner-produced data
  - Home does not create a second owner for points, time, rank, evidence, or explanations
  - removed mock seam is no longer seeded as current truth
  - remaining mocks/placeholders stay explicitly identified
definition_of_done:
  - at least one additional Home seam is moved from mock/legacy data to contract-faithful owner output
notes:
  - candidate/ranking/DecisionTrace work may become a separate Algorithm epic or follow-on task set depending on repository state after Task 8
source:
  - Task 1 Home conformance report
  - docs/ssot/screens/home-today.md
  - relevant owner feature SSOT/materialization
```

## dependency_plan

```yaml
dependency_plan:
  proposed_depends_on_updates:
    - task_id: 3
      depends_on: [1, 2]
      rationale: primary navigation should be changed only after both endpoint surfaces are runtime-verified
      confidence: high
      review_flags: []

    - task_id: 4
      depends_on: [3]
      rationale: origin-aware handoff requires the canonical Skill Tree to be the actual navigation destination
      confidence: high
      review_flags: []

    - task_id: 5
      depends_on: [4]
      rationale: legacy/fake scope state can be safely removed from the integrated path once the canonical handoff exists
      confidence: medium
      review_flags:
        - dependency_uncertainty

    - task_id: 6
      depends_on: [4]
      rationale: the resolution context reconciliation must target the actual canonical selection contract and entry behavior
      confidence: medium
      review_flags:
        - dependency_uncertainty
        - resolution_context_contract_mismatch

    - task_id: 7
      depends_on: [5, 6]
      rationale: Home should adapt only clean confirmed scope state into the reconciled frozen context family
      confidence: high
      review_flags: []

    - task_id: 8
      depends_on: [3, 4, 5, 6, 7]
      rationale: the vertical slice requires routing, handoff, clean state, contract reconciliation and Home adaptation
      confidence: high
      review_flags: []

    - task_id: 9
      depends_on: [2, 3]
      rationale: retire only drift actually touched by the verified bounded-cluster primary path
      confidence: medium
      review_flags:
        - dependency_uncertainty

    - task_id: 10
      depends_on: [8]
      rationale: broader Home mock replacement should follow proof of the first integrated slice
      confidence: high
      review_flags: []

  blocked_by_notes:
    - >
      Task 6 contains a real contract mismatch: current ResolutionRequest requires PathDemandSnapshot,
      while current Algorithm SSOT describes Path demand as optional for current-window resolution.
      Do not silently choose one interpretation.

  apex_sync_handoff_requests:
    - validate_dependencies
    - compute_next_action
    - compute_focus_candidates
```

## priority_urgency_focus_rationale

```yaml
priority_urgency_focus_rationale:
  epic_priority: high
  priority_rationale: >
    This is the principal new Leela development initiative named by the operator
    for the first full-portfolio weekly cycle and now has repository-backed scope.

  urgency:
    due_date: null
    rationale: >
      The work is intended to move during 2026-W34, but no binding deadline was supplied.

  provisional_focus_recommendation:
    focus_candidate_title: Verify Home runtime against current Home screen contract
    parallel_candidate_title: Verify bounded spatial Skill Tree runtime
    rationale: >
      Static repository evidence is now strong enough; the remaining uncertainty
      before changing routing/state is what the two existing endpoint surfaces
      actually do in runtime. These verifications are independent and unblock
      the primary-route decision without inventing architecture.
    confidence: high
    assumptions:
      - current locked Home and Skill Tree SSOT remain authoritative
      - Leela-Cloud-2026 remains the current runtime implementation repository
    handoff_needed:
      - validate_dependencies
      - compute_focus_candidates
      - compute_next_action
```

## review_flags

```yaml
review_flags:
  operator_review_needed:
    - approve this v2 decomposition before canonical epic/task creation

  resolution_context_contract_mismatch:
    - Packet 09 runtime ResolutionContext is narrower than current Algorithm SSOT
    - confirmed ScopeSelection and Home narrowing are not yet frozen in the runtime context

  path_optionality_mismatch:
    - current ResolutionRequest requires PathDemandSnapshot identity/revision
    - current Algorithm SSOT describes Path demand as optional for current-window resolution

  legacy_surface_disposition_requires_runtime_verification:
    - bounded cluster is the conforming renderer but currently hidden from normal navigation
    - legacy /skill-tree may still need explicit accessibility/debug fallback retention

  deferred_not_blocking_first_milestone:
    - DecisionTrace runtime owner is not implemented
    - full ResolutionCandidate runtime contract was not found
    - eligibility engine is not implemented
    - guided-pool fallback/current-window defaulting is not fully implemented
    - Skill Tree backend status/progress remain fixture-only
    - Content creator relationships/prerequisites remain incomplete
```

## handoff_requests

```yaml
handoff_requests:
  to_apex_sync_after_canonical_write:
    - validate_dependencies
    - compute_next_action
    - scan_blockers
    - rebuild_registry
    - compute_focus_candidates

  to_apex_session_after_operator_approval:
    - create apex-meta/epics/leela-core-interaction-development/epic.md
    - create approved canonical task records
    - preserve this packet and checkpoint sources in task source fields
    - update session planning feed after confirmed write
```

## operator_gate

```yaml
operator_gate:
  status: operator_review_needed
  recommended_decision: approved_for_handoff
  allowed_next_states:
    - approved_for_handoff
    - needs_revision
  mutation_allowed_by_this_packet: false
  next_if_approved:
    - route canonical epic/task creation through Apex Session
    - run Apex Sync validation after records exist
```

## Durable continuation rule

Future work on this epic must begin by reading this v2 packet and the latest checkpoint/worklog files from GitHub. Do not reconstruct the project from conversational memory. If new repository evidence changes the plan, save a new checkpoint first, then update or supersede this packet.
