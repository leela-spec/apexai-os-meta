# Apex KB Source Intake Lock Template

Use this template before Phase 1 analysis when the source set is large, nested, high-risk, or used to generate/repair skills.

```yaml
source_intake_lock:
  lock_id: "<kb-slug>-source-intake-lock-YYYY-MM-DD"
  kb_slug: "<kb-slug>"
  custody_profile: "standard | skill_generation | research_base"
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
  created_by: "apex-kb"
  purpose: >
    Lock the accepted source universe, custody mode, inventory, exclusions,
    and pointer-only exceptions before Phase 1 semantic ingest.

operator_decisions:
  critical_sources_must_be_copied_or_snapshotted: true
  pointer_only_allowed_without_exception: false
  phase_1_allowed_after_this_lock: true
  phase_2_allowed_after_this_lock: false
  phase_2_required_phrase: "approve ingest"

accepted_sources:
  - source_id: "<first-class-source-id>"
    original_path_or_url: "<path-or-url>"
    source_family: "official_doc | official_repo | repo_extract | academic | internal_doc | community_corpus | current_package | other"
    authority_tier: "A | B | C | unknown"
    evidence_role: "<what this source should contribute>"
    storage_decision: "snapshot_copy | copy_into_kb | pointer_only_exception"
    snapshot_path: "apex-meta/kb/<kb-slug>/raw/refs/<source-id>/"
    source_hash_or_inventory_hash: "<sha256-or-NA>"
    no_hash_reason: "NA | directory_hash_not_available | binary | other"
    first_class_reason: "<why this is not hidden under another source>"
    include_reason: "<why accepted>"
    expected_inventory:
      must_have_files_or_patterns: []
      useful_files_or_patterns: []
      optional_files_or_patterns: []
    observed_inventory:
      file_count: 0
      directory_count: 0
      notable_files: []
      notable_directories: []
      missing_expected_items: []
    risk_flags: []
    phase_1_status: "ready | blocked | defer"

excluded_or_deferred_sources:
  - source_id_or_path: "<source-id-or-path>"
    decision: "excluded | deferred | duplicate"
    reason: "<why not included now>"
    revisit_condition: "<when to reconsider, or NA>"

nested_source_promotions:
  - parent_source_id: "<parent>"
    nested_path: "<nested package/corpus path>"
    promoted_source_id: "<new source id>"
    reason: "Own package, own references/scripts/assets, distinct corpus, or distinct authority role."

pointer_only_exceptions:
  - source_id: "<source-id>"
    approved_by_operator: false
    no_copy_reason: "<reason>"
    stable_source_path: "<path>"
    source_hash_or_no_hash_reason: "<hash-or-reason>"
    future_read_access_confirmed: false
    blocks_phase_1: true
    blocks_phase_2: true

anti_pseudo_validation_guard:
  manifest_is_registration_not_understanding: true
  source_intake_lock_is_scope_not_semantic_ingest: true
  phase_1_analysis_must_read_actual_files: true
  final_skill_generation_requires_compiled_wiki_or_operator_override: true

completion_gate:
  ready_for_phase_1_when:
    - every accepted critical source has snapshot_path or approved pointer exception
    - every nested high-value source has first-class source_id or explicit defer decision
    - source-manifest.json records accepted sources
    - this lock file is written under log/
  not_ready_when:
    - accepted source has missing raw/refs copy without exception
    - source identity is broad parent only but hides package/corpus subtrees
    - manifest entry exists but no inventory/custody status is recorded
```
