# Apex KB Python CLI

Apex KB is a local, manifest-driven Python application. The CLI owns configuration, paths, state transitions, deterministic stages, semantic task packets, imports, and truthful status. AI workers only perform bounded semantic judgment.

## Install

From the repository root:

```powershell
python -m pip install -e ".\apex-meta\apex-kb-cli[test]"
```

This installs the stable public executable:

```powershell
apex-kb
```

Legacy `apex_kb.py`, `apex_kb_start.py`, and `apex_kb_control.py` remain implementation donors and compatibility surfaces. They are not the normal operator interface or lifecycle authority.

## Start

Create a canonical `run-config.yaml` using separate source and destination topology:

```yaml
source:
  repository: leela-spec/leela
  root: C:/GitDev/leela
  folders:
    - LeelaAppDevelopment

destination:
  repository: leela-spec/apexai-os-meta
  root: C:/GitDev/apexai-os-meta
  folder: apex-meta/kb/leela-app-development

exclusions: []

topics:
  - name: Skill Tree
    phrases: ["skill tree", "skilltree"]
    ambiguous_or_negative_terms: ["tree"]
    questions:
      - What is the current Skill Tree and what does it own?

run_options:
  source_handling: pointer_only
  semantic_depth: standard
  output: query_ready
  non_text: inventory_and_report
  ai_help_after_preflight: false
```

Preview and confirm:

```powershell
apex-kb start --config .\run-config.yaml
```

For scripted execution:

```powershell
apex-kb start --config .\run-config.yaml --non-interactive --yes --json-output
```

`start` prints the canonical guided template first, validates the complete configuration, performs a read-only preview, shows one readback, requests confirmation, and only then writes `run-config.yaml`, `run-manifest.json`, and `run-state.json`.

## Status

```powershell
apex-kb status --run-root C:\GitDev\apexai-os-meta\apex-meta\kb\leela-app-development
```

Status is reconstructed from durable files only.

## Continue

```powershell
apex-kb continue --run-root C:\GitDev\apexai-os-meta\apex-meta\kb\leela-app-development
```

The first continuation inventories sources. The second creates one portable semantic task packet. Place the schema-valid result at the packet's declared incoming path, then run `continue` again to validate and import it. V1 does not launch an AI provider automatically.

## V1 boundary

Implemented: exact Start asset, separate source/destination roots, frozen manifest hash, atomic state, deterministic inventory, portable Phase 1 task packet, structural import, bounded repair instructions, resume/status, structural postflight, and a thin optional Skill launcher.

Not yet implemented: exhaustive field-separated corpus-intelligence ranking, multi-topic scheduling, Phase 2 compilation, independent semantic acceptance execution, retrieval rebuild, maintenance/update runs, copy/snapshot source modes, and non-text extraction.
