# Historical Path Authority Lint Spec

```yaml
artifact_name: historical_path_authority_lint_spec
package_path: .claude/skills/apex-kb/references/historical-path-authority-lint-spec.md
source_doctrine:
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/migration-to-claude-native-orchestration.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/migration-safety-patterns.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/audit/semantic-open-questions.md
purpose: >
  Define a future deterministic lint/check that prevents old OpenClaw runtime
  paths, legacy local paths, and historical config references from being treated
  as current repo/runtime authority.
status: spec_only_not_executable
```

## Detection targets

```yaml
detection_targets:
  historical_path_markers:
    - OpenClaw
    - old OpenClaw
    - legacy runtime
    - historical source evidence
    - C:\\
    - local Windows path
  current_authority_markers:
    - current target path
    - write to
    - update
    - replace
    - runtime authority
    - config authority
```

## Required distinction

Historical references may remain in KB pages and migration reports for source custody. They must not appear as current target paths or runtime authority unless an explicit operator decision promotes them.

```yaml
valid_historical_reference:
  required_marker: historical_source_evidence
  allowed_use:
    - source_trace
    - deprecated_appendix
    - migration_risk_note
    - contradiction_or_open_question

invalid_current_authority_reference:
  examples:
    - old_path_used_as_write_target
    - old_config_used_as_current_runtime_policy
    - old_provider_claim_used_without_current_verification
```

## Lint findings

```yaml
findings:
  unmarked_legacy_path:
    severity: warning
    message: "Legacy path appears without historical-source marker."
  historical_path_used_as_current_target:
    severity: fail
    message: "Historical path appears to be used as current implementation target."
  stale_provider_or_model_claim:
    severity: warning
    message: "Provider/model/cost/performance claim requires current verification."
  old_role_promoted_without_decision:
    severity: fail
    message: "Old role name appears promoted into current agent/skill without recorded operator decision."
```

## Acceptance criteria for future implementation

```yaml
acceptance_criteria:
  - read_only_by_default
  - supports_allowlist_for_known_historical_source_pages
  - fails_when_legacy_paths_are_used_as_current_targets
  - warns_on_unverified_current_provider_or_model_claims
  - reports_line_or_span_when_possible
```
