---
title: "Source Payload Custody Manifest"
page_type: concept
kb_slug: "llm-wiki-project-repos"
concept_slug: "source-payload-custody-manifest"
created_at: "2026-07-06"
status: "active"
confidence: "high"
claim_label: "source_backed_summary"
---

# Source Payload Custody Manifest

## Definition

The source payload custody manifest is a deterministic companion artifact to `source-manifest.json`. `source-manifest.json` records source identity and semantic source references; `source-payload-manifest.json` proves raw payload state through file, group, and root hashes.

## Target Artifact

```yaml
artifact:
  path: "apex-meta/kb/<kb-slug>/manifests/source-payload-manifest.json"
  command: "generate-source-payload-manifest"
  owner: python_deterministic_layer
  insertion_point:
    after: "source-intake"
    before:
      - "phase0"
      - "ingest_phase_1_analysis"
      - "ingest_phase_2_wiki_compile"
```

## Required Behavior

```yaml
behavior:
  hash_algorithm: sha256
  grouping:
    default: "first-level folders under raw/"
    direct_raw_files: "group root"
    forbidden:
      - "hardcoded semantic batches"
      - "filename-based semantic inference"
      - "LLM-decided deterministic source groups"
  idempotency:
    - "stable paths"
    - "sorted groups"
    - "sorted file records"
    - "no generated_at by default"
```

## Patch Ideas

```yaml
patches:
  - id: SCM-001
    title: "Add generate-source-payload-manifest"
    target: "apex-meta/scripts/apex_kb.py"
    priority: P0
    acceptance:
      - "writes manifests/source-payload-manifest.json only with --allow-write"
      - "records file_count, total_size_bytes, per-file sha256, group sha256, root sha256"
      - "stable rerun produces byte-identical output"
  - id: SCM-002
    title: "Add command contract docs"
    target: ".claude/skills/apex-kb/references/script-command-contract.md"
    priority: P1
    acceptance:
      - "documents command placement after source-intake and before Phase 0"
  - id: SCM-003
    title: "Use payload manifest in future Phase 0/Phase 1 reports"
    target: "Apex KB runbook and report templates"
    priority: P1
    acceptance:
      - "reports cite payload manifest hash/no-hash reason"
```

## Raw Source Reopen Triggers

Reopen source-payload planning files when implementing exact JSON schema, hashing serialization, CLI flags, or idempotency tests.
