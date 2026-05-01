---
promptflow_id: special_ops_knowledge_bank_kb_base_build
target_agent: special_ops__knowledge_bank
target_repo: leela-spec/apexai-os-meta
target_branch: main
target_kb_root: managed/agent_kb/special_ops__knowledge_bank/
source_repo: leela-spec/MasterOfArts
source_branch: main
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: draft
quality: developing
created_at: 2026-05-01
updated_at: 2026-05-01
owner: special_ops__knowledge_bank
validator: special_ops__informatics_design
---

# Promptflow: Special Ops Knowledge Bank KB Base Build

## 1. Target lock

- **Decision:** Build the KB base and appendix KB for exactly one head agent: `special_ops__knowledge_bank`.
- **Target KB root:** `managed/agent_kb/special_ops__knowledge_bank/` in `leela-spec/apexai-os-meta` on `main`.
- **Source root:** `leela-spec/MasterOfArts` on `main`.
- **Primary source index:** `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`.
- **Scaffold authority:** use the Apex five-file agent-KB scaffold: `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix target:** create the deep body of knowledge under `managed/agent_kb/special_ops__knowledge_bank/appendices/`.
- **Non-target:** do not build KBs for the other Special Ops agents in this run.

## 2. Repo-write continuity rule

- **Rule:** This promptflow must live in the target repo on `main` and must be updated there whenever execution logic changes.
- **Rule:** At the start of every future run, fetch this file from `managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_BASE_BUILD.md` and treat it as the active promptflow authority after current user instruction.
- **Rule:** If a better constraint, source decision, validation rule, or stage boundary is discovered during execution, patch this promptflow first and commit the update to `main` before relying on that new logic.
- **Rule:** Never leave promptflow improvements only in chat, memory, or an external scratchpad.
- **Rule:** If direct repo write to `main` fails, stop with `repo_write_blocked` and do not continue manufacturing KB files from unpersisted instructions.
- **Commit prefix:** use `special_ops_kb_promptflow:` for promptflow changes and `special_ops_kb:` for generated KB files.

## 3. Authority order

1. Current explicit user instruction.
2. This promptflow file in the Apex repo.
3. `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` in MasterOfArts.
4. Repo files in the selected `special_ops__knowledge_bank` source slice marked `primary`.
5. Repo files in the selected source slice marked `supporting`.
6. Evidence-only failure or anti-drift material.
7. Generated KB files after they are written and verified.

- **Conflict rule:** Do not silently reconcile load-bearing source conflicts. Create `appendices/SOURCE_CONFLICT_REPORT.md` and stop the affected stage.
- **Promotion rule:** Generated KB files are draft/candidate KB surfaces unless a separate promotion process accepts them.

## 4. Architecture lock: thin scaffold, deep appendices

- **Decision:** The five scaffold files are navigation, activation, and operating guidance surfaces. They must not become bulk knowledge dumps.
- **Decision:** The appendices are the deep reference layer. They hold source manifests, information rankings, candidate ledgers, evidence notes, and conflict reports.
- **Rule:** `ESSENCE.md` is the smallest activation surface and must point to appendix IDs for deeper context instead of restating the body of knowledge.
- **Rule:** `BEST_PRACTICES.md` contains governing operating patterns and compact source-basis pointers, not full source excerpts.
- **Rule:** `MISTAKES.md` captures reusable failure patterns and recovery guidance, not a full incident archive.
- **Rule:** `TEMPLATES.md` contains reusable forms and row schemas, not hidden promptflow law.
- **Rule:** `LEARNING_QUEUE.md` remains candidate-only and must never behave as accepted truth.
- **Appendix pointer rule:** Every scaffold file must include a short `Appendix map` or `Source basis` section that points to the relevant appendix row IDs.
- **Density gate:** If a scaffold file starts absorbing detailed source content, move that material into an appendix and replace it with a short decision, rule, or pointer.

## 5. Selected source index

### 5.1 Binding source-map file

| Path | Role | Read mode | Use |
|---|---:|---:|---|
| `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` | source index | read full | binding source map and cluster boundary |

### 5.2 Core `special_ops__knowledge_bank` sources

| Path | Role | Read mode | Reason for inclusion |
|---|---:|---:|---|
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md` | primary | read full | agent-ranked candidate selection for the Knowledge Bank lane |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md` | primary | read full | corpus inventory, duplicate status, target agents, triage decisions |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/MASTER_IDEA_LEDGER.md` | primary | read full | normalized source-to-KB idea ledger and scoring fields |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md` | primary | read full | role ownership, non-ownership, metrics, safeguards, KB lane mapping |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md` | supporting | read full | compact doctrine candidate pool |
| `OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md` | supporting/evidence | read full | anti-drift evidence, failure safeguards, non-generalization warnings |
| `AIHowTo/Codex/Improvement_Capture_Rule.md` | supporting | read full | rules for persistent improvement capture and validation |
| `AIHowTo/Codex/CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | read full | continuity and preservation guidance relevant to KB migration |

### 5.3 Cross-lane constraint sources

Use these only to constrain structure, prompt discipline, and validation. They must not become content authority for the Knowledge Bank agent unless the core source slice supports the same claim.

| Path | Role | Read mode | Use limit |
|---|---:|---:|---|
| `AIHowTo/BasicFiles4Agents/InformationsDesign/INFORMATION_DESIGN_80_20_ESSENCE.md` | structural constraint | read full | chunking, labels, retrieval clarity, anti-sprawl |
| `AIHowTo/BasicFiles4Agents/PromptDesign/PROMPT_DESIGN_80_20_BEST_PRACTICE.md` | prompt-flow constraint | skim or read relevant | prompt shape, authority declaration, stop conditions |
| `AIHowTo/BasicFiles4Agents/WorkflowResearch/WORKFLOW_80_20_ESSENCE.md` | workflow constraint | skim or read relevant | staged execution, one-artifact discipline, continuation hygiene |
| `AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | validation constraint | read relevant | source authority, verification, escalation handling |
| `managed/agent_kb/AGENT_KB_INDEX.md` in Apex | target scaffold | read full | target KB root and five-file convention |
| `managed/agents/special_ops__knowledge_bank.md` in Apex | activation seed | read full | compact current seed and role boundary |
| `managed/knowledge/AGENT_KB_LANES.md` in Apex | shared governance | read relevant | shared KB lane rules only when needed |

### 5.4 Explicit exclusions

- **Exclude:** full Special Ops KB factory output for all agents.
- **Exclude:** other Special Ops source clusters as primary content.
- **Exclude:** broad repo traversal beyond the selected index when the selected sources answer the task.
- **Exclude:** web research.
- **Exclude:** manually attached outside-repo files unless current user instruction names them for this run.
- **Exclude:** any accepted-truth mutation or governance-file rewrite outside `managed/agent_kb/special_ops__knowledge_bank/` unless separately authorized.

## 6. Index consistency and plausibility check

Before manufacturing KB content, perform a bounded check of whether the already-created indexes appear sufficient.

### 6.1 Required index cross-checks

Compare the selected source universe across:

1. `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`
2. `KB_RANKINGS_BY_AGENT.md`
3. `SOURCE_INVENTORY_LEDGER.md`
4. `MASTER_IDEA_LEDGER.md`
5. `ROLE_AND_KB_TARGET_MAP.md`
6. `ESSENCE_CANDIDATES.md`
7. `FAILURE_AND_ANTI_DRIFT_LEDGER.md`

### 6.2 Plausibility questions

- **Coverage:** Are the top-ranked `special_ops__knowledge_bank` candidates represented in the source slice?
- **Role fit:** Do selected sources map to the Knowledge Bank agent’s real remit: KB architecture, candidate lifecycle, placement, source manifests, appendices, learning capture, and anti-sprawl?
- **Exclusion fit:** Are non-target Special Ops sources excluded unless they constrain KB construction?
- **Duplication:** Are exact duplicates and same-filename variants represented once, with duplicate status recorded?
- **Missing-value risk:** Does any high-value source from the rankings or idea ledger appear absent from the promptflow source slice?
- **Authority risk:** Is any evidence-only or failure source being treated as doctrine without corroboration?

### 6.3 Required output

Record the check inside `appendices/APPENDIX_KB_SOURCE_MANIFEST.md` using these sections:

1. `Source universe decision`
2. `Indexed source table`
3. `Cross-index plausibility check`
4. `Included high-value sources`
5. `Excluded or deferred sources`
6. `Index gap register`
7. `Unresolved blockers`

- **Stop rule:** If a missing source appears material to the Knowledge Bank agent and cannot be safely excluded, stop before writing scaffold files.

## 7. Output contract

### 7.1 Main KB files

Create or update exactly these main files in `managed/agent_kb/special_ops__knowledge_bank/`:

1. `BEST_PRACTICES.md`
2. `MISTAKES.md`
3. `TEMPLATES.md`
4. `LEARNING_QUEUE.md`
5. `ESSENCE.md`

### 7.2 Appendix KB files

Create or update these appendix files in `managed/agent_kb/special_ops__knowledge_bank/appendices/`:

1. `APPENDIX_KB_SOURCE_MANIFEST.md`
2. `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
3. `APPENDIX_KB_CANDIDATE_LEDGER.md`
4. `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
5. `SOURCE_CONFLICT_REPORT.md` only if a load-bearing conflict exists.

### 7.3 File purposes

| File | Primary job | Must not become |
|---|---|---|
| `BEST_PRACTICES.md` | positive operating doctrine for KB placement, lifecycle, candidate intake, source slicing, appendix routing, and compaction | broad meta-ops doctrine or all-agent governance |
| `MISTAKES.md` | failure modes, confusion pairs, warning signs, recovery playbooks | generalized incident archive |
| `TEMPLATES.md` | reusable machine-readable templates for KB entries, source manifests, ranking ledgers, candidate ledgers, promotion requests, handoffs, audits | hidden promptflow law |
| `LEARNING_QUEUE.md` | candidate-only lessons and improvement backlog | accepted truth or promotion bypass |
| `ESSENCE.md` | compressed activation block derived from the other four files plus seed boundary | new doctrine source or appendix replacement |
| `APPENDIX_KB_SOURCE_MANIFEST.md` | source list, read status, role, source limit, missing/unreadable register, index plausibility check | candidate ledger |
| `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | ranked information units and source slices by value, target file, confidence, and appendix pointer | accepted KB truth |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | normalized KB candidates extracted from rankings and idea ledgers | accepted KB truth |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | failure/evidence excerpts and safeguards with evidence-only status | universal doctrine by overgeneralization |

## 8. Information ranking model

Create `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` before drafting scaffold files.

### 8.1 Ranking dimensions

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
- `scaffold_summary_needed` yes/no
- `status`

### 8.2 Ranking posture

- **Prefer:** high-agent-specific, high-actionability, high-evidence, reusable information.
- **Demote:** general AI advice, evidence-only incidents, duplicated material, and sources better owned by other Special Ops agents.
- **Split:** if information is useful but bulky, place the detail in appendices and place only the governing summary in a scaffold file.
- **Preserve:** source traceability, duplicate status, and uncertainty.

## 9. Generation sequence

### Phase 0 - repo preflight and promptflow self-sync

- Fetch this promptflow from Apex `main`.
- Verify target repo write permission.
- Verify target root exists or create it if absent.
- Patch this promptflow first if current user instruction adds a new durable rule.
- Commit promptflow changes to `main` before continuing.

### Phase 1 - source validation, index plausibility, and source manifest

- Read the binding source index.
- Fetch every core `special_ops__knowledge_bank` source listed in section 5.2.
- Fetch only cross-lane constraint sources needed for structure and validation.
- Perform the index consistency and plausibility check in section 6.
- Create `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`.
- If a primary source is inaccessible or a material index gap appears, stop affected generation and record the blocker.

### Phase 2 - information ranking ledger

- Rank the useful information units using section 8.
- Separate scaffold-summary material from appendix-detail material.
- Write `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`.

### Phase 3 - candidate ledger extraction

- Extract only candidates aligned to `special_ops__knowledge_bank` or directly constraining its KB lifecycle.
- Normalize each candidate into a row with: `candidate_id`, `title`, `source_path`, `source_role`, `candidate_class`, `target_file`, `evidence_strength`, `risk`, `status`, `notes`.
- Link candidate rows to information-ranking rows when applicable.
- Write `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`.

### Phase 4 - anti-drift appendix

- Extract failure and risk evidence without turning single incidents into universal doctrine.
- Group by risk family: `source ambiguity`, `context loss`, `candidate-to-canon leakage`, `knowledge sprawl`, `unchecked rewrite`, `missing validation`, `duplicate/conflicting sources`.
- Write `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

### Phase 5 - `BEST_PRACTICES.md`

- Derive positive doctrine only from primary/supporting sources and the ranking ledger.
- Required sections: Purpose, Scope, Source basis, Appendix map, Core rules, Candidate intake, Placement and lifecycle, Compaction and appendices, Handoff and validation, Quality checks, Open questions.
- Keep detailed evidence in appendices and point to row IDs.
- Commit after writing and fetching back.

### Phase 6 - `MISTAKES.md`

- Derive negative boundaries from anti-drift evidence plus role ownership limits.
- Required sections: Purpose, Source basis, Appendix map, Failure taxonomy, Mistake register, Confusion pairs, Warning signals, Prevention rules, Recovery playbooks, Escalation triggers, QA checks, Open questions.
- Commit after writing and fetching back.

### Phase 7 - `TEMPLATES.md`

- Produce reusable templates only for the Knowledge Bank agent.
- Required templates: KB entry, source manifest row, information ranking row, candidate ledger row, evidence-only note, promotion request stub, handoff note, QA audit mini-report.
- Commit after writing and fetching back.

### Phase 8 - `LEARNING_QUEUE.md`

- Preserve candidate-only status.
- Required sections: Purpose, Source basis, Appendix map, Intake rule, Learning candidates, Promotion candidates, Rejected/deferred notes, Review cadence, Anti-auto-promotion rule.
- Commit after writing and fetching back.

### Phase 9 - `ESSENCE.md`

- Compress only `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`, `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`, and the Apex activation seed.
- Do not introduce new sources, rules, or authority.
- Required sections: One-sentence identity, Why this agent exists, Core judgment model, Non-negotiable behaviors, Default operating sequence, Appendix map, Hard boundaries, Activation prompt, Open questions.
- Keep it a smart guide into the KB system, not the KB system itself.
- Commit after writing and fetching back.

### Phase 10 - final QA and handoff

- Verify all required files exist.
- Verify source manifest includes index plausibility check and index gap register.
- Verify information ranking ledger exists and is used by scaffold files.
- Verify all scaffold files include appendix pointers.
- Verify candidate/provisional/evidence-only status is visible where relevant.
- Verify `ESSENCE.md` adds no new doctrine and does not replace appendices.
- Verify no file outside the target KB root was changed except this promptflow when explicitly updated.
- Emit a session-style handoff summary in the final response.

## 10. Quality gates

- **Gate:** Target remains `special_ops__knowledge_bank` only.
- **Gate:** Existing indexes are used first; broad repo searching is only for bounded gap verification.
- **Gate:** Index consistency and plausibility check is completed before scaffold drafting.
- **Gate:** Information ranking ledger is completed before scaffold drafting.
- **Gate:** Every material source claim is traceable to the source manifest, ranking ledger, or candidate ledger.
- **Gate:** Evidence-only material is not promoted into doctrine without primary/supporting corroboration.
- **Gate:** Appendix files are appendices, not runtime authority.
- **Gate:** Five scaffold files stay compact and navigational; deep detail goes to appendices.
- **Gate:** `LEARNING_QUEUE.md` is candidate-only.
- **Gate:** `ESSENCE.md` is compression and guidance only.
- **Gate:** No accepted truth changes are claimed.
- **Gate:** Promptflow improvements are committed to repo main before they are relied on.

## 11. Stop conditions

Stop and report if any of these occur:

- `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` cannot be read.
- A core primary source cannot be fetched from `MasterOfArts@main`.
- Apex target root or write permission is unavailable.
- A material index gap appears and cannot be resolved through the already-created indexes.
- A source conflict affects the target identity, source universe, scaffold, appendix model, or promotion boundary.
- The requested output requires guessing from filenames instead of reading files.
- The task drifts into building all Special Ops agents.
- The run would modify shared governance or accepted truth without separate authorization.
- The promptflow needs an update but cannot be committed to `main`.

## 12. Reporting format

After each phase, report in this compact structure:

```yaml
phase_completed: <phase id and name>
files_written:
  - <repo-relative path>
repo_commits:
  - <sha or pending>
validation_status: pass | fragile | blocked
blockers:
  - <none or blocker>
next_phase: <phase id and name>
```

Final response must include:

```yaml
target_locked: special_ops__knowledge_bank
repo_promptflow_path: managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_BASE_BUILD.md
main_files_expected: 5
appendix_files_expected: 4_or_5_if_conflict
source_validation_status: pass | fragile | blocked
index_plausibility_status: pass | fragile | blocked
ranking_ledger_status: pass | fragile | blocked
next_safe_action: <one sentence>
```

## 13. Machine-readable execution block

```yaml
accepted_target:
  agent_id: special_ops__knowledge_bank
  target_repo: leela-spec/apexai-os-meta
  target_branch: main
  target_root: managed/agent_kb/special_ops__knowledge_bank/
  source_repo: leela-spec/MasterOfArts
  source_branch: main
  source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

main_outputs:
  - managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
  - managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
  - managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
  - managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md
  - managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md

appendix_outputs:
  - managed/agent_kb/special_ops__knowledge_bank/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
  - managed/agent_kb/special_ops__knowledge_bank/appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
  - managed/agent_kb/special_ops__knowledge_bank/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  - managed/agent_kb/special_ops__knowledge_bank/appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  - managed/agent_kb/special_ops__knowledge_bank/appendices/SOURCE_CONFLICT_REPORT.md

promptflow_self_update:
  path: managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_BASE_BUILD.md
  rule: update_on_main_before_relying_on_new_execution_logic
  blocker_if_unwritable: repo_write_blocked
```
