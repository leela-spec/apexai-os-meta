# Constant Frame Control and Handoff Workflow

```yaml
workflow_name: constant-frame-control-and-handoff
source_doctrine:
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/handoff-validation-and-risk-doctrine.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/migration-to-claude-native-orchestration.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/old-agent-kb-migration-decision-packet.md
purpose: >
  Keep long-running LLM, Codex, GitHub, and operator handoffs bounded to the
  actual next task. Prevent promptflow drift, lifecycle recreation, advisory
  routing collapse, and accidental writes outside the approved surface.
```

## Use when

Use this workflow when creating or continuing a handover that spans chats, tools, repo writes, KB phases, or implementation decisions.

## Required frame

Every handover must include:

```yaml
frame:
  mission: ""
  current_state: ""
  next_step_only: ""
  explicit_non_goals: []
  source_hierarchy: []
  allowed_reads: []
  allowed_writes: []
  forbidden_writes: []
  operator_gates: []
  stop_conditions: []
  final_report_shape: ""
```

## Operating rules

- State where the system is now before describing what to do next.
- Do not recreate the whole lifecycle when the next task is a continuation.
- Do not turn advisory routing into execution authority.
- Do not treat a previous summary as current source truth when compiled KB pages or repo files are available.
- For repo-affecting tasks, include exact paths and allowed/forbidden writes before execution.
- Preserve unresolved operator decisions instead of silently resolving them.

## Completion criteria

```yaml
completion_criteria:
  - mission_is_single_and_current
  - current_state_is_explicit
  - next_step_is_implementation_or_decision_oriented
  - non_goals_are_visible
  - allowed_and_forbidden_writes_are_visible_when_repo_is_involved
  - stop_conditions_are_visible
  - final_report_shape_is_declared
```
