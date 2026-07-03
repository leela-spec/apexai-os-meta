# Batch 04 — Reusable Patterns and Migration

## source_scope

This batch extracts reusable design patterns from the old Apex full orchestration agent KB and classifies them for current Apex/Claude-native migration. It distinguishes patterns worth preserving from old-system details that should remain historical evidence rather than binding current architecture.

## source_files_read

```yaml
source_files_read:
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/AGENT_KB_INDEX.md
    reason: role root map, scaffold convention, working-surface boundaries
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
    reason: adversarial validator boundary and route discipline
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/BEST_PRACTICES.md
    reason: accepted validation practices and promotion discipline
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/MISTAKES.md
    reason: reusable failure patterns
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/TEMPLATES.md
    reason: reusable validation templates
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/LEARNING_QUEUE.md
    reason: candidate lifecycle and promotion route
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
    reason: internal-mode doctrine and non-sprawl pattern
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__knowledge_bank/ESSENCE.md
    reason: KB placement, lifecycle routing, appendix-first architecture
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__informatics_design/ESSENCE.md
    reason: chunking, taxonomy, retrieval clarity, information design
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
    reason: structural QA and anti-drift guardrails
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__prompts_workflows/ESSENCE.md
    reason: target-first, bounded execution, stage-gated prompt/workflow pattern
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
    reason: advisory routing boundary and route states
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/BEST_PRACTICES.md
    reason: routing practices for repo execution and current verification
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/MISTAKES.md
    reason: routing mistakes and countermeasures
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/TEMPLATES.md
    reason: routing decision card, source authority card, repo execution router, handoff note
```

## source_grounded_claims

```yaml
claims:
  - id: C001
    text: "The most reusable old-system pattern is not the exact agent roster but the durable role-boundary file pattern: compact ESSENCE, accepted practices, accepted mistakes, reusable templates, and candidate-only learning."
    source: "AGENT_KB_INDEX.md / Scaffold convention; all scaffold files read"
    confidence: high
    label: source_backed_summary

  - id: C002
    text: "The old system's anti-sprawl pattern is to keep strong internal modes inside one agent appendix rather than multiplying permanent agents."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Status, Doctrine statement, Non-drift rules"
    confidence: high
    label: source_backed_summary

  - id: C003
    text: "The scaffold/appendix split is directly reusable for Apex KB: compact surfaces should orient agents, while appendices or wiki concept pages carry detailed evidence, ledgers, examples, and QA traces."
    source: "special_ops__knowledge_bank/ESSENCE.md / Operating rule and Required local surfaces; special_ops__informatics_design/ESSENCE.md / Scaffold / appendix split"
    confidence: high
    label: source_backed_summary

  - id: C004
    text: "The old system's source/candidate/canon separation is a reusable safety pattern for Apex KB Phase 1 to Phase 2 gating."
    source: "meta_detective/LEARNING_QUEUE.md / Purpose, Promotion route, Queue safeguards; special_ops__hygiene_clean/ESSENCE.md / Status vocabulary"
    confidence: high
    label: source_backed_summary

  - id: C005
    text: "The old system should not be migrated by copying old OpenClaw runtime paths or config authority; many files explicitly deny config mutation and runtime authority for advisory or validator lanes."
    source: "meta_detective/ESSENCE.md / Does not own; special_ops__ai_handling_routing/ESSENCE.md / Does not own and Core doctrine; special_ops__prompts_workflows/ESSENCE.md / Does not own"
    confidence: high
    label: source_backed_summary

  - id: C006
    text: "Prompt/workflow doctrine is reusable as a workflow or skill pattern because it requires target-first framing, bounded execution, source lock, stage gates, verification, deferred candidate capture, and explicit stop/handoff."
    source: "special_ops__prompts_workflows/ESSENCE.md / Core doctrine and Default sequence"
    confidence: high
    label: source_backed_summary

  - id: C007
    text: "AI Handling Routing's repo execution router is reusable as an operator gate before any connector-backed or local repo write."
    source: "special_ops__ai_handling_routing/TEMPLATES.md / AIHR-TPL-004 Repo execution router"
    confidence: high
    label: source_backed_summary

  - id: C008
    text: "Hygiene Clean's exact-span before rewrite, one-file-before-many, and closure-by-evidence doctrines are reusable as deterministic lint/audit and repo-patching acceptance criteria."
    source: "special_ops__hygiene_clean/ESSENCE.md / Operating doctrine"
    confidence: high
    label: source_backed_summary

  - id: C009
    text: "Informatics Design's rule that content should be small, self-contained, explicitly labeled, and understandable when retrieved in isolation is directly relevant to Apex KB wiki page design and retrieval."
    source: "special_ops__informatics_design/ESSENCE.md / Core rule and Operating priorities"
    confidence: high
    label: source_backed_summary

  - id: C010
    text: "Knowledge Bank's rule to build from source indexes first and keep scaffold files compact maps well to Apex KB's Phase 0 → Phase 1 → Phase 2 lifecycle."
    source: "special_ops__knowledge_bank/ESSENCE.md / Operating rule"
    confidence: high
    label: source_backed_summary

  - id: C011
    text: "Old mistakes such as summary elevation, validator-becomes-executor, candidate-to-canon leakage, advisory routing collapse, path drift, and config-authority overreach should become reusable anti-pattern pages."
    source: "meta_detective/MISTAKES.md; special_ops__ai_handling_routing/MISTAKES.md"
    confidence: high
    label: source_backed_summary

  - id: C012
    text: "Some old-system score conventions are inconsistent: Meta Detective mandates 1-100 EVD/IMP/RSK, while AI Handling Routing examples use 1-5 EVD/IMP/RSK values."
    source: "meta_detective/BEST_PRACTICES.md / Score convention; special_ops__ai_handling_routing/BEST_PRACTICES.md / Accepted practices"
    confidence: high
    label: source_backed_summary

  - id: C013
    text: "Phase 2 should preserve unresolved contradictions and migration questions rather than silently normalizing them into a clean architecture story."
    source: "meta_detective/BEST_PRACTICES.md / source authority and contradiction practices; special_ops__informatics_design/ESSENCE.md / keep unresolved design questions visibly unresolved"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: reusable-agent-doctrine-scaffold
    label: "Reusable agent doctrine scaffold"
    definition: "A five-file doctrine scaffold for durable roles or capability lanes."
    source: "AGENT_KB_INDEX.md / Scaffold convention"
    migration_target: skill_or_kb_page_template
    phase2_value: high

  - slug: anti-agent-sprawl-internal-modes
    label: "Anti-agent-sprawl internal modes"
    definition: "Strong specialized behaviors can exist as internal modes/checklists under one role rather than new permanent agents."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Doctrine statement and Final operating axiom"
    migration_target: workflow_or_subprocess_pattern
    phase2_value: high

  - slug: phase-gated-knowledge-promotion
    label: "Phase-gated knowledge promotion"
    definition: "Candidate material becomes accepted doctrine only through source, owner, validator, scoring, overlap check, and promotion route."
    source: "meta_detective/LEARNING_QUEUE.md / Promotion route; special_ops__knowledge_bank/ESSENCE.md / Core constraints"
    migration_target: operator_gate_and_kb_lifecycle_pattern
    phase2_value: high

  - slug: appendix-first-evidence-architecture
    label: "Appendix-first evidence architecture"
    definition: "Deep evidence and ledgers live in appendices or lower-level pages while compact scaffold pages stay navigational."
    source: "special_ops__knowledge_bank/ESSENCE.md / Required local surfaces; special_ops__informatics_design/ESSENCE.md / Scaffold / appendix split"
    migration_target: kb_page_design_pattern
    phase2_value: high

  - slug: repo-write-preflight-contract
    label: "Repo write preflight contract"
    definition: "Before repo mutation, declare repo, branch, target root, operation class, target files, allowed/forbidden actions, checks, stop conditions, and commit strategy."
    source: "special_ops__ai_handling_routing/TEMPLATES.md / Repo execution router"
    migration_target: operator_gate_or_script_preflight
    phase2_value: high

  - slug: exact-span-before-rewrite
    label: "Exact-span before rewrite"
    definition: "Bounded defects should receive minimal span repair unless rewrite authority is explicit."
    source: "special_ops__hygiene_clean/ESSENCE.md / Operating doctrine; special_ops__ai_handling_routing/BEST_PRACTICES.md / AIHR-BP-006"
    migration_target: deterministic_patch_policy
    phase2_value: high

  - slug: retrieval-isolation-chunking-rule
    label: "Retrieval isolation chunking rule"
    definition: "Knowledge units should be small, self-contained, explicitly labeled, function-typed, and understandable when retrieved alone."
    source: "special_ops__informatics_design/ESSENCE.md / Core rule, Operating priorities, Default rules"
    migration_target: kb_page_and_query_design
    phase2_value: high

  - slug: current-verification-warning
    label: "Current verification warning"
    definition: "Model/provider/cost/performance claims should be marked needs_current_verification unless verified in the current run."
    source: "special_ops__ai_handling_routing/ESSENCE.md / Core doctrine; special_ops__ai_handling_routing/BEST_PRACTICES.md / AIHR-BP-007"
    migration_target: safety_rule_or_operator_gate
    phase2_value: medium

  - slug: constant-frame-control
    label: "Constant frame control"
    definition: "High-risk promptflows should carry explicit state, task payload, gate checks, stop signal, and closure proof across turns."
    source: "special_ops__prompts_workflows/ESSENCE.md / Core doctrine"
    migration_target: workflow_pattern
    phase2_value: high
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - id: old_openclaw_agent_kb_system
    type: historical_system
    migration_status: source_pattern_not_binding_runtime
    source: "AGENT_KB_INDEX.md and source file paths"

  - id: reusable_scaffold_files
    type: artifact_family
    members: [ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md, LEARNING_QUEUE.md]
    migration_status: preserve_as_pattern
    source: "AGENT_KB_INDEX.md / Scaffold convention"

  - id: appendices
    type: artifact_family
    migration_status: preserve_as_deep_evidence_or_concept_layer_pattern
    source: "special_ops__knowledge_bank/ESSENCE.md; special_ops__informatics_design/ESSENCE.md; meta_detective/APPENDIX_INTERNAL_MODES.md"

  - id: learning_queue
    type: artifact_family
    migration_status: preserve_as_candidate_capture_only
    source: "meta_detective/LEARNING_QUEUE.md"

  - id: validation_templates
    type: artifact_family
    migration_status: preserve_as_checklists_or_operator_gates
    source: "meta_detective/TEMPLATES.md; special_ops__ai_handling_routing/TEMPLATES.md"

  - id: failure_patterns
    type: artifact_family
    migration_status: preserve_as_anti_pattern_pages
    source: "meta_detective/MISTAKES.md; special_ops__ai_handling_routing/MISTAKES.md"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "The old role taxonomy is useful evidence but should not automatically become the current Apex/Claude-native permanent agent set."
    source: "AGENT_KB_INDEX.md; all role ESSENCE files read"
    confidence: medium
    label: working_hypothesis

  - id: T002
    text: "Meta Detective uses 1-100 scores as active doctrine, while AI Handling Routing accepted practices use 1-5 scores. Phase 2 should not silently merge these scales."
    source: "meta_detective/BEST_PRACTICES.md / Score convention; special_ops__ai_handling_routing/BEST_PRACTICES.md / Accepted practices"
    confidence: high
    label: source_backed_summary

  - id: T003
    text: "Appendices are useful for evidence and detail, but current Apex KB wiki synthesis should avoid recreating large appendix sprawl without index-first retrieval logic."
    source: "special_ops__knowledge_bank/ESSENCE.md / Operating rule; special_ops__informatics_design/ESSENCE.md / Operating priorities"
    confidence: medium
    label: working_hypothesis

  - id: T004
    text: "Old-source paths refer to OpenClaw and managed agent surfaces; current migration should preserve concepts and doctrine without claiming those old paths still exist as current runtime authority."
    source: "source path patterns across read files"
    confidence: high
    label: source_backed_summary

  - id: T005
    text: "Some patterns could be implemented as skills, workflows, subagents, scripts, or operator gates; Phase 2 should preserve this as an index question, not a prematurely resolved implementation decision."
    source: "special_ops__prompts_workflows/ESSENCE.md; special_ops__ai_handling_routing/TEMPLATES.md; meta_detective/APPENDIX_INTERNAL_MODES.md"
    confidence: medium
    label: operator_question
```

## migration_notes

```yaml
migration_notes:
  should_become_skills:
    - "source-authority-before-verification checklist"
    - "Phase-gated KB promotion and learning-queue handling"
    - "repo write preflight and postflight discipline"
    - "verification verdict packet generator"

  should_become_workflows:
    - "target-first bounded promptflow sequence"
    - "constant frame control for high-risk multi-turn work"
    - "Phase 1 to operator gate to Phase 2 wiki compile"
    - "failure-pattern to countermeasure capture loop"

  should_become_subagents_or_internal_modes_only_when_needed:
    - "Evidence & Source Verifier"
    - "Contradiction & Logic Auditor"
    - "Boundary & Authority Guardian"
    - "Risk & Failure-Mode Red Teamer"
    - "Verdict & Escalation Synthesizer"

  should_become_deterministic_scripts_or_lint_checks:
    - "pointer integrity checks"
    - "stale-state checks"
    - "frontmatter/status vocabulary checks"
    - "source manifest and source path validation"
    - "forbidden write path detection"

  should_become_operator_gates:
    - "approve ingest before Phase 2"
    - "manual review before runtime config/provider/model policy change"
    - "escalation on primary-source conflict"
    - "no self-approval for validator-created fixes"

  should_be_preserved_for_future_phase2_wiki_synthesis:
    - "role boundary pages"
    - "source/candidate/canon separation"
    - "candidate-only learning queue"
    - "scaffold/appendix split"
    - "verification verdict packet"
    - "routing decision card"
    - "repo execution router"
    - "anti-patterns from mistakes files"

  should_be_deprecated_or_not_carried_forward_as_binding:
    - "old OpenClaw-specific runtime paths"
    - "runtime config authority inside advisory lanes"
    - "separate permanent agents for every Meta Detective internal mode"
    - "learning queue material as runtime truth"
    - "legacy local Windows paths as current repo authority"
    - "unverified current model/provider/cost claims"
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - reusable-old-agent-kb-patterns
    - migration-to-claude-native-orchestration
    - deprecated-old-runtime-assumptions
  concepts:
    - reusable-agent-doctrine-scaffold
    - anti-agent-sprawl-internal-modes
    - phase-gated-knowledge-promotion
    - appendix-first-evidence-architecture
    - repo-write-preflight-contract
    - exact-span-before-rewrite
    - retrieval-isolation-chunking-rule
    - current-verification-warning
    - constant-frame-control
  entities:
    - old-openclaw-agent-kb-system
    - reusable-scaffold-files
    - appendices
    - learning-queue
    - validation-templates
    - failure-patterns
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
