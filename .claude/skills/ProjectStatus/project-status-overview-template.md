# Project Status Overview - {{PORTFOLIO_OR_SCOPE}}

> **Overview state:** {{CURRENT | CURRENT_WITH_REVIEW | PARTIAL | STALE | BLOCKED}}  
> **Confirmed landscape:** {{ONE_TO_THREE_SENTENCE_CROSS_PROJECT_SUMMARY}}  
> **Next action:** {{OPEN_NEXT_TASK | REVIEW_STALE_PROJECT | RESOLVE_BLOCKER | REFRESH_OVERVIEW | USE_AS_ROUTING_CONTEXT}}  
> **Review needed:** {{HIGHEST_IMPACT_CONFIRMED_STATE_OR_FRESHNESS_ISSUE_OR_NONE}}  
> **Counts:** {{ACTIVE_COUNT}} active; {{BLOCKED_COUNT}} blocked; {{REVIEW_COUNT}} review; {{STALE_COUNT}} stale

> **Truth gate:** This overview projects confirmed accepted project state. Candidate changes, approvals without a confirmed write, and prepared updates do not become new overview truth.

## Operator action

- [ ] Open the highest-ranked confirmed next task.
- [ ] Review a stale, conflicting, or blocked project card.
- [ ] Refresh the overview from confirmed durable sources.
- [ ] Use this overview as context for planning or routing.

**Decision or instruction:** {{OPERATOR_DECISION_OR_PENDING}}

## Portfolio focus

**Highest-ranked confirmed task:** {{TASK_AND_PROJECT}}  
**Most important blocker:** {{BLOCKER_AND_PROJECT_OR_NONE}}  
**Freshness concern:** {{PROJECT_OR_NONE}}  
**Cross-project dependency:** {{DEPENDENCY_OR_NONE}}

## Project - {{PROJECT_NAME}} (repeat per confirmed active project)

**Accepted status:** {{CONFIRMED_STATUS}}  
**Current phase or goal:** {{CURRENT_PHASE_OR_GOAL}}  
**Current priority:** {{CONFIRMED_PRIORITY}}  
**Next confirmed task:** {{NEXT_TASK}}  
**Blocker:** {{BLOCKER_OR_NONE}}  
**Freshness:** {{DATE_OR_FRESHNESS_STATE}}  
**Durable source:** [{{J10_OR_KB_SOURCE_LABEL}}]({{DURABLE_SOURCE_REF}}) - `{{DURABLE_SOURCE_REF}}`

### Tasks

1. **{{TASK_TITLE}}** `{{PRIORITY_URGENCY_DATE_RATING}}`
   - Status: {{TASK_STATUS}}
   - Next action: {{TASK_NEXT_ACTION}}
   - Deadline: {{DATE_OR_NONE}}
   - Subtasks:
     - **{{SUBTASK_TITLE_OR_NONE}}** `{{SUBTASK_PRIORITY_URGENCY_DATE_RATING_OR_NONE}}` - {{SUBTASK_STATUS_OR_NONE}}

### Project review flags (include when material)

- **Issue:** {{STALE_CONFLICTING_MISSING_OR_BLOCKED_ITEM}}
- **Why it matters:** {{IMPACT}}
- **Operator action:** {{RESOLUTION}}

## Ranked task view

Use manual override first, then deadline, priority, and urgency according to the live ProjectStatus contract.

| Rank | Task and project | Rating | Confirmed next action |
|---|---|---|---|
| {{RANK}} | {{TASK}} - {{PROJECT}} | `{{PRIORITY_URGENCY_DATE_RATING}}` | {{NEXT_ACTION}} |

## Unassigned items (include when confirmed work lacks a project assignment)

- {{ITEM}} - assign or resolve by: {{ACTION_OR_DATE}}

`Unassigned` is temporary and must not become a hidden permanent project category.

## Operator validation (include only when a relevant flag exists)

- {{UNCERTAIN_RATING_INVALID_RATING_INVALID_DATE_OR_UNRESOLVED_ASSIGNMENT_FLAG}}

## Archived or inactive projects (include only when needed for the current decision)

- **{{PROJECT}}:** {{CONFIRMED_INACTIVE_OR_ARCHIVED_STATUS}} - source: `{{SOURCE_REF}}`

## Overview provenance and freshness

**Confirmed durable result references:**

- `{{J10_RESULT_REF_OR_EXISTING_DURABLE_SOURCE}}`

**Overview generated or refreshed on:** {{DATE_TIME}}  
**Stale threshold or policy reference:** {{POLICY_REF_OR_NONE}}  
**Excluded candidates or unconfirmed changes:** {{REFS_OR_NONE}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Project_Status_Overview"
  artifact_ref: "{{ARTIFACT_REF}}"
  overview_truth_state: "{{OVERVIEW_STATE}}"
  confirmed_project_refs:
    - project_ref: "{{PROJECT_REF}}"
      accepted_state_ref: "{{DURABLE_SOURCE_REF}}"
      freshness: "{{FRESHNESS}}"
  highest_ranked_task_ref: "{{TASK_REF}}"
  material_review_flags:
    - "{{REVIEW_FLAG_OR_NONE}}"
  operator_validation_flags:
    - "{{OPERATOR_VALIDATION_FLAG_OR_NONE}}"
  next_consumers:
    - "{{WEEKLY_COMMAND_BRIEF_OR_PRECAP_NEXT_DAY_BRIEF_OR_AI_ROUTING_CARD}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/16-project-status-overview-design.okf.yaml"
  round6_overlay_intent_ref: "round6-patches/06-j11-project-status-contract-alignment.patch"
  overlay_application_status: "intended_guidance_not_applied_by_this_package"
  domain_contract_refs:
    - ".claude/skills/ProjectStatus/SKILL.md"
    - ".claude/skills/ProjectStatus/project-status-overview-contract_v2_fixed.md"
```

Example: [J11 Project Status Overview](../../../apex-meta/operator-output-design/step4-operator-template-system/examples/master-of-arts-example-fragments.md)
