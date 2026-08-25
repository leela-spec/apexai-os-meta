# OKF Program: Two-Week Weekly-Orchestration Closed-Loop Simulation
```yaml
okf:
  id: hermes-weekly-orchestration-professional-simulation-v1
  version: 1.0
  status: executing
  document_role: hermes_simulation_program_launcher

program:
  name: Two-Week Weekly-Orchestration Closed-Loop Simulation
  target_runtime: Hermes
  control_repo: leela-spec/apexai-os-meta
  branch: main
  mode: shadow_execution

safety_invariants:
  production_state_mutation: forbidden
  source_repo_task_mutation: forbidden
  source_board_mutation: forbidden
  real_calendar_write: forbidden
  production_skill_rewrite: forbidden
```

## Program Charter & Authority
This program materializes the complete 2-week execution lifecycle of the Apex AIOS Weekly Orchestrator. All state, boards, prompt files, routing records, evidence dumps, and reviews are strictly generated within this isolated simulation directory.
