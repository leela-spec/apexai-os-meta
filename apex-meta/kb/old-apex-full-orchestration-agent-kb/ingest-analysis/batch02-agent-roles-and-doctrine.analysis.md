# Batch 02 — Agent Roles and Doctrine

## source_scope

This batch extracts old Apex agent roles, doctrine boundaries, ownership exclusions, and role classes from the managed agent KB corpus. It focuses on role definition rather than implementation.

## source_files_read

```yaml
source_files_read:
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/AGENT_KB_INDEX.md
    reason: first-wave agent role map, default owner/validator table, working-surface pointers
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/alfred/ESSENCE.md
    reason: operator-facing intake role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_ops/ESSENCE.md
    reason: orchestration and execution-control role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_strategy/ESSENCE.md
    reason: strategy/recommendation role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
    reason: adversarial validator role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
    reason: validator internal modes and non-agent boundary
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
    reason: advisory routing specialist role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__knowledge_bank/ESSENCE.md
    reason: KB lifecycle and placement specialist role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
    reason: structural QA and hygiene validator role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__informatics_design/ESSENCE.md
    reason: information architecture specialist role
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__prompts_workflows/ESSENCE.md
    reason: reusable prompt/workflow specialist role
```

## source_grounded_claims

```yaml
claims:
  - id: C001
    text: "The first-wave role set is explicitly indexed and includes Alfred, Meta Ops, Meta Strategy, Meta Detective, Knowledge Bank, Informatics Design, Prompts Workflows, AI Handling Routing, and Hygiene Clean."
    source: "AGENT_KB_INDEX.md / Agent KB root map"
    confidence: high
    label: raw_source

  - id: C002
    text: "Alfred is an operator-facing intake, alignment, and route-brief lane that frames tasks for the wider system and hands bounded work onward."
    source: "alfred/ESSENCE.md / Agent boundary and Owns"
    confidence: high
    label: raw_source

  - id: C003
    text: "Meta Ops is the bounded orchestration and activation lane; it sequences work, activates the smallest useful specialist set, integrates outputs, and owns execution control."
    source: "meta_ops/ESSENCE.md / Agent boundary and Owns"
    confidence: high
    label: raw_source

  - id: C004
    text: "Meta Strategy owns option framing, scenarios, timing, leverage analysis, and recommendation packets, but not execution control or direct implementation."
    source: "meta_strategy/ESSENCE.md / Agent boundary, Owns, Does not own"
    confidence: high
    label: raw_source

  - id: C005
    text: "Meta Detective is an adversarial validation lane that validates and challenges but does not execute, apply patches, mutate accepted truth, or promote its own learning."
    source: "meta_detective/ESSENCE.md / Agent boundary, Owns, Does not own, Core constraints"
    confidence: high
    label: raw_source

  - id: C006
    text: "Meta Detective's internal modes are selection lenses inside one validator agent, not separate agents, separate KB roots, or runtime entities."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Purpose, Status, Doctrine statement"
    confidence: high
    label: raw_source

  - id: C007
    text: "Special Ops AI Handling Routing owns advisory model/tool and execution-surface routing posture, but not runtime config mutation, provider-policy authority, all-agent orchestration, or final approval."
    source: "special_ops__ai_handling_routing/ESSENCE.md / Agent boundary, Owns, Does not own"
    confidence: high
    label: raw_source

  - id: C008
    text: "Special Ops Knowledge Bank owns KB placement, lifecycle routing, source manifesting, candidate packaging, appendix architecture, and knowledge coherence; it does not own final strategy, direct promotion approval, or adversarial validation."
    source: "special_ops__knowledge_bank/ESSENCE.md / Agent boundary, Owns, Does not own"
    confidence: high
    label: raw_source

  - id: C009
    text: "Special Ops Hygiene Clean owns structural QA, pointer/source integrity, stale-state checks, closure evidence, and drift detection, but not accepted-truth mutation or promotion approval."
    source: "special_ops__hygiene_clean/ESSENCE.md / Agent boundary, Owns, Does not own"
    confidence: high
    label: raw_source

  - id: C010
    text: "Special Ops Informatics Design owns information architecture, taxonomy, terminology stability, chunking, appendix design, retrieval clarity, and cold-start usability, but not domain truth validation or promotion approval."
    source: "special_ops__informatics_design/ESSENCE.md / Agent boundary"
    confidence: high
    label: raw_source

  - id: C011
    text: "Special Ops Prompts Workflows owns reusable prompt structures, workflow-stage patterns, bounded execution sequences, promptflow skeletons, and handoff templates, but not orchestration, model/config routing, KB placement, or promotion authority."
    source: "special_ops__prompts_workflows/ESSENCE.md / Agent boundary, Owns, Does not own"
    confidence: high
    label: raw_source

  - id: C012
    text: "The old role system repeatedly defines negative ownership boundaries; those exclusions are as important as the role's positive capabilities."
    source: "all ESSENCE.md files read / Does not own sections"
    confidence: high
    label: source_backed_summary

  - id: C013
    text: "Persistent roles are expected to have durable KB roots, while internal modes can remain within an accepted appendix and should not automatically become more permanent agents."
    source: "AGENT_KB_INDEX.md / Agent KB root map and Working surface pointers; meta_detective/APPENDIX_INTERNAL_MODES.md / not_a_separate_agent and Doctrine statement"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: persistent-agent-role
    label: "Persistent agent role"
    definition: "A durable role with a managed KB root, compact seed/boundary doctrine, owner, and validator."
    source: "AGENT_KB_INDEX.md / Agent KB root map"
    phase2_value: high

  - slug: internal-mode-not-agent
    label: "Internal mode, not agent"
    definition: "A reusable validation or operating lens inside one role, preserved in appendix doctrine without separate runtime identity."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Doctrine statement"
    phase2_value: high

  - slug: negative-ownership-boundary
    label: "Negative ownership boundary"
    definition: "A role's explicit does-not-own list, used to prevent role drift and authority creep."
    source: "role ESSENCE files / Does not own sections"
    phase2_value: high

  - slug: validator-like-role
    label: "Validator-like role"
    definition: "A role that checks source authority, evidence, structure, drift, contradiction, or closure safety without owning the execution fix."
    source: "meta_detective/ESSENCE.md; special_ops__hygiene_clean/ESSENCE.md"
    phase2_value: high

  - slug: executor-like-role
    label: "Executor-like role"
    definition: "A role that sequences or controls execution but must be bounded by validators and explicit authority surfaces."
    source: "meta_ops/ESSENCE.md"
    phase2_value: medium

  - slug: specialist-lane
    label: "Specialist lane"
    definition: "A bounded capability lane such as KB lifecycle, information architecture, prompts/workflows, routing, or hygiene."
    source: "special_ops__knowledge_bank/ESSENCE.md; special_ops__informatics_design/ESSENCE.md; special_ops__prompts_workflows/ESSENCE.md; special_ops__ai_handling_routing/ESSENCE.md"
    phase2_value: high
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - id: alfred
    classification: [persistent, routing_like, intake_like]
    owns: [operator_intake, constraint_capture, bounded_handoff_framing]
    not_owns: [execution_control, final_strategy, adversarial_validation, config_mutation]
    validator: meta_ops
    source: "alfred/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: meta_ops
    classification: [persistent, executor_like, orchestration_like]
    owns: [orchestration, specialist_activation, sequencing, bounded_synthesis, execution_control]
    not_owns: [final_strategy, adversarial_validation, direct_canon_mutation, config_authority]
    validator: meta_detective
    source: "meta_ops/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: meta_strategy
    classification: [persistent, strategy_like, recommendation_like]
    owns: [option_framing, scenario_comparison, timing_analysis, leverage_analysis, recommendation_packets]
    not_owns: [execution_control, implementation, direct_promotion, config_authority]
    validator: meta_detective
    source: "meta_strategy/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: meta_detective
    classification: [persistent, validator_like, adversarial_reviewer]
    owns: [source_authority_challenge, contradiction_surfacing, assumption_pressure, drift_challenge, risk_review, verdict_packets]
    not_owns: [execution, patch_application, direct_promotion, self_validation_as_final_approval]
    validator: special_ops__hygiene_clean
    source: "meta_detective/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: evidence_source_verifier
    classification: [internal_mode, validator_lens]
    owns: [source_authority_classification, evidence_sufficiency_review, source_candidate_canon_status_check]
    not_owns: [strategy_choice, patching, KB_placement]
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Mode map and doctrine sections"

  - id: contradiction_logic_auditor
    classification: [internal_mode, validator_lens]
    owns: [contradiction_detection, inference_jump_review, unsupported_claim_surfacing]
    not_owns: [rewriting_artifact, strategy_choice, patches]
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Mode map and doctrine sections"

  - id: boundary_authority_guardian
    classification: [internal_mode, validator_lens]
    owns: [role_boundary_drift_detection, promotion_safety_pressure, validator_executor_separation]
    not_owns: [orchestration_control, KB_placement_ownership, structural_cleanup_execution]
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Mode map and doctrine sections"

  - id: risk_failure_mode_red_teamer
    classification: [internal_mode, validator_lens]
    owns: [premortem_challenge, base_rate_challenge, reversibility_review, falsification_test_design]
    not_owns: [mitigation_execution, project_management, final_strategy]
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Risk & Failure-Mode Red Teamer doctrine"

  - id: verdict_escalation_synthesizer
    classification: [internal_mode, verdict_lens]
    owns: [verdict_synthesis, confidence_consolidation, evidence_gap_statement, escalation_recommendation]
    not_owns: [implementing_fix, applying_patch, promoting_KB_candidates]
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Verdict & Escalation Synthesizer doctrine"

  - id: special_ops__knowledge_bank
    classification: [persistent, specialist_like, kb_lifecycle_like]
    owns: [source_manifesting, candidate_ledgering, appendix_architecture, KB_lifecycle_routing]
    not_owns: [final_strategy, promotion_approval, config_mutation]
    validator: special_ops__informatics_design
    source: "special_ops__knowledge_bank/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: special_ops__informatics_design
    classification: [persistent, specialist_like, structure_like]
    owns: [taxonomy, terminology_stability, chunking, retrieval_clarity]
    not_owns: [domain_truth_validation, promotion_approval, orchestration_control]
    validator: special_ops__hygiene_clean
    source: "special_ops__informatics_design/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: special_ops__hygiene_clean
    classification: [persistent, validator_like, structural_QA_like]
    owns: [structural_QA, pointer_integrity, stale_state_checks, closure_safety]
    not_owns: [truth_mutation, promotion_approval, strategy_authority]
    validator: meta_detective
    source: "special_ops__hygiene_clean/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: special_ops__prompts_workflows
    classification: [persistent, specialist_like, workflow_like]
    owns: [prompt_structures, workflow_stage_patterns, handoff_templates, anti_drift_promptflows]
    not_owns: [orchestration_authority, model_config_routing, KB_placement, promotion_approval]
    validator: meta_ops
    source: "special_ops__prompts_workflows/ESSENCE.md; AGENT_KB_INDEX.md"

  - id: special_ops__ai_handling_routing
    classification: [persistent, specialist_like, routing_like]
    owns: [model_tool_selection_posture, source_authority_routing, handoff_readiness, fallback_path_suggestions]
    not_owns: [runtime_config_mutation, provider_policy, all_agent_orchestration, final_approval]
    validator: meta_ops
    source: "special_ops__ai_handling_routing/ESSENCE.md; AGENT_KB_INDEX.md"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "Meta Ops owns execution control, but must not self-validate high-impact output; this creates an intended control-plane tension between execution and validation."
    source: "meta_ops/ESSENCE.md / Owns and Core constraints; meta_detective/ESSENCE.md / Validator relationship"
    confidence: high
    label: source_backed_summary

  - id: T002
    text: "Meta Detective has several strong internal modes, but the appendix explicitly forbids turning them into separate agents or KB roots."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Status and Doctrine statement"
    confidence: high
    label: raw_source

  - id: T003
    text: "Hygiene Clean and Meta Detective both detect drift, but Hygiene owns structural QA and closure safety while Detective owns adversarial truth, evidence, contradiction, and risk challenge."
    source: "meta_detective/ESSENCE.md / Detective to Hygiene boundary; special_ops__hygiene_clean/ESSENCE.md / Agent boundary and Owns"
    confidence: high
    label: source_backed_summary

  - id: T004
    text: "Special Ops AI Handling Routing can recommend routing posture but must stop before runtime config or provider-policy authority."
    source: "special_ops__ai_handling_routing/ESSENCE.md / Does not own and Core doctrine"
    confidence: high
    label: raw_source

  - id: T005
    text: "Role names are old-system/OpenClaw-specific and should be migrated as patterns unless the operator explicitly chooses to preserve the exact old taxonomy."
    source: "AGENT_KB_INDEX.md; all ESSENCE files read"
    confidence: medium
    label: working_hypothesis
```

## migration_notes

```yaml
migration_notes:
  preserve:
    - "Durable role pages should encode owns, does-not-own, read triggers, core constraints, owner, validator, and review_due."
    - "Internal modes should be preserved as mode doctrine, not automatically expanded into agent sprawl."
    - "Executor-like roles require validator-like roles and explicit stop conditions."
    - "Specialist lanes should remain bounded by negative ownership clauses."
  adapt:
    - "Map role boundaries to Claude-native skills, subagents, workflows, scripts, and operator gates based on function rather than old role names."
    - "Use Meta Detective's internal mode system as a general validator-design pattern for future Apex/Claude-native workflows."
    - "Use AI Handling Routing's advisory boundary as a pattern for tool/model routing, not as runtime config authority."
  deprecate_or_handle_carefully:
    - "Expanding every useful validation lens into a permanent agent."
    - "Treating a validator's proposed fix as self-approved execution."
    - "Importing old OpenClaw runtime authority surfaces into current Apex without operator decision."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - old-agent-role-system
    - validator-executor-specialist-boundaries
  concepts:
    - persistent-agent-role
    - internal-mode-not-agent
    - negative-ownership-boundary
    - validator-like-role
    - executor-like-role
    - specialist-lane
    - advisory-routing-boundary
  entities:
    - alfred
    - meta-ops
    - meta-strategy
    - meta-detective
    - evidence-source-verifier
    - contradiction-logic-auditor
    - boundary-authority-guardian
    - risk-failure-mode-red-teamer
    - verdict-escalation-synthesizer
    - special-ops-knowledge-bank
    - special-ops-informatics-design
    - special-ops-hygiene-clean
    - special-ops-prompts-workflows
    - special-ops-ai-handling-routing
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
