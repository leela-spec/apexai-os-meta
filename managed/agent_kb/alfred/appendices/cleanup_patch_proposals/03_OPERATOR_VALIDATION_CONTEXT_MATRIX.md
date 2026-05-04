# Operator Validation Context Matrix

Purpose: compact human validation layer for the Alfred KB cleanup proposal.

No cleanup patches are applied by this file. Use it to approve, reject, or revise the proposed deletions before any locked Codex apply instruction is created.

## Why deletion diffs exist

The intended operation is deletion. The `.diff` files are not extra product artifacts; they are reviewable, auditable deletion recipes.

They exist so the operator can validate exact removals before anything is deleted, and so Codex later applies only approved changes one by one.

## Validation options

| option | meaning | when to choose |
|---|---|---|
| A — delete | Remove the file. | File is obsolete, redirect-only, already integrated, or historical patch debris. |
| B — extract then delete | First move unique high-impact content into the correct canonical file or appendix, then delete. | File contains one remaining useful rule, schema, decision, or candidate. |
| C — keep for now | Do not delete in this cleanup pass. | Integration is unclear, references are active, or provenance is still needed. |
| D — revise proposal | Keep the target decision, but require a better exact diff or reference cleanup first. | Proposal is directionally right but not apply-ready. |

## Recommended decisions

| id | target | context | recommendation | reason | operator choice |
|---|---|---|---|---|---|
| D001 | `appendices/APEX_ALFRED_CANONICAL_PATCH_DIFFS_OPTION_B.patch` | historical patch artifact | A — delete | Patch artifacts should not remain as runtime KB authority after canonical content is promoted. | pending |
| D002 | `working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` | working decision lock | A — delete after refs | Content appears promoted into process-handover appendices/canonical scaffold; keep only source/audit trace if needed. | pending |
| D003 | `working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md` | non-canonical handover prompt flow | A — delete after refs | Prompt flow is superseded by resulting appendices/canonical structure. | pending |
| D004 | `working/ALFRED_WORKFLOW_DECISION_LOCK.md` | parent working lock | C or D | Needs final high-impact/provenance check before safe deletion. | pending |
| D005 | `working/ALFRED_WORKFLOW_PREFILLED_QA.md` | support QA/context | B or C | Delete only if no candidate remains for `LEARNING_QUEUE.md`. | pending |
| D006 | `working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md` | completed patch handover | A or C | Likely delete, but provenance value should be checked first. | pending |
| D007 | `AGENT_CARD.md` | absorbed redirect | A — delete | Redirect-only; canonical owners already listed. | pending |
| D008 | `DOCTRINE.md` | absorbed redirect | A — delete | Redirect-only; doctrine already points to canonical files. | pending |
| D009 | `ROLE_BOUNDARIES.md` | absorbed redirect | A — delete | Redirect-only; boundary content points to `ESSENCE`, `BEST_PRACTICES`, `MISTAKES`. | pending |
| D010 | `HANDOFF_SCHEMA.md` | absorbed redirect | A — delete | Redirect-only; forms/process authority point to `TEMPLATES` and process contracts. | pending |
| D011 | `ROUTING_CONTRACT.md` | moved redirect | A — delete | Active routing matrix lives in `appendices/APPENDIX_ROUTING_MATRIX.md`. | pending |
| D012 | `WORKFLOW_PLAYBOOK.md` | moved redirect | A — delete | Active workflow playbook lives in `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`. | pending |

## Recommended validation package

| package | approve these | hold these | why |
|---|---|---|---|
| Conservative cleanup | D001, D007-D012 | D002-D006 | Deletes obvious patch/redirect clutter only. Lowest risk. |
| Standard cleanup | D001-D003, D007-D012 | D004-D006 | Deletes obvious clutter plus already-promoted working flow files. Balanced. |
| Aggressive cleanup | D001-D012 | none | Only safe after full final reference/provenance check and apply-ready diffs for every target. |

## My recommendation

Choose **Standard cleanup**:

- approve D001-D003 and D007-D012,
- hold D004-D006 until final provenance/high-impact check,
- then create exact apply-ready deletion diffs and reference cleanup patches,
- only then create `99_CODEX_APPLY_APPROVED_DIFFS_ONLY.md`.

## Apply-readiness caveat

Some proposal `.diff` files are intentionally marked `needs_revision_before_apply`. That is not a decision failure; it means the deletion direction is proposed, but the exact patch must still be regenerated and checked before Codex can apply it.
