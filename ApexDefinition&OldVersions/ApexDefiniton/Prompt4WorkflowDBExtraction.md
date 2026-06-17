# Prompt: Build a Rich Workflow Example Database for the Apex/Hermes Orchestration System

You are working inside the project **Apex_AI_With_Hermes**.

Your role is **Master Hermes + AI Orchestration Architect**.

Your task is to create a rich, structured database of example workflows that will later be used to define Hermes profiles, SOUL.md files, skills, workflow skills, Kanban routines, cron routines, and agent interaction patterns.

Do **not** build the final Hermes system yet.

Do **not** create profile files or SKILL.md files yet.

Your task is to extract, define, normalize, and organize **example workflows** at the **macro and meso level**.

---

# 0. Source Priority

Use the attached decision file as the architectural authority:

- `apex_hermes_orchestration_decisions_v0_1.md`
    

This file defines the current system decision:

```yaml
architecture:
  operator_interface:
    - alfred
  meta_heads:
    - meta_strategist
    - meta_operations
    - meta_detective_controller
  implementation_logic:
    profiles: durable role boundaries
    skills: reusable procedures
    workflow_skills: repeatable multi-step procedures
    kanban: durable multi-profile coordination
    cron: recurring routines
    delegate_task: transient one-shot specialist work
```

Treat the decision file as binding unless the user explicitly corrects it.

Also use any attached or available sources, including:

```yaml
source_classes:
  chat_histories:
    - workshop_creation
    - learning_psychology_creation
    - building_hermes_system
    - other relevant prior GPT chats
  alex_concepts:
    - learning_psychology
    - puzzling
    - skeleton
    - other conceptual frameworks
  existing_workflow_sources:
    - OpenCLAW workflow/process files
    - Alfred operating-loop files
    - Hermes profile/skill/Kanban/curator references
    - existing skill drafts
    - existing handover files
```

---

# 1. Core Objective

Create a **Workflow Example Database**.

The database should contain realistic examples of how the future Apex/Hermes orchestration system should handle work.

The purpose is to answer:

```yaml
core_questions:
  - What real workflows does this orchestration system need to support?
  - Which workflows are macro routines versus meso procedures?
  - Which profile owns each workflow?
  - Which workflows should become skills?
  - Which workflows should become workflow skills?
  - Which workflows require Kanban?
  - Which workflows require cron?
  - Which workflows use transient delegation?
  - What are the inputs, outputs, gates, and handoff packets?
  - What examples should later be used to create actual SKILL.md files?
```

---

# 2. Architectural Frame

Use this as the fixed profile model.

```yaml
profiles:
  alfred:
    role: operator_interface
    owns:
      - user intake
      - clarification
      - morning review
      - operator-facing summaries
      - operator decision capture
      - handover interface

  meta_strategist:
    role: strategy_head
    owns:
      - strategic evaluation
      - prioritization
      - scenarios
      - option generation
      - leverage analysis
      - recommendations
      - high-level synthesis

  meta_operations:
    role: operations_head
    owns:
      - orchestration intake
      - project routing
      - workflow design
      - prompt design
      - handoff packets
      - Kanban decomposition
      - session export
      - night loop
      - daily command board
      - craft-flow handoff
      - metrics and variables

  meta_detective_controller:
    role: control_head
    owns:
      - verification
      - no-drift validation
      - contradiction detection
      - QA review
      - handoff risk checks
      - escalation
      - mistake memory
```

Do **not** invent extra agents for every workflow.

Do **not** create separate agents for:

```yaml
not_profiles:
  - deep_researcher
  - patchspec_writer
  - night_planner
  - session_export_agent
  - daily_command_board_builder
  - skill_curator
  - knowledge_bank_ops
  - informatics_design
  - promotion_reviewer
```

Those are skills, routines, workflow skills, cron routines, or Hermes-native mechanisms.

---

# 3. What You Are Building

Create a structured database of workflow examples.

Each workflow example should make the orchestration system more concrete.

The final output should be a Markdown report with machine-readable YAML blocks.

Use this structure:

```markdown
# Apex/Hermes Workflow Example Database v0.1

## 1. Source Scan Summary

## 2. Workflow Taxonomy

## 3. Macro Workflow Catalogue

## 4. Meso Workflow Catalogue

## 5. Workflow Example Records

## 6. Input/Output Mechanism Map

## 7. Profile Ownership Map

## 8. Skill / Workflow Skill / Kanban / Cron Candidate Map

## 9. Example Workflow Sets by Source Domain

## 10. Gaps, Open Questions, and Next Prompts
```

---

# 4. Definitions

Use these definitions consistently.

## 4.1 Macro Workflow

A macro workflow is a large recurring or high-level process.

Examples:

```yaml
macro_workflows:
  - daily_operator_loop
  - night_planning_loop
  - workflow_database_creation
  - workshop_creation_pipeline
  - learning_psychology_content_creation
  - Hermes_system_buildout
  - project_to_execution_pipeline
  - source_ingestion_to_skill_candidate_pipeline
```

A macro workflow usually contains multiple meso workflows.

## 4.2 Meso Workflow

A meso workflow is a repeatable sub-process inside a macro workflow.

Examples:

```yaml
meso_workflows:
  - source_ingestion
  - long_list_extraction
  - short_list_selection
  - workflow_normalization
  - handoff_packet_creation
  - strategic_review
  - operations_planning
  - detective_validation
  - Kanban_decomposition
  - session_export
  - daily_command_board_generation
```

## 4.3 Skill Candidate

A skill candidate is a repeatable procedure that can later become a Hermes `SKILL.md`.

Examples:

```yaml
skill_candidates:
  - orchestration-intake
  - project-routing
  - handoff-packet
  - workflow-extraction
  - workflow-normalization
  - session-export
  - night-loop
  - daily-command-board
  - no-drift-validation
  - prompt-design
```

## 4.4 Kanban Candidate

A Kanban candidate is a workflow that requires durable multi-step tracking.

Use Kanban when:

```yaml
use_kanban_when:
  - multiple_profiles_needed
  - work_should_survive_restart
  - human_may_interject
  - parallel_lanes_exist
  - review_iteration_expected
  - audit_trail_matters
```

## 4.5 Cron Candidate

A cron candidate is a recurring routine.

Examples:

```yaml
cron_candidates:
  - night_loop
  - daily_command_board
  - weekly_project_review
  - recurring_repo_hygiene
  - recurring_validation_check
```

---

# 5. Required Workflow Record Format

Every workflow example must use this schema.

```yaml
workflow_record:
  workflow_id:
  workflow_name:
  level: macro | meso
  source_domain:
  source_reference:
  source_confidence: high | medium | low
  current_status: extracted | inferred | needs_user_validation

  purpose:
  trigger:
  entry_context:
  operator_intent:
  profile_owner:
  supporting_profiles:

  mechanism_type:
    primary: skill | workflow_skill | kanban | cron | delegate_task | profile_behavior | context_file
    secondary: []

  inputs:
    required:
      - name:
        description:
    optional:
      - name:
        description:

  outputs:
    primary:
      - name:
        description:
    secondary:
      - name:
        description:

  macro_sequence:
    - step:
      actor:
      action:
      output:

  meso_steps:
    - step:
      actor:
      action:
      input:
      output:
      gate_or_stop_condition:

  handoffs:
    - from:
      to:
      packet_needed: true | false
      packet_type:
      return_expected:

  validation:
    required: true | false
    validator:
    validation_type:
    pass_condition:
    fail_condition:

  Kanban_logic:
    use_kanban: true | false
    reason:
    possible_cards:
      - title:
        assignee_profile:
        dependencies:
        expected_output:

  cron_logic:
    use_cron: true | false
    cadence:
    reason:

  skill_candidate:
    should_be_skill: true | false
    likely_skill_name:
    owning_profile:
    trigger_description:

  examples:
    clean_example:
    ambiguous_example:
    failure_or_edge_case:

  open_questions:
    - question:
      why_it_matters:
```

Keep records concise but complete.

---

# 6. Extraction Process

Proceed in phases.

## Phase A — Source Orientation

First inspect available files and identify workflow-bearing material.

Create a source map:

```yaml
source_map:
  - source_id:
    source_name:
    source_type: chat_history | concept_doc | repo_file | skill_draft | decision_file
    contains:
      - agents
      - workflows
      - prompts
      - routines
      - examples
      - validation_logic
      - Kanban_logic
      - cron_logic
    extraction_priority: high | medium | low
```

Prioritize sources that contain actual procedures, repeated patterns, handoffs, or examples.

## Phase B — Long List Workflow Extraction

Extract a long list of candidate workflows.

Use this schema:

```yaml
workflow_long_list_item:
  id:
  name:
  source:
  rough_description:
  likely_level: macro | meso | unclear
  likely_owner:
  likely_mechanism:
  keep_reason:
```

Do not over-filter yet.

## Phase C — Short List Selection

Reduce the long list into a short list of high-value workflows.

Selection criteria:

```yaml
shortlist_criteria:
  - recurring_or_reusable
  - important_for_agent_orchestration
  - clear_profile_interaction
  - can_generate_skill_later
  - useful_for_daily_or_project_execution
  - useful_for building_the_Hermes_system_itself
```

Create:

```yaml
workflow_short_list:
  - workflow_id:
    workflow_name:
    why_selected:
    expected_later_artifact:
```

## Phase D — Normalize Workflow Records

For each short-listed workflow, create a full `workflow_record`.

Start with 10–20 high-value workflows.

Do not attempt to define everything at once.

## Phase E — Identify Missing Inputs

For each workflow, list what information is still missing.

```yaml
missing_information:
  - workflow_id:
    missing_field:
    question_for_user:
    default_assumption:
```

## Phase F — Generate Next Prompts

Create prompts the user can use to continue defining the workflow database.

For example:

```yaml
next_prompt:
  target:
  purpose:
  prompt_text:
```

---

# 7. Workflow Domains To Extract

Make sure to cover these domains.

## 7.1 Building the Hermes Orchestration System Itself

This is the primary test case.

Question:

> How would the agent system handle the task of creating the agent system?

Extract workflows for:

```yaml
hermes_buildout_workflows:
  - architecture_decision_capture
  - profile_definition
  - SOUL_file_creation
  - skill_database_design
  - workflow_database_creation
  - source_ingestion
  - workflow_extraction
  - workflow_normalization
  - skill_candidate_selection
  - profile_skill_assignment
  - Kanban_orchestration_design
  - validation_and_no_drift_review
```

## 7.2 Daily / Night / Session Operating Loop

Extract workflows for:

```yaml
operating_loop_workflows:
  - daily_command_board_generation
  - morning_review
  - focused_work_session_start
  - craft_flow_handoff
  - session_export
  - night_loop
  - next_day_prepared_sessions
  - weekly_review
```

## 7.3 Workshop Creation

Extract workflows for:

```yaml
workshop_creation_workflows:
  - raw_idea_to_workshop_outline
  - workshop_phase_design
  - exercise_sequence_design
  - facilitation_script_creation
  - safety_and_container_review
  - workshop_iteration_from_feedback
```

## 7.4 Learning Psychology Creation

Extract workflows for:

```yaml
learning_psychology_workflows:
  - concept_extraction
  - learning_model_design
  - explanation_generation
  - exercise_design
  - curriculum_mapping
  - validation_against_learning_principles
```

## 7.5 Alex Concepts

Extract workflows for:

```yaml
alex_concept_workflows:
  - concept_ingestion
  - concept_clustering
  - skeleton_creation
  - puzzling_process
  - theory_to_practice_translation
  - principle_to_exercise_conversion
```

## 7.6 Prompt / Workflow / Skill Creation

Extract workflows for:

```yaml
skill_creation_workflows:
  - successful_workflow_to_skill_candidate
  - prompt_design_for_specific_model
  - workflow_skill_spec_creation
  - skill_trigger_description_design
  - skill_example_generation
  - skill_validation
```

---

# 8. Input / Output Mechanism Design

For every workflow, define:

```yaml
io_mechanism:
  entry_points:
    - user_request
    - chat_history
    - repo_file
    - session_export
    - daily_board
    - Kanban_card
    - cron_trigger
    - operator_override

  inputs:
    - raw_text
    - project_context
    - decision_record
    - source_files
    - examples
    - constraints
    - previous_outputs

  outputs:
    - workflow_record
    - handoff_packet
    - skill_candidate
    - Kanban_card_spec
    - cron_routine_spec
    - session_export
    - daily_board_item
    - validation_report
```

Also identify how many workflow steps can realistically be done in one model call.

Use this field:

```yaml
execution_granularity:
  one_call_possible: true | false
  recommended_call_boundary:
  reason:
```

---

# 9. Required Routine / Procedure Catalogue

Create a catalogue of routines and procedures that the system probably needs.

Use this structure:

```yaml
routine_catalogue_item:
  routine_id:
  routine_name:
  category:
    - daily
    - nightly
    - weekly
    - project
    - workflow_creation
    - skill_creation
    - validation
    - Kanban
    - operator_interface
  owner_profile:
  mechanism:
  trigger:
  input_packet:
  output_packet:
  should_be_cron:
  should_be_skill:
  should_be_Kanban:
```

At minimum include:

```yaml
minimum_routines:
  - orchestration_intake
  - project_routing
  - handoff_packet_creation
  - session_start
  - session_export
  - night_loop
  - daily_command_board
  - morning_review
  - workflow_extraction
  - workflow_normalization
  - skill_candidate_selection
  - skill_spec_creation
  - prompt_design
  - no_drift_validation
  - Kanban_decomposition
  - weekly_review
  - repo_hygiene_review
```

---

# 10. Output Requirements

Produce the following report:

```markdown
# Apex/Hermes Workflow Example Database v0.1

## 1. Source Scan Summary
Briefly state what files/sources were inspected and which were most useful.

## 2. Source Map
YAML source map.

## 3. Workflow Long List
YAML or table.

## 4. Workflow Short List
YAML or table.

## 5. Workflow Taxonomy
Macro workflows, meso workflows, skill candidates, Kanban candidates, cron candidates.

## 6. Workflow Records
Use the full `workflow_record` schema.

## 7. Routine / Procedure Catalogue
Use the `routine_catalogue_item` schema.

## 8. Profile Ownership Map
Map every workflow to Alfred, Meta Strategist, Meta Operations, or Meta Detective/Controller.

## 9. I/O Mechanism Map
Define entry points, inputs, outputs, and call boundaries.

## 10. Next Prompts
Give prompts for the next iteration.
```

---

# 11. Quality Rules

Follow these rules:

```yaml
quality_rules:
  - Keep the system simple.
  - Do not create extra profiles.
  - Do not confuse workflow functions with agents.
  - Prefer skills over profiles for repeatable procedures.
  - Prefer Kanban only for durable multi-profile coordination.
  - Prefer cron only for recurring routines.
  - Mark inferred workflows explicitly.
  - Do not silently promote uncertain examples into canonical workflows.
  - Preserve rough examples if they reveal useful workflow structure.
  - Focus on macro and meso levels first.
  - Do not write final SKILL.md files yet.
```

---

# 12. First Output Strategy

Do not try to finish the entire database in one pass.

Start with this sequence:

```yaml
first_pass:
  output_1:
    name: source_scan_and_workflow_long_list
    target_count: 30_to_60_candidate_workflows

  output_2:
    name: workflow_short_list
    target_count: 10_to_20_high_value_workflows

  output_3:
    name: normalized_workflow_records
    target_count: 10_full_records

  output_4:
    name: routine_catalogue
    target_count: 15_to_25_routines

  output_5:
    name: next_questions_and_prompts
    target_count: 10_to_20_questions_or_prompts
```

If the task becomes too large, complete `output_1` and `output_2` first, then stop and ask for review.

---

# 13. Critical Interpretation

The first workflow to model is:

```yaml
primary_test_workflow:
  name: building_the_Apex_Hermes_orchestration_system
  question: >
    How would the future agent orchestration system handle the task of creating
    and improving itself?
  reason: >
    This is the most recursive and useful test case. If the system can define
    its own workflows, extract skill candidates, route profile responsibilities,
    and validate decisions, then it can probably handle other complex projects.
```

Use this as the anchor example.

After that, add examples from workshop creation, learning psychology, Alex concepts, and daily/night routines.

---

# 14. Final Instruction

Create the workflow database in a way that can later be transformed into:

```yaml
later_artifacts:
  - profile_file_tree
  - SOUL.md_files
  - profile_context_files
  - SKILL.md_files
  - workflow_skill_files
  - Kanban_routine_specs
  - cron_routine_specs
  - validation_checklists
```

But do not create those files yet.

Your output is the **example workflow database**, not the final Hermes implementation.