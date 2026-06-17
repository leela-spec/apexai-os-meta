# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for `special_ops__hygiene_clean` learning.

This file is never runtime truth. It stores proposed improvements, failure patterns, and template candidates until they are validated and routed.

## Write permissions

- `special_ops__hygiene_clean` may add candidate entries.
- `meta_detective` may add validation notes.
- No writer may self-promote entries into accepted files.
- Truth-changing outcomes require the governed promotion path.

## Status vocabulary

| Status | Meaning |
|---|---|
| `candidate` | Captured for later review; not accepted guidance. |
| `strong_candidate` | High-fit candidate with stronger evidence or reuse value; still not accepted truth. |
| `needs_validation` | Requires source, overlap, owner, or routing validation before action. |
| `evidence_only` | Preserved as support or postmortem evidence; not a rule candidate by itself. |
| `accepted_in_kb_base` | Already represented in the current KB scaffold or appendices; not global runtime truth by placement alone. |
| `promotion_required` | Requires governed promotion before any truth-changing use. |
| `rejected` | Not suitable for this KB or superseded by a better target. |
| `archived` | Retained for trace only; no active follow-up. |

## Appendix map

| Appendix | Use |
|---|---|
| `appendices/APPENDIX_KB_SOURCE_MANIFEST.md` | source coverage and gap-risk context |
| `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | ranked source-derived information units |
| `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md` | current candidate pool and scoring basis |
| `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | evidence notes and drift safeguards |
| `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | QA status, deferred research, and recommended patch sequence |

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
  status_after_review: candidate | strong_candidate | evidence_only | accepted_in_kb_base | promotion_required | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | appendix | archive
  evidence_refs: []
  realization_trace_ref: appendices/APPENDIX_KB_CANDIDATE_LEDGER.md | none
  scores:
    EVD:
    IMP:
    RSK:
    REL:
  owner: special_ops__hygiene_clean
  validator: meta_detective
  overlap_check:
  promotion_required: true | false
  approval_required: true | false
  runtime_truth_claimed: false
  review_due:
```

## Pending entries from KB-base build

| id | status | summary | candidate_target | evidence_refs | next validation |
|---|---|---|---|---|---|
| HC-LQ-001 | strong_candidate | Add source-authority and verification-gate practice to accepted practices after meta_detective review. | best_practice | `HC-CAND-001`, `HC-EVID-001` to `HC-EVID-003` | verify against QA/Hygiene Protocol and current promotion boundary |
| HC-LQ-002 | strong_candidate | Add exact-span repair and no-whole-file-rewrite rule for bounded defects. | best_practice | `HC-CAND-005`, `HC-CAND-007`, `HC-CAND-008` | verify wording with process owner before acceptance |
| HC-LQ-003 | strong_candidate | Add execute-not-explain drift as a reusable mistake pattern. | mistake | `HC-EVID-010` to `HC-EVID-012` | validate severity defaults and stop conditions |
| HC-LQ-004 | strong_candidate | Add process-gate bypass as a reusable mistake pattern. | mistake | `HC-EVID-013`, `HC-EVID-014` | validate how to test gate compliance |
| HC-LQ-005 | candidate | Add exact-preservation validation template with count/metric/checksum checks. | template | `HC-EVID-017` | restrict to exact preservation contexts |
| HC-LQ-006 | candidate | Add residual-guidance classification template. | template | `HC-EVID-018` | confirm it remains hygiene template, not architecture authority |

## Realization trace boundary

Candidate realization fields such as `realized_as`, `realized_file`, `scaffold_id`, `status_after_build`, and `next_validation` belong in `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`.

This queue may point to that ledger, but it must not duplicate ledger trace state or imply that queue placement accepts a candidate into runtime truth.

## Promotion route

1. Capture candidate here.
2. Score `EVD` / `IMP` / `RSK` / `REL`.
3. Validate with `meta_detective`.
4. Check overlap with existing accepted KB surfaces.
5. Route to target file class only if verified.
6. Package durable truth changes through the governed promotion path.
7. Apply only after approval where required.

## Queue hygiene rules

- Do not leave candidates without status.
- Do not close by omission.
- Do not copy evidence-only postmortems into accepted rules without extraction and validation.
- Do not use this queue as a substitute for promotion packets.
- Archive rejected or superseded candidates with reason.
- Do not treat `accepted_in_kb_base` as global runtime truth.
- Do not duplicate candidate realization state; point to the candidate ledger.
