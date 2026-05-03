# APPENDIX_KB_CANDIDATE_LEDGER

## Purpose

Candidate ledger for `special_ops__hygiene_clean` Apex KB base extraction.

Candidates are reusable hygiene-control units. They are not accepted truth, not promotion packets, and not direct edits to managed runtime law.

## Candidate status rules

| Status | Meaning |
|---|---|
| `strong_candidate` | High-fit, high-reuse unit suitable for scaffold summary and later verification. |
| `candidate` | Useful unit that should remain appendix-level or template-level until validated. |
| `evidence_only` | Postmortem or example evidence; may support a rule but is not itself a rule. |
| `blocked` | Candidate cannot advance because a source, authority, or conflict issue remains unresolved. |

## Candidate scoring model

| Field | Meaning |
|---|---|
| `EVD` | evidence strength / direct support |
| `IMP` | consequence for structural hygiene and drift prevention |
| `RSK` | risk if misused, overgeneralized, or treated as accepted truth |
| `REL` | likely reuse frequency for this agent |

## Candidate table

| candidate_id | source_or_info_id | candidate_unit | candidate_target | EVD | IMP | RSK | REL | validation_need | status |
|---|---|---|---|---:|---:|---:|---:|---|---|
| HC-CAND-001 | HC-INFO-001 | Source authority and verification must be separate gates: authority before action, verification before approval. | best_practice | 95 | 100 | 20 | 100 | meta_detective review before acceptance | strong_candidate |
| HC-CAND-002 | HC-INFO-002 | Universal audit checks should inspect chunk self-containment, file typing, pass/fail state, and severity. | template | 90 | 95 | 25 | 95 | align with Apex QA/Hygiene constraints before acceptance | strong_candidate |
| HC-CAND-003 | HC-INFO-003 | Optimize hygiene outputs for retrieval clarity, low ambiguity, handoff reliability, and auditability. | essence | 88 | 95 | 20 | 95 | keep compact; do not expand into informatics doctrine | strong_candidate |
| HC-CAND-004 | HC-INFO-004 | Hygiene Clean owns QA reports, hygiene backlog, check execution, and closure recommendations; it does not own truth mutation or promotion. | essence | 90 | 100 | 15 | 100 | role-boundary review | strong_candidate |
| HC-CAND-005 | HC-INFO-005 | A hygiene-relevant execution must declare exact mode, branch/root, target files, allowed actions, forbidden actions, stop conditions, and deliverable. | template | 90 | 95 | 30 | 95 | test against patch/migration cases | strong_candidate |
| HC-CAND-006 | HC-INFO-006 | Use one-file-at-a-time execution for drift-sensitive files; validate before advancing. | best_practice | 90 | 95 | 25 | 95 | confirm exception boundaries | strong_candidate |
| HC-CAND-007 | HC-INFO-007 | Wording drift is a hygiene finding when a path or structure repair becomes semantic redesign. | mistake | 85 | 95 | 45 | 90 | classify severity using QA constraints | strong_candidate |
| HC-CAND-008 | HC-INFO-008 | Execute-not-explain drift occurs when a bounded repair task becomes explanation, process teaching, or broad reframing. | mistake | 85 | 95 | 50 | 95 | define stop wording | strong_candidate |
| HC-CAND-009 | HC-INFO-009 | Process files must function as blocking gates; citing doctrine is insufficient. | best_practice | 90 | 98 | 35 | 95 | require preflight proof in template | strong_candidate |
| HC-CAND-010 | HC-INFO-010 | Target-topology drift appears when new target files are designed before proving existing living files cannot absorb the logic. | mistake | 85 | 90 | 40 | 80 | restrict to harmonization/merge-mode contexts | strong_candidate |
| HC-CAND-011 | HC-INFO-011 | Exact-preservation validation should include expected file count, missing/extra files, size/line metrics, and checksums. | template | 90 | 88 | 20 | 80 | use only where exact preservation matters | candidate |
| HC-CAND-012 | HC-INFO-012 | Residual guidance should separate confirmed structure, recommended extensions, omitted elements, and open cautions. | template | 85 | 85 | 30 | 80 | keep as audit template, not architecture law | candidate |
| HC-CAND-013 | HC-INFO-013 | Source manifest rows must record duplicate group, representative source, access blockers, triage, and inclusion decision. | template | 90 | 92 | 30 | 90 | apply in future KB builds | strong_candidate |
| HC-CAND-014 | HC-INFO-014 | Failure evidence remains evidence and safeguards, not automatic universal doctrine. | essence | 90 | 95 | 25 | 95 | keep visible in scaffold | strong_candidate |
| HC-CAND-015 | HC-INFO-015 | KB essence candidates remain candidates until verification and required approval. | learning_queue | 85 | 90 | 20 | 85 | preserve non-promotion wording | strong_candidate |
| HC-CAND-016 | HC-INFO-016 | Candidate rows should preserve impact/evidence/integration score, drift warning, validator, target, status, and confidence. | learning_queue | 85 | 85 | 25 | 90 | adapt to local queue schema | candidate |

## Role-boundary candidates

| Boundary | Candidate expression | Status |
|---|---|---|
| Owns | structural QA, audit artifacts, pointer/source checks, stale-state detection, hygiene backlog, closure recommendations | strong_candidate |
| Does not own | truth mutation, promotion approval, strategy, architecture design, stop-law ownership | strong_candidate |
| Default posture | correctness-only cleanup; do not fuse creative linking or strategic reframing into hygiene work | strong_candidate |

## Validation-template candidates

```yaml
hygiene_audit_record:
  audit_id:
  target_scope:
  source_authority:
  checked_surfaces:
  expected_surfaces:
  missing_surfaces:
  extra_surfaces:
  exact_preservation_required: true | false
  metrics_checked:
    bytes: true | false
    chars: true | false
    lines: true | false
    checksum: true | false
  findings:
    - finding_id:
      severity: P0 | P1 | P2 | P3
      affected_surface:
      evidence_refs:
      required_action:
  verdict: pass | revise | fail | blocked
```

## Source-and-residual templates

```yaml
source_manifest_row:
  source_class:
  source_role: primary | supporting | evidence | excluded
  read_mode: full | skim | evidence_only
  duplicate_status:
  representative_source:
  access_status:
  inclusion_decision:
  role_fit:
  authority_risk:
```

```yaml
residual_guidance_row:
  item_id:
  classification: confirmed_structure | recommended_extension | optional_omitted | open_caution
  source_basis:
  hygiene_implication:
  allowed_next_action:
  forbidden_next_action:
```

## Blocked candidates

No candidate is blocked in this build. Recorded gap risks are non-blocking and remain in `APPENDIX_KB_SOURCE_MANIFEST.md`.
