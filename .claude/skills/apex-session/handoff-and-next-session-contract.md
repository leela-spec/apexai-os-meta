# Handoff and Next Session Contract

~~~yaml
handoff_and_next_session_contract:
  file_role: canonical_handoff_and_next_session_contract
  owns:
    - task_plan
    - findings
    - progress
    - next_session_context
    - planning_layer_feed

  handoff_format:
    base_path: "apex-meta/handoff/"
    files:
      - task_plan.md
      - findings.md
      - progress.md
      - next-session.md

  task_plan:
    path: "apex-meta/handoff/task_plan.md"
    role: current_session_plan_and_phase_tracking
    required_content:
      - current_step
      - open_items
      - handoff_requests
      - review_flags

  findings:
    path: "apex-meta/handoff/findings.md"
    role: durable_discoveries_and_decisions
    required_content:
      - decisions_made
      - state_delta_summary
      - entity_update_proposal
      - raw_source_path

  progress:
    path: "apex-meta/handoff/progress.md"
    role: append_only_session_activity_log
    required_content:
      - session_progress_log
      - operator_validation_result
      - review_flags

  next_session_context:
    path: "apex-meta/handoff/next-session.md"
    role: context_bootstrap_for_next_session
    required_sections:
      - Current Step
      - Open Items
      - Risks
      - Decisions Made
      - Next Actions

  planning_layer_feed:
    role: "Provide confirmed session context to apex-plan without decomposing new work."
    required_content:
      - current_step
      - open_items
      - risks
      - decisions_made
      - next_actions
      - handoff_requests
      - review_flags
~~~

## 1. Handoff Write Rules

~~~yaml
handoff_write_rules:
  output_mode:
    chat_output_only: true
    generated_files_are_file_blocks_not_repo_writes: true

  confirmation:
    required_for_repo_write: true
    accepted_confirm_tokens:
      - CONFIRM
      - CONFIRM WRITE
      - CONFIRM MUTATION

  append_policy:
    progress:
      append_only: true
    findings:
      update_with_operator_confirmed_decisions: true
    task_plan:
      update_with_current_session_plan: true
    next_session:
      replace_with_latest_context_bootstrap_after_review: true
~~~

## 2. Next Session Context Sections

~~~yaml
next_session_required_sections:
  Current Step:
    required: true
    purpose: "State the exact point where the next session should resume."
  Open Items:
    required: true
    purpose: "List unresolved work without computing deterministic next-task order."
  Risks:
    required: true
    purpose: "List uncertainty, blockers, drift, or sync-required flags."
  Decisions Made:
    required: true
    purpose: "Carry forward validated decisions."
  Next Actions:
    required: true
    purpose: "Describe proposed human-readable actions without apex-sync ranking."
~~~

## 3. Planning Layer Feed

~~~yaml
planning_layer_feed_rules:
  destination_owner: apex-plan
  produced_by: apex-session
  may_include:
    - confirmed_status_updates
    - state_delta_summary
    - entity_update_proposal
    - operator_validation_result
    - handoff_requests
    - review_flags

  must_not_include:
    - deterministic_next_action_report
    - blocker_report
    - registry_rebuild_result
    - drift_score
    - priority_score
    - urgency_score
    - unlock_depth_score
    - focus_candidate_ordering
~~~

## 4. Non-Goals

~~~yaml
non_goals:
  - "Do not compute the next task."
  - "Do not rank focus candidates."
  - "Do not rebuild registry content."
  - "Do not resolve blocker state."
  - "Do not replace apex-plan decomposition."
  - "Do not omit review_flags when handoff context is incomplete."
~~~