# APPENDIX_KB_SOURCE_MANIFEST

## Purpose

Source manifest for the `special_ops__hygiene_clean` KB base build.

This appendix records the indexed source slice, coverage check, duplication handling, gap risk, and authority-risk disposition before scaffold drafting.

## Execution lock

| Field | Value |
|---|---|
| agent | `special_ops__hygiene_clean` |
| repo | `leela-spec/MasterOfArts` |
| branch | `main` |
| target_root | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/` |
| mode | appendix-first KB base build |
| write_scope | target root only |

## Current update authority note

For the approved Hygiene Clean KB scaffold-update pass, `appendices/ChangesHygiene.md` and `appendices/ChangesHygiene2.md` are the local approval and design-table authorities.

`appendices/PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md` governs creation of the per-file unified-diff artifacts for that pass.

The older base-build promptflow remains historical build context only. It does not supersede the current folder-local unified-diff manufacturing promptflow for this update sequence.

## Source authority order used

| Tier | Source | Role in this build | Status |
|---|---|---|---|
| 1 | `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` | primary source-index slice for target agent | used |
| 2 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md` | top-ranked candidate selection by agent | used |
| 3 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md` | duplicate/access/triage evidence | used |
| 4 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md` | normalized idea and scoring evidence | used |
| 5 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md` | role boundary and ownership guardrails | used |
| 6 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md` | compact candidate doctrine evidence | used |
| 7 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | anti-drift and failure evidence | used |

## Indexed source slice

| Source path | Source role | Read instruction | Inclusion status | Hygiene-clean relevance |
|---|---|---|---|---|
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | primary | read full | included | drift prevention, cleanup failures, audit safeguards |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md` | primary | read full | included | duplicate handling, access blockers, source triage |
| `AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | primary | read full | included | source authority, verification, stop/escalation gates |
| `AIHowTo/Codex/CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | read full | included | mode lock, path discipline, one-file-at-a-time hygiene |
| `AIHowTo/Codex/Failure&Research/CodexDriftValidation.md` | evidence | evidence only | included | wording drift, migration overreach, content-preservation failures |
| `AIHowTo/Codex/Failure&Research/Failure1-ConstantContextLoss.md` | evidence | evidence only | included | execute-not-explain failure, context loss, fence corruption handling |
| `AIHowTo/Codex/Failure&Research/CodexMoveButEditFailure.md` | evidence | evidence only | included | move/edit conflation and process-gate bypass evidence |
| `OpenClaw/04_final-system-setup/AdvancedUpdateProcess/DRIFT_SALVAGE_AUDIT.md` | supporting | read full | included | drift root-cause classification and salvage path |
| `OpenClaw/04_final-system-setup/BaselinePatches/VALIDATION_REPORT.md` | supporting | read full | included | validation checklist, source/target checksum discipline |
| `OpenClaw/04_final-system-setup/BaselinePatches/HIERARCHY_AND_RESIDUAL_GUIDANCE.md` | supporting | read full | included | hierarchy guidance, residual caution, placement hygiene |

## Top-ranked candidate coverage

| Candidate id | Source basis | Covered in | Coverage status |
|---|---|---|---|
| `KB-INFORMATICS-DESIGN-017` | open questions and provisional-boundary discipline | information ranking ledger; candidate ledger | represented |
| `KB-INFORMATICS-DESIGN-045` | universal audit checks | information ranking ledger; candidate ledger; templates | represented |
| `KB-INFORMATICS-DESIGN-048` | file type table and retrieval expectations | information ranking ledger; candidate ledger | represented |
| `KB-INFORMATICS-DESIGN-050` | optimization priorities | information ranking ledger; best practices | represented |
| `KB-INFORMATICS-DESIGN-054` | stable terminology and chunk vocabulary | information ranking ledger; best practices | represented |
| `KB-INFORMATICS-DESIGN-063` | alternate file-type table evidence | candidate ledger; duplication notes | represented |
| `KB-META-OPS-001` | iterative process and density gates | information ranking ledger; templates | represented |
| `KB-CODEX-EXECUTION-PROCESS-073` | process drift from simple patching to over-engineering | anti-drift appendix; mistakes | represented |
| `KB-FAILURE-POSTMORTEMS-AND-ANTI-DRIFT-009` | retrieval clarity, low drift, auditability | essence; best practices | represented |
| `KB-META-OPS-023` | density-check bypass finding | anti-drift appendix; mistakes | represented |
| `KB-PROMPTS-WORKFLOWS-024` | one artifact per step and stop-after-step discipline | templates; best practices | represented |
| `KB-PROMPTS-WORKFLOWS-048` | terminology prompt evidence | candidate ledger | represented |

## Role-fit check

| Check | Result | Notes |
|---|---|---|
| Structural QA / hygiene fit | pass | Sources emphasize audit checks, pointer/source integrity, drift detection, and closure discipline. |
| Strategy authority leakage | pass | Strategy and broad roadmap content excluded except where it constrains hygiene. |
| Promotion authority leakage | pass | Candidate and evidence entries remain non-promotional; hygiene findings do not mutate accepted truth. |
| Informatics-design constraint use | pass | Included only for auditability, chunk integrity, file typing, and retrieval hygiene. |
| Evidence-only postmortem use | pass | Postmortems are used as failure evidence and recovery guidance, not universal doctrine. |

## Duplication handling

| Duplicate class | Handling |
|---|---|
| `same_filename_elsewhere` records | representative repo-accessible source is recorded once; variants remain evidence, not separate scaffold doctrine |
| exact duplicate groups | do not duplicate candidate rows unless the variant changes role or risk meaning |
| local-source labels in ledgers | map to repo-accessible representative paths when the source index supplies them |
| prompt/workflow duplicates | include only when they constrain hygiene execution, not prompt-cookbook content |

## Gap risk

| Gap | Source-gap severity | Disposition | Follow-up |
|---|---|---|---|
| One source-inventory access blocker exists for an external/local `UpdateProcessSSOTS` directory | P2 | not blocking for this build because the promptflow source slice has repo-accessible sources and ledgers sufficient for KB base extraction | monitor if future update depends on blocked external/local material |
| Several ledger source paths preserve older local corpus labels | P3 | handled by mapping to repo-accessible source-index paths or treating as ledger evidence only | preserve representative-source mapping in future manifests |
| Some high-value informatics-design raw sources are represented through ledgers rather than fetched as standalone raw files | P2 | acceptable for this KB base because the target agent needs compact hygiene doctrine plus appendices, not full informatics canon extraction | revisit only if Hygiene needs deeper Informatics-owned doctrine |

## Authority risk

| Risk | Control |
|---|---|
| Treating a hygiene finding as accepted truth | keep findings in candidate/evidence status unless promotion accepts them |
| Treating a source summary as primary when raw source exists | use source index and direct files first; mark ledger summaries as derived when appropriate |
| Turning cleanup into design authority | restrict scaffold rules to QA, validation, drift detection, and closure mechanics |
| Collapsing evidence and rule | store postmortems in anti-drift appendix and summarize only reusable safeguards in scaffold files |
| Silent closure of P0/P1 findings | require explicit finding records and closure evidence |

## Source Notes register

| note_id | source_path | source_gap_severity | source_note_type | decision | rationale | affected_candidates | affected_scaffold_files | follow_up | status |
|---|---|---|---|---|---|---|---|---|---|
| SN-HC-001 | `appendices/ChangesHygiene.md`; `appendices/ChangesHygiene2.md` | none | authority_note | use as current update authority | Operator approved all listed integrations; design table declares exact changed-file set. | `HYG-UPD-001` to `HYG-UPD-013`; `HC-CAND-001` to `HC-CAND-016` | all approved changed files | validate patch artifacts against both files | monitored |
| SN-HC-002 | `appendices/PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md` | none | authority_note | govern unified-diff artifact creation | Prevents scope expansion and requires one diff artifact per target file. | all approved update candidates | all approved changed files | final patchset validation after all seven artifacts exist | monitored |
| SN-HC-003 | external/local `UpdateProcessSSOTS` directory | P2 | access_blocker | non-blocking for current pass | Current target-folder-local authorities and existing ledgers are sufficient for approved diff artifact creation. | none directly | none directly | revisit only if future work depends on that directory | deferred |
| SN-HC-004 | older local corpus labels in source ledgers | P3 | representative_choice | map to repo-accessible representative paths or treat as ledger evidence | Prevents source-summary substitution while preserving evidence lineage. | source and provenance candidates | source manifest and candidate ledger | preserve mapping notes in future manifest refreshes | monitored |

## Conflict Watch register

| watch_id | potential_conflict | affected_scope | severity | current_handling | escalation_condition | status |
|---|---|---|---|---|---|---|
| CW-HC-001 | Historical base-build promptflow vs current unified-diff manufacturing promptflow | current KB update sequence | P2 | current folder-local unified-diff promptflow governs this pass | if an artifact attempts direct scaffold mutation instead of `.diff` creation | monitored |
| CW-HC-002 | Candidate realization vs runtime-truth promotion | candidate ledger, learning queue, essence | P1 | realization means represented in KB base only; runtime truth requires governed promotion | if any diff claims `runtime_truth` for a candidate | monitored |
| CW-HC-003 | Source notes as manifest section vs standalone appendix | source manifest | P3 | keep Source Notes register inside this manifest; do not create standalone appendix yet | if source notes outgrow manifest or require independent lifecycle | deferred |

## Conflict report decision

`SOURCE_CONFLICT_REPORT.md` was not created in this pass.

Reason: no material primary-source conflict blocked scaffold drafting. The observed issues are access/duplication/gap risks that are explicitly recorded above and routed through candidate/evidence status.

## Build disposition

- **Coverage:** pass.
- **Role fit:** pass.
- **Duplication:** recorded and bounded.
- **Gap risk:** non-blocking for KB base build.
- **Authority risk:** controlled by candidate-only and evidence-only status rules.
- **Source notes:** represented locally in this manifest; no standalone source-notes appendix created in this pass.
- **Conflict watch:** monitored locally; no material blocking conflict found.
- **Proceed to scaffold drafting:** yes.
