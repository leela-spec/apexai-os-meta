# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/usage/usage-tracking-summary.md

# Usage Tracking Summary — APEX example

No usage inventory or quota context was supplied. This example uses low-confidence degraded usage planning and avoids current quota or pricing claims.

```yaml
usage_tracking_summary_status:
  summary_id: usage_tracking_summary_2026_06_18_apex_template_layer
  execution_day: "2026-06-18"
  dependency_status: missing
  routing_status: generic_defaults_used
  usage_inventory_status: missing
  quota_claims_made: false
  actual_usage_logged: false
  validation_status: low_confidence_auto_generated
```

## Planning Basis

| Input | Used? | Status | Notes |
|---|---:|---|---|
| AI surface inventory | false | missing | No current inventory supplied. |
| Monthly quota map | false | missing | No remaining quota claims made. |
| Model usage summary | false | missing | Not available. |
| Routing recommendation packet | false | missing | Generic placeholders only. |
| Operator usage preferences | false | missing | Can be added later. |

## Flow Usage Overview

| Flow | APEX role | Usage intent | High-value scarce candidate? | Low-cost candidate? | Review flag |
|---|---|---|---:|---:|---|
| F1 | APEX repo foundation | Repo inspection and path reasoning. | unknown | unknown | Usage context missing. |
| F2 | APEX skill database contracts | Contract/template boundary synthesis. | unknown | unknown | Usage context missing. |
| F3 | APEX output templates/examples | Artifact drafting. | unknown | unknown | Usage context missing. |
| F4 | APEX validation/handover | Review and handoff drafting. | unknown | unknown | Usage context missing. |

## Capture Fields for Later Review

```yaml
usage_capture_fields:
  planned_surface_or_provider: provider_unspecified
  actual_surface_or_provider: "<fill_after_execution>"
  planned_reason: "Template-layer generation and validation."
  actual_result_quality: "<fill_after_execution>"
  actual_usage_notes: "<fill_after_execution>"
  capture_destination: FlowRecap_handoff_block_or_usage_delta_later
```

## Operator Review Flags

| Flag ID | Severity | Flag | Suggested action |
|---|---|---|---|
| USAGE-ORF-001 | medium | Usage context is missing. | Provide AI surface inventory or accept degraded mode. |
