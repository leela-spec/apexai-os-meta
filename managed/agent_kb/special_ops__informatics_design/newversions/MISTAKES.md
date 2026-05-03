# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for `special_ops__informatics_design` learning.

This file is never runtime truth and never self-promotes entries into accepted scaffold files.

## Write permissions

- `special_ops__informatics_design` may add candidate entries.
- `special_ops__hygiene_clean` may add validation notes.
- No writer may self-promote entries into accepted files.

## Promotion route

1. Capture candidate here.
2. Score `EVD` / `IMP` / `RSK`.
3. Validate hygiene impact and target placement.
4. Check whether the target is scaffold or appendix.
5. Route accepted changes through the governed KB promotion path when broader truth changes are involved.

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | appendix | archive
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__informatics_design
  validator: special_ops__hygiene_clean
  overlap_check:
  review_due:
```

## Pending provisional questions

| id | status | summary | candidate_target | evidence_refs | required validation |
|---|---|---|---|---|---|
| LQ-INF-001 | needs_validation | Determine whether sentence-level strictness should ever become a universal governed-Markdown rule. | best_practice or archive | `INFORMATION_DESIGN_OPEN_QUESTIONS.md` | repeated failures showing current guidance is insufficient |
| LQ-INF-002 | needs_validation | Determine whether prompt templates should become a governed information-design file class or remain adjacent operational assets. | template or archive | `INFORMATION_DESIGN_OPEN_QUESTIONS.md`, `Promptflow.md` | evidence that prompt-template placement affects retrieval/governance reliability |
| LQ-INF-003 | needs_validation | Determine how far schema-constrained structure should go beyond semantically structured Markdown. | best_practice or template | `INFORMATION_DESIGN_OPEN_QUESTIONS.md` | evidence that Markdown structure alone cannot preserve boundaries |
| LQ-INF-004 | needs_validation | Determine whether plain-language file-type declaration is sufficient or a stricter machine-readable declaration is needed. | template | `FILE_TAXONOMY_GPT.md`, `INFORMATION_DESIGN_OPEN_QUESTIONS.md` | audit failures caused by inconsistent declaration patterns |
| LQ-INF-005 | needs_validation | Determine the healthy boundary between useful reinforcement and contradiction-causing redundancy across governance-like files. | best_practice or mistake | `INFORMATION_DESIGN_OPEN_QUESTIONS.md` | maintenance evidence from downstream governance drafts |

## Candidate capture rules

- **Rule:** Candidate entries must preserve source path and candidate ID when available.
- **Rule:** Candidate entries must state whether they target scaffold, appendix, or archive.
- **Rule:** Provisional items must stay visibly provisional.
- **Constraint:** Do not treat repeated use as promotion.
- **Constraint:** Do not add broad content-truth validation work here; that belongs to validation or governance owners.

## Current appendix-backed candidate set

- **Pointer:** `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
- **Pointer:** `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
- **Pointer:** `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
