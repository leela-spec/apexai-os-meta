# Apex KB Ingest, Query, Lint, and Audit Rules

```yaml
rules_document:
  artifact_name: apex_kb_operation_rules
  file_role: operational_rules_for_ingest_query_lint_audit
  package_path: ".claude/skills/apex-kb/"
  canonical_contract: "references/kb-contract.md"
  custody_hardening: "references/source-custody-and-read-verification.md"
  source_trace:
    governing_map: "APEX KB — LLM-Wiki Blueprint Capability Map.md"
    copied_blueprint_behaviors:
      - two_phase_ingest
      - source_hashing_before_ingest
      - phase_1_analysis_before_wiki_generation
      - operator_review_gate
      - contradiction_detection
      - index_first_query
      - read_small_relevant_page_set
      - quick_lint_and_full_lint_split
      - review_queue_processing
      - audit_feedback_grouping
    adapted_blueprint_behaviors:
      - raw_path_to_apex_meta_kb_raw
      - hidden_llm_wiki_metadata_to_visible_manifests
      - bash_validation_to_python_validation
      - CLAUDE_md_schema_to_kb_schema_md
      - source_custody_profile_overlay
      - actual_file_read_ledger_for_strict_profiles
```

# Shared Operation Rules

```yaml
shared_operation_rules:
  kb_root:
    required: true
    path_template: "apex-meta/kb/<kb-slug>/"
    missing_behavior: "Stop and request scaffold mode or an existing KB root."
  kb_schema:
    required: true
    path_template: "apex-meta/kb/<kb-slug>/kb-schema.md"
    missing_behavior: "Stop unless scaffold mode is active."
    must_define:
      - kb_topic_title
      - kb_source_authority_list
      - kb_concept_taxonomy_top_level
      - kb_language_policy
      - kb_operator_review_policy
  source_grounding:
    raw_source_or_approved_pointer_required: true
    generated_pages_require_source_pointers: true
    missing_source_rule: "Never infer source contents from filename, title, summary, manifest entry, or prior memory."
    manifest_rule: "Manifest proves registration/custody only, not source reading or semantic comprehension."
    contradiction_rule: "Expose contradictions instead of silently resolving them."
  source_storage_policy:
    allowed_modes:
      - pointer_only
      - copy_into_kb
      - snapshot_copy
    custody_profiles:
      standard:
        default_for_repo_internal_sources: pointer_only
        default_for_external_or_uploaded_sources: copy_into_kb
        pointer_only_allowed: true
      skill_generation:
        default_for_repo_internal_sources: snapshot_copy
        default_for_external_or_uploaded_sources: snapshot_copy
        pointer_only_allowed: false
        pointer_only_exception_requires:
          - explicit_operator_approval
          - no_copy_reason
          - stable_source_path
          - source_hash_or_no_hash_reason
          - future_read_access_confirmed
          - exception_recorded_in_source_intake_lock
      research_base:
        default_for_repo_internal_sources: snapshot_copy
        default_for_external_or_uploaded_sources: snapshot_copy
        pointer_only_allowed: false
        pointer_only_exception_requires:
          - explicit_operator_approval
          - no_copy_reason
          - stable_source_path
          - source_hash_or_no_hash_reason
          - future_read_access_confirmed
          - exception_recorded_in_source_intake_lock
    generated_pages_must_record:
      - source_storage_mode
      - source_path
      - source_hash_or_no_hash_reason
      - source_pointer_or_snapshot_path
  epistemic_fields:
    confidence:
      allowed: [high, medium, low, mixed, unknown]
    claim_label:
      allowed:
        - raw_source
        - source_backed_summary
        - behavioral_inference
        - working_hypothesis
        - operator_question
        - practitioner_question
    rule: "Do not place claim-label values inside the confidence field."
  ownership_split:
    python_owns:
      - source_hashing
      - source_inventory_when_scripted
      - scaffold_structure
      - manifest_shape_validation
      - frontmatter_validation
      - dead_wikilink_detection
      - orphan_page_detection
      - stale_index_detection
      - machine_index_generation
      - audit_file_listing
      - audit_shape_validation
    llm_owns:
      - source_relevance_judgment
      - source_intake_lock_recommendation
      - concept_extraction
      - entity_synthesis
      - contradiction_interpretation
      - phase_1_analysis
      - actual_file_read_ledger_reporting
      - wiki_page_drafting
      - semantic_index_summary
      - query_answer_synthesis
      - knowledge_gap_framing
      - operator_review_recommendation
  forbidden_shared_behavior:
    - write_outside_kb_root_without_explicit_operator_approval
    - contact_external_people_or_services
    - use_public_web_without_operator_request
    - treat_old_apex_kb_drafts_as_canonical
    - replace_blueprint_mechanisms_with_generic_KB_advice
    - collapse_python_and_llm_ownership
    - treat_manifest_as_source_comprehension
    - substitute_prior_chat_memory_for_source_reading
```

# Source Intake Lock Rules

```yaml
source_intake_lock_rules:
  purpose: >
    Lock source universe, custody, inventory, first-class source IDs, exclusions,
    and pointer-only exceptions before semantic ingest for large, nested,
    skill-generation, or research-base KBs.
  required_when:
    - custody_profile_is_skill_generation
    - custody_profile_is_research_base
    - source_set_is_large_or_nested
    - operator_rejects_pointer_only
    - source_contains_nested_packages_or_blueprint_corpora
    - prior_failure_involved_pseudo_validation_or_unread_sources
  output_path: "log/source-intake-lock.md"
  template: "templates/source-intake-lock-template.md"
  must_record:
    - accepted_sources
    - excluded_or_deferred_sources
    - source_id_mapping
    - original_path_or_url
    - snapshot_path_or_pointer_exception
    - observed_inventory
    - missing_expected_items
    - nested_source_promotions
    - pointer_only_exceptions
    - phase_1_ready_or_blocked_verdict
  must_not:
    - create_wiki_pages
    - claim_semantic_understanding
    - treat_source_intake_lock_as_phase_1_analysis
```

# Ingest Rules

```yaml
ingest_rules:
  purpose: >
    Convert one preserved source or approved pointer exception into Phase 1 analysis
    first, then approved wiki pages, manifest updates, index updates, and review flags.
  modes:
    ingest_phase_1:
      writes_allowed:
        - "ingest-analysis/<source-slug>.analysis.md"
      writes_forbidden:
        - "wiki/concepts/*"
        - "wiki/entities/*"
        - "wiki/summaries/*"
        - "semantic sections of wiki/index.md"
      must_halt_after_phase_1: true
    ingest_phase_2:
      requires_operator_confirmation: true
      confirmation_phrase: "approve ingest"
      writes_allowed:
        - "wiki/concepts/*"
        - "wiki/entities/*"
        - "wiki/summaries/*"
        - "wiki/index.md"
        - "manifests/source-manifest.json"
        - "audit/*"
        - "log/*"
  phase_gate_policy:
    normal_mode:
      same_prompt_approval_allowed: false
      requires_separate_operator_turn: true
    explicit_test_mode:
      same_prompt_approval_allowed: true
      condition: "Phase 1 artifacts must exist before Phase 2 generation begins."
  phase_0_preflight:
    owner: python
    required_checks:
      - kb_root_exists
      - kb_schema_exists
      - raw_source_or_approved_pointer_exists
      - source_manifest_exists_or_can_be_created
      - source_hash_calculated_or_no_hash_reason_recorded
      - duplicate_source_hash_checked
      - previous_ingest_analysis_checked
      - index_freshness_checked
      - strict_profile_custody_checked
    output:
      artifact_name: ingest_preflight_report
      may_be_embedded_in: "ingest-analysis/<source-slug>.analysis.md"
      fields:
        kb_slug: string
        custody_profile: string
        source_path: string
        snapshot_path: string_or_null
        source_hash: string_or_null
        no_hash_reason: string_or_null
        source_status: "new | duplicate | changed | missing | pointer_only_exception | copied | snapshotted"
        existing_manifest_entry: boolean
        existing_phase_1_analysis: boolean
        source_intake_lock_available: boolean
        index_status: "fresh | stale | missing | unknown"
        review_flags: list
  phase_1_analysis:
    owner: llm
    required_input:
      - source_content_or_approved_pointer_metadata
      - kb_schema
      - ingest_preflight_report
      - relevant_existing_index_or_pages_when_available
      - source_intake_lock_when_required
    required_output_path_template: "ingest-analysis/<source-slug>.analysis.md"
    required_sections:
      - source_identity
      - source_summary
      - source_access_ledger_when_required
      - extraction_candidates
      - concept_candidates
      - entity_candidates
      - claim_candidates
      - contradiction_candidates
      - open_questions
      - proposed_wiki_page_changes
      - proposed_index_changes
      - operator_review_gate
    extraction_rules:
      source_summary:
        rule: "Summarize what the source contributes to the KB, not the whole document exhaustively."
      source_access_ledger:
        rule: "List actual files opened/read, files seen but not read, missing expected files, and anti-pseudo-validation checks for strict profiles."
      concepts:
        rule: "Extract reusable ideas, methods, frameworks, distinctions, or terms."
      entities:
        rule: "Extract durable named systems, people, organizations, projects, tools, repos, or artifacts."
      claims:
        rule: "Extract claims only when they affect future reasoning or KB structure."
      contradictions:
        rule: "Compare against existing KB pages when available and flag unresolved conflict."
      open_questions:
        rule: "Capture unclear source authority, missing context, ambiguous terminology, and operator decisions."
    halt_conditions:
      - contradiction_requires_operator_review
      - source_authority_unclear
      - raw_source_missing
      - strict_profile_source_custody_missing
      - source_access_ledger_missing_when_required
      - duplicate_source_hash_with_different_metadata
      - operator_review_policy_requires_gate
      - phase_2_not_approved
  phase_2_generation:
    owner: llm
    requires:
      - completed_phase_1_analysis
      - operator_confirmation_phrase
      - source_access_ledger_when_required
      - source_intake_lock_when_required_or_operator_override
    allowed_actions:
      - create_or_update_summary_pages
      - create_or_update_concept_pages
      - create_or_update_entity_pages
      - add_source_pointers
      - add_wikilinks
      - add_contradiction_callouts
      - add_open_questions
      - draft_llm_summary_index_section
      - propose_manifest_semantic_fields
    page_update_policy:
      prefer_update_existing_page: true
      duplicate_page_creation_requires_reason: true
      preserve_existing_source_pointers: true
      preserve_existing_contradiction_notes: true
      append_or_reconcile_open_questions: true
    manifest_update_policy:
      deterministic_fields_owner: python
      semantic_fields_owner: llm
      required_manifest_effect:
        - source_registered_or_updated
        - source_hash_recorded_or_no_hash_reason_recorded
        - generated_pages_listed
        - phase_1_analysis_path_recorded
        - review_flags_recorded
  phase_3_postflight:
    owner: python
    required_checks:
      - frontmatter_validation
      - source_pointer_presence
      - wikilink_validation
      - stale_index_status
      - manifest_shape_validation
      - strict_profile_custody_fields_present
```

# Query Rules

```yaml
query_rules:
  index_first: true
  default_page_count: "3-5 relevant pages unless the operator requests a broader audit."
  answer_contract:
    must_include:
      - direct_answer_or_summary
      - evidence_pages
      - confidence
      - contradictions_or_gaps
      - source_limits
    must_not:
      - answer_from_raw_memory_when_compiled_pages_exist
      - hide_stale_index_status
      - treat_missing_pages_as_no_issue
      - overread_entire_kb_without_reason
```

# Lint Rules

```yaml
lint_rules:
  quick_lint_owner: python
  full_lint_owner: python_plus_llm
  deterministic_checks:
    - required_paths_exist
    - manifest_valid_json
    - generated_pages_have_frontmatter
    - generated_pages_have_source_pointers
    - wikilinks_resolve
    - orphan_pages_reported
    - stale_index_reported
    - strict_profile_custody_fields_present
  semantic_checks:
    - confidence_claim_label_separated
    - contradictions_visible
    - source_authority_unclear_flags_visible
    - phase_1_read_ledger_present_when_required
    - pages_do_not_claim_unread_sources
  correction_policy:
    auto_rewrite_allowed: false
    operator_decision_required_for_semantic_repairs: true
```

# Audit Rules

```yaml
audit_rules:
  audit_item_types:
    - contradiction
    - missing_source
    - missing_read_ledger
    - source_authority_unclear
    - pointer_only_exception
    - stale_index
    - broken_link
    - operator_feedback
    - quality_issue
  allowed_decisions:
    - accept
    - partial
    - reject
    - defer
  forbidden:
    - delete_resolved_feedback_history
    - silently_resolve_human_feedback
    - convert_audit_items_into_project_tasks_without_apex_plan_handoff
```
