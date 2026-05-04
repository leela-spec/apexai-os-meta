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

### ALFRED-LQ-001 — Full Weekly Rhythm Plan v1.1

```yaml
id: ALFRED-LQ-001
status: candidate
source_ref: appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md
summary: Define a fuller Weekly Rhythm Plan only after Daily Command Board and tracking evidence are stable.
candidate_target: best_practice
evidence_refs:
  - appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md
scores:
  EVD: 60
  IMP: 80
  RSK: 65
source_status: provisional
owner: alfred
validator: meta_ops
overlap_check: does not duplicate accepted Daily Command Board rules
review_due: 2026-07-25
```

### ALFRED-LQ-002 — Monthly Direction Map operationalization

```yaml
id: ALFRED-LQ-002
status: candidate
source_ref: appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md
summary: Convert Monthly Direction Map from placeholder to operational planning model only after daily/weekly evidence matures.
candidate_target: template
evidence_refs:
  - managed/agent_kb/alfred/TEMPLATES.md
scores:
  EVD: 50
  IMP: 75
  RSK: 60
source_status: provisional
owner: alfred
validator: meta_ops
overlap_check: placeholder exists in TEMPLATES.md only if promoted through patch flow
review_due: 2026-07-25
```

### ALFRED-LQ-003 — Low-risk OpState auto-apply classes

```yaml
id: ALFRED-LQ-003
status: candidate
source_ref: appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
summary: Identify whether any future OpState delta classes are safe for auto-apply without operator review.
candidate_target: best_practice
evidence_refs: []
scores:
  EVD: 40
  IMP: 70
  RSK: 80
source_status: provisional
owner: alfred
validator: meta_detective
overlap_check: must not weaken accepted no-direct-mutation rule
review_due: 2026-07-25
```

### ALFRED-LQ-004 — Future algorithm from tracking evidence

```yaml
id: ALFRED-LQ-004
status: candidate
source_ref: future tracking records
summary: Explore whether tracking records can later calibrate Alfred process priority and board recommendation rules.
candidate_target: best_practice
evidence_refs: []
scores:
  EVD: 35
  IMP: 75
  RSK: 65
source_status: unknown
owner: alfred
validator: meta_ops
overlap_check: must not become Algorithm/BP/XP replacement
review_due: 2026-07-25
```

### ALFRED-LQ-005 — Future BP/XP relation

```yaml
id: ALFRED-LQ-005
status: candidate
source_ref: future Leela metric source-extension pass
summary: Reconsider whether Alfred process tracking should reference BP/XP after source validation.
candidate_target: needs_validation
evidence_refs: []
scores:
  EVD: 25
  IMP: 70
  RSK: 75
source_status: not_accessible
owner: alfred
validator: meta_detective
overlap_check: accepted Alfred v1 excludes BP/XP tracking
review_due: 2026-07-25
```

### Additional future candidates

- Future mood/energy tracking reconsideration.
- Pattern library storage structure.
- Automation of candidate detection.
- Visualization of Daily Command Board.
- Calibration of `EVD / IMP / RSK + URG` and P-class rules from real use.

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
