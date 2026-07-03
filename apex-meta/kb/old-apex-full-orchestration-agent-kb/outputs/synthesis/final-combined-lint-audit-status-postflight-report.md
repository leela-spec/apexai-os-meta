# Final Combined Lint/Audit/Status Postflight Report

```yaml
verdict: PASS_WITH_WARNINGS
branch: main
previous_validated_commit: d2b41809908f3e248e1c2c253bb05d9d433dcffb
commands_validated:
  - lint-repo-execution-router
  - lint-historical-path-authority
script_checked: apex-meta/scripts/apex_kb.py
target_kb: apex-meta/kb/old-apex-full-orchestration-agent-kb

validation:
  command_presence:
    lint_repo_execution_router: PASS
    lint_historical_path_authority: PASS
  py_compile: PASS
  help_output:
    script_help: PASS
    lint_repo_execution_router_help: PASS
    lint_historical_path_authority_help: PASS
  router_lint:
    valid_fixture: PASS
    invalid_fixture_detected: PASS
    json_output: PASS
  historical_path_authority_lint:
    valid_fixture: PASS
    invalid_fixture_detected: PASS
    json_output: PASS
  target_kb_checks:
    status_json: PASS
    lint_json: PASS
    audit_json: PASS
    status_exit: 0
    lint_exit: 0
    audit_exit: 0
  real_surface_checks:
    router_synthesis_surface_exit: 2
    historical_wiki_surface_exit: 2
    router_synthesis_surface_findings: 39
    historical_wiki_surface_findings: 18

warnings:
  - NONE

failures:
  - NONE

notes:
  - "Invalid fixture PASS means the command detected invalid input and exited non-zero as expected."
  - "Real-surface findings are recorded only; this task does not auto-fix KB content."
  - "Parser now accepts subcommand-level --json for health, status, lint, and audit so the documented postflight command shape emits parseable JSON."
```
