```yaml
ingest_analysis:
  analysis_id: "apex-kb-skill-test-et-heller-narm-analysis"
  kb_slug: "apex-kb-skill-test"
  source_slug: "et-heller-narm"
  source_ref:
    source_path: "apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md"
    source_type: "note"
    source_hash: "64a0dae9c1cbc3bba6bd0299e345a4863560c6bce22b60444755585d0e06e6cd"
    hash_algorithm: "sha256"
    no_hash_reason: "NA"
  created_at: "2026-06-22T20:20:00Z"
  created_by: "apex-kb"
  phase: ingest_phase_1
  status: operator_review_needed
  preflight:
    report_available: true
    duplicate_source_candidates: []
    existing_manifest_entry: false
    existing_phase_1_analysis: false
    index_status: "missing"
    preflight_review_flags: []
  operator_gate:
    phase_2_allowed: false
    required_confirmation_phrase: "approve ingest"
```

# 1. Source Identity
```yaml
source_identity:
  title: "Entwicklungstrauma heilen / NARM notes"
  author_or_origin: "Laurence Heller, Aline LaPierre, Angelika Doerne material as captured in source"
  publication_or_creation_date: "unknown"
  source_authority_level: "primary"
  source_authority_rationale: "Operator supplied raw notes; the source itself presents NARM concepts and authorship context."
  source_scope: "NARM model, five biologically based core needs, five adaptive survival structures, nervous-system regulation, anger, grief, contact, and recovery."
  source_limitations:
    - "Source text is an extracted markdown note with OCR/encoding artifacts."
    - "This analysis only extracts the passages needed for the small skill-package test KB."
```

# 2. Source Summary
```yaml
source_summary:
  one_sentence_core: "The source frames NARM as a resource-oriented model for restoring contact, self-regulation, identity, and aliveness by understanding five core needs and five adaptive survival structures."
  compact_summary: "The source states that NARM emphasizes present-moment contact with body, feelings, and others while considering early coping patterns only insofar as they affect current contact and aliveness. It identifies five biologically based core needs: contact, attunement, trust, autonomy, and love/sexuality. When these needs are chronically unmet, five corresponding adaptive survival structures develop, each tied to impaired core capacities. The source also treats anger and aggression as life-force expressions that can become dysregulated when needs are unmet, and it distinguishes integrated anger from blame. Later passages connect integrated anger with access to grief over lost contact."
  relevant_to_kb_because:
    - "Provides the main source-backed framework for the test KB's concept pages."
  likely_not_relevant_for:
    - "Does not by itself establish a diagnosis or a complete individual treatment plan."
```

# 3. Extraction Candidates
```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "ET-Heller-NARM.md:185-231, five core needs and adaptive survival structures"
      reason: "Defines the core NARM structure used by the concept pages."
      extraction_priority: "high"
    - section_ref: "ET-Heller-NARM.md:289-307, distorted expressions of life force"
      reason: "Grounds anger/protest as a survival-linked expression of unmet needs."
      extraction_priority: "high"
    - section_ref: "ET-Heller-NARM.md:5009-5021, integration of anger and grief"
      reason: "Connects anger integration with access to grief and restored contact."
      extraction_priority: "high"
  reusable_definitions:
    - term: "five core needs"
      source_pointer: "ET-Heller-NARM.md:185-204"
      definition_candidate: "Contact, attunement, trust, autonomy, and love/sexuality are presented as biologically based needs tied to wellbeing and adult capacities."
      confidence: "high"
    - term: "adaptive survival structures"
      source_pointer: "ET-Heller-NARM.md:204-231 and 509-517"
      definition_candidate: "Adaptive survival structures are coping adaptations formed when core needs are chronically unmet."
      confidence: "high"
  reusable_processes:
    - process_name: "anger integration before grief access"
      source_pointer: "ET-Heller-NARM.md:5009-5021"
      process_summary: "The source describes tracking anger in the body, differentiating it from blame, and then gaining access to longing, pain, and grief."
      possible_apex_use: "Use as a source-backed therapeutic reasoning pattern in the compiled KB."
      confidence: "medium"
```

# 4. Concept Candidates
```yaml
concept_candidates:
  - concept_slug: "five-core-needs"
    concept_label: "Five Core Needs"
    source_pointers:
      - "ET-Heller-NARM.md:185-204"
    concept_summary: "NARM names contact, attunement, trust, autonomy, and love/sexuality as core needs with corresponding capacities."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/five-core-needs.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
  - concept_slug: "adaptive-survival-strategies"
    concept_label: "Adaptive Survival Strategies"
    source_pointers:
      - "ET-Heller-NARM.md:204-231"
      - "ET-Heller-NARM.md:509-517"
    concept_summary: "The source links chronically unmet core needs to adaptive survival structures that protect survival and attachment while impairing present contact."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/adaptive-survival-strategies.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
  - concept_slug: "anger-as-protector-of-grief"
    concept_label: "Anger as Protector of Grief"
    source_pointers:
      - "ET-Heller-NARM.md:289-307"
      - "ET-Heller-NARM.md:5009-5021"
    concept_summary: "The source supports a pattern where anger/protest can protect unmet needs and, when integrated, can open access to pain, longing, and grief."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/anger-as-protector-of-grief.md"
    related_existing_pages:
      - "none"
    confidence: "medium"
    review_flags: []
```

# 5. Entity Candidates
```yaml
entity_candidates:
  - entity_slug: "narm"
    entity_label: "NeuroAffective Relational Model"
    entity_type: "framework"
    source_pointers:
      - "ET-Heller-NARM.md:171-185"
    entity_summary: "NARM is the framework organizing the source's claims about developmental trauma, contact, regulation, and survival structures."
    proposed_page_action: "no_page_needed"
    proposed_page_path: "wiki/entities/narm.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
```

# 6. Claim Candidates
```yaml
claim_candidates:
  - claim_id: "C001"
    claim_text: "NARM identifies five core needs: contact, attunement, trust, autonomy, and love/sexuality."
    source_pointer: "ET-Heller-NARM.md:185-204"
    claim_type: "definition"
    applies_to:
      - "five-core-needs"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/five-core-needs.md"
    review_flags: []
  - claim_id: "C002"
    claim_text: "Chronically unmet core needs initiate corresponding adaptive survival structures."
    source_pointer: "ET-Heller-NARM.md:204-231"
    claim_type: "definition"
    applies_to:
      - "adaptive-survival-strategies"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/adaptive-survival-strategies.md"
    review_flags: []
  - claim_id: "C003"
    claim_text: "Anger and protest can be survival-relevant responses to unmet needs, but chronic non-discharged activation can become symptomatic."
    source_pointer: "ET-Heller-NARM.md:289-307"
    claim_type: "fact"
    applies_to:
      - "anger-as-protector-of-grief"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/anger-as-protector-of-grief.md"
    review_flags: []
```

# 7. Contradiction Candidates
```yaml
contradiction_candidates:
  status: "none_detected"
  items: []
```

# 8. Proposed Wiki Page Changes
```yaml
proposed_wiki_page_changes:
  summaries:
    - action: "create"
      path: "wiki/summaries/source-summary-et-heller-narm.md"
      reason: "Preserve a compact source-level summary for future queries."
      source_pointers_required: true
  concepts:
    - action: "create"
      path: "wiki/concepts/five-core-needs.md"
      reason: "Central reusable NARM structure."
      source_pointers_required: true
    - action: "create"
      path: "wiki/concepts/adaptive-survival-strategies.md"
      reason: "Central mechanism linking unmet needs to coping adaptations."
      source_pointers_required: true
    - action: "create"
      path: "wiki/concepts/anger-as-protector-of-grief.md"
      reason: "Source-backed bridge to the personal shadow insight."
      source_pointers_required: true
  entities: []
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "The KB centers on NARM needs/survival structures and anger-grief integration."
```

# 9. Proposed Manifest Updates
```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "et-heller-narm"
    source_path: "apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md"
    source_hash: "64a0dae9c1cbc3bba6bd0299e345a4863560c6bce22b60444755585d0e06e6cd"
    hash_algorithm: "sha256"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/et-heller-narm.analysis.md"
    generated_pages: []
    semantic_tags:
      - "narm"
      - "developmental-trauma"
      - "core-needs"
    concept_candidates:
      - "five-core-needs"
      - "adaptive-survival-strategies"
      - "anger-as-protector-of-grief"
    entity_candidates:
      - "narm"
    review_flags: []
```

# 10. Open Questions
```yaml
open_questions:
  operator_questions:
    - question_id: "Q001"
      question: "Should the test KB copy local raw sources into its own raw/notes folder, or is an explicit source pointer to the manual baseline raw file sufficient?"
      blocks_phase_2: false
      related_source_pointer: "source policy ambiguity"
  kb_questions:
    - question_id: "KQ001"
      question: "Should later KB expansion include entity pages for NARM and named authors?"
      proposed_handling: "leave_as_gap"
      related_pages:
        - "wiki/summaries/source-summary-et-heller-narm.md"
```

# 11. Review Flags
```yaml
review_flags:
  - flag_id: "RF001"
    type: "scope"
    severity: "low"
    summary: "The source is large; this test extracts only the passages needed for a minimal coherent KB."
    required_before_phase_2: false
    proposed_resolution: "Keep the test KB small and record scope limitation."
```

# 12. Operator Review Gate
```yaml
operator_review_gate:
  phase_1_result: "ready_for_operator_review"
  phase_2_recommendation: "approve"
  phase_2_allowed_now: false
  required_operator_phrase: "approve ingest"
  recommended_operator_decision:
    decision: "approve"
    rationale: "The source is present, hashed, and provides the required source-backed framework for the small test KB."
  if_approved_next_actions:
    - "Generate source summary and concept pages with source pointers."
    - "Update LLM summary section of wiki/index.md."
    - "Run deterministic postflight lint."
  if_rejected_next_actions:
    - "Do not generate wiki pages."
    - "Keep this analysis as Phase 1 evidence."
```
