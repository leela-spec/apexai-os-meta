```yaml
ingest_analysis:
  analysis_id: "apex-kb-skill-test-shadow-insight-v1-analysis"
  kb_slug: "apex-kb-skill-test"
  source_slug: "shadow-insight-v1"
  source_ref:
    source_path: "apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md"
    source_type: "note"
    source_hash: "06d39530b31392f17873171f2781c4b50fa3e2efbd622aab9bb0c500c072acc7"
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
  title: "shadow_insight_v1"
  author_or_origin: "operator supplied introspective note"
  publication_or_creation_date: "unknown"
  source_authority_level: "primary"
  source_authority_rationale: "The note directly records the operator's self-reported breakthrough insight."
  source_scope: "Anger, grief, self-compassion, Jungian shadow framing, and a practice rule."
  source_limitations:
    - "Self-report; not a clinical diagnosis."
```

# 2. Source Summary
```yaml
source_summary:
  one_sentence_core: "The source states that anger, frustration, and irritation often cover grief, and that grief can open access to self-compassion."
  compact_summary: "The note frames anger as a protective surface state that blocks vulnerable grief, sadness, and self-compassion. It says the ego may prefer anger because anger feels active, powerful, justified, and controllable. In Jungian terms, vulnerable grief and neediness are shadow content, while anger and control operate as persona defense. The practice rule asks what grief, pain, or need for compassion is underneath anger."
  relevant_to_kb_because:
    - "Provides the personal source that fuses with NARM anger/grief passages."
  likely_not_relevant_for:
    - "Does not establish general clinical truth beyond the operator's self-observation."
```

# 3. Extraction Candidates
```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "shadow_insight_v1.md:Core Insight"
      reason: "Central source-backed claim."
      extraction_priority: "high"
    - section_ref: "shadow_insight_v1.md:Practice Rule"
      reason: "Provides operational questions for applied use."
      extraction_priority: "high"
  reusable_definitions:
    - term: "anger as protector"
      source_pointer: "shadow_insight_v1.md:Mechanism"
      definition_candidate: "Anger protects against vulnerable grief and pain."
      confidence: "high"
  reusable_processes:
    - process_name: "anger-to-grief inquiry"
      source_pointer: "shadow_insight_v1.md:Practice Rule"
      process_summary: "When anger appears, ask what grief, compassion need, or protected pain is underneath, and stay with sadness briefly without converting it into blame."
      possible_apex_use: "Use as an applied practice in the anger/grief concept page."
      confidence: "high"
```

# 4. Concept Candidates
```yaml
concept_candidates:
  - concept_slug: "anger-as-protector-of-grief"
    concept_label: "Anger as Protector of Grief"
    source_pointers:
      - "shadow_insight_v1.md:Core Insight"
      - "shadow_insight_v1.md:Practice Rule"
    concept_summary: "The source presents anger as a protective wall that can become a doorway into grief and self-compassion."
    proposed_page_action: "create"
    proposed_page_path: "wiki/concepts/anger-as-protector-of-grief.md"
    related_existing_pages:
      - "none"
    confidence: "high"
    review_flags: []
```

# 5. Entity Candidates
```yaml
entity_candidates: []
```

# 6. Claim Candidates
```yaml
claim_candidates:
  - claim_id: "C001"
    claim_text: "Anger, frustration, and irritation often cover grief."
    source_pointer: "shadow_insight_v1.md:Core Insight"
    claim_type: "fact"
    applies_to:
      - "anger-as-protector-of-grief"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/anger-as-protector-of-grief.md"
    review_flags: []
  - claim_id: "C002"
    claim_text: "When grief is allowed, self-compassion becomes accessible."
    source_pointer: "shadow_insight_v1.md:Psychological Interpretation"
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
      path: "wiki/summaries/source-summary-shadow-insight-v1.md"
      reason: "Preserve the personal insight separately from the general NARM source."
      source_pointers_required: true
  concepts:
    - action: "update"
      path: "wiki/concepts/anger-as-protector-of-grief.md"
      reason: "Adds personal practice logic to the source-backed NARM anger/grief concept."
      source_pointers_required: true
  entities: []
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "The personal note is the main source for anger-to-grief inquiry."
```

# 9. Proposed Manifest Updates
```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "shadow-insight-v1"
    source_path: "apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md"
    source_hash: "06d39530b31392f17873171f2781c4b50fa3e2efbd622aab9bb0c500c072acc7"
    hash_algorithm: "sha256"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/shadow-insight-v1.analysis.md"
    generated_pages: []
    semantic_tags:
      - "anger"
      - "grief"
      - "shadow-integration"
    concept_candidates:
      - "anger-as-protector-of-grief"
    entity_candidates: []
    review_flags: []
```

# 10. Open Questions
```yaml
open_questions:
  operator_questions: []
  kb_questions:
    - question_id: "KQ001"
      question: "How should future KB pages distinguish personal introspection from generalized therapeutic claims?"
      proposed_handling: "leave_as_gap"
      related_pages:
        - "wiki/concepts/anger-as-protector-of-grief.md"
```

# 11. Review Flags
```yaml
review_flags:
  - flag_id: "RF001"
    type: "source_authority"
    severity: "medium"
    summary: "This is primary self-report for the operator, not external clinical authority."
    required_before_phase_2: false
    proposed_resolution: "Label personal claims as self-report or working hypothesis when generalized."
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
    rationale: "The source is short, present, hashed, and directly supports one minimal concept and summary page."
  if_approved_next_actions:
    - "Generate source summary."
    - "Update anger/grief concept with explicit self-report pointers."
  if_rejected_next_actions:
    - "Do not generate wiki pages from this source."
```
