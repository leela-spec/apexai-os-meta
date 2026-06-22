~~~yaml
state_delta_and_entity_rules:
  file_role: canonical_state_delta_and_entity_contract
  owns:
    - state_delta_summary
    - entity_update_proposal
    - raw_source_preservation_policy
    - duplicate_entity_risk_policy

  state_delta_summary:
    purpose: "Extract durable state changes from session evidence without computing planning rank."
    required_fields:
      source:
        type: string
      raw_source_path:
        type: string
      notes:
        type: string
      review_flags:
        type: string_array

  entity_update_proposal:
    purpose: "Propose an update to an entity file while preserving raw_source."
    required_fields:
      entity_id:
        type: string
      entity_path:
        type: string
      entity_type:
        type: string
      raw_source:
        type: string
      raw_source_path:
        type: string
      source:
        type: string
      notes:
        type: string
      confirmation_token:
        type: string
        allowed:
          - CONFIRM
          - CONFIRM WRITE
          - CONFIRM MUTATION
      review_flags:
        type: string_array

  raw_source_preservation_policy:
    raw_sources_path: "apex-meta/raw/"
    rule: "Preserve raw_source exactly and do not rewrite raw_source_path content."
    entity_files_path: "apex-meta/entities/"
    entity_update_rule: "Update entity files only after explicit operator confirmation."
    index_rebuild_owner: apex-sync

  duplicate_entity_risk_policy:
    trigger: "The same entity_id, entity_type, or entity meaning appears in more than one entity_path."
    required_review_flag: duplicate_entity_risk
    write_allowed_without_confirmation: false
~~~

## 1. State Delta Extraction

~~~yaml
state_delta_extraction:
  input_material:
    - session_progress_log
    - findings
    - progress
    - raw_source
    - raw_source_path
    - operator_instruction

  extraction_rules:
    preserve_uncertainty_as_review_flags: true
    preserve_source_trace: true
    do_not_infer_missing_raw_source: true
    do_not_resolve_conflict_between_sources_silently: true

  allowed_review_flags:
    - raw_source_missing
    - conflict_between_sources
    - entity_update_uncertain
    - duplicate_entity_risk
~~~

## 2. Entity Update Proposal Rules

~~~yaml
entity_update_rules:
  entity_path:
    base_path: "apex-meta/entities/"
    required_extension: ".md"

  raw_source_path:
    base_path: "apex-meta/raw/"
    preserve_raw_sources_do_not_rewrite: true

  confirmation:
    required_before_write: true
    accepted_confirm_tokens:
      - CONFIRM
      - CONFIRM WRITE
      - CONFIRM MUTATION

  index_rebuild:
    owner: apex-sync
    session_action: "Create handoff_requests when index rebuild is needed."
~~~

## 3. Entity Types

~~~yaml
entity_type_policy:
  entity_type:
    type: string
    allowed:
      - project
      - concept
      - source
      - decision
      - artifact
      - operator_context

  unknown_entity_type:
    review_flags:
      - entity_update_uncertain
    write_allowed_without_confirmation: false
~~~

## 4. Non-Goals

~~~yaml
non_goals:
  - "Do not rewrite raw_source content."
  - "Do not create entity files without confirmation_token."
  - "Do not rebuild the entity index."
  - "Do not merge duplicate entities silently."
  - "Do not treat uncertain state deltas as confirmed facts."
  - "Do not compute focus scores from state deltas."
~~~