---
# PROJECT RECORD TEMPLATE
# Copy this file to .claude/kb/projects/<project-id>.md and fill all fields.
# Remove placeholder comments after filling.

id: <kebab-case-project-id>
name: <Project Full Name>
domain_type: <dev|content|business|comms|investment>
project_status: <intake|scoping|active|blocked|review|done|archived>
created_or_updated_at: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
priority: <1-100>
urgency: <1-100>
date: <DD-MM-YYYY|NA>
next_action: <one sentence — what happens next>
blocked_by: <what is blocking, or remove this line if not blocked>
confidence: <high|medium|low|unknown>
operator_review_needed: true
operator_validated_at: <YYYY-MM-DD or remove if not yet validated>
current_milestone_id: <M1 or remove if no milestones yet>
active_milestone_ids: []
project_status_summary_for_precap: <one sentence for PrecapNextDay to read>
repo_url: <https://github.com/org/repo or remove if not applicable>
source_repo: <origin repo if this is a child project, or remove>
parent_project_id: <parent project id or remove>
---

## Domain Overlay

<!-- Add the block matching your domain_type. Remove the others. -->

<!-- dev_fields:
  open_prs: <count or NA>
  deployment_status: <deployed|staging|local|NA>
  tech_stack: <>
  default_branch: main
  test_status: <passing|failing|unknown>
  acceptance_criteria: <>
  artifact_refs: []
  notes: <free text for anything not in schema> -->

<!-- content_fields / business_fields / comms_fields / investment_fields -->
<!-- See references/domain-overlay-rules.md for field list per domain -->

## Milestones

```yaml
milestones:
  - id: M1
    name: <milestone name>
    status: pending
    status_reason: <why this status>
    depends_on: []
    unlocks: [M2]
    blocked_by:
    deadline: NA
    priority_weight: 50
    definition_of_done: <what must be true for operator to confirm done>
    next_action: <first concrete step>
    operator_review_needed: true
```

## Progress Log

<!-- Append entries below. Never delete existing entries. -->

```yaml
progress_log: []
```
