# Alfred Agent KB

## Purpose

Folder index for Alfred's Apex AI agent knowledge base.

Alfred is the operator-facing intake, alignment, and route-brief lane. The Alfred KB resolves through the canonical five-file scaffold. Additional files are either source/audit controls, absorbed redirects, moved redirects, or active subordinate appendices under `appendices/` that support retrieval without becoming parallel authority.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
file_status: folder_index_after_appendix_folder_move
source_phase: pass_a_source_bundle_complete
canonical_consolidation_status: complete
absorbed_redirect_pass_status: complete
appendix_decision_pass_status: complete
appendix_folder_move_status: complete
source_posture: validated_core_only
canonical_scaffold_status: primary_runtime_kb_interface
supporting_material_status: redirected_or_subordinate_appendix_or_source_audit_control
leela_surface_map_status: intentionally_skipped_until_source_extension
validator: meta_ops
next_recommended_action: run_manual_source_extension_audit_before_hardening_detailed_leela_surface_mechanics
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

The files below do not define a second KB scaffold.

| File | Current classification | Canonical owner / role |
|---|---|---|
| `AGENT_CARD.md` | absorbed redirect | Durable identity, activation, boundary, input/output, and quality-bar material resolves to `ESSENCE.md`, with method/forms/source posture routed to the relevant canonical or source/audit files. |
| `DOCTRINE.md` | absorbed redirect | Durable doctrine resolves to `ESSENCE.md`; operating method resolves to `BEST_PRACTICES.md`; failure-pattern material resolves to `MISTAKES.md`. |
| `ROLE_BOUNDARIES.md` | absorbed redirect | Boundary doctrine resolves to `ESSENCE.md`; boundary practice resolves to `BEST_PRACTICES.md`; boundary failures resolve to `MISTAKES.md`. |
| `HANDOFF_SCHEMA.md` | absorbed redirect | Reusable Alfred handoff forms resolve to `TEMPLATES.md`; process-level handoff authority resolves to `managed/processes/AGENT_HANDOFF_CONTRACTS.md`. |
| `ROUTING_CONTRACT.md` | moved redirect | Active routing appendix moved to `appendices/APPENDIX_ROUTING_MATRIX.md`. |
| `WORKFLOW_PLAYBOOK.md` | moved redirect | Active workflow appendix moved to `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`. |
| `SOURCE_MANIFEST.md` | source/audit control | Keep. This is provenance and source-status control, not doctrine. |
| `COVERAGE_AUDIT.md` | source/audit control | Keep. This constrains validated/provisional/source-gap claims, but is not accepted doctrine by itself. |

## Active subordinate appendices

| Appendix file | Appendix type | Reason retained | Canonical owner |
|---|---|---|---|
| `appendices/APPENDIX_ROUTING_MATRIX.md` | routing matrix | Preserves detailed per-target trigger/rationale/output lookup tables with retrieval value beyond canonical summaries. | `BEST_PRACTICES.md` |
| `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md` | workflow playbook | Preserves detailed stepwise workflows, outputs, and stop conditions that would bloat `BEST_PRACTICES.md`. | `BEST_PRACTICES.md` |

Appendices are subordinate references. They must not introduce new route targets, route authority, process authority, accepted doctrine, source status, or promotion rules unless the canonical owner and promotion path are updated first.

## Redirect files

| Redirect file | Use instead |
|---|---|
| `AGENT_CARD.md` | `ESSENCE.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md` |
| `DOCTRINE.md` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md` |
| `ROLE_BOUNDARIES.md` | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md` |
| `HANDOFF_SCHEMA.md` | `TEMPLATES.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `managed/processes/AGENT_HANDOFF_CONTRACTS.md` |
| `ROUTING_CONTRACT.md` | `appendices/APPENDIX_ROUTING_MATRIX.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md`, `managed/processes/AGENT_HANDOFF_CONTRACTS.md` |
| `WORKFLOW_PLAYBOOK.md` | `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md`, `managed/processes/AGENT_HANDOFF_CONTRACTS.md` |

Do not add new doctrine to redirect files. Redirect files exist for compatibility and pointer hygiene only.

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
| detailed route lookup table or workflow procedure too bulky for canonical files | `appendices/` subordinate appendix only |

## Routing summary

| Need | Route |
|---|---|
| Execution coordination, sequencing, integration | `meta_ops` |
| Options, scenarios, timing, leverage, recommendation packet | `meta_strategy` |
| Contradiction, adversarial validation, drift-risk review | `meta_detective` |
| Reusable prompt/workflow/handoff/checklist pattern | `special_ops__prompts_workflows` |
| KB placement, source map, candidate/canon separation | `special_ops__knowledge_bank` |
| Clarify operator intent before routing | Alfred/operator loop |

For detailed routing lookup, use `appendices/APPENDIX_ROUTING_MATRIX.md` as a subordinate appendix. If the appendix conflicts with `ESSENCE.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md`, or `managed/processes/AGENT_HANDOFF_CONTRACTS.md`, the canonical/process owner wins.

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
4. Keep subordinate appendices retrieval-focused and explicitly subordinate.
5. Keep active appendices under `appendices/`; keep old root paths as redirects for compatibility.
6. Do not let support files become a parallel scaffold.
7. Keep `LEARNING_QUEUE.md` candidate-only.
8. Keep future writes one file per turn where possible; structural moves may require create-new-file plus redirect-old-file.
9. Use the governed promotion path for truth-bearing changes.
10. Run source-extension audit before hardening detailed Leela surface mechanics.

## Recommended next actions

1. Run the manual source-extension audit before creating `LEELA_SURFACE_MAP.md` or hardening detailed Leela mechanics.
2. Update `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` only after source-extension audit records actual read status.
3. Keep old root-path redirects until repo references are updated or compatibility is no longer needed.
