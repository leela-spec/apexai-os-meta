# KB Schema - <kb-topic-title>

```yaml
kb_schema:
  kb_slug: "<kb-slug>"
  kb_topic_title: "<kb-topic-title>"
  kb_source_authority_list:
    - authority_level: primary
      description: "Original source material, project-owned contracts, direct operator evidence."
    - authority_level: secondary
      description: "Validated implementation reports and curated interpretive material."
    - authority_level: tertiary
      description: "Background material used for orientation only."
  kb_concept_taxonomy_top_level:
    - source_custody
    - lifecycle
    - concepts
    - entities
    - summaries
    - contradictions
    - open_questions
  kb_language_policy:
    primary_language: english
    preserve_source_language_when_relevant: true
    translation_requires_label: true
  kb_operator_review_policy:
    ingest_phase_2_requires_phrase: "approve ingest"
    same_prompt_approval_allowed_normal_mode: false
    contradiction_handling: "expose, do not silently resolve"
    uncertain_authority_handling: "mark unclear and ask operator"
```
