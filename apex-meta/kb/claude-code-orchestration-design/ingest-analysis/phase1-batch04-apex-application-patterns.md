# Phase 1 Batch 04 — Apex Application Patterns

```yaml
title: "Apex Application Patterns"
source_batch_id: "phase1-batch04-apex-application-patterns"
kb_slug: "claude-code-orchestration-design"
phase: "ingest_phase_1"
status: "operator_review_needed"
created_at: "2026-07-02T00:00:00Z"
claim_labels_allowed:
  - fact
  - interpretation
  - recommendation
  - open_question
  - contradiction
confidence_labels_allowed:
  - high
  - medium
  - low
operator_gate:
  phase_2_allowed: false
  required_confirmation_phrase: "approve ingest"
```

## 1. Source Scope

This batch maps Claude/agent/skill orchestration patterns into Apex-specific skill, prompt, artifact, and KB lifecycle practices. It focuses on accepted Apex operator notes and prompt/workflow KB material: skill handoff via artifact contracts, prompt-pack discipline, source authority, bounded execution, explicit task state, gates, HALT/CLARIFY controls, file-output verification, and Phase 1/Phase 2 separation.

This is Phase 1 semantic ingest only. Phase 2 wiki synthesis is blocked pending operator approval with the exact phrase `approve ingest`.

## 2. Source Files Read

```yaml
source_files_read:
  - source_id: "apex-alfred-skill-definition-guide"
    path: "raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Apex_Alfred_Skill_Definition_Guide.md"
    source_type: "operator_supplied_note"
    authority: "primary"
    pointers:
      - "lines 5-18: PreCap / FlowRecap / APSU loop and skill mapping"
      - "lines 21-43: SKILL.md zones"
      - "lines 44-75: frontmatter and allowed-tools discipline"
      - "lines 76-93: objective and procedure block rules"
      - "lines 94-120: artifact handoff and operator gate patterns"
  - source_id: "prompt-workflow-essence"
    path: "raw/source-groups/prompt-engineer-research-base/raw/refs/old-prompt-workflow-kb/ESSENCE.md"
    source_type: "operator_supplied_prompt_workflow_note"
    authority: "primary"
    pointers:
      - "lines 5-14: purpose and agent boundary"
      - "lines 15-33: owns and does-not-own boundaries"
      - "lines 34-45: core doctrine"
      - "lines 47-63: read conditions and default sequence"
  - source_id: "prompt-workflow-best-practices"
    path: "raw/source-groups/prompt-engineer-research-base/raw/refs/old-prompt-workflow-kb/BEST_PRACTICES_v_old.md"
    source_type: "operator_supplied_prompt_workflow_note"
    authority: "primary"
    pointers:
      - "lines 31-51: full-body/live-edit vs patch mode"
      - "lines 53-72: freeze objective, target, source authority, non-goals, output contract, stop condition"
      - "lines 74-112: bounded stage-gated execution and source/verification gates"
      - "lines 114-149: capture out-of-mode improvements and clean handoffs"
      - "lines 151-188: durable QA and examples as regression tests"
      - "lines 190-230: explicit state frames and atomic task packets"
      - "lines 232-242: routing controls instead of prose warnings"
  - source_id: "promptflow-kb-base-build"
    path: "raw/source-groups/prompt-engineer-research-base/raw/refs/old-prompt-workflow-kb/PROMPTFLOW_KB_BASE_BUILD.md"
    source_type: "operator_supplied_promptflow"
    authority: "primary"
    pointers:
      - "lines 22-36: repo boundary and target lock"
      - "lines 37-53: source authority"
      - "lines 54-64: thin scaffold, deep appendices"
      - "lines 75-86: index consistency and plausibility check"
      - "lines 87-117: ranking model, sequence, and quality gates"
  - source_id: "execution-control-contracts"
    path: "raw/source-groups/prompt-engineer-research-base/raw/refs/old-prompt-workflow-kb/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"
    source_type: "operator_supplied_execution_contract"
    authority: "primary"
    pointers:
      - "lines 32-37: appendix purpose"
      - "lines 38-80: scope/authority lock and claim-status legend"
      - "lines 82-117: authority hierarchy and runtime/model caution"
      - "lines 118-190: state block and task payload contracts"
      - "lines 192-221: gate-check contract"
      - "continuation lines 1-51: HALT and CLARIFY contracts"
      - "continuation lines 52-94: file-output contract"
      - "continuation lines 95-153: split and task-closure contracts"
      - "continuation lines 154-245: frame-control, promotion, and external-claim handling"
      - "continuation lines 247-280: validation checklist"
  - source_id: "source-root-map"
    path: "manifests/migration/source-root-map.json"
    source_type: "migration_manifest"
    authority: "primary_navigation"
    pointers:
      - "lines 56-65 and 137-153: prompt-engineer-research-base copied as prompt-pack and Apex application pattern source group"
  - source_id: "phase0-navigation-report"
    path: "manifests/phase0/phase0-navigation-report.md"
    source_type: "phase0_navigation"
    authority: "primary_navigation"
    pointers:
      - "lines 20-24: Phase 0 boundary and forbidden semantic/state outputs"
```

## 3. Source-Grounded Claims

```yaml
claims:
  - id: "B04-C001"
    label: fact
    confidence: high
    claim: >
      Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills, while `OperatorExecutesPlannedFlow` remains a human action with a documented output contract rather than a skill file.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 5-18"

  - id: "B04-C002"
    label: fact
    confidence: high
    claim: >
      Apex skill files should separate routing metadata, a concise objective block, and a numbered procedure block; procedure steps should be artifact-focused and end in a completion gate.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 21-43"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 76-93"

  - id: "B04-C003"
    label: fact
    confidence: high
    claim: >
      Apex skill descriptions function as routing keys and should name exact input artifacts, exact output artifacts, and a boundary/non-purpose clause.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 44-67"

  - id: "B04-C004"
    label: fact
    confidence: high
    claim: >
      Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical/logical slot and downstream skills read that artifact.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 94-107"

  - id: "B04-C005"
    label: fact
    confidence: high
    claim: >
      Operator gates are a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 108-120"

  - id: "B04-C006"
    label: fact
    confidence: high
    claim: >
      The prompt/workflow lane owns reusable prompt structures, workflow-stage patterns, bounded execution sequences, promptflow skeletons, handoff templates, source-authority wording, and out-of-mode improvement capture; it does not own orchestration authority, model/config routing authority, KB placement authority, QA severity, promotion approval, or config mutation.
    source_pointers:
      - "ESSENCE.md lines 11-33"

  - id: "B04-C007"
    label: fact
    confidence: high
    claim: >
      Apex prompt/workflow doctrine requires target, source authority, non-goals, output contract, and stop condition to be named before execution; verification follows execution before completion is reported.
    source_pointers:
      - "ESSENCE.md lines 34-45"
      - "ESSENCE.md lines 55-63"
      - "BEST_PRACTICES_v_old.md lines 53-72"
      - "BEST_PRACTICES_v_old.md lines 94-112"

  - id: "B04-C008"
    label: fact
    confidence: high
    claim: >
      Bounded, stage-gated, artifact-centered execution is preferred over broad autonomy or giant multi-phase prompts in subscription-chat or handoff contexts.
    source_pointers:
      - "BEST_PRACTICES_v_old.md lines 74-92"

  - id: "B04-C009"
    label: fact
    confidence: high
    claim: >
      Out-of-mode improvements should be captured explicitly instead of applied silently; clean handoffs should include settled state, source priority, non-redo list, exact next job, risks, and success condition.
    source_pointers:
      - "BEST_PRACTICES_v_old.md lines 114-149"

  - id: "B04-C010"
    label: fact
    confidence: high
    claim: >
      Prompt/workflow examples are treated as behavioral regression tests; they check whether prompts preserve target, source, mode, validation, and stop discipline.
    source_pointers:
      - "BEST_PRACTICES_v_old.md lines 171-188"

  - id: "B04-C011"
    label: fact
    confidence: high
    claim: >
      High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction.
    source_pointers:
      - "BEST_PRACTICES_v_old.md lines 190-230"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-190"

  - id: "B04-C012"
    label: fact
    confidence: high
    claim: >
      The promptflow base build contract enforces repo boundary, target lock, source authority, thin scaffold/deep appendices, index plausibility checks, and quality gates before scaffold drafting.
    source_pointers:
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 22-64"
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 75-117"

  - id: "B04-C013"
    label: fact
    confidence: high
    claim: >
      Execution-control contracts define HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure.
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-51"
      - "BEST_PRACTICES_v_old.md lines 232-242"

  - id: "B04-C014"
    label: fact
    confidence: high
    claim: >
      File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed.
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 52-94"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 125-153"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 247-280"

  - id: "B04-C015"
    label: fact
    confidence: high
    claim: >
      External model, runtime, platform, API, and provider-behavior claims default to future-research or adjacent-lane status and should not become accepted prompt/workflow doctrine without independent verification.
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 82-117"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 222-245"

  - id: "B04-C016"
    label: interpretation
    confidence: high
    claim: >
      For Apex, Claude Code orchestration should be implemented as a source-locked artifact lifecycle: deterministic navigation, Phase 1 semantic ingest, explicit operator gate, then Phase 2 wiki synthesis only after approval.
    source_pointers:
      - "phase0-navigation-report.md lines 20-24"
      - "kb-schema.md lines 25-28"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 94-120"

  - id: "B04-C017"
    label: recommendation
    confidence: high
    claim: >
      Apex should use Claude Code skills for repeatable procedures, but preserve Apex lifecycle safety through explicit artifacts, state blocks, task payloads, gates, HALT/CLARIFY signals, and deterministic verification instead of relying on conversational continuity.
    source_pointers:
      - "BEST_PRACTICES_v_old.md lines 190-230"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-221"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-94"

  - id: "B04-C018"
    label: contradiction
    confidence: medium
    claim: >
      There is a tension between prompt/workflow artifact completeness and `SKILL.md` concision: Apex needs detailed contracts, but both the promptflow source and skill-design source push dense examples/schemas into appendices or references rather than the main activation file.
    source_pointers:
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 54-64"
      - "Apex_Alfred_Skill_Definition_Guide.md lines 85-93"

  - id: "B04-C019"
    label: open_question
    confidence: medium
    claim: >
      The exact filesystem convention for per-flow prompt packs in Claude-native Apex remains unresolved in the ingested sources; current evidence supports separate prompt-pack artifacts, but Phase 2 should not invent final paths without operator confirmation or additional source authority.
    source_pointers:
      - "ESSENCE.md lines 15-24"
      - "BEST_PRACTICES_v_old.md lines 53-92"
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 54-64"
```

## 4. Concepts Extracted

```yaml
concepts_extracted:
  - concept_slug: apex-artifact-contract-handoff
    label: "Apex artifact-contract handoff"
    definition: "A skill-to-skill connection pattern where artifacts, not direct calls, carry state and outputs between process stages."
    confidence: high
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 94-107"

  - concept_slug: operator-gated-orchestration
    label: "Operator-gated orchestration"
    definition: "A lifecycle design where downstream execution stops until the operator explicitly approves a proposed artifact or transition."
    confidence: high
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 108-120"

  - concept_slug: promptflow-frame-control
    label: "Promptflow frame control"
    definition: "A prompt/workflow discipline that carries explicit target, state, authority, constraints, gates, and stop signals to prevent drift."
    confidence: high
    source_pointers:
      - "ESSENCE.md lines 34-45"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 82-190"

  - concept_slug: atomic-task-payload
    label: "Atomic task payload"
    definition: "A one-task instruction object with explicit target, scope, input references, constraints, and validation conditions."
    confidence: high
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 157-190"
      - "BEST_PRACTICES_v_old.md lines 210-230"

  - concept_slug: halt-clarify-routing-controls
    label: "HALT/CLARIFY routing controls"
    definition: "Control signals that stop execution or request one blocking clarification instead of guessing or claiming partial success."
    confidence: high
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-51"

  - concept_slug: fetch-back-validation
    label: "Fetch-back validation"
    definition: "A file-write closure requirement: read back the written file and verify content, scope, and claim status before success is reported."
    confidence: high
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 52-94"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 125-153"

  - concept_slug: thin-scaffold-deep-appendices
    label: "Thin scaffold, deep appendices"
    definition: "An information architecture where activation files stay compact and detailed schemas/evidence live in referenced appendices."
    confidence: high
    source_pointers:
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 54-64"

  - concept_slug: source-authority-preflight
    label: "Source authority preflight"
    definition: "A pre-execution gate that establishes which sources outrank summaries, memory, and unverified claims before synthesis or writes."
    confidence: high
    source_pointers:
      - "ESSENCE.md lines 34-45"
      - "BEST_PRACTICES_v_old.md lines 94-112"
```

## 5. Entities Extracted

```yaml
entities_extracted:
  - entity_slug: precap-week
    entity_label: "PreCapWeek"
    entity_type: "apex_process_skill"
    role: "Weekly strategic planning skill in the Apex orchestration loop."
    confidence: medium

  - entity_slug: precap-next-day
    entity_label: "PreCapNextDay"
    entity_type: "apex_process_skill"
    role: "Daily executable planning skill that consumes weekly direction and project state."
    confidence: medium

  - entity_slug: flow-recap-skill
    entity_label: "FlowRecapSkill"
    entity_type: "apex_process_skill"
    role: "Digest skill that converts raw flow execution evidence into structured recap memory."
    confidence: medium

  - entity_slug: all-project-status-packet-update
    entity_label: "AllProjectStatusPacketUpdate / APSU"
    entity_type: "apex_process_skill"
    role: "Status-merge process that consumes flow recap packets and updates project status."
    confidence: medium

  - entity_slug: prompt-engineer-research-base
    entity_label: "Prompt Engineer Research Base"
    entity_type: "source_group"
    role: "Copied source group for prompt-pack, artifact-contract, and Apex application patterns."
    confidence: high

  - entity_slug: special-ops-prompts-workflows
    entity_label: "special_ops__prompts_workflows"
    entity_type: "legacy_operator_lane"
    role: "Prior prompt/workflow lane whose doctrine supplies reusable Apex frame-control and promptflow patterns."
    confidence: medium
```

## 6. Contradictions or Tensions

```yaml
contradictions_or_tensions:
  - id: "B04-T001"
    label: contradiction
    confidence: medium
    summary: >
      Apex needs rich execution contracts, but rich contracts should not bloat activation files. The sources converge on keeping SKILL.md/scaffold files compact and moving heavy schemas/evidence into references or appendices.
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 85-93"
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 54-64"

  - id: "B04-T002"
    label: contradiction
    confidence: high
    summary: >
      Chat continuity is explicitly insufficient for high-risk work. Apex prompt/workflow sources require explicit state blocks, atomic payloads, gates, and fetch-back proof; this conflicts with any workflow that claims completion from conversational memory alone.
    source_pointers:
      - "BEST_PRACTICES_v_old.md lines 190-230"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-221"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 125-153"

  - id: "B04-T003"
    label: contradiction
    confidence: medium
    summary: >
      Prompt/workflow sources include old repo/path names and OpenCLAW/MasterOfArts-specific paths. Their process patterns are reusable, but their absolute target paths and repo boundaries must not be copied as current Apex runtime paths.
    source_pointers:
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 22-36"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 38-55"

  - id: "B04-T004"
    label: contradiction
    confidence: high
    summary: >
      External/runtime/platform claims are explicitly not promotable without verification. This supports the KB rule that Phase 1 should preserve open questions and claim status rather than silently turning unverified runtime claims into doctrine.
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 107-117"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 222-245"
```

## 7. Open Questions

```yaml
open_questions:
  - id: "B04-Q001"
    label: open_question
    confidence: medium
    question: "What is the canonical Apex filesystem slot for per-flow prompt-pack artifacts in the Claude-native version?"
    source_pointers:
      - "ESSENCE.md lines 15-24"
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 54-64"

  - id: "B04-Q002"
    label: open_question
    confidence: medium
    question: "Which Apex processes should be represented as Claude Code skills, which should be rules or reference skills, and which should remain human/operator actions only?"
    source_pointers:
      - "Apex_Alfred_Skill_Definition_Guide.md lines 5-18"

  - id: "B04-Q003"
    label: open_question
    confidence: medium
    question: "Should HALT/CLARIFY/file-output/task-closure schemas become reusable Apex-wide contracts, or stay local to prompt/workflow execution lanes?"
    source_pointers:
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 1-153"

  - id: "B04-Q004"
    label: open_question
    confidence: medium
    question: "Which old OpenCLAW/MasterOfArts promptflow structures should be translated into current Apex paths, and which should remain historical evidence only?"
    source_pointers:
      - "PROMPTFLOW_KB_BASE_BUILD.md lines 22-36"
      - "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 38-80"
```

## 8. Proposed Phase 2 Wiki Targets

```yaml
proposed_phase_2_wiki_targets:
  summaries:
    - "wiki/summaries/apex-application-patterns.md"
  concepts:
    - "wiki/concepts/apex-artifact-contract-handoff.md"
    - "wiki/concepts/operator-gated-orchestration.md"
    - "wiki/concepts/promptflow-frame-control.md"
    - "wiki/concepts/atomic-task-payload.md"
    - "wiki/concepts/halt-clarify-routing-controls.md"
    - "wiki/concepts/fetch-back-validation.md"
    - "wiki/concepts/thin-scaffold-deep-appendices.md"
    - "wiki/concepts/source-authority-preflight.md"
  entities:
    - "wiki/entities/precap-week.md"
    - "wiki/entities/precap-next-day.md"
    - "wiki/entities/flow-recap-skill.md"
    - "wiki/entities/all-project-status-packet-update.md"
    - "wiki/entities/prompt-engineer-research-base.md"
    - "wiki/entities/special-ops-prompts-workflows.md"
  contradiction_pages:
    - "wiki/concepts/skilled-orchestration-vs-artifact-contract-boundary.md"
    - "wiki/concepts/legacy-openclaw-paths-vs-current-apex-paths.md"
```

## 9. Phase 2 Gate Statement

Phase 2 is blocked. Do not write `wiki/concepts/`, `wiki/entities/`, `wiki/summaries/`, semantic index sections, or final compiled KB pages until the operator gives the exact approval phrase in a later turn:

```text
approve ingest
```
