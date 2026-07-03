# Batch 01 — Agent KB Architecture

## source_scope

This batch analyzes the old Apex managed agent KB as a durable agent-doctrine architecture: KB root mapping, five-file scaffolds, owner/validator metadata, source/candidate/canon separation, compact activation files, appendix-backed detail, and cross-session behavior preservation.

The run used the mirrored source corpus under:

```text
apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/
```

The original operator-designated source root remains:

```text
ApexDefinition&OldVersions/OldApexFullOrchestrationSystem/managed/agent_kb/
```

## source_files_read

```yaml
source_files_read:
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/AGENT_KB_INDEX.md
    reason: root map and five-file scaffold convention
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/alfred/ESSENCE.md
    reason: example compact agent boundary file
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_ops/ESSENCE.md
    reason: orchestration role boundary
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_strategy/ESSENCE.md
    reason: strategy role boundary
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/ESSENCE.md
    reason: validator role and accepted compact doctrine
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/BEST_PRACTICES.md
    reason: accepted practice schema and promotion discipline
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/LEARNING_QUEUE.md
    reason: candidate-only queue semantics
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md
    reason: accepted appendix doctrine and scaffold/appendix relationship
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__knowledge_bank/ESSENCE.md
    reason: KB placement and lifecycle routing doctrine
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__informatics_design/ESSENCE.md
    reason: structure, taxonomy, chunking, and retrieval-safety doctrine
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__hygiene_clean/ESSENCE.md
    reason: structural QA, pointer integrity, stale-state, and closure-safety doctrine
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__prompts_workflows/ESSENCE.md
    reason: prompt/workflow boundary and staged execution doctrine
  - path: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/ESSENCE.md
    reason: advisory routing boundary and routing card doctrine
```

Helper/navigation files read:

```yaml
helper_files_read:
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/README.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/manifests/source-inventory.json
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/manifests/phase0/source-priority-candidates.md
```

## source_grounded_claims

```yaml
claims:
  - id: C001
    text: "The old agent KB has an explicit root index whose purpose is to map every first-wave agent to its KB root inside managed/agent_kb."
    source: "AGENT_KB_INDEX.md / Purpose"
    confidence: high
    label: raw_source

  - id: C002
    text: "Each agent KB root follows the same five-file scaffold: ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md, and LEARNING_QUEUE.md."
    source: "AGENT_KB_INDEX.md / Scaffold convention"
    confidence: high
    label: raw_source

  - id: C003
    text: "LEARNING_QUEUE.md is explicitly candidate-only and is never runtime truth."
    source: "AGENT_KB_INDEX.md / Scaffold convention; meta_detective/LEARNING_QUEUE.md / Purpose and Queue safeguards"
    confidence: high
    label: raw_source

  - id: C004
    text: "Agent KB roots encode owner and validator relationships rather than treating every role as self-validating."
    source: "AGENT_KB_INDEX.md / Agent KB root map"
    confidence: high
    label: source_backed_summary

  - id: C005
    text: "ESSENCE.md functions as the compact activation and boundary doctrine surface for an agent, while appendices hold deeper evidence, ranking, candidate detail, and anti-drift material where present."
    source: "alfred/ESSENCE.md; special_ops__knowledge_bank/ESSENCE.md / Operating rule and Required local surfaces; special_ops__informatics_design/ESSENCE.md / Scaffold / appendix split"
    confidence: high
    label: source_backed_summary

  - id: C006
    text: "The old system uses accepted appendix doctrine for detail that is too large or mode-specific for compact scaffold files, as shown by Meta Detective's APPENDIX_INTERNAL_MODES.md."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Purpose, Status, Relationship to scaffold files"
    confidence: high
    label: source_backed_summary

  - id: C007
    text: "The structure creates durable behavior across sessions by storing compact role boundaries, accepted practices, known mistakes, reusable templates, candidate queues, and owner/validator metadata in persistent files."
    source: "AGENT_KB_INDEX.md; meta_detective/BEST_PRACTICES.md / Entry schema; meta_detective/MISTAKES.md / Entry schema; meta_detective/TEMPLATES.md / Template schema; meta_detective/LEARNING_QUEUE.md / Entry schema"
    confidence: high
    label: source_backed_summary

  - id: C008
    text: "The old KB architecture intentionally separates source material, candidate material, accepted doctrine, and runtime truth to reduce accidental canonization."
    source: "meta_detective/LEARNING_QUEUE.md / Purpose and Promotion route; special_ops__hygiene_clean/ESSENCE.md / Status vocabulary and Operating doctrine; special_ops__knowledge_bank/ESSENCE.md / Core constraints"
    confidence: high
    label: source_backed_summary

  - id: C009
    text: "The mirrored source corpus is already available inside the KB root and records an original_source_root plus mirrored_source_root, so Phase 1 can proceed from visible source corpus rather than blocking on the old local path."
    source: "manifests/source-inventory.json / generated_at, original_source_root, mirrored_source_root"
    confidence: high
    label: raw_source

  - id: C010
    text: "Phase 0 navigation artifacts exist and classify source-priority candidates as deterministic navigation hints, not semantic authority rankings."
    source: "manifests/phase0/source-priority-candidates.md / opening note"
    confidence: high
    label: raw_source
```

## concepts_extracted

```yaml
concepts_extracted:
  - slug: five-file-agent-kb-scaffold
    label: "Five-file agent KB scaffold"
    definition: "The durable agent KB shape built from ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES, and LEARNING_QUEUE."
    source: "AGENT_KB_INDEX.md / Scaffold convention"
    phase2_value: high

  - slug: compact-essence-activation-surface
    label: "Compact ESSENCE activation surface"
    definition: "ESSENCE.md stores accepted compact boundary doctrine, owns/does-not-own lists, read triggers, and core constraints."
    source: "alfred/ESSENCE.md; meta_detective/ESSENCE.md; special_ops__hygiene_clean/ESSENCE.md"
    phase2_value: high

  - slug: candidate-only-learning-queue
    label: "Candidate-only learning queue"
    definition: "Learning queues capture useful future patterns but are not runtime truth until routed through owner/validator review and promotion."
    source: "meta_detective/LEARNING_QUEUE.md / Purpose, Write permissions, Promotion route, Queue safeguards"
    phase2_value: high

  - slug: owner-validator-agent-kb-model
    label: "Owner/validator KB model"
    definition: "Each role has a default owner and validator, preventing self-validation and clarifying escalation paths."
    source: "AGENT_KB_INDEX.md / Agent KB root map"
    phase2_value: high

  - slug: scaffold-appendix-split
    label: "Scaffold/appendix split"
    definition: "Compact scaffold files stay navigational while appendices carry evidence, candidate ledgers, source manifests, rankings, examples, and QA traces."
    source: "special_ops__knowledge_bank/ESSENCE.md / Required local surfaces; special_ops__informatics_design/ESSENCE.md / Scaffold / appendix split"
    phase2_value: high

  - slug: accepted-appendix-doctrine
    label: "Accepted appendix doctrine"
    definition: "A detailed appendix can become accepted operating doctrine without becoming a new agent, KB root, or runtime authority."
    source: "meta_detective/APPENDIX_INTERNAL_MODES.md / Purpose and Status"
    phase2_value: medium
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - id: alfred
    type: agent_role
    owns: [operator-facing intake, constraint capture, route brief framing, ambiguity clarification]
    does_not_own: [execution control, final strategy ownership, adversarial validation, runtime law, config mutation]
    source: "alfred/ESSENCE.md"

  - id: meta_ops
    type: agent_role
    owns: [orchestration, specialist activation, sequencing, bounded synthesis, validator routing, execution control]
    does_not_own: [operator personal priorities, final strategy, adversarial validation, direct canon mutation, config authority]
    source: "meta_ops/ESSENCE.md"

  - id: meta_strategy
    type: agent_role
    owns: [option framing, scenario comparison, timing analysis, leverage analysis, recommendation packets]
    does_not_own: [execution control, direct implementation, direct promotion, operator override, config authority]
    source: "meta_strategy/ESSENCE.md"

  - id: meta_detective
    type: validator_role
    owns: [adversarial validation, source authority challenge, contradiction surfacing, drift challenge, risk pressure, verdict packets]
    does_not_own: [primary execution, patch application, direct implementation, orchestration control, direct promotion]
    source: "meta_detective/ESSENCE.md"

  - id: special_ops__knowledge_bank
    type: specialist_role
    owns: [KB source manifesting, candidate ledgering, appendix-first architecture, KB placement and lifecycle routing]
    does_not_own: [final strategy, direct promotion approval, config mutation, adversarial validation ownership]
    source: "special_ops__knowledge_bank/ESSENCE.md"

  - id: special_ops__informatics_design
    type: specialist_role
    owns: [information architecture, taxonomy, terminology stability, chunking, appendix architecture, retrieval clarity]
    does_not_own: [domain truth validation, strategic direction, total KB governance, promotion approval, orchestration control]
    source: "special_ops__informatics_design/ESSENCE.md"

  - id: special_ops__hygiene_clean
    type: structural_validator_role
    owns: [structural QA, pointer integrity, stale-state checks, closure evidence, drift detection]
    does_not_own: [accepted-truth mutation, promotion approval, strategy authority, architecture design authority, config authority]
    source: "special_ops__hygiene_clean/ESSENCE.md"

  - id: special_ops__prompts_workflows
    type: specialist_role
    owns: [reusable prompt structures, workflow-stage patterns, promptflow skeletons, handoff templates]
    does_not_own: [orchestration authority, model/config routing authority, KB placement authority, promotion approval]
    source: "special_ops__prompts_workflows/ESSENCE.md"

  - id: special_ops__ai_handling_routing
    type: routing_specialist_role
    owns: [advisory model/tool posture, source-authority routing checks, ambiguity and escalation posture, handoff readiness]
    does_not_own: [runtime config mutation, provider-policy authority, all-agent orchestration authority, final approval]
    source: "special_ops__ai_handling_routing/ESSENCE.md"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "The root index names multiple special ops roots, but not every root was read end-to-end in this Phase 1 batch."
    source: "AGENT_KB_INDEX.md / Agent KB root map"
    confidence: high
    label: operator_question

  - id: T002
    text: "Learning queues can contain promoted trace records, but the operational doctrine must move to the promoted target file; this creates a necessary distinction between trace visibility and runtime authority."
    source: "meta_detective/LEARNING_QUEUE.md / Purpose, DET-LQ-005, Promotion route, Queue safeguards"
    confidence: high
    label: source_backed_summary

  - id: T003
    text: "Appendix-backed detail increases durability and retrieval depth, but scaffold files must remain compact; Phase 2 should preserve this split instead of converting every appendix into front-page doctrine."
    source: "special_ops__knowledge_bank/ESSENCE.md / Operating rule; special_ops__informatics_design/ESSENCE.md / Scaffold / appendix split"
    confidence: high
    label: source_backed_summary

  - id: T004
    text: "Some source roles are OpenClaw-specific. They are valuable as patterns, but current Apex/Claude-native synthesis must not preserve old runtime names as binding architecture by default."
    source: "multiple ESSENCE files use OpenClaw/final-system paths and role names"
    confidence: medium
    label: working_hypothesis
```

## migration_notes

```yaml
migration_notes:
  preserve:
    - "Five-file scaffold as a reusable doctrine pattern for durable agents or durable capability lanes."
    - "Candidate-only learning queues with owner, validator, score, overlap_check, and review_due."
    - "Owner/validator split for every durable role-like knowledge surface."
    - "Scaffold/appendix split for compression and retrieval efficiency."
    - "Accepted appendix doctrine for large mode packs that should not become new agents."
  adapt:
    - "Map old managed/agent_kb roots into current Apex KB wiki concepts and entities rather than resurrecting old runtime folders."
    - "Translate OpenClaw-specific path names into current Apex/Claude-native abstractions."
    - "Treat Phase 0 priority candidates as navigation aids, not authority rankings."
  deprecate_or_handle_carefully:
    - "Any direct claim that storage alone creates accepted canon."
    - "Any direct reuse of legacy runtime config or OpenClaw execution surfaces."
    - "Any learning queue content used as runtime truth without promotion."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - old-agent-kb-architecture
    - source-candidate-canon-separation
  concepts:
    - five-file-agent-kb-scaffold
    - compact-essence-activation-surface
    - candidate-only-learning-queue
    - owner-validator-agent-kb-model
    - scaffold-appendix-split
    - accepted-appendix-doctrine
  entities:
    - alfred
    - meta-ops
    - meta-strategy
    - meta-detective
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
