---
title: "Source Summary: ET Heller NARM"
page_type: summary
kb_slug: "apex-kb-skill-test"
source_refs:
  - source_id: "et-heller-narm"
    source_path: "apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md"
    source_hash: "64a0dae9c1cbc3bba6bd0299e345a4863560c6bce22b60444755585d0e06e6cd"
    source_pointer: "ET-Heller-NARM.md:171-231; 289-307; 5009-5021"
created_at: "2026-06-22T20:25:00Z"
updated_at: "2026-06-22T20:25:00Z"
confidence: "source_backed_summary"
status: "active"
review_flags:
  - "large_source_minimal_extraction"
---

# Source Summary: ET Heller NARM

```yaml
page_metadata:
  page_type: summary
  intended_use: "Fast source-level context retrieval for future AI work."
  source_grounding: "All substantive claims are tied to source_refs or inline source pointers."
```

## Core Summary
This source presents NARM as a model oriented toward contact, aliveness, self-regulation, identity, and present-moment capacity rather than only past explanation. It identifies [[five-core-needs]] and links chronically unmet needs to [[adaptive-survival-strategies]]. It also frames anger/protest as a survival-relevant response to unmet needs and describes a therapeutic process where integrated anger can open access to longing, pain, grief, contact, and individuation. Source pointers: `ET-Heller-NARM.md:171-231`, `ET-Heller-NARM.md:289-307`, `ET-Heller-NARM.md:5009-5021`.

## What This Source Adds to the KB
```yaml
adds:
  - "NARM's five core needs and corresponding capacities."
  - "The adaptive survival structure model."
  - "A source-backed bridge between anger, unmet needs, grief, and restored contact."
clarifies:
  - "Anger can be life-force/protest energy, not only a problem behavior."
limits:
  - "This test summary extracts only selected passages from a large source."
```

## Key Claims
```yaml
key_claims:
  - claim_id: "C001"
    claim: "Contact, attunement, trust, autonomy, and love/sexuality are NARM's five core needs."
    source_pointer: "ET-Heller-NARM.md:185-204"
    confidence: "high"
    used_in_pages:
      - "wiki/concepts/five-core-needs.md"
  - claim_id: "C002"
    claim: "Chronically unmet core needs lead to corresponding adaptive survival structures."
    source_pointer: "ET-Heller-NARM.md:204-231"
    confidence: "high"
    used_in_pages:
      - "wiki/concepts/adaptive-survival-strategies.md"
  - claim_id: "C003"
    claim: "Integrated anger can support contact with grief, longing, and healthy boundaries."
    source_pointer: "ET-Heller-NARM.md:5009-5021"
    confidence: "medium"
    used_in_pages:
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
    source_pointer: "ET-Heller-NARM.md:289-307; 5009-5021"
```

## Extracted Entities
```yaml
extracted_entities:
  - entity_slug: "narm"
    entity_label: "NeuroAffective Relational Model"
    entity_type: "framework"
    page_path: "none"
    source_pointer: "ET-Heller-NARM.md:171-185"
```

## Contradictions and Tensions
```yaml
contradictions:
  status: "none_detected"
  items: []
```

## Open Questions
```yaml
open_questions:
  - question_id: "Q001"
    question: "Should later expansion create separate pages for each survival structure?"
    proposed_handling: "ingest_more_sources"
    source_pointer: "ET-Heller-NARM.md:204-231"
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
    - "[[source-summary-shadow-insight-v1]]"
    - "[[first-fusion-notes]]"
```
