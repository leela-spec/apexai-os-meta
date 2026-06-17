# Apex/Hermes System Seed v0.1 — Macro/Meso Architecture

## 0. Status

```yaml
document:
  id: apex_hermes_system_seed_v0_1
  status: macro_meso_seed
  source_basis:
    - Apex/Hermes Workflow Example Database Master of Arts v0.1
    - Hermes process vocabulary / workflow extraction decisions
    - Current fixed four-profile architecture
  purpose: >
    Translate the workflow example database into a first system seed for building
    the Apex/Hermes orchestration infrastructure. This file defines profile
    responsibilities, SOUL/context implications, skill candidates, workflow-skill
    candidates, Kanban candidates, cron candidates, routine ownership, and next
    iteration gates.
  scope:
    included:
      - agent/profile architecture
      - profile responsibilities
      - SOUL.md information requirements
      - context-file information requirements
      - skill candidate map
      - workflow-skill candidate map
      - Kanban candidate map
      - cron candidate map
      - macro/meso workflow ownership
      - validation requirements
      - next build sequence
    excluded:
      - final SOUL.md files
      - final SKILL.md files
      - concrete cron JSON
      - concrete kanban_create calls
      - micro-level procedure steps
      - implementation commands
```

---

# 1. System Interpretation

```yaml
system_interpretation:
  main_goal: >
    Build a personal Hermes-based orchestration system that can support the
    Master of Arts / Leela / personal AI operating system work by routing
    projects, extracting workflows, creating skill candidates, validating outputs,
    running daily/night loops, and coordinating durable multi-profile work.

  current_artifact_role: >
    The workflow database is not the system itself. It is the first evidence
    layer from which system profiles, skills, routines, Kanban boards, cron jobs,
    and validation loops will later be generated.

  design_stage:
    current: macro_meso_translation
    next: system_seed_validation
    later:
      - profile_file_tree
      - SOUL.md_drafts
      - context_file_drafts
      - SKILL.md_drafts
      - Kanban_graph_specs
      - cron_specs
      - validation_checklists
```

---

# 2. Fixed Profile Architecture

Do not create additional profiles unless a later review proves that durable memory/config/tool isolation is required.

```yaml
profiles:
  alfred:
    type: hermes_profile
    layer: operator_interface
    role_summary: >
      User-facing assistant for intake, clarification, session start, morning
      review, operator-facing summaries, and handover to the meta profiles.
    owns:
      - user_intake
      - clarification
      - morning_review_interface
      - session_start
      - focused_session_prompt
      - operator_decision_capture
      - review_packet_presentation
      - handover_interface
    does_not_own:
      - strategic prioritization
      - workflow system design
      - validation authority
      - Kanban decomposition
      - skill lifecycle decisions
    main_outputs:
      - intake_packet
      - clarified_intent_packet
      - operator_decision_capture
      - focused_session_prompt
      - review_packet

  meta_strategist:
    type: hermes_profile
    layer: strategy_head
    role_summary: >
      Strategy profile for prioritization, leverage analysis, project ranking,
      transformation arcs, decision framing, and synthesis.
    owns:
      - strategic_evaluation
      - prioritization
      - leverage_analysis
      - scenario_analysis
      - option_generation
      - project_to_execution_matrix
      - transformation_arc_definition
      - weekly_project_review
      - shortlist_selection
    does_not_own:
      - routine execution tracking
      - low-level workflow normalization
      - daily command-board generation
      - final validation authority
    main_outputs:
      - prioritization
      - leverage_analysis
      - transformation_arc
      - project_matrix
      - strategic_options
      - workflow_shortlist

  meta_operations:
    type: hermes_profile
    layer: operations_head
    role_summary: >
      Operations profile for workflow extraction, routing, handoffs, prompt design,
      Kanban decomposition, daily/night loops, session export, workshop outlines,
      and project execution packaging.
    owns:
      - orchestration_intake
      - project_routing
      - workflow_extraction
      - workflow_normalization
      - source_scan
      - source_map_creation
      - handoff_packet_creation
      - Kanban_decomposition
      - daily_command_board
      - night_loop
      - session_export
      - skill_candidate_selection
      - workshop_creation_pipeline
      - idea_database_entry_creation
      - sequencing_to_Leela_use_case_mapping
    does_not_own:
      - final strategic authority
      - adversarial validation authority
      - profile identity decisions
      - native Hermes skill curation as a custom agent
    main_outputs:
      - workflow_records
      - source_maps
      - handoff_packets
      - Kanban_card_specs
      - skill_candidate_maps
      - workshop_outlines
      - session_exports
      - daily_boards

  meta_detective_controller:
    type: hermes_profile
    layer: control_head
    role_summary: >
      Control profile for verification, no-drift validation, contradiction
      detection, safety review, risk review, handoff review, and acceptance
      criteria enforcement.
    owns:
      - no_drift_validation
      - contradiction_detection
      - source_fidelity_check
      - mechanism_fit_review
      - profile_boundary_check
      - safety_container_review
      - risk_review
      - handoff_fidelity_review
      - acceptance_criteria_review
      - mistake_memory_candidates
    does_not_own:
      - primary execution
      - daily-board creation
      - strategy generation as primary owner
      - workflow creation as primary owner
    main_outputs:
      - validation_report
      - no_drift_report
      - risk_review
      - contradiction_detection
      - safety_review
      - QA_notes
```

---

# 3. SOUL.md Information Requirements

This section defines what each profile’s future `SOUL.md` must express. It does not write the final SOUL files yet.

```yaml
soul_information_requirements:
  alfred:
    identity:
      - user-facing interface
      - calm operator support
      - clarifies without over-questioning
      - converts vague user intent into structured packets
    style:
      - concise
      - direct
      - practical
      - decision-oriented
    avoid:
      - doing strategy itself
      - overloading user with system internals
      - inventing workflows
      - validating its own outputs
    ambiguity_default: >
      Ask only if a missing variable blocks intake; otherwise create a best-effort
      intake packet and mark uncertainty.

  meta_strategist:
    identity:
      - strategic evaluator
      - prioritization engine
      - leverage and sequencing thinker
      - synthesis profile
    style:
      - explicit tradeoffs
      - structured options
      - ranks by criteria
      - separates strategy from execution
    avoid:
      - low-level implementation details
      - producing final execution boards without operations
      - ignoring constraints or readiness
    ambiguity_default: >
      Produce ranked options with assumptions and ask meta_operations to package
      execution only after strategic direction is clear.

  meta_operations:
    identity:
      - workflow architect
      - process normalizer
      - routing and handoff profile
      - Kanban decomposition owner
    style:
      - operational
      - schema-driven
      - preserves input/output contracts
      - converts ideas into action packets
    avoid:
      - inventing profiles
      - skipping validation gates
      - treating every task as Kanban
      - prematurely writing final files
    ambiguity_default: >
      Create a normalized workflow record with inferred fields clearly marked,
      then route to strategist or detective when needed.

  meta_detective_controller:
    identity:
      - adversarial validator
      - no-drift checker
      - contradiction detector
      - safety and risk reviewer
    style:
      - precise
      - skeptical
      - source-grounded
      - pass/fail oriented
    avoid:
      - primary execution
      - over-polishing away useful roughness
      - accepting unsupported claims
      - letting uncertain items become canonical
    ambiguity_default: >
      Mark uncertainty, require source or rationale, and return actionable
      correction notes rather than rewriting the whole artifact.
```

---

# 4. Profile Context / AGENTS.md Information Requirements

Project-specific rules should not go into SOUL.md. They belong in profile context files or `AGENTS.md` / `.hermes.md`.

```yaml
context_file_information:
  global_project_context:
    belongs_in: AGENTS.md_or_.hermes.md
    should_include:
      - fixed four-profile architecture
      - macro/meso/micro build sequence
      - mechanism decision rules
      - Master of Arts project domains
      - Leela terminology: Spark / Session / Flow
      - no extra profiles unless durable isolation is justified
      - workflow is design-time abstraction, not Hermes runtime primitive
      - final artifacts must not be created until validated

  meta_operations_context:
    should_include:
      - workflow extraction schema
      - source map format
      - long list / shortlist / workflow record sequence
      - handoff packet conventions
      - Kanban decomposition rules
      - daily/night loop logic
      - skill candidate selection rules

  meta_strategist_context:
    should_include:
      - prioritization criteria
      - Master of Arts project matrix variables
      - readiness / leverage / effort / risk / mission alignment
      - strategy-to-execution handoff packet format

  meta_detective_context:
    should_include:
      - no-drift validation checklist
      - profile boundary checklist
      - mechanism fit checklist
      - safety and risk review rules
      - physical workshop safety constraints
      - legal/tax uncertainty gate rules

  alfred_context:
    should_include:
      - user intake format
      - morning review pattern
      - session start packet
      - operator decision capture
      - presentation style for review packets
```

---

# 5. Macro Workflow Layer

```yaml
macro_workflows:
  W01_hermes_self_buildout_workflow_database_creation:
    owner_profile: meta_operations
    supporting_profiles: [alfred, meta_strategist, meta_detective_controller]
    mechanism: Kanban_task_graph + workflow_skill
    role_in_system: recursive anchor workflow
    later_artifacts:
      - hermes-self-buildout workflow skill
      - system-buildout Kanban routine
      - validation checklist
      - profile/context seed update routine

  W03_master_of_arts_project_to_execution_matrix:
    owner_profile: meta_strategist
    supporting_profiles: [alfred, meta_operations, meta_detective_controller]
    mechanism: Kanban_task_graph + strategy skill + weekly cron
    role_in_system: portfolio prioritization and execution routing
    later_artifacts:
      - project-to-execution-matrix skill
      - Master of Arts portfolio board
      - weekly project review cron
      - daily board integration

  W05_raw_concept_to_workshop_outline_pipeline:
    owner_profile: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism: workflow_skill + optional Kanban for large workshops
    role_in_system: core Master of Arts production workflow
    later_artifacts:
      - workshop-creation-pipeline workflow skill
      - workshop-production board
      - safety-container-review skill

  W08_sequencing_coaching_format_to_Leela_use_case:
    owner_profile: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller, alfred]
    mechanism: workflow_skill + Kanban for productization
    role_in_system: bridge between Master of Arts concepts and Leela product design
    later_artifacts:
      - sequencing-to-leela-use-case workflow skill
      - Leela use-case board
      - product backlog packet format

  W09_legal_organizational_self_employment_setup_board:
    owner_profile: meta_operations
    supporting_profiles: [meta_detective_controller, meta_strategist, alfred]
    mechanism: Kanban_task_graph + recurring cron routines
    role_in_system: durable business operations setup
    later_artifacts:
      - self-employment-setup board
      - self-employment-checklist skill
      - monthly finance review cron
      - quarterly risk/compliance review cron
```

---

# 6. Meso Workflow Layer

```yaml
meso_workflows:
  W02_source_scan_to_workflow_record_normalization:
    owner_profile: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism: workflow_skill
    role_in_system: reusable extraction engine for all source corpora
    later_artifacts:
      - workflow-extraction skill
      - workflow-normalization skill
      - source-map-creation skill
      - no-drift validation gate

  W04_raw_idea_to_idea_database_entry:
    owner_profile: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism: workflow_skill
    role_in_system: high-volume idea capture and knowledge structuring
    later_artifacts:
      - audio-to-idea-database-entry workflow skill
      - idea clustering routine
      - project mapping routine

  W06_workshop_architecture_slide_compression:
    owner_profile: meta_operations
    supporting_profiles: [meta_detective_controller]
    mechanism: skill
    role_in_system: scan-optimized workshop/information-design transformation
    later_artifacts:
      - workshop-architecture-slide-compression skill
      - information-design validation checklist

  W07_embodied_technique_to_drill_protocol:
    owner_profile: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism: workflow_skill
    role_in_system: embodied insight to practice protocol
    later_artifacts:
      - embodied-technique-to-drill workflow skill
      - movement-analysis-to-drill skill
      - safety/overclaim review checklist

  W10_specialized_agent_handover_packet_creation:
    owner_profile: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller, alfred]
    mechanism: skill
    role_in_system: context transfer to another chat/profile/agent
    later_artifacts:
      - specialized-agent-handover skill
      - handoff-packet-creation skill
      - privacy/scope validation checklist
```

---

# 7. Core Routine Layer

```yaml
core_routines:
  operator_interface:
    - id: R01
      name: orchestration_intake
      owner_profile: alfred
      mechanism: skill
      input: raw_request
      output: clarified_intent_packet

    - id: R12
      name: morning_review
      owner_profile: alfred
      mechanism: cron + skill
      input: daily_board
      output: operator_decision_capture

    - id: R13
      name: session_start
      owner_profile: alfred
      mechanism: skill
      input: board_item
      output: focused_session_prompt

  workflow_creation:
    - id: R04
      name: source_scan
      owner_profile: meta_operations
      mechanism: skill
      input: source_files
      output: source_map

    - id: R05
      name: workflow_extraction
      owner_profile: meta_operations
      mechanism: skill
      input: source_map
      output: workflow_long_list

    - id: R06
      name: workflow_shortlist_selection
      owner_profile: meta_strategist
      mechanism: skill
      input: workflow_long_list
      output: workflow_shortlist

    - id: R07
      name: workflow_normalization
      owner_profile: meta_operations
      mechanism: workflow_skill
      input: workflow_shortlist
      output: workflow_records

    - id: R08
      name: skill_candidate_selection
      owner_profile: meta_operations
      mechanism: skill
      input: workflow_records
      output: skill_candidate_map

  validation:
    - id: R09
      name: no_drift_validation
      owner_profile: meta_detective_controller
      mechanism: skill
      input: draft_artifact_and_sources
      output: validation_report

    - id: R18
      name: safety_container_review
      owner_profile: meta_detective_controller
      mechanism: skill
      input: workshop_outline
      output: safety_review

  operations:
    - id: R02
      name: project_routing
      owner_profile: meta_operations
      mechanism: skill
      input: project_context
      output: routed_profile_and_mechanism

    - id: R03
      name: handoff_packet_creation
      owner_profile: meta_operations
      mechanism: skill
      input: source_context
      output: handover_packet

    - id: R10
      name: Kanban_decomposition
      owner_profile: meta_operations
      mechanism: skill
      input: workflow_record
      output: Kanban_card_specs

    - id: R14
      name: session_export
      owner_profile: meta_operations
      mechanism: skill
      input: chat_outputs_and_decisions
      output: session_export

  recurring_loops:
    - id: R11
      name: daily_command_board
      owner_profile: meta_operations
      mechanism: cron + skill
      input: project_matrix_and_carryover
      output: daily_board

    - id: R15
      name: night_loop
      owner_profile: meta_operations
      mechanism: cron + skill
      input: session_exports_and_open_loops
      output: next_day_prepared_sessions

    - id: R16
      name: weekly_project_review
      owner_profile: meta_strategist
      mechanism: cron + optional Kanban
      input: project_matrix_and_metrics
      output: reprioritized_portfolio

    - id: R20
      name: self_employment_finance_review
      owner_profile: meta_operations
      mechanism: cron + skill
      input: receipts_invoices_costs_revenue
      output: finance_review
```

---

# 8. Skill Candidate Layer

This section defines future skill candidates only. It does not write `SKILL.md`.

```yaml
skill_candidates:
  workflow_extraction:
    owner_profile: meta_operations
    purpose: Extract candidate workflows from source corpora.
    trigger: User provides chat histories, project docs, or source files for workflow mining.
    macro_or_meso: meso

  workflow_normalization:
    owner_profile: meta_operations
    purpose: Convert selected workflows into normalized workflow records.
    trigger: Workflow shortlist is ready.
    macro_or_meso: meso

  source_map_creation:
    owner_profile: meta_operations
    purpose: Classify available sources by type, relevance, and extraction value.
    trigger: New source corpus is provided.
    macro_or_meso: meso

  project_routing:
    owner_profile: meta_operations
    purpose: Route user requests/projects to profile, skill, Kanban, cron, or delegation mechanism.
    trigger: Clarified user intent or project context exists.
    macro_or_meso: meso

  handoff_packet_creation:
    owner_profile: meta_operations
    purpose: Create compact transfer packets for another chat/profile/agent.
    trigger: User asks for handover or cross-agent transfer.
    macro_or_meso: meso

  idea_database_entry:
    owner_profile: meta_operations
    purpose: Convert raw idea into structured reusable Markdown entry.
    trigger: User provides spoken or rough idea.
    macro_or_meso: meso

  workshop_phase_design:
    owner_profile: meta_operations
    purpose: Build a workshop phase arc from concept, audience, and transformation goal.
    trigger: Workshop outline or concept requires structuring.
    macro_or_meso: meso

  exercise_sequence_design:
    owner_profile: meta_operations
    purpose: Convert principles into exercise sequence grammar.
    trigger: Workshop or embodied-learning process needs drills.
    macro_or_meso: meso

  architecture_slide_compression:
    owner_profile: meta_operations
    purpose: Compress workshop/project logic into one-screen scan-optimized map.
    trigger: User asks for architecture, scan map, or small-image-readable overview.
    macro_or_meso: meso

  movement_analysis_to_drill:
    owner_profile: meta_operations
    purpose: Convert embodied/martial insight into protocol and teaching structure.
    trigger: User provides movement or technique insight.
    macro_or_meso: meso

  self_employment_checklist:
    owner_profile: meta_operations
    purpose: Convert legal/business setup source into actionable checklist.
    trigger: User asks to operationalize self-employment setup.
    macro_or_meso: meso

  no_drift_validation:
    owner_profile: meta_detective_controller
    purpose: Validate source fidelity, profile boundaries, and mechanism fit.
    trigger: Draft artifact is ready for review.
    macro_or_meso: meso

  safety_container_review:
    owner_profile: meta_detective_controller
    purpose: Review workshops, partner drills, and child/physical exercises for safety/container issues.
    trigger: Physical, child, or partner-contact workshop draft exists.
    macro_or_meso: meso

  prompt_design:
    owner_profile: meta_operations
    purpose: Design prompt packets for model/chat execution.
    trigger: A workflow requires external chat execution or operator-driven AI work.
    macro_or_meso: meso
```

---

# 9. Workflow-Skill Candidate Layer

```yaml
workflow_skill_candidates:
  hermes_self_buildout:
    owner_profile: meta_operations
    purpose: Coordinate source scan, long list, shortlist, normalization, validation, and system seed update.
    contains_skills:
      - source_map_creation
      - workflow_extraction
      - workflow_shortlist_selection
      - workflow_normalization
      - no_drift_validation
      - skill_candidate_selection
    may_use_kanban: true

  raw_concept_to_workshop_outline:
    owner_profile: meta_operations
    purpose: Turn raw workshop concept into phase outline, exercises, safety review, and scan map.
    contains_skills:
      - workshop_phase_design
      - exercise_sequence_design
      - safety_container_review
      - architecture_slide_compression
    may_use_kanban: true

  raw_idea_to_knowledge_entry:
    owner_profile: meta_operations
    purpose: Turn rough/spoken idea into structured entry, tags, project mapping, and next actions.
    contains_skills:
      - idea_database_entry
      - project_routing
      - no_drift_validation
    may_use_kanban: false

  sequencing_to_leela_use_case:
    owner_profile: meta_operations
    purpose: Convert a Sequencing/Master of Arts process into Leela-compatible use case and agent interaction model.
    contains_skills:
      - project_routing
      - workflow_normalization
      - no_drift_validation
    may_use_kanban: true

  embodied_technique_to_drill_protocol:
    owner_profile: meta_operations
    purpose: Convert movement insight into drill protocol, safety review, and content/workshop candidates.
    contains_skills:
      - movement_analysis_to_drill
      - safety_container_review
      - project_routing
    may_use_kanban: false
```

---

# 10. Kanban Candidate Layer

```yaml
kanban_routines:
  hermes_self_buildout_board:
    owner_profile: meta_operations
    purpose: Durable board for creating and improving the Hermes infrastructure.
    graph_shape: source_scan -> long_list -> shortlist -> normalized_records -> validation -> system_seed_update
    required_profiles:
      - alfred
      - meta_operations
      - meta_strategist
      - meta_detective_controller
    human_gates:
      - approve architecture seed
      - approve skill candidate priority
      - approve transition to micro implementation

  master_of_arts_project_portfolio_board:
    owner_profile: meta_strategist
    purpose: Rank and route Master of Arts projects into execution lanes.
    graph_shape: intake -> strategic ranking -> operations decomposition -> risk review -> operator decision
    required_profiles:
      - alfred
      - meta_strategist
      - meta_operations
      - meta_detective_controller
    human_gates:
      - choose priority horizon
      - approve selected project lanes

  workshop_production_board:
    owner_profile: meta_operations
    purpose: Produce major workshops through strategy, outline, exercises, safety, materials, and review.
    graph_shape: concept_intake -> transformation_arc -> outline -> safety_review -> materials -> operator_review
    required_profiles:
      - alfred
      - meta_strategist
      - meta_operations
      - meta_detective_controller
    human_gates:
      - approve workshop direction
      - approve safety-sensitive activities
      - approve final facilitator version

  leela_use_case_definition_board:
    owner_profile: meta_operations
    purpose: Translate Master of Arts / Sequencing concepts into Leela use cases.
    graph_shape: scenario -> Spark/Session/Flow mapping -> agent interaction model -> validation -> backlog
    required_profiles:
      - meta_strategist
      - meta_operations
      - meta_detective_controller
      - alfred
    human_gates:
      - choose product granularity
      - approve backlog inclusion

  self_employment_setup_board:
    owner_profile: meta_operations
    purpose: Durable setup board for legal, finance, insurance, compliance, and recurring operations.
    graph_shape: business_scope -> formal_setup -> finance_setup -> insurance_risk_review -> compliance_routines
    required_profiles:
      - alfred
      - meta_operations
      - meta_strategist
      - meta_detective_controller
    human_gates:
      - confirm launch activities
      - confirm legal/tax advisor questions
      - approve external submission steps
```

---

# 11. Cron Candidate Layer

```yaml
cron_candidates:
  daily_command_board:
    owner_profile: meta_operations
    cadence: daily
    purpose: Generate operator-ready daily board from project matrix, carryover, session exports, and open loops.
    input_packet:
      - project_matrix
      - carryover_tasks
      - session_exports
      - open_loops
    output_packet:
      - daily_board
      - recommended_focus_options

  morning_review:
    owner_profile: alfred
    cadence: daily_morning
    purpose: Present daily board and capture operator choice.
    input_packet:
      - daily_board
    output_packet:
      - operator_decision_capture
      - selected_session_start_packet

  night_loop:
    owner_profile: meta_operations
    cadence: nightly
    purpose: Convert session exports and open loops into prepared next-day work sessions.
    input_packet:
      - session_exports
      - unresolved_tasks
      - operator_notes
    output_packet:
      - next_day_prepared_sessions
      - workflow_improvement_candidates

  weekly_project_review:
    owner_profile: meta_strategist
    cadence: weekly
    purpose: Reprioritize Master of Arts portfolio by readiness, leverage, risk, effort, and current life context.
    input_packet:
      - project_matrix
      - progress_metrics
      - open_constraints
    output_packet:
      - reprioritized_portfolio
      - recommended_next_week_focus

  monthly_finance_review:
    owner_profile: meta_operations
    cadence: monthly
    purpose: Review receipts, invoices, revenue, costs, and bookkeeping state.
    input_packet:
      - receipts
      - invoices
      - costs
      - revenue
    output_packet:
      - finance_review
      - missing_documents_list

  quarterly_risk_compliance_review:
    owner_profile: meta_detective_controller
    cadence: quarterly
    purpose: Review business/workshop/product risks and compliance gates.
    input_packet:
      - business_activity_scope
      - workshop_activity_list
      - product_activity_list
      - open_risk_items
    output_packet:
      - risk_review
      - professional_advice_questions
```

---

# 12. Delegation Candidate Layer

Use `delegate_task` only for bounded synchronous subtasks, not durable profile-owned work.

```yaml
delegate_task_candidates:
  generate_visual_mockup_for_architecture_slide:
    parent_profile: meta_operations
    use_when: A workshop architecture map needs a quick visual variant.
    why_not_kanban: One-shot creative variant; no durable state required.

  create_copy_variants_for_micro_ritual_script:
    parent_profile: meta_operations
    use_when: Several short wording options are needed.
    why_not_kanban: Short synchronous generation; no human gate inside subtask.

  extract_candidate_branding_names:
    parent_profile: meta_strategist
    use_when: Need divergent naming options before synthesis.
    why_not_kanban: Anonymous parallel exploration is sufficient.

  draft_one_specific_exercise_script:
    parent_profile: meta_operations
    use_when: One exercise needs a first-pass script.
    why_not_kanban: Bounded generation that returns to parent workflow.

  summarize_one_source_chat_for_workflow_extraction:
    parent_profile: meta_operations
    use_when: Large source needs bounded summary before normalization.
    why_not_kanban: Use Kanban only if many source chats require durable parallel extraction.
```

---

# 13. Initial File / Folder Implications

No files should be created yet. This is only the future target structure.

```yaml
future_file_tree_concept:
  profiles:
    alfred:
      future_files:
        - SOUL.md
        - config.yaml
        - context/operator_interface.md
        - skills/orchestration-intake/SKILL.md
        - skills/morning-review/SKILL.md
        - skills/session-start/SKILL.md

    meta_strategist:
      future_files:
        - SOUL.md
        - config.yaml
        - context/strategy_principles.md
        - context/project_prioritization_rules.md
        - skills/workflow-shortlist-selection/SKILL.md
        - skills/project-to-execution-matrix/SKILL.md
        - skills/weekly-project-review/SKILL.md

    meta_operations:
      future_files:
        - SOUL.md
        - config.yaml
        - context/workflow_library_index.md
        - context/project_routing_rules.md
        - skills/source-map-creation/SKILL.md
        - skills/workflow-extraction/SKILL.md
        - skills/workflow-normalization/SKILL.md
        - skills/project-routing/SKILL.md
        - skills/handoff-packet-creation/SKILL.md
        - skills/kanban-decomposition/SKILL.md
        - skills/session-export/SKILL.md
        - skills/night-loop/SKILL.md
        - skills/daily-command-board/SKILL.md
        - skills/workshop-creation-pipeline/SKILL.md
        - skills/idea-database-entry/SKILL.md

    meta_detective_controller:
      future_files:
        - SOUL.md
        - config.yaml
        - context/validation_rules.md
        - context/safety_and_risk_rules.md
        - skills/no-drift-validation/SKILL.md
        - skills/safety-container-review/SKILL.md
        - skills/handoff-risk-check/SKILL.md
        - skills/mechanism-fit-review/SKILL.md
```

---

# 14. Validation Rules for This Seed

```yaml
seed_validation_rules:
  profile_boundary:
    - only four durable profiles are used
    - no workflow function becomes a new profile without justification
    - every workflow has an owner profile
    - every validation workflow has meta_detective_controller involved

  mechanism_fit:
    - repeatable one-profile process becomes skill
    - repeatable multi-step process becomes workflow_skill
    - durable multi-profile process becomes Kanban
    - recurring process becomes cron
    - bounded synchronous subtask becomes delegate_task

  macro_meso_boundary:
    - no final SKILL.md content yet
    - no concrete cron JSON yet
    - no concrete kanban_create calls yet
    - no detailed step-by-step implementation commands yet
    - only responsibilities, candidate artifacts, and process ownership

  source_fidelity:
    - source confidence remains visible
    - inferred workflows remain marked inferred
    - open questions remain unresolved until user validates
    - rough design logic is not over-cleaned

  operational_usefulness:
    - every workflow maps to later artifact candidates
    - every profile has clear ownership
    - every routine has input and output packets
    - every Kanban candidate has reason for durability
    - every cron candidate has recurrence reason
```

---

# 15. Gaps / Decisions Needed Before Micro-Level Implementation

```yaml
open_decisions:
  authoritative_decision_file:
    question: Is apex_hermes_orchestration_decisions_v0_1.md binding, or should this seed become the new binding architecture file?
    default_now: Use this seed as working architecture until superseded.

  priority_weighting:
    question: For Master of Arts project ranking, should we prioritize cash flow, low effort, Leela leverage, personal mission, public visibility, or launch speed?
    default_now: Low effort + high readiness + high Leela/Master-of-Arts leverage.

  idea_database_storage:
    question: Should idea entries remain chat-output blocks or be appended to a persistent Markdown knowledge file?
    default_now: Chat-output blocks until persistence target is validated.

  workshop_output_default:
    question: Should workshop workflows default to working outline, scan architecture, script, or facilitator checklist?
    default_now: Working outline first; scan architecture on request.

  Leela_granularity:
    question: Should Leela translation produce conceptual use case, screen flow, data model, or Hermes agent interaction spec?
    default_now: Conceptual use case + Hermes agent interaction spec.

  legal_business_launch_scope:
    question: Which activities launch first: coaching, workshops, martial arts, cacao/products, content, or Leela?
    default_now: Separate low-risk immediate activities from regulated/high-risk activities.
```

---

# 16. Recommended Evolution Process From Here

```yaml
evolution_process:
  step_1_validate_seed:
    owner: user + meta_detective_controller
    action: Review this seed for wrong ownership, missing workflows, overreach, and unclear priorities.
    output: approved_system_seed_v0_2

  step_2_create_component_registry:
    owner: meta_operations
    action: Convert profiles, routines, skills, workflow skills, Kanban routines, and cron candidates into a component registry.
    output: component_registry_v0_1

  step_3_prioritize_first_implementation_slice:
    owner: meta_strategist
    action: Pick the smallest useful system slice.
    recommended_slice:
      - alfred intake
      - meta_operations workflow extraction
      - meta_detective no-drift validation
      - source_scan_to_workflow_record workflow
    output: implementation_slice_v0_1

  step_4_write_profile_context_drafts:
    owner: meta_operations
    action: Draft SOUL/context outlines for the four profiles, still not final implementation.
    output: profile_context_drafts_v0_1

  step_5_write_first_skill_specs:
    owner: meta_operations
    action: Write skill specifications before final SKILL.md files.
    first_skill_specs:
      - workflow-extraction
      - workflow-normalization
      - no-drift-validation
      - handoff-packet-creation
      - project-routing
    output: skill_specs_v0_1

  step_6_design_first_kanban_graph:
    owner: meta_operations
    action: Design the Hermes self-buildout Kanban graph at meso level.
    output: hermes_self_buildout_kanban_spec_v0_1

  step_7_design_first_cron_loop:
    owner: meta_operations
    action: Design daily command board, morning review, and night loop cron specs at meso level.
    output: operating_loop_cron_specs_v0_1

  step_8_micro_implementation_only_after_review:
    owner: user
    action: Approve which artifacts become real files.
    output: permission_to_create_actual_Hermes_files
```

---

# 17. Recommended First Implementation Slice

Do not start by implementing everything. Start with the self-buildout loop.

```yaml
first_slice:
  name: workflow_extraction_and_validation_slice
  purpose: >
    Make the system capable of processing more source chats into usable
    workflow records without losing source fidelity.

  included_profiles:
    - alfred
    - meta_operations
    - meta_detective_controller
    - meta_strategist

  included_skills_to_spec_first:
    - orchestration-intake
    - source-map-creation
    - workflow-extraction
    - workflow-normalization
    - no-drift-validation
    - workflow-shortlist-selection

  included_kanban_candidate:
    - hermes-self-buildout-board

  excluded_for_now:
    - legal setup board implementation
    - Leela product backlog implementation
    - workshop production board implementation
    - finance cron implementation
    - final profile file creation
```

---

# 18. Working Conclusion

```yaml
conclusion:
  is_current_extraction_usable: true
  use_as: macro_meso_seed_source
  do_not_use_as:
    - direct implementation spec
    - final profile file content
    - final SKILL.md content
    - final cron job definitions
    - final Kanban board
  next_best_action: >
    Validate this system seed, then create a component registry and first
    implementation slice around workflow extraction + no-drift validation.
```