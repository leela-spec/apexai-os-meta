# Alfred Agent KB

## Purpose

Folder index for Alfred's Apex AI agent knowledge base.

Alfred is the operator-facing intake, alignment, and route-brief lane. This KB records Alfred's source basis, coverage status, role doctrine, routing contract, handoff schema, and workflow playbook.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
file_status: created_as_folder_index
source_phase: pass_a_source_bundle_complete
write_phase_status: core_kb_files_created_or_repaired
source_posture: validated_core_only
leela_surface_map_status: intentionally_skipped_for_this_iteration
validator: meta_ops
next_recommended_action: review_core_kb_or_attach_manual_sources_for_source_extension
```

## Core files

| File | Status | Purpose |
|---|---|---|
| `SOURCE_MANIFEST.md` | repaired | Source ledger for index, repo-readable sources, and local/manual source gaps. |
| `COVERAGE_AUDIT.md` | created | Separates validated, provisional, and source-gap-dependent claim areas. |
| `ROLE_BOUNDARIES.md` | created | Defines Alfred's owns / does-not-own boundaries. |
| `ROUTING_CONTRACT.md` | created | Defines routing targets, route rules, and non-routes. |
| `HANDOFF_SCHEMA.md` | created | Defines required handoff fields, templates, examples, and invalid patterns. |
| `DOCTRINE.md` | created | Compact validated Alfred doctrine. |
| `WORKFLOW_PLAYBOOK.md` | created | Validated Alfred workflows for intake, routing, validation, source gaps, and one-file writes. |
| `LEARNING_QUEUE.md` | pre-existing | Candidate-only learning intake; not accepted doctrine. |

## Intentionally skipped

| File | Status | Reason |
|---|---|---|
| `LEELA_SURFACE_MAP.md` | skipped | User requested to leave it out; detailed Leela surface mechanics remain source-gap-dependent. |

## Routing summary

| Need | Route |
|---|---|
| Execution coordination, sequencing, integration | `meta_ops` |
| Options, scenarios, timing, leverage, recommendation packet | `meta_strategy` |
| Contradiction, adversarial validation, drift-risk review | `meta_detective` |
| Reusable prompt/workflow/handoff/checklist pattern | `special_ops__prompts_workflows` |
| KB placement, source map, candidate/canon separation | `special_ops__knowledge_bank` |
| Clarify operator intent before routing | Alfred/operator loop |

## Source posture

This KB is grounded in the repaired source manifest and coverage audit. Local/manual sources listed there remain source gaps unless they are attached or otherwise directly read in a later source-extension pass.

## Operating rule

Alfred makes the next safe move legible.

A valid Alfred output names the next owner, expected output, evidence basis, constraints, source gaps, validation posture, and stop condition.

## Recommended next actions

1. Review the core KB files for consistency.
2. Attach or make repo-accessible the local/manual source files if detailed Leela surface doctrine is needed.
3. Only after source-extension, consider creating `LEELA_SURFACE_MAP.md` or detailed workflow extensions.
4. Keep future writes one file per turn with fetch-before-write and fetch-back verification.
