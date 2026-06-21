# Apex Plan Package Manifest

```yaml
package_metadata:
  package_name: apex-plan
  package_path: ".claude/skills/apex-plan/"
  package_role: no_script_operator_gated_project_planning
  read_when: operator_inspects_package_structure_or_validates_file_inventory

file_index:
  - path: ".claude/skills/apex-plan/SKILL.md"
    purpose: "Skill entrypoint, routing contract, procedure, failure modes, output requirements, and completion gate."
    read_when:
      - skill_invocation
      - entrypoint_review
      - boundary_validation

  - path: ".claude/skills/apex-plan/references/plan-cluster-contract.md"
    purpose: "Canonical scope, cluster mapping, process ownership, durable paths, and handoff boundaries."
    read_when:
      - validating_package_scope
      - clarifying_boundaries
      - preparing_handoff_requests

  - path: ".claude/skills/apex-plan/references/task-record-contract.md"
    purpose: "Canonical task record fields, status enum, dependency field, actionability rule, and mutation boundary."
    read_when:
      - creating_task_records
      - validating_task_fields
      - checking_dependency_values

  - path: ".claude/skills/apex-plan/references/decomposition-and-dependency-rules.md"
    purpose: "Rules for decomposing work, proposing depends_on, and flagging dependency uncertainty."
    read_when:
      - decomposing_work
      - proposing_dependencies
      - flagging_circular_dependency_risk

  - path: ".claude/skills/apex-plan/references/priority-urgency-focus-policy.md"
    purpose: "Priority values, due_date urgency policy, and provisional focus rationale boundaries."
    read_when:
      - assigning_priority
      - explaining_urgency
      - drafting_focus_rationale

  - path: ".claude/skills/apex-plan/templates/epic-template.md"
    purpose: "Blank proposed epic record template for operator review packets."
    read_when:
      - drafting_epic_record
      - operator_requests_template

  - path: ".claude/skills/apex-plan/templates/task-template.md"
    purpose: "Blank proposed task record template with all required fields."
    read_when:
      - drafting_task_record
      - operator_requests_template

  - path: ".claude/skills/apex-plan/package-manifest.md"
    purpose: "Lightweight package index and package-level acceptance checks."
    read_when:
      - package_inventory_review
      - file_count_validation

package_boundaries:
  must_do:
    - capture_project_goal_scope_constraints_source_and_review_flags
    - define_epic_record_under_apex_meta_epics_slug
    - draft_task_records_with_required_fields
    - propose_depends_on_relationships
    - explain_priority_due_date_and_focus_qualitatively
    - emit_apex_sync_and_apex_session_handoff_requests
  must_not_do:
    - generate_scripts
    - run_bash
    - run_python
    - compute_exact_next_task
    - traverse_dependency_graph
    - scan_blockers
    - rebuild_registry
    - mutate_status_or_session_state
    - write_durable_files

acceptance_checks:
  required_files_present: true
  no_scripts_generated: true
  status_enum_preserved: true
  depends_on_integer_array_preserved: true
  priority_policy_preserved: true
  due_date_policy_preserved: true
  apex_sync_boundary_present: true
  apex_session_boundary_present: true
```