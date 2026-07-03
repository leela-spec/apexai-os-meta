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
  kb_slug: old-apex-full-orchestration-agent-kb
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

Use this skill when the user asks to validate, verify, approve, challenge, audit, route, or decide whether to carry forward an AI output, implementation plan, migration packet, handover, KB phase output, or repo-change proposal.

Treat the task as medium or high risk when it touches repo writes, runtime configuration, provider/model policy, KB phase gates, current architecture migration, or authority promotion.

Do not use this skill for trivial formatting, low-risk copy edits, or pure drafting unless validation or approval is requested.

## Core doctrine

```yaml
rules:
  source_authority_before_verification: >
    Classify what each source is before trusting, forwarding, approving,
    routing, patching, or implementing an output.
  approval_by_fluency_is_invalid: >
    Do not approve an artifact because it is polished, coherent, or plausible.
    Require concrete evidence, read-back, diff, test, schema, source pointer,
    or acceptance criteria.
  validator_executor_separation: >
    Validators return findings, evidence gaps, risks, stop conditions, and
    owner routes. They do not implement or self-approve the reviewed fix.
  historical_source_not_runtime_authority: >
    Old OpenClaw paths, old local paths, old role rosters, and stale provider
    claims remain historical evidence unless separately verified and promoted.
  candidate_not_canon: >
    Learning queues, draft patterns, and candidate notes are not runtime truth
    until promoted through an owner/validator or operator gate.
```

## Source authority classes

```yaml
source_authority_classes:
  current_primary:
    examples: [live_repo_file_read_in_current_run, current_operator_instruction, current_official_docs, deterministic_report_from_current_target_state]
    default_trust: high
  compiled_kb_primary:
    examples: [compiled_wiki_index, compiled_summary_page, compiled_concept_page, compiled_entity_page, semantic_open_questions_audit_page]
    default_trust: high_or_frontmatter_limited
  secondary_analysis:
    examples: [ingest_analysis, prior_research_report, migration_decision_packet]
    default_trust: medium
  historical_evidence:
    examples: [old_OpenClaw_paths, old_local_paths, old_agent_role_roster, old_model_or_provider_claims]
    default_trust: low_for_current_runtime_authority
  unverified_claim:
    examples: [memory_based_statement, filename_inference, plausible_AI_synthesis_without_source_pointer]
    default_trust: low
  operator_decision:
    examples: [approval_phrase, scope_expansion, explicit_override]
    default_trust: binding_within_stated_scope
```

## Procedure

1. Define the artifact or decision under review, requested action, stakes, affected surfaces, and explicit operator constraints.
2. Build a source ledger with source name, authority class, read status, relevance, and limits.
3. Check for validator/executor collapse. If the validator is also expected to implement and approve a high-risk fix, stop or route.
4. Scan for these anti-patterns: approval by fluency, summary elevation, advisory routing collapse, path drift, candidate-as-canon, old-runtime-authority import, unsupported current claims.
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
  key_findings:
    - ""
  evidence_gaps:
    - "NONE | "
  risks:
    - "NONE | "
  stop_conditions:
    - "NONE | "
  required_operator_decisions:
    - "NONE | "
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

## Verdict semantics

```yaml
PASS: "Evidence is sufficient, authority is clear, and no blocking gaps or operator decisions remain."
PASS_WITH_WARNINGS: "Artifact is usable, but limits or risks must be carried into the next step."
NEEDS_OPERATOR_DECISION: "Evidence is sufficient but a human authority choice is required before proceeding."
FAIL: "Required sources are missing, claims are unsupported, authority is inverted, or high-risk validation/execution is collapsed."
```

## Repo-affecting work addendum

For repo-affecting work, require or produce this route contract before execution:

```yaml
repo_route_contract:
  repository: ""
  branch: ""
  exact_target_paths: []
  operation_class: "create | update | delete | rename | generated_output | config_change"
  allowed_actions: []
  forbidden_actions: []
  pre_write_checks: []
  post_write_checks: []
  stop_conditions: []
  commit_strategy: "direct_main | short_lived_branch | no_commit | operator_decision"
```

If the route contract is missing for medium/high-risk repo work, return `NEEDS_OPERATOR_DECISION` or `FAIL` rather than approving execution.

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
