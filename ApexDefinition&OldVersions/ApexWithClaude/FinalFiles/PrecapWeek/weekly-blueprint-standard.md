## Purpose

```
purpose:  file_role: standard_no_meeting_weekday_blueprint  owns:    - weekly_blueprint_standard    - fixed_blocks    - planned_blocks    - weekday_scope    - default_time_precision_rule  goal: >    Define the standard Monday through Friday weekday blueprint used by the    precap-week skill when the week has normal capacity and does not require    meeting-heavy deformation rules.  blueprint_role:    provides_default_structure: true    guides_weekday_direction: true    supports_calendar_block_proposals: true    does_not_create_daily_plan: true    does_not_create_prompt_packets: true
```

## Scope

```
weekday_scope:  included_days:    - Monday    - Tuesday    - Wednesday    - Thursday    - Friday  excluded_days:    - Saturday    - Sunday_regular_day_planning  allowed_sunday_exception:    - Sunday_weekly_precap_session  scope_rules:    monday_to_friday_only: true    saturday_planning_excluded: true    sunday_regular_planning_excluded: true    sunday_weekly_precap_session_allowed: true    no_weekend_recovery_or_life_planning_in_this_file: true
```

## Time Precision Rule

```
default_time_precision_rule:  internal_precision: 15_minutes  use_internal_precision_when:    - exact_times_are_needed    - calendar_constraints_have_precise_boundaries    - calendar_block_proposals_need_start_and_end_times    - fixed_blocks_have_operator_provided_times  preserve_exact_known_times: true  human_facing_output:    preferred_grain: block_level    avoid_over_granular_output: true    show_exact_times_only_when_useful: true  rules:    - use_15_minute_internal_precision_when_exact_times_are_needed    - preserve_exact_known_times_when_provided    - do_not_expand_weekday_direction_into_minute_by_minute_schedule    - keep_operator_facing_weekly_output_readable
```

## Fixed Blocks

```
fixed_blocks:  definition: >    Fixed blocks are protected anchors in the standard weekday blueprint. They    should be preserved before discretionary project-flow planning unless the    operator explicitly changes them or a known calendar constraint makes them    impossible.  items:    morning_routine:      block_role: day_start_anchor      default_status: protected      planning_effect:        - reserve_before_first_work_flow        - avoid_scheduling_project_work_inside_block    lunch_prep:      block_role: midday_food_preparation_anchor      default_status: protected      planning_effect:        - reserve_before_lunch_break        - protect_transition_into_midday    lunch_break:      block_role: midday_recovery_anchor      default_status: protected      planning_effect:        - reserve_as_non_work_block        - prevent_work_flow_overlap    day_outro:      block_role: workday_shutdown_anchor      default_status: protected      planning_effect:        - reserve_end_of_day_shutdown_space        - support_next_day_continuity    sleep_routine:      block_role: day_end_recovery_anchor      default_status: protected      planning_effect:        - protect_evening_boundary        - prevent_overextension  preservation_rules:    preserve_before_planned_blocks: true    mark_conflict_if_calendar_constraint_overlaps: true    do_not_delete_without_operator_instruction: true    do_not_use_as_project_work_capacity: true
```

## Planned Blocks

```
planned_blocks:  definition: >    Planned blocks are flexible weekday blocks placed around fixed blocks and    fixed calendar constraints. They carry work, admin, physical, social, or    evening direction, but remain adjustable.  items:    work_flows:      block_role: primary_project_progress      flexibility: medium      allowed_projects:        - Leela        - MasterOfArts        - Apex        - Investment        - Residual      planning_effect:        - place_highest_priority_project_work_first        - preserve_default_project_order_when_capacity_allows        - reduce_or_defer_only_when_constraints_require    admin_or_2Do:      block_role: operational_maintenance      flexibility: high      planning_effect:        - place_after_primary_work_capacity_when_possible        - shift_or_reduce_when_project_work_or_calendar_constraints_require        - keep_visible_if_admin_pressure_is_named_by_operator    physical_social_or_evening_blocks:      block_role: life_energy_recovery_and_social_support      flexibility: medium      planning_effect:        - preserve_when_realistic        - avoid_overfilling_evenings_after_heavy_workdays        - shift_or simplify_when_weekday_capacity_is_tight  adjustment_rules:    planned_blocks_can_shift: true    planned_blocks_can_compress: true    planned_blocks_can_defer: true    planned_blocks_can_be_omitted_with_reason: true    do_not_treat_planned_blocks_as_fixed_commitments: true
```

## Standard Weekday Pattern

```
weekly_blueprint_standard:  pattern_type: standard_no_meeting_weekday  applies_when:    - no_meeting_heavy_deformation_is_required    - calendar_constraints_do_not_overload_day    - normal_weekday_capacity_is_available    - operator_has_not_supplied_a_different_blueprint  standard_weekday_pattern:    morning:      sequence:        - morning_routine        - work_flow_1        - work_flow_2      planning_intent: >        Start with protected routine, then use the clearest early energy for        priority project work.    midday:      sequence:        - lunch_prep        - lunch_break        - work_flow_3      planning_intent: >        Protect food and recovery, then continue meaningful work after the        midday reset.    afternoon:      sequence:        - admin_or_2Do        - work_flow_4      planning_intent: >        Use the afternoon for operational maintenance and the final planned        project-flow block when capacity allows.    evening:      sequence:        - physical_social_or_evening_blocks        - day_outro        - sleep_routine      planning_intent: >        Preserve recovery, social, physical, or evening space before shutdown        and sleep boundaries.  block_level_output_rule:    show_sections_not_micro_slots: true    keep_weekday_direction_compact: true    avoid_full_daily_schedule: true
```

## Project Flow Priority

```
project_flow_priority:  default_full_capacity_order:    1: Leela    2: MasterOfArts    3: Apex    4: Investment    5: Residual  default_order_rule: >    At full standard capacity, use the default project order as the starting    point for work-flow direction unless operator intent, current project state,    project_priority_signal, ratings, or calendar constraints justify a    different allocation.  project_roles:    Leela:      default_role: primary_product_work      default_priority_behavior: preserve_when_relevant    MasterOfArts:      default_role: business_or_content_work      default_priority_behavior: preserve_when_relevant    Apex:      default_role: orchestration_system_work      default_priority_behavior: preserve_when_relevant    Investment:      default_role: investment_or_financial_review_work      default_priority_behavior: include_when_active_or_priority_raised    Residual:      default_role: overflow_recovery_unassigned_or_other_non_fixed_material      default_priority_behavior: lowest_unless_operator_raises  residual_policy:    lowest_priority_by_default: true    operator_can_raise: true    includes:      - overflow_work      - recovery_work      - unassigned_items      - other_non_fixed_project_material
```

## Use Rules

```
use_rules:  when_to_use:    - standard_weekday_capacity_available    - no_meeting_heavy_week_rules_needed    - operator_requests_normal_weekly_planning    - calendar_constraints_allow_regular_block_structure  how_to_apply:    1: confirm_weekday_scope    2: preserve_fixed_blocks    3: place_known_calendar_constraints_around_fixed_blocks    4: identify_remaining_capacity_windows    5: apply_default_project_flow_priority_at_full_capacity    6: place_admin_or_2Do_where_capacity_allows    7: preserve_physical_social_or_evening_blocks_when_realistic    8: output_block_level_weekday_direction  conflict_handling:    calendar_constraint_conflicts_with_fixed_block:      response: flag_for_operator_review    calendar_constraint_reduces_planned_block_capacity:      response: shift_compress_defer_or_omit_planned_block_with_reason    operator_priority_conflicts_with_default_project_order:      response: follow_operator_priority_and_record_reason    residual_competes_with_fixed_project_work:      response: keep_residual_lower_unless_operator_raises  handoff_to_other_reference:    meeting_heavy_deformation_needed:      read: references/weekly-blueprint-meeting-example.md    output_schema_needed:      read: references/weekly-plan-output-contract.md    calendar_rule_needed:      read: references/calendar-planning-guidance.md
```

## Non-Goals

```
non_goals:  not_meeting_heavy_deformation_rules: true  not_precap_week_output_schema: true  not_full_daily_schedule: true  not_next_day_plan: true  not_prompt_packet_generation: true  not_project_execution: true  not_status_merge: true  not_calendar_event_creation: true  not_saturday_plan: true  not_regular_sunday_plan: true  boundary_statement: >    This file defines the standard weekday blueprint only. It does not define    meeting-heavy reductions, the complete weekly output contract, detailed    daily plans, prompt packets, project execution, status merging, or calendar    event creation.
```