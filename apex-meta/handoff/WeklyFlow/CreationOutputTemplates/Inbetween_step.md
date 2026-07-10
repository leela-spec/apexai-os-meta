## Feedback incorporated

You are right: I confused **“compact result card first”** with **“compact artifact overall.”**

The result card can remain short, but the weekly and daily planning artifacts themselves must contain enough detail to let you judge:

- whether every project is moving in the right direction,
    
- whether priorities match your intentions,
    
- what concrete work is planned,
    
- how flows and sprints fit together,
    
- and what will actually be produced.
    

The existing design principles do not require shallow outputs. They require the decision summary to come first, followed by progressively deeper content.

# Verification of J3 terminology and sprint structure

## J3 is PreCap Next Day

“Tomorrow Action Brief” was the operator-facing artifact label selected during Step 2. The actual skill is still:

```yaml
skill: precap-next-day
primary_output: next_day_plan
output_role: resilient_daily_orchestration_compiler
```

That is confirmed by the live `PrecapNextDay` entrypoint.

Because **Tomorrow Action Brief** is unfamiliar and obscures its relationship to the skill, I recommend changing the operator-facing name to:

> **PreCap Next Day Brief**

Machine-facing artifact name remains:

```yaml
artifact_name: next_day_plan
```

This gives us:

```yaml
operator_name: PreCap Next Day Brief
machine_artifact: next_day_plan
produced_by: precap-next-day
```

## The three sprints are still present

Yes. The live flow-packet template explicitly contains:

- **S1**
    
- **S2**
    
- **S3**
    

Each sprint has its own focus, expected output, workflow/process label, prompt-pack reference, and review flag.

The skill procedure also requires each flow packet to include sprint intent and expected outputs.

The previous J3 draft was therefore too shallow because it reduced a complete three-sprint flow to one `exact_next_action`.

# Revised Round 2

## J1 — Project State Success Card

**Decision:** Keep, with one clarification.

The short result card is only the top summary. It does not replace the detailed project-state content beneath it.

```yaml
project_state_success_card:
  result_card:
    outcome: concise_summary
    next_action: best_immediate_operator_action
    review_needed: most_important_state_question

  project_state_detail:
    per_project:
      - project_name
      - current_phase
      - current_goal
      - active_workstreams
      - accepted_priorities
      - next_action_candidates
      - blockers
      - stale_or_conflicting_information
      - important_artifact_refs

  planning_handoff:
    - usable_for_PreCapWeek
    - usable_for_PreCapNextDay
    - review_needed_before_planning
```

This remains a **state input**, not the weekly plan itself.

---

# J2 — Weekly Command Brief

## Corrected primary purpose

> Show the complete, understandable weekly direction across all active projects, with enough project-level goals, priorities, tasks, targets, constraints, and expected outputs for Marco to judge whether the planned week reflects what he actually wants.

## Remove the three-priority maximum

The previous rule:

```yaml
maximum_recommended_primary_priorities: 3
```

is rejected.

Replace it with:

```yaml
weekly_priority_policy:
  fixed_global_maximum: null
  minimum_major_weekly_outcomes_across_portfolio: 3
  normal_major_outcomes_per_active_project: 1_to_5
  normal_action_items_per_project: 1_to_7
  extended_action_items_per_project_when_needed: up_to_10
  planning_basis:
    - number_of_active_projects
    - project_complexity
    - available_weekly_capacity
    - deadlines
    - dependencies
    - operator_intent
  compression_rule: >
    Do not remove meaningful work merely to meet an arbitrary display limit.
    Group related work under project outcomes when readability requires it.
```

“One priority per project per day” may produce at least five meaningful items in a normal working week, but it should remain a **planning heuristic**, not a rigid quota.

## Revised structure

### 1. Weekly result card

This remains compact:

```yaml
weekly_result_card:
  result_state: ready_or_review_needed_or_blocked
  portfolio_direction: two_to_five_sentence_summary
  active_projects: <count>
  major_outcomes_planned: <count>
  next_operator_action: approve_edit_or_resolve
  review_needed:
    - "<highest-impact decision>"
```

The summary may now be several sentences, not necessarily one.

### 2. Portfolio-level weekly direction

```yaml
portfolio_week:
  weekly_intent:
    - "<what the entire week should achieve>"
  major_cross_project_outcomes:
    - "<outcome 1>"
    - "<outcome 2>"
    - "<outcome 3>"
    - "<additional outcomes when needed>"
  capacity_and_constraints:
    - "<constraint affecting several projects>"
  major_operator_decisions:
    - "<decision>"
```

### 3. One substantial section per project

```yaml
projects:
  - project: "<project name>"

    weekly_target:
      outcome: "<what should be different by the end of the week>"
      success_evidence:
        - "<observable result>"
        - "<artifact, decision, milestone, or completed stage>"

    why_this_week:
      - "<planning signal>"
      - "<deadline, dependency, momentum, or strategic reason>"

    priorities:
      - priority: "<major priority>"
        desired_result: "<result>"
        status: "<ready|review_needed|blocked>"

    planned_work:
      - "<action or deliverable 1>"
      - "<action or deliverable 2>"
      - "<action or deliverable 3>"
      - "<flexibly continue from 1–7, or up to 10 when justified>"

    dependencies:
      - "<dependency>"

    blockers_and_risks:
      - "<blocker or risk>"

    decisions_needed:
      - "<operator choice>"

    expected_outputs:
      - "<artifact, decision, specification, implementation, or handoff>"

    candidate_days:
      - day: "<optional proposed day>"
        focus: "<project focus>"
```

This is an **OKF-style hierarchical bullet structure**, not a wide table.

### 4. Cross-project sequencing

```yaml
cross_project_sequence:
  must_happen_first:
    - "<work that unlocks other work>"

  can_run_in_parallel:
    - "<parallel workstreams>"

  should_not_compete:
    - "<items that should not be planned together>"

  deferred_deliberately:
    - item: "<item>"
      reason: "<reason>"
```

### 5. Daily seed map

Instead of handing off only one first-day sentence:

```yaml
daily_seed_map:
  monday:
    candidate_projects:
      - "<project>"
    likely_outcomes:
      - "<outcome>"

  tuesday:
    candidate_projects:
      - "<project>"
    likely_outcomes:
      - "<outcome>"

  remaining_days:
    status: flexible
    planning_rule: >
      PreCap Next Day decides the final flows and sprints using updated project
      state, completed work, blockers, calendar constraints, and operator intent.
```

The weekly brief can suggest daily distribution without pretending the week will remain unchanged.

---

# J3 — PreCap Next Day Brief

## Corrected name

```yaml
previous_operator_name: Tomorrow Action Brief
new_operator_name: PreCap Next Day Brief
machine_artifact: next_day_plan
```

## Corrected primary purpose

> Compile project-manager state, weekly direction, recent execution evidence, constraints, and available capacity into a detailed next-day plan containing the day strategy, represented flows, and three-sprint plan for every active flow.

## Revised depth

The daily brief must not contain only:

- one daily sentence,
    
- one next action per flow,
    
- or one compact flow preview.
    

It should expose enough detail to evaluate the whole day.

## Revised structure

### 1. Day result card

```yaml
precap_next_day_result:
  result_state: ready_or_review_needed_or_partial_or_blocked
  day_direction: two_to_five_sentence_summary
  represented_flows:
    planned: <count>
    compressed: <count>
    skipped: <count>
    blocked: <count>
  total_sprints_planned: <count>
  key_expected_outputs:
    - "<output>"
  next_operator_action: "<approve, edit, reorder, or resolve>"
  review_needed:
    - "<decision>"
```

Again, this is only the first-screen summary.

### 2. Day strategy

```yaml
day_strategy:
  primary_day_outcomes:
    - "<major outcome 1>"
    - "<major outcome 2>"
    - "<additional outcomes when justified>"

  projects_touched:
    - project: "<project>"
      reason_for_inclusion: "<reason>"
      intended_day_progress: "<progress target>"

  continuity_from_week:
    - weekly_priority: "<priority>"
      day_contribution: "<how today advances it>"

  capacity_assumptions:
    - "<available time or attention assumption>"

  fixed_constraints:
    - "<calendar, dependency, tool, source, or decision constraint>"
```

### 3. Full flow overview

The day plan may still represent F1–F4, but each flow receives more than a preview.

```yaml
flows:
  - flow_id: F1
    project: "<project>"
    flow_title: "<meaningful operator title>"
    flow_status: "<planned|compressed|skipped|blocked|omitted>"

    why_this_flow_today:
      - "<reason>"
      - "<connection to weekly priority>"

    flow_goal:
      - "<primary goal>"
      - "<secondary goal when needed>"

    expected_flow_outputs:
      - "<output>"
      - "<output>"

    required_context:
      available:
        - "<source or artifact>"
      missing:
        - "<missing context>"

    dependencies:
      - "<dependency>"

    review_flags:
      - "<flag>"
```

### 4. Three sprints inside every active flow

```yaml
flow_sprint_plan:
  S1:
    role: first_work_sprint
    goal: "<specific sprint goal>"
    tasks:
      - "<task 1>"
      - "<task 2>"
      - "<additional tasks as justified>"
    inputs:
      - "<input>"
    prompt_or_tool_ref:
      - "<prompt pack reference>"
    expected_outputs:
      - "<output>"
    done_when:
      - "<observable completion condition>"
    review_or_stop_condition:
      - "<condition>"

  S2:
    role: second_work_or_deepening_sprint
    goal: "<specific sprint goal>"
    tasks:
      - "<task 1>"
      - "<task 2>"
    dependency_on_S1:
      - "<dependency or none>"
    prompt_or_tool_ref:
      - "<prompt pack reference>"
    expected_outputs:
      - "<output>"
    done_when:
      - "<observable completion condition>"
    review_or_stop_condition:
      - "<condition>"

  S3:
    role: recap_capture_handoff_sprint
    goal: "<capture, synthesis, validation, or handoff goal>"
    tasks:
      - "<capture output>"
      - "<record decisions>"
      - "<prepare raw evidence or handoff>"
    expected_outputs:
      - "<raw-flow evidence, decision record, validation, or handoff>"
    done_when:
      - "<capture and handoff are sufficient>"
```

This matches the existing live flow template, which still explicitly carries S1, S2, and S3.

### 5. Detailed daily sequencing

```yaml
execution_sequence:
  - order: 1
    flow: F1
    sprint: S1
    reason_for_order: "<reason>"

  - order: 2
    flow: F1
    sprint: S2
    reason_for_order: "<reason>"

  - order: 3
    flow: F2
    sprint: S1
    reason_for_order: "<reason>"

  - order: 4
    flow: "<flow>"
    sprint: "<sprint>"
    reason_for_order: "<reason>"
```

This allows either:

- completing one flow before moving to another,
    
- interleaving flows,
    
- or compressing a sprint when justified.
    

### 6. Project-manager context used

```yaml
planning_context_used:
  project_manager_inputs:
    - project: "<project>"
      current_state_used:
        - "<state>"
      priority_used:
        - "<priority>"
      blocker_used:
        - "<blocker>"
      next_action_candidate_used:
        - "<candidate>"

  weekly_plan_inputs:
    - "<weekly outcome or priority>"

  recent_execution_inputs:
    - "<FlowRecap, status, or skip marker>"

  ignored_or_deferred_signals:
    - signal: "<signal>"
      reason: "<reason>"
```

This is essential because it lets you see **why** the plan chose particular work.

### 7. End-of-day expected state

```yaml
expected_end_of_day:
  project_progress:
    - project: "<project>"
      expected_change:
        - "<change>"
      expected_artifacts:
        - "<artifact>"

  decisions_expected:
    - "<decision>"

  evidence_to_capture:
    - "<evidence>"

  handoffs_prepared:
    - "<FlowRecap or next-cycle handoff>"
```

# Revised planning-depth principle

I propose adding this rule to Round 2:

```yaml
planning_depth_rule:
  result_card_is_compact: true
  underlying_plan_is_not_forced_to_be_compact: true

  weekly_plan_must_make_visible:
    - each_active_project
    - project_level_outcomes
    - project_level_priorities
    - planned_work_items
    - expected_outputs
    - blockers
    - decisions
    - cross_project_dependencies

  daily_plan_must_make_visible:
    - project_manager_context_used
    - weekly_priorities_advanced
    - all_represented_flows
    - three_sprints_per_full_flow
    - sprint_tasks
    - sprint_outputs
    - sequence
    - review_conditions
    - end_of_day_expected_state

  compression_allowed_only_when:
    - operator_requests_compact_view
    - flow_is_explicitly_compressed
    - detail_is_available_through_a_direct_reference

  arbitrary_priority_caps_forbidden: true
```

## Updated Round 2 status

```yaml
round_2_feedback:
  J1_project_state_success_card:
    decision: keep_with_clarification

  J2_weekly_command_brief:
    decision: major_revision
    changes:
      - remove_three_priority_maximum
      - add_per_project_OKF_work_plan
      - allow_one_to_seven_normal_work_items
      - allow_up_to_ten_when_justified
      - add_cross_project_sequencing
      - preserve_full_planning_visibility

  J3_tomorrow_action_brief:
    decision: rename_and_major_revision
    new_name: PreCap_Next_Day_Brief
    verified_skill: precap-next-day
    verified_machine_output: next_day_plan
    three_sprint_structure_preserved: true
    add_full_flow_and_sprint_detail: true
```

No Round 2 repo file has been written yet.