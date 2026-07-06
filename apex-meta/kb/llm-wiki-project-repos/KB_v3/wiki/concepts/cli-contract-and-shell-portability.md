---
title: "CLI Contract and Shell Portability"
page_type: concept
kb_slug: "llm-wiki-project-repos"
concept_slug: "cli-contract-and-shell-portability"
created_at: "2026-07-06"
status: "active"
confidence: "high"
claim_label: "source_backed_summary"
---

# CLI Contract and Shell Portability

## Definition

CLI contract friction occurs when handover command examples and actual script parsers accept different argument placement, flag names, or shell output behavior. In Apex KB this caused repeated reruns despite the lifecycle logic being sound.

## Failure Surfaces

```yaml
failures:
  global_flag_placement:
    observed: "--json and --allow-write often had to appear before the subcommand"
    desired: "safe acceptance before or after subcommand where unambiguous"
  flag_aliases:
    observed:
      - "source-intake expected --source-path, while instructions used --source"
      - "hash expected --path, while instructions used --source"
    desired: "aliases preserve existing commands and old handovers"
  powershell_json:
    observed: "PowerShell redirection wrote UTF-16, breaking JSON validation"
    desired: "UTF-8 output path or documented Set-Content -Encoding utf8 pattern"
  ordered_execution:
    observed: "commands marked exactly-in-order were run in parallel"
    desired: "sequential execution when order is specified"
```

## Patch Ideas

```yaml
patches:
  - id: CLI-001
    title: "Accept global flags before and after subcommands"
    target:
      - "apex-meta/scripts/apex_kb.py"
      - "apex-meta/scripts/apex_kb_retrieval.py"
    priority: P0
    acceptance:
      - "apex_kb.py --kb-root KB --allow-write index works"
      - "apex_kb.py --kb-root KB index --allow-write works"
      - "apex_kb.py --kb-root KB --json status works"
      - "apex_kb.py --kb-root KB status --json works"
  - id: CLI-002
    title: "Add source/path aliases"
    target: "apex-meta/scripts/apex_kb.py"
    priority: P1
    acceptance:
      - "source-intake accepts --source and --source-path"
      - "hash accepts --source and --path"
  - id: CLI-003
    title: "Add command-contract --json"
    target: "apex-meta/scripts/apex_kb.py"
    priority: P1
    acceptance: "Script can emit machine-readable supported flag placement and subcommand surface."
  - id: CLI-004
    title: "PowerShell-safe JSON output"
    target: "scripts and handover examples"
    priority: P1
    acceptance: "JSON outputs are parseable as UTF-8 on PowerShell, Bash, and cmd."
```

## Routes Here

Use this page before writing deterministic Codex prompts or patching `apex_kb.py` command surfaces.
