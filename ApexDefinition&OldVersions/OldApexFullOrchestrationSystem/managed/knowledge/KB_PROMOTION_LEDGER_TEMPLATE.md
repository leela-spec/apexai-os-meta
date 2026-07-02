# KB_PROMOTION_LEDGER_TEMPLATE

## Purpose

This file defines the managed template for packaging proposed KB promotions into reviewable, auditable promotion candidates.

It exists to preserve separation between:

- source material
- candidate learning
- accepted canon
- rejected or archived proposals

A promotion candidate is not accepted truth. A learning-queue entry is not accepted truth. Accepted content moves only through validation, decision, and trace.

## When to use

Use this template when a source, learning queue entry, research finding, session export, hygiene finding, or operator instruction proposes that managed OpenClaw knowledge should change.

Use it for candidate changes to:

- `managed/agent_kb/<agent_id>/ESSENCE.md`
- `managed/agent_kb/<agent_id>/BEST_PRACTICES.md`
- `managed/agent_kb/<agent_id>/MISTAKES.md`
- `managed/agent_kb/<agent_id>/TEMPLATES.md`
- `managed/knowledge/` governance files
- `managed/processes/` process contracts
- archive or rejection records for material candidates

Use it before accepted knowledge is modified, not after.

## Non-goals

This template does not:

- approve its own candidates
- replace `managed/rules/PROMOTION_PROTOCOL.md`
- replace validator judgment
- convert source material into canon by citation alone
- convert `LEARNING_QUEUE.md` entries into runtime truth
- define runtime config changes
- authorize `openclaw.json` edits
- store raw source dumps
- create final approved entries by itself
- allow the original writer to self-promote their own candidate

## Promotion candidate packet schema

```yaml
promotion_candidate:
  id:
  created_at:
  created_by:
  source_ref:
  source_type: learning_queue | session_export | research_report | hygiene_finding | operator_request | current_file_audit | other
  proposed_target:
  target_file:
  target_section:
  summary:
  candidate_type: essence | best_practice | mistake | template | governance | process | archive
  current_status: candidate | strong_candidate | needs_validation
  evidence_refs:
    - ref:
      relevance:
      limitation:
  scores:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
  owner:
  validator:
  secondary_validator:
  operator_review_required: true | false
  overlap_check:
    checked_against:
      - target_or_surface:
    conflict_found: true | false
    conflict_summary:
    required_resolution:
  source_candidate_canon_check:
    source_material_identified: true | false
    candidate_boundary_preserved: true | false
    accepted_canon_target_identified: true | false
    learning_queue_runtime_truth_forbidden: true
    source_promoted_directly: false
  risk_if_promoted:
  risk_if_rejected:
  review_due:
  decision:
    status: accepted | rejected | archived | needs_revision
    decided_by:
    decision_date:
    rationale:
    applied_trace:
```

## Required metadata

Every promotion candidate must name:

- `id`
- `created_at`
- `created_by`
- `source_ref`
- `source_type`
- `proposed_target`
- `target_file`
- `summary`
- `candidate_type`
- `current_status`
- `evidence_refs`
- `scores.EVD`
- `scores.IMP`
- `scores.RSK`
- `owner`
- `validator`
- `operator_review_required`
- `overlap_check`
- `source_candidate_canon_check`
- `risk_if_promoted`
- `risk_if_rejected`
- `review_due`
- `decision.status`

A candidate without a target file, validator, evidence reference, score set, or source/candidate/canon check is invalid.

## Scoring schema

Scores use the locked `EVD` / `IMP` / `RSK` model on a 1-100 scale.

Scores are interpreted primarily by band, not by exact numeric value. Fine-grain differences inside the same band must not be used to bypass validation, overlap, escalation, or operator-review requirements.

| Score range | Meaning |
|---:|---|
| 1-20 | low |
| 21-40 | limited |
| 41-60 | material |
| 61-80 | strong/high |
| 81-100 | decisive/highest |

### `EVD` — evidence strength

`EVD` measures how strongly the available evidence supports the proposed promotion.

| Score range | Use when |
|---:|---|
| 1-20 | evidence is weak, indirect, mostly asserted, or not yet traceable enough for the proposed target |
| 21-40 | evidence is present but narrow, stale, incomplete, or materially caveated |
| 41-60 | evidence materially supports the candidate but still needs validation before accepted use |
| 61-80 | evidence is strong across relevant surfaces, repeated use, or bounded validation |
| 81-100 | evidence is decisive, current, bounded, directly tied to the target, and suitable for high-confidence review |

### `IMP` — impact

`IMP` measures how materially the proposed promotion improves OpenClaw operation, governance, retrieval, or drift control.

| Score range | Use when |
|---:|---|
| 1-20 | impact is minor, cosmetic, or local without durable governance effect |
| 21-40 | impact is limited to a narrow local case or reversible improvement |
| 41-60 | impact is material for a recurring workflow, agent boundary, KB route, or process surface |
| 61-80 | impact is high for governance, routing, KB quality, operational stability, or cross-agent behavior |
| 81-100 | impact is highest-order and affects load-bearing system behavior, truth authority, promotion paths, or runtime safety |

### `RSK` — risk

`RSK` measures the risk of promoting the candidate incorrectly, prematurely, or into the wrong surface.

| Score range | Use when |
|---:|---|
| 1-20 | promotion risk is low, localized, reversible, and authority is clear |
| 21-40 | risk is limited but still requires visible rationale and target clarity |
| 41-60 | risk is material and requires explicit validation or overlap review |
| 61-80 | risk is high because authority, scope, downstream behavior, or reversibility may shift |
| 81-100 | risk is highest because a wrong promotion could corrupt canon, governance, routing, runtime authority, or config boundaries |

## Overlap check

Every candidate must check for overlap before decision.

The overlap check must answer:

- Does another file already own this rule, practice, mistake, template, governance point, or process contract?
- Is the proposed target the correct surface?
- Would the promotion duplicate, contradict, or weaken existing canon?
- Does the candidate belong in per-agent KB, shared `managed/knowledge/`, or `managed/processes/`?
- Does the candidate affect another agent's boundary or validator responsibility?

If overlap is unresolved, the candidate status must be `needs_validation` or the decision status must be `needs_revision`.

## Source/candidate/canon separation check

Every candidate must preserve the following boundary:

| Layer | Meaning | Runtime truth status |
|---|---|---|
| Source material | Evidence, reports, sessions, audits, current files, or operator notes | not canon by itself |
| Candidate | A proposed learning or governance change packaged for review | not accepted truth |
| Accepted canon | Validated content applied to the correct governed target | accepted only after approval and trace |
| Rejected or archived item | A reviewed candidate that did not become accepted canon | not accepted truth |

Required checks:

- `LEARNING_QUEUE.md` entries remain candidate-only.
- Source material is evidence, not canon.
- Repeated use is not automatic promotion.
- Session exports can nominate candidates, but cannot mutate truth directly.
- Hygiene findings can nominate candidates, but cannot mutate truth directly.
- Accepted content must be traceable to a validation decision.
- Rejected items are marked rejected or archived; they are not silently deleted.

## Validator requirements

Every candidate must name an owner and at least one validator.

Default validator expectations:

| Candidate target | Owner | Validator expectation |
|---|---|---|
| Per-agent `ESSENCE.md` | target agent | default validator for that agent KB root |
| Per-agent `BEST_PRACTICES.md` | target agent | default validator for that agent KB root |
| Per-agent `MISTAKES.md` | target agent | default validator for that agent KB root |
| Per-agent `TEMPLATES.md` | target agent | default validator for that agent KB root |
| `managed/knowledge/` governance file | `special_ops__knowledge_bank` | `special_ops__informatics_design` or `meta_detective`, depending on risk |
| `managed/processes/` process contract | process owner | `meta_ops` and `meta_detective` for load-bearing process changes |
| archive or rejection record | original owner | original validator or hygiene validator |

No writer may self-promote their own candidate. If the proposer is also the owner, the validator must be independent.

Governance or process promotions require the proper validator before acceptance. High-risk authority, routing, or truth-boundary changes require explicit operator review when required by the governing promotion path.

## Decision states

Candidate status and decision status are distinct.

### Candidate status

| Status | Meaning |
|---|---|
| `candidate` | captured but not yet strongly supported |
| `strong_candidate` | evidence appears strong enough for review |
| `needs_validation` | cannot proceed without validator review or overlap resolution |

### Decision status

| Status | Meaning |
|---|---|
| `accepted` | validator approved the candidate for application to the named target |
| `rejected` | validator rejected the candidate and recorded why |
| `archived` | candidate is retained for history but not active for promotion |
| `needs_revision` | candidate is not ready and must be corrected before another decision |

`accepted` does not mean applied unless `applied_trace` is present or another governed application trace identifies the change.

## Promotion decision record

When a decision is made, record:

```yaml
promotion_decision_record:
  candidate_id:
  decision_status: accepted | rejected | archived | needs_revision
  decided_by:
  decision_date:
  validator:
  operator_review:
    required: true | false
    completed: true | false
    reviewer:
  rationale:
  evidence_refs_used:
    - ref:
  target_file:
  target_section:
  application_required: true | false
  applied_trace:
  follow_up_required:
```

A decision record must be sufficient for a later reviewer to reconstruct why the candidate advanced, looped back, or stopped.

## Rejection and archive handling

Rejected or archived candidates must remain visible enough to prevent repeated rediscovery.

Minimum handling:

- preserve the candidate ID
- preserve the source reference
- preserve the rejected or archived decision status
- record the rationale
- record whether the candidate may be reconsidered
- record the condition that would justify reconsideration

Do not silently delete rejected candidates when they explain a future boundary, failure pattern, or drift risk.

## Invalid patterns

The following patterns are invalid:

- candidate with no validator
- candidate with no evidence reference
- candidate with no target file
- candidate with no owner
- candidate with no `EVD` / `IMP` / `RSK` scores
- candidate with scores outside the 1-100 range
- candidate using unbanded pseudo-precision to bypass validation
- self-promotion by the writer or original drafter
- `LEARNING_QUEUE.md` entry treated as runtime truth
- source material copied into canon without validation
- rejected candidate silently deleted
- governance change routed only as a per-agent practice
- process contract change routed only as a per-agent template
- runtime config change disguised as KB cleanup

## Acceptance criteria

This template is valid when:

- it uses `EVD`, `IMP`, and `RSK` as the required scoring model
- scoring uses the 1 to 100 scale
- scoring is interpreted primarily by five bands, not by unsupported fine-grain differences
- source, candidate, canon, rejection, and archive states are distinct
- learning queues are candidate-only
- owner and validator are mandatory
- self-promotion is forbidden
- overlap checks are mandatory
- governance and process candidates require the proper validator
- accepted content requires validation and trace
- rejected or archived items remain visibly dispositioned
- runtime config doctrine is excluded
