# Apex KB Mechanistic Workflow Pack

## Purpose

This pack replaces an interpretation-heavy Apex KB entry flow with a **manual, CLI-first, manifest-driven workflow**.

The runtime rule is:

> Scripts own stages, paths, state, validation, and next actions. AI receives only bounded semantic assignments generated from locked files.

## Locked decisions

1. **One start surface:** `/apex-kb start` is a thin convenience adapter. The canonical authority is the CLI control plane. There is no separate “AI start” lifecycle.
2. **One operator draft:** `manifests/run-config.okf.json` contains the operator's run choices.
3. **Read-only preflight before lock:** schema, path, overlap, capability, and scope checks run before expensive work. Success is compact; details appear only for warnings or failures.
4. **One locked manifest:** the confirmed configuration is compiled into `manifests/run-manifest.json` with a SHA-256 configuration hash.
5. **One state owner:** `manifests/run-state.json` owns progress. Chat memory never owns lifecycle state.
6. **One primary topic per standard build run:** additional topics and later source integration are separate future workflows.
7. **Deterministic Phase 0:** inventory, structure extraction, field-separated ranking, duplicates, dates/lifecycle hints, work packs, and a statistics report.
8. **No AI-written prompts:** scripts combine stable prompt templates with generated run-specific instruction files.
9. **Small semantic contexts:** one topic, one bounded source batch, one exact output boundary.
10. **Validation feedback is data:** failed checks are written back into the next instruction file; the AI repairs only named failures.

## Why there is no separate “layer architecture” document set

The layers are encoded in executable boundaries: file paths, schemas, script ownership, stage results, and allowed writes. Creating six prose architecture files would duplicate these rules and create another drift surface. This pack keeps exactly one compact workflow contract for human orientation and test generation.

## Package map

| File | Runtime role |
|---|---|
| `.claude/skills/apex-kb/SKILL.md` | Manual-only launcher. Runs the control command and relays output verbatim. |
| `templates/welcome-intake.okf.md` | Fixed welcome message, field help, option help, and exact input shape. |
| `templates/run-config-template.okf.json` | Human-editable operator input template. |
| `references/run-config.schema.json` | Machine validation for the operator input. |
| `references/preflight-report.schema.json` | Read-only preflight result contract. |
| `references/run-manifest.schema.json` | Locked canonical configuration contract. |
| `references/stage-result.schema.json` | Standard result envelope for every script/stage. |
| `references/mechanistic-workflow-contract.okf.yaml` | Complete input -> script -> output -> consumer map. |
| `references/phase0-ranking-and-stats-contract.okf.md` | Exact deterministic ranking and statistics contract. |
| `references/phase0-stats.schema.json` | Machine contract for Phase 0 statistics. |
| `templates/phase0-stats-report.okf.md` | Human-readable Phase 0 report projection. |
| `templates/topic-registry-template.okf.json` | Locked topic, vocabulary, and target-question structure. |
| `references/semantic-task-instructions.schema.json` | Shared schema for generated Phase 1/2 instruction files. |
| `references/semantic-batch-execution-guide.okf.md` | Stable guidance loaded for every semantic batch. |
| `templates/phase1-prompt-template.okf.md` | Stable Phase 1 prompt. |
| `templates/phase1-run-instructions.okf.yaml` | Generated Phase 1 input shape. |
| `templates/phase2-prompt-template.okf.md` | Stable Phase 2 prompt. |
| `templates/phase2-run-instructions.okf.yaml` | Generated Phase 2 input shape. |
| `templates/semantic-handoff-packet-template.md` | Human projection that points to the prompt, guide, and instruction file. |
| `IMPLEMENTATION-CHANGE-MANIFEST.okf.yaml` | Exact current files/functions that must be changed or added. |

## Hash and lock, in plain language

- **Hash:** a SHA-256 fingerprint of the normalized configuration object. If any locked value changes, the fingerprint changes.
- **Lock:** a logical workflow state, not encryption and not an operating-system file lock. After confirmation, every stage records and checks the same configuration hash.
- **Change handling:** a changed hash blocks execution. The operator must create a new manifest revision; the control plane invalidates every downstream artifact affected by that change.

## Standard run

```text
/apex-kb start
  -> fixed welcome
  -> operator saves run-config.okf.json
  -> schema + read-only preflight
  -> compact operator confirmation
  -> run-manifest.json is hashed and locked
  -> deterministic source intake and Phase 0
  -> Phase 0 stats + topic work pack
  -> generated Phase 1 instructions + stable prompt
  -> bounded semantic batches + deterministic reconciliation
  -> generated Phase 2 instructions + stable prompt
  -> deterministic structural checks
  -> independent semantic acceptance
  -> deterministic postflight
```

## Deliberately deferred

The workflow for **adding new sources to an existing KB, refreshing affected pages, or building another topic against an existing KB** is a separate lifecycle. It must use change detection and impact analysis rather than rerunning the new-KB pipeline. The thin `SKILL.md` contains this as an explicit TODO and blocks accidental use of the new-build route for that purpose.
