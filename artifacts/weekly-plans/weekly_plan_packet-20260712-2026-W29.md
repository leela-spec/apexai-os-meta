# weekly_plan_packet-20260712-2026-W29

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: weekly_plan_packet
  gate: G1
  packet_id: "weekly_plan_packet-20260712-2026-W29"
  produced_by: apex-precap-week
  accountability: meta_strategy
  lifecycle_stage: proposal
  status: partial
  target_surface: none
  next_state: "Week 2026-W29 direction is confirmed: Apex primary (fable-orchestrator closure Mon-Tue, NARM-support task 001 Wed-Thu, regression-suite packet decision), all other fixed projects at maintenance/deferred; first_precap_next_day_seed becomes the approved input for PreCapNextDay."
  prerequisites: []
  expected_action: operator confirms G1, then precap-next-day consumes first_precap_next_day_seed
  sources:
    - state/apex-project-status.md
    - apex-meta/epics/narm-support-knowledgebase/001.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260712-orchestrator-regression-suite.md
  uncertainties:
    - "state/apex-project-status.md is empty (bootstrap) — cross-project priority basis rests solely on operator weekly intent."
    - "No flow_recap_packets exist (first cycle) — no evidence trail behind claimed fable-orchestrator completion state."
    - "NARM-support knowledgebase is assumed to belong under the Apex fixed project (epic lives in apex-meta); operator has not confirmed the mapping."
    - "Calendar constraints not supplied — all capacity shapes assumed standard; no overload detection possible."
    - "apex_plan_packet-20260712-orchestrator-regression-suite.md is an unreviewed proposal; scheduling its review does not endorse its content."
  unresolved_risk: "Weekday capacity may be overcommitted because zero calendar data was available; all five weekdays planned at standard capacity on assumption only."
  stop_condition: "PreCapNextDay must halt if G1 is not confirmed, if the operator rejects the NARM-under-Apex mapping, or if real calendar constraints contradict the assumed standard capacity."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

```yaml
precap_week_output:
  output_metadata:
    artifact_name: precap_week_output
    schema_version: "0.1"
    week_id: "2026-W29"
    created_at: "2026-07-12"
    output_status: operator_review_needed
    primary_consumer: PreCapNextDay
  input_basis:
    weekly_intent:
      status: provided
      summary: "Close fable-orchestrator initiative (full-loop verification, simulation records, target-log closure); start NARM-support KB task 001 (safety and scope boundaries) — sole unblocked task; review pending orchestrator-regression-suite plan packet."
    detailed_project_state_files:
      status: partial
      role: preferred_future_primary_project_state_input
      notes:
        - "Only Apex-side files available: apex-meta/epics/narm-support-knowledgebase/001.md and the pending plan packet. No state files for Leela, MasterOfArts, Investment."
    current_project_status_overview:
      status: missing
      role: primary_compact_input_allowed_in_v0_1
      notes:
        - "state/apex-project-status.md is empty — bootstrap mode; degraded confidence."
    project_priority_signal:
      status: inferred_from_overview
      notes:
        - "Inferred from operator weekly intent only; no ratings supplied by operator."
    calendar_constraints:
      status: unavailable
      notes:
        - "No calendar data supplied in dispatch; standard-capacity assumption applied to all weekdays."
    weekly_blueprint:
      status: standard
      notes:
        - "Standard weekday blueprint assumed; no meeting-week deformation data available."
  weekly_direction:
    week_focus: "Close the fable-orchestrator initiative to done, then open NARM-support execution with task 001 safety/scope boundaries."
    success_definition: "By Friday: fable-orchestrator verified closed (full-loop verification done, simulation records + target-log closure filed), NARM-support task 001 completed or at operator-review stage, and a confirm/reject/revise decision recorded on the regression-suite plan packet."
    strategic_notes:
      - "Sequence matters: finish orchestrator closure before NARM ramp-up to avoid split focus across two open initiatives."
      - "NARM task 001 gates tasks 2-8; it is the single unblocking move for that epic."
      - "First full weekly loop cycle — treat this week as calibration for the loop itself."
    major_constraints:
      - "Empty project status state (bootstrap) — no confirmed prior truth to plan against."
      - "No calendar data — capacity assumptions unverified."
    planning_posture: uncertain
  project_weekly_priorities:
    Leela:
      rating: "[50/20/NA]"
      weekly_goal: "No operator intent this week; hold at maintenance, no planned pushes."
      planned_role: maintenance
      notes:
        - "Rating inferred with low confidence; no project state available."
    MasterOfArts:
      rating: "[50/20/NA]"
      weekly_goal: "No operator intent this week; hold at maintenance, no planned pushes."
      planned_role: maintenance
      notes:
        - "Rating inferred with low confidence; no project state available."
    Apex:
      rating: "[95/90/17-07]"
      weekly_goal: "Close fable-orchestrator (verification, simulation records, target-log closure); complete NARM-support task 001 safety/scope boundaries; decide on regression-suite plan packet."
      planned_role: primary
      notes:
        - "NARM-support KB mapped under Apex by assumption (epic lives in apex-meta) — operator to confirm."
    Investment:
      rating: "[40/15/NA]"
      weekly_goal: "Deferred unless operator raises a specific item."
      planned_role: deferred
      notes:
        - "No signal received; deferred first under uncertain posture."
    Residual:
      rating: "[30/30/NA]"
      weekly_goal: "Absorb overflow from orchestrator closure and any recovery work from the first loop cycle."
      planned_role: overflow
      notes:
        - "Lowest priority per residual policy; operator has not raised it."
  weekday_plan_direction:
    Monday:
      day_role: start
      priority_projects:
        - Apex
      capacity_shape: unknown
      intended_direction: "Run fable-orchestrator full-loop verification and capture simulation records."
      calendar_notes:
        - "No calendar data; treat capacity as assumed-standard, unverified."
      deferred_or_reduced:
        - Residual
        - Investment
    Tuesday:
      day_role: build
      priority_projects:
        - Apex
      capacity_shape: unknown
      intended_direction: "Complete target-log closure for fable-orchestrator; review the orchestrator-regression-suite plan packet and record a confirm/reject/revise decision."
      calendar_notes:
        - "No calendar data; assumed standard."
      deferred_or_reduced:
        - Investment
    Wednesday:
      day_role: build
      priority_projects:
        - Apex
      capacity_shape: unknown
      intended_direction: "Open NARM-support execution: draft safety and scope boundaries per epic task 001."
      calendar_notes:
        - "No calendar data; assumed standard."
      deferred_or_reduced:
        - Investment
    Thursday:
      day_role: build
      priority_projects:
        - Apex
      capacity_shape: unknown
      intended_direction: "Finish NARM-support task 001 to operator-review quality; assess which of tasks 2-8 unblock."
      calendar_notes:
        - "No calendar data; assumed standard."
      deferred_or_reduced:
        - Investment
    Friday:
      day_role: review
      priority_projects:
        - Apex
        - Residual
      capacity_shape: unknown
      intended_direction: "Close open loops from both initiatives, absorb overflow via Residual, and consolidate the week's evidence for the first status merge."
      calendar_notes:
        - "No calendar data; assumed standard."
      deferred_or_reduced:
        - Investment
  first_precap_next_day_seed:
    target_day: Monday
    seed_status: operator_review_needed
    weekly_context_summary: "Bootstrap week, Apex primary: close fable-orchestrator first (verification + simulation records Mon), then target-log closure and regression-suite packet decision Tue, then NARM-support task 001 Wed-Thu."
    priority_projects:
      - Apex
    starting_constraints:
      - "No calendar data — verify actual Monday availability before locking daily blocks."
      - "Empty project status state — plan from weekly intent only."
    recommended_first_day_direction: "Build Monday around fable-orchestrator full-loop verification and simulation-record capture; nothing else competes."
    missing_context_for_precap_next_day:
      - "Actual Monday calendar constraints."
      - "Confirmed apex-project-status baseline (state file is empty)."
      - "Operator confirmation of NARM-support-under-Apex mapping (affects later-week days, not Monday)."
  calendar_source_status:
    status: calendar_unavailable
    operator_review_required: true
    notes:
      - "No calendar input supplied in dispatch; all capacity shapes are assumptions. No calendar block proposals issued — insufficient basis."
  assumptions:
    - assumption: "All five weekdays have standard work capacity (no meetings or fixed commitments)."
      risk: high
      review_required: true
    - assumption: "NARM-support knowledgebase work belongs under the Apex fixed project."
      risk: medium
      review_required: true
    - assumption: "Fable-orchestrator completion claims in the weekly intent are accurate enough to plan closure-verification work against."
      risk: low
      review_required: true
    - assumption: "Leela, MasterOfArts, and Investment genuinely need no push this week because the operator named none."
      risk: medium
      review_required: true
  missing_inputs:
    - input_name: current_project_status_overview
      effect: "No confirmed cross-project truth; priorities rest entirely on operator weekly intent."
      required_before_approval: false
    - input_name: flow_recap_packets
      effect: "No evidence trail from a prior cycle; first-cycle bootstrap, no continuity check possible."
      required_before_approval: false
    - input_name: fixed_calendar_constraints
      effect: "Capacity shapes unknown; overload detection impossible; daily plans must re-verify availability."
      required_before_approval: false
    - input_name: project_priority_signal_ratings
      effect: "All ratings inferred, not operator-supplied; treat as provisional."
      required_before_approval: false
  operator_validation:
    status: operator_review_needed
    review_flags:
      - missing_project_state
      - missing_or_partial_calendar
      - unclear_project_priority
    approval_required_before_precap_next_day: true
```
