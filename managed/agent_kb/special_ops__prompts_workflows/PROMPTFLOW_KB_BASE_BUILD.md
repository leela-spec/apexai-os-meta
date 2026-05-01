---
promptflow_id: special_ops_prompts_workflows_kb_base_build
target_agent: special_ops__prompts_workflows
target_repo: leela-spec/apexai-os-meta
target_branch: main
target_kb_root: managed/agent_kb/special_ops__prompts_workflows/
source_repo: leela-spec/MasterOfArts
source_branch: main
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: draft
quality: developing
created_at: 2026-05-01
owner: special_ops__prompts_workflows
validator: meta_ops
---

# Promptflow: Special Ops Prompts Workflows KB Base Build

## 1. Target lock

- **Decision:** Build the KB base and appendix KB for exactly one head agent: `special_ops__prompts_workflows`.
- **Target KB root:** `managed/agent_kb/special_ops__prompts_workflows/` in `leela-spec/apexai-os-meta` on `main`.
- **Source root:** `leela-spec/MasterOfArts` on `main`.
- **Primary source index:** `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`.
- **Scaffold:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix target:** `managed/agent_kb/special_ops__prompts_workflows/appendices/`.
- **Role boundary:** reusable prompt and workflow construction, sequencing, handoff, and validation patterns.
- **Non-target:** do not make this agent orchestration authority, KB placement authority, config authority, or QA severity authority.

## 2. Repo-write continuity rule

- **Rule:** This promptflow must live in the target repo on `main` and must be updated before relying on any changed execution logic.
- **Rule:** At the start of every future run, fetch this file and treat it as the active promptflow authority after current user instruction.
- **Rule:** Never leave promptflow improvements only in chat, memory, or scratchpads.
- **Stop:** if direct write to `main` fails, stop with `repo_write_blocked`.
- **Commit prefix:** `special_ops_prompts_workflows_promptflow:` for this file; `special_ops_prompts_workflows_kb:` for generated KB files.

## 3. Architecture lock: thin scaffold, deep appendices

- **Decision:** The five scaffold files are compact navigation, activation, and operating guidance surfaces.
- **Decision:** Deep prompt/workflow evidence, examples, ranked patterns, and source notes live in appendices.
- **Rule:** `ESSENCE.md` is an activation and routing summary, not a long prompt cookbook.
- **Rule:** `BEST_PRACTICES.md` contains compact rules for prompt/workflow design and links to appendix row IDs.
- **Rule:** `MISTAKES.md` captures reusable workflow failure modes, not a full incident archive.
- **Rule:** `TEMPLATES.md` contains reusable prompt/workflow templates and row schemas, not hidden runtime law.
- **Rule:** `LEARNING_QUEUE.md` remains candidate-only and does not become accepted doctrine.
- **Appendix pointer rule:** Every scaffold file must include `Appendix map` or `Source basis` pointers.
- **Density gate:** move bulky examples and evidence into appendices; keep only the distilled rule in scaffold files.

## 4. Source authority and selected slice

### 4.1 Existing indexes first

Use already-created indexes before broad source traversal:

1. `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`
2. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`
3. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md`
4. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md`
5. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md`
6. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md`
7. `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`

### 4.2 Agent-specific source filter

- **Include:** rows and source files targeting `special_ops__prompts_workflows`.
- **Include:** prompt design, workflow research, promptflow, handoff, validation, and process-gate materials.
- **Include as constraints only:** informatics-design material that governs file shape, retrieval clarity, or appendix structure.
- **Include as evidence only:** failure/postmortem material about promptflow drift, blind long-document updating, missing validation, or process docs treated as background.
- **Exclude:** broad meta-ops orchestration doctrine unless it directly constrains prompt/workflow handoff or stage gates.
- **Exclude:** AI model/tool routing unless the source is explicitly about prompt/workflow selection logic.

## 5. Index consistency and plausibility check

Before writing scaffold files, record a bounded plausibility check in `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`.

Required questions:

- **Coverage:** Are top-ranked `special_ops__prompts_workflows` candidates represented?
- **Role fit:** Do selected sources serve reusable prompt/workflow construction rather than broad orchestration?
- **Duplication:** Are duplicate/same-filename variants represented once with duplicate status?
- **Gap risk:** Is a high-value workflow or promptflow source absent from the selected slice?
- **Authority risk:** Is evidence-only material being treated as doctrine?

Required sections in the manifest:

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

Create `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` before drafting scaffold files.

Each row must include:

- `info_id`
- `source_path`
- `source_role`
- `source_section_or_candidate_id`
- `information_unit`
- `agent_relevance`
- `actionability`
- `evidence_strength`
- `reuse_frequency_likelihood`
- `drift_risk`
- `recommended_target_file`
- `appendix_pointer`
- `scaffold_summary_needed`
- `status`

Ranking posture:

- **Prefer:** prompt/workflow-specific, reusable, validated, high-actionability units.
- **Demote:** generic AI advice, one-off incident details, and material owned by other agents.
- **Split:** put examples and detailed evidence in appendices; put only durable rules in scaffold files.

## 8. Generation sequence

1. **Phase 0:** fetch this promptflow, verify write access, patch promptflow first if current instruction changes execution logic.
2. **Phase 1:** validate indexed source slice and write `APPENDIX_KB_SOURCE_MANIFEST.md`.
3. **Phase 2:** write `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`.
4. **Phase 3:** write `APPENDIX_KB_CANDIDATE_LEDGER.md`.
5. **Phase 4:** write `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.
6. **Phase 5:** write `BEST_PRACTICES.md` with `Appendix map`.
7. **Phase 6:** write `MISTAKES.md` with `Appendix map`.
8. **Phase 7:** write `TEMPLATES.md`, including prompt, workflow, handoff, ranking-row, and audit templates.
9. **Phase 8:** write `LEARNING_QUEUE.md`, preserving candidate-only status.
10. **Phase 9:** write `ESSENCE.md` as compression-only activation guidance.
11. **Phase 10:** final QA: verify files, appendix pointers, candidate/evidence status, and no out-of-root writes.

## 9. Quality gates

- **Gate:** Target remains `special_ops__prompts_workflows` only.
- **Gate:** Existing indexes are used first.
- **Gate:** Index plausibility check and ranking ledger precede scaffold drafting.
- **Gate:** Scaffold files remain compact and navigational.
- **Gate:** Deep examples and evidence remain appendices.
- **Gate:** Evidence-only material is not promoted to doctrine without corroboration.
- **Gate:** `LEARNING_QUEUE.md` is candidate-only.
- **Gate:** `ESSENCE.md` adds no new doctrine.
- **Gate:** No shared governance or accepted truth is modified.

## 10. Stop conditions

Stop if:

- the source index cannot be read
- a primary indexed source cannot be fetched
- a material index gap appears
- target identity or role boundary conflicts
- task drifts into other Special Ops agents
- promptflow update is needed but cannot be committed

## 11. Machine-readable execution block

```yaml
accepted_target:
  agent_id: special_ops__prompts_workflows
  target_repo: leela-spec/apexai-os-meta
  target_branch: main
  target_root: managed/agent_kb/special_ops__prompts_workflows/
  source_repo: leela-spec/MasterOfArts
  source_branch: main
  source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

main_outputs:
  - managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
  - managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
  - managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
  - managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
  - managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md

appendix_outputs:
  - managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  - managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
  - managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  - managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  - managed/agent_kb/special_ops__prompts_workflows/appendices/SOURCE_CONFLICT_REPORT.md
```
