# Recoverable Preflight Conditions

```yaml
recoverable_preflight_conditions:
  purpose: "Repair deterministic mechanical/environmental failures, then rerun the original bounded operation."
  rule: "Recovery never authorizes semantic guessing, broader scope, or mutation before unique live resolution."
  allowed:
    - id: text_line_ending_variance
      detect: "candidate differs only by LF|CRLF|CR"
      repair: "normalize comparison input only; preserve target newline convention on write"
    - id: markdown_whitespace_variance
      detect: "candidate differs only by trailing horizontal whitespace or whitespace-only blank lines"
      repair: "normalize lookup only; require one resolved live target; preserve unchanged target text"
    - id: stale_git_lock
      detect: "exact lock exists; no active owner process; age exceeds configured grace period"
      repair: "remove exact verified stale lock; rerun one Git operation"
    - id: transient_no_write_failure
      detect: "timeout|temporary_unavailable|retry_after|connection_reset; no partial mutation"
      repair: "bounded idempotent retry with backoff; stop at retry budget"
    - id: in_repo_path_representation_variance
      detect: "separator|case representation resolves to one in-repo path; no symlink escape"
      repair: "canonicalize lookup path; enforce resolved-path allowlist before read or write"
  never_recover_automatically:
    - zero_or_multiple_live_target_matches
    - visible_content_difference
    - path_outside_allowlist_or_symlink_escape
    - active_lock_owner_or_unknown_lock_state
    - partial_mutation_or_failed_rollback
    - unexpected_diff_scope
    - schema_or_policy_violation
  proof_required:
    - condition_classification
    - repair_action_and_result
    - single_resolved_target_after_repair
    - post_mutation_diff_scope
    - validation_outcome
```
