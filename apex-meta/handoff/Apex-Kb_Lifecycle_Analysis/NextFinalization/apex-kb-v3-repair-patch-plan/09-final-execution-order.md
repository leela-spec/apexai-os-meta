# Final Execution Order

## 1. Planning package order

```yaml
read_order:
  - "00-global-rules.md"
  - "01-read-verification-ledger.md"
  - "02-current-state-audit.md"
  - "03-target-file-map.md"
  - "04-feature-repair-index.md"
  - "05-agent-mode-patch-pack-builder-contract.md"
  - "06-validation-contract.md"
  - "07-codex-applier-contract.md"
  - "08-risk-and-rollback-policy.md"
````

## 2. Agent Mode builder execution order

```yaml
agent_mode_builder_order:
  - step: 1
    action: "repo preflight on live terminal Git worktree"
  - step: 2
    action: "read all target files from live main"
  - step: 3
    action: "repair apex-meta/scripts/apex_kb.py behaviors"
    features:
      - pointer_only_phase0
      - quality_coverage
      - query_eval
      - graph_process_flow
      - status_freshness_split
      - cli_output_json_regression
  - step: 4
    action: "repair apex-meta/scripts/apex_kb_retrieval.py only if output-json or flag placement validation fails"
  - step: 5
    action: "repair docs/contracts to match implemented behavior"
  - step: 6
    action: "add acceptance tests"
  - step: 7
    action: "validate patches individually and cumulatively"
  - step: 8
    action: "revert target files and leave patch artifacts only"
```

## 3. Codex applier execution order

```yaml
codex_applier_order:
  - step: 1
    action: "git checkout main && git pull --ff-only origin main"
  - step: 2
    action: "git apply --check repair patch pack"
  - step: 3
    action: "git apply repair patch pack"
  - step: 4
    action: "py_compile both scripts"
  - step: 5
    action: "run help checks"
  - step: 6
    action: "run targeted behavior fixture checks"
  - step: 7
    action: "verify docs match behavior"
  - step: 8
    action: "commit and push main only if all checks pass"
```

## 4. Feature order

```yaml
feature_order:
  1: pointer_only_phase0
  2: quality_coverage
  3: query_eval
  4: graph_process_flow
  5: status_freshness_split
  6: cli_output_json_regression
  7: retrieval_cli_output_json_regression
  8: docs_alignment
  9: acceptance_tests
```
