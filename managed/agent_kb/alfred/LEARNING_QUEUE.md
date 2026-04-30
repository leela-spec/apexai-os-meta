# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Alfred learning.

This file is never runtime truth. It does not override `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, or `TEMPLATES.md`, and it must not be used as a shortcut around validation or promotion.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
canonical_file: LEARNING_QUEUE.md
file_status: candidate_queue_consolidation_guarded
truth_status: candidate_only_never_runtime_truth
constrained_by:
  - managed/agent_kb/alfred/ESSENCE.md
  - managed/agent_kb/alfred/BEST_PRACTICES.md
  - managed/agent_kb/alfred/MISTAKES.md
  - managed/agent_kb/alfred/TEMPLATES.md
  - managed/agent_kb/alfred/SOURCE_MANIFEST.md
  - managed/agent_kb/alfred/COVERAGE_AUDIT.md
validator: meta_ops
next_recommended_file: managed/agent_kb/alfred/README.md
review_due: 2026-07-25
```

## Write permissions

- `alfred` may add candidate entries.
- `meta_ops` may add routing or validation notes.
- validators may update review status.
- no writer may self-promote entries into accepted files.
- no support file may bypass this queue and promotion path when material is unvalidated.

## Canonical target map

| Candidate material type | Candidate target |
|---|---|
| identity, authority, owns/does-not-own boundary, activation trigger | `essence` |
| intake method, route method, source-gap practice, EVD/IMP/RSK practice, one-file repair method | `best_practice` |
| recurring failure pattern, drift risk, anti-pattern, invalid use | `mistake` |
| reusable intake form, route brief, handoff packet, escalation form, report format | `template` |
| source/audit/provenance note that is not doctrine | `archive` or source/audit control note |
| incomplete or unclear material | `needs_validation` status before target selection |

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
  source_status: fully_read | partially_read | not_accessible | provisional | mixed | unknown
  owner: alfred
  validator: meta_ops
  overlap_check:
  review_due:
```

## Candidate boundary rules

- A queue entry is not accepted doctrine.
- A repeated queue entry is still not accepted doctrine.
- A strong candidate is still not accepted doctrine.
- A candidate may inform a review question but may not silently drive execution as runtime truth.
- If the candidate depends on unread local/manual material, mark `source_status: not_accessible` or `provisional` and preserve the source gap.
- If the candidate duplicates content already absorbed into a canonical file, archive or reject it rather than re-promoting it.
- If the candidate belongs in a support/source/audit file rather than a canonical file, mark `candidate_target: archive` and route through source/audit control instead of promotion to accepted doctrine.

## Pending entries

- EMPTY_STATE: no pending Alfred learning entries.

## Promotion route

1. Capture candidate here.
2. Classify the candidate target using the canonical target map.
3. Score `EVD` / `IMP` / `RSK`.
4. Record `source_status` explicitly.
5. Check overlap against `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, and `TEMPLATES.md`.
6. Validate with `meta_ops` or the required validator.
7. Package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`.
8. Apply only through the governed promotion path.

## Consolidation guardrail

During Alfred KB consolidation, this queue must not become a dumping ground for already-accepted material. Consolidated accepted content belongs in:

- `ESSENCE.md` for identity and authority,
- `BEST_PRACTICES.md` for operating method,
- `MISTAKES.md` for failure patterns,
- `TEMPLATES.md` for reusable forms.

Only genuinely unvalidated, future, unresolved, or source-gap-dependent learning belongs here.
