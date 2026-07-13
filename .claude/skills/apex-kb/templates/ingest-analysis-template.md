---
analysis_id: "<kb-slug>-<source-slug>-analysis"
kb_slug: "<kb-slug>"
source_slug: "<source-slug>"
run_profile:
  output_tier: "source_only | analysis_only | compiled_minimal | compiled_full | query_ready"
  safe_mode: "none | phase1_only | operator_explicit_stop_before_wiki"
source_payload_manifest_ref:
  path: "manifests/source-payload-manifest.json"
  status_at_analysis_time: "fresh | missing | stale | not_checked"
source_ref:
  source_path: "<raw/source/path/or/pointer>"
  source_type: "article | paper | note | ref | other"
  source_hash: "<sha256-or-NA>"
  hash_algorithm: "sha256 | sha256-tree | NA"
  no_hash_reason: "NA | pointer_only | source_unavailable | other"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
semantic_compile_policy:
  phase_2_continues_when_output_tier_includes_wiki: true
  stop_before_wiki_only_for: "analysis_only | phase1_only | operator_explicit_stop_before_wiki"
  optional_resume_phrase: "approve ingest"
---

# Phase 1 Ingest Analysis - <source title>


## 1. Source Identity and Read Record

```yaml
source_identity:
  title: "<explicit title or filename>"
  author_or_origin: "<known or unknown>"
  publication_or_creation_date: "YYYY-MM-DD | YYYY-MM | YYYY | unknown"
  authority_class: "canonical_specification | implementation_evidence | current_contract | user_story_or_example | historical | proposal | secondary | unknown"
  authority_rationale: "<source-grounded rationale>"
  scope: "<what the source covers>"
  limitations: []
source_read:
  read_status: "complete | targeted | blocked"
  reviewed_passages: []
  unavailable_reason: "<reason or NA>"
```

## 2. Target-Query Coverage

```yaml
target_query_coverage:
  - query_id: "<stable query id>"
    outcome: "answered | partial | contradicted | blocked | not_covered"
    answer_or_finding: "<source-grounded result>"
    source_pointers: []
    additional_evidence_required: []
topic_completion_effect: "supports | partial | blocks"
```

## 3. Source Summary

```yaml
source_summary:
  one_sentence_core: "<central contribution>"
  compact_summary: "<source-grounded summary>"
  relevant_to_kb_because: []
  likely_not_relevant_for: []
```

## 4. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "<heading/page/line/passage>"
      reason: "<why it matters>"
      extraction_priority: "high | medium | low"
  reusable_definitions: []
  reusable_processes: []
```

## 5. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "<kebab-case>"
    concept_label: "<label>"
    source_pointer: "<exact pointer>"
    summary: "<source-grounded candidate>"
    confidence: "high | medium | low"
    disposition: "promote | embed_in_summary | defer_blocked | reject_no_independent_value"
    disposition_rationale: "<retrieval-value rationale>"
    target_query_ids: []
    destination_page: "<wiki path or NA>"
```

## 6. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "<kebab-case>"
    entity_label: "<label>"
    entity_type: "person | organization | tool | project | artifact | other"
    source_pointer: "<exact pointer>"
    summary: "<source-grounded candidate>"
    confidence: "high | medium | low"
    disposition: "promote | embed_in_summary | defer_blocked | reject_no_independent_value"
    disposition_rationale: "<retrieval-value rationale>"
    target_query_ids: []
    destination_page: "<wiki path or NA>"
```

## 7. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<heading/page/line/passage>"
    target_query_ids: []
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```

## 8. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "<conflict, gap, or uncertainty>"
    source_pointer: "<pointer>"
    availability_class: "evidence_unavailable | evidence_conflict | future_change | readable_unopened"
    completion_effect: "none | supporting_gap | blocks_priority_query"
    affected_query_ids: []
    proposed_handling: "audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator"
```

## 9. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  summaries: []
  concepts: []
  entities: []
page_architecture_rationale: "<answer coverage and duplication rationale>"
audit_items: []
manifest_updates: []
```

## 10. Compile Decision

```yaml
compile_decision:
  status: operator_review_needed
  phase_2_ready: true | false
  unresolved_priority_query_ids: []
  additional_sources_to_read: []
  truthful_state_if_stopped: "analysis_complete_unvalidated | partial"
```

Stop for `analysis_only` or an explicit safe mode. Otherwise continue only when critical evidence coverage is resolved; Phase 2 must follow the v2 page and semantic-acceptance contracts.
