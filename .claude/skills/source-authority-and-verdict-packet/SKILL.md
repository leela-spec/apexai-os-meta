---
name: source-authority-and-verdict-packet
description: >
  Use this skill when validating, approving, challenging, or routing research,
  handovers, KB outputs, migration packets, or repo-change proposals. It
  classifies source authority before verification, rejects approval by fluency,
  enforces validator/executor separation, and returns a verdict packet with
  evidence, gaps, risks, stop conditions, and next-owner routing. It does not
  implement the reviewed fix, change runtime configuration, or provide final
  operator approval.
---

# Source Authority and Verdict Packet

## Contract

```yaml
package_name: source-authority-and-verdict-packet
primary_role: validation_and_routing_guardrail
source_doctrine:
  primary_pages:
    - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/handoff-validation-and-risk-doctrine.md
    - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/validation-and-routing-guardrails.md
    - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/entities/meta-detective-internal-modes.md
  decision_packet:
    - apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/old-agent-kb-migration-decision-packet.md
owns:
  - source_authority_classification
  - evidence_sufficiency_review
  - contradiction_and_inference_jump_detection
  - validator_executor_separation
  - verdict_packet_generation
  - stop_condition_framing
  - next_owner_or_validator_routing
does_not_own:
  - implementing_the_reviewed_fix
  - applying_patches
  - changing_runtime_configuration
  - changing_provider_or_model_policy
  - final_operator_approval
  - promoting_candidate_material_to_runtime_truth
```

## Trigger conditions

Use this skill when the operator asks to validate, verify, approve, challenge, audit, route, or decide whether to carry forward an AI output, implementation plan, migration packet, handover, KB phase output, or repo-change proposal.

Treat the task as medium or high risk when it touches repo writes, runtime configuration, provider/model policy, KB phase gates, current architecture migration, or authority promotion.

## Doctrine

```yaml
rules:
  source_authority_before_verification: "Classify each source before trusting, approving, routing, or implementing an output."
  approval_by_fluency_is_invalid: "Do not approve an artifact because it is polished or plausible; require evidence, read-back, diff, test, schema, source pointer, or acceptance criteria."
  validator_executor_separation: "Validators return findings, gaps, risks, stop conditions, and owner routes; they do not implement or self-approve the reviewed fix."
  historical_source_not_runtime_authority: "Old OpenClaw paths, old local paths, old role rosters, and stale provider claims remain historical evidence unless verified and promoted."
  candidate_not_canon: "Learning queues, draft patterns, and candidate notes are not runtime truth until promoted through an owner/validator or operator gate."
```

## Source authority classes

```yaml
current_primary: "Live repo files read in the current run, current operator instruction, current official docs, or deterministic report from current target state."
compiled_kb_primary: "Approved compiled KB wiki index, summary, concept, entity, or audit page."
secondary_analysis: "Phase 1 analysis, prior research report, or migration decision packet."
historical_evidence: "Old paths, old role names, old configs, old runtime assumptions, or legacy examples."
unverified_claim: "Memory-based, filename-inferred, or plausible AI synthesis without source pointer."
operator_decision: "Human authority decision such as approval phrase, scope expansion, or explicit override."
```

## Procedure

1. Define the artifact or decision under review, requested action, stakes, affected surfaces, and explicit operator constraints.
2. Build a source ledger with source name, authority class, read status, relevance, and limits.
3. Check for validator/executor collapse. If the validator is also expected to implement and approve a high-risk fix, stop or route.
4. Scan for approval by fluency, summary elevation, advisory routing collapse, path drift, candidate-as-canon, old-runtime-authority import, and unsupported current claims.
5. Return the verdict packet. Preserve unresolved operator decisions instead of silently normalizing them.

## Verdict packet schema

```yaml
VERDICT_PACKET:
  verdict: "PASS | PASS_WITH_WARNINGS | NEEDS_OPERATOR_DECISION | FAIL"
  confidence: "high | medium | low | mixed"
  artifact_or_decision_reviewed: ""
  source_authority_summary:
    current_primary_sources_read: []
    compiled_kb_primary_sources_read: []
    secondary_sources_read: []
    historical_sources_used: []
    unverified_or_unread_sources: []
  key_findings: []
  evidence_gaps: []
  risks: []
  stop_conditions: []
  required_operator_decisions: []
  next_owner_or_route: ""
  validator_executor_boundary:
    validator_did_not_execute_fix: true
    executor_needed: "yes | no"
    final_approval_owner: "operator | separate_validator | not_required | other"
  anti_pattern_scan:
    approval_by_fluency: "clear | warning | violation"
    summary_elevation: "clear | warning | violation"
    advisory_routing_collapse: "clear | warning | violation"
    path_drift: "clear | warning | violation"
    candidate_as_canon: "clear | warning | violation"
    old_runtime_authority_import: "clear | warning | violation"
```

## Repo-affecting work addendum

For repo-affecting work, require or produce a route contract before execution: repository, branch, exact target paths, operation class, allowed actions, forbidden actions, pre-write checks, post-write checks, stop conditions, and commit strategy.

If this contract is missing for medium/high-risk repo work, return `NEEDS_OPERATOR_DECISION` or `FAIL` rather than approving execution.

## Completion criteria

```yaml
completion_criteria:
  - source_authority_was_classified_before_verdict
  - concrete_sources_or_evidence_gaps_are_visible
  - validation_did_not_rely_on_fluency_or_plausibility
  - validator_executor_boundary_is_explicit
  - verdict_packet_uses_allowed_verdict_values
  - risks_and_stop_conditions_are_visible
  - next_owner_or_route_is_actionable
  - unresolved_operator_decisions_are_preserved
```
