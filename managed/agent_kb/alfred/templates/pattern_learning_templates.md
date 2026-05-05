# Pattern Learning Templates

## Purpose

Reusable Alfred pattern-learning forms.

These templates support candidate-first pattern capture, rejected-pattern archive, and promotion restraint.

## Boundary

Pattern observations remain candidate-first until threshold evidence and promotion rules are satisfied. One occurrence is not a pattern. Rejection should preserve trace when the candidate may resurface with new evidence.

## ALFRED-TPL-017 — Pattern Candidate v1

Use when repeated observations may become a future stable pattern.

```yaml
pattern_candidate_v1:
  pattern_id: PAT-YYYYMMDD-001
  observation: <what repeated or appears useful>
  occurrences:
    count: <integer>
    refs: []
  suspected_value: <why it may matter>
  constraints: []
  evidence:
    EVD: <1-100>
    IMP: <1-100>
    RSK: <1-100>
  status: candidate | strong_candidate | needs_validation | rejected | promoted
  promotion_threshold_note: <what evidence is still needed>
  stop_condition: Do not promote after one occurrence.
```

## Pattern candidate extended fields

Use when origin, type, and future target surface matter.

```yaml
pattern_candidate_extended_v1:
  candidate_id:
  created_at:
  created_by: Alfred | Night | MetaOps | Operator
  candidate_type: planning | craft_flow | handoff | blocker | operator_override | tracking | rhythm
  summary:
  evidence_count:
  source_records: []
  repeated_signal:
  proposed_use:
  risk_if_wrong:
  status: candidate
  operator_review_needed: true | false
  target_future_surface:
```

## ALFRED-TPL-029 — Rejected Pattern Archive v1

Use when a rejected candidate should retain enough trace to prevent repeated rediscovery or silent loss.

```yaml
rejected_pattern_archive_v1:
  candidate_id:
  rejected_at:
  rejection_reason:
  source_tracking_records: []
  resurface_only_if_new_evidence_count: ">=2"
```

## Invalid use

- Do not promote after one occurrence.
- Do not delete rejected candidates silently when future resurfacing is plausible.
- Do not treat pattern candidates as OpState or doctrine.
- Do not use pattern learning as Algorithm/Stats replacement.
