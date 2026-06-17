---
promptflow_id: special_ops_knowledge_bank_kb_base_build
target_agent: special_ops__knowledge_bank
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_branch: main
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: draft
quality: developing
created_at: 2026-05-01
owner: special_ops__knowledge_bank
validator: special_ops__informatics_design
---

# Promptflow: Special Ops Knowledge Bank KB Base Build

## 1. Hard repo boundary

- **Decision:** Execute entirely inside `leela-spec/MasterOfArts`.
- **Decision:** Read sources from `leela-spec/MasterOfArts` and write outputs only into `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/` in the same repo.
- **Forbidden:** do not read from, write to, patch, or treat `leela-spec/apexai-os-meta` as a target or runtime surface for this promptflow.
- **Stop:** if execution context points at Apex, stop with `wrong_repo_context` before writing anything.

## 2. Target lock

- **Agent:** `special_ops__knowledge_bank`.
- **Role boundary:** KB placement, lifecycle, source manifesting, candidate routing, appendix architecture, learning capture, and anti-sprawl safeguards.
- **Scaffold:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/`.
- **Non-target:** other Special Ops KBs, shared governance, accepted-truth promotion, or Apex migration.

## 3. Source authority

Use existing indexes first:

1. `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`
2. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`
3. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md`
4. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md`
5. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md`
6. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md`
7. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`

- **Include:** source-index section for `special_ops__knowledge_bank` plus rows in ledgers targeting that agent.
- **Include as constraints:** information-design and promptflow sources only when they directly govern KB structure or validation.
- **Include as evidence only:** failure/postmortem material.
- **Exclude:** broad repo traversal unless a bounded index-gap check proves a high-value source is missing.

## 4. Architecture lock: thin scaffold, deep appendices

- **Decision:** Scaffold files are compact activation, navigation, and operating guidance surfaces.
- **Decision:** Appendices hold the deep body of knowledge.
- **Rule:** `ESSENCE.md` is compression-only and points into appendices.
- **Rule:** `BEST_PRACTICES.md` contains compact doctrine with appendix pointers.
- **Rule:** `MISTAKES.md` contains reusable failure patterns, not a full archive.
- **Rule:** `TEMPLATES.md` contains reusable forms, not hidden promptflow law.
- **Rule:** `LEARNING_QUEUE.md` is candidate-only.
- **Density gate:** if detailed source content enters a scaffold file, move it to an appendix and replace it with a rule or pointer.

## 5. Required appendices

Create/update before scaffold drafting:

1. `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`
2. `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
3. `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
4. `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
5. `appendices/SOURCE_CONFLICT_REPORT.md` only if needed

## 6. Index consistency and plausibility check

Record in `APPENDIX_KB_SOURCE_MANIFEST.md`:

- **Coverage:** top-ranked `special_ops__knowledge_bank` candidates are represented.
- **Role fit:** sources map to KB lifecycle and appendix architecture.
- **Exclusion fit:** non-target sources are excluded unless structurally necessary.
- **Duplication:** duplicates and same-filename variants are recorded once with status.
- **Gap risk:** high-value missing sources are listed in an index gap register.
- **Authority risk:** evidence-only material is not treated as doctrine.

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
- **Gate:** Deep details stay in appendices.
- **Gate:** Candidate and evidence statuses stay explicit.
- **Gate:** No shared governance or accepted truth is changed.

## 10. Machine-readable execution block

```yaml
accepted_target:
  agent_id: special_ops__knowledge_bank
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  source_repo: leela-spec/MasterOfArts
  branch: main
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
  source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
forbidden_repos:
  - leela-spec/apexai-os-meta
main_outputs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md
```
