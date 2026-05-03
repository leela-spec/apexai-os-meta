# APPENDIX_KB_INFORMATION_RANKING_LEDGER

## Purpose

Information ranking ledger for the `special_ops__hygiene_clean` KB base. Rows are candidate extraction units, not accepted truth.

## Ranking fields

`info_id`, `source_path`, `source_role`, `source_section_or_candidate_id`, `information_unit`, `agent_relevance`, `actionability`, `evidence_strength`, `reuse_frequency_likelihood`, `drift_risk`, `recommended_target_file`, `appendix_pointer`, `scaffold_summary_needed`, `status`.

## Ledger

| info_id | source_path | source_role | source_section_or_candidate_id | information_unit | agent_relevance | actionability | evidence_strength | reuse_frequency_likelihood | drift_risk | recommended_target_file | appendix_pointer | scaffold_summary_needed | status |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| HC-INFO-001 | `AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | primary | SOURCE_AUTHORITY + VERIFICATION_ESCALATION | Separate pre-step source authority from post-step verification; no authority means no trust and no verification means no approval. | 100 | 100 | 95 | 100 | 20 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#authority-and-verification-gates` | yes | strong_candidate |
| HC-INFO-002 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md` | primary ledger | `KB-INFORMATICS-DESIGN-045` | Universal audit checks: self-contained chunks, clear file typing, pass/fail criteria, and severity-aware audit results. | 98 | 95 | 90 | 95 | 25 | `TEMPLATES.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-table` | yes | strong_candidate |
| HC-INFO-003 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md` | primary ledger | `KB-INFORMATICS-DESIGN-050` | Optimize first for retrieval/context efficiency, ambiguity reduction, handoff reliability, and auditability. | 95 | 92 | 88 | 95 | 20 | `ESSENCE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-table` | yes | strong_candidate |
| HC-INFO-004 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md` | primary ledger | `Agent_special_ops__hygiene_clean_Gem.md` | Hygiene Clean owns QA reports, hygiene backlog, and check execution; it does not own truth mutation, architecture design, promotion, or stop law. | 100 | 95 | 90 | 100 | 15 | `ESSENCE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#role-boundary-candidates` | yes | strong_candidate |
| HC-INFO-005 | `AIHowTo/Codex/CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | execution mode lock | Every execution must declare one mode, exact root, closed target set, stop conditions, and Git-visible review. | 95 | 95 | 90 | 95 | 30 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#migration-and-patch-drift` | yes | strong_candidate |
| HC-INFO-006 | `AIHowTo/Codex/CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | one-file-at-a-time rule | Broad multi-file passes create context loss and rewrite cascades; execute one file, validate, then advance. | 92 | 95 | 90 | 95 | 25 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#migration-and-patch-drift` | yes | strong_candidate |
| HC-INFO-007 | `AIHowTo/Codex/Failure&Research/CodexDriftValidation.md` | evidence | wording drift findings | Content drift occurs when path repair becomes semantic redesign; classify as P1/P2 and restore or narrow. | 95 | 90 | 85 | 90 | 45 | `MISTAKES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#wording-and-rewrite-drift` | yes | strong_candidate |
| HC-INFO-008 | `AIHowTo/Codex/Failure&Research/Failure1-ConstantContextLoss.md` | evidence | lessons learned | Execution failure appears as explanation instead of action, broad reframing, rewrite instinct, and loss of current task lock. | 95 | 95 | 85 | 95 | 50 | `MISTAKES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#execute-not-explain-failure` | yes | strong_candidate |
| HC-INFO-009 | `AIHowTo/Codex/Failure&Research/CodexMoveButEditFailure.md` | evidence | process docs as gates | Rules fail when cited as inspiration instead of enforced as blocking gates. | 98 | 95 | 90 | 95 | 35 | `BEST_PRACTICES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#process-gate-bypass` | yes | strong_candidate |
| HC-INFO-010 | `OpenClaw/04_final-system-setup/AdvancedUpdateProcess/DRIFT_SALVAGE_AUDIT.md` | supporting | missing merge-map gate | Target topology drift happens when a process designs target files before proving merge into living files is impossible. | 90 | 85 | 85 | 80 | 40 | `MISTAKES.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#topology-and-merge-mode-drift` | yes | strong_candidate |
| HC-INFO-011 | `OpenClaw/04_final-system-setup/BaselinePatches/VALIDATION_REPORT.md` | supporting | validation scope | Validation should check expected file count, missing/extra files, byte/char/line counts, and checksums where exact preservation matters. | 88 | 90 | 90 | 80 | 20 | `TEMPLATES.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#validation-template-candidates` | yes | candidate |
| HC-INFO-012 | `OpenClaw/04_final-system-setup/BaselinePatches/HIERARCHY_AND_RESIDUAL_GUIDANCE.md` | supporting | residual cautions | Residual hierarchy decisions must separate confirmed structure, recommended extensions, optional/omitted elements, and open cautions. | 85 | 85 | 85 | 80 | 30 | `TEMPLATES.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#source-and-residual-templates` | yes | candidate |
| HC-INFO-013 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md` | primary ledger | duplicate/access inventory | Duplicate groups, source lanes, agent targets, access blockers, and triage decisions must be visible before extraction. | 92 | 90 | 90 | 90 | 30 | `TEMPLATES.md` | `APPENDIX_KB_SOURCE_MANIFEST.md#duplication-handling` | yes | strong_candidate |
| HC-INFO-014 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | primary ledger | failure safeguards | Failure evidence should remain safeguards and evidence, not automatic universal doctrine. | 95 | 90 | 90 | 95 | 25 | `ESSENCE.md` | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#evidence-status-boundary` | yes | strong_candidate |
| HC-INFO-015 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md` | primary ledger | candidate-only warning | Essence candidates require second-agent verification and operator approval where thresholds require it. | 90 | 85 | 85 | 85 | 20 | `LEARNING_QUEUE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-status-rules` | yes | strong_candidate |
| HC-INFO-016 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md` | primary ledger | scoring formula | Candidate evaluation should preserve impact, evidence, integration success, risk warning, validator, destination, and confidence. | 85 | 90 | 85 | 90 | 25 | `LEARNING_QUEUE.md` | `APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-scoring-model` | yes | candidate |

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
- **Proceed to candidate ledger:** yes.
