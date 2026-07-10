# Handover Prompt — APEX Step 3 Operator-Facing Output Design Principles + Artifact Family

## Role

You are the continuation architect for the APEX operator-output design process in:

```yaml
repository:
  full_name: leela-spec/apexai-os-meta
  branch: main
```

Your task is to execute **Step 3 only**:

> Define the APEX operator-facing output design principles and concrete artifact family that translate the verified Step 2 operator user stories into reusable cards, briefs, handoff blocks, review gates, and template acceptance criteria.

This is a continuation of completed work. Do not restart the architecture from memory and do not ask Marco to redefine the user stories.

---

## 1. Current verified state

Step 2 is complete and operator-verified.

```yaml
step_2_status:
  macro_loop: verified
  operator_value_language: verified
  planning_side_user_stories: verified
  execution_and_recap_user_stories: verified
  status_and_learning_user_stories: verified
  output_jobs: locked
  verified_by: Marco
  status: ready_for_step3
```

The Step 2 package is stored at:

```text
apex-meta/operator-output-design/step2-operator-user-stories/
```

Read the files from GitHub. Treat them as source authority for Step 3.

---

## 2. Required read order

Read these first, in this order:

```yaml
required_read_order:
  1: apex-meta/operator-output-design/step2-operator-user-stories/00-package-manifest.okf.yaml
  2: apex-meta/operator-output-design/step2-operator-user-stories/01-verification-decisions.okf.yaml
  3: apex-meta/operator-output-design/step2-operator-user-stories/02-macro-loop-and-value-frame.okf.yaml
  4: apex-meta/operator-output-design/step2-operator-user-stories/06-output-jobs-and-artifact-family.okf.yaml
  5: apex-meta/operator-output-design/step2-operator-user-stories/03-planning-side-user-stories.okf.yaml
  6: apex-meta/operator-output-design/step2-operator-user-stories/04-execution-recap-user-stories.okf.yaml
  7: apex-meta/operator-output-design/step2-operator-user-stories/05-status-learning-user-stories.okf.yaml
  8: apex-meta/operator-output-design/step2-operator-user-stories/07-step3-handoff-brief.okf.md
```

Then inspect only the current skill files needed to understand existing output authority and avoid schema duplication.

At minimum inspect:

```yaml
skill_sources_to_inspect:
  - .claude/Claude.md
  - .claude/skills/PrecapWeek/
  - .claude/skills/PrecapNextDay/
  - .claude/skills/raw-flow-dump-normalize/
  - .claude/skills/flow-recap/
  - .claude/skills/model-usage-log/
  - .claude/skills/status-merge/
  - .claude/skills/project-kb-manager/
  - .claude/skills/ProjectStatus/
  - .claude/skills/AIRouting/
```

Use the actual live paths found in the repository. Record path or casing drift as a source warning. Do not silently normalize paths during Step 3.

---

## 3. Locked operator-value principles

These were verified by Marco and are not open design questions:

```yaml
locked_operator_value_principles:
  first_10_seconds:
    every_primary_output_must_answer:
      - what_changed
      - what_next
      - what_needs_review

  result_card_first:
    required: true
    meaning: >
      The operator-facing success/result card appears before detailed schema,
      validation, provenance, or completion-gate blocks.

  human_first_machine_second:
    preferred_human_surfaces:
      - cards
      - short_lists
      - compact_summaries
    avoid_as_primary_surface:
      - wide_markdown_tables
      - raw_schema_fields
      - implementation_noise
      - validation_noise_before_operator_value

  operator_decision_language:
    preferred_actions:
      - approve
      - edit
      - reject
      - defer
      - clarify
      - execute
      - skip
      - mark_blocked

  no_silent_mutation:
    required: true
    meaning: >
      Durable state changes must be visibly classified as candidate, accepted,
      rejected, deferred, or unresolved.

  resilient_partial_context:
    required: true
    meaning: >
      Missing, stale, contradictory, or partial inputs must reduce confidence
      and create review flags rather than fabricated certainty.
```

Do not weaken or reinterpret these principles.

---

## 4. Locked output jobs and artifact family

Step 3 must define the operator-facing design family for all twelve locked jobs:

```yaml
locked_artifacts:
  J1:
    job: Show accepted current project reality before planning.
    artifact: Project State Success Card
  J2:
    job: Turn state into weekly direction.
    artifact: Weekly Command Brief
  J3:
    job: Turn weekly and state context into tomorrow's executable plan.
    artifact: Tomorrow Action Brief
  J4:
    job: Make each planned flow directly executable.
    artifact: Flow Execution Card
  J5:
    job: Provide ready-to-copy prompts per flow.
    artifact: Flow Prompt Pack
  J6:
    job: Normalize messy execution evidence.
    artifact: Raw Flow Dump / Skip Marker Card
  J7:
    job: Convert execution into reviewable memory.
    artifact: FlowRecap Result Card
  J8:
    job: Capture planned-vs-actual AI usage lightly.
    artifact: Usage Learning Card
  J9:
    job: Review candidate state changes before durable merge.
    artifact: Status Merge Decision Card
  J10:
    job: Store accepted project memory compactly.
    artifact: Project KB Update Card
  J11:
    job: Show the cross-project active landscape.
    artifact: Project Status Overview
  J12:
    job: Recommend tool or model route before execution.
    artifact: AI Routing Card
```

The purpose of Step 3 is not merely to repeat these names. It must define a coherent design system that explains:

```yaml
for_each_artifact_define:
  - operator_job
  - primary_question_answered
  - result_card_anatomy
  - required_human_visible_fields
  - optional_human_visible_fields
  - machine_readable_handoff_block
  - operator_decision_actions
  - missing_context_behavior
  - stale_or_conflicting_context_behavior
  - provenance_visibility
  - token_efficiency_rule
  - downstream_handoff
  - acceptance_criteria
```

---

## 5. Step 3 objective

Create a source package at:

```text
apex-meta/operator-output-design/step3-output-design-system/
```

The package should convert the Step 2 stories into concrete, reusable design specifications.

Recommended files:

```yaml
step3_target_files:
  - 00-package-manifest.okf.yaml
  - 01-operator-output-design-principles.okf.yaml
  - 02-shared-card-and-brief-anatomy.okf.yaml
  - 03-planning-artifact-family.okf.yaml
  - 04-execution-artifact-family.okf.yaml
  - 05-recap-learning-artifact-family.okf.yaml
  - 06-state-routing-artifact-family.okf.yaml
  - 07-review-gate-language-and-decision-patterns.okf.yaml
  - 08-resilience-provenance-and-confidence-rules.okf.yaml
  - 09-template-acceptance-criteria.okf.yaml
  - 10-step4-research-or-template-handoff.okf.md
```

You may adjust filenames if repo inspection shows a better naming convention, but preserve the separation of responsibilities and keep files small enough for manual review.

---

## 6. Work iteratively

Do not produce the entire package in one opaque pass.

Use this sequence:

```yaml
iteration_sequence:
  round_1:
    topic: shared_design_principles_and_common_anatomy
    output:
      - draft of files 01 and 02
    operator_review_focus:
      - first_screen_value
      - human_vs_machine_layering
      - shared_card_sections

  round_2:
    topic: planning_artifacts
    output:
      - draft of file 03
    covers:
      - J1
      - J2
      - J3

  round_3:
    topic: execution_artifacts
    output:
      - draft of file 04
    covers:
      - J4
      - J5
      - J6

  round_4:
    topic: recap_and_learning_artifacts
    output:
      - draft of file 05
    covers:
      - J7
      - J8

  round_5:
    topic: state_and_routing_artifacts
    output:
      - draft of file 06
    covers:
      - J9
      - J10
      - J11
      - J12

  round_6:
    topic: cross_cutting_rules
    output:
      - drafts of files 07, 08, and 09

  finalization:
    topic: package_manifest_and_next_handoff
    output:
      - files 00 and 10
```

Show Marco compact drafts and ask him to keep, change, or reject them. Do not ask him to design the system from scratch.

Do not write a draft section to GitHub until it has either:

```yaml
write_gate:
  accepted_by_marco: true
  or:
    instruction_explicitly_allows_unverified_draft_write: true
```

When writing verified material, label its verification state explicitly.

---

## 7. Design constraints

### 7.1 Schema authority

Existing skill contracts remain schema authority.

Step 3 owns presentation and operator interaction rules, not domain schemas.

```yaml
step3_must_not_own:
  - next_day_plan_schema
  - flow_packet_schema
  - flow_prompt_pack_schema
  - flow_recap_packet_schema
  - model_usage_delta_schema
  - status_merge_packet_schema
  - project_database_schema
  - routing_recommendation_packet_schema
  - calendar_event_write_schema
```

Use references to existing contracts instead of copying their schemas.

### 7.2 Human-visible layer

The operator-facing layer should hide implementation detail unless it affects a decision.

```yaml
human_visible_priority:
  first:
    - outcome_or_current_state
    - next_action
    - review_decision
    - blockers_or_warnings
  second:
    - concise_evidence_or_provenance
    - downstream_handoff
  later_or_collapsed:
    - identifiers
    - schema_fields
    - validation_details
    - technical metadata
```

### 7.3 Machine-readable layer

Each artifact may include a compact machine block, but the machine block must:

```yaml
machine_block_rules:
  - remain secondary to the human-facing result card
  - contain only fields needed by downstream consumers
  - reference authoritative schemas instead of redefining them
  - preserve candidate_vs_accepted_state
  - preserve source_confidence_and_freshness
  - avoid duplicating the full human-facing content
```

### 7.4 Tables

Use tables only when comparison genuinely benefits from rows and columns.

Do not use wide tables as the main operator interface.

### 7.5 Research

Do not begin broad Deep Research automatically.

First identify which Step 3 decisions can be derived from verified internal sources and which decisions genuinely need external evidence.

If external research is needed, create a narrow research brief only after the internal design problem is precisely stated.

---

## 8. Required acceptance criteria

The Step 3 package is complete only when:

```yaml
completion_criteria:
  source_grounding:
    all_step2_files_read: true
    relevant_live_skill_sources_inspected: true
    path_or_casing_drift_recorded: true

  coverage:
    all_12_locked_jobs_mapped: true
    all_12_artifacts_have_operator_job: true
    all_12_artifacts_have_result_card_anatomy: true
    all_12_artifacts_have_operator_decisions: true
    all_12_artifacts_have_resilience_behavior: true
    all_12_artifacts_have_handoff_definition: true
    all_12_artifacts_have_acceptance_criteria: true

  design_quality:
    first_10_seconds_rule_preserved: true
    result_card_first_preserved: true
    cards_and_short_lists_primary: true
    no_silent_mutation_preserved: true
    partial_context_resilience_preserved: true
    machine_blocks_secondary_and_compact: true

  boundaries:
    no_existing_skill_schema_redefined: true
    no_runtime_built: true
    no_agent_or_scheduler_built: true
    no_calendar_event_created: true
    no_FlowRecap_executed: true
    no_project_state_merged: true

  process:
    iterative_operator_review_used: true
    verification_state_recorded: true
    files_small_enough_for_manual_review: true
```

---

## 9. Explicitly out of scope

```yaml
out_of_scope:
  - rewriting current skill packages
  - applying Step 1 prompt-blocker patches
  - building final Markdown templates before the design spec is accepted
  - running PreCapWeek
  - running PreCapNextDay
  - executing project work
  - running raw-flow-dump-normalize on real work
  - running FlowRecap
  - merging project status
  - modifying the project KB
  - creating calendar events
  - building agents, subagents, cron, schedulers, or runtime orchestration
```

If repo hygiene issues interfere with Step 3, record them as blockers or assumptions. Do not silently fix unrelated files.

---

## 10. First response required from the new chat

After inspecting the required sources, respond with:

1. A concise source/access verdict.
2. A statement confirming the locked Step 2 decisions will not be reopened.
3. A proposed Round 1 draft covering:
   - shared operator-output design principles;
   - common card/brief anatomy;
   - the human-facing versus machine-readable layering rule.
4. Compact keep/change/reject questions for Marco.

Do not begin with generic UX research. Do not create all Step 3 files before the first operator review.
