# Batch 03 — Handoffs, Validation, and Risk

## source_scope

This batch analyzes how the old system controls handoffs, validation, risk, contradiction, source authority, failure loops, and boundary drift. The highest-signal sources are Meta Detective, AI Handling Routing, Hygiene Clean, and Prompts Workflows doctrine.

## source_files_read

```yaml
source_files_read:
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
    reason: adversarial validation boundary and route-to-owner rules
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/BEST_PRACTICES.md
    reason: accepted validation practices and stop conditions
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/MISTAKES.md
    reason: recurring validation failure patterns and countermeasures
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/TEMPLATES.md
    reason: validation verdict, contradiction, boundary, risk, and handoff packet shapes
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/LEARNING_QUEUE.md
    reason: candidate capture and promotion route
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
    reason: internal validation mode flow and handoff map
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
    reason: advisory route states, source authority, and escalation posture
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/BEST_PRACTICES.md
    reason: routing objective freeze, source authority, execution-surface separation
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/MISTAKES.md
    reason: routing failure patterns, verification theater, path drift, config overreach
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/TEMPLATES.md
    reason: routing decision, source authority, repo execution, and handoff templates
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
    reason: structural QA, pointer integrity, stale-state, and closure safety
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__prompts_workflows/ESSENCE.md
    reason: target-first, stage-gated, verify-before-trust prompt/workflow doctrine
```

## source_grounded_claims

```yaml
claims:
  - id: C001
    text: "The old system treats source authority classification as a pre-step gate before verification, handoff, or approval."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-001; special_ops__ai_handling_routing/BEST_PRACTICES.md / AIHR-BP-003; special_ops__ai_handling_routing/ESSENCE.md / Core doctrine"
    confidence: high
    label: source_backed_summary

  - id: C002
    text: "Approval by fluency is an explicit failure pattern: structured or polished output is not enough without concrete evidence, read-back, diff, source check, test, schema, or acceptance criterion."
    source: "meta_detective/MISTAKES.md / DET-MIS-001; special_ops__ai_handling_routing/MISTAKES.md / AIHR-MISTAKE-003"
    confidence: high
    label: source_backed_summary

  - id: C003
    text: "Meta Detective must return verdicts and escalation recommendations without implementing the fix under review."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-004; meta_detective/MISTAKES.md / DET-MIS-004; meta_detective/APPENDIX_INTERNAL_MODES.md / Non-drift rules"
    confidence: high
    label: source_backed_summary

  - id: C004
    text: "Substantial validation should end with a verdict, evidence gap, stop condition, and next owner/validator route."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-010; meta_detective/TEMPLATES.md / DET-TPL-002; meta_detective/APPENDIX_INTERNAL_MODES.md / Standard validation flow"
    confidence: high
    label: source_backed_summary

  - id: C005
    text: "The old validation flow uses explicit verdict states: pass, revise, hold, needs_input, and escalate."
    source: "meta_detective/ESSENCE.md / Default verdicts; meta_detective/APPENDIX_INTERNAL_MODES.md / Verdict definitions"
    confidence: high
    label: raw_source

  - id: C006
    text: "The old validation flow uses confidence tiers VERIFIED, PROBABLE, WEAK, and UNSAFE for evidence-dependent claims."
    source: "meta_detective/ESSENCE.md / Core constraints; meta_detective/APPENDIX_INTERNAL_MODES.md / Confidence definitions; special_ops__ai_handling_routing/ESSENCE.md / Minimal routing card"
    confidence: high
    label: raw_source

  - id: C007
    text: "Meta Detective internal modes route different finding types to different owners rather than treating all issues as generic critique."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Mode selection rule and Handoff map"
    confidence: high
    label: source_backed_summary

  - id: C008
    text: "Hygiene Clean owns structural QA, pointer integrity, stale-state, cleanup-risk validation, and closure safety, while Meta Detective owns adversarial source/evidence/contradiction/risk pressure."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Non-drift rules and Handoff map; special_ops__hygiene_clean/ESSENCE.md / Agent boundary and Owns"
    confidence: high
    label: source_backed_summary

  - id: C009
    text: "The old routing doctrine requires freezing task, non-task, target output, source authority, constraints, stop conditions, and validator before choosing a route or handoff."
    source: "special_ops__ai_handling_routing/ESSENCE.md / Core doctrine and Minimal routing card; special_ops__ai_handling_routing/TEMPLATES.md / routing_decision_card"
    confidence: high
    label: source_backed_summary

  - id: C010
    text: "Repo-affecting work requires exact repo-relative paths, operation class, target files, allowed/forbidden actions, pre-write checks, post-write checks, and commit strategy."
    source: "special_ops__ai_handling_routing/BEST_PRACTICES.md / AIHR-BP-005 and AIHR-BP-006; special_ops__ai_handling_routing/TEMPLATES.md / AIHR-TPL-004 Repo execution router"
    confidence: high
    label: source_backed_summary

  - id: C011
    text: "Advisory routing must stop for manual or governance review if it touches runtime config, provider policy, model registry, permissions, or config authority."
    source: "special_ops__ai_handling_routing/ESSENCE.md / Does not own and Core doctrine; special_ops__ai_handling_routing/BEST_PRACTICES.md / AIHR-BP-008; special_ops__ai_handling_routing/MISTAKES.md / AIHR-MISTAKE-008"
    confidence: high
    label: source_backed_summary

  - id: C012
    text: "Repeated failure and retry loops are explicit risks; on attempt two or later, the system should require meaningful delta or stop/escalate."
    source: "meta_detective/MISTAKES.md / DET-MIS-007"
    confidence: high
    label: raw_source

  - id: C013
    text: "Prompt/workflow doctrine reinforces target-first framing, bounded execution, source lock, stage gates, constant frame control, and verify-before-trust behavior."
    source: "special_ops__prompts_workflows/ESSENCE.md / Core doctrine and Default sequence"
    confidence: high
    label: source_backed_summary

  - id: C014
    text: "Mistakes are captured as accepted failure patterns with trigger conditions, countermeasures, evidence references, scores, owner, validator, and review_due, turning incidents into durable prevention doctrine."
    source: "meta_detective/MISTAKES.md / Entry schema; special_ops__ai_handling_routing/MISTAKES.md / Entry schema"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: source-authority-before-verification
    label: "Source authority before verification"
    definition: "Classify governing source authority before trusting, forwarding, patching, or approving an output."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-001; AIHR-BP-003"
    phase2_value: high

  - slug: verification-verdict-packet
    label: "Verification verdict packet"
    definition: "A bounded validation output containing artifact, modes, evidence checked, findings, verdict, evidence gap, stop condition, owner, validator, and handoff target."
    source: "meta_detective/TEMPLATES.md / DET-TPL-002; meta_detective/APPENDIX_INTERNAL_MODES.md / Verdict & Escalation Synthesizer doctrine"
    phase2_value: high

  - slug: validator-executor-separation
    label: "Validator/executor separation"
    definition: "Validators may identify defects and required routes, but do not implement or self-approve the fix."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-004; meta_detective/MISTAKES.md / DET-MIS-004"
    phase2_value: high

  - slug: routing-decision-card
    label: "Routing decision card"
    definition: "A compact route contract freezing task, non-task, output, source authority, overload class, route surface, mode, constraints, stop conditions, fallback, validator, and confidence."
    source: "special_ops__ai_handling_routing/TEMPLATES.md / AIHR-TPL-001"
    phase2_value: high

  - slug: repo-execution-router
    label: "Repo execution router"
    definition: "A pre-write contract for repo mutation with repo, branch, target root, operation class, target files, allowed/forbidden actions, checks, stop conditions, and commit strategy."
    source: "special_ops__ai_handling_routing/TEMPLATES.md / AIHR-TPL-004"
    phase2_value: high

  - slug: approval-by-fluency
    label: "Approval by fluency"
    definition: "Passing an artifact because it looks coherent or polished without concrete evidence."
    source: "meta_detective/MISTAKES.md / DET-MIS-001"
    phase2_value: high

  - slug: summary-elevation
    label: "Summary elevation"
    definition: "Treating derived summaries, chat recaps, or working notes as stronger than original artifacts."
    source: "meta_detective/MISTAKES.md / DET-MIS-002"
    phase2_value: high

  - slug: advisory-routing-collapse
    label: "Advisory routing collapse"
    definition: "Advisory chat routing becoming repo execution without mode lock, exact paths, or post-write verification."
    source: "special_ops__ai_handling_routing/MISTAKES.md / AIHR-MISTAKE-004"
    phase2_value: high

  - slug: path-drift
    label: "Path drift"
    definition: "Using vague filenames, stale paths, Windows local paths, or guessed repo paths as execution authority."
    source: "special_ops__ai_handling_routing/MISTAKES.md / AIHR-MISTAKE-006"
    phase2_value: high

  - slug: constant-frame-control
    label: "Constant frame control"
    definition: "For high-risk promptflows, carry explicit state, atomic task payload, gate checks, stop signal, and closure proof rather than relying on conversational continuity."
    source: "special_ops__prompts_workflows/ESSENCE.md / Core doctrine"
    phase2_value: medium
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - id: meta_detective
    role_in_validation: "adversarial validator and challenger"
    validation_outputs: [source_evidence_check, contradiction_audit, boundary_verdict, risk_packet, validation_verdict_packet]
    hard_boundary: "does not execute fixes, patch, mutate truth, or self-promote"
    source: "meta_detective/ESSENCE.md; meta_detective/APPENDIX_INTERNAL_MODES.md"

  - id: special_ops__hygiene_clean
    role_in_validation: "structural QA and closure-safety validator"
    validation_outputs: [audit_findings, pointer_integrity_checks, stale_state_checks, closure_evidence_checks]
    hard_boundary: "does not mutate accepted truth or approve promotion"
    source: "special_ops__hygiene_clean/ESSENCE.md"

  - id: special_ops__ai_handling_routing
    role_in_validation: "advisory routing checker"
    validation_outputs: [routing_decision_card, source_authority_card, model_tool_fit_card, repo_execution_router, config_impact_stop_note]
    hard_boundary: "does not mutate runtime config or become final approval authority"
    source: "special_ops__ai_handling_routing/ESSENCE.md; special_ops__ai_handling_routing/TEMPLATES.md"

  - id: special_ops__prompts_workflows
    role_in_validation: "promptflow and handoff pattern builder"
    validation_outputs: [target_first_prompts, staged_source_lock_promptflows, handoff_templates]
    hard_boundary: "templates do not create runtime authority"
    source: "special_ops__prompts_workflows/ESSENCE.md"

  - id: meta_ops
    role_in_validation: "execution/orchestration owner that receives execution implications and owner ambiguity returns"
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Handoff map; meta_ops/ESSENCE.md"

  - id: meta_strategy
    role_in_validation: "recommendation owner that receives strategy revisions, options, scenarios, timing, and leverage returns"
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Handoff map; meta_strategy/ESSENCE.md"

  - id: special_ops__knowledge_bank
    role_in_validation: "KB placement and promotion-lifecycle owner"
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Handoff map; special_ops__knowledge_bank/ESSENCE.md"

  - id: special_ops__informatics_design
    role_in_validation: "taxonomy, file-shape, information-structure owner"
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Handoff map; special_ops__informatics_design/ESSENCE.md"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "The system needs validators to identify fixes, but the same doctrine forbids validators from implementing those fixes; Phase 2 should preserve the distinction between correction recommendation and correction execution."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-004; meta_detective/MISTAKES.md / DET-MIS-004"
    confidence: high
    label: source_backed_summary

  - id: T002
    text: "Routing doctrine supports repo execution only after explicit route contract, but the presence of write tools can tempt advisory work to collapse into execution."
    source: "special_ops__ai_handling_routing/MISTAKES.md / AIHR-MISTAKE-004; special_ops__ai_handling_routing/TEMPLATES.md / Repo execution router"
    confidence: high
    label: source_backed_summary

  - id: T003
    text: "Source authority doctrine requires primary-source checking, but Phase 1 itself is sampled; any Phase 2 compiled pages must preserve source-read scope and unresolved coverage limits."
    source: "Phase 1 execution scope and source_files_read in this batch; meta_detective/BEST_PRACTICES.md / DET-BP-001"
    confidence: medium
    label: operator_question

  - id: T004
    text: "AI Handling Routing uses EVD/IMP/RSK scores in 1-5 examples, while Meta Detective and several later files insist on 1-100 scoring; this should be normalized or explicitly scoped in Phase 2."
    source: "special_ops__ai_handling_routing/BEST_PRACTICES.md / Accepted practices use 5-point scores; meta_detective/BEST_PRACTICES.md / Score convention"
    confidence: high
    label: source_backed_summary

  - id: T005
    text: "Hygiene and Detective both address drift, but their drift domains are different. Merging them would hide whether a finding is structural, adversarial, or mixed."
    source: "meta_detective/BEST_PRACTICES.md / DET-BP-009; special_ops__hygiene_clean/ESSENCE.md / Routing boundary summary"
    confidence: high
    label: source_backed_summary
```

## migration_notes

```yaml
migration_notes:
  preserve:
    - "Source authority before verification as a hard query and execution pre-step."
    - "Verification verdict packets for high-risk outputs, handoffs, KB promotions, and repo writes."
    - "Verdict/confidence vocabulary: pass/revise/hold/needs_input/escalate and VERIFIED/PROBABLE/WEAK/UNSAFE."
    - "Routing cards and repo execution routers for any repo-affecting work."
    - "Failure-pattern files as anti-regression doctrine."
  adapt:
    - "Convert old handoff cards into Claude-native workflow/skill/operator-gate templates."
    - "Represent validator modes as callable checklists or sub-processes, not necessarily permanent agents."
    - "Use Hygiene Clean doctrine to design deterministic lint/audit checks in Apex KB where possible."
  deprecate_or_handle_carefully:
    - "Any route that asks a validator to patch and approve the same artifact."
    - "Any write path that relies on local Windows paths instead of repo-relative paths."
    - "Any current model/provider/cost claim preserved without current verification."
    - "Mixed 1-5 and 1-100 score scales without normalization."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - handoff-validation-and-risk-doctrine
    - routing-and-repo-execution-safety
  concepts:
    - source-authority-before-verification
    - verification-verdict-packet
    - validator-executor-separation
    - routing-decision-card
    - repo-execution-router
    - approval-by-fluency
    - summary-elevation
    - advisory-routing-collapse
    - path-drift
    - constant-frame-control
  entities:
    - meta-detective
    - special-ops-hygiene-clean
    - special-ops-ai-handling-routing
    - special-ops-prompts-workflows
    - meta-ops
    - meta-strategy
    - special-ops-knowledge-bank
    - special-ops-informatics-design
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
