---
analysis_id: "<kb-slug>-<source-slug>-analysis"
kb_slug: "<kb-slug>"
source_slug: "<source-slug>"
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
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
---

# Phase 1 Ingest Analysis - <source title>

## 1. Source Identity

```yaml
source_identity:
  title: "<explicit title or filename>"
  author_or_origin: "<known or unknown>"
  publication_or_creation_date: "YYYY-MM-DD | YYYY-MM | YYYY | unknown"
  source_authority_level: "primary | secondary | tertiary | unclear"
  source_authority_rationale: "<source-grounded rationale>"
  source_scope: "<what the source covers>"
  source_limitations:
    - "<limitation or uncertainty>"
```

## 2. Source Summary

```yaml
source_summary:
  one_sentence_core: "<central contribution>"
  compact_summary: "<3-7 sentence source-grounded summary>"
  relevant_to_kb_because:
    - "<reason>"
  likely_not_relevant_for:
    - "<scope limit>"
```

## 3. Extraction Candidates

```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "<heading/page/line/passage>"
      reason: "<why it matters>"
      extraction_priority: "high | medium | low"
  reusable_definitions: []
  reusable_processes: []
```

## 4. Concept Candidates

```yaml
concept_candidates:
  - concept_slug: "<kebab-case>"
    concept_label: "<label>"
    source_pointer: "<heading/page/line/passage>"
    summary: "<source-grounded candidate>"
    confidence: "high | medium | low"
```

## 5. Entity Candidates

```yaml
entity_candidates:
  - entity_slug: "<kebab-case>"
    entity_label: "<label>"
    entity_type: "person | organization | tool | project | artifact | other"
    source_pointer: "<heading/page/line/passage>"
    summary: "<source-grounded candidate>"
    confidence: "high | medium | low"
```

## 6. Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<heading/page/line/passage>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```

## 7. Contradictions and Open Questions

```yaml
contradictions: []
open_questions:
  - question_id: Q001
    question: "<question>"
    proposed_handling: "audit_item | planning_task_candidate | leave_as_gap | ask_operator"
```

## 8. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  summaries: []
  concepts: []
  entities: []
audit_items: []
manifest_updates: []
```

## 9. Operator Gate

Stop here. Do not generate wiki pages until the operator provides the exact phrase `approve ingest` after reviewing this analysis.
