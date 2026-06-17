# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/next-day-plan.md

# PreCap Next Day — 2026-06-18

Example role: APEX-only filled example for the PreCap Next Day output template layer.

This is a review fixture. It does not execute APEX work, run FlowRecap, merge status, or write calendar events.

## 1. Plan Status

```yaml
plan_status:
  plan_id: next_day_plan_2026_06_18_apex_template_layer
  artifact_name: next_day_plan
  execution_day: "2026-06-18"
  generation_mode: bootstrap_mode
  review_status: operator_review_recommended
  project_execution_status: not_executed
  prompt_execution_status: not_executed
  calendar_write_status: review_only
  FlowRecap_status: handoff_prepared_not_run
  validation_status: operator_review_recommended
```

## 2. Operator Review First

| Priority | Review item | Why it matters | Operator action |
|---:|---|---|---|
| 1 | Confirm path strategy: keep `.claude/skills/PrecapNextDay/` for this pass or later normalize to `.claude/skills/precap-next-day/`. | The repo currently uses CamelCase while manifest-like references historically point lowercase. | Decide before package normalization. |
| 2 | Review APEX-only flow labels. | F1-F4 are presentation labels for this example, not schema changes. | Approve or rename labels. |
| 3 | Review prompt-pack placeholder depth. | Prompt doctrine stays upstream; these packs use placeholders. | Approve placeholder-first mode. |

## 3. Input Context

| Input category | Status | Used for planning? | Confidence | Notes |
|---|---|---:|---|---|
| operator_day_intent | supplied | yes | high | Build a critique-ready example system for PreCap Next Day templates. |
| current_project_status_overview | missing | no | low | No live APEX project state was supplied. |
| repo_package_scan | partial | yes | medium | Existing package found under `.claude/skills/PrecapNextDay/`. |
| calendar_context | missing | no | unknown | Calendar request remains review-only. |
| usage_context | missing | no | low | Usage summary uses degraded defaults. |

```yaml
input_resilience_summary:
  missing_inputs:
    - current_project_status_overview
    - concrete_Apex_build_state
    - usage_inventory
    - calendar_constraints
  assumptions:
    - Use bootstrap_mode because this is a template-layer fixture.
    - Treat all active flows as APEX-only build slices.
    - Keep APEX labels presentation-only when contract schema is constrained.
  degraded_mode_reasons:
    - No concrete execution-state input was supplied.
  planning_conflicts:
    - Repo actual path and historical manifest path differ.
```

## 4. APEX Day Strategy

Create a complete, reviewable template layer for the PreCap Next Day skill package. The day is split into four APEX-only flows: repo foundation, contract boundary mapping, output template/example creation, and validation/handover. No project work is executed; the outputs are templates, examples, and review fixtures.

## 5. APEX Flow Overview

| Flow | APEX role | Status | Sprint count | Primary goal | Expected output | Flow packet | Prompt pack | Review flags |
|---|---|---|---:|---|---|---|---|---|
| F1 | APEX repo foundation | planned | 3 | Resolve package path and file-set expectations. | Repo/package path decision notes. | `flows/F1-flow-packet.md` | `prompts/F1-flow-prompt-pack.md` | path mismatch |
| F2 | APEX skill database contracts | planned | 3 | Map contract authority vs template authority. | Field-surface boundary map. | `flows/F2-flow-packet.md` | `prompts/F2-flow-prompt-pack.md` | schema drift risk |
| F3 | APEX output templates/examples | planned | 3 | Create blank templates and filled examples. | Template/example package. | `flows/F3-flow-packet.md` | `prompts/F3-flow-prompt-pack.md` | placeholder depth |
| F4 | APEX validation/handover | planned | 3 | Audit outputs and prepare critique handoff. | Final audit and next update queue. | `flows/F4-flow-packet.md` | `prompts/F4-flow-prompt-pack.md` | validation incomplete until operator review |

## 6. Generated File Index

| Artifact | Path/ref | Status | Depends on | Operator action |
|---|---|---|---|---|
| next_day_plan | `next-day-plan.md` | review_ready | daily-plan-output-contract | Review dashboard structure. |
| F1-F4 flow packets | `flows/*.md` | review_ready | flow-packet-contract | Review APEX labels and sprint framing. |
| F1-F4 prompt packs | `prompts/*.md` | review_ready_degraded | flow-prompt-pack-contract | Review prompt placeholder policy. |
| raw flow dump template | `capture/raw-flow-dump-template.md` | prepared_not_filled | flow-packet-contract | Use after execution only. |
| skipped flow marker template | `capture/skipped-flow-marker-template.md` | prepared_not_filled | flow-packet-contract | Use only if flow is skipped. |
| calendar request | `calendar/calendar-event-write-request.md` | review_only | calendar-event-write-contract | No write approval requested. |
| usage summary | `usage/usage-tracking-summary.md` | low_confidence_auto_generated | usage-tracking-dependency-contract | Supply usage inventory later. |
| FlowRecap handoff | `handoff/FlowRecap-handoff.md` | prepared_not_run | flow-packet-contract | Use after execution only. |
| final audit | `handoff/template-layer-final-audit-summary.md` | draft | validation-checklist | Critique and update. |

## 7. Usage / Calendar / Workflow Summaries

```yaml
usage_calendar_workflow_summary:
  usage_tracking_status: missing_context_degraded
  routing_status: generic_defaults_used
  calendar_request_status: review_only
  workflow_process_status: low_confidence_inferred
  review_required: true
```

## 8. Capture and FlowRecap Preparation

| Capture artifact | Prepared? | Filled by PreCap? | Notes |
|---|---:|---:|---|
| raw_flow_dump_template | true | false | Prepared for future execution capture. |
| skipped_flow_marker_template | true | false | Prepared for skipped-flow cases. |
| FlowRecap_handoff_block | true | false | Prepared, not executed. |

## 9. Operator Review Flags

| Flag ID | Severity | Flag | Suggested action |
|---|---|---|---|
| ORF-001 | high | Path naming mismatch remains unresolved. | Decide preserve-vs-normalize in a later pass. |
| ORF-002 | medium | APEX labels are presentation-only and may need stronger contract-safe placement. | Review flow packet examples. |
| ORF-003 | medium | Prompt packs are placeholders, not final prompt doctrine. | Approve or request deeper prompt examples. |
| ORF-004 | low | Usage and calendar context are intentionally degraded. | Supply real context later if needed. |

## 10. Completion Gate

```yaml
completion_gate:
  next_day_plan_exists: true
  fixed_flows_are_represented_or_explicitly_omitted: true
  represented_flows_have_flow_packet_references: true
  represented_flows_have_flow_prompt_pack_references: true
  prompt_packs_are_ready_or_marked_degraded_with_review_flags: true
  usage_tracking_hooks_exist_or_degraded_usage_review_flag_exists: true
  calendar_writes_are_request_based_and_not_claimed_completed_without_approval: true
  FlowRecap_handoff_exists_without_running_FlowRecap: true
  missing_inputs_are_review_flags_not_blockers: true
  no_project_execution_FlowRecap_output_or_status_merge_created: true
```
