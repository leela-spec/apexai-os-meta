# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Knowledge Bank learning. This file is never runtime truth.

## Write permissions

- `special_ops__knowledge_bank` may add candidate entries
- `special_ops__informatics_design` may add validation notes
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
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check:
  review_due:
```

## Pending entries

- EMPTY_STATE: no pending Knowledge Bank learning entries.

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK`
3. validate placement and structure
4. route to the target file class
5. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
6. apply only through the governed promotion path
