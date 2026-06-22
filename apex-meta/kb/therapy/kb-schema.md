# Therapy KB Schema

```yaml
kb_schema:
  kb_topic_title: "NARM-support reflection knowledgebase"
  kb_source_authority_list:
    - "operator-supplied raw notes under apex-meta/kb/therapy/raw/notes/"
    - "NARM theory source ET-Heller-NARM.md"
    - "operator-authored or AI-assisted reflection handover notes, treated as self-report / working-formulation sources"
  kb_concept_taxonomy_top_level:
    - narm_theory
    - personal_patterns
    - fusion_links
    - session_preparation
    - self_exploration_flows
    - evidence_and_directness_rules
  kb_language_policy: "Preserve source language. Use English for compiled repo-facing process artifacts unless the source formulation is better preserved in German."
  kb_operator_review_policy:
    phase_2_requires_operator_phrase: "approve ingest"
    psychological_claim_labels_required:
      - raw_source
      - source_backed_summary
      - behavioral_inference
      - working_hypothesis
      - operator_question
      - practitioner_question
  boundary:
    reflection_support_only: true
    not_a_medical_record: true
    not_a_diagnosis: true
    not_professional_advice: true
    intended_use: "preparation and reflective organization only"
```
