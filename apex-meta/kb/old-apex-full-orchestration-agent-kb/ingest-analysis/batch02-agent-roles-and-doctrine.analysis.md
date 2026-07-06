---
title: "Rerun Batch 02 — Agent Roles and Doctrine"
page_type: ingest_analysis
kb_slug: old-apex-full-orchestration-agent-kb
phase: ingest_phase_1_rerun
status: operator_gate_already_approved_for_rerun
created_at: "2026-07-06T22:45:00+02:00"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: high
claim_label: source_grounded_analysis
phase_2_allowed: true
phase_2_approval_phrase: "approve ingest"
---

# Rerun Batch 02 — Agent Roles and Doctrine

## source_scope

This replacement Phase 1 batch extracts the old agent role model as a role-boundary and authority-separation system. It distinguishes persistent roles, specialist lanes, validator-like roles, executor-like roles, and internal modes.

## files_read

```yaml
files_read:
  root_map:
    - path: sources/primary/managed-agent-kb/AGENT_KB_INDEX.md
      pointer: "Agent KB root map; Working surface pointers"
  role_essence_files:
    - path: sources/primary/managed-agent-kb/alfred/ESSENCE.md
      pointer: "operator-facing intake and route-brief lane"
    - path: sources/primary/managed-agent-kb/meta_ops/ESSENCE.md
      pointer: "orchestration, specialist activation, sequencing, execution control"
    - path: sources/primary/managed-agent-kb/meta_strategy/ESSENCE.md
      pointer: "option framing, timing, leverage, recommendation packets"
    - path: sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
      pointer: "adversarial validation and non-execution boundary"
    - path: sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
      pointer: "advisory model/tool/repo routing lane"
    - path: sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
      pointer: "structural QA, pointer integrity, closure evidence"
  accepted_appendices:
    - path: sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
      pointer: "mode map, verdict definitions, confidence definitions, standard validation flow"
```

## source_grounded_claims

```yaml
claims:
  - id: A02-C001
    claim: "The first-wave role set is explicitly indexed and includes Alfred, Meta Ops, Meta Strategy, Meta Detective, Knowledge Bank, Informatics Design, Prompts Workflows, AI Handling Routing, and Hygiene Clean."
    source_pointer: "AGENT_KB_INDEX.md / Agent KB root map"
    confidence: high
    claim_label: raw_source

  - id: A02-C002
    claim: "Alfred owns operator-facing intake, constraint capture, route-brief framing, user-facing synthesis before orchestration, and ambiguity clarification."
    source_pointer: "alfred/ESSENCE.md / Owns"
    confidence: high
    claim_label: raw_source

  - id: A02-C003
    claim: "Meta Ops owns bounded orchestration, specialist activation, sequencing, bounded synthesis, validator routing, and execution control."
    source_pointer: "meta_ops/ESSENCE.md / Owns"
    confidence: high
    claim_label: raw_source

  - id: A02-C004
    claim: "Meta Strategy owns recommendation logic but explicitly does not own execution control, direct implementation, direct promotion, operator override, or config authority."
    source_pointer: "meta_strategy/ESSENCE.md / Owns and Does not own"
    confidence: high
    claim_label: raw_source

  - id: A02-C005
    claim: "Meta Detective validates and challenges; it does not execute, patch, directly implement, mutate accepted truth, or self-validate as final approval."
    source_pointer: "meta_detective/ESSENCE.md / Agent boundary, Does not own, Core constraints"
    confidence: high
    claim_label: raw_source

  - id: A02-C006
    claim: "Meta Detective internal modes are selected validation lenses inside one validator role, not separate managed agents or separate KB roots."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Status and Doctrine statement"
    confidence: high
    claim_label: raw_source

  - id: A02-C007
    claim: "Special Ops AI Handling Routing gives advisory source-authority, model/tool, execution-surface, fallback, and escalation routing guidance, but does not mutate runtime config or provider policy."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md / Agent boundary, Owns, Does not own"
    confidence: high
    claim_label: raw_source

  - id: A02-C008
    claim: "Special Ops Hygiene Clean owns structural QA, pointer/dependency/source-integrity checks, stale-state checks, closure evidence, and drift detection, but not accepted-truth mutation or promotion approval."
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md / Owns and Does not own"
    confidence: high
    claim_label: raw_source

  - id: A02-C009
    claim: "Negative ownership boundaries are load-bearing doctrine; the system preserves what each role must not own to prevent authority creep."
    source_pointer: "all role ESSENCE files / Does not own sections"
    confidence: high
    claim_label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: persistent-agent-role
    label: "Persistent agent role"
    definition: "A durable named lane with a KB root, compact boundary doctrine, owner, validator, and explicit non-ownership."
    source_pointer: "AGENT_KB_INDEX.md / Agent KB root map"
    phase2_value: high

  - slug: internal-mode-not-agent
    label: "Internal mode, not agent"
    definition: "A reusable operating lens inside one role that does not justify a separate permanent agent or KB root by itself."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md"
    phase2_value: high

  - slug: negative-ownership-boundary
    label: "Negative ownership boundary"
    definition: "A does-not-own list that prevents role drift, config overreach, self-validation, and accidental mutation authority."
    source_pointer: "role ESSENCE files"
    phase2_value: high

  - slug: validator-executor-separation
    label: "Validator/executor separation"
    definition: "A validator checks and routes defects but does not become the executor of the fix."
    source_pointer: "meta_detective/ESSENCE.md; meta_detective/APPENDIX_INTERNAL_MODES.md"
    phase2_value: high

  - slug: routing-specialist-lane
    label: "Routing specialist lane"
    definition: "A bounded advisor for source-authority, model/tool, execution-surface, fallback, and escalation routing, without config authority."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md"
    phase2_value: high
```

## entities_extracted

```yaml
entities_extracted:
  - id: alfred
    type: persistent_agent_role
    owns: [operator_intake, constraint_capture, route_brief_framing]
    does_not_own: [execution_control, final_strategy, adversarial_validation, config_mutation]
    source_pointer: "alfred/ESSENCE.md"

  - id: meta_ops
    type: persistent_agent_role
    owns: [orchestration, specialist_activation, sequencing, bounded_synthesis, execution_control]
    does_not_own: [adversarial_validation, direct_canon_mutation, final_strategy, config_authority]
    source_pointer: "meta_ops/ESSENCE.md"

  - id: meta_strategy
    type: persistent_agent_role
    owns: [option_framing, scenario_comparison, timing_analysis, leverage_analysis, recommendation_packets]
    does_not_own: [execution_control, implementation, direct_promotion, config_authority]
    source_pointer: "meta_strategy/ESSENCE.md"

  - id: meta_detective
    type: persistent_validator_role
    owns: [source_authority_challenge, contradiction_surfacing, boundary_challenge, risk_review, verdict_packets]
    does_not_own: [execution, patch_application, direct_implementation, direct_promotion]
    source_pointer: "meta_detective/ESSENCE.md"

  - id: meta_detective_internal_modes
    type: internal_mode_pack
    members: [evidence_source_verifier, contradiction_logic_auditor, boundary_authority_guardian, risk_failure_mode_red_teamer, verdict_escalation_synthesizer]
    current_authority: accepted_appendix_doctrine
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Mode map"

  - id: special_ops__ai_handling_routing
    type: routing_specialist_lane
    owns: [advisory_routing, source_authority_routing_checks, repo_execution_vs_chat_routing_checks]
    does_not_own: [runtime_config_mutation, provider_policy_authority, final_approval]
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md"

  - id: special_ops__hygiene_clean
    type: structural_validator_lane
    owns: [structural_QA, pointer_integrity, stale_state_checks, closure_evidence]
    does_not_own: [truth_mutation, promotion_approval, strategy_authority, config_authority]
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: A02-T001
    tension: "Meta Ops owns execution control in the historical role system, but current Apex KB semantic work must not mutate execution surfaces unless separately routed."
    disposition: "Preserve role doctrine as historical pattern; enforce Apex KB boundary for this rerun."
    confidence: high

  - id: A02-T002
    tension: "Internal modes are valuable and specialized, but treating every mode as a persistent agent would contradict their accepted non-agent status."
    disposition: "Compile as entity/concept doctrine, not as current subagent implementation."
    confidence: high
```

## open_questions

```yaml
open_questions:
  - id: A02-Q001
    question: "Which old roles should remain only entities in this KB, and which patterns should influence future Apex-native skills or workflows?"
    blocker: false
  - id: A02-Q002
    question: "Should validator internal modes become checklists, subagents, prompt modules, or remain wiki doctrine only?"
    blocker: false
```

## proposed_phase_2_wiki_targets

```yaml
summaries:
  - old-agent-role-system
concepts:
  - validation-and-routing-guardrails
  - agent-doctrine-and-promotion-patterns
entities:
  - old-agent-roles
  - meta-detective-internal-modes
```

## phase_gate_statement

```yaml
phase_2_gate:
  required_phrase: approve ingest
  status_for_this_rerun: approved
```
