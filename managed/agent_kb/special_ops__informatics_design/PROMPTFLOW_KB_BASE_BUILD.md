---
promptflow_id: special_ops_informatics_design_kb_base_build
target_agent: special_ops__informatics_design
target_repo: leela-spec/apexai-os-meta
target_branch: main
target_kb_root: managed/agent_kb/special_ops__informatics_design/
source_repo: leela-spec/MasterOfArts
source_branch: main
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: draft
quality: developing
created_at: 2026-05-01
owner: special_ops__informatics_design
validator: special_ops__hygiene_clean
---

# Promptflow: Special Ops Informatics Design KB Base Build

## 1. Target lock

- **Decision:** Build the KB base and appendix KB for exactly one head agent: `special_ops__informatics_design`.
- **Target KB root:** `managed/agent_kb/special_ops__informatics_design/` in `leela-spec/apexai-os-meta` on `main`.
- **Source root:** `leela-spec/MasterOfArts` on `main`.
- **Primary source index:** `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`.
- **Scaffold:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix target:** `managed/agent_kb/special_ops__informatics_design/appendices/`.
- **Role boundary:** information architecture, file typing, taxonomy, retrieval clarity, terminology, chunking, appendix architecture, and machine-readable knowledge design.
- **Non-target:** do not make this agent strategic truth authority, promotion authority, or broad KB content owner.

## 2. Repo-write continuity rule

- **Rule:** This promptflow must live in the target repo on `main` and must be updated before relying on changed execution logic.
- **Rule:** Fetch this file at the start of every future run and treat it as active promptflow authority after current user instruction.
- **Rule:** Never leave promptflow improvements only in chat, memory, or scratchpads.
- **Stop:** if direct write to `main` fails, stop with `repo_write_blocked`.
- **Commit prefix:** `special_ops_informatics_design_promptflow:` for this file; `special_ops_informatics_design_kb:` for generated KB files.

## 3. Architecture lock: thin scaffold, deep appendices

- **Decision:** The five scaffold files are compact navigation, activation, and operating guidance surfaces.
- **Decision:** Deep information-design evidence, taxonomy variants, terminology tables, audit matrices, and source notes live in appendices.
- **Rule:** `ESSENCE.md` is a compact activation guide for information design judgment, not the full canon.
- **Rule:** `BEST_PRACTICES.md` contains durable information-design rules with appendix row pointers.
- **Rule:** `MISTAKES.md` captures recurring structure, chunking, terminology, and retrieval failures.
- **Rule:** `TEMPLATES.md` contains reusable file, taxonomy, terminology, audit, and ranking templates.
- **Rule:** `LEARNING_QUEUE.md` remains candidate-only.
- **Appendix pointer rule:** Every scaffold file must include `Appendix map` or `Source basis` pointers.
- **Density gate:** bulky tables, source comparisons, and research detail go to appendices; scaffold files keep distilled rules.

## 4. Source authority and selected slice

### 4.1 Existing indexes first

Use already-created indexes before broad traversal:

1. `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`
2. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`
3. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md`
4. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md`
5. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md`
6. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md`
7. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`

### 4.2 Agent-specific source filter

- **Include:** rows and source files targeting `special_ops__informatics_design`.
- **Include:** information-design canon, file taxonomy, terminology, audit checklist, implementation maps, open questions, chunking/retrieval rules, and source-index architecture.
- **Include as constraints only:** prompts/workflows sources that define promptflow staging for information-design artifact creation.
- **Include as evidence only:** failure/postmortem material about mixed-purpose blobs, overlong files, missing structure gates, and terminology drift.
- **Exclude:** broad strategy, model routing, or hygiene severity material unless needed to validate information-design rules.

## 5. Index consistency and plausibility check

Before scaffold drafting, record a bounded plausibility check in `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`.

Required questions:

- **Coverage:** Are top-ranked `special_ops__informatics_design` candidates represented?
- **Role fit:** Do selected sources serve structure, taxonomy, retrieval clarity, and machine-readable knowledge design?
- **Duplication:** Are GPT/Gemini/Perplexity variants represented as variants rather than blindly duplicated?
- **Gap risk:** Is a high-value canon, taxonomy, terminology, audit, or open-question file absent?
- **Authority risk:** Are provisional design questions being hardened into final doctrine?

Required manifest sections:

1. `Source universe decision`
2. `Indexed source table`
3. `Cross-index plausibility check`
4. `Included high-value sources`
5. `Excluded or deferred sources`
6. `Index gap register`
7. `Unresolved blockers`

- **Stop:** material unresolved index gaps block scaffold drafting.

## 6. Output contract

### 6.1 Main files

Create or update exactly:

1. `BEST_PRACTICES.md`
2. `MISTAKES.md`
3. `TEMPLATES.md`
4. `LEARNING_QUEUE.md`
5. `ESSENCE.md`

### 6.2 Appendix files

Create or update:

1. `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`
2. `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
3. `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
4. `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
5. `appendices/SOURCE_CONFLICT_REPORT.md` only if needed

## 7. Information ranking model

Create `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` before scaffold files.

Each row must include: `info_id`, `source_path`, `source_role`, `source_section_or_candidate_id`, `information_unit`, `agent_relevance`, `actionability`, `evidence_strength`, `reuse_frequency_likelihood`, `drift_risk`, `recommended_target_file`, `appendix_pointer`, `scaffold_summary_needed`, `status`.

Ranking posture:

- **Prefer:** structure-specific, retrieval-specific, taxonomy-specific, terminology-specific, high-evidence rules.
- **Demote:** generic writing advice, style preferences, and provisional ideas without evidence.
- **Split:** keep full tables, variants, and evidence in appendices; scaffold files hold the stable distilled design rules.

## 8. Generation sequence

1. **Phase 0:** fetch this promptflow, verify write access, patch promptflow first if needed.
2. **Phase 1:** validate indexed source slice and write `APPENDIX_KB_SOURCE_MANIFEST.md`.
3. **Phase 2:** write `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`.
4. **Phase 3:** write `APPENDIX_KB_CANDIDATE_LEDGER.md`.
5. **Phase 4:** write `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.
6. **Phase 5:** write `BEST_PRACTICES.md` with `Appendix map`.
7. **Phase 6:** write `MISTAKES.md` with `Appendix map`.
8. **Phase 7:** write `TEMPLATES.md`, including file-taxonomy, terminology, audit, source-manifest, ranking-row, and appendix templates.
9. **Phase 8:** write `LEARNING_QUEUE.md`, preserving candidate-only status.
10. **Phase 9:** write `ESSENCE.md` as compression-only activation guidance.
11. **Phase 10:** final QA: verify files, appendix pointers, candidate/evidence status, and no out-of-root writes.

## 9. Quality gates

- **Gate:** Target remains `special_ops__informatics_design` only.
- **Gate:** Existing indexes are used first.
- **Gate:** Index plausibility check and ranking ledger precede scaffold drafting.
- **Gate:** Scaffold files remain compact and navigational.
- **Gate:** Provisional open questions remain visibly provisional.
- **Gate:** Deep tables and source comparisons remain appendices.
- **Gate:** `LEARNING_QUEUE.md` is candidate-only.
- **Gate:** `ESSENCE.md` adds no new doctrine.
- **Gate:** No shared governance, promotion authority, or accepted truth is modified.

## 10. Stop conditions

Stop if the source index cannot be read, a primary indexed source cannot be fetched, a material index gap appears, target identity conflicts, the task drifts into other Special Ops agents, or promptflow update is needed but cannot be committed.

## 11. Machine-readable execution block

```yaml
accepted_target:
  agent_id: special_ops__informatics_design
  target_repo: leela-spec/apexai-os-meta
  target_branch: main
  target_root: managed/agent_kb/special_ops__informatics_design/
  source_repo: leela-spec/MasterOfArts
  source_branch: main
  source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

main_outputs:
  - managed/agent_kb/special_ops__informatics_design/BEST_PRACTICES.md
  - managed/agent_kb/special_ops__informatics_design/MISTAKES.md
  - managed/agent_kb/special_ops__informatics_design/TEMPLATES.md
  - managed/agent_kb/special_ops__informatics_design/LEARNING_QUEUE.md
  - managed/agent_kb/special_ops__informatics_design/ESSENCE.md

appendix_outputs:
  - managed/agent_kb/special_ops__informatics_design/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  - managed/agent_kb/special_ops__informatics_design/appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
  - managed/agent_kb/special_ops__informatics_design/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  - managed/agent_kb/special_ops__informatics_design/appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  - managed/agent_kb/special_ops__informatics_design/appendices/SOURCE_CONFLICT_REPORT.md
```
