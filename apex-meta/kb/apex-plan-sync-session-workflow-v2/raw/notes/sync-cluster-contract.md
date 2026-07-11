# Sync Cluster Contract

## package_role

`apex-sync` is the canonical package for deterministic Apex read-side
synchronization.

```yaml
package_role:
  package_name: apex-sync
  package_path: .claude/skills/apex-sync/
  package_status: final_canonical_v1
  cluster: B_SYNC
  role: deterministic_read_side_synchronization
  execution_model: skill_entrypoint_plus_standard_library_python_script
  canonical_script_path: scripts/apex_sync.py
```

The package reads Apex task files, computes synchronization reports, validates
read-side consistency, and previews or writes the compact work registry under a
strict write exception.

## B_SYNC_process_scope

```yaml
B_SYNC_process_scope:
  owns_read_side_computation: true
  default_mode: dry_run
  script_language: Python
  standard_library_only: true
  shell_out_allowed: false
  external_dependencies_allowed: false
  task_file_mutation_allowed: false
  handoff_file_mutation_allowed: false
  skill_file_mutation_allowed: false
  only_write_exception: apex-meta/registry/index.md
```

`apex-sync` is invoked only for deterministic computation from already-existing
task files. It does not create task intent, mutate task state, or interpret
operator decisions.

## owned_processes

`apex-sync` owns these process functions:

| Process | Meaning |
|---|---|
| `PM4_compute_next_action` | Compute dependency-satisfied next action candidates from existing task files. |
| `PM5_detect_blockers` | Detect blocked tasks, unsatisfied dependencies, missing dependency targets, and blocked tasks lacking blocker reasons. |
| `PM7_detect_stall` | Detect stale non-done tasks from task timestamps. |
| `PM8_generate_work_registry` | Generate the deterministic work registry preview and gated registry write. |
| `KB4_rebuild_index` | Rebuild the compact task index as registry content. |
| `KB5_detect_drift` | Compare current task files against the registry and report drift. |
| `PD1_compute_priority_score` | Convert H7 priority values into numeric scores. |
| `PD2_compute_urgency_score` | Compute due-date urgency as days until due or `999`. |
| `PD3_compute_unlock_depth` | Count downstream tasks unlocked by completing a task. |
| `PD4_compute_focus_candidates` | Sort actionable candidates by priority, urgency, unlock depth, and id. |

## excluded_processes

`apex-sync` must not own these process functions:

| Excluded process | Correct package boundary |
|---|---|
| `PM1_project_capture` | Belongs outside B_SYNC. |
| `PM2_human_decomposition` | Belongs outside B_SYNC. |
| `PM6_status_mutation` | Belongs to session/mutation handling. |
| `KB1_session_narrative` | Belongs to session handling. |
| `KB2_state_delta_interpretation` | Belongs to session handling. |
| `KB3_entity_synthesis` | Belongs to session handling. |
| `KB6_next_session_authoring` | Belongs to session handling. |
| `PD5_operator_validation` | Belongs to operator-gated mutation/session logic. |
| `PD6_planning_feed_authoring` | Belongs to session/planning-feed authoring. |

## cross_package_routing

Use this routing table when a request crosses the B_SYNC boundary:

| Request type | Route |
|---|---|
| Capture a new project, task, or idea | Not `apex-sync`; route to planning/capture behavior. |
| Decompose a project into tasks | Not `apex-sync`; route to planning/decomposition behavior. |
| Compute what is next from existing tasks | `apex-sync`. |
| Find blockers from existing tasks | `apex-sync`. |
| Rebuild or preview the registry | `apex-sync`. |
| Mutate a task status | Not `apex-sync`; route to session/mutation behavior. |
| Author `task_plan.md`, `findings.md`, `progress.md`, or `next-session.md` | Not `apex-sync`; route to session/handoff behavior. |
| Validate an operator decision | Not `apex-sync`; route to operator-gated validation behavior. |
| Create planning prose or next-day planning feed | Not `apex-sync`; route to planning/session feed behavior. |

## read_side_only_policy

`apex-sync` is read-side by default.

Allowed reads:

- `apex-meta/epics/*/[0-9][0-9][0-9].md`
- `apex-meta/registry/index.md` for drift comparison

Forbidden writes:

- Task files
- Handoff files
- Skill files
- Source-knowledge files
- Project capture files
- Session narrative files
- Entity synthesis files
- Planning-feed files

The script may create in-memory reports and print them to stdout. Printed output
is not considered a repo write.

## registry_write_exception

The single write exception is:

```txt
apex-meta/registry/index.md
```

The exception is valid only when all conditions are true:

```yaml
registry_write_exception:
  subcommand: registry
  dry_run: false
  explicit_operator_intent_required: true
  allowed_path: apex-meta/registry/index.md
  task_file_mutation: forbidden
  handoff_file_mutation: forbidden
  skill_file_mutation: forbidden
```

All other subcommands remain dry-run report generators.

## custom_python_caveats

The following behavior is custom Apex Python and must not be described as copied
from unavailable sources:

- `blocker_report`
- `stall_report`
- `registry_report`
- `drift_report`
- `unlock_depth`

Forbidden claims:

- `copied_llm_wiki_update_index_py`
- `copied_kanban_blocker_script`
- `copied_OpenClaw_TaskFlow`
- `fully_source_backed_B_SYNC_without_custom_python`
- `copied_bash_script_behavior_as_python_without_adaptation`

The final implementation adapts available CCPM, Task Master, Backlog, and
llm-wiki concepts into Apex-specific Python. It does not copy unavailable
`update-index.py` or Kanban blocker script behavior.

## final_acceptance_invariants

```yaml
final_acceptance_invariants:
  package_status: final_canonical_v1
  canonical_script_path: scripts/apex_sync.py
  no_final_script_under_apex_meta_scripts: true
  H1_status_enum:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  dependency_field: depends_on
  default_mode: dry_run
  only_allowed_write_path: apex-meta/registry/index.md
  standard_library_only: true
  shell_out_allowed: false
  task_status_mutation_allowed: false
  handoff_authoring_allowed: false
  operator_validation_claim_allowed: false
  custom_Apex_Python_caveats_present: true
```