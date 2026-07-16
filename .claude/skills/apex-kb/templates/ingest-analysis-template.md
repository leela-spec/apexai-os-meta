---
analysis_id: "<kb-slug>-<topic-slug>-analysis"
kb_slug: "<kb-slug>"
topic_slug: "<topic-slug>"
source_count: <accepted-source-count>
created_at: "YYYY-MM-DDTHH:MM:SSZ"
created_by: "apex-kb"
phase: ingest_phase_1
status: analysis_complete
semantic_compile_policy:
  phase_2_continues_when_output_tier_includes_wiki: true
  stop_before_wiki_only_for: "analysis_only | operator_explicit_stop_before_wiki"
  next_stage_owner: "manifests/run-state.json"
  handoff_owner: "log/runs/<run-id>/packets/phase2-<topic-slug>.json"
---

# Phase 1 Analysis - <topic title>

One Phase 1 file exists per registry topic, matching `wiki/summaries/<topic-slug>.md`
one-to-one. It carries every source accepted for the topic, not one file per source.
This file has exactly one reader class: the Phase 2 synthesis LLM (plus the operator during
review) - no deterministic tool parses these YAML/table bodies, so structure for LLM synthesis
and provenance fidelity, not for a machine parser. Read each raw source before writing its
record; do not infer content from a filename or prior summary.

## 1. Source Inventory

List every source considered for this topic, ranked by authority/relevance. Rejected or
held-back sources get exactly this one row and nothing else below - no per-source record, no
tokens spent past this table.

| rank | source_id | source_path | authority | recency | disposition | hash_prefix |
|------|-----------|--------------|-----------|---------|-------------|-------------|
| 1 | `<source-id>` | `<raw/source/path>` | primary \| secondary \| tertiary \| unclear | `<YYYY-Qn or unknown>` | accepted | `<sha256 prefix>` |
| 2 | `<source-id>` | `<raw/source/path>` | ... | ... | rejected: `<reason>` | - |

## 2. Per-Source Records (accepted sources only)

Repeat this block once per accepted source. Keep `concept_slug:` / `entity_slug:` /
`disposition:` on their own lines exactly as shown - deterministic lint greps these keys.

### `<source_id>` - authority: `<primary|secondary|tertiary|unclear>`

```yaml
source_identity:
  title: "<explicit title or filename>"
  author_or_origin: "<known or unknown>"
  publication_or_creation_date: "YYYY-MM-DD | YYYY-MM | YYYY | unknown"
  authority_rationale: "<source-grounded rationale>"
  scope: "<what the source covers>"
  limitations: []
  read_status: "complete | targeted | blocked"
  reviewed_passages: []

target_query_coverage:
  - query_id: "<stable query id>"
    outcome: "answered | partial | contradicted | blocked | not_covered"
    answer_or_finding: "<source-grounded result>"
    source_pointers: []
    additional_evidence_required: []
topic_completion_effect: "supports | partial | blocks"

source_summary:
  one_sentence_core: "<central contribution>"
  relevant_to_kb_because: []
  likely_not_relevant_for: []

extraction_candidates:
  high_value_sections:
    - section_ref: "<heading/page/line/passage>"
      reason: "<why it matters>"
      extraction_priority: "high | medium | low"
  reusable_definitions: []
  reusable_processes: []

key_claims:
  - claim_id: C001
    claim: "<specific claim>"
    source_pointer: "<heading/page/line/passage>"
    target_query_ids: []
    confidence: "high | medium | low"
    state: "present | proposed | open"
    claim_label: "source_backed_summary"

concept_candidates:
  - concept_slug: "<kebab-case>"
    concept_label: "<label>"
    source_pointer: "<exact pointer>"
    summary: "<source-grounded candidate>"
    confidence: "high | medium | low"
    disposition: promote
    disposition_rationale: "<retrieval-value rationale>"
    target_query_ids: []
    destination_page: "<wiki path or NA>"

entity_candidates:
  - entity_slug: "<kebab-case>"
    entity_label: "<label>"
    entity_type: "person | organization | tool | project | artifact | other"
    source_pointer: "<exact pointer>"
    summary: "<source-grounded candidate>"
    confidence: "high | medium | low"
    disposition: promote
    disposition_rationale: "<retrieval-value rationale>"
    target_query_ids: []
    destination_page: "<wiki path or NA>"

uncertainty_triggers:
  - id: U001
    description: "<conflict, gap, or uncertainty>"
    source_pointer: "<pointer>"
    availability_class: "evidence_unavailable | evidence_conflict | future_change | readable_unopened"
    completion_effect: "none | supporting_gap | blocks_priority_query"
    affected_query_ids: []
    severity: "blocking | notable | minor"
    proposed_handling: "audit_item | planning_task_candidate | revisit_source | leave_as_gap | ask_operator"
```

The `disposition:` line must read exactly `promote`, `embed_in_summary`, `defer_blocked`, or
`reject_no_independent_value` with nothing appended - deterministic lint matches the full line.
The `state:` field on each claim answers the operator's present-vs-proposed-vs-open question and
carries forward unchanged into the Phase 2 Key Claims table - never re-derive it there.

## 3. Cross-Source Synthesis Notes

200-400 words, written for the Phase 2 LLM, placed last so it lands at the end of this file's
context (the position an LLM reader weighs most before drafting). Explicitly name: conflicts
between sources, which claim wins by authority, which claims survived reconciliation and which
were discarded and why, and outstanding topic-completion blockers. Reference claim IDs
(`C001`, `C002`, ...) and `source_id`s inline rather than restating full claims.

## 4. Concept Candidate Shortlist

Deduplicated across every accepted source in this topic. The Phase 2 LLM copies `concept_slug`
values directly into the wiki page's `related_concepts` frontmatter - no re-inference needed.

| concept_slug | concept_label | source_ids | disposition |
|---|---|---|---|
| `<slug>` | `<label>` | `<source-id>, <source-id>` | promote \| embed_in_summary \| defer_blocked \| reject_no_independent_value |

## 5. Entity Candidate Shortlist

Deduplicated. The Phase 2 LLM copies `entity_slug` values directly into `related_entities`.

| entity_slug | entity_label | entity_type | source_ids |
|---|---|---|---|
| `<slug>` | `<label>` | `<type>` | `<source-id>` |

## 6. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  summaries: []
  concepts: []
  entities: []
page_architecture_rationale: "<answer coverage and duplication rationale>"
audit_items: []
manifest_updates: []
```

## 7. Compile Decision

```yaml
compile_decision:
  status: analysis_complete | partial
  phase_2_ready: true | false
  unresolved_priority_query_ids: []
  additional_sources_to_read: []
  truthful_state_if_stopped: "analysis_complete_unvalidated | partial"
```

Stop for `analysis_only`, an explicit safe mode, or a packet stop condition. Otherwise return the exact Phase 1 packet completion response. The deterministic control plane validates this file and the topic ledger, derives the Phase 2 packet, and remains the only owner of the next lifecycle stage. Phase 2 must follow the v2 page and semantic-acceptance contracts.
