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

## 7. Uncertainty / Raw Source Triggers

```yaml
uncertainty_triggers:
  # Consolidate contradictions, open questions, and reasons to revisit the raw source.
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<heading/page/line/passage>"
    proposed_handling: "audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator"
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

## 9. Compile Decision

If the selected output tier is `analysis_only` or the safe mode is `phase1_only` / `operator_explicit_stop_before_wiki`, stop here. Otherwise continue into Phase 2 wiki compile and produce pages that implement the adaptive page value contract.
