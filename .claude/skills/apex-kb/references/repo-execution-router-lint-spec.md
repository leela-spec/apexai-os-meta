# Repo Execution Router Lint Spec

```yaml
artifact_name: repo_execution_router_lint_spec
package_path: .claude/skills/apex-kb/references/repo-execution-router-lint-spec.md
source_doctrine:
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/handoff-validation-and-risk-doctrine.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/validation-and-routing-guardrails.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/migration-safety-patterns.md
purpose: >
  Define a future deterministic lint/check that detects underspecified repo
  execution handovers before file mutation.
status: spec_only_not_executable
```

## Required route contract fields

```yaml
repo_route_contract_required_fields:
  - repository
  - branch
  - exact_target_paths
  - operation_class
  - allowed_actions
  - forbidden_actions
  - pre_write_checks
  - post_write_checks
  - stop_conditions
  - commit_strategy
```

## Lint findings

```yaml
findings:
  missing_exact_target_paths:
    severity: fail
    message: "Repo-affecting work must list exact repo-relative target paths before writes."
  missing_operation_class:
    severity: fail
    message: "Operation class is required: create, update, delete, rename, generated_output, or config_change."
  missing_allowed_or_forbidden_actions:
    severity: warning
    message: "Allowed and forbidden actions should be explicit to prevent advisory routing collapse."
  missing_post_write_checks:
    severity: warning
    message: "Post-write read-back or deterministic check is required for medium/high-risk work."
  validator_executor_collapse:
    severity: fail
    message: "High-risk work cannot rely on the same actor to validate, execute, and final-approve without explicit operator override."
```

## Non-goals

- This spec does not implement the script.
- This spec does not decide semantic correctness.
- This spec does not replace the source-authority-and-verdict-packet skill.

## Acceptance criteria for future implementation

```yaml
acceptance_criteria:
  - read_only_by_default
  - accepts_markdown_or_yaml_handover_input
  - reports_missing_required_route_fields
  - distinguishes_fail_from_warning
  - allows_historical_path_mentions_when_explicitly_marked_as_historical_source_evidence
```
