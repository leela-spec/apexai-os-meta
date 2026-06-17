# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Meta Strategy learning. This file is never runtime truth.

## Write permissions

- `meta_strategy` may add candidate entries
- `meta_detective` may add validation notes
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
  owner: meta_strategy
  validator: meta_detective
  overlap_check:
  review_due:
```

## Pending entries

- EMPTY_STATE: no pending Meta Strategy learning entries.

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK`
3. route to the target file class
4. validate with `meta_detective`
5. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
6. apply only through the governed promotion path
