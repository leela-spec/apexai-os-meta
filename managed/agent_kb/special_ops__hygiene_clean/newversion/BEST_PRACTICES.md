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

| Gap | Severity | Disposition |
|---|---|---|
| One source-inventory access blocker exists for an external/local `UpdateProcessSSOTS` directory | P2 | not blocking for this build because the promptflow source slice has repo-accessible sources and ledgers sufficient for KB base extraction |
| Several ledger source paths preserve older local corpus labels | P3 | handled by mapping to repo-accessible source-index paths or treating as ledger evidence only |
| Some high-value informatics-design raw sources are represented through ledgers rather than fetched as standalone raw files | P2 | acceptable for this KB base because the target agent needs compact hygiene doctrine plus appendices, not full informatics canon extraction |

## Authority risk

| Risk | Control |
|---|---|
| Treating a hygiene finding as accepted truth | keep findings in candidate/evidence status unless promotion accepts them |
| Treating a source summary as primary when raw source exists | use source index and direct files first; mark ledger summaries as derived when appropriate |
| Turning cleanup into design authority | restrict scaffold rules to QA, validation, drift detection, and closure mechanics |
| Collapsing evidence and rule | store postmortems in anti-drift appendix and summarize only reusable safeguards in scaffold files |
| Silent closure of P0/P1 findings | require explicit finding records and closure evidence |

## Conflict report decision

`SOURCE_CONFLICT_REPORT.md` was not created in this pass.

Reason: no material primary-source conflict blocked scaffold drafting. The observed issues are access/duplication/gap risks that are explicitly recorded above and routed through candidate/evidence status.

## Build disposition

- **Coverage:** pass.
- **Role fit:** pass.
- **Duplication:** recorded and bounded.
- **Gap risk:** non-blocking for KB base build.
- **Authority risk:** controlled by candidate-only and evidence-only status rules.
- **Proceed to scaffold drafting:** yes.
