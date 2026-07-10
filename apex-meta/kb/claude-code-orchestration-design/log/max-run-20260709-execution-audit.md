# Max Run 20260709 Execution Audit

```yaml
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
audit_type: execution_and_quality_audit
status: audit_completed_with_findings
created_at: 2026-07-10T00:00:00Z
repository: leela-spec/apexai-os-meta
branch: main
base_commit: 94714d11f257b6706442cc62d8c0c291b0f847d9
head_commit_audited: 428b504be80206878715c40962acaad781ed7503
```

## Executive Finding

The LLM phase produced the requested max-run parallel output set, but the run should not be treated as clean query-ready completion. It is a partial-quality semantic compile that requires cleanup and deterministic postflight before promotion.

## Evidence Checked

```yaml
github_connector_checks:
  - repository access confirmed for leela-spec/apexai-os-meta
  - compared base commit 94714d11f257b6706442cc62d8c0c291b0f847d9 to head commit 428b504be80206878715c40962acaad781ed7503
  - fetched source-payload-manifest.json
  - fetched root query-eval-pack.json
  - fetched representative Phase 1 files
  - fetched representative summary, concept, entity pages
  - searched for required Phase 2 value-contract headings
  - checked combined commit status and commit workflow runs
```

## Findings

### F1 — Too many direct commits to main

```yaml
severity: high
finding: "The run produced 37 commits ahead of the deterministic baseline instead of a small grouped commit set."
evidence: "compare_commits reported ahead_by: 37 and total_commits: 37."
risk:
  - partial-run interruption risk
  - harder rollback
  - harder review
  - commit history noise
recommended_action: "For future runs, use a tree/blob batch commit or a branch/PR audit flow instead of one commit per file."
```

### F2 — Unrelated file changed in comparison window

```yaml
severity: high
finding: "The diff from deterministic baseline to audited head includes a file outside the KB root."
file: apex-meta/operator-output-design/step2-operator-user-stories/00-package-manifest.okf.yaml
commit: b3b3ff6b8258f15b505118bdcdd6ed4434d3d58a
risk:
  - violates one-KB-root scope if attributed to this run
  - contaminates audit range
interpretation: "This may be a concurrent/unrelated commit, but it is present in the base-to-head range and must be separated before declaring the Apex KB run clean."
recommended_action: "Audit the unrelated commit separately and do not include it in Apex KB run success accounting."
```

### F3 — Source payload manifest is empty

```yaml
severity: critical
finding: "source-payload-manifest.json exists but contains empty content in connector read."
file: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
risk:
  - deterministic source custody is not proven
  - payload-root/file-count claims cannot be trusted from committed artifact alone
  - query-ready closure is invalid until repaired or explained
recommended_action: "Regenerate source-payload-manifest.json in terminal and recommit before postflight closure."
```

### F4 — No deterministic postflight actually ran after writes

```yaml
severity: critical
finding: "No GitHub status checks or workflow runs are attached to the audited head commit."
risk:
  - wiki index not rebuilt
  - retrieval index not rebuilt
  - stale check not run
  - status/lint not run
  - required sections only connector-searched, not script-validated
recommended_action: "Run index, retrieval build-index, stale, status, and lint in a live worktree."
```

### F5 — A write-probe artifact was left behind

```yaml
severity: medium
finding: "A temporary write probe file remains committed."
file: apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-write-probe.md
risk:
  - log noise
  - misleading artifact inventory
recommended_action: "Delete the probe file or mark it explicitly as non-semantic connector test debris."
```

### F6 — Phase 2 pages satisfy required headings but are thin

```yaml
severity: medium
finding: "Search confirmed the max-run Phase 2 pages include required value-contract headings, but most pages are intentionally compressed after connector blocking."
evidence:
  required_headings_found:
    - Adaptive Ranked Source Set
    - Macro / Meso / Micro
    - Key Claims
    - Routes Here
    - Uncertainty / Raw Source Reopen Triggers
risk:
  - pages may pass structural lint but provide low semantic density
  - source grounding is mostly file-level, not line-level
  - some pages provide routing doctrine rather than deep compile
recommended_action: "Treat pages as a first focused compile, not maximum-detail final doctrine. Expand high-value pages after postflight."
```

### F7 — Frontmatter is minimal and may not satisfy stricter internal template expectations

```yaml
severity: medium
finding: "Pages include user-required frontmatter fields, but many omit richer template fields such as created_at, updated_at, source_hash, source_storage_mode, related concepts/entities, and review flags."
risk:
  - deterministic lint may warn if template expectations are stricter than the user's minimal frontmatter contract
  - source custody is weaker than full Apex KB template standard
recommended_action: "Run lint; if warnings appear, patch frontmatter in batch."
```

### F8 — Final report overstates quality if read as completion

```yaml
severity: high
finding: "The final report says status completed_with_terminal_postflight_required. This is accurate only if interpreted as LLM artifact creation complete, not query-ready complete."
risk:
  - operator may treat artifacts as validated when only connector read-back occurred
recommended_action: "Use status partial_quality_compile_until_postflight in any downstream handoff."
```

### F9 — Some source-read claims are broad

```yaml
severity: medium
finding: "The report says selected raw Claude Code and operator-research files were read. Actual source access was selective and sampled, not exhaustive."
risk:
  - may imply broader corpus coverage than occurred
recommended_action: "Keep all claims scoped to selected raw files and Phase 0 routing artifacts."
```

## What Did Work

```yaml
passed_checks:
  - all requested max-run Phase 1 file names exist in the compare file list
  - all requested 8 summary pages exist in the compare file list
  - all requested 10 concept pages exist in the compare file list
  - all requested 7 entity pages exist in the compare file list
  - query-routing-candidates.md exists
  - query-eval-seed.json exists and maps the six requested operator queries
  - old root wiki pages were not modified in the audited diff
  - new Phase 2 pages include the five required value-contract headings according to GitHub search
```

## Cleanup / Repair Plan

```yaml
immediate_repairs:
  - separate_or_exclude_unrelated_operator_output_design_commit_from_apex_kb_run_accounting
  - delete_or_mark_log/max-run-20260709-write-probe.md
  - regenerate_source_payload_manifest
  - run_terminal_postflight_commands
  - capture postflight output in a new log file
  - patch final report status from completed_with_terminal_postflight_required to partial_quality_compile_until_postflight if deterministic postflight fails

postflight_commands:
  - python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design index --allow-write --json
  - python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-code-orchestration-design build-index --allow-write --json
  - python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/claude-code-orchestration-design stale --json
  - python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design status --json
  - python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/claude-code-orchestration-design lint --json
```

## Audit Verdict

```yaml
verdict: not_clean_query_ready
llm_artifacts_created: true
old_outputs_overwritten: false
scope_violation_in_compare_window: true
critical_blockers:
  - empty_source_payload_manifest
  - no_deterministic_postflight_after_writes
quality_risk:
  - thin_phase2_pages_due_to_connector_write_limits
  - many_direct_commits_to_main
recommended_operator_position: "Do not promote or rely on max-run outputs as final until deterministic postflight and cleanup are complete."
```
