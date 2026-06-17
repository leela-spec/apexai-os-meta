# FILE: .claude/skills/PrecapNextDay/templates/usage-tracking-summary-template.md

# Usage Tracking Summary — <execution_day>

Template role: lightweight usage intent and capture preparation.

Schema authority: `references/usage-tracking-dependency-contract.md`.

Default to degraded/low-confidence if no usage inventory or quota context is supplied. Do not make current quota, price, or limit claims without operator-verified source context.

## 1. Dependency Status

```yaml
usage_tracking_summary_status:
  summary_id: "usage_tracking_summary_<execution_day>"
  execution_day: "<YYYY-MM-DD>"
  dependency_status: "<available|partially_available|missing|stale|operator_review_needed>"
  routing_status: "<routing_packet_available|generic_defaults_used|missing|operator_review_needed>"
  usage_inventory_status: "<available|partial|missing|unknown>"
  quota_claims_made: false
  actual_usage_logged: false
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence_auto_generated|blocked_by_missing_operator_decision>"
```

## 2. Planning Basis

| Input | Used? | Status | Notes |
|---|---:|---|---|
| AI surface inventory | <true/false> | <available|partial|missing|unknown> | <notes> |
| Monthly quota map | <true/false> | <available|partial|missing|unknown> | <notes> |
| Model usage summary | <true/false> | <available|partial|missing|unknown> | <notes> |
| Routing recommendation packet | <true/false> | <available|partial|missing|unknown> | <notes> |
| Operator usage preferences | <true/false> | <supplied|missing|unknown> | <notes> |

## 3. Flow Usage Overview

| Flow | APEX role | Usage intent | High-value scarce candidate? | Low-cost candidate? | Review flag |
|---|---|---|---:|---:|---|
| F1 | APEX repo foundation | <intent> | <true/false/unknown> | <true/false/unknown> | <flag> |
| F2 | APEX skill database contracts | <intent> | <true/false/unknown> | <true/false/unknown> | <flag> |
| F3 | APEX output templates/examples | <intent> | <true/false/unknown> | <true/false/unknown> | <flag> |
| F4 | APEX validation/handover | <intent> | <true/false/unknown> | <true/false/unknown> | <flag> |

## 4. Capture Fields for Later Review

```yaml
usage_capture_fields:
  planned_surface_or_provider: "<provider_or_surface_hint>"
  actual_surface_or_provider: "<fill_after_execution>"
  planned_reason: "<reason>"
  actual_result_quality: "<fill_after_execution>"
  actual_usage_notes: "<fill_after_execution>"
  capture_destination: "FlowRecap_handoff_block_or_usage_delta_later"
```

## 5. Operator Review Flags

| Flag ID | Severity | Flag | Suggested action |
|---|---|---|---|
| USAGE-ORF-001 | <low|medium|high> | <flag> | <action> |

## 6. Completion Gate

```yaml
usage_summary_completion_gate:
  dependency_status_declared: true
  volatile_quota_claims_avoided: true
  flow_usage_overview_present: true
  capture_fields_present: true
  missing_usage_context_review_flagged_when_needed: true
  actual_usage_not_logged_before_execution: true
```
