# Codex Apply Prompt

Work in `leela-spec/apexai-os-meta` on `main`.

1. Run `git checkout main` and `git pull --ff-only origin main`.
2. Verify the recorded baseline in `patch-builder/000-patch-manifest.md`. Stop if the target-file contents do not match that baseline.
3. Run every individual `git apply --check` command in `patch-builder/validation-plan.md`.
4. Run the cumulative `git apply --check` in manifest order.
5. Apply the seven patches in manifest order.
6. Run the full validation plan exactly as written. Resolve no failure with manual equivalent edits or workarounds.
7. Stop on any patch-check, compilation, required fixture, scope, or validation failure.
8. Confirm exactly the seven target files changed.
9. Commit directly to `main` with message: `Add Apex KB capability routing and postflight`.
10. Push `origin main`.

Final report:

```yaml
starting_sha: ""
baseline_verified: false
individual_patch_checks: []
cumulative_patch_check: ""
changed_files: []
validation_results: []
commit_sha: ""
push_result: ""
workaround_used: false
```
