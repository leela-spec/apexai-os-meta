---
analysis_id: "<kb-slug>-<topic-id>-analysis"
run_id: "<run-id>"
config_hash: "sha256:<64-hex>"
kb_slug: "<kb-slug>"
topic_id: "<topic-id>"
phase: phase1
status: in_progress | analysis_complete | partial
last_validated_batch: "<batch-id-or-none>"
source_count_reviewed: 0
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
---

# Phase 1 Analysis — <Topic Name>

This cumulative topic file is updated only through generated Phase 1 batch instructions. The semantic ledger is the machine progress owner.

## 1. Locked Question Status

| query_id | priority | status | concise finding | supporting source IDs | remaining evidence need |
|---|---|---|---|---|---|
| `<id>` | critical | answered / partial / contradicted / blocked / not_covered | `<finding>` | `<ids>` | `<need or none>` |

## 2. Candidate Source Disposition

Every candidate surfaced by Phase 0 receives one row, including unopened, duplicate, incidental, irrelevant-after-review, and blocked files.

| source_id | Phase 0 tier | read status | semantic disposition | individual topic value | duplicate/version relation | authority/freshness assessment | exact pointers | next action |
|---|---|---|---|---|---|---|---|---|
| `<id>` | filename / h1 / heading / body_strong / body_weak / linked | complete / targeted / blocked / unopened | core / contextual / historical / prototype / implementation / duplicate / superseded / incidental / irrelevant_after_review / unreadable | `<one sentence>` | `<relation or none>` | `<evidence-based assessment>` | `<pointers>` | none / next_batch / operator_question |

## 3. Validated Batch Records

Repeat once per validated batch. Do not rewrite prior validated records unless a repair instruction names them.

### Batch `<batch-id>`

```yaml
instruction_id: "<instruction-id>"
input_fingerprints: {}
sources_reviewed: []
questions_advanced: []
questions_still_unresolved: []
unexpected_findings:
  - finding: "<finding>"
    treatment: candidate_follow_up | uncertainty | contradiction
    source_pointer: "<pointer>"
```

## 4. Source Findings

Repeat once per reviewed source.

```yaml
source:
  source_id: "<source-id>"
  path: "<path>"
  read_status: complete | targeted | blocked
  reviewed_passages: []
  one_sentence_core: "<source contribution>"
  authority_and_freshness:
    assessment: "<semantic judgment grounded in evidence>"
    evidence: []
  question_coverage:
    - query_id: "<id>"
      outcome: answered | partial | contradicted | blocked | not_covered
      finding: "<finding>"
      pointers: []
  claims:
    - claim_id: "<source-id>-C001"
      claim: "<claim>"
      state: present | proposed | open
      confidence: high | medium | low
      pointer: "<pointer>"
  contradictions: []
  reusable_definitions: []
  reusable_processes: []
  concept_candidates: []
  entity_candidates: []
```

## 5. Cross-Source Reconciliation

- Current definition and why it wins:
- Historical/prototype alternatives:
- Contradictions preserved:
- Duplicate/supersession relationships:
- Remaining critical/routine blockers:

## 6. Phase 2 Input

```yaml
phase2_input:
  ready: true | false
  direct_answers_by_query: {}
  claims_to_preserve: []
  concepts_approved_for_pages: []
  entities_approved_for_pages: []
  source_atlas_rows_required: []
  uncertainty_to_preserve: []
  unresolved_query_ids: []
```

## 7. Compile Decision

```yaml
compile_decision:
  status: analysis_complete | partial
  phase2_ready: true | false
  reason: "<reason>"
  truthful_state_if_stopped: analysis_complete_unvalidated | partial
```
