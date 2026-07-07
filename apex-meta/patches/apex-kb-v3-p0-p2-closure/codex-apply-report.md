```yaml
repo: leela-spec/apexai-os-meta
branch: main
patches_applied:
  - 001-apex-kb-cli-flags-output-json.patch
  - 002-apex-kb-retrieval-cli-flags-output-json.patch
  - 003-apex-kb-pointer-only-phase0.patch
  - 004-apex-kb-status-freshness-split.patch
  - 005-apex-kb-quality-coverage.patch
  - 006-apex-kb-query-eval.patch
  - 007-apex-kb-graph-process-flow.patch
  - 008-script-command-contract.patch
validation:
  git_apply_check: FAIL
  py_compile_apex_kb: PASS
  py_compile_retrieval: PASS
  changed_file_scope: PASS
  marker_checks: PASS
workarounds:
  used: true
  details:
    - "All eight patch fragments used abbreviated hunk headers that git apply could not parse; equivalent bounded manual changes were applied and documented in PATCH_WORKAROUND_REPORT.md."
commit:
  sha: "PENDING"
```
