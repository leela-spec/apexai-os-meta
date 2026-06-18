# Project KB Schema

```yaml id="ef1ueq"
schema_metadata:
  schema_owner: references/project-schema.md
  schema_version: "1.0"
  purpose: sole_field_type_and_allowed_value_authority

schemas:
  base_record:
    required:
      id: { type: string, format: kebab-case }
      name: { type: string }
      domain_type: { type: enum, allowed: [dev, content, business, comms, investment] }
      project_status: { type: enum, allowed: [intake, scoping, active, blocked, review, done, archived] }
      created_or_updated_at: { type: string, format: YYYY-MM-DD }
      last_updated: { type: string, format: YYYY-MM-DD }
      priority: { type: integer, min: 1, max: 100 }
      urgency: { type: integer, min: 1, max: 100 }
      date: { type: string, allowed: [DD-MM-YYYY, NA] }
      next_action: { type: string }
      confidence: { type: enum, allowed: [high, medium, low, unknown] }
      operator_review_needed: { type: boolean }
      project_status_summary_for_precap: { type: string, constraint: one_sentence_feeds_current_project_status_overview }
    optional:
      blocked_by: { type: string }
      operator_validated_at: { type: string, format: YYYY-MM-DD }
      current_milestone_id: { type: string }
      active_milestone_ids: { type: list, items: { type: string } }
      repo_url: { type: string }
      source_repo: { type: string }
      parent_project_id: { type: string }

  milestone:
    required:
      id: { type: string, format: M[integer] }
      name: { type: string }
      status: { type: enum, allowed: [pending, active, done, blocked, skipped] }
      priority_weight: { type: integer, min: 1, max: 100 }
      definition_of_done: { type: string }
      next_action: { type: string }
      operator_review_needed: { type: boolean }
    optional:
      status_reason: { type: string }
      depends_on: { type: list, items: { type: string, format: milestone_id } }
      unlocks: { type: list, items: { type: string, format: milestone_id } }
      blocked_by: { type: string }
      deadline: { type: string, allowed: [DD-MM-YYYY, NA] }

  progress_log_entry:
    append_only: true
    required:
      session_id: { type: string }
      what_happened: { type: string }
      next_step: { type: string }
      source: { type: enum, allowed: [flow_recap, operator_note, manual] }
    optional:
      date: { type: string, format: YYYY-MM-DD }

  registry_entry:
    compact: true
    required:
      id: { type: string }
      name: { type: string }
      domain_type: { type: enum, allowed: [dev, content, business, comms, investment] }
      project_status: { type: enum, allowed: [intake, scoping, active, blocked, review, done, archived] }
      priority: { type: integer, min: 1, max: 100 }
      urgency: { type: integer, min: 1, max: 100 }
      date: { type: string, allowed: [DD-MM-YYYY, NA] }
      last_updated: { type: string, format: YYYY-MM-DD }
      project_status_summary_for_precap: { type: string }
    optional:
      current_milestone_id: { type: string }

  consumed_recap_entry:
    append_only: true
    required:
      recap_id: { type: string }
      consumed_at: { type: string, format: YYYY-MM-DD }
      project_id: { type: string }
      session_id: { type: string }

domain_overlay_field_blocks:
  dev_fields:
    open_prs: { type: string }
    deployment_status: { type: string }
    tech_stack: { type: list, items: { type: string } }
    default_branch: { type: string }
    test_status: { type: string }
    acceptance_criteria: { type: string }
    artifact_refs: { type: list, items: { type: string } }
    notes: { type: string }

  content_fields:
    content_type: { type: string }
    brief_status: { type: string }
    draft_url: { type: string }
    publish_date: { type: string, format: YYYY-MM-DD, optional: true }
    channel: { type: string }
    editorial_stage: { type: string }
    review_owner: { type: string }
    notes: { type: string }

  business_fields:
    offer_or_product: { type: string }
    business_stage: { type: string }
    client: { type: string }
    decision_needed: { type: string }
    success_metric: { type: string }
    stakeholder: { type: string }
    risk_level: { type: string }
    notes: { type: string }

  comms_fields:
    platform: { type: string }
    thread_url: { type: string }
    action_required: { type: string }
    response_status: { type: string }
    waiting_on: { type: string }
    next_follow_up: { type: string, format: YYYY-MM-DD, optional: true }
    relationship_priority: { type: string }
    notes: { type: string }

  investment_fields:
    asset_type: { type: string }
    thesis: { type: string }
    thesis_status: { type: string }
    position_size: { type: string }
    entry_date: { type: string, format: YYYY-MM-DD, optional: true }
    exit_criteria: { type: string }
    risk_level: { type: string }
    notes: { type: string }

non_goals:
  - Do not define application rules, progression logic, or write procedures.
  - Do not reference other package files.
```