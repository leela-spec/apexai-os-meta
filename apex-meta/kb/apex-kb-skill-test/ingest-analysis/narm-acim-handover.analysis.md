```yaml
ingest_analysis:
  analysis_id: "apex-kb-skill-test-narm-acim-handover-analysis"
  kb_slug: "apex-kb-skill-test"
  source_slug: "narm-acim-handover"
  source_ref:
    source_path: "apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md"
    source_type: "note"
    source_hash: "b2f3b75d5aab80d95c88b3b245478b15d9510637d41e63571f5619ccebf9a8b5"
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
  title: "Psychological Handover: Working Formulation, Patterns, and Intervention Priorities"
  author_or_origin: "operator supplied therapeutic handover note"
  publication_or_creation_date: "unknown"
  source_authority_level: "secondary"
  source_authority_rationale: "The source is a structured synthesis based on self-report and explicitly says it is not a formal diagnosis."
  source_scope: "Working formulation for anger, betrayal/exclusion sensitivity, grief, boundaries, shadow integration, nervous-system regulation, and ACIM/Buddhist non-bypass framing."
  source_limitations:
    - "The source warns that it is not a formal diagnosis."
    - "It contains hypotheses and intervention priorities rather than verified external facts."
```

# 2. Source Summary
```yaml
source_summary:
  one_sentence_core: "The handover frames the main work as transforming betrayal/exclusion/recognition activation into calibrated discernment, mature boundaries, clean communication, self-compassion, and spiritually non-attached action."
  compact_summary: "The source names recurrent anger, mistrust, vigilance, and relational ambiguity as primary difficulties. It organizes anger as a surface layer over grief, hurt, vulnerability, and fear of exclusion, while also preserving the values protected by anger. It warns against suppressing anger and recommends using it as a doorway into grief, boundary intelligence, and calibration. It also describes spiritual non-bypass as clear seeing without attack, boundary without hatred, and forgiveness without naivete."
  relevant_to_kb_because:
    - "Provides the fusion layer connecting NARM, personal shadow insight, and practical relational/spiritual protocols."
  likely_not_relevant_for:
    - "Does not establish medical diagnosis or general population claims."
```

# 3. Extraction Candidates
```yaml
extraction_candidates:
  high_value_sections:
    - section_ref: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:0 Status / Caution"
      reason: "Defines authority limits."
      extraction_priority: "high"
    - section_ref: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:3 Important Breakthrough Insight"
      reason: "Restates anger covers grief and intervention implications."
      extraction_priority: "high"
    - section_ref: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:9 Spiritual / ACIM / Buddhist Formulation"
      reason: "Defines the non-bypass boundary/forgiveness frame."
      extraction_priority: "medium"
    - section_ref: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:18 Most Important Summary"
      reason: "Provides concise fusion summary."
      extraction_priority: "high"
  reusable_definitions:
    - term: "boundary without hatred"
      source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:9 Spiritual / ACIM / Buddhist Formulation"
      definition_candidate: "A mature spiritual application where facts, boundaries, trust adjustment, and clear communication remain available without making grievance into identity."
      confidence: "medium"
  reusable_processes:
    - process_name: "validate signal, regulate charge, test story, choose boundary, integrate grief"
      source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:18 Most Important Summary"
      process_summary: "The source proposes preserving perception while reducing trauma-charge and choosing proportionate action."
      possible_apex_use: "Use in fusion notes as a compact protocol."
      confidence: "medium"
```

# 4. Concept Candidates
```yaml
concept_candidates:
  - concept_slug: "anger-as-protector-of-grief"
    concept_label: "Anger as Protector of Grief"
    source_pointers:
      - "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:3 Important Breakthrough Insight"
    concept_summary: "The source confirms the anger/grief insight as intervention priority and warns against suppressing anger."
    proposed_page_action: "update"
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
    claim_text: "The handover is a working formulation, not a formal diagnosis."
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:0 Status / Caution"
    claim_type: "warning"
    applies_to:
      - "first-fusion-notes"
    confidence: "high"
    proposed_destination:
      page_type: "summary"
      page_path: "wiki/summaries/first-fusion-notes.md"
    review_flags: []
  - claim_id: "C002"
    claim_text: "Anger should not simply be suppressed; it can be used as a doorway into grief and defended vulnerability."
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:3 Important Breakthrough Insight"
    claim_type: "recommendation"
    applies_to:
      - "anger-as-protector-of-grief"
    confidence: "high"
    proposed_destination:
      page_type: "concept"
      page_path: "wiki/concepts/anger-as-protector-of-grief.md"
    review_flags: []
  - claim_id: "C003"
    claim_text: "Mature spiritual application keeps human-level boundaries while refusing grievance as identity."
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:9 Spiritual / ACIM / Buddhist Formulation"
    claim_type: "recommendation"
    applies_to:
      - "first-fusion-notes"
    confidence: "medium"
    proposed_destination:
      page_type: "summary"
      page_path: "wiki/summaries/first-fusion-notes.md"
    review_flags: []
```

# 7. Contradiction Candidates
```yaml
contradiction_candidates:
  status: "possible"
  items:
    - contradiction_id: "X001"
      severity: "medium"
      source_claim: "Do not suppress anger; use it as a doorway."
      conflicting_existing_claim: "Spiritual aspiration wants forgiveness and non-attack, which could be misapplied as bypassing."
      current_source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:3 and 9"
      existing_source_pointer: "same source"
      interpretation: "This is a productive tension, not a contradiction: anger must be integrated without becoming attack."
      proposed_handling: "add_contradiction_callout"
      review_required: true
```

# 8. Proposed Wiki Page Changes
```yaml
proposed_wiki_page_changes:
  summaries:
    - action: "create"
      path: "wiki/summaries/first-fusion-notes.md"
      reason: "Needed to record how the NARM and personal insight sources are fused without overwriting source boundaries."
      source_pointers_required: true
  concepts:
    - action: "update"
      path: "wiki/concepts/anger-as-protector-of-grief.md"
      reason: "Adds caution, boundary, and spiritual non-bypass framing."
      source_pointers_required: true
  entities: []
  index:
    semantic_summary_update_needed: true
    proposed_index_notes:
      - "The KB should mark fusion notes as mixed confidence and not as formal diagnosis."
```

# 9. Proposed Manifest Updates
```yaml
proposed_manifest_updates:
  source_entry:
    source_id: "narm-acim-handover"
    source_path: "apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md"
    source_hash: "b2f3b75d5aab80d95c88b3b245478b15d9510637d41e63571f5619ccebf9a8b5"
    hash_algorithm: "sha256"
    ingest_status: "phase_1_complete_operator_review_needed"
    ingest_analysis_path: "ingest-analysis/narm-acim-handover.analysis.md"
    generated_pages: []
    semantic_tags:
      - "working-formulation"
      - "boundaries"
      - "spiritual-non-bypass"
    concept_candidates:
      - "anger-as-protector-of-grief"
    entity_candidates: []
    review_flags:
      - "not_formal_diagnosis"
```

# 10. Open Questions
```yaml
open_questions:
  operator_questions: []
  kb_questions:
    - question_id: "KQ001"
      question: "Which future sources should validate or revise the handover's hypotheses?"
      proposed_handling: "ingest_more_sources"
      related_pages:
        - "wiki/summaries/first-fusion-notes.md"
```

# 11. Review Flags
```yaml
review_flags:
  - flag_id: "RF001"
    type: "source_authority"
    severity: "medium"
    summary: "The source is a working therapeutic formulation and explicitly not a diagnosis."
    required_before_phase_2: false
    proposed_resolution: "Keep confidence mixed and status needs_review where claims synthesize multiple frameworks."
```

# 12. Operator Review Gate
```yaml
operator_review_gate:
  phase_1_result: "ready_for_operator_review"
  phase_2_recommendation: "approve_with_changes"
  phase_2_allowed_now: false
  required_operator_phrase: "approve ingest"
  recommended_operator_decision:
    decision: "approve_with_changes"
    rationale: "Use only a small fusion summary and avoid treating hypotheses as diagnosis."
  if_approved_next_actions:
    - "Generate first fusion notes with caution markers."
    - "Update anger/grief concept with boundary and non-bypass framing."
  if_rejected_next_actions:
    - "Do not generate fusion pages from this source."
```
