# APPENDIX_KB_INFORMATION_RANKING_LEDGER

## Purpose

- **Purpose:** Rank reusable information-design units for the `special_ops__informatics_design` KB base.
- **Boundary:** This is a KB-base ranking ledger, not a promotion decision or accepted-truth mutation.
- **Input basis:** Existing source index and resource screening ledgers, then repo-accessible informatics-design equivalents.

## Ranking rows

| info_id | source_path | source_role | source_section_or_candidate_id | information_unit | agent_relevance | actionability | evidence_strength | reuse_frequency_likelihood | drift_risk | recommended_target_file | appendix_pointer | scaffold_summary_needed | status |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| ID-001 | `AIHowTo/BasicFiles4Agents/InformationsDesign/INFORMATION_DESIGN_80_20_ESSENCE.md` | primary | Core rule | Information should be small, self-contained, explicitly labeled, function-typed, and understandable in isolation. | high | high | high | high | low | `ESSENCE.md`, `BEST_PRACTICES.md` | source manifest | yes | accepted-for-KB-base |
| ID-002 | `AIHowTo/BasicFiles4Agents/InformationsDesign/INFORMATION_DESIGN_80_20_ESSENCE.md` | primary | 10 highest-value rules | One chunk / one job; explicit labels; stable terminology; stable structure; function typing; boundary preservation; visible purpose; anti-sprawl; explicit unresolvedness. | high | high | high | high | low | `BEST_PRACTICES.md` | anti-drift appendix | yes | accepted-for-KB-base |
| ID-003 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FinalInformaticsDesign/INFORMATION_DESIGN_OPEN_QUESTIONS.md` | primary equivalent | KB-INFORMATICS-DESIGN-017 | Sentence strictness, schema-first structure, prompt-template placement, file-type declaration strength, and redundancy remain provisional. | high | high | high | medium | high if hardened | `LEARNING_QUEUE.md`, `ESSENCE.md` | candidate ledger | yes | provisional-boundary |
| ID-004 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/AUDIT_CHECKLIST_GPT.md` | primary equivalent | KB-INFORMATICS-DESIGN-045 | Universal audit checks: chunk self-containment, semantic labeling, terminology consistency, structural boundaries, mixed-purpose drift, evidence/decision clarity. | high | high | high | high | low | `BEST_PRACTICES.md`, `TEMPLATES.md` | anti-drift appendix | yes | accepted-for-KB-base |
| ID-005 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/FILE_TAXONOMY_GPT.md` | primary equivalent | KB-INFORMATICS-DESIGN-048 | File type is determined by function, not author, directory, or tool. Mixed-purpose content must remain bounded and labeled. | high | high | high | high | medium | `BEST_PRACTICES.md`, `TEMPLATES.md` | candidate ledger | yes | accepted-for-KB-base |
| ID-006 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/INFORMATION_DESIGN_CANON_GPT.md` | primary equivalent | KB-INFORMATICS-DESIGN-050 | Optimization order: retrieval/context efficiency, ambiguity reduction, handoff reliability, maintainability, then aesthetics. | high | high | high | high | low | `ESSENCE.md`, `BEST_PRACTICES.md` | source manifest | yes | accepted-for-KB-base |
| ID-007 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfGPT/TERMINOLOGY_GPT.md` | primary equivalent | KB-INFORMATICS-DESIGN-054 | Stable core vocabulary: chunk, semantic label, terminology consistency, typed information, file taxonomy, index-detail layering, provisional rule, mixed-purpose file. | high | high | high | high | medium | `TEMPLATES.md`, `BEST_PRACTICES.md` | candidate ledger | yes | accepted-for-KB-base |
| ID-008 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfPerp/FILE_TAXONOMY_Perp.md` | variant equivalent | KB-INFORMATICS-DESIGN-063 | Taxonomy variant confirms file-type table and function-based file classes. | medium | medium | medium-high | medium | low | appendices only | source manifest | no | represented-as-variant |
| ID-009 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfPerp/INFORMATION_DESIGN_CANON_Perp.md` | variant equivalent | KB-INFORMATICS-DESIGN-065 / 067 | Strong guidance confirms short focused files, tables/checklists for structured content, and retrieval-first optimization. | medium | medium | medium-high | medium | low | appendices only | source manifest | no | represented-as-variant |
| ID-010 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FirstInfWorkingDesignFiles/FilesOfPerp/TERMINOLOGY_Perp.md` | variant equivalent | KB-INFORMATICS-DESIGN-068 / 070 | Terminology change rule and stable vocabulary purpose confirm synonym-drift prevention. | medium | high | medium-high | medium | medium | `TEMPLATES.md` | candidate ledger | yes | accepted-for-KB-base |
| ID-011 | `OpenClaw/02_research-kb/best-practices/operational-framework/InformaticsDesign/FinalInformaticsDesign/ExecutionHandover_NoDrift.md` | evidence | KB-INFORMATICS-DESIGN-009 / 010 | Evidence-layer runs must not drift into governance finalization; keep target deliverables bounded. | high | high | high | medium | high if ignored | `MISTAKES.md`, `LEARNING_QUEUE.md` | anti-drift appendix | yes | accepted-for-KB-base |
| ID-012 | `OpenClaw/02_research-kb/best-practices/operational-framework/UpdateProcessSSOTS/Failure_Postmortem_Reorg_And_Move_Edit_Violation_v1.md` | evidence | KB-CODEX-EXECUTION-PROCESS-071 / 072 | Referenced process rules must act as blocking gates, not background context. | medium | high | high | medium | high if ignored | `MISTAKES.md` | anti-drift appendix | yes | accepted-for-KB-base |
| ID-013 | `AIHowTo/BasicFiles4Agents/SingleAiGuide_research&Guides/LIMITED_AGENT_STYLE_GUIDE.md` | supporting style | Non-negotiable style rules | Use typed bullets, make dependencies explicit, avoid prose blobs, avoid mixed-role bullets, and do not treat draft reasoning as accepted truth. | high | high | high | high | low | `TEMPLATES.md`, `BEST_PRACTICES.md` | source manifest | yes | accepted-for-KB-base |
| ID-014 | `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md` | primary ledger | Agent_special_ops__informatics_design.md | Agent owns structural standards, functional labels, terminology stability, retrieval clarity, and cold-start usability; it does not own content validation or strategic direction. | high | high | high | high | low | `ESSENCE.md` | source manifest | yes | accepted-for-KB-base |

## Ranking interpretation

- **Use in scaffold:** ID-001, ID-002, ID-004, ID-005, ID-006, ID-007, ID-010, ID-011, ID-012, ID-013, ID-014.
- **Keep provisional:** ID-003 and unresolved variants from open-questions sources.
- **Keep in appendix only:** variant rows that confirm but do not materially alter the compact scaffold.

## Density gate

- **Decision:** This ledger intentionally stays in the appendix.
- **Constraint:** Scaffold files may summarize rankings but must not duplicate this table.
