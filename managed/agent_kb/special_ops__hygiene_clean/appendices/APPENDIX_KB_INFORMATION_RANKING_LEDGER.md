# APPENDIX_KB_INFORMATION_RANKING_LEDGER

## Purpose

Information ranking ledger for the `special_ops__hygiene_clean` Apex KB base. Rows are candidate extraction units, not accepted truth.

## Ranking fields

`info_id`, `source_class`, `information_unit`, `agent_relevance`, `actionability`, `evidence_strength`, `reuse_frequency_likelihood`, `drift_risk`, `recommended_target_file`, `appendix_pointer`, `scaffold_summary_needed`, `status`.

## Ledger

| info_id | source_class | information_unit | agent_relevance | actionability | evidence_strength | reuse_frequency_likelihood | drift_risk | recommended_target_file | appendix_pointer | scaffold_summary_needed | status |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| HC-INFO-001 | authority_and_verification | Separate pre-step source authority from post-step verification; no authority means no trust and no verification means no approval. | 100 | 100 | 95 | 100 | 20 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#authority-and-verification-gates` | yes | strong_candidate |
| HC-INFO-002 | audit_design | Universal audit checks should inspect chunk self-containment, file typing, pass/fail state, and severity. | 98 | 95 | 90 | 95 | 25 | `TEMPLATES.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-table` | yes | strong_candidate |
| HC-INFO-003 | hygiene_optimization | Optimize hygiene outputs for retrieval clarity, low ambiguity, handoff reliability, and auditability. | 95 | 92 | 88 | 95 | 20 | `ESSENCE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-table` | yes | strong_candidate |
| HC-INFO-004 | role_boundary | Hygiene Clean owns QA reports, hygiene backlog, check execution, and closure recommendations; it does not own truth mutation or promotion. | 100 | 95 | 90 | 100 | 15 | `ESSENCE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#role-boundary-candidates` | yes | strong_candidate |
| HC-INFO-005 | execution_mode_lock | Every execution must declare one mode, exact root, closed target set, stop conditions, and review evidence. | 95 | 95 | 90 | 95 | 30 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#migration-and-patch-drift` | yes | strong_candidate |
| HC-INFO-006 | one_file_at_a_time | Broad multi-file passes create context loss and rewrite cascades; execute one file, validate, then advance. | 92 | 95 | 90 | 95 | 25 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#migration-and-patch-drift` | yes | strong_candidate |
| HC-INFO-007 | rewrite_drift | Content drift occurs when path repair becomes semantic redesign; classify and restore or narrow. | 95 | 90 | 85 | 90 | 45 | `MISTAKES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#wording-and-rewrite-drift` | yes | strong_candidate |
| HC-INFO-008 | execution_compliance | Execution failure appears as explanation instead of action, broad reframing, rewrite instinct, and loss of current task lock. | 95 | 95 | 85 | 95 | 50 | `MISTAKES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#execute-not-explain-failure` | yes | strong_candidate |
| HC-INFO-009 | process_gates | Rules fail when cited as inspiration instead of enforced as blocking gates. | 98 | 95 | 90 | 95 | 35 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#process-gate-bypass` | yes | strong_candidate |
| HC-INFO-010 | target_topology | Target-topology drift happens when a process designs target files before proving merge into living files is impossible. | 90 | 85 | 85 | 80 | 40 | `MISTAKES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#topology-and-merge-mode-drift` | yes | strong_candidate |
| HC-INFO-011 | validation_scope | Validation should check expected file count, missing/extra files, byte/char/line counts, and checksums where exact preservation matters. | 88 | 90 | 90 | 80 | 20 | `TEMPLATES.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#validation-template-candidates` | yes | candidate |
| HC-INFO-012 | residual_guidance | Residual hierarchy decisions must separate confirmed structure, recommended extensions, optional/omitted elements, and open cautions. | 85 | 85 | 85 | 80 | 30 | `TEMPLATES.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#source-and-residual-templates` | yes | candidate |
| HC-INFO-013 | source_manifesting | Duplicate groups, source lanes, agent targets, access blockers, and triage decisions must be visible before extraction. | 92 | 90 | 90 | 90 | 30 | `TEMPLATES.md` | `APPENDIX_KB_SOURCE_MANIFEST.md#duplication-handling` | yes | strong_candidate |
| HC-INFO-014 | evidence_boundary | Failure evidence should remain safeguards and evidence, not automatic universal doctrine. | 95 | 90 | 90 | 95 | 25 | `ESSENCE.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#evidence-status-boundary` | yes | strong_candidate |
| HC-INFO-015 | candidate_approval | Essence candidates require second-agent verification and operator approval where thresholds require it. | 90 | 85 | 85 | 85 | 20 | `LEARNING_QUEUE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-status-rules` | yes | strong_candidate |
| HC-INFO-016 | candidate_scoring | Candidate evaluation should preserve impact, evidence, integration success, risk warning, validator, destination, and confidence. | 85 | 90 | 85 | 90 | 25 | `LEARNING_QUEUE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-scoring-model` | yes | candidate |

## Scaffold routing summary

| Target file | Include only |
|---|---|
| `ESSENCE.md` | compact boundary, optimization priorities, non-promotion rule, appendix map |
| `BEST_PRACTICES.md` | source authority gate, verification gate, execution mode lock, one-file-at-a-time, process docs as blocking gates |
| `MISTAKES.md` | wording drift, execute-not-explain drift, topology drift, move/edit conflation, silent closure |
| `TEMPLATES.md` | finding record, audit pass, closure record, source manifest row, ranking row, evidence note |
| `LEARNING_QUEUE.md` | candidate intake, scoring, validation, promotion routing without acceptance |

## Status

- **Ranking complete:** yes.
- **Material unresolved gap:** no.
- **Accepted truth mutation:** no.
