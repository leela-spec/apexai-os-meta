# TEMPLATES

## Purpose

Reusable templates for `special_ops__hygiene_clean` audits, findings, closure checks, source manifests, ranking rows, and evidence notes.

Detailed candidate basis lives in `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`.

## Template chooser

| Need | Use template |
|---|---|
| Run or report a bounded audit | `hygiene_audit_record` |
| Record a hygiene issue | `finding_record` |
| Close, downgrade, defer, or escalate a finding | `closure_record` plus closure validity checklist |
| Lock a drift-sensitive execution mode | `execution_mode_lock` |
| Record source coverage or access status | `source_manifest_row` |
| Record source-note decisions | `source_note_row` |
| Rank a reusable information unit | `information_ranking_row` |
| Record source evidence or postmortem evidence | `evidence_note` |
| Trace candidate realization into scaffold or appendix | `candidate_realization_trace` |
| Report unsafe source disagreement | `source_conflict_report` |

## Severity crib

| Severity | Local meaning | Default handling |
|---|---|---|
| `P0` | Critical governance, authority, or trace failure; normal continuation is unsafe. | hold or escalate immediately |
| `P1` | High-risk integrity failure affecting current routing, source trust, closure, or approval safety. | remediate before normal progression or declare bounded degraded handling |
| `P2` | Material hygiene debt that degrades reliability but is not immediately blocking. | backlog with bounded follow-up path |
| `P3` | Low-risk cleanup, naming, formatting, or minor consistency issue. | batch cleanup or explicit deferment |

## Closure validity checklist

A closure is valid only when every applicable check is true:

- the original finding remains identifiable
- the affected surface was rechecked after remediation
- required action is complete or explicit deferment/downgrade is recorded
- closure evidence references are visible
- residual risk is stated when any risk remains
- downgrade reason is stated when severity changed
- follow-up path is stated for deferred or partially remediated issues
- verifier is named or verification owner is explicitly pending
- closure does not silently promote candidate content into runtime truth

## Hygiene audit record

```yaml
hygiene_audit_record:
  audit_id:
  target_scope:
  generated_at:
  source_authority:
    primary_sources: []
    derived_sources: []
    missing_sources: []
    conflicts: []
  checked_surfaces: []
  expected_surfaces: []
  check_families:
    authority_boundary: true | false
    verification_boundary: true | false
    candidate_truth_boundary: true | false
    cross_agent_ownership: true | false
    config_impact_review: true | false
  missing_surfaces: []
  extra_surfaces: []
  exact_preservation_required: true | false
  metrics_checked:
    file_count: true | false
    missing_files: true | false
    extra_files: true | false
    size: true | false
    bytes: true | false
    chars: true | false
    lines: true | false
    checksum: true | false
  highest_severity: P0 | P1 | P2 | P3 | none
  verdict: pass | revise | fail | blocked
```

## Finding record

```yaml
finding_record:
  finding_id:
  finding_class: authority_drift | verification_drift | rewrite_drift | mode_drift | scope_drift | closure_drift | candidate_truth_drift | pointer_failure | state_integrity_failure | source_gap | config_impact_review_missing | cross_agent_ownership_unclear | exact_preservation_failure
  severity: P0 | P1 | P2 | P3
  affected_surface:
  description:
  evidence_refs: []
  required_action:
  hold_or_escalation_needed: true | false
  owner:
  routed_owner:
  routing_reason:
  verifier:
  status: open | remediating | blocked | closed | escalated
```

## Closure record

```yaml
closure_record:
  finding_id:
  closure_status: closed | downgraded | deferred | escalated
  closure_evidence_refs: []
  affected_surface_checked: true | false
  required_action_completed: true | false
  residual_risk:
  downgrade_reason:
  follow_up_path:
  closed_by:
  verified_by:
  closed_at:
```

## Candidate realization trace

```yaml
candidate_realization_trace:
  candidate_id:
  source_file:
  approved_decision: integrate_into_scaffold | integrate_into_appendix | split_between_scaffold_and_appendix | keep_as_candidate | defer | reject
  realized_as:
  realized_file:
  scaffold_id:
  status_after_build: accepted_in_kb_base | candidate | strong_candidate | evidence_only | deferred | rejected | promotion_required
  next_validation:
  notes:
```

## Execution-mode lock

```yaml
execution_mode_lock:
  mode: inspect_only | patch_only | validate_only | create_only | move_only | content_draft_only
  repo:
  branch_or_ref:
  root:
  target_files: []
  allowed_actions: []
  forbidden_actions: []
  stop_conditions: []
  deliverable:
  protected_spans:
  verification_plan:
```

## Source manifest row

```yaml
source_manifest_row:
  source_path:
  source_role: primary | supporting | evidence | excluded
  read_mode: full | skim | evidence_only
  duplicate_status:
  representative_source:
  access_status: readable | blocked | partial | unknown
  inclusion_decision: include | exclude | evidence_only | defer
  role_fit:
  authority_risk:
  notes:
```

## Source note row

```yaml
source_note_row:
  note_id:
  source_path:
  source_gap_severity: P0 | P1 | P2 | P3 | none
  source_note_type: access_blocker | duplicate_resolution | representative_choice | conflict_watch | authority_note | inclusion_note
  decision:
  rationale:
  affected_candidates: []
  affected_scaffold_files: []
  follow_up:
  status: open | monitored | closed | deferred
```

## Information ranking row

```yaml
information_ranking_row:
  info_id:
  source_path:
  source_role:
  source_section_or_candidate_id:
  information_unit:
  agent_relevance: 0-100
  actionability: 0-100
  evidence_strength: 0-100
  reuse_frequency_likelihood: 0-100
  drift_risk: 0-100
  recommended_target_file:
  appendix_pointer:
  scaffold_summary_needed: true | false
  status: candidate | strong_candidate | evidence_only | blocked
```

## Evidence note

```yaml
evidence_note:
  evidence_id:
  source_path:
  evidence_type: primary_rule | supporting_process | postmortem | validation_report | ledger_row
  observed_failure_or_control:
  hygiene_extraction:
  reusable_safeguard:
  limits_of_use:
  related_candidates: []
```

## Source conflict report trigger

Create `appendices/SOURCE_CONFLICT_REPORT.md` only when one of these is true:

- two primary sources conflict on target boundary, role ownership, or allowed action
- a required source is missing and cannot be bypassed safely
- duplicate variants differ materially and representative-source selection is unsafe
- authority risk cannot be bounded inside the source manifest

## Minimal conflict report shape

```yaml
source_conflict_report:
  conflict_id:
  affected_scope:
  source_a:
  source_b:
  conflict_watch_status: open | monitored | closed
  source_gap_severity: P0 | P1 | P2 | P3 | none
  affected_candidates: []
  conflict_summary:
  blocking: true | false
  safest_interim_handling:
  required_decision:
  owner:
  validator:
```
