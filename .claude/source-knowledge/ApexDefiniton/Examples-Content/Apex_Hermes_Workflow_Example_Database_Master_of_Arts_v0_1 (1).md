# Apex/Hermes Workflow Example Database v0.1

**Scope:** First-pass workflow database extracted from the Master of Arts project context and the attached `Prompt4WorkflowDBExtraction.md` schema.

**Status:** Draft database for review. This is not a Hermes implementation. It does not create profiles, SOUL.md files, SKILL.md files, Kanban boards, or cron jobs.

---

## 1. Source Scan Summary

### Inspected / used sources

- **Prompt4WorkflowDBExtraction.md:** Governing schema and Hermes profile model.
- **Master Of Arts Meta.docx:** Main project map for concepts, outputs, media, events, business structure, Leela integration, routines, workshop/product ideas, and prioritization.
- **Workshop Structure Analysis.txt:** Strong pattern for converting dense workshop material into scan-optimized architecture maps.
- **Selfständigkeit rechtlich und organisatorisch.txt:** Strong process source for legal/organizational self-employment setup.
- **Project conversation context:** Agent swarm testing, content creation workflow, Audio-to-Idea Database, Peaceful Warrior / Superhero Training, dating-agent handover, cacao ceremony protocol, martial arts technique analysis.

### Best workflow-bearing chats / sources to process next, in order

1. **Agent Swarm Testing Workflow:** Best source for Hermes/Apex orchestration examples; use as recursive system-building case.
2. **Content Creation Workflow:** Best source for the iterative concept/workshop/document creation engine.
3. **Workshop Structure Analysis:** Best source for information-design workflow and scan-optimized outputs.
4. **Peaceful Warrior / Superhero Training:** Best source for workshop creation, facilitation logic, child safety, and embodied progression.
5. **Audio to Idea Database:** Best source for raw-idea ingestion, clustering, tags, project mapping, and next-action extraction.
6. **Master Of Arts Meta:** Best source for project portfolio routing, prioritization, output matrices, and business/content strategy.
7. **Selfständigkeit legal/organizational guide:** Best source for operations board workflow: legal setup, finance, insurance, compliance.
8. **Dating Agent Handover:** Best source for persona extraction and specialized-agent handover generation.
9. **Cacao Ceremony Protocol:** Best source for micro-script generation from intention/context constraints.
10. **Kampfkunst Technik Analyse:** Best source for embodied technique analysis -> drill/protocol/media output workflow.

---

## 2. Source Map

```yaml
source_map:
  - source_id: S01
    source_name: Prompt4WorkflowDBExtraction.md
    source_type: prompt_spec
    contains: [agents, workflows, routines, validation_logic, Kanban_logic, cron_logic, examples]
    extraction_priority: high
    reason: Governing schema and fixed Hermes profile architecture.

  - source_id: S02
    source_name: Master Of Arts Meta.docx
    source_type: concept_doc
    contains: [projects, concepts, outputs, routines, prioritization, business_structure, examples]
    extraction_priority: high
    reason: Central map of project domains, outputs, media/events/products, and Leela integration.

  - source_id: S03
    source_name: Workshop Structure Analysis.txt
    source_type: process_analysis
    contains: [workflows, information_design, validation_logic, examples]
    extraction_priority: high
    reason: Explicit distinction between document-oriented and slide-oriented workshop architecture outputs.

  - source_id: S04
    source_name: Selfständigkeit rechtlich und organisatorisch.txt
    source_type: operations_guide
    contains: [legal_process, finance_process, risk_process, compliance, checklists]
    extraction_priority: medium
    reason: Good durable operations-board candidate; less central to Hermes but concrete and procedural.

  - source_id: S05
    source_name: Audio to Idea Database chat pattern
    source_type: chat_history_pattern
    contains: [raw_idea_ingestion, metadata, clustering, project_mapping, next_actions]
    extraction_priority: high
    reason: Repeatable transformation from rough speech to structured reusable knowledge.

  - source_id: S06
    source_name: Peaceful Warrior / Superhero Training chats
    source_type: chat_history_pattern
    contains: [workshop_design, facilitation, safety, exercises, iteration]
    extraction_priority: high
    reason: Strong example of concept -> embodied workshop -> scan architecture -> refinement.

  - source_id: S07
    source_name: Agent Swarm Testing Workflow chat
    source_type: chat_history_pattern
    contains: [agent_orchestration, sequencing_system, use_cases, workflow_description]
    extraction_priority: high
    reason: Closest source for Hermes-native orchestration scenario generation.

  - source_id: S08
    source_name: Cacao Ceremony Protocol chat
    source_type: chat_history_pattern
    contains: [micro_script_generation, context_adaptation, ritual_design]
    extraction_priority: medium
    reason: Useful small workflow for context-sensitive facilitation copy.

  - source_id: S09
    source_name: Dating Agent Handover chat
    source_type: handover_pattern
    contains: [persona_extraction, goal_mapping, compatibility_filters, agent_handover]
    extraction_priority: medium
    reason: Good workflow for handover packet creation to specialized agents.

  - source_id: S10
    source_name: Kampfkunst Technik Analyse chat
    source_type: domain_analysis_pattern
    contains: [embodied_analysis, movement_principles, drills, artistic_translation]
    extraction_priority: medium
    reason: Useful for embodied-learning workflow examples.
```

---

## 3. Workflow Long List

```yaml
workflow_long_list:
  - {id: L01, name: hermes_self_buildout_workflow, source: S01/S07, likely_level: macro, likely_owner: meta_operations, likely_mechanism: kanban, keep_reason: Recursive anchor workflow for building the orchestration system.}
  - {id: L02, name: architecture_decision_capture, source: S01, likely_level: meso, likely_owner: meta_strategist, likely_mechanism: skill, keep_reason: Prevents drift in profile/system design.}
  - {id: L03, name: source_scan_and_source_map_creation, source: S01, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Required for every database/buildout pass.}
  - {id: L04, name: workflow_long_list_extraction, source: S01, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Converts source corpus into candidate workflow set.}
  - {id: L05, name: workflow_shortlist_selection, source: S01, likely_level: meso, likely_owner: meta_strategist, likely_mechanism: skill, keep_reason: Prioritizes high-value examples.}
  - {id: L06, name: workflow_record_normalization, source: S01, likely_level: meso, likely_owner: meta_operations, likely_mechanism: workflow_skill, keep_reason: Converts selected workflows into reusable schema records.}
  - {id: L07, name: profile_ownership_assignment, source: S01, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Maps work to fixed Hermes profile boundaries.}
  - {id: L08, name: no_drift_validation_review, source: S01/S03, likely_level: meso, likely_owner: meta_detective_controller, likely_mechanism: skill, keep_reason: Ensures source fidelity and prevents invention.}
  - {id: L09, name: skill_candidate_selection, source: S01, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Converts repeatable workflows into later SKILL.md candidates.}
  - {id: L10, name: kanban_decomposition_for_multistep_work, source: S01, likely_level: meso, likely_owner: meta_operations, likely_mechanism: kanban, keep_reason: Durable coordination for multi-profile work.}

  - {id: L11, name: daily_command_board_generation, source: S01/S02, likely_level: macro, likely_owner: meta_operations, likely_mechanism: cron, keep_reason: Needed to organize projects, priorities, and day execution.}
  - {id: L12, name: morning_review, source: S01/S02, likely_level: meso, likely_owner: alfred, likely_mechanism: cron, keep_reason: Operator-facing decision and attention routing.}
  - {id: L13, name: focused_work_session_start, source: S01/S02, likely_level: meso, likely_owner: alfred, likely_mechanism: skill, keep_reason: Starts a concrete session from board item or project intent.}
  - {id: L14, name: session_export, source: S01/S05, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Captures outputs and future context.}
  - {id: L15, name: night_loop, source: S01/S02, likely_level: macro, likely_owner: meta_operations, likely_mechanism: cron, keep_reason: Converts day residue into tomorrow-ready structure.}
  - {id: L16, name: weekly_project_review, source: S01/S02, likely_level: macro, likely_owner: meta_strategist, likely_mechanism: cron, keep_reason: Reprioritizes Master of Arts portfolio.}

  - {id: L17, name: raw_idea_to_idea_database_entry, source: S05, likely_level: meso, likely_owner: meta_operations, likely_mechanism: workflow_skill, keep_reason: Core reusable transformation of spoken/raw ideas into structured knowledge.}
  - {id: L18, name: idea_clustering_and_project_mapping, source: S05/S02, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Links ideas to Leela, Master of Arts, workshops, content, and next actions.}
  - {id: L19, name: principle_to_practice_translation, source: S05/S10, likely_level: meso, likely_owner: meta_strategist, likely_mechanism: skill, keep_reason: Turns abstract principles into embodied exercises or rules.}
  - {id: L20, name: theory_to_content_asset_pipeline, source: S02/S05, likely_level: macro, likely_owner: meta_operations, likely_mechanism: kanban, keep_reason: Turns concepts into videos, blogs, workshop modules, or Leela templates.}

  - {id: L21, name: raw_concept_to_workshop_outline, source: S06, likely_level: macro, likely_owner: meta_operations, likely_mechanism: workflow_skill, keep_reason: Reusable workshop creation procedure.}
  - {id: L22, name: workshop_phase_design, source: S06, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Builds phase arc from safety to transfer.}
  - {id: L23, name: exercise_sequence_design, source: S06/S10, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Converts principle to exercise grammar.}
  - {id: L24, name: facilitation_script_creation, source: S06/S08, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Converts outline into spoken facilitator lines.}
  - {id: L25, name: safety_container_review, source: S06/S04, likely_level: meso, likely_owner: meta_detective_controller, likely_mechanism: skill, keep_reason: Critical for child workshops, partner contact, physical exercises, events.}
  - {id: L26, name: workshop_architecture_slide_compression, source: S03/S06, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Creates one-screen concept-map view for design discussions.}
  - {id: L27, name: workshop_iteration_from_feedback, source: S03/S06, likely_level: meso, likely_owner: meta_operations, likely_mechanism: workflow_skill, keep_reason: Refines format and content from user corrections.}

  - {id: L28, name: project_to_execution_matrix, source: S02, likely_level: macro, likely_owner: meta_strategist, likely_mechanism: kanban, keep_reason: Maps concepts x outputs x business variables x constraints.}
  - {id: L29, name: demand_prioritized_offer_development, source: S02, likely_level: macro, likely_owner: meta_strategist, likely_mechanism: kanban, keep_reason: Advertise/perfect courses upon need; low-effort strategy.}
  - {id: L30, name: media_output_planning, source: S02, likely_level: macro, likely_owner: meta_operations, likely_mechanism: kanban, keep_reason: Converts projects into website/content/community/video outputs.}
  - {id: L31, name: Master_of_Arts_Leela_use_case_translation, source: S02/S07, likely_level: macro, likely_owner: meta_operations, likely_mechanism: workflow_skill, keep_reason: Translates ideation into digital Leela build/use cases.}
  - {id: L32, name: sequencing_coaching_format_definition, source: S02/S05, likely_level: macro, likely_owner: meta_strategist, likely_mechanism: kanban, keep_reason: Core professionalized coaching format.}

  - {id: L33, name: legal_self_employment_setup_board, source: S04, likely_level: macro, likely_owner: meta_operations, likely_mechanism: kanban, keep_reason: Concrete external operations process with documents, gates, and compliance.}
  - {id: L34, name: bookkeeping_and_finance_system_setup, source: S04, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Repeatable setup for accounts, receipts, software, EÜR, controlling.}
  - {id: L35, name: risk_insurance_review, source: S04, likely_level: meso, likely_owner: meta_detective_controller, likely_mechanism: skill, keep_reason: Risk gate for workshops/products/coaching.}
  - {id: L36, name: product_sales_compliance_setup, source: S04/S02, likely_level: meso, likely_owner: meta_detective_controller, likely_mechanism: skill, keep_reason: Relevant to cacao/supplement product plans.}

  - {id: L37, name: specialized_agent_handover_creation, source: S09, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Generates compact transfer packets for future agents.}
  - {id: L38, name: persona_goal_compatibility_extraction, source: S09, likely_level: meso, likely_owner: meta_strategist, likely_mechanism: skill, keep_reason: Extracts human values/goals/style for specialized-agent context.}
  - {id: L39, name: micro_ritual_script_generation, source: S08, likely_level: meso, likely_owner: meta_operations, likely_mechanism: skill, keep_reason: Small but reusable context-to-script workflow.}
  - {id: L40, name: embodied_technique_to_drill_protocol, source: S10, likely_level: meso, likely_owner: meta_operations, likely_mechanism: workflow_skill, keep_reason: Converts movement insight into practice structure and media output.}
```

---

## 4. Workflow Short List

```yaml
workflow_short_list:
  - workflow_id: W01
    workflow_name: Hermes Self-Buildout Workflow Database Creation
    why_selected: Primary recursive test case; directly builds the orchestration system's own examples.
    expected_later_artifact: workflow_skill + Kanban routine + validation checklist

  - workflow_id: W02
    workflow_name: Source Scan to Workflow Record Normalization
    why_selected: Core reusable extraction pattern for every future workflow database pass.
    expected_later_artifact: workflow-extraction SKILL.md

  - workflow_id: W03
    workflow_name: Master of Arts Project-to-Execution Matrix
    why_selected: Converts broad creative/business project space into concrete actions, outputs, and constraints.
    expected_later_artifact: Kanban routine + daily board integration

  - workflow_id: W04
    workflow_name: Raw Idea to Idea Database Entry
    why_selected: Repeatable high-volume process for spoken ideas and concept capture.
    expected_later_artifact: workflow_skill + knowledge-bank routine

  - workflow_id: W05
    workflow_name: Raw Concept to Workshop Outline Pipeline
    why_selected: Central Master of Arts production workflow; combines pedagogy, embodiment, facilitation, and safety.
    expected_later_artifact: workflow_skill

  - workflow_id: W06
    workflow_name: Workshop Architecture Slide Compression
    why_selected: Explicitly corrected workflow pattern; highly reusable for scan-optimized design discussions.
    expected_later_artifact: information-design skill

  - workflow_id: W07
    workflow_name: Embodied Technique to Drill Protocol
    why_selected: Captures unique Master of Arts embodied-analysis process.
    expected_later_artifact: movement-analysis workflow skill

  - workflow_id: W08
    workflow_name: Sequencing Coaching Format to Leela Use Case
    why_selected: Bridges life-operating-system concept, coaching templates, and digital product buildout.
    expected_later_artifact: workflow_skill + product backlog cards

  - workflow_id: W09
    workflow_name: Legal / Organizational Self-Employment Setup Board
    why_selected: Concrete operational project with gates, compliance, finance, insurance, and external actions.
    expected_later_artifact: Kanban board + checklist skill

  - workflow_id: W10
    workflow_name: Specialized Agent Handover Packet Creation
    why_selected: Needed to move context between chats/agents without losing personal/project nuance.
    expected_later_artifact: handoff-packet SKILL.md
```

---

## 5. Workflow Taxonomy

```yaml
macro_workflows:
  - W01: Hermes Self-Buildout Workflow Database Creation
  - W03: Master of Arts Project-to-Execution Matrix
  - W05: Raw Concept to Workshop Outline Pipeline
  - W08: Sequencing Coaching Format to Leela Use Case
  - W09: Legal / Organizational Self-Employment Setup Board

meso_workflows:
  - W02: Source Scan to Workflow Record Normalization
  - W04: Raw Idea to Idea Database Entry
  - W06: Workshop Architecture Slide Compression
  - W07: Embodied Technique to Drill Protocol
  - W10: Specialized Agent Handover Packet Creation

skill_candidates:
  - workflow-extraction
  - workflow-normalization
  - source-map-creation
  - project-routing
  - handoff-packet-creation
  - idea-database-entry
  - workshop-phase-design
  - exercise-sequence-design
  - architecture-slide-compression
  - movement-analysis-to-drill
  - self-employment-checklist
  - no-drift-validation

workflow_skill_candidates:
  - hermes-self-buildout
  - raw-concept-to-workshop-outline
  - raw-idea-to-knowledge-entry
  - sequencing-to-leela-use-case
  - embodied-technique-to-drill-protocol

Kanban_candidates:
  - W01
  - W03
  - W05
  - W08
  - W09

cron_candidates:
  - daily_command_board_generation
  - morning_review
  - night_loop
  - weekly_project_review
  - recurring_no_drift_validation
```

---

## 6. Workflow Records

```yaml
workflow_records:
  - workflow_id: W01
    workflow_name: Hermes Self-Buildout Workflow Database Creation
    level: macro
    source_domain: Hermes orchestration / recursive system buildout
    source_reference: [S01, S07]
    source_confidence: high
    current_status: extracted
    purpose: Model how Hermes would build and improve its own orchestration infrastructure.
    trigger: User asks to extract workflows, define agent interactions, or create Hermes buildout examples.
    entry_context: Attached workflow extraction prompt plus Master of Arts project sources.
    operator_intent: Fill Hermes with realistic example workflows before building final profiles/skills.
    profile_owner: meta_operations
    supporting_profiles: [alfred, meta_strategist, meta_detective_controller]
    mechanism_type:
      primary: kanban
      secondary: [workflow_skill, skill, context_file]
    inputs:
      required:
        - {name: architecture_decision_record, description: Binding profile/mechanism rules.}
        - {name: source_corpus, description: Chats, docs, prompts, prior handovers, workflow files.}
        - {name: output_schema, description: Workflow DB report and workflow_record schema.}
      optional:
        - {name: user_priority_override, description: Domains or workflows to emphasize.}
    outputs:
      primary:
        - {name: workflow_database, description: Structured macro/meso workflow examples.}
      secondary:
        - {name: skill_candidate_map, description: Later SKILL.md and workflow skill candidates.}
        - {name: Kanban_candidate_map, description: Durable workflows needing cards/lanes.}
        - {name: validation_report, description: Drift and uncertainty markers.}
    macro_sequence:
      - {step: 1, actor: alfred, action: capture operator intent and constraints, output: intake packet}
      - {step: 2, actor: meta_operations, action: scan sources and produce source map, output: source map}
      - {step: 3, actor: meta_operations, action: extract workflow long list, output: 30-60 candidates}
      - {step: 4, actor: meta_strategist, action: shortlist by leverage and reuse, output: 10-20 workflows}
      - {step: 5, actor: meta_operations, action: normalize workflow records, output: full records}
      - {step: 6, actor: meta_detective_controller, action: validate no drift and mechanism fit, output: QA notes}
      - {step: 7, actor: alfred, action: present operator-facing database and next decisions, output: review packet}
    meso_steps:
      - {step: 1, actor: meta_operations, action: distinguish profile vs skill vs workflow skill vs Kanban vs cron, input: candidate list, output: mechanism map, gate_or_stop_condition: uncertain items marked inferred}
      - {step: 2, actor: meta_detective_controller, action: check for forbidden profile proliferation, input: mechanism map, output: corrected profile map, gate_or_stop_condition: only fixed profiles used}
    handoffs:
      - {from: alfred, to: meta_operations, packet_needed: true, packet_type: orchestration_intake, return_expected: source_map}
      - {from: meta_operations, to: meta_strategist, packet_needed: true, packet_type: workflow_long_list, return_expected: shortlist}
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: normalized_records, return_expected: validation_notes}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: no_drift_and_profile_boundary_check
      pass_condition: All workflows use fixed profiles and uncertain source claims are marked.
      fail_condition: New agents invented, final Hermes files created prematurely, or source uncertainty hidden.
    Kanban_logic:
      use_kanban: true
      reason: Multi-profile, durable, iterative, review-heavy system-building work.
      possible_cards:
        - {title: Build source map, assignee_profile: meta_operations, dependencies: [], expected_output: source_map}
        - {title: Extract workflow long list, assignee_profile: meta_operations, dependencies: [source_map], expected_output: candidate_list}
        - {title: Validate profile boundaries, assignee_profile: meta_detective_controller, dependencies: [normalized_records], expected_output: validation_report}
    cron_logic:
      use_cron: false
      cadence: null
      reason: Buildout is project-driven; later recurring reviews can be cron.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: hermes-workflow-database-extraction
      owning_profile: meta_operations
      trigger_description: User asks to extract/normalize example workflows from a source corpus.
    examples:
      clean_example: Extract 10 Master of Arts workflows and assign profile/mechanism ownership.
      ambiguous_example: User gives many chats but no priority; default to Hermes, workshop, idea DB, daily ops.
      failure_or_edge_case: Treating every function as a new agent instead of skill/routine/Kanban.
    open_questions:
      - {question: Where is the authoritative apex_hermes_orchestration_decisions file?, why_it_matters: Current prompt references it, but it was not available in inspected sources.}

  - workflow_id: W02
    workflow_name: Source Scan to Workflow Record Normalization
    level: meso
    source_domain: workflow creation / extraction
    source_reference: [S01]
    source_confidence: high
    current_status: extracted
    purpose: Convert messy project material into normalized workflow records.
    trigger: New corpus, chat history, project folder, or uploaded source set is provided.
    entry_context: One or more source files plus target workflow schema.
    operator_intent: Identify reusable workflows without overfitting or inventing agents.
    profile_owner: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism_type:
      primary: workflow_skill
      secondary: [skill]
    inputs:
      required:
        - {name: source_files, description: Uploaded/project documents and chat excerpts.}
        - {name: extraction_schema, description: Source map, long list, shortlist, workflow_record.}
      optional:
        - {name: domain_priority, description: User-selected domains to emphasize.}
    outputs:
      primary:
        - {name: normalized_workflow_records, description: Schema-compliant records.}
      secondary:
        - {name: missing_information, description: Unresolved fields and default assumptions.}
    macro_sequence:
      - {step: 1, actor: meta_operations, action: inspect sources, output: source_map}
      - {step: 2, actor: meta_operations, action: extract long list, output: candidate list}
      - {step: 3, actor: meta_strategist, action: select high-value workflows, output: shortlist}
      - {step: 4, actor: meta_operations, action: normalize records, output: workflow records}
      - {step: 5, actor: meta_detective_controller, action: verify fidelity, output: validation notes}
    meso_steps:
      - {step: 1, actor: meta_operations, action: mark source confidence, input: source evidence, output: confidence labels, gate_or_stop_condition: low evidence marked inferred}
      - {step: 2, actor: meta_operations, action: assign primary mechanism, input: workflow behavior, output: skill/workflow_skill/Kanban/cron/delegate classification, gate_or_stop_condition: recurring routines are cron; durable coordination is Kanban}
    handoffs:
      - {from: meta_operations, to: meta_strategist, packet_needed: true, packet_type: long_list, return_expected: prioritized_shortlist}
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: normalized_records, return_expected: validation_notes}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: source_fidelity_check
      pass_condition: Every extracted claim has a source or is explicitly inferred.
      fail_condition: Confidently canonizing unsupported workflows.
    Kanban_logic:
      use_kanban: false
      reason: One corpus pass can usually be one workflow skill unless corpus is large.
      possible_cards: []
    cron_logic:
      use_cron: false
      cadence: null
      reason: Triggered by source ingestion, not recurring by default.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: workflow-normalization
      owning_profile: meta_operations
      trigger_description: Normalize workflow candidates into workflow_record schema.
    examples:
      clean_example: Convert Master of Arts workshop chats into 10 workflow records.
      ambiguous_example: A brainstorm doc has ideas but no explicit steps; infer cautiously.
      failure_or_edge_case: Compressing rough fragments so much that useful design logic is lost.
    open_questions:
      - {question: Should confidence scoring include numeric evidence count?, why_it_matters: Helps later automation select which records need validation.}

  - workflow_id: W03
    workflow_name: Master of Arts Project-to-Execution Matrix
    level: macro
    source_domain: Master of Arts portfolio operations
    source_reference: [S02]
    source_confidence: high
    current_status: extracted
    purpose: Convert broad Master of Arts concepts into prioritized outputs, business variables, and next actions.
    trigger: User asks what to work on, which project to prioritize, or how concepts translate into outputs.
    entry_context: Project map with concepts, media, events, products, cost/risk/partner/status variables.
    operator_intent: Avoid overwhelm; route ideas into concrete execution flows.
    profile_owner: meta_strategist
    supporting_profiles: [alfred, meta_operations, meta_detective_controller]
    mechanism_type:
      primary: kanban
      secondary: [workflow_skill, context_file]
    inputs:
      required:
        - {name: concept_inventory, description: Coaching, workshops, topics, media, events, products, Leela.}
        - {name: variable_matrix, description: Cost, risk, revenue, partner need, room need, public/private, status.}
      optional:
        - {name: time_window, description: Today, week, month, quarter, launch horizon.}
    outputs:
      primary:
        - {name: execution_matrix, description: Prioritized projects mapped to output forms and next actions.}
      secondary:
        - {name: daily_board_items, description: Concrete tasks for the current operating loop.}
        - {name: Kanban_cards, description: Durable cards for multi-step work.}
    macro_sequence:
      - {step: 1, actor: alfred, action: capture current operator objective, output: priority frame}
      - {step: 2, actor: meta_strategist, action: rank projects by leverage, readiness, cost, risk, output potential, output: ranked matrix}
      - {step: 3, actor: meta_operations, action: decompose top projects into cards/tasks, output: execution board}
      - {step: 4, actor: meta_detective_controller, action: flag contradictions/risks, output: risk notes}
      - {step: 5, actor: alfred, action: present decision options, output: operator choice}
    meso_steps:
      - {step: 1, actor: meta_strategist, action: detect quick wins, input: matrix, output: quick_win_list, gate_or_stop_condition: low cost + high readiness + visible output}
      - {step: 2, actor: meta_operations, action: translate selected project into output plan, input: operator choice, output: cards, gate_or_stop_condition: each card has owner, output, next action}
    handoffs:
      - {from: meta_strategist, to: meta_operations, packet_needed: true, packet_type: ranked_project_options, return_expected: execution_decomposition}
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: proposed_execution_cards, return_expected: risk_review}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: feasibility_and_constraint_check
      pass_condition: Selected tasks match readiness, risk, public/private constraints, and dependencies.
      fail_condition: Promoting low-readiness ideas into immediate execution without gate.
    Kanban_logic:
      use_kanban: true
      reason: Portfolio contains parallel lanes, dependencies, review, and durable project memory.
      possible_cards:
        - {title: Define Sequencing coaching format, assignee_profile: meta_strategist, dependencies: [], expected_output: positioning document}
        - {title: Produce morning routine video set, assignee_profile: meta_operations, dependencies: [concept_ready], expected_output: 3-video plan}
        - {title: Map Leela use cases from Master of Arts flows, assignee_profile: meta_operations, dependencies: [concept_inventory], expected_output: use_case_set}
    cron_logic:
      use_cron: true
      cadence: weekly
      reason: Project matrix should be reviewed weekly to prevent drift and overextension.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: project-to-execution-matrix
      owning_profile: meta_strategist
      trigger_description: User asks to prioritize or operationalize Master of Arts projects.
    examples:
      clean_example: Rank Morning Routine, Kamasutra Flows, Dance Fusion, Coaching, and Products by readiness and leverage.
      ambiguous_example: User says “what should I do next?” without horizon; default to this week.
      failure_or_edge_case: Choosing social media because it is attractive while ignoring stated cost/time burden.
    open_questions:
      - {question: Which variable weights matter most: cash flow, low effort, personal mission, launch speed, or public safety?, why_it_matters: Determines ranking logic.}

  - workflow_id: W04
    workflow_name: Raw Idea to Idea Database Entry
    level: meso
    source_domain: idea capture / knowledge base
    source_reference: [S05]
    source_confidence: medium
    current_status: inferred
    purpose: Convert spontaneous spoken/raw ideas into compact, reusable, English-only Markdown idea records.
    trigger: User dictates an idea, realization, process insight, or project fragment.
    entry_context: Raw note may be multilingual, nonlinear, emotional, repetitive, or incomplete.
    operator_intent: Preserve insight while making it searchable, clusterable, and actionable.
    profile_owner: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism_type:
      primary: workflow_skill
      secondary: [context_file]
    inputs:
      required:
        - {name: raw_idea_text, description: Spoken or rough typed idea.}
      optional:
        - {name: project_context, description: Leela, Master of Arts, Coaching, Sequencing, workshop, etc.}
    outputs:
      primary:
        - {name: idea_database_entry, description: Markdown code block with metadata, core, tags, mapping, rules, next actions.}
      secondary:
        - {name: clustering_links, description: Links to related projects, principles, or future artifacts.}
    macro_sequence:
      - {step: 1, actor: alfred, action: receive raw note, output: intake}
      - {step: 2, actor: meta_operations, action: distill core and classify, output: structured entry}
      - {step: 3, actor: meta_strategist, action: map leverage/project relevance, output: project mapping}
      - {step: 4, actor: meta_detective_controller, action: preserve semantic fidelity, output: drift check}
    meso_steps:
      - {step: 1, actor: meta_operations, action: extract distilled core, input: raw note, output: coherent insight, gate_or_stop_condition: no silent simplification of substantive information}
      - {step: 2, actor: meta_operations, action: assign tags and project mapping, input: coherent insight, output: metadata block, gate_or_stop_condition: uncertain mapping marked tentative}
      - {step: 3, actor: meta_strategist, action: derive next actions and principle links, input: metadata block, output: action list, gate_or_stop_condition: actions are small and executable}
    handoffs:
      - {from: alfred, to: meta_operations, packet_needed: true, packet_type: raw_idea_packet, return_expected: database_entry}
      - {from: meta_operations, to: meta_strategist, packet_needed: false, packet_type: classification_request, return_expected: leverage_notes}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: semantic_fidelity_check
      pass_condition: Entry preserves core meaning, unresolved roughness, and project relevance.
      fail_condition: Over-cleaning or renaming the concept so the original insight is lost.
    Kanban_logic:
      use_kanban: false
      reason: Single-entry transformation is one-call possible.
      possible_cards: []
    cron_logic:
      use_cron: false
      cadence: null
      reason: Event-triggered by user notes.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: audio-to-idea-database-entry
      owning_profile: meta_operations
      trigger_description: User provides raw spoken idea and wants database-ready structured entry.
    examples:
      clean_example: Convert a realization about choosing emotional state into a classified Leela/Sequencing rule.
      ambiguous_example: Idea belongs to both personal practice and product design; mark both.
      failure_or_edge_case: Turning a raw insight into generic self-help language.
    open_questions:
      - {question: Should entries be stored in one cumulative file or emitted as isolated blocks only?, why_it_matters: Determines knowledge-bank persistence workflow.}

  - workflow_id: W05
    workflow_name: Raw Concept to Workshop Outline Pipeline
    level: macro
    source_domain: workshop creation
    source_reference: [S06, S02]
    source_confidence: high
    current_status: extracted
    purpose: Transform rough concept material into a coherent workshop arc with exercises, facilitation, safety, and transfer.
    trigger: User asks to create or refine a workshop, class, training, retreat, or session.
    entry_context: Concept may include topic, audience, body practices, exercises, metaphors, constraints, and rough notes.
    operator_intent: Produce a usable workshop architecture without flattening rough design logic.
    profile_owner: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism_type:
      primary: workflow_skill
      secondary: [kanban, skill]
    inputs:
      required:
        - {name: workshop_concept, description: Core idea, audience, theme, constraints.}
        - {name: pedagogical_arc, description: Desired transformation/progression.}
      optional:
        - {name: source_notes, description: Rough notes, exercises, examples, prior outlines.}
        - {name: timebox, description: 45 min, 90 min, day workshop, etc.}
    outputs:
      primary:
        - {name: workshop_outline, description: Phase-based outline with facilitation logic and exercises.}
      secondary:
        - {name: safety_review, description: Risks and container requirements.}
        - {name: architecture_summary, description: One-screen scan map.}
    macro_sequence:
      - {step: 1, actor: alfred, action: capture audience, length, desired output, output: workshop intake}
      - {step: 2, actor: meta_strategist, action: define transformation arc and core principle, output: workshop strategy}
      - {step: 3, actor: meta_operations, action: create phase sequence and exercises, output: outline}
      - {step: 4, actor: meta_detective_controller, action: review safety, age fit, contact risk, drift, output: safety/QA notes}
      - {step: 5, actor: meta_operations, action: revise into selected format, output: final working outline}
    meso_steps:
      - {step: 1, actor: meta_operations, action: preserve rough notes and options, input: source notes, output: design inventory, gate_or_stop_condition: do not silently delete Ggf/options/2Dos}
      - {step: 2, actor: meta_operations, action: build phase blocks, input: strategy, output: phase outline, gate_or_stop_condition: phases form narrative + embodied progression}
      - {step: 3, actor: meta_operations, action: specify exercise grammar, input: phase outline, output: drills/scripts, gate_or_stop_condition: each exercise has why, what, cue, learning point}
    handoffs:
      - {from: meta_strategist, to: meta_operations, packet_needed: true, packet_type: workshop_strategy_packet, return_expected: outline}
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: workshop_outline, return_expected: safety_review}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: safety_and_fidelity_review
      pass_condition: Workshop matches audience, preserves intent, includes safety/container checks.
      fail_condition: Produces generic workshop or unsafe partner-contact sequence.
    Kanban_logic:
      use_kanban: true
      reason: Major workshops require iterative writing, safety review, materials, testing, and feedback.
      possible_cards:
        - {title: Define workshop transformation arc, assignee_profile: meta_strategist, dependencies: [], expected_output: core arc}
        - {title: Draft phase outline, assignee_profile: meta_operations, dependencies: [core arc], expected_output: outline}
        - {title: Review safety/container, assignee_profile: meta_detective_controller, dependencies: [outline], expected_output: safety notes}
    cron_logic:
      use_cron: false
      cadence: null
      reason: Project-triggered, not recurring by default.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: workshop-creation-pipeline
      owning_profile: meta_operations
      trigger_description: User asks to build workshop from raw concept/source notes.
    examples:
      clean_example: Build Peaceful Warrior Superhero Training from safety, identity, movement, and communication principles.
      ambiguous_example: User asks for “nice break” without deciding calm vs energizing; generate options and criteria.
      failure_or_edge_case: Removing brainstorming fragments that are essential to design rationale.
    open_questions:
      - {question: Should workshop output default to working outline, scan map, script, or facilitation sheet?, why_it_matters: Output format changes compression and detail level.}

  - workflow_id: W06
    workflow_name: Workshop Architecture Slide Compression
    level: meso
    source_domain: information design / workshop architecture
    source_reference: [S03, S06]
    source_confidence: high
    current_status: extracted
    purpose: Compress dense workshop material into one-screen architecture optimized for fast scanning.
    trigger: User asks for scan-optimized workshop architecture, concept map, executive summary slide, or small-image readability.
    entry_context: Existing workshop outline or phase structure.
    operator_intent: See full workshop logic in seconds, not read a document.
    profile_owner: meta_operations
    supporting_profiles: [meta_detective_controller]
    mechanism_type:
      primary: skill
      secondary: [delegate_task]
    inputs:
      required:
        - {name: workshop_outline, description: Existing outline or phase list.}
      optional:
        - {name: visual_constraints, description: one-screen, small screenshot, 5-7 blocks, why/what, module/outcome/exercises.}
    outputs:
      primary:
        - {name: architecture_slide_text, description: Hierarchical bullet map with 5-7 blocks.}
      secondary:
        - {name: visual_design_brief, description: Optional instructions for image/slide generation.}
    macro_sequence:
      - {step: 1, actor: meta_operations, action: identify top-level workshop objects, output: 5-7 blocks}
      - {step: 2, actor: meta_operations, action: compress each block into Why/What or Outcome/Exercises, output: scan map}
      - {step: 3, actor: meta_detective_controller, action: verify no document-style prose remains, output: pass/fail}
    meso_steps:
      - {step: 1, actor: meta_operations, action: select only architecture-level content, input: outline, output: block list, gate_or_stop_condition: max 5-7 blocks}
      - {step: 2, actor: meta_operations, action: remove facilitation detail/examples unless critical, input: block list, output: one-screen hierarchy, gate_or_stop_condition: each bullet below one line}
      - {step: 3, actor: meta_detective_controller, action: test small-image readability, input: one-screen hierarchy, output: compression verdict, gate_or_stop_condition: understandable in under 10 seconds}
    handoffs:
      - {from: meta_operations, to: meta_detective_controller, packet_needed: false, packet_type: compressed_map, return_expected: readability_review}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: format_fidelity_check
      pass_condition: One screen, low prose, visual hierarchy, scan-optimized blocks.
      fail_condition: Output reads like a document summary instead of architecture slide.
    Kanban_logic:
      use_kanban: false
      reason: Usually a one-call formatting/compression skill.
      possible_cards: []
    cron_logic:
      use_cron: false
      cadence: null
      reason: On-demand artifact transformation.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: workshop-architecture-slide-compression
      owning_profile: meta_operations
      trigger_description: User asks for workshop architecture summary optimized for scan/small-picture view.
    examples:
      clean_example: Convert Superhero Workshop into 5 blocks: Mindset, Zauber Acht, Stand, Selbstverteidigung, Transfer.
      ambiguous_example: User asks “make it nicer”; determine whether they mean document polish or scan architecture.
      failure_or_edge_case: Adding explanatory paragraphs, violating one-screen rule.
    open_questions:
      - {question: Should the default structure be Why/What or Module/Outcome/Exercises?, why_it_matters: The latter may fit workshop-design reasoning better.}

  - workflow_id: W07
    workflow_name: Embodied Technique to Drill Protocol
    level: meso
    source_domain: martial arts / embodied learning / art practice
    source_reference: [S10, S02]
    source_confidence: medium
    current_status: inferred
    purpose: Transform embodied martial-arts insight into a structured drill, partner protocol, and optional artistic/media output.
    trigger: User describes a movement insight, technical principle, body mechanic, or practice image.
    entry_context: Rough embodied description may include foot position, pressure line, flow image, mirror practice, partner context.
    operator_intent: Preserve kinesthetic nuance and convert it into repeatable practice.
    profile_owner: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller]
    mechanism_type:
      primary: workflow_skill
      secondary: [skill]
    inputs:
      required:
        - {name: embodied_insight, description: Raw movement/technique description.}
      optional:
        - {name: safety_constraints, description: Partner safety, intensity, beginner/intermediate level.}
        - {name: output_mode, description: drill, teaching script, video concept, art practice.}
    outputs:
      primary:
        - {name: drill_protocol, description: Solo/partner steps with objective, cues, and progression.}
      secondary:
        - {name: movement_principles, description: Underlying mechanics and metaphors.}
        - {name: media_or_art_prompt, description: Optional video/art translation.}
    macro_sequence:
      - {step: 1, actor: alfred, action: capture raw technique note, output: technique intake}
      - {step: 2, actor: meta_operations, action: extract mechanics and constraints, output: principle map}
      - {step: 3, actor: meta_operations, action: design solo + partner drill progression, output: practice protocol}
      - {step: 4, actor: meta_detective_controller, action: safety/overclaim review, output: adjusted protocol}
    meso_steps:
      - {step: 1, actor: meta_operations, action: separate observation, principle, drill, metaphor, input: raw note, output: structured analysis, gate_or_stop_condition: avoid inventing combat claims}
      - {step: 2, actor: meta_operations, action: define repetitions and feedback signals, input: principle map, output: drill protocol, gate_or_stop_condition: observable success criteria exist}
      - {step: 3, actor: meta_strategist, action: map to Master of Arts outputs, input: drill, output: workshop/video/content candidates, gate_or_stop_condition: output fit is explicit}
    handoffs:
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: drill_protocol, return_expected: safety_review}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: physical_safety_and_domain_humility_check
      pass_condition: Drill is safe, bounded, and clear about training context.
      fail_condition: Treating speculative technique insight as proven self-defense efficacy.
    Kanban_logic:
      use_kanban: false
      reason: Single drill protocol can be produced one-call; full video/course production would need Kanban.
      possible_cards: []
    cron_logic:
      use_cron: false
      cadence: null
      reason: On-demand practice design.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: embodied-technique-to-drill
      owning_profile: meta_operations
      trigger_description: User gives embodied technique insight and wants a structured practice protocol.
    examples:
      clean_example: Convert foot-hook/knee-pressure control insight into partner sensitivity drill.
      ambiguous_example: User describes an aesthetic movement image; output as art/practice instead of combat technique.
      failure_or_edge_case: Losing the artistic/kinetic quality by reducing everything to dry biomechanics.
    open_questions:
      - {question: Should martial-art protocols default to German or English?, why_it_matters: Workshop language and future database language may differ.}

  - workflow_id: W08
    workflow_name: Sequencing Coaching Format to Leela Use Case
    level: macro
    source_domain: Leela / Sequencing / coaching product design
    source_reference: [S02, S07, S05]
    source_confidence: medium
    current_status: inferred
    purpose: Translate Sequencing as a coaching format into Leela-compatible use cases, templates, and digital workflows.
    trigger: User asks how a concept, routine, or coaching process becomes a Leela feature/use case.
    entry_context: Conceptual material about routines, flows, Spark/Session/Flow, life organization, transformation, coaching sessions.
    operator_intent: Use Sequencing as the organizational layer for agentic AI and Leela execution.
    profile_owner: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller, alfred]
    mechanism_type:
      primary: workflow_skill
      secondary: [kanban, context_file]
    inputs:
      required:
        - {name: sequencing_concept, description: Coaching principle, routine, life process, or transformation structure.}
        - {name: Leela_context, description: App terminology and feature constraints.}
      optional:
        - {name: user_scenario, description: Real-life use case from Master of Arts day/project execution.}
    outputs:
      primary:
        - {name: Leela_use_case_flow, description: User story and process flow using canonical Leela terms.}
      secondary:
        - {name: agent_interaction_model, description: Hermes profiles/skills used to support the flow.}
        - {name: product_backlog_cards, description: Implementation-ready abstractions.}
    macro_sequence:
      - {step: 1, actor: meta_strategist, action: define transformation principle and user value, output: use-case rationale}
      - {step: 2, actor: meta_operations, action: map principle into Spark/Session/Flow sequence, output: process flow}
      - {step: 3, actor: meta_operations, action: define agent orchestration interactions, output: Hermes interaction pattern}
      - {step: 4, actor: meta_detective_controller, action: check terminology and scope drift, output: validation notes}
      - {step: 5, actor: alfred, action: present operator-facing scenario, output: reviewable use case}
    meso_steps:
      - {step: 1, actor: meta_operations, action: extract user scenario, input: project context, output: scenario packet, gate_or_stop_condition: concrete actor, trigger, target output}
      - {step: 2, actor: meta_operations, action: sequence process flow, input: scenario packet, output: Spark/Session/Flow mapping, gate_or_stop_condition: no noncanonical terms introduced}
      - {step: 3, actor: meta_strategist, action: evaluate leverage/product value, input: flow mapping, output: product priority, gate_or_stop_condition: value proposition clear}
    handoffs:
      - {from: meta_strategist, to: meta_operations, packet_needed: true, packet_type: transformation_principle, return_expected: use_case_flow}
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: Leela_flow, return_expected: terminology_check}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: canonical_term_and_scope_check
      pass_condition: Uses Spark/Session/Flow correctly and does not conflate coaching content with app implementation.
      fail_condition: Invents unsupported product architecture or new terminology.
    Kanban_logic:
      use_kanban: true
      reason: Product use cases require strategy, workflow, examples, validation, and implementation backlog.
      possible_cards:
        - {title: Extract Master of Arts sequencing scenario, assignee_profile: meta_operations, dependencies: [], expected_output: scenario packet}
        - {title: Map to Leela process terms, assignee_profile: meta_operations, dependencies: [scenario packet], expected_output: flow map}
        - {title: Validate product scope, assignee_profile: meta_detective_controller, dependencies: [flow map], expected_output: validation notes}
    cron_logic:
      use_cron: false
      cadence: null
      reason: Product definition is project-driven; recurring backlog review may be cron.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: sequencing-to-leela-use-case
      owning_profile: meta_operations
      trigger_description: User asks to convert a Sequencing/Master of Arts process into a Leela app use case.
    examples:
      clean_example: Convert “daily four flows” into a Leela day-planning and review process.
      ambiguous_example: Concept is both personal philosophy and app feature; split into coaching template and product use case.
      failure_or_edge_case: Treating an inspirational principle as an implementation spec without intermediate mapping.
    open_questions:
      - {question: Which Leela implementation granularity is desired: conceptual use case, Nowa screen flow, data model, or agent workflow?, why_it_matters: Prevents mismatched output.}

  - workflow_id: W09
    workflow_name: Legal / Organizational Self-Employment Setup Board
    level: macro
    source_domain: business operations / legal setup
    source_reference: [S04, S02]
    source_confidence: high
    current_status: extracted
    purpose: Convert legal/organizational setup requirements into an executable business operations board.
    trigger: User prepares self-employment, coaching/workshop/product business setup, or compliance review.
    entry_context: Business model includes coaching, workshops, trainings, physical products, content, and Leela-related business questions.
    operator_intent: Start legally and organizationally clean while minimizing bureaucracy.
    profile_owner: meta_operations
    supporting_profiles: [meta_detective_controller, meta_strategist, alfred]
    mechanism_type:
      primary: kanban
      secondary: [skill, context_file]
    inputs:
      required:
        - {name: business_activity_scope, description: Coaching, consulting, workshops, products, location, expected revenue.}
        - {name: legal_guide, description: Source checklist and recommendations.}
      optional:
        - {name: city_or_location, description: Munich, Münster, Passau, online.}
        - {name: revenue_forecast, description: Kleinunternehmer threshold and planning estimate.}
    outputs:
      primary:
        - {name: self_employment_kanban_board, description: Formalities, finance, taxes, insurance, product compliance, documentation.}
      secondary:
        - {name: risk_checklist, description: Items requiring tax/legal/professional confirmation.}
        - {name: document_collection_list, description: Forms, IDs, invoices, receipts, insurance docs.}
    macro_sequence:
      - {step: 1, actor: alfred, action: collect current business scope and open decisions, output: intake packet}
      - {step: 2, actor: meta_operations, action: convert guide into cards and sequence, output: operations board}
      - {step: 3, actor: meta_detective_controller, action: flag legal/tax uncertainty and risk gates, output: risk notes}
      - {step: 4, actor: meta_strategist, action: evaluate business model implications, output: strategic notes}
      - {step: 5, actor: alfred, action: present next action checklist, output: operator-ready sequence}
    meso_steps:
      - {step: 1, actor: meta_operations, action: separate formal setup, tax setup, bookkeeping, insurance, product compliance, input: legal guide, output: card lanes, gate_or_stop_condition: each lane has next action}
      - {step: 2, actor: meta_detective_controller, action: identify professional-advice gates, input: card lanes, output: warnings/gates, gate_or_stop_condition: no legal advice presented as final certainty}
      - {step: 3, actor: meta_operations, action: build recurring finance routine, input: bookkeeping requirements, output: monthly/quarterly routine, gate_or_stop_condition: receipts, invoices, EÜR, controlling included}
    handoffs:
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: compliance_board, return_expected: risk_gates}
      - {from: meta_operations, to: meta_strategist, packet_needed: true, packet_type: business_scope, return_expected: model_implications}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: legal_risk_and_source_limit_check
      pass_condition: Board distinguishes execution checklist from professional legal/tax advice.
      fail_condition: Overconfident legal conclusions or missing product/insurance risks.
    Kanban_logic:
      use_kanban: true
      reason: Multi-step, external dependencies, durable documents, human action, compliance gates.
      possible_cards:
        - {title: Decide Rechtsform and activity wording, assignee_profile: meta_strategist, dependencies: [], expected_output: decision note}
        - {title: Prepare Gewerbeanmeldung packet, assignee_profile: meta_operations, dependencies: [activity wording], expected_output: submission checklist}
        - {title: Set up bookkeeping system, assignee_profile: meta_operations, dependencies: [business account decision], expected_output: finance workflow}
        - {title: Review insurance and product liability, assignee_profile: meta_detective_controller, dependencies: [activity scope], expected_output: risk checklist}
    cron_logic:
      use_cron: true
      cadence: monthly_finance_review; quarterly_compliance_review
      reason: Finance and compliance require recurring review.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: self-employment-operations-board
      owning_profile: meta_operations
      trigger_description: User asks to turn business/legal guide into executable setup plan.
    examples:
      clean_example: Build board for coaching, workshops, martial arts, meditation, cacao/supplements, content.
      ambiguous_example: Some work may be freiberuflich vs gewerblich; mark as tax-advisor gate.
      failure_or_edge_case: Skipping insurance/product liability because focus is only on registration.
    open_questions:
      - {question: Which business activities are actually launching first?, why_it_matters: Determines compliance priority and card sequence.}

  - workflow_id: W10
    workflow_name: Specialized Agent Handover Packet Creation
    level: meso
    source_domain: agent handover / context transfer
    source_reference: [S09, S01]
    source_confidence: medium
    current_status: inferred
    purpose: Create compact, high-fidelity handover packets for another specialized chat/agent.
    trigger: User asks to create a handover for another agent/project/chat.
    entry_context: Existing project memory, goals, style, constraints, relevant source excerpts, desired target agent role.
    operator_intent: Transfer enough context to make the next agent effective without dumping irrelevant history.
    profile_owner: meta_operations
    supporting_profiles: [meta_strategist, meta_detective_controller, alfred]
    mechanism_type:
      primary: skill
      secondary: [context_file]
    inputs:
      required:
        - {name: target_agent_role, description: Dating agent, workshop agent, Hermes builder, content agent, etc.}
        - {name: source_context, description: User/project memory and relevant chat material.}
      optional:
        - {name: target_output, description: What the next agent should do with the handover.}
    outputs:
      primary:
        - {name: handover_packet, description: Structured Markdown brief for another agent.}
      secondary:
        - {name: prompt_for_next_chat, description: Directly usable invocation prompt.}
    macro_sequence:
      - {step: 1, actor: alfred, action: capture target agent and desired use, output: handover objective}
      - {step: 2, actor: meta_strategist, action: select highest-leverage identity/goals/context, output: relevance map}
      - {step: 3, actor: meta_operations, action: structure into handover packet and prompt, output: handover document}
      - {step: 4, actor: meta_detective_controller, action: check sensitivity, fidelity, and overreach, output: reviewed handover}
    meso_steps:
      - {step: 1, actor: meta_strategist, action: determine relevance filters, input: target role, output: inclusion/exclusion criteria, gate_or_stop_condition: avoid irrelevant biography}
      - {step: 2, actor: meta_operations, action: assemble sections, input: source context, output: handover packet, gate_or_stop_condition: enough context for agent action}
      - {step: 3, actor: meta_detective_controller, action: flag unsupported claims and sensitive material, input: packet, output: clean packet, gate_or_stop_condition: explicit uncertainty where needed}
    handoffs:
      - {from: meta_strategist, to: meta_operations, packet_needed: true, packet_type: relevance_map, return_expected: handover_packet}
      - {from: meta_operations, to: meta_detective_controller, packet_needed: true, packet_type: handover_packet, return_expected: QA_notes}
    validation:
      required: true
      validator: meta_detective_controller
      validation_type: handover_fidelity_and_scope_check
      pass_condition: Packet is specific, relevant, truthful, and usable by the target agent.
      fail_condition: Dumping irrelevant context or asserting speculative personal traits as facts.
    Kanban_logic:
      use_kanban: false
      reason: Usually one-call unless the handover is large and multi-source.
      possible_cards: []
    cron_logic:
      use_cron: false
      cadence: null
      reason: On-demand transfer artifact.
    skill_candidate:
      should_be_skill: true
      likely_skill_name: specialized-agent-handover
      owning_profile: meta_operations
      trigger_description: User asks to create a handover/prompt for another specialized chat or agent.
    examples:
      clean_example: Create dating-agent handover from personal goals, relationship filters, lifestyle vision, communication style.
      ambiguous_example: Target agent is vague; default to context, goals, constraints, first tasks, quality rules.
      failure_or_edge_case: Making the packet too flattering or too personal to be operationally useful.
    open_questions:
      - {question: Should handovers include memory-level personal context by default?, why_it_matters: Privacy and relevance tradeoff.}
```

---

## 7. Routine / Procedure Catalogue

```yaml
routine_catalogue:
  - {routine_id: R01, routine_name: orchestration_intake, category: [operator_interface], owner_profile: alfred, mechanism: skill, trigger: user_request, input_packet: raw_request, output_packet: clarified_intent_packet, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R02, routine_name: project_routing, category: [project, operator_interface], owner_profile: meta_operations, mechanism: skill, trigger: clarified_intent_packet, input_packet: project_context, output_packet: routed_profile_and_mechanism, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R03, routine_name: handoff_packet_creation, category: [project, operator_interface], owner_profile: meta_operations, mechanism: skill, trigger: transfer_to_agent_or_chat, input_packet: source_context, output_packet: handover_packet, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R04, routine_name: source_scan, category: [workflow_creation], owner_profile: meta_operations, mechanism: skill, trigger: new_source_corpus, input_packet: source_files, output_packet: source_map, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R05, routine_name: workflow_extraction, category: [workflow_creation], owner_profile: meta_operations, mechanism: skill, trigger: source_map_complete, input_packet: source_map, output_packet: workflow_long_list, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R06, routine_name: workflow_shortlist_selection, category: [workflow_creation], owner_profile: meta_strategist, mechanism: skill, trigger: long_list_ready, input_packet: workflow_long_list, output_packet: workflow_shortlist, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R07, routine_name: workflow_normalization, category: [workflow_creation], owner_profile: meta_operations, mechanism: workflow_skill, trigger: shortlist_ready, input_packet: workflow_shortlist, output_packet: workflow_records, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R08, routine_name: skill_candidate_selection, category: [skill_creation], owner_profile: meta_operations, mechanism: skill, trigger: workflow_records_ready, input_packet: workflow_records, output_packet: skill_candidate_map, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R09, routine_name: no_drift_validation, category: [validation], owner_profile: meta_detective_controller, mechanism: skill, trigger: artifact_ready_for_review, input_packet: draft_artifact_and_sources, output_packet: validation_report, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R10, routine_name: Kanban_decomposition, category: [Kanban, project], owner_profile: meta_operations, mechanism: skill, trigger: durable_multistep_work_detected, input_packet: workflow_record, output_packet: Kanban_card_specs, should_be_cron: false, should_be_skill: true, should_be_Kanban: true}
  - {routine_id: R11, routine_name: daily_command_board, category: [daily, operator_interface], owner_profile: meta_operations, mechanism: cron, trigger: daily_start_or_night_loop_output, input_packet: project_matrix_and_carryover, output_packet: daily_board, should_be_cron: true, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R12, routine_name: morning_review, category: [daily, operator_interface], owner_profile: alfred, mechanism: cron, trigger: morning, input_packet: daily_board, output_packet: operator_decision_capture, should_be_cron: true, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R13, routine_name: session_start, category: [daily, project], owner_profile: alfred, mechanism: skill, trigger: operator_selects_task, input_packet: board_item, output_packet: focused_session_prompt, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R14, routine_name: session_export, category: [daily, project], owner_profile: meta_operations, mechanism: skill, trigger: session_end, input_packet: chat_outputs_and_decisions, output_packet: session_export, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R15, routine_name: night_loop, category: [nightly], owner_profile: meta_operations, mechanism: cron, trigger: end_of_day, input_packet: session_exports_and_open_loops, output_packet: next_day_prepared_sessions, should_be_cron: true, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R16, routine_name: weekly_project_review, category: [weekly, project], owner_profile: meta_strategist, mechanism: cron, trigger: weekly, input_packet: project_matrix_and_metrics, output_packet: reprioritized_portfolio, should_be_cron: true, should_be_skill: true, should_be_Kanban: true}
  - {routine_id: R17, routine_name: workshop_architecture_compression, category: [project], owner_profile: meta_operations, mechanism: skill, trigger: scan_optimized_overview_requested, input_packet: workshop_outline, output_packet: architecture_slide_text, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R18, routine_name: safety_container_review, category: [validation], owner_profile: meta_detective_controller, mechanism: skill, trigger: physical_or_child_workshop_draft_ready, input_packet: workshop_outline, output_packet: safety_review, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R19, routine_name: idea_database_entry_creation, category: [project, workflow_creation], owner_profile: meta_operations, mechanism: workflow_skill, trigger: raw_idea_received, input_packet: raw_idea, output_packet: structured_idea_entry, should_be_cron: false, should_be_skill: true, should_be_Kanban: false}
  - {routine_id: R20, routine_name: self_employment_finance_review, category: [project, validation], owner_profile: meta_operations, mechanism: cron, trigger: monthly, input_packet: receipts_invoices_costs_revenue, output_packet: finance_review, should_be_cron: true, should_be_skill: true, should_be_Kanban: false}
```

---

## 8. Profile Ownership Map

```yaml
profile_ownership_map:
  alfred:
    primary_workflows: []
    supporting_workflows: [W01, W03, W04, W05, W08, W09, W10]
    owns_routines: [R01, R12, R13]
    main_outputs: [intake_packet, operator_decision_capture, focused_session_prompt, review_packet]

  meta_strategist:
    primary_workflows: [W03]
    supporting_workflows: [W01, W02, W04, W05, W07, W08, W09, W10]
    owns_routines: [R06, R16]
    main_outputs: [prioritization, leverage_analysis, transformation_arc, project_matrix, strategic_options]

  meta_operations:
    primary_workflows: [W01, W02, W04, W05, W06, W07, W08, W09, W10]
    supporting_workflows: [W03]
    owns_routines: [R02, R03, R04, R05, R07, R08, R10, R11, R14, R15, R17, R19, R20]
    main_outputs: [workflow_records, handoff_packets, Kanban_cards, workshop_outlines, session_exports, daily_boards]

  meta_detective_controller:
    primary_workflows: []
    supporting_workflows: [W01, W02, W03, W04, W05, W06, W07, W08, W09, W10]
    owns_routines: [R09, R18]
    main_outputs: [no_drift_report, risk_review, contradiction_detection, safety_review, validation_notes]
```

---

## 9. I/O Mechanism Map

```yaml
io_mechanism_map:
  entry_points:
    user_request:
      used_by: [W01, W02, W03, W05, W06, W08, W09, W10]
      notes: Main operator-driven entry point.
    raw_idea:
      used_by: [W04, W07]
      notes: Spoken/rough thought transformed into structured entry or drill.
    chat_history:
      used_by: [W01, W02, W10]
      notes: Requires source scan and confidence marking.
    project_context:
      used_by: [W03, W05, W08, W09]
      notes: Master of Arts project map, Leela terminology, workshop history.
    Kanban_card:
      used_by: [W01, W03, W05, W08, W09]
      notes: Durable multi-step execution entry.
    cron_trigger:
      used_by: [daily_command_board, morning_review, night_loop, weekly_project_review, finance_review]
      notes: Recurring routines, not one-off creative tasks.
    operator_override:
      used_by: [all]
      notes: User can override priority, format, language, or source scope.

  common_inputs:
    - raw_text
    - project_context
    - source_files
    - decision_record
    - examples
    - constraints
    - previous_outputs
    - operator_priority

  common_outputs:
    - workflow_record
    - source_map
    - workflow_long_list
    - workflow_shortlist
    - handoff_packet
    - skill_candidate
    - Kanban_card_spec
    - cron_routine_spec
    - session_export
    - daily_board_item
    - validation_report

  execution_granularity:
    W01:
      one_call_possible: false
      recommended_call_boundary: source_scan -> long_list -> shortlist -> records -> validation
      reason: Large multi-source recursive buildout; review iteration likely.
    W02:
      one_call_possible: true
      recommended_call_boundary: one corpus batch
      reason: Meso extraction can be done in one call if source size is manageable.
    W03:
      one_call_possible: false
      recommended_call_boundary: rank projects first, then decompose selected project
      reason: Portfolio strategy and execution planning should be staged.
    W04:
      one_call_possible: true
      recommended_call_boundary: one idea entry per call or small batch
      reason: High fidelity improves with small units.
    W05:
      one_call_possible: false
      recommended_call_boundary: strategy arc -> outline -> safety review -> script/materials
      reason: Workshop quality depends on iteration and format-specific outputs.
    W06:
      one_call_possible: true
      recommended_call_boundary: one outline to one architecture map
      reason: Compression is bounded and format-driven.
    W07:
      one_call_possible: true
      recommended_call_boundary: one technique insight to one drill protocol
      reason: Can be compact unless developing full curriculum/media.
    W08:
      one_call_possible: false
      recommended_call_boundary: scenario -> Leela mapping -> Hermes interactions -> backlog
      reason: Product/use-case definition needs staged abstraction.
    W09:
      one_call_possible: false
      recommended_call_boundary: legal setup -> finance setup -> risk review -> recurring routines
      reason: External tasks, documents, and compliance gates are durable.
    W10:
      one_call_possible: true
      recommended_call_boundary: one target agent handover
      reason: Usually a bounded context-transfer artifact.
```

---

## 10. Skill / Workflow Skill / Kanban / Cron Candidate Map

```yaml
candidate_map:
  skills:
    - workflow-extraction
    - workflow-normalization
    - project-routing
    - handoff-packet-creation
    - architecture-slide-compression
    - safety-container-review
    - no-drift-validation
    - self-employment-checklist
    - finance-review
    - prompt-design

  workflow_skills:
    - hermes-workflow-database-extraction
    - raw-idea-to-knowledge-entry
    - workshop-creation-pipeline
    - sequencing-to-leela-use-case
    - embodied-technique-to-drill-protocol

  Kanban_routines:
    - hermes-self-buildout-board
    - Master-of-Arts-project-portfolio-board
    - workshop-production-board
    - Leela-use-case-definition-board
    - self-employment-setup-board

  cron_routines:
    - daily-command-board
    - morning-review
    - night-loop
    - weekly-project-review
    - monthly-finance-review
    - quarterly-risk-compliance-review

  delegate_task_use_cases:
    - generate_visual_mockup_for_architecture_slide
    - create_copy_variants_for_micro_ritual_script
    - extract_candidate_branding_names
    - draft_one_specific_exercise_script
    - summarize_one_source_chat_for_workflow_extraction
```

---

## 11. Gaps / Open Questions

```yaml
missing_information:
  - workflow_id: W01
    missing_field: authoritative_decision_file
    question_for_user: Please provide apex_hermes_orchestration_decisions_v0_1.md or confirm the prompt's embedded architecture is binding.
    default_assumption: Use embedded Prompt4WorkflowDBExtraction architecture as binding for now.

  - workflow_id: W03
    missing_field: priority_weighting
    question_for_user: Should prioritization favor cash flow, low effort, Leela leverage, personal mission, or visibility?
    default_assumption: Favor low-effort + high-readiness + high-Leela/Master-of-Arts leverage.

  - workflow_id: W04
    missing_field: storage_target
    question_for_user: Should idea entries remain chat outputs or be appended to a persistent Markdown knowledge file?
    default_assumption: Emit as standalone Markdown code blocks unless a file is requested.

  - workflow_id: W05
    missing_field: default_workshop_format
    question_for_user: Should workshop outputs default to working outline, scan architecture, script, or facilitator checklist?
    default_assumption: Default to working outline unless scan-optimized is explicitly requested.

  - workflow_id: W06
    missing_field: visual_output_mode
    question_for_user: Should architecture maps be text-only, image, slide, or both?
    default_assumption: Text-first; generate image/slide only when explicitly requested.

  - workflow_id: W08
    missing_field: Leela_product_granularity
    question_for_user: Should use cases be product strategy, user flow, Nowa/Flutter implementation, or Hermes agent interaction spec?
    default_assumption: Use product strategy + agent interaction spec unless implementation is requested.

  - workflow_id: W09
    missing_field: launch_scope
    question_for_user: Which activities launch first: coaching, martial arts, workshops, cacao/products, content, or Leela?
    default_assumption: Separate immediate low-risk launch from later regulated/product/event expansion.
```

---

## 12. Next Prompts

```yaml
next_prompts:
  - target: W01 Hermes self-buildout
    purpose: Validate recursive system-building workflow.
    prompt_text: |
      Review W01 and correct the Hermes self-buildout sequence. Mark which parts should become Kanban cards, which parts should become skills, and which parts are only one-shot delegation.

  - target: W03 Master of Arts project matrix
    purpose: Turn project portfolio into executable Kanban.
    prompt_text: |
      Use the Master of Arts project map to create a ranked execution matrix for the next 30 days. Score each project by readiness, cash-flow potential, Leela leverage, public risk, partner need, and effort.

  - target: W04 Idea database
    purpose: Formalize the Audio-to-Idea workflow.
    prompt_text: |
      Define the canonical Markdown schema for Audio-to-Idea Database entries. Include metadata, distilled core, classification, project mapping, operational rules, next actions, and clustering links.

  - target: W05 Workshop pipeline
    purpose: Turn the workshop creation pattern into a workflow skill draft.
    prompt_text: |
      Convert the Raw Concept to Workshop Outline Pipeline into a detailed workflow-skill specification, but do not write SKILL.md yet. Include triggers, inputs, steps, gates, validation, and example source/output pairs.

  - target: W06 Architecture compression
    purpose: Create a reusable information-design routine.
    prompt_text: |
      Create a strict checklist for scan-optimized workshop architecture outputs. Include one-screen rule, 5-7 object rule, bullet length rule, visual hierarchy, and failure examples.

  - target: W08 Leela use cases
    purpose: Build concrete agentic orchestration examples.
    prompt_text: |
      Generate five realistic Master of Arts to Leela use-case scenarios using Spark / Session / Flow terminology. For each, define operator trigger, Hermes agent interactions, inputs, outputs, and validation gates.

  - target: W09 Self-employment setup
    purpose: Operationalize legal/business setup.
    prompt_text: |
      Convert the self-employment guide into a Kanban board with lanes for legal setup, tax setup, bookkeeping, insurance, product compliance, website/legal pages, and recurring finance review.
```
