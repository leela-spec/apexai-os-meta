# Alfred Agent KB

## Purpose

Folder index for Alfred's Apex AI agent knowledge base.

Alfred is the operator-facing intake, alignment, and route-brief lane. The Alfred KB now resolves through the canonical five-file scaffold. Additional files are either source/audit controls or temporary appendices pending redirect/removal.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
file_status: folder_index_after_canonical_consolidation
source_phase: pass_a_source_bundle_complete
canonical_consolidation_status: complete
source_posture: validated_core_only
canonical_scaffold_status: primary_runtime_kb_interface
supporting_material_status: absorbed_or_control_or_pending_redirect
leela_surface_map_status: intentionally_skipped_for_this_iteration
validator: meta_ops
next_recommended_action: redirect_or_remove_absorbed_support_files_one_at_a_time
```

## Canonical five-file KB scaffold

The canonical Alfred KB interface is the five-file scaffold defined by `managed/agent_kb/AGENT_KB_INDEX.md`, `managed/knowledge/AGENT_KB_LANES.md`, and `managed/knowledge/KB_STARTING_SOURCE_MAP.md`.

| File | Status | Primary role | Consolidation result |
|---|---|---|---|
| `ESSENCE.md` | consolidated | Accepted compact identity, authority, owns/does-not-own boundary, activation triggers, input/output contract, and durable Alfred doctrine. | Absorbed durable identity/boundary content from `AGENT_CARD.md`, `DOCTRINE.md`, and `ROLE_BOUNDARIES.md`. |
| `BEST_PRACTICES.md` | consolidated | Accepted Alfred operating method: intake, alignment, routing, boundary checks, source-gap protection, EVD/IMP/RSK use, and one-file repair discipline. | Absorbed durable practice content from `ROLE_BOUNDARIES.md`, `ROUTING_CONTRACT.md`, and `WORKFLOW_PLAYBOOK.md`. |
| `MISTAKES.md` | consolidated | Accepted recurring Alfred failure patterns and anti-patterns. | Added scaffold-replacement drift, appendix-as-authority drift, duplicate-doctrine drift, template-governance confusion, and self-validation risk. |
| `TEMPLATES.md` | consolidated | Accepted reusable Alfred forms. | Absorbed reusable handoff and route-brief forms from `HANDOFF_SCHEMA.md`. |
| `LEARNING_QUEUE.md` | guarded | Candidate-only learning intake; never runtime truth. | Added canonical target map, candidate boundary rules, and consolidation guardrail. |

## Support-file classification

The files below no longer define a second KB scaffold. They are classified by current post-consolidation role.

| File | Current classification | Canonical owner / next action |
|---|---|---|
| `AGENT_CARD.md` | absorbed duplicate | Durable content is now in `ESSENCE.md`. Next action: redirect or delete. |
| `DOCTRINE.md` | absorbed duplicate | Durable doctrine is now in `ESSENCE.md`; practice/failure material moved into `BEST_PRACTICES.md` / `MISTAKES.md`. Next action: redirect or delete. |
| `ROLE_BOUNDARIES.md` | absorbed duplicate / possible temporary appendix | Core boundaries are now in `ESSENCE.md`; boundary practices and failures are now in `BEST_PRACTICES.md` / `MISTAKES.md`. Next action: redirect unless detailed appendix remains required. |
| `ROUTING_CONTRACT.md` | absorbed duplicate / possible temporary appendix | Routing method is now in `BEST_PRACTICES.md`; route forms are now in `TEMPLATES.md`. Next action: redirect unless detailed route matrix remains required. |
| `HANDOFF_SCHEMA.md` | absorbed duplicate / possible temporary appendix | Core handoff forms and invalid-use patterns are now in `TEMPLATES.md` / `MISTAKES.md`. Next action: redirect unless extended examples remain required. |
| `WORKFLOW_PLAYBOOK.md` | absorbed duplicate / possible temporary appendix | Workflow methods are now in `BEST_PRACTICES.md`; reusable forms are now in `TEMPLATES.md`. Next action: redirect unless extended playbook remains required. |
| `SOURCE_MANIFEST.md` | source/audit control | Keep. This is provenance and source-status control, not doctrine. |
| `COVERAGE_AUDIT.md` | source/audit control | Keep. This constrains validated/provisional/source-gap claims, but is not accepted doctrine by itself. |

## Intentionally skipped

| File | Status | Reason |
|---|---|---|
| `LEELA_SURFACE_MAP.md` | skipped | Detailed Leela surface mechanics remain source-gap-dependent unless a later source-extension pass reads the relevant attached/manual sources. |

## Canonical ownership rule

| Content type | Canonical destination |
|---|---|
| identity, authority, owns/does-not-own, activation triggers | `ESSENCE.md` |
| operating method, routing practice, boundary checks, source-gap practice, EVD/IMP/RSK use | `BEST_PRACTICES.md` |
| recurring failure pattern, drift risk, invalid use, anti-pattern | `MISTAKES.md` |
| reusable intake form, route brief, handoff packet, escalation form, report format | `TEMPLATES.md` |
| unvalidated future learning | `LEARNING_QUEUE.md` |
| provenance, source status, coverage state | `SOURCE_MANIFEST.md` / `COVERAGE_AUDIT.md` |

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

Accepted canonical files must not harden claims from unread local/manual sources. Source/audit files may record source gaps, provisional interpretations, and audit controls, but they do not make those claims accepted runtime truth by storage alone.

## Operating rule

Alfred makes the next safe move legible.

A valid Alfred output names the next owner, expected output, evidence basis, constraints, source gaps, validation posture, and stop condition.

## Maintenance rule

When adding or repairing Alfred KB material:

1. Keep the five canonical files as the primary KB scaffold.
2. Route durable content to the correct canonical owner by content type.
3. Keep `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` as source/audit controls.
4. Do not let support files become a parallel scaffold.
5. Keep `LEARNING_QUEUE.md` candidate-only.
6. Keep future writes one file per turn with fetch-before-write and fetch-back verification.
7. Redirect or delete absorbed duplicate support files only after their durable content has been verified in canonical files.

## Recommended next actions

1. Redirect or delete `AGENT_CARD.md` after verifying `ESSENCE.md` remains sufficient.
2. Redirect or delete `DOCTRINE.md` after verifying `ESSENCE.md`, `BEST_PRACTICES.md`, and `MISTAKES.md` remain sufficient.
3. Decide whether `ROLE_BOUNDARIES.md`, `ROUTING_CONTRACT.md`, `HANDOFF_SCHEMA.md`, and `WORKFLOW_PLAYBOOK.md` should become slim appendices or redirects.
4. Keep `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md`.
5. Run a separate source-extension pass before hardening detailed Leela surface mechanics.
