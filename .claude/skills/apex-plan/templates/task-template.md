# Task Template

Use this template as proposed content for `apex-meta/epics/<slug>/<id>.md`. This template is not a command to write the file.

```markdown
---
id: 1
title: "<task-title>"
status: open
priority: medium
due_date: null
depends_on: []
blocked_by: []
acceptance_criteria:
  - "<observable acceptance criterion>"
definition_of_done:
  - "<completion check>"
notes:
  - "<planning note or assumption>"
source:
  - "<operator note or context reference>"
---

# Task 001 — <task-title>

## Planning Rationale

<Explain why this task exists and how it supports the epic goal.>

## Dependency Rationale

<Explain proposed depends_on relationships or state that there are none.>

## Priority and Urgency Rationale

<Explain priority qualitatively and record whether due_date is known.>

## Review Flags

```yaml
review_flags:
  - operator_review_needed
```

## Handoff Requests

```yaml
handoff_requests:
  to_apex_sync:
    - validate_dependencies
  to_apex_session:
    - request_operator_confirmed_write
```
```