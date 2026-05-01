---
promptflow_id: special_ops_ai_handling_routing_kb_base_build
target_agent: special_ops__ai_handling_routing
target_repo: leela-spec/apexai-os-meta
target_branch: main
target_kb_root: managed/agent_kb/special_ops__ai_handling_routing/
source_repo: leela-spec/MasterOfArts
source_branch: main
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: draft
quality: developing
created_at: 2026-05-01
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# Promptflow: Special Ops AI Handling Routing KB Base Build

## 1. Target lock

- **Decision:** Build the KB base and appendix KB for exactly one head agent: `special_ops__ai_handling_routing`.
- **Target KB root:** `managed/agent_kb/special_ops__ai_handling_routing/` in `leela-spec/apexai-os-meta` on `main`.
- **Source root:** `leela-spec/MasterOfArts` on `main`.
- **Primary source index:** `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`.
- **Scaffold:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix target:** `managed/agent_kb/special_ops__ai_handling_routing/appendices/`.
- **Role boundary:** advisory AI-mode, model, tool, handoff, routing, and capability-selection guidance.
- **Non-target:** do not make this agent config authority, model-provider policy authority, all-agent orchestration authority, or QA severity authority.

## 2. Repo-write continuity rule

- **Rule:** This promptflow must live in the target repo on `main` and must be updated before relying on changed execution logic.
- **Rule:** Fetch this file at the start of every future run and treat it as active promptflow authority after current user instruction.
- **Rule:** Never leave promptflow improvements only in chat, memory, or scratchpads.
- **Stop:** if direct write to `main` fails, stop with `repo_write_blocked`.
- **Commit prefix:** `special_ops_ai_handling_routing_promptflow:` for this file; `special_ops_ai_handling_routing_kb:` for generated KB files.

## 3. Architecture lock: thin scaffold, deep appendices

- **Decision:** The five scaffold files are compact navigation, activation, and operating guidance surfaces.
- **Decision:** Deep routing evidence, mode-comparison material, decision matrices, and source notes live in appendices.
- **Rule:** `ESSENCE.md` is a compact routing activation guide, not a full model/tool encyclopedia.
- **Rule:** `BEST_PRACTICES.md` contains durable routing heuristics and appendix pointers, not full research excerpts.
- **Rule:** `MISTAKES.md` captures mode-mismatch and routing failure patterns, not a full postmortem archive.
- **Rule:** `TEMPLATES.md` contains reusable routing cards, decision matrices, and handoff templates, not hidden config law.
- **Rule:** `LEARNING_QUEUE.md` remains candidate-only.
- **Appendix pointer rule:** Every scaffold file must include `Appendix map` or `Source basis` pointers.
- **Density gate:** bulky examples, model comparisons, and evidence go to appendices; scaffold files keep only distilled guidance.

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

- **Include:** rows and source files targeting `special_ops__ai_handling_routing`.
- **Include:** Agent Mode vs thinking mode, Deep Research vs repo execution, Codex handoff, tool/model routing, escalation by capability, and routing baseline material.
- **Include as constraints only:** prompt/workflow material that defines handoff shape; informatics material that defines table/routing-card structure.
- **Include as evidence only:** mode-mismatch failures, blind updater warnings, capability-assumption failures, and routing drift incidents.
- **Exclude:** prompt cookbook content unless it materially affects mode/tool routing.
- **Exclude:** config-file edits or provider-specific operational claims unless explicitly sourced and bounded.

## 5. Index consistency and plausibility check

Before scaffold drafting, record a bounded plausibility check in `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`.

Required questions:

- **Coverage:** Are top-ranked `special_ops__ai_handling_routing` candidates represented?
- **Role fit:** Do selected sources serve mode/tool/model routing rather than prompt drafting or system governance?
- **Duplication:** Are duplicate/same-filename variants represented once with duplicate status?
- **Gap risk:** Is a high-value routing baseline or capability-selection source absent?
- **Authority risk:** Is advisory routing being treated as runtime config authority?

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

- **Prefer:** agent-specific, actionable, evidence-backed routing units.
- **Demote:** generic AI advice, unsourced provider claims, and materials owned by other agents.
- **Split:** place detailed matrices and examples in appendices; scaffold files keep compact routing heuristics.

## 8. Generation sequence

1. **Phase 0:** fetch this promptflow, verify write access, patch promptflow first if needed.
2. **Phase 1:** validate indexed source slice and write `APPENDIX_KB_SOURCE_MANIFEST.md`.
3. **Phase 2:** write `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`.
4. **Phase 3:** write `APPENDIX_KB_CANDIDATE_LEDGER.md`.
5. **Phase 4:** write `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.
6. **Phase 5:** write `BEST_PRACTICES.md` with `Appendix map`.
7. **Phase 6:** write `MISTAKES.md` with `Appendix map`.
8. **Phase 7:** write `TEMPLATES.md`, including routing card, capability matrix, handoff, ranking-row, and audit templates.
9. **Phase 8:** write `LEARNING_QUEUE.md`, preserving candidate-only status.
10. **Phase 9:** write `ESSENCE.md` as compression-only activation guidance.
11. **Phase 10:** final QA: verify files, appendix pointers, candidate/evidence status, and no out-of-root writes.

## 9. Quality gates

- **Gate:** Target remains `special_ops__ai_handling_routing` only.
- **Gate:** Existing indexes are used first.
- **Gate:** Index plausibility check and ranking ledger precede scaffold drafting.
- **Gate:** Scaffold files remain compact and navigational.
- **Gate:** Routing guidance remains advisory unless separately accepted by governance/config authority.
- **Gate:** Deep examples and evidence remain appendices.
- **Gate:** `LEARNING_QUEUE.md` is candidate-only.
- **Gate:** `ESSENCE.md` adds no new doctrine.
- **Gate:** No shared governance, config, or accepted truth is modified.

## 10. Stop conditions

Stop if the source index cannot be read, a primary indexed source cannot be fetched, a material index gap appears, target identity conflicts, the task drifts into other Special Ops agents, or promptflow update is needed but cannot be committed.

## 11. Machine-readable execution block

```yaml
accepted_target:
  agent_id: special_ops__ai_handling_routing
  target_repo: leela-spec/apexai-os-meta
  target_branch: main
  target_root: managed/agent_kb/special_ops__ai_handling_routing/
  source_repo: leela-spec/MasterOfArts
  source_branch: main
  source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

main_outputs:
  - managed/agent_kb/special_ops__ai_handling_routing/BEST_PRACTICES.md
  - managed/agent_kb/special_ops__ai_handling_routing/MISTAKES.md
  - managed/agent_kb/special_ops__ai_handling_routing/TEMPLATES.md
  - managed/agent_kb/special_ops__ai_handling_routing/LEARNING_QUEUE.md
  - managed/agent_kb/special_ops__ai_handling_routing/ESSENCE.md

appendix_outputs:
  - managed/agent_kb/special_ops__ai_handling_routing/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  - managed/agent_kb/special_ops__ai_handling_routing/appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
  - managed/agent_kb/special_ops__ai_handling_routing/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  - managed/agent_kb/special_ops__ai_handling_routing/appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  - managed/agent_kb/special_ops__ai_handling_routing/appendices/SOURCE_CONFLICT_REPORT.md
```
