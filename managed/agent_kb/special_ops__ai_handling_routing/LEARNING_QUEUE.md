# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for AI Handling Routing learning. This file is never runtime truth.

## Write permissions

- `special_ops__ai_handling_routing` may add candidate entries
- `meta_ops` may add validation notes
- `meta_detective` may add escalation notes when overreach risk appears
- no writer may self-promote entries into accepted files

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | archive
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  overlap_check:
  review_due:
```

## Pending entries

- EMPTY_STATE: no pending AI Handling Routing learning entries.

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK`
3. validate with `meta_ops`
4. escalate to manual review whenever config impact is implicated
5. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
6. apply only through the governed promotion path
