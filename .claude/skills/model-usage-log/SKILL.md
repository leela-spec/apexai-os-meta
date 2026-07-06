---
name: model-usage-log
description: Use this skill when you need to capture compact post-execution model or AI-surface usage evidence from APEX flows, compare planned vs actual usage, record route reuse/avoid signals, or create advisory usage summaries for future PreCapNextDay and AIRouting review. This skill does not choose models, define quotas, claim pricing, execute prompts, or mutate project status.
---

# model-usage-log

## Purpose

Create minimal, advisory post-execution usage-learning artifacts for APEX.

This skill records what model, provider surface, or AI route appears to have been used after execution, compares that against planned usage when available, and produces compact reuse-or-avoid signals for future planning.

It is intentionally small. It is not a routing engine, quota system, pricing source, runtime meter, calendar writer, project-status merger, or automation layer.

## Use This Skill When

```yaml
use_when:
  - FlowRecap or operator notes include actual model_or_surface usage evidence.
  - Planned usage exists and actual usage should be compared against it.
  - A route reuse, avoid, or high-value-only signal should be captured for later planning.
  - Usage evidence is missing but the missing evidence should be recorded as low-confidence learning.
  - A compact usage_summary is needed for future PreCapNextDay or AIRouting review context.
```

## Do Not Use This Skill When

```yaml
avoid_when:
  - The task is to choose a model before execution.
  - The task is to define or update AI_surface_inventory.
  - The task is to define or update monthly_quota_map.
  - The task is to claim provider pricing or current product limits.
  - The task is to execute prompts, automate work, schedule work, or create calendar events.
  - The task is to mutate ProjectStatus or perform status merge.
  - The task is to replace AIRouting, FlowRecap, PreCapNextDay, project-kb-manager, or ProjectStatus.
```

## Supporting Files

```yaml
supporting_files:
  - path: ".claude/skills/model-usage-log/references/model-usage-delta-contract.md"
    read_when: "Creating or validating a model_usage_delta."
    provides:
      - model_usage_delta_schema
      - planned_vs_actual_usage_record_rules
      - route_reuse_or_avoid_signal_values
      - missing_usage_data_degraded_behavior

  - path: ".claude/skills/model-usage-log/references/usage-summary-contract.md"
    read_when: "Aggregating one or more deltas into a usage_summary."
    provides:
      - usage_summary_schema
      - route_signal_rollup_rules
      - scarcity_or_quota_notes_boundaries
      - next_PreCapNextDay_usage_context_shape

  - path: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    read_when: "The operator needs a copy-paste model_usage_delta skeleton."
    provides:
      - model_usage_delta_template
      - degraded_behavior_block
      - confidence_block

  - path: ".claude/skills/model-usage-log/examples/apex-minimal-model-usage-example.md"
    read_when: "A concrete minimal example is useful for interpreting sparse evidence."
    provides:
      - synthetic_usage_candidate
      - low_confidence_delta_example
      - mini_usage_summary_example

  - path: ".claude/skills/model-usage-log/package-manifest.md"
    read_when: "Checking package scope, file inventory, or source gaps."
    provides:
      - package_scope
      - artifact_flow
      - completion_gates
      - source_inspection_register
```

## Procedure

1. **Classify the request.** Decide whether the operator needs a `model_usage_delta`, a `usage_summary`, or both.
2. **Inspect supplied evidence.** Use only available FlowRecap, planned usage, prompt-pack, artifact, transcript, or operator-note references. Do not invent model, quota, cost, or provider facts.
3. **Load the smallest needed support file.** Use the delta contract for single-flow learning, the summary contract for rollups, and the template only when a copy-paste artifact is needed.
4. **Preserve ownership boundaries.** Reference AIRouting, PreCapNextDay, FlowRecap, and ProjectStatus artifacts without redefining their schemas.
5. **Compare planned vs actual usage.** If planned and actual data are both present, summarize the match or mismatch. If actual evidence is missing, still create a low-confidence degraded record when useful.
6. **Set the route signal.** Use only one of: `reuse_route`, `avoid_route`, `use_only_for_high_value_tasks`, `insufficient_data`, or `operator_review_needed`.
7. **Set confidence and validation status.** Degrade confidence when model labels, planned usage refs, source refs, quota notes, pricing, or exact usage evidence are missing.
8. **Output advisory context only.** Do not mutate quota maps, AIRouting files, project status, calendars, runtime execution state, or any external system.

## Primary Output: model_usage_delta

```yaml
model_usage_delta_required_fields:
  - usage_delta_id
  - artifact_name
  - execution_day
  - source_flow_recap_refs
  - planned_usage_refs
  - actual_usage_evidence
  - model_or_surface_used
  - usage_purpose
  - planned_vs_actual_summary
  - route_reuse_or_avoid_signal
  - confidence
  - validation_status
```

## Secondary Output: usage_summary

```yaml
usage_summary_required_fields:
  - summary_id
  - created_or_updated_at
  - covered_period
  - usage_deltas_included
  - useful_routes
  - routes_to_avoid
  - scarcity_or_quota_notes
  - next_PreCapNextDay_usage_context
  - confidence
  - validation_status
```

## Validation Status Values

```yaml
validation_status_values:
  - valid
  - valid_with_warnings
  - operator_review_recommended
  - low_confidence_auto_generated
  - blocked_by_missing_operator_decision
```

## Route Signal Values

```yaml
route_reuse_or_avoid_signal_values:
  - reuse_route
  - avoid_route
  - use_only_for_high_value_tasks
  - insufficient_data
  - operator_review_needed
```

## Failure Modes

```yaml
failure_modes:
  - trigger: "Exact model, provider, cost, token count, or quota impact is not supplied."
    correction: "Mark the missing field as unknown or null, add a confidence flag, and avoid truth claims."

  - trigger: "The user asks for pre-execution routing advice."
    correction: "Route to AIRouting instead of producing a model_usage_delta."

  - trigger: "The source looks like a planned usage budget but no execution evidence exists."
    correction: "Create only a low-confidence degraded record if the absence itself is useful."

  - trigger: "The usage signal conflicts across sources."
    correction: "Preserve the conflict and set validation_status to operator_review_recommended."

  - trigger: "Quota or pricing notes are stale, inferred, or unsourced."
    correction: "Keep them as advisory notes only and add quota_or_pricing_not_verified."

  - trigger: "A downstream consumer needs a usage_summary but there are no deltas."
    correction: "Create an empty sparse summary with low confidence and no route recommendation."

  - trigger: "The task requires changing ProjectStatus, calendar events, repo automation, or runtime state."
    correction: "Do not perform that action from this skill. Output advisory usage context only."

  - trigger: "A FlowRecap or ProjectStatus contract file is missing."
    correction: "Reference artifact names conservatively and do not define their schemas."
```

## Completion Gate

```yaml
completion_gate:
  artifact_is_advisory_only: true
  exact_model_claims_are_sourced_or_marked_unknown: true
  quota_or_pricing_claims_are_sourced_or_not_claimed: true
  planned_usage_refs_are_referenced_not_redefined: true
  FlowRecap_schema_is_not_redefined: true
  AIRouting_schema_is_not_redefined: true
  ProjectStatus_schema_is_not_redefined: true
  route_signal_uses_allowed_values_only: true
  confidence_and_validation_status_are_present: true
  missing_evidence_degrades_confidence_without_blocking: true
  no_automation_or_runtime_metering_added: true
```
