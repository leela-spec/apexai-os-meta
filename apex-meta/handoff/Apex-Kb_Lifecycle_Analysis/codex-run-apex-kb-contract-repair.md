# Codex Handoff — Run Apex KB Contract Repair Script

## Mission

Run the repo-local Apex KB repair script and report the result. This is a local file-maintenance task inside this repository only.

## Target repo

```text
C:\GitDev\apexai-os-meta
```

If the local checkout is at another path, use that checkout path instead.

## Script to run

```text
scripts/fix_apex_kb_package_contracts.py
```

## Allowed file scope

The script is expected to modify only these files:

```text
.claude/skills/apex-kb/SKILL.md
.claude/skills/apex-kb/templates/wiki-page-templates.md
.claude/skills/apex-kb/references/script-command-contract.md
.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
apex-meta/scripts/apex_kb.py
```

It may also create backups under:

```text
.repair-backups/apex-kb-contract-repair/<timestamp>/
```

Do not modify files outside this scope unless the script reports a hard local blocker. If that happens, stop and report the blocker.

## Execution steps

Run from the repository root:

```powershell
cd C:\GitDev\apexai-os-meta
python scripts\fix_apex_kb_package_contracts.py --check
```

Review the printed diff and confirm it is limited to the allowed file scope.

Then run:

```powershell
python scripts\fix_apex_kb_package_contracts.py --apply
python scripts\fix_apex_kb_package_contracts.py --validate
```

Then inspect the resulting local diff:

```powershell
git status --short
git diff -- .claude/skills/apex-kb/SKILL.md .claude/skills/apex-kb/templates/wiki-page-templates.md .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md apex-meta/scripts/apex_kb.py
```

## Expected repairs

```yaml
expected_repairs:
  skill_md:
    - uncollapse supporting_files YAML
    - uncollapse failure_modes YAML
    - uncollapse completion_gate YAML
    - add source_storage_modes
    - add normal_mode_vs_explicit_test_mode_phase_gate_policy
    - add separate confidence and claim_label fields

  wiki_page_templates:
    - uncollapse markdown frontmatter templates
    - add claim_label_allowed
    - add source_storage_mode to source_refs
    - add applied_card block for concept pages

  script_command_contract:
    - align invocation pattern with actual parser
    - record --source-slug as required for preflight
    - record --title and --topic-title behavior for scaffold
    - remove unsupported --algorithm from hash contract
    - add JSON output compatibility notes

  operation_rules:
    - add source_storage_policy
    - add epistemic_fields
    - add phase_gate_policy

  apex_kb_py:
    - replace permissive shell-out wording with strict no-shell-out wording
```

## Validation expectations

`--validate` should run these smoke checks internally:

```powershell
python apex-meta\scripts\apex_kb.py --help
python apex-meta\scripts\apex_kb.py --json scaffold --kb-root apex-meta\kb\apex-kb-contract-smoke --title "Apex KB Contract Smoke"
```

The scaffold command is a dry run unless `--allow-write` is explicitly passed.

## Report format

Return this compact report:

```yaml
codex_result:
  check_exit_code: <int>
  apply_exit_code: <int>
  validate_exit_code: <int>
  changed_files:
    - <path>
  backup_path: <path-or-NA>
  validation_summary:
    apex_kb_help: passed | failed
    scaffold_dry_run: passed | failed
  remaining_warnings:
    - <warning-or-NA>
  recommendation: ready_for_second_apex_kb_test | needs_manual_review
```

Do not create commits or push changes unless the operator separately requests that.
