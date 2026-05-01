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
owner: special_ops__knowledge_bank
validator: special_ops__informatics_design
---

# Promptflow: Special Ops Knowledge Bank KB Base Build

## 1. Target lock

- **Decision:** This promptflow builds the KB base and appendix KB for exactly one head agent: `special_ops__knowledge_bank`.
- **Target KB root:** `managed/agent_kb/special_ops__knowledge_bank/` in `leela-spec/apexai-os-meta` on `main`.
- **Source root:** `leela-spec/MasterOfArts` on `main`.
- **Primary source index:** `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`.
- **Scaffold authority:** use the Apex agent-KB scaffold convention: `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`.
- **Appendix target:** create appendix material under `managed/agent_kb/special_ops__knowledge_bank/appendices/`.
- **Non-target:** do not build KBs for the other Special Ops agents in this run.

## 2. Repo-write continuity rule

- **Rule:** The current promptflow must live in the target repo on `main` and must be updated there whenever the execution logic changes.
- **Rule:** At the start of every future run, fetch this file from `managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_BASE_BUILD.md` and treat it as the active promptflow authority after current user instruction.
- **Rule:** If a better constraint, source decision, validation rule, or stage boundary is discovered during execution, patch this promptflow first and commit the update to `main` before continuing.
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

## 4. Selected source index

### 4.1 Binding source-map file

| Path | Role | Read mode | Use |
|---|---:|---:|---|
| `agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` | source index | read full | binding source map and cluster boundary |

### 4.2 Core `special_ops__knowledge_bank` sources

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

### 4.3 Cross-lane constraint sources

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

### 4.4 Explicit exclusions

- **Exclude:** full Special Ops KB factory output for all agents.
- **Exclude:** other Special Ops source clusters as primary content.
- **Exclude:** broad repo traversal beyond the selected index when the selected sources answer the task.
- **Exclude:** web research.
- **Exclude:** manually attached outside-repo files unless current user instruction names them for this run.
- **Exclude:** any accepted-truth mutation or governance-file rewrite outside `managed/agent_kb/special_ops__knowledge_bank/` unless separately authorized.

## 5. Output contract

### 5.1 Main KB files

Create or update exactly these main files in `managed/agent_kb/special_ops__knowledge_bank/`:

1. `BEST_PRACTICES.md`
2. `MISTAKES.md`
3. `TEMPLATES.md`
4. `LEARNING_QUEUE.md`
5. `ESSENCE.md`

### 5.2 Appendix KB files

Create or update these appendix files in `managed/agent_kb/special_ops__knowledge_bank/appendices/`:

1. `APPENDIX_KB_SOURCE_MANIFEST.md`
2. `APPENDIX_KB_CANDIDATE_LEDGER.md`
3. `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
4. `SOURCE_CONFLICT_REPORT.md` only if a load-bearing conflict exists.

### 5.3 File purposes

| File | Primary job | Must not become |
|---|---|---|
| `BEST_PRACTICES.md` | positive operating doctrine for KB placement, lifecycle, candidate intake, source slicing, and compaction | broad meta-ops doctrine or all-agent governance |
| `MISTAKES.md` | failure modes, confusion pairs, warning signs, recovery playbooks | generalized incident archive |
| `TEMPLATES.md` | reusable machine-readable templates for KB entries, source manifests, candidate ledgers, promotion requests, handoffs, audits | hidden prompt-flow law |
| `LEARNING_QUEUE.md` | candidate-only lessons and improvement backlog | accepted truth or promotion bypass |
| `ESSENCE.md` | compressed activation block derived from the other four files plus seed boundary | new doctrine source |
| `APPENDIX_KB_SOURCE_MANIFEST.md` | source list, read status, role, source limit, missing/unreadable register | candidate ledger |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | normalized candidates extracted from rankings and idea ledgers | accepted KB truth |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | failure/evidence excerpts and safeguards with evidence-only status | universal doctrine by overgeneralization |

## 6. Generation sequence

### Phase 0 - repo preflight and promptflow self-sync

- Fetch this promptflow from Apex `main`.
- Verify target repo write permission.
- Verify target root exists or create it if absent.
- Patch this promptflow first if current user instruction adds a new durable rule.
- Commit promptflow changes to `main` before continuing.

### Phase 1 - source validation and source manifest

- Read the binding source index.
- Fetch every core `special_ops__knowledge_bank` source listed in section 4.2.
- Fetch only the cross-lane constraint sources needed for structure and validation.
- Create `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`.
- If a primary source is inaccessible, stop affected generation and record the blocker.

### Phase 2 - candidate ledger extraction

- Extract only candidates aligned to `special_ops__knowledge_bank` or directly constraining its KB lifecycle.
- Normalize each candidate into a row with: `candidate_id`, `title`, `source_path`, `source_role`, `candidate_class`, `target_file`, `evidence_strength`, `risk`, `status`, `notes`.
- Write `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`.

### Phase 3 - anti-drift appendix

- Extract failure and risk evidence without turning single incidents into universal doctrine.
- Group by risk family: `source ambiguity`, `context loss`, `candidate-to-canon leakage`, `knowledge sprawl`, `unchecked rewrite`, `missing validation`, `duplicate/conflicting sources`.
- Write `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

### Phase 4 - `BEST_PRACTICES.md`

- Derive positive doctrine only from primary/supporting sources.
- Required sections: Purpose, Scope, Source basis, Core rules, Candidate intake, Placement and lifecycle, Compaction and appendices, Handoff and validation, Quality checks, Open questions.
- Commit after writing and fetching back.

### Phase 5 - `MISTAKES.md`

- Derive negative boundaries from anti-drift evidence plus role ownership limits.
- Required sections: Purpose, Failure taxonomy, Mistake register, Confusion pairs, Warning signals, Prevention rules, Recovery playbooks, Escalation triggers, QA checks, Open questions.
- Commit after writing and fetching back.

### Phase 6 - `TEMPLATES.md`

- Produce reusable templates only for the Knowledge Bank agent.
- Required templates: KB entry, source manifest row, candidate ledger row, evidence-only note, promotion request stub, handoff note, QA audit mini-report.
- Commit after writing and fetching back.

### Phase 7 - `LEARNING_QUEUE.md`

- Preserve candidate-only status.
- Required sections: Purpose, Intake rule, Learning candidates, Promotion candidates, Rejected/deferred notes, Review cadence, Anti-auto-promotion rule.
- Commit after writing and fetching back.

### Phase 8 - `ESSENCE.md`

- Compress only `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`, and the Apex activation seed.
- Do not introduce new sources, rules, or authority.
- Required sections: One-sentence identity, Why this agent exists, Core judgment model, Non-negotiable behaviors, Default operating sequence, Hard boundaries, Activation prompt, Open questions.
- Commit after writing and fetching back.

### Phase 9 - final QA and handoff

- Verify all required files exist.
- Verify all files include source slices or source-basis sections.
- Verify candidate/provisional/evidence-only status is visible where relevant.
- Verify `ESSENCE.md` adds no new doctrine.
- Verify no file outside the target KB root was changed except this promptflow when explicitly updated.
- Emit a session-style handoff summary in the final response.

## 7. Quality gates

- **Gate:** Target remains `special_ops__knowledge_bank` only.
- **Gate:** Every material source claim is traceable to the source manifest or candidate ledger.
- **Gate:** Evidence-only material is not promoted into doctrine without primary/supporting corroboration.
- **Gate:** Appendix files are appendices, not runtime authority.
- **Gate:** `LEARNING_QUEUE.md` is candidate-only.
- **Gate:** `ESSENCE.md` is compression-only.
- **Gate:** No accepted truth changes are claimed.
- **Gate:** No broad repo discovery is used when indexed sources are sufficient.
- **Gate:** Promptflow improvements are committed to repo main before they are relied on.

## 8. Stop conditions

Stop and report if any of these occur:

- `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` cannot be read.
- A core primary source cannot be fetched from `MasterOfArts@main`.
- Apex target root or write permission is unavailable.
- A source conflict affects the target identity, source universe, scaffold, or promotion boundary.
- The requested output requires guessing from filenames instead of reading files.
- The task drifts into building all Special Ops agents.
- The run would modify shared governance or accepted truth without separate authorization.
- The promptflow needs an update but cannot be committed to `main`.

## 9. Reporting format

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
appendix_files_expected: 3_or_4_if_conflict
source_validation_status: pass | fragile | blocked
next_safe_action: <one sentence>
```

## 10. Machine-readable execution block

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
  - managed/agent_kb/special_ops__knowledge_bank/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  - managed/agent_kb/special_ops__knowledge_bank/appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  - managed/agent_kb/special_ops__knowledge_bank/appendices/SOURCE_CONFLICT_REPORT.md

promptflow_self_update:
  path: managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_BASE_BUILD.md
  rule: update_on_main_before_relying_on_new_execution_logic
  blocker_if_unwritable: repo_write_blocked
```
