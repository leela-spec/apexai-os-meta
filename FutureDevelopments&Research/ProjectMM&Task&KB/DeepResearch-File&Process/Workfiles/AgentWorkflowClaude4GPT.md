## Recommended Agent Mode Workflow

## Phase 0 — Session Init (one-time, ~2 min)

Paste into Agent Mode browser window:

text

`AGENT MODE INIT — APEX HARMONIZATION CONSTRUCTION Repo: leela-spec/apexai-os-meta (clone via PAT) Research is complete. Do NOT re-read source repos. git clone https://<PAT>@github.com/leela-spec/apexai-os-meta.git cd apexai-os-meta All decisions are pre-locked. Your job is file generation only. Read and follow these decisions exactly — do not rediscover them: H1 STATUS ENUM: [open, in-progress, blocked, done, deferred] H2 BASE PATH: apex-meta/ H3 DEPENDENCY FIELD: depends_on (int array) H4 SCRIPT LANGUAGE: Python H5 CLUSTERS: A=PLAN (PM1,PM2,PM3,PD1,PD2,PD4), B=SYNC (PM4,PM5,PM7,PM8,KB4,KB5), C=SESSION (PM6,KB1,KB2,KB3,KB6,PD3,PD5,PD6) H6 HANDOFF FORMAT: task_plan.md + findings.md + progress.md + next-session.md H7 PRIORITY: high=3 / medium=2 / low=1; urgency = days-to-due-date normalized LIVE SKILLS — do not break:   .claude/skills/status-merge/SKILL.md  .claude/skills/flow-recap/SKILL.md  .claude/skills/project-kb-manager/SKILL.md  .claude/skills/PrecapNextDay/SKILL.md Gate rule: before writing ANY file, output delta proposal. Wait for CONFIRM.`

---

## Phase 1 — Write `decisions.md` (was Step 2, now pre-populated)

Since H1–H7 are already resolved by the research, the agent writes directly:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/657e91e5-74f3-4d93-af70-290dcafee694/ProThinkingGPT_v1-2.md?AWSAccessKeyId=ASIA2F3EMEYE6KO7FJZ6&Signature=F5tSUvhgOUON2hLm0GfOmEB9nrE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDz7R7EfarHLK78UG9BYG2z2Zb8laqzkg3gQZJ4Qr06nwIgf%2BSs1e9rIjE%2FqSpM5Fi1RvkSYCohLpunBZSYuUe0YbEq%2FAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDMab4ekgF9BRq%2BT%2FmyrQBE0rxGGfmV%2FhIc70VvMv6NU9bmhGUvF4ZSRkxzLvbAnjVIHo1nKe83YagA0XB%2FngPz1ae%2B69VBRC6sLjedUvd1JyTThKcnVQcAq%2Br%2FdLb1WHRNdQf5k4CazRJk4W9nAgFQgZdJ9biYIDG1lqbY0H5f6KpXq9XSL%2Flg6Vt7wgJODrmtnLFjL1w5tEN0vGpvAoqHeBPzDWBtX9JcUemp%2F9SVjTYNkgME5%2FXh1qK%2BRWuAr0IjlYpHS7fqHSwhReOEMMTIA81JAmp0DDTGjKVxTam3lObbR7YLndkV7xgl3n4eR1UGkLNqs585%2B1EbBj8UBVQKG2GiW%2FdBAdre7uo5eHcJqRV38e%2FW%2BZlf2RHrYgcxvlR3ID%2BrkHUUXO5hT4o6tev7kMB04dAObV6lNig83d7plSBtfbQv4FYlt7w6POO3DRbsMTB8mEiLxVXbQ6Jjx9GFxy1AJN2q6pp0N19rX6DwGzf2HY9qIACoTK4SaU%2BfRXcrQgVLVMvMnAvfo7Lr8hqJQhxHsb%2Balgvu1sAZIdugKdb1Xa8ynJksZB7oUE7upAPUX2Ee1i6HNVxoSCWiV6X5Py8BX6QH0OcqliZGPHp3SNP960wMxyLmHSOtAWDvSdBHCoWzLDt2GttCmg8ARaN6m2wpFrrLLk7kELNA5%2ByexSK6U2NnggqPXQKscOxQiOElzW3T1Rtq2SWeNXmznQGWT5ajlMAOY9ZFalhU0aKL6wQHkdG1KMR5%2FqrdfyKepQ4hjkoBE3dLeA5rL%2BsQBfskKJcUehN2FkYFhasgM8Tc8w1qLU0QY6mAFj%2FezP%2FEWFnINRNYD7ECOW4pSx0bm08d8L0kpFGUqDQHabci2Xm3bSi4wPjex6twFhG6SQNpgYv8iZEImQrvLgZ6acxGq46NnmIw3%2FsMUwPTYIIzwl7C6FoP22j%2Fy0aLkN%2FeacDL1r1dipseYzWjeV2xmK10PdOoNak26E1v1nxfGMcq5RDsRddcimjEFhN2g3t%2B2S%2FLa%2FYg%3D%3D&Expires=1781866281)

text

`Write apex-meta/harmonization/decisions.md Use the H1–H7 values from the init message verbatim. Include source evidence URLs per decision (from the research output). Validate: all 7 decisions present, file has YAML frontmatter with step:2 status:locked. Commit: git commit -m "APEX STEP 2 — decisions locked from ProThinking research" CONFIRM before writing.`

---

## Phase 2 — Field Schema + Task Template (Step 3)

The research confirmed the canonical field set from Backlog.md TypeScript types. Paste:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/657e91e5-74f3-4d93-af70-290dcafee694/ProThinkingGPT_v1-2.md?AWSAccessKeyId=ASIA2F3EMEYE6KO7FJZ6&Signature=F5tSUvhgOUON2hLm0GfOmEB9nrE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDz7R7EfarHLK78UG9BYG2z2Zb8laqzkg3gQZJ4Qr06nwIgf%2BSs1e9rIjE%2FqSpM5Fi1RvkSYCohLpunBZSYuUe0YbEq%2FAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDMab4ekgF9BRq%2BT%2FmyrQBE0rxGGfmV%2FhIc70VvMv6NU9bmhGUvF4ZSRkxzLvbAnjVIHo1nKe83YagA0XB%2FngPz1ae%2B69VBRC6sLjedUvd1JyTThKcnVQcAq%2Br%2FdLb1WHRNdQf5k4CazRJk4W9nAgFQgZdJ9biYIDG1lqbY0H5f6KpXq9XSL%2Flg6Vt7wgJODrmtnLFjL1w5tEN0vGpvAoqHeBPzDWBtX9JcUemp%2F9SVjTYNkgME5%2FXh1qK%2BRWuAr0IjlYpHS7fqHSwhReOEMMTIA81JAmp0DDTGjKVxTam3lObbR7YLndkV7xgl3n4eR1UGkLNqs585%2B1EbBj8UBVQKG2GiW%2FdBAdre7uo5eHcJqRV38e%2FW%2BZlf2RHrYgcxvlR3ID%2BrkHUUXO5hT4o6tev7kMB04dAObV6lNig83d7plSBtfbQv4FYlt7w6POO3DRbsMTB8mEiLxVXbQ6Jjx9GFxy1AJN2q6pp0N19rX6DwGzf2HY9qIACoTK4SaU%2BfRXcrQgVLVMvMnAvfo7Lr8hqJQhxHsb%2Balgvu1sAZIdugKdb1Xa8ynJksZB7oUE7upAPUX2Ee1i6HNVxoSCWiV6X5Py8BX6QH0OcqliZGPHp3SNP960wMxyLmHSOtAWDvSdBHCoWzLDt2GttCmg8ARaN6m2wpFrrLLk7kELNA5%2ByexSK6U2NnggqPXQKscOxQiOElzW3T1Rtq2SWeNXmznQGWT5ajlMAOY9ZFalhU0aKL6wQHkdG1KMR5%2FqrdfyKepQ4hjkoBE3dLeA5rL%2BsQBfskKJcUehN2FkYFhasgM8Tc8w1qLU0QY6mAFj%2FezP%2FEWFnINRNYD7ECOW4pSx0bm08d8L0kpFGUqDQHabci2Xm3bSi4wPjex6twFhG6SQNpgYv8iZEImQrvLgZ6acxGq46NnmIw3%2FsMUwPTYIIzwl7C6FoP22j%2Fy0aLkN%2FeacDL1r1dipseYzWjeV2xmK10PdOoNak26E1v1nxfGMcq5RDsRddcimjEFhN2g3t%2B2S%2FLa%2FYg%3D%3D&Expires=1781866281)

text

`Write apex-meta/harmonization/field-schema.md and task-template.md Source: Backlog.md TaskInterface (S2b), CCPM structure.md (S1b), Task Master schema (S3a) Fields confirmed: name, status(H1), created, updated, priority(H7), urgency(H7),   depends_on(H3), parallel, conflicts_with, effort(XS/S/M/L/XL), epic, due_date Mark: required/optional/computed per research evidence. No invented fields. Commit after CONFIRM.`

---

## Phase 3 — Python Scripts (highest priority — Cluster B scripts first)

The research identified 4 scripts that MUST be Python:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/657e91e5-74f3-4d93-af70-290dcafee694/ProThinkingGPT_v1-2.md?AWSAccessKeyId=ASIA2F3EMEYE6KO7FJZ6&Signature=F5tSUvhgOUON2hLm0GfOmEB9nrE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDz7R7EfarHLK78UG9BYG2z2Zb8laqzkg3gQZJ4Qr06nwIgf%2BSs1e9rIjE%2FqSpM5Fi1RvkSYCohLpunBZSYuUe0YbEq%2FAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDMab4ekgF9BRq%2BT%2FmyrQBE0rxGGfmV%2FhIc70VvMv6NU9bmhGUvF4ZSRkxzLvbAnjVIHo1nKe83YagA0XB%2FngPz1ae%2B69VBRC6sLjedUvd1JyTThKcnVQcAq%2Br%2FdLb1WHRNdQf5k4CazRJk4W9nAgFQgZdJ9biYIDG1lqbY0H5f6KpXq9XSL%2Flg6Vt7wgJODrmtnLFjL1w5tEN0vGpvAoqHeBPzDWBtX9JcUemp%2F9SVjTYNkgME5%2FXh1qK%2BRWuAr0IjlYpHS7fqHSwhReOEMMTIA81JAmp0DDTGjKVxTam3lObbR7YLndkV7xgl3n4eR1UGkLNqs585%2B1EbBj8UBVQKG2GiW%2FdBAdre7uo5eHcJqRV38e%2FW%2BZlf2RHrYgcxvlR3ID%2BrkHUUXO5hT4o6tev7kMB04dAObV6lNig83d7plSBtfbQv4FYlt7w6POO3DRbsMTB8mEiLxVXbQ6Jjx9GFxy1AJN2q6pp0N19rX6DwGzf2HY9qIACoTK4SaU%2BfRXcrQgVLVMvMnAvfo7Lr8hqJQhxHsb%2Balgvu1sAZIdugKdb1Xa8ynJksZB7oUE7upAPUX2Ee1i6HNVxoSCWiV6X5Py8BX6QH0OcqliZGPHp3SNP960wMxyLmHSOtAWDvSdBHCoWzLDt2GttCmg8ARaN6m2wpFrrLLk7kELNA5%2ByexSK6U2NnggqPXQKscOxQiOElzW3T1Rtq2SWeNXmznQGWT5ajlMAOY9ZFalhU0aKL6wQHkdG1KMR5%2FqrdfyKepQ4hjkoBE3dLeA5rL%2BsQBfskKJcUehN2FkYFhasgM8Tc8w1qLU0QY6mAFj%2FezP%2FEWFnINRNYD7ECOW4pSx0bm08d8L0kpFGUqDQHabci2Xm3bSi4wPjex6twFhG6SQNpgYv8iZEImQrvLgZ6acxGq46NnmIw3%2FsMUwPTYIIzwl7C6FoP22j%2Fy0aLkN%2FeacDL1r1dipseYzWjeV2xmK10PdOoNak26E1v1nxfGMcq5RDsRddcimjEFhN2g3t%2B2S%2FLa%2FYg%3D%3D&Expires=1781866281)

|Script|Source algorithm|Priority rank|
|---|---|---|
|`find_next_task.py`|Task Master S3c — dependency satisfaction + priority sort|1|
|`show_blocked.py`|Kanban show_blocked.sh (S5b) — rewritten Python|2|
|`update_index.py`|llm-wiki S6b — adapt frontmatter keys to Apex|3 (FULL copy)|
|`drift_check.py`|S6b dry-run + S9b hash pattern — custom build|14|
|`score_unlock_depth.py`|S3c reverse traversal — custom build|16|

Paste for each script individually — **one script per agent turn**:

text

`Write scripts/find_next_task.py Algorithm: port find-next-task.js (S3c) to Python over Apex Markdown/YAML files. Input: apex-meta/ task files with H1 status and H3 depends_on fields. Output: stdout — ranked list of eligible tasks (id | priority | dep_count | title) Error: if file missing or malformed frontmatter, print warning and skip file. Must not: write any task file, modify status. Run it after writing. Show output. CONFIRM before writing.`

---

## Phase 4 — SKILL Files (Clusters B → C → A)

After scripts are verified running, generate SKILL files. Order matches research priority rank:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/657e91e5-74f3-4d93-af70-290dcafee694/ProThinkingGPT_v1-2.md?AWSAccessKeyId=ASIA2F3EMEYE6KO7FJZ6&Signature=F5tSUvhgOUON2hLm0GfOmEB9nrE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDz7R7EfarHLK78UG9BYG2z2Zb8laqzkg3gQZJ4Qr06nwIgf%2BSs1e9rIjE%2FqSpM5Fi1RvkSYCohLpunBZSYuUe0YbEq%2FAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDMab4ekgF9BRq%2BT%2FmyrQBE0rxGGfmV%2FhIc70VvMv6NU9bmhGUvF4ZSRkxzLvbAnjVIHo1nKe83YagA0XB%2FngPz1ae%2B69VBRC6sLjedUvd1JyTThKcnVQcAq%2Br%2FdLb1WHRNdQf5k4CazRJk4W9nAgFQgZdJ9biYIDG1lqbY0H5f6KpXq9XSL%2Flg6Vt7wgJODrmtnLFjL1w5tEN0vGpvAoqHeBPzDWBtX9JcUemp%2F9SVjTYNkgME5%2FXh1qK%2BRWuAr0IjlYpHS7fqHSwhReOEMMTIA81JAmp0DDTGjKVxTam3lObbR7YLndkV7xgl3n4eR1UGkLNqs585%2B1EbBj8UBVQKG2GiW%2FdBAdre7uo5eHcJqRV38e%2FW%2BZlf2RHrYgcxvlR3ID%2BrkHUUXO5hT4o6tev7kMB04dAObV6lNig83d7plSBtfbQv4FYlt7w6POO3DRbsMTB8mEiLxVXbQ6Jjx9GFxy1AJN2q6pp0N19rX6DwGzf2HY9qIACoTK4SaU%2BfRXcrQgVLVMvMnAvfo7Lr8hqJQhxHsb%2Balgvu1sAZIdugKdb1Xa8ynJksZB7oUE7upAPUX2Ee1i6HNVxoSCWiV6X5Py8BX6QH0OcqliZGPHp3SNP960wMxyLmHSOtAWDvSdBHCoWzLDt2GttCmg8ARaN6m2wpFrrLLk7kELNA5%2ByexSK6U2NnggqPXQKscOxQiOElzW3T1Rtq2SWeNXmznQGWT5ajlMAOY9ZFalhU0aKL6wQHkdG1KMR5%2FqrdfyKepQ4hjkoBE3dLeA5rL%2BsQBfskKJcUehN2FkYFhasgM8Tc8w1qLU0QY6mAFj%2FezP%2FEWFnINRNYD7ECOW4pSx0bm08d8L0kpFGUqDQHabci2Xm3bSi4wPjex6twFhG6SQNpgYv8iZEImQrvLgZ6acxGq46NnmIw3%2FsMUwPTYIIzwl7C6FoP22j%2Fy0aLkN%2FeacDL1r1dipseYzWjeV2xmK10PdOoNak26E1v1nxfGMcq5RDsRddcimjEFhN2g3t%2B2S%2FLa%2FYg%3D%3D&Expires=1781866281)

**Cluster B first** (PM4, PM5, PM7, PM8, KB4, KB5):

text

`Write .claude/skills/apex-sync/SKILL.md Triggers: "what's next", "any blockers", "stall check", "rebuild registry", "sync state", "drift report" Calls scripts: find_next_task.py, show_blocked.py, update_index.py, drift_check.py Base: CCPM track.md pattern (S1c) — script-first rule Validate H1/H2/H3 compliance. Confirm live skills not broken. CONFIRM before writing.`

**Cluster C** (PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6):

text

`Write .claude/skills/apex-session/SKILL.md Write-gate: ALL mutations require delta proposal → operator types CONFIRM Triggers: "log session", "update status", "apply deltas", "handoff", "operator approve" KB6 output: apex-meta/handoff/next-session.md (H6 format) Base: planning-with-files (S4a) + crewAI human_input gate (S8a) CONFIRM before writing.`

**Cluster A** (PM1, PM2, PM3, PD1, PD2, PD4):

text

`Write .claude/skills/apex-plan/SKILL.md No scripts. Pure instruction + file writes. Triggers: "capture project", "decompose", "assign dependencies", "score priority", "new epic" Operator approval gate before creating any new epic or task file. Base: CCPM structure.md (S1b) + Backlog task contract (S2b) CONFIRM before writing.`

---

## Phase 5 — Final Validation Checklist

After all files committed, run this in terminal:

bash

`python3 scripts/find_next_task.py       # must execute without error python3 scripts/update_index.py --dry-run  # must scan apex-meta/ grep -r "H1" apex-meta/harmonization/  # decisions present ls .claude/skills/                      # apex-sync, apex-session, apex-plan exist`

Then paste the final gate:

text

`Run validation: □ H1 enum used identically in all 3 SKILL files □ H2 paths consistent across decisions.md and all SKILLs □ H3 depends_on field name consistent □ apex-sync does NOT write task content □ KB6 handoff format present in apex-session □ status-merge and flow-recap inputs still satisfied □ PD5 operator gate present in apex-session AND apex-plan Report YES/NO per checkbox. Fix any NO before closing session.`

---

## Key Differences from Previous Q&A

The prior Q&A described the **research phase** (Steps 1–4 of the original prompt flow). That research is now **done**. This workflow skips directly to construction — decisions are pre-locked, sources are identified, the agent's only job is to write files and run scripts. Total estimated agent turns: **~12–15**, one file/script per CONFIRM cycle.