# Risk and Rollback Policy

## 1. Risk posture

```yaml
overall_risk: medium_high
recovery_mode: targeted_repair
do_not_revert_by_default: true
````

## 2. Highest-risk repairs

```yaml
highest_risk:
  graph_process_flow:
    risk: high
    reason:
      - "Correct extraction must include YAML/path/process/contract edges, not just Markdown links."
      - "Risk of creating noisy or misleading graph artifacts."
    mitigation:
      - "Keep deterministic and additive."
      - "Use simple Python stdlib extraction."
      - "Keep graph non-blocking."
      - "Write artifacts under manifests/phase0 only."

  pointer_only_phase0:
    risk: medium_high
    reason:
      - "Path resolution can accidentally escape KB root if not constrained."
      - "Repo-local pointers must be allowed safely without network fetch."
    mitigation:
      - "Allow only kb-root-relative or repo-local text files."
      - "Reject network URLs."
      - "Report unresolved paths instead of guessing."
      - "Never count a pointer file as scanned unless parsed."

  quality_coverage:
    risk: medium
    reason:
      - "May drift into subjective grading."
    mitigation:
      - "Use structural heuristics only."
      - "No LLM grading."
      - "No page_value_score."
      - "Report-only unless strict mode is explicitly selected."

  query_eval:
    risk: medium
    reason:
      - "Could become semantic grading."
    mitigation:
      - "Validate schema only."
      - "Do not judge answer quality."
      - "Do not run LLM evals."
```

## 3. Rollback policy

```yaml
rollback_policy:
  if_patch_pack_invalid:
    action: "reject patch pack before application"
    revert_needed: false
  if_codex_apply_fails_git_apply_check:
    action: "stop without manual edits"
    revert_needed: false
  if_static_validation_fails_after_apply:
    action: "git reset --hard HEAD before commit"
    report: "FAIL"
  if_behavior_validation_fails_after_apply:
    action: "git reset --hard HEAD before commit"
    report: "FAIL_WITH_BEHAVIOR_REGRESSION"
  if_bad_commit_pushed:
    preferred: "targeted repair follow-up"
    fallback: "git revert <bad-commit> only if runtime behavior is worse than pre-repair"
```

## 4. Revert threshold

```yaml
revert_only_if:
  - "repair corrupts source-payload manifest behavior"
  - "repair breaks scaffold/source-intake/phase0/index/lint/status baseline"
  - "repair creates writes outside kb_root"
  - "repair mutates non-Apex-KB systems"
  - "repair cannot be isolated by targeted follow-up"
```
