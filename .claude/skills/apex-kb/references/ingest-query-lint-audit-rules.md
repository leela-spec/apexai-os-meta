# Apex KB Ingest, Query, Lint, and Audit Rules
```yaml
rules_document:
  artifact_name: apex_kb_operation_rules
  file_role: operational_rules_for_ingest_query_lint_audit
  package_path: ".claude/skills/apex-kb/"
  canonical_contract: "references/kb-contract.md"
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
      - llm_wiki_review_json_to_apex_audit_files_or_manifest_flags
    out_of_scope_for_this_file:
      - script_cli_command_contract
      - exact_python_argument_names
      - wiki_page_templates
      - package_manifest
      - graph_visualization
      - Obsidian_plugin_UI
```


#

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
    raw_source_or_pointer_required: true
    generated_pages_require_source_pointers: true
    missing_source_rule: "Never infer source contents from filename, title, summary, or prior memory."
    contradiction_rule: "Expose contradictions instead of silently resolving them."
  source_storage_policy:
    allowed_modes:
      - pointer_only
      - copy_into_kb
      - snapshot_copy
    default_for_repo_internal_sources: pointer_only
    default_for_external_or_uploaded_sources: copy_into_kb
    generated_pages_must_record:
      - source_storage_mode
      - source_path
      - source_hash

  epistemic_fields:
    confidence:
      meaning: "How strongly the KB should trust the page or claim."
      allowed:
        - high
        - medium
        - low
        - mixed
        - unknown
    claim_label:
      meaning: "What kind of epistemic object the statement is."
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
      - concept_extraction
      - entity_synthesis
      - contradiction_interpretation
      - phase_1_analysis
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
```


#

# Ingest Rules
```yaml
ingest_rules:
  purpose: >
    Convert one raw source or source pointer into Phase 1 analysis first, then
    approved wiki pages, manifest updates, index updates, and review flags.
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
      - raw_source_or_pointer_exists
      - source_manifest_exists_or_can_be_created
      - source_hash_calculated_or_no_hash_reason_recorded
      - duplicate_source_hash_checked
      - previous_ingest_analysis_checked
      - index_freshness_checked
    output:
      artifact_name: ingest_preflight_report
      may_be_embedded_in: "ingest-analysis/<source-slug>.analysis.md"
      fields:
        kb_slug: string
        source_path: string
        source_hash: string_or_null
        no_hash_reason: string_or_null
        source_status: "new | duplicate | changed | missing | pointer_only"
        existing_manifest_entry: boolean
        existing_phase_1_analysis: boolean
        index_status: "fresh | stale | missing | unknown"
        review_flags: list
  phase_1_analysis:
    owner: llm
    required_input:
      - source_content_or_pointer_metadata
      - kb_schema
      - ingest_preflight_report
      - relevant_existing_index_or_pages_when_available
    required_output_path_template: "ingest-analysis/<source-slug>.analysis.md"
    required_sections:
      - source_identity
      - source_summary
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
      - duplicate_source_hash_with_different_metadata
      - operator_review_policy_requires_gate
      - phase_2_not_approved
  phase_2_generation:
    owner: llm
    requires:
      - completed_phase_1_analysis
      - operator_confirmation_phrase
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
      - broken_wikilink_detection
      - orphan_page_detection
      - stale_index_detection
      - manifest_shape_validation
    output:
      artifact_name: ingest_postflight_report
      fields:
        status: "passed | passed_with_flags | failed"
        generated_pages: list
        updated_pages: list
        manifest_status: string
        broken_links: list
        orphan_pages: list
        stale_index: boolean
        review_flags: list
```


#

# Query Rules
```yaml
query_rules:
  purpose: >
    Answer operator or agent questions from the compiled KB by reading the
    index first, then a small relevant set of wiki pages, and reporting
    evidence, contradictions, confidence, and gaps.
  index_first_required: true
  default_relevant_page_count:
    minimum: 3
    maximum: 5
    exception: "Read more only when the query spans many page families or the index is stale."
  required_read_sequence:
    1: "Read wiki/index.md."
    2: "Select likely relevant summaries, concepts, and entities."
    3: "Read the selected pages."
    4: "Answer from compiled KB pages."
    5: "Report evidence pages, contradictions, confidence, and gaps."
  query_inputs:
    required:
      - kb_slug
      - question
    optional:
      - preferred_page_family
      - save_query_output
      - confidence_threshold
      - include_open_questions
      - include_source_pointers
  answer_contract:
    required_sections:
      - answer
      - evidence_pages
      - confidence
      - contradictions
      - knowledge_gaps
      - suggested_followups
    confidence_values:
      - high
      - medium
      - low
      - insufficient_kb_evidence
    evidence_page_fields:
      - page_path
      - page_type
      - relevance_reason
      - source_pointer_available
  save_query_output:
    default: false
    path_template: "outputs/queries/<query-slug>.md"
    save_when:
      - operator_requests_save
      - answer_is_reusable_context
      - query_resolves_recurring_decision
      - query_exposes_major_KB_gap
  forbidden_query_behavior:
    - answer_from_unread_pages
    - answer_from_memory_when_compiled_pages_are_available
    - hide_stale_index_status
    - claim_raw_source_support_without_source_pointer
    - read_entire_KB_by_default
    - create_new_wiki_pages_during_query_without_operator_request
```


#

# Lint Rules
```yaml
lint_rules:
  purpose: >
    Check KB health with deterministic validation first, then optional semantic
    review flags when a full lint is requested.
  lint_modes:
    quick_lint:
      owner: python
      token_cost: low
      checks:
        - kb_root_exists
        - kb_schema_exists
        - index_exists
        - required_directories_exist
        - frontmatter_shape_valid
        - dead_wikilinks
        - orphan_pages
        - source_manifest_exists
        - stale_index_status
        - audit_folder_shape
    full_lint:
      owner: python_plus_llm
      token_cost: medium
      python_checks:
        - all_quick_lint_checks
        - source_pointer_presence
        - manifest_source_page_consistency
        - audit_target_existence
        - query_output_shape
      llm_checks:
        - weak_page_summaries
        - missing_concept_descriptions
        - unclear_entity_pages
        - unresolved_contradiction_quality
        - stale_semantic_index_summary
        - likely_missing_crosslinks
        - knowledge_gap_quality
  lint_report_contract:
    required_sections:
      - deterministic_findings
      - semantic_review_flags
      - broken_links
      - orphan_pages
      - stale_index
      - missing_source_pointers
      - malformed_pages
      - audit_shape_issues
      - recommended_next_action
    status_values:
      - passed
      - passed_with_flags
      - failed
  correction_policy:
    automatic_rewrites_allowed: false
    allowed_without_operator_confirmation:
      - report_findings
      - propose_corrections
      - identify_files_to_update
    requires_operator_confirmation:
      - edit_wiki_pages
      - edit_kb_schema
      - resolve_audit_items
      - rebuild_semantic_index_summary
  forbidden_lint_behavior:
    - silently_fix_pages
    - delete_orphans_without_review
    - remove_source_pointers
    - collapse_deterministic_findings_into_semantic_opinion
    - treat_llm_quality_flags_as_parser_errors
```


#

# Audit Rules
```yaml
audit_rules:
  purpose: >
    Capture, group, review, and resolve human or model feedback about KB page
    quality, contradictions, staleness, naming, gaps, or source problems.
  audit_item_types:
    - contradiction
    - quality
    - staleness
    - gap
    - naming
    - source_authority
    - broken_link
    - missing_source_pointer
    - duplicate_page
    - operator_note
  audit_locations:
    open_items: "audit/"
    resolved_items: "audit/resolved/"
  audit_item_contract:
    required_fields:
      audit_id: string
      type: string
      severity: "low | medium | high | critical"
      target_path: string
      target_anchor: string_or_null
      source_ref: string_or_null
      created_at: "YYYY-MM-DD"
      status: "open | resolved | deferred | rejected"
      summary: string
      proposed_resolution: string_or_null
  audit_review_sequence:
    1: "List open audit items."
    2: "Group by target_path, type, and severity."
    3: "Select one item or one target group for review."
    4: "Read the target page and source pointers when available."
    5: "Propose accept, partial, reject, or defer."
    6: "Apply resolution only after operator decision."
    7: "Move resolved item to audit/resolved/ while preserving history."
  operator_decisions:
    accept:
      meaning: "Apply the proposed correction or page update."
    partial:
      meaning: "Apply only specified parts; keep remaining issue open or deferred."
    reject:
      meaning: "Do not apply; preserve rejection reason."
    defer:
      meaning: "Keep item open or mark deferred with next review condition."
  forbidden_audit_behavior:
    - resolve_feedback_without_operator_decision
    - delete_audit_history
    - edit_target_page_without_reading_it
    - assume_source_authority_when_schema_is_unclear
    - merge_unrelated_audit_items_only_because_they_share_a_page
```


#

# Review Flags and Failure Modes
```yaml
review_flags_and_failure_modes:
  review_flags:
    source_missing:
      severity: critical
      action: "Stop ingest or query claim that depends on missing source."
    kb_schema_missing:
      severity: critical
      action: "Stop unless scaffold mode is active."
    duplicate_source_hash:
      severity: medium
      action: "Report duplicate and ask whether to skip, compare, or reingest."
    contradiction_detected:
      severity: high
      action: "Record contradiction and require operator review when policy says so."
    source_authority_unclear:
      severity: high
      action: "Use kb_source_authority_list or request operator decision."
    stale_index:
      severity: medium
      action: "Report before query confidence or run deterministic rebuild when approved."
    broken_wikilinks:
      severity: medium
      action: "Report affected pages and links."
    orphan_pages:
      severity: low
      action: "Report and propose link or archive decision."
    phase_2_without_approval:
      severity: critical
      action: "Stop and request exact confirmation phrase."
    external_contact_requested_or_implied:
      severity: critical
      action: "Refuse external contact and keep work local."
  failure_modes:
    missing_kb_slug:
      correction: "Request kb_slug or infer only if supplied in path."
    missing_kb_root:
      correction: "Offer scaffold mode or request existing root."
    missing_raw_source:
      correction: "Request source path or source pointer."
    malformed_kb_schema:
      correction: "Report invalid fields and stop semantic operations."
    invalid_source_manifest:
      correction: "Run or request deterministic manifest validation."
    missing_phase_1_analysis:
      correction: "Run ingest_phase_1 before ingest_phase_2."
    operator_gate_not_satisfied:
      correction: "Stop before Phase 2 writes."
    query_insufficient_evidence:
      correction: "Answer with insufficient_kb_evidence and list gaps."
    lint_failed:
      correction: "Return report; do not auto-fix."
    audit_resolution_unapproved:
      correction: "Keep item open or deferred."
```


#

# Completion Gates
```yaml
completion_gates:
  ingest_phase_1_complete:
    required:
      - ingest_analysis_file_created
      - source_identity_recorded
      - source_summary_created
      - concept_candidates_listed
      - entity_candidates_listed
      - contradiction_candidates_listed_or_none_recorded
      - open_questions_recorded_or_none_recorded
      - proposed_page_changes_listed
      - operator_review_gate_present
      - no_wiki_pages_written
  ingest_phase_2_complete:
    required:
      - operator_confirmation_phrase_received
      - approved_page_changes_applied
      - generated_or_updated_pages_have_source_pointers
      - contradictions_preserved_or_reviewed
      - source_manifest_updated_or_failure_reported
      - index_updated_or_stale_index_flagged
      - postflight_report_created
  query_complete:
    required:
      - index_read_first
      - relevant_pages_read
      - answer_grounded_in_pages
      - evidence_pages_named
      - contradictions_reported
      - knowledge_gaps_reported
      - confidence_stated
  quick_lint_complete:
    required:
      - deterministic_findings_reported
      - broken_links_reported
      - orphan_pages_reported
      - stale_index_status_reported
      - missing_required_paths_reported
  full_lint_complete:
    required:
      - quick_lint_completed
      - semantic_review_flags_reported
      - source_pointer_quality_checked
      - recommended_next_action_present
  audit_complete:
    required:
      - open_items_grouped
      - selected_item_or_group_reviewed
      - operator_decision_recorded_or_requested
      - resolved_items_archived_when_approved
      - unresolved_items_preserved
