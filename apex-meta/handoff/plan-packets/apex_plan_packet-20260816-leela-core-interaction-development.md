---
okf: open-knowledge-format
okf_version: 1
title: "Apex Plan Packet — Leela Core Interaction Development"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
updated: 2026-08-16
status: operator_review_needed
planning_status: evidence_checked_candidate
package: apex-plan
project: Leela
candidate_epic_slug: leela-core-interaction-development
target_week: 2026-W34
operator_gate: operator_review_needed
canonical_mutation_performed: false
---

# Apex Plan Packet — Leela Core Interaction Development

## 1. Purpose

Capture the first real Leela development project for the 2026-W34 portfolio cycle using current repository evidence rather than chat memory or greenfield assumptions.

The operator's direction is:

- begin new Leela development from the most basic interaction layer;
- start with Home, then move into Skill Tree;
- include the real data, materialization, spatial-design, and interaction foundations;
- aim for working first versions rather than final production completeness.

This packet supersedes the earlier chat-only greenfield decomposition that treated Home as something to define and build from scratch.

## 2. Source Basis

### Operator source

- 2026-08-16 portfolio intake: start from Home, then Skill Tree, including data, materialization, spatial design, and related foundations.
- 2026-08-16 clarification: desired milestone is working versions of each relevant feature/foundation.

### Product/specification repository

Repository: `leela-spec/leela`, branch `main`.

Relevant source paths:

- `LeelaAppDevelopment/Nowa/Nowa Basic Files/F0 Nowa Workspace and Git SSOT.md`
- `LeelaAppDevelopment/StatusQuo/FeatureSpecs&Wireframes/FeatureUpdates_In_February/Home Patch Specs_process basics.md`
- `LeelaAppDevelopment/StatusQuo/FeatureSpecs&Wireframes/FeatureUpdates_In_February/Skill Tree Specs v3.md`
- `LeelaAppDevelopment/StatusQuo/FeatureSpecs&Wireframes/FeatureUpdates_26-03/Skill Tree Update N4 v1.md`
- `LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md`
- `LeelaAppDevelopment/StatusQuo/Spatial Skill Tree & path/`

Important source finding: the Nowa workspace SSOT states that Home is authoritative in the Spark prototype while non-Home feature screens may remain placeholders until their specifications are updated.

### Runtime/implementation repository

Repository: `leela-spec/Leela-Cloud-2026`, branch `master`.

Relevant source paths:

- `lib/pages/s_c_r_home_today.dart`
- `lib/pages/leela_home.dart`
- `lib/globals/g_s_data.dart`
- `lib/globals/g_s_spark.dart`
- `lib/features/skill_tree/`
- `test/pages/s_c_r_home_today_lifecycle_test.dart`
- `docs/ssot/decisions/2026-07-29-home-is-a-screen.md`
- `docs/ssot/screens/home-today.md`

## 3. Current-State Findings

### 3.1 Home already exists

The operative Home is `SCR_Home_Today` at `/home`, implemented by `lib/pages/s_c_r_home_today.dart`.

It already contains substantial UI and interaction structure:

- top navigation;
- orb / feature preview region;
- feature tabs for Skill Tree, Path, Rhythm, Sequences, and Stats;
- TP / XP / BP achievement donuts;
- upcoming-events table;
- recommendation hero carousel;
- scope picker;
- duration picker;
- Spark Pre-Run navigation;
- bottom navigation including Universe, Play, Kharma, and Rhythm.

`lib/pages/leela_home.dart` also exists, but is currently an almost-empty generated Scaffold with a Lab Playground FAB. Its runtime role/disposition must be determined before cleanup.

### 3.2 Locked architecture: Home is a screen, not a feature owner

`docs/ssot/decisions/2026-07-29-home-is-a-screen.md` locks Home as a presentation/composition surface rather than a 12th concept/domain owner.

Home composes read-only output from domain owners and should own only local presentation/interaction state.

The current screen contract at `docs/ssot/screens/home-today.md` defines these principal ownership boundaries:

- feature preview/navigation <- route registry and feature-owned preview data;
- weekly TP/XP/BP <- Algorithm + Stats;
- upcoming events/current-window projection <- Rhythm;
- Next Best Action alternatives/evidence <- Algorithm + Sequencing view representation;
- explanation/nudges <- Sid;
- scope and duration requests <- Skill Tree + Rhythm + explicit user request.

Home must not independently calculate points, ranking, temporal supply, Path demand, recommendation fallbacks, Algorithm evidence, or other domain truth.

### 3.3 Current runtime does not yet satisfy the current Home contract

The current Home screen is visually substantial, but the current SSOT explicitly marks major runtime targets as `to_change`.

Observed implementation gaps include:

- `SCRHomeToday.initState()` calls `GS_Data.fn_seedHomeMockData()`.
- `GS_Data` hardcodes feature tabs, hero recommendations, upcoming events, metrics, a recommendation payload, and Path example data.
- TP/XP/BP values also exist as Home-local integer fields in `SCRHomeToday` instead of owner-produced snapshots.
- `GS_Spark` initializes mock scope/resolved-scope/recommendation state.
- `GS_Spark.generateRecommendations()` currently creates simplified local recommendations using duration/projected point formulas rather than the current Algorithm resolution/evidence contract.
- the current recommendation DTO remains a flat/legacy representation and lacks the current `ResolutionCandidate`/`DecisionTrace` semantics.
- Home's feature-tab open callback is currently empty.
- Search and Settings callbacks are currently empty.
- Upcoming-row callback is currently empty.
- the current Home lifecycle test protects pending scope/duration navigation, but deliberately removes carousel content because of known card-layout debt; therefore current automated Home coverage is narrow.

### 3.4 Consequence for project planning

The project must not start with "define Home" or "build Home" as if it were greenfield.

The correct starting pattern is:

1. reconcile current implementation against current SSOT;
2. verify actual runtime behavior visually/interactionally;
3. classify what stays, what is mock/prototype debt, what is broken, and what is obsolete;
4. repair navigation/lifecycle seams that are already intended;
5. replace mock/legacy data wiring incrementally with owner-backed read models;
6. only then derive the Home -> Skill Tree vertical slice from the actual existing Skill Tree implementation and SSOT.

## 4. Revised Project Capture Record

```yaml
project_capture_record:
  goal: >
    Establish a working, contract-correct first integrated Leela interaction
    path beginning from the existing Home surface and proceeding into the
    existing Skill Tree system, while replacing mock or legacy wiring with
    real owner-backed data, resolution, materialization, and spatial behavior.

  scope:
    in_scope:
      - current Home implementation audit
      - Home screen-contract conformance
      - Home runtime verification
      - Home navigation and lifecycle seams
      - owner-backed Home read-model integration
      - current-window resolution integration
      - existing Skill Tree runtime/SSOT audit
      - Home -> Skill Tree integration slice
      - data/materialization/spatial contracts needed by that slice

    out_of_scope:
      - rebuild Home from scratch
      - treat Home as a domain/concept owner
      - full production completion of Leela
      - broad Leela-wide unresolved decisions
      - Leela project-management cleanup
      - speculative architecture not grounded in repository evidence

  constraints:
    - reuse existing working UI before rebuilding
    - validate actual runtime before deriving implementation tasks
    - replace mock data incrementally
    - preserve locked domain ownership boundaries
    - current repository evidence outranks chat reconstruction
    - implementation architecture must be derived from current Leela sources, not invented by Apex Plan

  source:
    - operator portfolio intake 2026-08-16
    - operator clarification 2026-08-16
    - leela-spec/leela current specs and Nowa SSOT
    - leela-spec/Leela-Cloud-2026 current runtime and current SSOT projection

  review_flags:
    - operator_review_needed
```

## 5. Proposed Task Records

These are planning proposals only. No canonical task files are created by this packet.

### Task 1 — Audit current Home implementation against current Home SSOT

```yaml
id: 1
title: Audit current Home implementation against Home screen SSOT
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - current Home runtime files and current Home SSOT are inspected together
  - conforming behavior is listed
  - missing behavior is listed
  - obsolete behavior is listed
  - mock-data dependencies are listed
  - ownership violations are listed
  - visible interaction/navigation defects are listed
  - required runtime-contract changes are listed without speculative redesign
definition_of_done:
  - one evidence-backed Home conformance/gap report exists
  - every major finding references a concrete runtime or SSOT source
notes:
  - this replaces the earlier greenfield task "Define minimum Home interaction slice"
source:
  - lib/pages/s_c_r_home_today.dart
  - lib/globals/g_s_data.dart
  - lib/globals/g_s_spark.dart
  - docs/ssot/screens/home-today.md
  - docs/ssot/decisions/2026-07-29-home-is-a-screen.md
```

### Task 2 — Verify Home visually and behaviorally in the running app

```yaml
id: 2
title: Verify Home visually and behaviorally in the running app
status: open
priority: high
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - current Home is run in the supported local/simulator environment
  - layout and responsive behavior are checked
  - orb/preview interaction is checked
  - feature tabs and their open affordances are checked
  - donut presentation and interaction are checked
  - upcoming expansion/rows are checked
  - recommendation carousel behavior is checked
  - scope and duration pickers are checked
  - Spark Pre-Run transition is checked
  - bottom navigation is checked
  - Sid/search/settings behavior is checked
  - visible loading/error/empty states are checked
definition_of_done:
  - observed runtime behavior is recorded separately from static-code assumptions
  - defects and divergences from the screen contract are captured
notes:
  - current automated Home coverage is insufficient to substitute for this runtime check
source:
  - lib/pages/s_c_r_home_today.dart
  - test/pages/s_c_r_home_today_lifecycle_test.dart
  - docs/ssot/screens/home-today.md
```

### Task 3 — Reconcile Home navigation and lifecycle defects

```yaml
id: 3
title: Reconcile Home navigation and lifecycle defects
status: open
priority: high
due_date: null
depends_on: [1, 2]
blocked_by: []
acceptance_criteria:
  - intended Home navigation callbacks are either wired or explicitly classified as intentionally unavailable
  - feature-tab open behavior is resolved
  - Search and Settings callback state is resolved
  - Upcoming row interaction is resolved
  - duplicate/obsolete LeelaHome page has an explicit disposition
  - Home navigation preserves current screen-contract ownership boundaries
  - lifecycle behavior remains safe for pending scope/duration navigation
definition_of_done:
  - no known Home navigation seam remains ambiguous between bug, placeholder, and intended behavior
  - relevant runtime checks/tests pass for changed seams
notes:
  - exact repair scope depends on Task 1 and Task 2 evidence
source:
  - lib/pages/s_c_r_home_today.dart
  - lib/pages/leela_home.dart
  - test/pages/s_c_r_home_today_lifecycle_test.dart
```

### Task 4 — Replace Home mock presentation data with owner-backed read models

```yaml
id: 4
title: Replace Home mock presentation data with owner-backed read models
status: open
priority: high
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - Home no longer depends on mock data for any seam selected for this first integration slice
  - Rhythm supplies the selected upcoming/current-window projection seam
  - Algorithm/Stats supplies the selected TP/XP/BP snapshot seam
  - Algorithm supplies ordered resolution candidates for the selected recommendation seam
  - Sequencing preserves the required candidate/view identity structure
  - Sid supplies explanation/nudge wording where included
  - Skill Tree supplies scope-selection representation where included
  - Home remains read-only with respect to owner-produced domain truth
definition_of_done:
  - selected Home seams consume contract-faithful owner outputs
  - removed mock seams are no longer seeded by GS_Data for that path
  - ownership rules from the Home screen contract remain intact
notes:
  - this task may be split after Task 1 if independent owner seams warrant separate implementation tasks
source:
  - lib/globals/g_s_data.dart
  - lib/globals/g_s_spark.dart
  - docs/ssot/screens/home-today.md
```

### Task 5 — Establish real current-window resolution flow

```yaml
id: 5
title: Establish real current-window resolution flow
status: open
priority: high
due_date: null
depends_on: [4]
blocked_by: []
acceptance_criteria:
  - Rhythm-provided current-window boundary is honored when present
  - explicit duration can narrow but not improperly widen the owner-authorized window
  - scope/mode/duration changes produce a fresh resolution context
  - resulting candidate order comes from the appropriate owner logic rather than Home-local ranking
  - typed no-feasible-candidate behavior is representable
  - evidence/trace boundaries between Algorithm, Sid, Sequencing, and Home are preserved
definition_of_done:
  - Home can request and render a contract-faithful current-window resolution result
  - local simplified recommendation generation is no longer authoritative for the integrated path
notes:
  - exact implementation depends on the current Algorithm/Rhythm/Sequencing materialization contracts
source:
  - docs/ssot/screens/home-today.md
  - lib/globals/g_s_spark.dart
```

### Task 6 — Validate Home as the first real integrated interaction surface

```yaml
id: 6
title: Validate Home as the first real integrated interaction surface
status: open
priority: high
due_date: null
depends_on: [3, 4, 5]
blocked_by: []
acceptance_criteria:
  - Home runs with the selected real/contract-faithful owner data seams
  - core Home interactions remain usable
  - owner-produced data is not silently recomputed by Home
  - navigation and lifecycle seams selected for the milestone work
  - known remaining mock or placeholder behavior is explicitly documented
definition_of_done:
  - one demonstrable Home baseline exists for subsequent Skill Tree integration
  - remaining Home gaps are separated from completed milestone behavior
notes: []
source:
  - outputs of tasks 1 through 5
```

### Task 7 — Audit existing Skill Tree implementation, SSOT, data, materialization, and spatial contracts

```yaml
id: 7
title: Audit existing Skill Tree implementation and current contracts
status: open
priority: high
due_date: null
depends_on: [1]
blocked_by: []
acceptance_criteria:
  - current lib/features/skill_tree implementation is inspected
  - current Skill Tree SSOT/spec sources are inspected
  - existing Skill Tree data model is identified
  - existing materialization contracts are identified
  - existing spatial-design representation/contracts are identified
  - implemented, missing, obsolete, and speculative parts are separated
  - Home-facing scope/preview/navigation seams are identified
definition_of_done:
  - one evidence-backed Skill Tree current-state/gap report exists
  - no next Skill Tree build task is based only on historical or chat assumptions
notes:
  - this task must precede any detailed greenfield Skill Tree decomposition
source:
  - lib/features/skill_tree/
  - LeelaAppDevelopment/StatusQuo/FeatureSpecs&Wireframes/FeatureUpdates_In_February/Skill Tree Specs v3.md
  - LeelaAppDevelopment/StatusQuo/FeatureSpecs&Wireframes/FeatureUpdates_26-03/Skill Tree Update N4 v1.md
  - LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md
  - LeelaAppDevelopment/StatusQuo/Spatial Skill Tree & path/
```

### Task 8 — Define the next real Home -> Skill Tree vertical slice

```yaml
id: 8
title: Define next Home to Skill Tree vertical slice from repository evidence
status: open
priority: high
due_date: null
depends_on: [6, 7]
blocked_by: []
acceptance_criteria:
  - the slice reuses existing Home and Skill Tree behavior wherever valid
  - required Home -> Skill Tree navigation/context transfer is explicit
  - required data structures are explicit
  - required materialization behavior is explicit
  - required spatial behavior is explicit
  - first working-version boundaries are explicit
  - tasks for implementation can be derived without rebuilding either surface wholesale
definition_of_done:
  - an implementation-ready vertical-slice proposal exists
  - all unresolved architecture or product decisions are flagged rather than invented
notes:
  - this is the point where the next implementation decomposition should be created
source:
  - outputs of tasks 6 and 7
```

## 6. Dependency Plan

```yaml
dependency_plan:
  proposed_depends_on_updates:
    - task_id: 3
      depends_on: [1, 2]
      rationale: navigation/lifecycle repairs should be based on both static conformance evidence and actual runtime observations
      confidence: high
      review_flags: []

    - task_id: 4
      depends_on: [1]
      rationale: mock replacement must first identify which runtime seams conflict with the current owner contracts
      confidence: high
      review_flags: []

    - task_id: 5
      depends_on: [4]
      rationale: current-window resolution requires owner-backed read-model seams rather than the current mock/local recommendation path
      confidence: medium
      review_flags:
        - dependency_uncertainty

    - task_id: 6
      depends_on: [3, 4, 5]
      rationale: integrated Home validation requires repaired interaction seams and the selected real-data/resolution path
      confidence: high
      review_flags: []

    - task_id: 7
      depends_on: [1]
      rationale: Skill Tree audit can begin once the Home ownership/integration boundary is understood
      confidence: medium
      review_flags:
        - dependency_uncertainty

    - task_id: 8
      depends_on: [6, 7]
      rationale: the next vertical slice should be based on a validated Home baseline plus verified Skill Tree current state
      confidence: high
      review_flags: []

  blocked_by_notes: []

  apex_sync_handoff_requests:
    - validate_dependencies
    - compute_next_action
    - compute_focus_candidates
```

## 7. Priority, Urgency, and Focus Rationale

```yaml
priority_urgency_focus_rationale:
  priority_summary: >
    High. This is the principal Leela development initiative named by the
    operator for the first full-portfolio weekly cycle.

  urgency_summary: >
    No binding due date was supplied. The work is intended to move during
    2026-W34, so due_date remains null rather than inventing a calendar deadline.

  provisional_focus_recommendation:
    focus_candidate_title: Audit current Home implementation against Home screen SSOT
    rationale: >
      Repository evidence shows Home already exists and the main uncertainty is
      conformance, runtime behavior, and mock/legacy wiring. The audit therefore
      unlocks a correct implementation plan without rebuilding existing work.
    confidence: high
    assumptions:
      - current locked Home decision and current screen contract remain authoritative
      - Leela-Cloud-2026 remains the current runtime implementation repository
    handoff_needed:
      - validate_dependencies
      - compute_focus_candidates
      - compute_next_action
```

## 8. Review Flags

```yaml
review_flags:
  - operator_review_needed
  - dependency_uncertainty

resolved_assumptions:
  - Home is not greenfield
  - Home is a screen, not a domain/concept owner
  - current runtime includes substantial Home UI
  - current runtime still includes mock/legacy Home data paths
  - detailed Skill Tree implementation tasks must wait for repository audit

unresolved_questions:
  - exact current disposition of lib/pages/leela_home.dart
  - exact current Skill Tree runtime completeness
  - which owner-backed Home seam should be implemented first after audit
  - exact materialization/spatial contracts that apply to the first Home -> Skill Tree slice
```

## 9. Operator Gate and Mutation Boundary

```yaml
operator_gate:
  status: operator_review_needed
  allowed_next_states:
    - approved_for_handoff
    - needs_revision

mutation_boundary:
  this_packet:
    may_do:
      - preserve evidence-backed project capture
      - propose task records
      - propose dependencies
      - preserve source references
    does_not_do:
      - create apex-meta/epics/leela-core-interaction-development/epic.md
      - create canonical task files
      - mutate task status
      - rebuild registry

  next_if_approved:
    - route operator-approved durable project/task creation through Apex Session
    - run Apex Sync dependency validation after canonical records exist
```

## 10. Supersession Note

This packet supersedes the earlier chat-only nine-task greenfield decomposition for `leela-core-interaction-development`.

Do not reconstruct that earlier version from chat memory. Use this repository packet and the referenced Leela source files as the planning basis for subsequent work.
