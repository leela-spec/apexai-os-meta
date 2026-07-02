---
analysis_id: claude-skill-design-secondary-navigation-analysis
kb_slug: claude-skill-design
source_slug: secondary-navigation
phase: ingest_phase_1
status: operator_review_needed
phase_2_allowed: false
required_confirmation_phrase: "approve ingest"
created_by: apex-kb
created_at: "2026-06-25T12:09:30Z"
---

# Phase 1 Ingest Analysis: Secondary Navigation

```yaml
source_ref:
  source_path: "apex-meta/kb/claude-skill-design/sources/curated/secondary/"
  source_type: "ref"
  source_storage_mode: "pointer_only"
  source_hash: "f3fcc320e9cb29139010d2de0e9a4ee4a7727db498acd82d7d74e45aa1dfcda6"
  hash_algorithm: "sha256"
  no_hash_reason: "NA"
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
```

## 1. Source Identity

```yaml
source_identity:
  title: "Secondary navigation and indexing pages"
  author_or_origin: "DeepWiki and related secondary sources"
  publication_or_creation_date: "unknown"
  source_authority_level: "secondary"
  source_authority_rationale: "Useful for navigation and discovery, but not canonical for claims about official skill behavior."
  source_scope: "Repository overviews, format-specification navigation, and secondary summaries."
  source_limitations:
    - "Secondary pages may summarize or transform primary content."
    - "Should not be used for canonical claims when official docs or repo files are available."
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "Secondary sources are useful navigation aids for finding relevant official/repo evidence but should not carry canonical claims."
  compact_summary: >
    The secondary group appears best suited to indexing, orientation, and source discovery.
    It can help identify which parts of official repos/specification pages deserve closer reading,
    but Phase 2 should cite primary sources for substantive claims whenever available. Secondary
    sources can still support a navigation note or an audit trail explaining how source groups were found.
  relevant_to_kb_because:
    - "Helps route future analysis through large repos."
    - "Can support source-discovery provenance."
  likely_not_relevant_for:
    - "Authoritative definitions of SKILL.md behavior."
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "secondary/deepwiki-anthropics-skills.html"
      reason: "Repository navigation and overview."
      extraction_priority: "low"
    - section_ref: "secondary/deepwiki-skill-md-format-specification.html"
      reason: "May help locate specification-relevant sections."
      extraction_priority: "low"
  reusable_definitions: []
  reusable_processes:
    - process_name: "secondary-source-as-navigation-only"
      source_pointer: "secondary/"
      process_summary: "Use secondary pages to discover primary evidence, then cite primary evidence in generated wiki pages."
      possible_apex_use: "Create a KB source authority rule."
      confidence: "medium"
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "source-authority-tiering"
    concept_label: "Source authority tiering"
    source_pointers:
      - "secondary/"
      - "official-docs/*.meta.md"
    concept_summary: "The KB should separate official claims, research interpretation, secondary navigation, and operator house rules."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/source-authority-tiering.md"
    related_existing_pages: ["none"]
    confidence: "medium"
    review_flags:
      - "requires kb-schema authority list"
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "deepwiki"
    entity_label: "DeepWiki"
    entity_type: "tool"
    source_pointers:
      - "secondary/deepwiki-anthropics-skills.html.meta.md"
      - "secondary/deepwiki-skill-md-format-specification.html.meta.md"
    entity_summary: "Secondary navigation source used for repo/spec orientation."
    proposed_page_action: "create"
    proposed_page_path: "wiki/entities/deepwiki.md"
    related_existing_pages: ["none"]
    confidence: "medium"
    review_flags:
      - "secondary authority only"
```

## 6. Claim Candidates

```yaml
claim_candidates:
  - claim_id: "C001"
    claim_text: "Secondary sources should be marked as navigation/indexing evidence rather than canonical support when primary sources exist."
    source_pointer: "corpus process note and secondary source group role"
    claim_label: "behavioral_inference"
    applies_to: ["source-authority-tiering"]
    confidence: "medium"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/source-authority-tiering.md"
    review_flags:
      - "operator should confirm authority policy."
```

## 7. Contradiction Candidates

```yaml
contradiction_candidates:
  status: "none_detected"
  items: []
```

## 8. Proposed Wiki Page Changes

```yaml
proposed_wiki_page_changes:
  summaries:
    - action: "create"
      path: "wiki/summaries/secondary-navigation.md"
      reason: "Document secondary source role and limitations."
      source_pointers_required: true
  concepts:
    - action: "create"
      path: "wiki/concepts/source-authority-tiering.md"
      reason: "Needed to safely combine mixed source types."
      source_pointers_required: true
  entities:
    - action: "create"
      path: "wiki/entities/deepwiki.md"
      reason: "Track secondary source origin."
      source_pointers_required: true
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "Secondary sources are navigation aids, not canonical claim sources."
```

## 9. Proposed Manifest Updates

```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "secondary-navigation"
    source_path: "apex-meta/kb/claude-skill-design/sources/curated/secondary/"
    source_hash: "f3fcc320e9cb29139010d2de0e9a4ee4a7727db498acd82d7d74e45aa1dfcda6"
    hash_algorithm: "sha256"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/secondary-navigation.analysis.md"
    generated_pages: []
    semantic_tags: ["secondary", "navigation", "source-authority"]
    concept_candidates: ["source-authority-tiering"]
    entity_candidates: ["deepwiki"]
    review_flags: ["secondary_not_canonical"]
```

## 10. Open Questions

```yaml
open_questions:
  operator_questions:
    - question_id: "Q001"
      question: "Should secondary sources be excluded from Phase 2 claim pages except for provenance/navigation notes?"
      blocks_phase_2: false
      related_source_pointer: "secondary/"
  kb_questions: []
```

## 11. Review Flags

```yaml
review_flags:
  - flag_id: "RF001"
    type: "source_authority"
    severity: "medium"
    summary: "Secondary sources should not be treated as canonical."
    required_before_phase_2: false
    proposed_resolution: "Use them for discovery/provenance unless operator authorizes a broader role."
```

## 12. Operator Review Gate

```yaml
operator_review_gate:
  phase_1_result: "ready_for_operator_review"
  phase_2_recommendation: "approve_with_changes"
  phase_2_allowed_now: false
  required_operator_phrase: "approve ingest"
  recommended_operator_decision:
    decision: "approve_with_changes"
    rationale: "Include as navigation/provenance support, not primary evidence."
```
