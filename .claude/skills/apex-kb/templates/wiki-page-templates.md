# Apex KB Wiki Page Templates

## Phase 2 adaptive page value rules


- Use the exact required headings: Target Questions Answered, Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, and Uncertainty / Raw Source Reopen Triggers.
- Declare only target-query IDs this page directly answers. A broad page must answer the material sub-questions, not merely state boundaries.
- Include only sources actually reviewed and materially used. Preserve unopened candidates in the topic ledger, never in page evidence.
- Scale sources and depth to answer requirements. `compiled_minimal` minimizes topology, not content.
- Do not duplicate frontmatter claims/source lists in prose or add numeric page-value scores.
- Create concept/entity pages only for independent project-specific retrieval value; otherwise preserve an embed/reject disposition.
- Run clean-context page-only and claim-entailment acceptance before `compiled_unvalidated`.
## Shared frontmatter


```yaml
required_fields:
  title: "<page title>"
  page_type: "summary | concept | entity | index | query_output | audit_item"
  kb_slug: "<kb-slug>"
  semantic_contract_version: "2"
  semantic_run_id: "<run-id>"
  target_query_ids: []
  source_refs:
    - source_id: "<source-id>"
      source_path: "<raw/source/path/or/pointer>"
      source_hash: "<sha256-or-NA>"
      source_pointer: "<heading/page/line/passage reference>"
      source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
      claims: []                    # claim IDs (C001...) from this source's Phase 1 record,
                                     # carried forward for claim-level provenance. Additive only.
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
  updated_at: "YYYY-MM-DDTHH:MM:SSZ"
  confidence: "high | medium | low | mixed | unknown"
  claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
  status: "draft | active | needs_review | deprecated | superseded"
```

`related_concepts` (summary, concept, entity pages) and `related_entities` (summary, concept
pages) are not in `required_fields` above, but every page type that declares them must populate
them from the matching Phase 1 topic file's Concept/Entity Candidate Shortlist - copy
`concept_slug`/`entity_slug` values directly, do not leave them `[]` when a shortlist exists and
do not re-infer relations the Phase 1 file already resolved.
## Summary page

```markdown
---
title: "<Source or Topic Summary>"
page_type: summary
kb_slug: "<kb-slug>"
summary_slug: "<summary-slug>"
semantic_contract_version: "2"
semantic_run_id: "<run-id>"
target_query_ids: []
source_refs:
  - source_id: "<source-id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
    claims: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts: []
related_entities: []
review_flags: []
---

# <Source or Topic Summary>

## Core Summary

<Direct source-grounded synthesis that answers the declared target questions.>

## Target Questions Answered

```yaml
target_questions_answered:
  - query_id: "<stable query id>"
    direct_answer: "<answer sufficient for compiled-first retrieval>"
    answer_section: "<this page heading or related page>"
```

## What This Adds

```yaml
adds: []
clarifies: []
limits: []
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Include only sources actually reviewed and materially used.
  - source_id: "<source-id>"
    source_path: "<path>"
    phase0_rank: 1 | NA
    analysis_ref: "ingest-analysis/<topic-slug>.analysis.md"
    reviewed_status: "complete | targeted"
    supported_query_ids: []
    claim_ids: []
    rationale: "<authority and relevance>"
    coverage: "<material contribution>"
```

## Macro / Meso / Micro

Each layer is a distinct scale, not a restatement. Target 3-5 sentences per layer (a 20-word
floor per layer is enforced on v2 pages) - enough to be a complete standalone thought at that
scale, never padded. Fold a one-line execution-flow chain into Micro instead of giving it a
separate heading (a new heading is a new retrieval chunk; the chain does not earn one).

```markdown
### Macro

<Why - the architectural context this page's subject lives in, the problem it solves, and the
design decision/value gained. 3-5 sentences.>

### Meso

<What it is - the feature/service/screen/model itself: its components, internal structure,
data shape, and connections to peer concepts. 3-5 sentences.>

### Micro

<How - the concrete execution path: trigger, ordered steps, outcome, key error paths or
preconditions. Include one inline flow chain, e.g. `TriggerEvent -> StepA -> StepB -> Outcome`.
3-6 sentences.>
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<pointer>"
    confidence: "high | medium | low"
    state: "present | proposed | open"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Connection Map

Optional. Include this section only when the topic has 3 or more directional edges to peer
summary pages - below that, fold the one or two edges into `Routes Here` instead and omit this
heading entirely (an unused heading still costs a retrieval chunk). This section is not part of
the six required Phase 2 value headings and is never required by the quality checker.

```yaml
edges:
  - direction: "inbound | outbound"
    peer: "<peer-topic-slug>"
    what_flows: "<data | event | control, <= 8 words>"
    contract: "<interface description, <= 15 words>"
```

## Routes Here

```yaml
routes:
  # Describe how a user or question might arrive at this page and where it may lead next.
  - question: "<example question that leads here>"
    leads_to: "<target page path>"
    rationale: "<why this route exists>"
  - related_page: "<kb-slug>/concepts/<concept>.md"
    relation: "<relation description>"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  # Consolidate contradictions, open questions, and reasons to revisit the raw source.
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<pointer>"
    proposed_handling: "<audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator>"
```
```

## Concept page

```markdown
---
title: "<Concept Label>"
page_type: concept
kb_slug: "<kb-slug>"
concept_slug: "<concept-slug>"
semantic_contract_version: "2"
semantic_run_id: "<run-id>"
target_query_ids: []
source_refs:
  - source_id: "<source-id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
    claims: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts: []
related_entities: []
review_flags: []
---

# <Concept Label>

## Definition

<Project-specific definition and operating consequences grounded in exact source pointers.>

## Target Questions Answered

```yaml
target_questions_answered:
  - query_id: "<stable query id>"
    direct_answer: "<answer sufficient for compiled-first retrieval>"
    answer_section: "<this page heading or related page>"
```

## Operating Rules

```yaml
rules: []
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Include only sources actually reviewed and materially used.
  - source_id: "<source-id>"
    source_path: "<path>"
    phase0_rank: 1 | NA
    analysis_ref: "ingest-analysis/<topic-slug>.analysis.md"
    reviewed_status: "complete | targeted"
    supported_query_ids: []
    claim_ids: []
    rationale: "<authority and relevance>"
    coverage: "<material contribution>"
```

## Macro / Meso / Micro

Same three scales as a summary page, scoped to this concept. Target 3-5 sentences per layer
(20-word floor per layer on v2 pages).

```markdown
### Macro

<Why - the architectural reason this concept exists and what problem it addresses. 3-5 sentences.>

### Meso

<What it is - the concept's structure, boundaries, and how it relates to peer concepts/entities.
3-5 sentences.>

### Micro

<How - the concrete rule or mechanism, anchored to source pointers. Include an inline chain if
the concept has an execution order. 3-6 sentences.>
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<pointer>"
    confidence: "high | medium | low"
    state: "present | proposed | open"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "<example question that leads here>"
    leads_to: "<target page path>"
    rationale: "<why this route exists>"
  - related_page: "<kb-slug>/entities/<entity>.md"
    relation: "<relation description>"
```

## Evidence

```yaml
evidence:
  - source_id: "<source-id>"
    source_pointer: "<pointer>"
    supports: "<claim or section>"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<pointer>"
    proposed_handling: "<audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator>"
```
```

## Entity page

```markdown
---
title: "<Entity Label>"
page_type: entity
kb_slug: "<kb-slug>"
entity_slug: "<entity-slug>"
semantic_contract_version: "2"
semantic_run_id: "<run-id>"
target_query_ids: []
entity_type: "person | organization | tool | project | artifact | source | other"
source_refs:
  - source_id: "<source-id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
    claims: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts: []
review_flags: []
---

# <Entity Label>

## Identity

```yaml
entity:
  label: "<Entity Label>"
  type: "<entity_type>"
  aliases: []
```

## Source-Grounded Summary

<Project-specific identity, fields, rules, lifecycle, and relationships grounded in exact source pointers.>

## Target Questions Answered

```yaml
target_questions_answered:
  - query_id: "<stable query id>"
    direct_answer: "<answer sufficient for compiled-first retrieval>"
    answer_section: "<this page heading or related page>"
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  # Include only sources actually reviewed and materially used.
  - source_id: "<source-id>"
    source_path: "<path>"
    phase0_rank: 1 | NA
    analysis_ref: "ingest-analysis/<topic-slug>.analysis.md"
    reviewed_status: "complete | targeted"
    supported_query_ids: []
    claim_ids: []
    rationale: "<authority and relevance>"
    coverage: "<material contribution>"
```

## Macro / Meso / Micro

Same three scales as a summary page, scoped to this entity. Narrow named entities may stay
concise (kb-contract.md concise_policy) but each layer must still be a real sentence, not a
placeholder - target 3-5 sentences per layer (20-word floor per layer on v2 pages).

```markdown
### Macro

<Why - the architectural reason this entity exists in the system. 3-5 sentences.>

### Meso

<What it is - the entity's structure, fields, or states, and its relationships to peer
concepts/entities. 3-5 sentences.>

### Micro

<How - its concrete lifecycle or behavior, anchored to source pointers. 3-6 sentences.>
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<pointer>"
    confidence: "high | medium | low"
    state: "present | proposed | open"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "<example question that leads here>"
    leads_to: "<target page path>"
    rationale: "<why this route exists>"
  - related_page: "<kb-slug>/summaries/<summary>.md"
    relation: "<relation description>"
```

## Evidence

```yaml
evidence: []
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "<contradiction, open question, or uncertainty>"
    source_pointer: "<pointer>"
    proposed_handling: "<audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator>"
```
```
