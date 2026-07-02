---
promptflow_id: special_ops_hygiene_clean_kb_base_build
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_branch: main
target_agent: special_ops__hygiene_clean
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: draft
quality: developing
created_at: 2026-05-01
owner: special_ops__hygiene_clean
validator: meta_detective
---

# Promptflow: Special Ops Hygiene Clean KB Base Build

## 1. Hard repo boundary

- **Decision:** Execute entirely inside `leela-spec/MasterOfArts`.
- **Decision:** Read sources from `leela-spec/MasterOfArts` and write outputs only into `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/` in the same repo.
- **Forbidden:** do not read from, write to, patch, or treat `leela-spec/apexai-os-meta` as a target or runtime surface for this promptflow.
- **Stop:** if execution context points at Apex, stop with `wrong_repo_context` before writing anything.

## 2. Target lock

- **Agent:** `special_ops__hygiene_clean`.
- **Role boundary:** structural QA, hygiene, audit, drift detection, cleanup discipline, validation, and closure logic.
- **Scaffold:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/`.
- **Non-target:** promotion authority, strategy authority, broad content ownership, or accepted-truth mutation.

## 3. Source authority

Use existing indexes first:

1. `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`
2. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`
3. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md`
4. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md`
5. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md`
6. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md`
7. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`

- **Include:** source-index section for `special_ops__hygiene_clean` plus ledger rows targeting that agent.
- **Include:** audit checklists, validation/authority rules, failure ledgers, anti-drift evidence, cleanup rules, source-integrity checks, drift salvage, validation reports, hierarchy guidance.
- **Include as constraints:** informatics-design material only when it defines auditability, chunk integrity, file typing, or retrieval hygiene.
- **Include as evidence only:** context-loss, move/edit, drift, validation bypass, long-document overwrite, and source ambiguity postmortems.
- **Exclude:** strategy recommendations, prompt cookbook content, and KB placement doctrine unless needed for hygiene review.

## 4. Architecture lock: thin scaffold, deep appendices

- **Decision:** Scaffold files are compact activation, navigation, and operating guidance surfaces.
- **Decision:** Appendices hold deep audit matrices, finding classes, evidence examples, closure notes, risk ledgers, and source notes.
- **Rule:** `ESSENCE.md` is compression-only and points into appendices.
- **Rule:** `BEST_PRACTICES.md` contains compact hygiene rules with appendix pointers.
- **Rule:** `MISTAKES.md` contains reusable failure patterns and recovery playbooks.
- **Rule:** `TEMPLATES.md` contains finding, audit, closure, source-manifest, ranking-row, and evidence-note templates.
- **Rule:** `LEARNING_QUEUE.md` is candidate-only.
- **Density gate:** if detailed evidence enters a scaffold file, move it to an appendix and replace it with a rule or pointer.

## 5. Required appendices

Create/update before scaffold drafting:

1. `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`
2. `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
3. `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
4. `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
5. `appendices/SOURCE_CONFLICT_REPORT.md` only if needed

## 6. Index consistency and plausibility check

Record in `APPENDIX_KB_SOURCE_MANIFEST.md`:

- **Coverage:** top-ranked `special_ops__hygiene_clean` candidates are represented.
- **Role fit:** sources serve structural QA/hygiene rather than strategy or promotion authority.
- **Duplication:** duplicates and same-filename variants are recorded once with status.
- **Gap risk:** missing high-value audit/checklist/failure sources are listed.
- **Authority risk:** hygiene findings are not treated as accepted truth or promotion authority.

Stop before scaffold drafting if a material gap remains unresolved.

## 7. Information ranking model

Create `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` with rows containing:

`info_id`, `source_path`, `source_role`, `source_section_or_candidate_id`, `information_unit`, `agent_relevance`, `actionability`, `evidence_strength`, `reuse_frequency_likelihood`, `drift_risk`, `recommended_target_file`, `appendix_pointer`, `scaffold_summary_needed`, `status`.

## 8. Generation sequence

1. Verify repo context is `leela-spec/MasterOfArts`.
2. Fetch this promptflow from MasterOfArts `main`.
3. Validate indexed source slice and write source manifest.
4. Write information ranking ledger.
5. Write candidate ledger.
6. Write anti-drift appendix.
7. Write `BEST_PRACTICES.md`.
8. Write `MISTAKES.md`.
9. Write `TEMPLATES.md`.
10. Write `LEARNING_QUEUE.md`.
11. Write `ESSENCE.md` last.
12. Fetch back every written file and verify no Apex path or repo reference is active.

## 9. Quality gates

- **Gate:** MasterOfArts is the only working repo.
- **Gate:** Existing indexes are used first.
- **Gate:** Index plausibility and ranking ledger precede scaffold drafting.
- **Gate:** Scaffold files stay compact and navigational.
- **Gate:** Hygiene findings remain findings unless promotion path accepts truth changes.
- **Gate:** Candidate and evidence statuses stay explicit.
- **Gate:** No shared governance, promotion authority, or accepted truth is changed.

## 10. Machine-readable execution block

```yaml
accepted_target:
  agent_id: special_ops__hygiene_clean
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  source_repo: leela-spec/MasterOfArts
  branch: main
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
  source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
forbidden_repos:
  - leela-spec/apexai-os-meta
```
