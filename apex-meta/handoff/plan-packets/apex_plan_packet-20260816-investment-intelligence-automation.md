---
title: "Apex Plan Packet — Investment Intelligence and Decision Automation"
document_role: apex_plan_operator_review_packet
created: 2026-08-16
status: operator_review_needed
planning_status: evidence_checked_candidate
package: apex-plan
candidate_epic_slug: investment-intelligence-automation
target_week: 2026-W34
canonical_mutation_performed: false
---

# Investment Intelligence and Decision Automation

## project_capture_record

```yaml
project_capture_record:
  goal: >
    Establish three equally important investment-support loops: scheduled
    discovery of relevant videos/information using existing OpenClaw/Hermes
    Cron capability, useful low-noise alerts, and structured feedback on
    operator portfolio/trading decisions.

  equal_priority_workstreams:
    - video_discovery
    - alerts
    - decision_feedback

  source:
    - operator portfolio input 2026-08-16
    - investment-intelligence-automation-checkpoint-01-source-reconnaissance-20260816.md
    - MasterOfArts OpenClaw/Hermes Cron documentation

  constraints:
    - do not rank the three workstreams against each other
    - use existing Cron capability rather than create a new scheduler architecture
    - Cron prompts must be self-contained because scheduled runs have fresh context
    - alerting should support silence/no-delivery when nothing meaningful happened
    - do not invent investment topics alert thresholds delivery channels or portfolio positions
    - decision feedback does not authorize autonomous trade execution
```

## epic_record

```yaml
epic_record:
  slug: investment-intelligence-automation
  title: Investment Intelligence and Decision Automation
  status: open
  priority: medium
  due_date: null
```

## proposed_task_records

### Workstream A — Video discovery

```yaml
- id: 1
  title: Define investment video-discovery contract
  status: open
  priority: medium
  due_date: null
  depends_on: []
  blocked_by:
    - operator_specific_topics_and_sources_required_during_execution
  acceptance_criteria:
    - search topics sources/channels or query families are explicit
    - time window and schedule are explicit
    - relevance criteria are explicit
    - duplicate/already-seen handling is explicit
    - output format captures source title link/date and why it matters
    - no investment recommendation is fabricated merely because content is discovered
  definition_of_done:
    - one self-contained scheduled-search contract exists

- id: 2
  title: Configure and test OpenClaw Cron video-search job
  status: open
  priority: medium
  due_date: null
  depends_on: [1]
  blocked_by: []
  acceptance_criteria:
    - existing Cron scheduler is used
    - job prompt is self-contained
    - one manual immediate test run succeeds before relying on schedule
    - duplicate/no-result behavior is bounded
    - results land in the selected output/delivery surface
    - job can be listed paused edited and removed through existing Cron controls
  definition_of_done:
    - one operational tested scheduled video-discovery job exists
```

### Workstream B — Alerts

```yaml
- id: 3
  title: Define investment alert contract and signal thresholds
  status: open
  priority: medium
  due_date: null
  depends_on: []
  blocked_by:
    - operator_specific_alert_conditions_required_during_execution
  acceptance_criteria:
    - alert categories and source inputs are explicit
    - meaningful-change/signal conditions are explicit
    - deduplication/cooldown behavior is explicit
    - no-signal behavior suppresses notification
    - delivery target is explicit
    - alert payload distinguishes observed fact from interpretation
  definition_of_done:
    - one implementation-ready low-noise alert contract exists

- id: 4
  title: Implement and test investment alert loop
  status: open
  priority: medium
  due_date: null
  depends_on: [3]
  blocked_by: []
  acceptance_criteria:
    - selected data/source collection is deterministic where practical
    - reasoning layer receives bounded source evidence
    - no-signal cases produce no notification
    - signal cases produce one concise evidence-backed alert
    - repeated identical signals do not create uncontrolled spam
    - manual test covers both silent and alerting paths
  definition_of_done:
    - operational alert loop behaves correctly for signal and no-signal cases
```

### Workstream C — Portfolio/trading decision feedback

```yaml
- id: 5
  title: Define portfolio and trading decision-feedback record
  status: open
  priority: medium
  due_date: null
  depends_on: []
  blocked_by:
    - operator_current_decision_process_required_during_execution
  acceptance_criteria:
    - record separates decision time evidence thesis expected outcome risk and later outcome
    - position/trade identifiers can be referenced without requiring autonomous brokerage access
    - feedback horizons/review triggers are explicit
    - later evaluation distinguishes decision quality from outcome luck where possible
    - source/evidence links can be preserved
  definition_of_done:
    - one reusable decision-feedback schema/process exists

- id: 6
  title: Automate decision-feedback collection and review
  status: open
  priority: medium
  due_date: null
  depends_on: [5]
  blocked_by: []
  acceptance_criteria:
    - new operator decisions can enter the feedback record with low friction
    - scheduled or event-based review can retrieve the original thesis/evidence
    - current outcome data can be attached from approved sources
    - feedback compares expectation evidence and outcome without rewriting the original decision
    - automation produces review/learning output but does not place trades
  definition_of_done:
    - at least one real decision can travel through capture to later automated feedback
```

### Cross-workstream validation

```yaml
- id: 7
  title: Validate integrated investment intelligence loop
  status: open
  priority: medium
  due_date: null
  depends_on: [2, 4, 6]
  blocked_by: []
  acceptance_criteria:
    - video discovery runs on schedule and produces bounded useful outputs
    - alert loop is low-noise and evidence-backed
    - decision-feedback loop preserves original operator decision context
    - outputs can cross-reference each other without creating hidden autonomous trading authority
    - failures are explicit and retriable
    - operator can pause/disable each automation independently
  definition_of_done:
    - all three equally important workstreams have one working validated version
```

## dependency_plan

```yaml
dependency_plan:
  parallel_chains:
    - 1 -> 2
    - 3 -> 4
    - 5 -> 6
  integration:
    - 2 + 4 + 6 -> 7
  priority_relationship:
    rule: equal_operator_priority_across_three_workstreams
    no_rank_inference: true
  apex_sync_handoff_requests:
    - validate_dependencies
    - compute_next_action
    - compute_focus_candidates_without_overriding_equal_operator_priority
```

## priority_urgency_focus_rationale

```yaml
priority_urgency_focus_rationale:
  epic_priority: medium
  due_date: null
  workstream_priority:
    video_discovery: equal
    alerts: equal
    decision_feedback: equal
  provisional_focus_recommendation: >
    Do not choose one of the three workstreams as operator-preferred. After
    canonical creation, Apex Sync may identify actionable tasks based on
    dependency/readiness while preserving the equal priority instruction.
```

## review_flags

```yaml
review_flags:
  - operator_review_needed
  - missing_operator_specific_search_contract
  - missing_operator_specific_alert_contract
  - missing_current_decision_journal_contract
  - no_autonomous_trade_execution_authority
  - three_workstreams_equal_priority
```

## handoff_requests

```yaml
handoff_requests:
  to_apex_session_after_operator_approval:
    - create canonical epic/task records
```

## operator_gate

```yaml
operator_gate:
  status: operator_review_needed
  recommended_decision: approved_for_handoff
  mutation_allowed_by_this_packet: false
```
