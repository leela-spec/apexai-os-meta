# KB Schema - Apex Plan Sync Session Workflow V2

```yaml
kb_schema:
  kb_slug: "apex-plan-sync-session-workflow-v2"
  kb_topic_title: "Apex Plan Sync Session Workflow V2"
  kb_source_authority_list:
    - authority_level: primary
      description: "Original source material, project-controlled contracts, direct operator-provided evidence."
    - authority_level: secondary
      description: "Interpretive summaries, implementation reports, validated external references."
    - authority_level: tertiary
      description: "Background material used only for orientation."
  kb_concept_taxonomy_top_level:
    - concepts
    - entities
    - summaries
    - contradictions
    - open_questions
  kb_language_policy:
    primary_language: english
    preserve_source_language_when_relevant: true
  kb_operator_review_policy:
    ingest_phase_2_requires_phrase: "approve ingest"
    same_prompt_approval_allowed: false
    contradiction_handling: "expose, do not silently resolve"
```
