
# FILE: .claude/skills/apex-sync/references/script-command-contract.md

```markdown
# Script Command Contract

```yaml
script_command_contract:
  canonical_source: ".claude/skills/apex-sync/references/script-command-contract.md"
  python_cli_contract: "apex-meta/scripts/apex_sync.py"

  command_interface:
    executable: "python apex-meta/scripts/apex_sync.py"
    root_default: "."
    global_flags:
      - name: "--root"
        type: string
        default: "."
        meaning: "Repository root containing apex-meta/."
      - name: "--json"
        type: boolean
        default: false
        meaning: "Emit JSON stdout instead of human-readable stdout."
      - name: "--dry-run"
        type: string
        allowed:
          - "true"
          - "false"
        default: "true"
        meaning: "Keep read-only default; use false only for explicit registry writes."

  subcommand_contracts:
    next:
      purpose: "Compute actionable next task candidates."
      output:
        - next_action_report
        - dependency_validation_report
      write_allowed: false
      example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run true next"

    blockers:
      purpose: "List blocked tasks and missing dependency targets."
      output:
        - blocker_report
        - dependency_validation_report
      write_allowed: false
      example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run true blockers"

    registry:
      purpose: "Rebuild or print compact registry index."
      output:
        - registry_report
      write_allowed: true
      write_conditions:
        subcommand: registry
        dry_run: false
        target_path: "apex-meta/registry/index.md"
      dry_run_example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run true registry"
      write_example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run false registry"

    stall:
      purpose: "Detect stale task candidates."
      output:
        - stall_report
      write_allowed: false
      example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run true stall"

    drift:
      purpose: "Detect registry/source mismatch."
      output:
        - drift_report
        - registry_report
      write_allowed: false
      example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run true drift"

    score:
      purpose: "Compute priority, urgency, unlock, and focus scores."
      output:
        - score_report
        - focus_candidate_report
      write_allowed: false
      example: "python apex-meta/scripts/apex_sync.py --root . --json --dry-run true score"

  exit_code_policy:
    success:
      script_exit_code: 0
      meaning: "Command completed and malformed task inputs, if any, were reported through review_flags."
    script_failed:
      script_exit_code: 1
      meaning: "Unexpected script failure; report script_failed and do not infer missing data."
    invalid_cli:
      script_exit_code: 2
      meaning: "Argument parser error before report generation."

  json_output_policy:
    enabled_by: "--json"
    stdout_root:
      required:
        - script_exit_code
      report_keys_allowed:
        - next_action_report
        - blocker_report
        - registry_report
        - stall_report
        - drift_report
        - score_report
        - focus_candidate_report
        - dependency_validation_report
    review_flags_key: review_flags
    dry_run_key: dry_run
    rule: >
      JSON output must preserve canonical report names and must not rename
      id, title, status, priority, due_date, depends_on, blocked_by,
      epic_slug, task_path, frontmatter, body, source, or review_flags.

  safety_policy:
    standard_library_only: true
    shell_out_allowed: false
    network_allowed: false
    external_dependencies_allowed: false
    task_file_mutation_allowed: false
    handoff_file_mutation_allowed: false
    entity_file_mutation_allowed: false
    skill_file_mutation_allowed: false
    registry_is_only_allowed_write_path: true
    
## Usage Notes

Global flags are supplied before the subcommand. `--dry-run false` is valid only when paired with `registry`; every other subcommand remains read-only regardless of output format.

The command contract owns invocation semantics only. Registry schemas are owned by `registry-and-drift-rules.md`. Scoring formulas are owned by `scoring-and-focus-rules.md`. Executable implementation behavior is owned by `apex-meta/scripts/apex_sync.py`.