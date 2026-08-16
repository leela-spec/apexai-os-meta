```okf
local_execution_packet:
  id: apex-sync-w34-20260816
  reason: >
    Browser orchestrator has no local checkout of leela-spec/apexai-os-meta and no
    gh client. Apex Sync contract forbids estimating deterministic reports from
    connector data. Run the canonical Python script in a real checkout.

  repository: leela-spec/apexai-os-meta
  branch: main
  required_base_commit: ba1af5d791f0b62104b90454c6a34d01f0f30343
  target_checkout_root: repository_root
  script_path: scripts/apex_sync.py
  dry_run: true

  output_root: apex-meta/handoff/sync-reports/20260816-w34

  commands:
    - name: next_and_dependency_validation
      command: >
        python scripts/apex_sync.py next --root . --json --dry-run true
        > apex-meta/handoff/sync-reports/20260816-w34/next.json
      expected_reports:
        - next_action_report
        - dependency_validation_report

    - name: blockers_and_dependency_validation
      command: >
        python scripts/apex_sync.py blockers --root . --json --dry-run true
        > apex-meta/handoff/sync-reports/20260816-w34/blockers.json
      expected_reports:
        - blocker_report
        - dependency_validation_report

    - name: registry_preview
      command: >
        python scripts/apex_sync.py registry --root . --json --dry-run true
        > apex-meta/handoff/sync-reports/20260816-w34/registry-preview.json
      expected_reports:
        - registry_report

    - name: stall_report
      command: >
        python scripts/apex_sync.py stall --root . --json --dry-run true
        --stale-days 14 --today 2026-08-16
        > apex-meta/handoff/sync-reports/20260816-w34/stall.json
      expected_reports:
        - stall_report

    - name: drift_report
      command: >
        python scripts/apex_sync.py drift --root . --json --dry-run true
        > apex-meta/handoff/sync-reports/20260816-w34/drift.json
      expected_reports:
        - drift_report
        - registry_report

    - name: score_and_focus_candidates
      command: >
        python scripts/apex_sync.py score --root . --json --dry-run true
        --today 2026-08-16
        > apex-meta/handoff/sync-reports/20260816-w34/score.json
      expected_reports:
        - score_report
        - focus_candidate_report

  required_executor_steps:
    - checkout main at or after required_base_commit
    - verify required_base_commit is an ancestor of HEAD
    - create output_root
    - run all six commands exactly
    - do not run registry with dry-run false
    - do not edit task status, dependencies, handoff narrative, or skill files
    - verify every command exits 0
    - verify 62 task files are discovered at the required repository state
    - verify no duplicate_task_id flag is produced solely by matching ids in different epics
    - verify every JSON contains report_name generated_at dry_run root script_exit_code review_flags
    - commit only generated Sync JSON reports
    - push origin main

  commit_message: "chore: add W34 Apex Sync dry-run reports"

  required_return_evidence:
    - final_commit_sha
    - git_status_clean
    - command_exit_codes
    - generated_report_paths
    - any script_failed evidence verbatim

  continuation_after_reports:
    - browser orchestrator reads committed report JSON
    - structural corrections route through Plan/Session if needed
    - if graph is valid enough, generate ProjectStatus
    - collect W34-specific inputs
    - run PreCap Week G1
```

## Codex execution prompt

```text
Repo: leela-spec/apexai-os-meta
Branch: main
Work directly on main.
Pull latest main.
Verify commit ba1af5d791f0b62104b90454c6a34d01f0f30343 is an ancestor of HEAD.
Create apex-meta/handoff/sync-reports/20260816-w34/.
Run:
python scripts/apex_sync.py next --root . --json --dry-run true > apex-meta/handoff/sync-reports/20260816-w34/next.json
python scripts/apex_sync.py blockers --root . --json --dry-run true > apex-meta/handoff/sync-reports/20260816-w34/blockers.json
python scripts/apex_sync.py registry --root . --json --dry-run true > apex-meta/handoff/sync-reports/20260816-w34/registry-preview.json
python scripts/apex_sync.py stall --root . --json --dry-run true --stale-days 14 --today 2026-08-16 > apex-meta/handoff/sync-reports/20260816-w34/stall.json
python scripts/apex_sync.py drift --root . --json --dry-run true > apex-meta/handoff/sync-reports/20260816-w34/drift.json
python scripts/apex_sync.py score --root . --json --dry-run true --today 2026-08-16 > apex-meta/handoff/sync-reports/20260816-w34/score.json
Require exit code 0 for every command.
Do not run registry with --dry-run false.
Do not modify task files, statuses, dependencies, handoff narrative, or skills.
Verify the six JSON files exist and contain the canonical report metadata.
Commit only the generated report files with message: chore: add W34 Apex Sync dry-run reports
Push origin main.
Report: commit SHA; each command exit code; generated report paths; git status.
```
