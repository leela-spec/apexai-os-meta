# Alfred Agent KB

## Purpose

Folder index for Alfred's Apex AI agent knowledge base.

Alfred is the operator-facing intake, alignment, and route-brief lane. This KB keeps Alfred's accepted doctrine in the canonical five-file scaffold and links additional source-control, coverage, routing, handoff, and workflow material as supporting KB references.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
file_status: folder_index_reconciled_with_canonical_scaffold
source_phase: pass_a_source_bundle_complete
write_phase_status: core_kb_files_created_or_repaired
source_posture: validated_core_only
canonical_scaffold_status: primary_runtime_kb_interface
supporting_material_status: indexed_and_linked_not_scaffold_replacement
leela_surface_map_status: intentionally_skipped_for_this_iteration
validator: meta_ops
next_recommended_action: audit_and_patch_canonical_files_for_links_to_supporting_material
```

## Canonical five-file KB scaffold

The canonical Alfred KB interface is the five-file scaffold defined by `managed/agent_kb/AGENT_KB_INDEX.md`, `managed/knowledge/AGENT_KB_LANES.md`, and `managed/knowledge/KB_STARTING_SOURCE_MAP.md`.

| File | Status | Primary role | Supporting material that should inform it |
|---|---|---|---|
| `ESSENCE.md` | exists | Accepted compact role boundary and durable Alfred doctrine. | `AGENT_CARD.md`, `ROLE_BOUNDARIES.md`, `DOCTRINE.md`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md` |
| `BEST_PRACTICES.md` | exists | Accepted reusable Alfred practices. | `WORKFLOW_PLAYBOOK.md`, `ROUTING_CONTRACT.md`, `HANDOFF_SCHEMA.md`, `COVERAGE_AUDIT.md` |
| `MISTAKES.md` | exists | Accepted recurring Alfred failure patterns and anti-patterns. | `ROLE_BOUNDARIES.md`, `COVERAGE_AUDIT.md`, `SOURCE_MANIFEST.md` |
| `TEMPLATES.md` | exists | Accepted reusable Alfred local templates. | `HANDOFF_SCHEMA.md`, `ROUTING_CONTRACT.md`, `WORKFLOW_PLAYBOOK.md` |
| `LEARNING_QUEUE.md` | exists | Candidate-only learning intake; never runtime truth. | `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`, promotion governance |

## Supporting indexed KB material

The files below are valid supporting KB material. They do not replace the canonical five-file scaffold. Their most important durable content should be represented, linked, or summarized inside the relevant canonical file when it is accepted doctrine, practice, mistake, template, or candidate learning.

| File | Status | Role | Canonical representation rule |
|---|---|---|---|
| `AGENT_CARD.md` | created | Fast identity card and operational summary. | Core identity belongs in `ESSENCE.md`; only keep this as a quick index/card. |
| `SOURCE_MANIFEST.md` | repaired | Source ledger for index, repo-readable sources, and local/manual source gaps. | Source posture should be referenced by all canonical files when source status matters. |
| `COVERAGE_AUDIT.md` | created | Separates validated, provisional, and source-gap-dependent claim areas. | Provisional/source-gap warnings should constrain `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, and `TEMPLATES.md`. |
| `ROLE_BOUNDARIES.md` | created | Detailed owns / does-not-own boundary file. | Most important durable boundary belongs in `ESSENCE.md`; failure implications belong in `MISTAKES.md`. |
| `ROUTING_CONTRACT.md` | created | Detailed routing targets, route rules, and non-routes. | Most important routing practice belongs in `BEST_PRACTICES.md`; route templates belong in `TEMPLATES.md`. |
| `HANDOFF_SCHEMA.md` | created | Required handoff fields, examples, and invalid handoff patterns. | Core handoff schema belongs in `TEMPLATES.md`; invalid handoff patterns belong in `MISTAKES.md`. |
| `DOCTRINE.md` | created | Conservative validated Alfred doctrine summary. | Durable doctrine belongs primarily in `ESSENCE.md`; this file remains a supporting synthesis. |
| `WORKFLOW_PLAYBOOK.md` | created | Repeatable Alfred workflows for intake, routing, validation, source gaps, and one-file writes. | Stable practices belong in `BEST_PRACTICES.md`; reusable workflow templates belong in `TEMPLATES.md`. |

## Intentionally skipped

| File | Status | Reason |
|---|---|---|
| `LEELA_SURFACE_MAP.md` | skipped | Detailed Leela surface mechanics remain source-gap-dependent unless a later source-extension pass reads the relevant attached/manual sources. |

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

Accepted canonical files must not harden claims from unread local/manual sources. Supporting files may record source gaps, provisional interpretations, and audit controls, but they do not make those claims accepted runtime truth by storage alone.

## Operating rule

Alfred makes the next safe move legible.

A valid Alfred output names the next owner, expected output, evidence basis, constraints, source gaps, validation posture, and stop condition.

## Maintenance rule

When adding or repairing Alfred KB material:

1. Keep the five canonical files as the primary KB scaffold.
2. Put detailed control, source, coverage, routing, and workflow expansions in supporting files.
3. Add or preserve links from canonical files to supporting files where the supporting file contains operationally important material.
4. Do not treat supporting files as a separate replacement scaffold.
5. Keep `LEARNING_QUEUE.md` candidate-only.
6. Keep future writes one file per turn with fetch-before-write and fetch-back verification.

## Recommended next actions

1. Audit `ESSENCE.md` and ensure it links the most important supporting doctrine without absorbing source-control detail.
2. Audit `BEST_PRACTICES.md` and normalize any `IDX-N4` or source-gap-dependent language against `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md`.
3. Audit `MISTAKES.md` and ensure source-gap hardening and scaffold-replacement drift are represented as accepted anti-patterns.
4. Audit `TEMPLATES.md` and ensure the handoff/routing templates link back to `HANDOFF_SCHEMA.md` and `ROUTING_CONTRACT.md`.
5. Attach/read manual sources in a separate source-extension pass before hardening detailed Leela surface mechanics.
