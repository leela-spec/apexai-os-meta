# APPENDIX_KB_SOURCE_MANIFEST

## Purpose

Apex-local source manifest for the `special_ops__hygiene_clean` KB base.

This appendix records coverage, role fit, duplication handling, gap risk, and authority-risk disposition for the Hygiene Clean KB. It does not preserve source-repo provenance and is not a runtime truth surface.

## Execution lock

| Field | Value |
|---|---|
| agent | `special_ops__hygiene_clean` |
| repo | `leela-spec/apexai-os-meta` |
| branch | `main` |
| target_root | `managed/agent_kb/special_ops__hygiene_clean/` |
| mode | Apex KB base promotion with legacy-value reconciliation |
| write_scope | target root only |

## Source authority order used

| Tier | Source class | Role in this KB | Status |
|---|---|---|---|
| 1 | Apex Hygiene KB base files | canonical new base for scaffold and appendices | used |
| 2 | Existing Apex Hygiene KB files | legacy-value source only | used selectively |
| 3 | Apex promotion and validation constraints | promotion, validation, and authority boundary checks | used selectively |

## Coverage check

| Surface | Coverage status | Notes |
|---|---|---|
| `ESSENCE.md` | represented | compact boundary, doctrine, read triggers, scaffold map, appendix map, status metadata |
| `BEST_PRACTICES.md` | represented | reusable hygiene rules with candidate status and evidence pointers |
| `MISTAKES.md` | represented | drift/failure patterns and recovery playbook |
| `LEARNING_QUEUE.md` | represented | candidate-only queue and Apex promotion route |
| `TEMPLATES.md` | legacy only | no clear canonical new-base counterpart was found; not overwritten |
| `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | represented | ranked information units and scaffold routing |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | represented | candidate units, scoring, role boundaries, and template candidates |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | represented | anti-drift evidence classes and safeguards |

## Role-fit check

| Check | Result | Notes |
|---|---|---|
| Structural QA / hygiene fit | pass | KB focuses on audit, source integrity, pointer checks, closure, and drift control. |
| Promotion authority leakage | pass | Candidate and evidence entries remain non-promotional. |
| Runtime/config mutation leakage | pass | No runtime config or provider/model config authority is claimed. |
| Architecture ownership leakage | pass | Hygiene records and routes findings; it does not own architecture design. |
| External source-repo provenance | pass | External source-repo provenance is intentionally omitted. |

## Duplication handling

| Duplicate class | Handling |
|---|---|
| Legacy empty-state scaffold | rejected because new KB content now exists |
| Legacy owner/validator/review metadata | patched compactly into scaffold status notes |
| Legacy promotion-route reference | patched into `LEARNING_QUEUE.md` |
| New-base filename mismatch | resolved by heading identity during this Apex-only reconciliation |
| External source/provenance labels | removed or generalized into Apex-local source classes |

## Gap risk

| Gap | Severity | Disposition |
|---|---|---|
| No clear canonical new-base `TEMPLATES.md` located | P1 | current legacy `TEMPLATES.md` left untouched; create or place a clean new-base templates file before promotion |
| New-base files were not filename-clean | P2 | reconciled by heading identity for clearly identifiable files; future uploads should preserve filename identity |
| Some appendix rows rely on evidence IDs whose full source detail is summarized rather than reproduced | P3 | acceptable for KB base; evidence remains pointer-based and non-promotional |

## Authority risk

| Risk | Control |
|---|---|
| Treating a hygiene finding as accepted truth | keep `candidate`, `strong_candidate`, and `evidence_only` statuses explicit |
| Treating scaffold guidance as runtime law | mark scaffold as `accepted_in_kb_base`, not standalone runtime truth |
| Turning cleanup into architecture authority | keep architecture, strategy, config, and promotion boundaries explicit |
| Silent closure of P0/P1 findings | require explicit evidence-backed closure |
| Carrying obsolete legacy content forward | use legacy files only for compact Apex-specific value |

## Conflict report decision

`SOURCE_CONFLICT_REPORT.md` was not created.

Reason: no material source conflict blocked this promotion. The only blocking mismatch was filename placement, resolved only where heading identity was clear.

## Build disposition

- **Coverage:** pass, except `TEMPLATES.md` pending clean new base.
- **Role fit:** pass.
- **Duplication:** bounded.
- **Gap risk:** non-blocking for promoted files.
- **Authority risk:** controlled by status and promotion boundaries.
