# Apex KB Ingest Analysis Template

```yaml
template_metadata:
  artifact_name: apex_kb_ingest_analysis
  file_role: phase_1_ingest_analysis_template
  package_path: ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
  output_path_template: "apex-meta/kb/<kb-slug>/ingest-analysis/<source-slug>.analysis.md"
  canonical_rules:
    kb_contract: ".claude/skills/apex-kb/references/kb-contract.md"
    operation_rules: ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    source_custody_rules: ".claude/skills/apex-kb/references/source-custody-and-read-verification.md"
    script_contract: ".claude/skills/apex-kb/references/script-command-contract.md"
  phase: ingest_phase_1
  required_halt_after_completion: true
  phase_2_requires_operator_phrase: "approve ingest"
  purpose: >
    Capture the LLM-owned semantic analysis of one preserved source before wiki
    page generation. This artifact proves what the source contributes, what
    files were actually opened/read, what was skipped, what should become wiki
    knowledge, and what requires operator review.
  write_scope:
    allowed_path: "apex-meta/kb/<kb-slug>/ingest-analysis/"
    forbidden_paths_during_phase_1:
      - "apex-meta/kb/<kb-slug>/wiki/"
      - "apex-meta/kb/<kb-slug>/manifests/source-manifest.json"
      - "apex-meta/kb/<kb-slug>/outputs/queries/"
      - "apex-meta/kb/<kb-slug>/audit/resolved/"
```

# Required Header

```yaml
ingest_analysis:
  analysis_id: "<kb-slug>-<source-slug>-analysis"
  kb_slug: "<kb-slug>"
  source_slug: "<source-slug>"
  custody_profile: "standard | skill_generation | research_base"
  source_ref:
    source_path: "<raw/source/path/or/approved-pointer>"
    snapshot_path: "apex-meta/kb/<kb-slug>/raw/refs/<source-id>/ | NA"
    source_type: "article | paper | note | ref | directory | package | other"
    source_hash_or_inventory_hash: "<sha256-or-NA>"
    hash_algorithm: "sha256 | directory_inventory | NA"
    no_hash_reason: "NA | pointer_exception | source_unavailable | binary | other"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
  created_by: "apex-kb"
  phase: ingest_phase_1
  status: operator_review_needed
  preflight:
    report_available: true
    source_intake_lock_available: true_or_false
    duplicate_source_candidates: []
    existing_manifest_entry: false
    existing_phase_1_analysis: false
    index_status: "fresh | stale | missing | unknown"
    preflight_review_flags: []
  operator_gate:
    phase_2_allowed: false
    required_confirmation_phrase: "approve ingest"
```

# 1. Source Identity

```yaml
source_identity:
  title: "<source title if explicit, otherwise filename/folder name>"
  author_or_origin: "<author/origin if known, otherwise unknown>"
  publication_or_creation_date: "YYYY-MM-DD | YYYY-MM | YYYY | unknown"
  source_authority_level: "primary | secondary | tertiary | unclear"
  source_authority_rationale: >
    <Short reason based only on available source context and kb-schema authority policy.>
  source_scope: >
    <What this source appears to cover.>
  source_limitations:
    - "<Known limitation, missing context, partial extraction, or uncertainty.>"
```

# 2. Source Access Ledger

Required for `skill_generation` and `research_base` custody profiles. Optional but recommended for `standard`.

```yaml
source_access_ledger:
  custody_profile: "standard | skill_generation | research_base"
  custody_verdict: "copied_or_snapshotted | pointer_exception_approved | insufficient_custody"
  source_root_examined: "apex-meta/kb/<kb-slug>/raw/refs/<source-id>/ | <approved pointer path>"
  files_opened_and_read:
    - path: "<relative path under raw/refs or approved pointer path>"
      read_depth: "full | targeted_sections | metadata_only"
      sections_or_ranges:
        - "<heading, line range, page range, or NA>"
      why_read: "<reason this file matters>"
      evidence_contribution: "<what this file contributed to analysis>"
  files_seen_but_not_read:
    - path: "<relative path>"
      reason_not_read: "binary | duplicate | irrelevant | too_large | deferred | inaccessible"
      blocks_phase_2: true_or_false
  missing_expected_files:
    - expected_path_or_pattern: "<path or pattern>"
      reason_expected: "<why it should exist>"
      blocks_phase_2: true_or_false
  anti_pseudo_validation_check:
    manifest_only_used_as_evidence: false
    prior_chat_memory_used_as_source: false
    path_name_used_as_content_evidence: false
    summary_substituted_for_source: false
```

# 3. Source Summary

```yaml
source_summary:
  one_sentence_core: >
    <One sentence capturing the source's central knowledge contribution.>
  compact_summary: >
    <Dense 3-7 sentence summary. Preserve specificity. Do not generalize beyond the source.>
  relevant_to_kb_because:
    - "<Reason this source belongs in this KB.>"
  likely_not_relevant_for:
    - "<Topic or use case this source does not support.>"
```

# 4. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "<heading/page/anchor/line/passage reference>"
      reason: "<Why this section matters>"
      extraction_priority: "high | medium | low"
  reusable_definitions:
    - term: "<term>"
      source_pointer: "<heading/page/anchor/line/passage reference>"
      definition_candidate: >
        <Source-grounded definition candidate.>
      confidence: "high | medium | low"
  reusable_processes:
    - process_name: "<process name>"
      source_pointer: "<heading/page/anchor/line/passage reference>"
      process_summary: >
        <Process logic extracted from source.>
      possible_apex_use: >
        <How this process might be reusable in Apex KB or downstream packages.>
      confidence: "high | medium | low"
```

# 5. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "<kebab-case-concept-slug>"
    concept_label: "<Human readable concept label>"
    source_pointers:
      - "<heading/page/anchor/line/passage reference>"
    concept_summary: >
      <What the source says about this concept.>
    proposed_page_action: "create | update | no_page_needed"
    proposed_page_path: "wiki/concepts/<concept-slug>.md"
    related_existing_pages:
      - "<existing wiki page path or none>"
    confidence: "high | medium | low"
    review_flags: []
```

# 6. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "<kebab-case-entity-slug>"
    entity_label: "<Human readable entity label>"
    entity_type: "person | organization | project | tool | framework | file | artifact | other"
    source_pointers:
      - "<heading/page/anchor/line/passage reference>"
    entity_summary: >
      <What the source establishes about this entity.>
    proposed_page_action: "create | update | no_page_needed"
    proposed_page_path: "wiki/entities/<entity-slug>.md"
    related_existing_pages:
      - "<existing wiki page path or none>"
    confidence: "high | medium | low"
    review_flags: []
```

# 7. Claim Candidates

```yaml
claim_candidates:
  - claim_id: "C001"
    claim_text: >
      <Specific claim extracted from the source.>
    source_pointer: "<heading/page/anchor/line/passage reference>"
    claim_type: "definition | decision | fact | recommendation | warning | open_question | other"
    applies_to:
      - "<concept/entity/artifact/process>"
    confidence: "high | medium | low"
    proposed_destination:
      page_type: "summary | concept | entity | index | audit | none"
      page_path: "<proposed page path or NA>"
    review_flags: []
```

# 8. Contradiction Candidates

```yaml
contradiction_candidates:
  status: "none_detected | possible | confirmed"
  items:
    - contradiction_id: "X001"
      severity: "low | medium | high"
      source_claim: >
        <Claim from the current source.>
      conflicting_existing_claim: >
        <Claim from existing KB material, if known.>
      current_source_pointer: "<heading/page/anchor/line/passage reference>"
      existing_source_pointer: "<existing page/source pointer or unknown>"
      interpretation: >
        <Neutral explanation of the conflict. Do not silently resolve.>
      proposed_handling: "add_contradiction_callout | create_audit_item | ask_operator | ignore_with_reason"
      review_required: true
```

# 9. Proposed Wiki Page Changes

```yaml
proposed_wiki_page_changes:
  summaries:
    - action: "create | update | skip"
      path: "wiki/summaries/<source-slug>.md"
      reason: "<Why this page should or should not exist>"
      source_pointers_required: true
  concepts:
    - action: "create | update | skip"
      path: "wiki/concepts/<concept-slug>.md"
      reason: "<Why this concept page should or should not be changed>"
      source_pointers_required: true
  entities:
    - action: "create | update | skip"
      path: "wiki/entities/<entity-slug>.md"
      reason: "<Why this entity page should or should not be changed>"
      source_pointers_required: true
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "<LLM-owned summary, category, gap, or contradiction note for index LLM section.>"
```

# 10. Proposed Manifest Updates

```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "<source-id>"
    source_path: "<raw/source/path/or/approved-pointer>"
    snapshot_path: "<snapshot path or NA>"
    source_hash_or_inventory_hash: "<sha256-or-NA>"
    hash_algorithm: "sha256 | directory_inventory | NA"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/<source-slug>.analysis.md"
    generated_pages: []
    semantic_tags:
      - "<tag>"
    concept_candidates:
      - "<concept-slug>"
    entity_candidates:
      - "<entity-slug>"
    review_flags:
      - "<flag or empty>"
```

# 11. Open Questions

```yaml
open_questions:
  operator_questions:
    - question_id: "Q001"
      question: "<Question needed before Phase 2 can safely generate/update pages.>"
      blocks_phase_2: true
      related_source_pointer: "<heading/page/anchor/line/passage reference or NA>"
  kb_questions:
    - question_id: "KQ001"
      question: "<Knowledge gap discovered from the source.>"
      proposed_handling: "audit_item | planning_task_candidate | leave_as_gap | ask_operator"
      related_pages:
        - "<page path or none>"
```

# 12. Review Flags

```yaml
review_flags:
  - flag_id: "RF001"
    type: "source_authority | contradiction | missing_context | duplicate_source | missing_read_ledger | pointer_exception | ambiguous_entity | naming | scope | other"
    severity: "low | medium | high"
    summary: "<Short review flag summary.>"
    required_before_phase_2: true
    proposed_resolution: "<What the operator or LLM should do next.>"
```

# 13. Operator Review Gate

```yaml
operator_review_gate:
  phase_1_result: "ready_for_operator_review | blocked | insufficient_source"
  phase_2_recommendation: "approve | approve_with_changes | reject | defer"
  phase_2_allowed_now: false
  required_operator_phrase: "approve ingest"
  recommended_operator_decision:
    decision: "approve | approve_with_changes | reject | defer"
    rationale: >
      <Short rationale based on source value, custody, files read, contradictions, and open questions.>
  if_approved_next_actions:
    - "Generate or update summary page with source pointers."
    - "Generate or update approved concept pages with source pointers."
    - "Generate or update approved entity pages with source pointers."
    - "Update LLM summary section of wiki/index.md."
    - "Run deterministic postflight lint."
  if_rejected_next_actions:
    - "Do not generate wiki pages."
    - "Keep this analysis as rejected or archived Phase 1 evidence if useful."
    - "Record rejection reason if operator provides one."
```

# Completion Gate

```yaml
completion_gate:
  invalid_if:
    - generated_wiki_content_during_phase_1
    - source_pointers_missing_from_claims
    - source_access_ledger_missing_for_strict_profile
    - manifest_or_prior_memory_substituted_for_source_reading
    - contradiction_silently_resolved
    - operator_gate_omitted
    - phase_2_marked_allowed_without_operator_phrase
```
