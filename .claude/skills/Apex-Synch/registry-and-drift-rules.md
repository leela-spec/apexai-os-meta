
# FILE: .claude/skills/apex-sync/references/registry-and-drift-rules.md

```markdown
# Registry and Drift Rules

```yaml
registry_and_drift_rules:
  canonical_source: ".claude/skills/apex-sync/references/registry-and-drift-rules.md"

  registry_schema:
    artifact_name: registry_report
    durable_path: "apex-meta/registry/index.md"
    source_glob: "apex-meta/epics/*/[0-9][0-9][0-9].md"
    format: markdown
    generated_by: "apex-meta/scripts/apex_sync.py registry"
    table_columns:
      - id
      - epic_slug
      - status
      - priority
      - due_date
      - depends_on
      - blocked_by
      - title
      - task_path
    required_metadata:
      registry_report:
        source:
          type: string
        task_count:
          type: integer
          min: 0
        review_flags_count:
          type: integer
          min: 0

  registry_rebuild_rules:
    default_mode: dry_run
    dry_run_behavior: "Print registry_report with generated registry_content; do not write files."
    write_behavior: "Write generated registry_content only to apex-meta/registry/index.md."
    write_requires:
      subcommand: registry
      dry_run: false
      target_path: "apex-meta/registry/index.md"
    sort_order:
      - epic_slug
      - id
    input_glob: "apex-meta/epics/*/[0-9][0-9][0-9].md"
    no_task_file_writes: true
    no_handoff_file_writes: true
    no_entity_file_writes: true
    no_skill_file_writes: true

  drift_detection_rules:
    artifact_name: drift_report
    comparison: "Regenerate registry_content from current task files and compare it to apex-meta/registry/index.md."
    drift_detected_when:
      - "apex-meta/registry/index.md is missing."
      - "apex-meta/registry/index.md content differs from regenerated registry_content."
      - "Task files produce review_flags that affect registry correctness."
    review_flags:
      - registry_out_of_date
      - drift_detected
      - malformed_frontmatter
      - missing_task_id
      - unsupported_status
      - missing_dependency_target
      - circular_dependency_risk
    write_allowed: false

  malformed_file_policy:
    malformed_frontmatter:
      action: "Report malformed_frontmatter and continue scanning remaining files."
    missing_task_id:
      action: "Report missing_task_id and exclude that file from id-based graph computation."
    unsupported_status:
      action: "Report unsupported_status and keep the task visible in validation output."
    missing_dependency_target:
      action: "Report missing_dependency_target in dependency_validation_report."
    circular_dependency_risk:
      action: "Report circular_dependency_risk and do not mark affected graph fully valid."
    invalid_due_date:
      action: "Treat urgency score as 999 and preserve the original due_date value."
      

## Registry Notes

The registry is generated state. It is never manually edited by `apex-sync`. The only allowed write behavior is an explicit `registry` command with `--dry-run false`.

`drift` is always read-only. It may include the regenerated registry content so the operator or a downstream gated process can inspect differences before any write.