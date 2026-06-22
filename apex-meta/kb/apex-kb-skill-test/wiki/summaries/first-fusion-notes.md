---
title: "First Fusion Notes"
page_type: summary
kb_slug: "apex-kb-skill-test"
source_refs:
  - source_id: "et-heller-narm"
    source_path: "apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md"
    source_hash: "64a0dae9c1cbc3bba6bd0299e345a4863560c6bce22b60444755585d0e06e6cd"
    source_pointer: "ET-Heller-NARM.md:185-231; 5009-5021"
  - source_id: "shadow-insight-v1"
    source_path: "apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md"
    source_hash: "06d39530b31392f17873171f2781c4b50fa3e2efbd622aab9bb0c500c072acc7"
    source_pointer: "shadow_insight_v1.md:Core Insight; Practice Rule"
  - source_id: "narm-acim-handover"
    source_path: "apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md"
    source_hash: "b2f3b75d5aab80d95c88b3b245478b15d9510637d41e63571f5619ccebf9a8b5"
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:0; 3; 9; 18"
created_at: "2026-06-22T20:25:00Z"
updated_at: "2026-06-22T20:25:00Z"
confidence: "mixed"
status: "needs_review"
review_flags:
  - "working_hypothesis"
  - "not_formal_diagnosis"
---

# First Fusion Notes

```yaml
page_metadata:
  page_type: summary
  intended_use: "Small synthesis page connecting the three test sources without erasing source boundaries."
  source_grounding: "Synthesis statements are marked as mixed confidence and are tied to source pointers."
```

## Core Summary
The smallest coherent fusion is: [[five-core-needs]] and [[adaptive-survival-strategies]] provide the structural NARM frame; [[anger-as-protector-of-grief]] provides the applied bridge between unmet needs, protective anger, grief, self-compassion, and boundaries. The handover source explicitly says it is a working formulation rather than a diagnosis, so this fusion should remain a working hypothesis. Source pointers: `ET-Heller-NARM.md:185-231`, `ET-Heller-NARM.md:5009-5021`, `shadow_insight_v1.md:Core Insight`, `PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:0; 18`.

## What This Source Adds to the KB
```yaml
adds:
  - "A minimal cross-source map for comparing the skill-test KB against the manual therapy KB."
  - "A caution that spiritual forgiveness must not become boundary bypass."
clarifies:
  - "Anger can be both protective signal and risk for blame/prosecution."
limits:
  - "This page is synthesis, not a new raw source or diagnosis."
```

## Key Claims
```yaml
key_claims:
  - claim_id: "C001"
    claim: "The handover source is a working formulation, not a formal diagnosis."
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:0 Status / Caution"
    confidence: "high"
    used_in_pages:
      - "wiki/summaries/first-fusion-notes.md"
  - claim_id: "C002"
    claim: "A useful stance is to validate the signal, regulate the charge, test the story, choose the proportionate boundary, and integrate hidden grief."
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:18 Most Important Summary"
    confidence: "medium"
    used_in_pages:
      - "wiki/summaries/first-fusion-notes.md"
      - "wiki/concepts/anger-as-protector-of-grief.md"
```

## Extracted Concepts
```yaml
extracted_concepts:
  - concept_slug: "five-core-needs"
    concept_label: "Five Core Needs"
    page_path: "wiki/concepts/five-core-needs.md"
    source_pointer: "ET-Heller-NARM.md:185-204"
  - concept_slug: "adaptive-survival-strategies"
    concept_label: "Adaptive Survival Strategies"
    page_path: "wiki/concepts/adaptive-survival-strategies.md"
    source_pointer: "ET-Heller-NARM.md:204-231"
  - concept_slug: "anger-as-protector-of-grief"
    concept_label: "Anger as Protector of Grief"
    page_path: "wiki/concepts/anger-as-protector-of-grief.md"
    source_pointer: "shadow_insight_v1.md:Core Insight; ET-Heller-NARM.md:5009-5021"
```

## Extracted Entities
```yaml
extracted_entities: []
```

## Contradictions and Tensions
```yaml
contradictions:
  status: "possible"
  items:
    - contradiction_id: "X001"
      severity: "medium"
      summary: "The fusion must preserve both boundary clarity and non-attack; suppressing either side would distort the source set."
      source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:9 Spiritual / ACIM / Buddhist Formulation"
      related_page: "wiki/concepts/anger-as-protector-of-grief.md"
      handling: "callout_added"
```

## Open Questions
```yaml
open_questions:
  - question_id: "Q001"
    question: "Which future sources should determine whether this fusion becomes an active protocol or remains a working hypothesis?"
    proposed_handling: "ingest_more_sources"
    source_pointer: "PsychologicalHandover_ChatTherapeuticFramework_inACIM.md:14 Possible Clinical Hypotheses"
```

## Backlinks
```yaml
backlinks:
  concepts:
    - "[[five-core-needs]]"
    - "[[adaptive-survival-strategies]]"
    - "[[anger-as-protector-of-grief]]"
  entities: []
  related_summaries:
    - "[[source-summary-et-heller-narm]]"
    - "[[source-summary-shadow-insight-v1]]"
```
