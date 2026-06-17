# APPENDIX_KB_SOURCE_MANIFEST

## Purpose

- **Purpose:** Record the bounded source slice used to build the `special_ops__informatics_design` KB base.
- **Scope:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/`.
- **Status:** source manifest for scaffold and appendix generation.
- **Boundary:** This manifest records source evidence and plausibility checks. It does not promote shared governance truth or mutate accepted system doctrine.

## Indexed source slice

| source_role | source_path | read_mode | used_for | status |
|---|---|---:|---|---|
| promptflow | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/PROMPTFLOW_KB_BASE_BUILD.md` | full | target lock, generation sequence, quality gates | used |
| source index | `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` | full | source slice, repo-accessible equivalents, manual-source boundary | used |
| primary | `AIHowTo/BasicFiles4Agents/InformationsDesign/INFORMATION_DESIGN_80_20_ESSENCE.md` | full | compact operating contract for information design | used |
| supporting | `AIHowTo/BasicFiles4Agents/InformationsDesign/INFORMATION_DESIGN_80_20_AGGREGATE_SNIPPET.md` | full | summary language for scaffold compression | used |
| primary ledger | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md` | full / targeted slice | top-ranked informatics-design candidates | used |
| primary ledger | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md` | full / targeted slice | duplicate status, source lane, target-agent mapping | used |
| primary ledger | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md` | full / targeted slice | idea units, candidate IDs, evidence notes, confidence | used |
| primary ledger | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md` | full | role boundary, owns / does-not-own, metrics, safeguards | used |
| supporting ledger | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md` | full | compact candidate summaries and validation pairings | used |
| supporting ledger | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | targeted | failure patterns and anti-drift controls | represented through candidate/evidence rows |
| primary equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FinalInformaticsDesign/INFORMATION_DESIGN_OPEN_QUESTIONS.md` | full | provisional boundary and unresolved-question handling | used |
| primary equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/AUDIT_CHECKLIST_GPT.md` | full | universal audit checks, pass/revise/fail guidance | used |
| primary equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/FILE_TAXONOMY_GPT.md` | full | file-type table, mixed-purpose file warning | used |
| primary equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/INFORMATION_DESIGN_CANON_GPT.md` | full | optimization priorities, hard/strong/provisional rule split | used |
| primary equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/TERMINOLOGY_GPT.md` | full | core vocabulary, synonym-drift controls, provisional terms | used |
| variant equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGemini/AUDIT_CHECKLIST_Gem.md` | ranked extract | audit-check variant comparison | represented |
| variant equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfPerp/FILE_TAXONOMY_Perp.md` | ranked extract | taxonomy variant comparison | represented |
| variant equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfPerp/INFORMATION_DESIGN_CANON_Perp.md` | ranked extract | strong-guidance variant comparison | represented |
| variant equivalent | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfPerp/TERMINOLOGY_Perp.md` | ranked extract | terminology change-rule variant | represented |
| constraint | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/Promptflow.md` | ranked extract | terminology/audit promptflow staging only | represented as constraint |
| evidence | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FinalInformaticsDesign/ExecutionHandover_NoDrift.md` | ranked extract | evidence-layer boundary and no-governance-finalization warning | represented |
| supporting style | `AIHowTo/BasicFiles4Agents/SingleAiGuide_research&Guides/LIMITED_AGENT_STYLE_GUIDE.md` | full | compact markdown style, typed bullets, metadata, relation discipline | used |
| appendix TODO | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/appendices/2Dos` | full | functional status, missing database candidates, research backlog, next-research appendix recommendation | resolved into QA/research appendix and deferred candidate records |

## Plausibility check

| check | result | notes |
|---|---|---|
| Coverage | pass | Top-ranked `KB-INFORMATICS-DESIGN-*` units are represented: open questions, audit checks, file taxonomy, optimization priorities, terminology, file-type variants, no-drift execution boundaries, and corrected reliability-audit gates. |
| Role fit | pass | Sources serve structure, taxonomy, retrieval clarity, terminology, chunking, appendix design, and machine-readable knowledge design. |
| Duplication | pass | GPT/Gemini/Perplexity material is treated as variant evidence. The scaffold does not blindly duplicate every variant. |
| Gap risk | low-medium | High-value canon, taxonomy, terminology, audit, open-question, source-index, folder-index, target-file-matrix, and reliability-audit classes are represented. Optional source-notes and sidecars remain deferred. |
| Authority risk | controlled | Open questions and provisional design matters remain visibly provisional. Scaffold files do not claim promotion authority or shared governance mutation. |
| Density gate | pass | Detailed ranking rows, source comparisons, candidate tables, anti-drift evidence, and next research planning live in appendices, not in scaffold files. |

## Non-blocking manual sources

- **Status:** The source index lists a small number of outside-repo manual files.
- **Decision:** They are not material blockers for this KB base because the top-ranked informatics-design source classes and repo-accessible equivalents are available in `leela-spec/MasterOfArts`.
- **Constraint:** Do not treat un-read manual files as evidence for accepted rules.

## Source conflict report decision

- **Decision:** `SOURCE_CONFLICT_REPORT.md` was not created in this run.
- **Reason:** No material source conflict blocks scaffold drafting. The main tension is already captured as provisional design questions: sentence-level strictness, schema-first structure, prompt-template placement, file-type declaration strength, healthy redundancy, source-note database need, and sidecar schema need.
- **Next condition:** Create `SOURCE_CONFLICT_REPORT.md` only if later evidence directly contradicts the current core rule set rather than merely qualifying it.
