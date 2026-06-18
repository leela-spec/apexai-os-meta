---
# EXAMPLE PROJECT RECORD — Apex OS Meta
# This is a real record. Uncertain fields carry operator_review_needed: true.

id: apex-os-meta
name: Apex OS Meta
domain_type: dev
project_status: active
created_or_updated_at: 2026-06-18
last_updated: 2026-06-18
priority: 90
urgency: 85
date: NA
next_action: Complete project-kb-manager skill package and commit all 10 files
blocked_by:
confidence: high
operator_review_needed: true
operator_validated_at:
current_milestone_id: M1
active_milestone_ids: [M1]
project_status_summary_for_precap: >-
  Apex OS Meta is active — building project-kb-manager skill (M1);
  FlowRecap integration and PrecapNextDay KB upgrade follow in sequence.
repo_url: https://github.com/leela-spec/apexai-os-meta
source_repo:
parent_project_id:
---

## Domain Overlay

```yaml
dev_fields:
  open_prs: 0
  deployment_status: NA
  tech_stack: Claude Code, Markdown, YAML, GitHub
  default_branch: main
  test_status: unknown
  acceptance_criteria: All 10 skill files committed; SKILL.md scores 8+ on pre-acceptance checklist
  artifact_refs:
    - .claude/skills/project-kb-manager/SKILL.md
    - .claude/kb/registry.md
  notes: FlowRecap skill is currently marked missing in repo — KB update mode requires interim operator-note fallback until FlowRecap is built
```

## Milestones

```yaml
milestones:
  - id: M1
    name: project-kb-manager skill package
    status: active
    status_reason: Files 1-5 committed; files 6-10 in progress
    depends_on: []
    unlocks: [M2]
    blocked_by:
    deadline: NA
    priority_weight: 90
    definition_of_done: All 10 files committed and passing global validation checklist
    next_action: Commit files 6-10 via push_files
    operator_review_needed: true

  - id: M2
    name: FlowRecap integration
    status: pending
    status_reason: Depends on M1 completion and FlowRecap skill existence
    depends_on: [M1]
    unlocks: [M3]
    blocked_by: FlowRecap skill not yet built
    deadline: NA
    priority_weight: 70
    definition_of_done: update project-kb trigger successfully consumes a real FlowRecap packet
    next_action: Build FlowRecap skill after M1 is done
    operator_review_needed: true

  - id: M3
    name: PrecapNextDay KB upgrade
    status: pending
    status_reason: Depends on M2 — KB must be populated before PrecapNextDay can read it
    depends_on: [M2]
    unlocks: []
    blocked_by:
    deadline: NA
    priority_weight: 60
    definition_of_done: PrecapNextDay reads .claude/kb/registry.md as primary project state source
    next_action: Add kb-integration-contract.md to PrecapNextDay references
    operator_review_needed: true
```

## Progress Log

```yaml
progress_log:
  - session_id: session-2026-06-18-design
    date: 2026-06-18
    what_happened: >-
      Full project-kb-manager design completed via Q&A session.
      GPT validation run and critically reviewed.
      Prompt flow corrected and executed.
      Files 1-5 committed to repo.
    next_step: Commit files 6-10 and run final audit
    source: operator_note
```
