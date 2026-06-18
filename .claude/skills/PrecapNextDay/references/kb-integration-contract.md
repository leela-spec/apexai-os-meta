# KB Integration Contract

```yaml
kb_integration_contract:
  artifact_name: kb_integration_contract
  file_role: precap_next_day_reference_contract
  purpose: >
    Define canonical file paths and field mappings that wire the
    project-kb-manager KB layer into PrecapNextDay's existing input contract.
    This file does not modify SKILL.md or any existing PrecapNextDay reference.
    It is additive only — a path resolution layer.

  ownership:
    owns:
      - canonical_project_state_sources
      - kb_field_mapping
    must_not_own:
      - input_intake_context
      - available_input_map
      - input_source_entry
      - next_day_plan
      - any schema owned by project-schema.md

  canonical_project_state_sources:
    current_project_status_overview:
      primary_path: .claude/kb/registry.md
      legacy_path: state/apex-project-status.md
      fallback_rule: >
        Use primary_path if file exists.
        Fall back to legacy_path if primary absent.
        If both absent, flag missing_current_project_status_overview per
        input-intake-and-resilience-contract.md missing_input_policy.
      representation: compact registry_entry list

    detailed_project_state_files:
      primary_glob: .claude/kb/projects/*.md
      representation: one full project_record per file
      loading_rule: load only when detailed_project_state_files input slot is needed

    next_PreCapNextDay_input_context:
      primary_path: .claude/kb/next-precap-context.md
      representation: top-3 projects by [priority/urgency] with next_action and blocked_by

  kb_field_mapping:
    # Maps KB base_record fields to PrecapNextDay input_source_entry vocabulary
    project_status_summary_for_precap: current_project_status_overview
    priority_urgency_date:             planning_signal  # [priority/urgency/date] format
    next_action:                       executable_next_chunk
    blocked_by:                        blocker_signal
    confidence:                        input_confidence  # values: high/medium/low/unknown

  read_when:
    - kb_state_available
    - project_state_source_resolution_needed
    - current_project_status_overview_missing

  non_goals:
    - Do not modify PrecapNextDay SKILL.md.
    - Do not redefine PrecapNextDay input schemas.
    - Do not add new required inputs to PrecapNextDay.
    - Do not define field types — those live in project-schema.md.
```
