# Apex Session Package Manifest

## package_name

~~~yaml
package_name: apex-session
~~~

## package_path

~~~yaml
package_path: ".claude/skills/apex-session/"
~~~

## package_status

~~~yaml
package_status: final_canonical_v1
~~~

## exact_file_index

~~~yaml
exact_file_index:
  package_root: ".claude/skills/apex-session/"
  files:
    - SKILL.md
    - references/session-cluster-contract.md
    - references/mutation-gate-rules.md
    - references/state-delta-and-entity-rules.md
    - references/handoff-and-next-session-contract.md
    - templates/task_plan.md
    - templates/findings.md
    - templates/progress.md
    - templates/next-session.md
    - package-manifest.md

  exact_file_count: 10

  excluded_directories:
    - scripts/
    - evals/
    - tests/
    - schemas/
    - examples/
    - assets/
    - agents/
~~~

## file_purpose_map

~~~yaml
file_purpose_map:
  SKILL.md:
    role: compact_skill_entrypoint
    purpose: >
      Defines invocation scope, objective, accepted inputs, final outputs,
      supporting file navigation, procedure, validation rules, failure modes,
      and completion gate.

  references/session-cluster-contract.md:
    role: C_SESSION_scope_contract
    purpose: >
      Defines package role, owned processes, excluded processes,
      cross-package routing, PD3 boundary, script/write exclusions, and final
      acceptance invariants.

  references/mutation-gate-rules.md:
    role: mutation_validation_contract
    purpose: >
      Defines H1 status validation, status_mutation_record schema,
      before_after_preview schema, operator_validation_record schema,
      confirmation gate, invalid mutation rejection, and final mutation output
      contract.

  references/state-delta-and-entity-rules.md:
    role: state_delta_and_entity_contract
    purpose: >
      Defines state_delta_summary schema, entity_update_record schema, raw
      source preservation, source conflict policy, duplicate entity risk policy,
      durable findings policy, and planning_feed policy.

  references/handoff-and-next-session-contract.md:
    role: H6_handoff_contract
    purpose: >
      Defines task_plan.md, findings.md, progress.md, next-session.md,
      required next-session sections, read-before-decide rule, planning feed,
      missing-context behavior, and final handoff checks.

  templates/task_plan.md:
    role: H6_template
    purpose: task plan artifact template with exact sections.

  templates/findings.md:
    role: H6_template
    purpose: findings artifact template with exact sections.

  templates/progress.md:
    role: H6_template
    purpose: progress artifact template with exact sections.

  templates/next-session.md:
    role: H6_template
    purpose: next-session artifact template with exact sections.

  package-manifest.md:
    role: package_index_and_validation_summary
    purpose: >
      Defines package status, exact file index, file purpose map, source basis,
      read order, package invariants, validation checklist, and forbidden
      claims.
~~~

## source_basis_map

~~~yaml
source_basis_map:
  SKILL.md:
    sources:
      - Phase 1 — Authority Extraction.md
      - Phase 5 — Process Coverage Gate v0.1.md
      - Phase 7 Package Readiness.txt
      - .claude/skills/apex-session/SKILL.md
      - planning-with-files SKILL.md
      - Backlog types/index.ts
      - CrewAI task.py SUBSTITUTE
      - Apex_Alfred_Skill_Definition_Guide.md

  references/session-cluster-contract.md:
    sources:
      - Phase 1 — Authority Extraction.md
      - Phase 5 — Process Coverage Gate v0.1.md
      - Phase 7 Package Readiness.txt
      - .claude/skills/apex-session/SKILL.md
      - .claude/skills/apex-session/package-manifest.md

  references/mutation-gate-rules.md:
    sources:
      - Backlog types/index.ts
      - Backlog parser.ts
      - CrewAI task.py SUBSTITUTE
      - Phase 5 — Process Coverage Gate v0.1.md
      - Phase 7 Package Readiness.txt

  references/state-delta-and-entity-rules.md:
    sources:
      - Backlog types/index.ts
      - Backlog parser.ts
      - llm-wiki SKILL.md
      - Phase 4 — Mechanism Ledger by Source v0.1.md
      - Phase 5 — Process Coverage Gate v0.1.md

  references/handoff-and-next-session-contract.md:
    sources:
      - Phase 1 — Authority Extraction.md
      - 00_Apex_Phase_Pack_Meta_Index.md
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/task_plan.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/findings.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/progress.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/next-session.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  package-manifest.md:
    sources:
      - .claude/skills/apex-session/package-manifest.md
      - generated final package files
      - Phase 7 Package Readiness.txt
~~~

## read_order

~~~yaml
read_order:
  normal_invocation:
    - SKILL.md
    - references/session-cluster-contract.md
    - references/mutation-gate-rules.md
    - references/state-delta-and-entity-rules.md
    - references/handoff-and-next-session-contract.md
    - relevant_template
    - package-manifest.md

  status_mutation_request:
    - SKILL.md
    - references/session-cluster-contract.md
    - references/mutation-gate-rules.md
    - templates/progress.md
    - references/handoff-and-next-session-contract.md

  handoff_request:
    - SKILL.md
    - references/handoff-and-next-session-contract.md
    - templates/task_plan.md
    - templates/findings.md
    - templates/progress.md
    - templates/next-session.md

  state_delta_or_entity_request:
    - SKILL.md
    - references/state-delta-and-entity-rules.md
    - references/mutation-gate-rules.md
    - references/handoff-and-next-session-contract.md
~~~

## package_invariants

~~~yaml
package_invariants:
  package_status: final_canonical_v1
  exact_file_count: 10
  C_SESSION_only: true
  H1_status_enum_exact:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  H6_handoff_files_exact:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  next_session_sections_exact:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
  no_scripts_in_package: true
  no_repo_write_claim: true
  no_apex_plan_scope: true
  no_apex_sync_scope: true
  no_public_web_research: true
  raw_source_reference_preservation_required: true
  operator_validation_required_for_consequential_mutation: true
  CrewAI_task_py_labeled_SUBSTITUTE: true
  llm_wiki_not_claimed_as_update_index_source: true
~~~

## validation_checklist

~~~yaml
validation_checklist:
  file_inventory:
    exact_file_count_is_10: true
    exact_tree_match: true
    no_extra_generated_directories: true

  SKILL_md:
    valid_frontmatter: true
    frontmatter_name_is_apex_session: true
    description_matches_final_contract: true
    objective_present: true
    skill_contract_present: true
    accepted_inputs_present: true
    final_outputs_present: true
    procedure_present: true
    validation_rules_present: true
    failure_modes_present: true
    completion_gate_present: true

  status_and_mutation:
    H1_status_enum_exact: true
    no_extra_task_status_values: true
    status_mutation_record_schema_present: true
    before_after_preview_schema_present: true
    operator_validation_record_schema_present: true
    invalid_mutation_rejection_present: true

  handoff:
    H6_files_present: true
    next_session_sections_exact: true
    templates_have_exact_required_sections: true

  boundaries:
    no_ranking_behavior: true
    no_blocker_scan_behavior: true
    no_registry_rebuild_behavior: true
    no_score_computation: true
    no_unlock_depth_computation: true
    no_new_project_decomposition: true
    no_script_execution: true
    no_calendar_operations: true

  formatting:
    no_collapsed_yaml: true
    no_collapsed_markdown: true
    headings_have_blank_lines: true
    code_fences_balanced: true
    no_source_citation_markup_inside_generated_files: true
    no_unresolved_placeholders_except_USER_INPUT_REQUIRED: true
~~~

## forbidden_claims

~~~yaml
forbidden_claims:
  - copied_CrewAI_getting_started_skill_source
  - copied_llm_wiki_update_index_behavior
  - copied_OpenClaw_TaskFlow_behavior
  - copied_Kanban_blocker_script_behavior
  - exact_next_task_ranking_inside_apex_session
  - blocker_scan_inside_apex_session
  - registry_rebuild_inside_apex_session
  - drift_detection_inside_apex_session
  - priority_score_computation_inside_apex_session
  - urgency_score_computation_inside_apex_session
  - unlock_depth_computation_inside_apex_session
  - silent_repo_mutation
  - scripts_generated_for_apex_session
~~~