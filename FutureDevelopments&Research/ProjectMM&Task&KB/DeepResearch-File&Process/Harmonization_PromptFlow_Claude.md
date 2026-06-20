## Apex — Claude Prompt Flow (repo access, sequential, each step feeds the next)

**How to use:** Open one Claude chat with repo access to `leela-spec/apexai-os-meta`. Paste Step 1. When Claude finishes and produces the output artifact, paste Step 2 into the **same chat**. Each step depends on what the previous step wrote to the repo or produced as output.

---

## Step 1 — Read + Map (foundation, no writing yet)

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 1 — BASELINE AUDIT Repo: leela-spec/apexai-os-meta ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Do not write any files yet. Read only. Read these files in this exact order. Record every field name, every status value, every path you find. LIVE SKILLS (integration anchors — must not be broken): 1. .claude/skills/status-merge/SKILL.md 2. .claude/skills/flow-recap/SKILL.md 3. .claude/skills/project-kb-manager/SKILL.md 4. .claude/skills/PrecapNextDay/SKILL.md SOURCE REPOS: 5. source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/structure.md 6. source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md 7. source-knowledge/ProjectRepos/backlog-main/ (find any task .md file and config) 8. source-knowledge/ProjectRepos/claude-task-master-main/ (find tasks schema or docs/task-structure.md) 9. source-knowledge/ProjectRepos/llm-wiki-main/ (find SKILL.md and any index script) 10. source-knowledge/ProjectRepos/gsd-core-next/ (find STATE.md and CONTEXT.md) 11. source-knowledge/ProjectRepos/planning-with-files-master/SKILL.md For each file read, produce a compact extraction block: FILE: [exact path] ─ status enum values found: [list or NONE] ─ YAML frontmatter fields found: [list with types] ─ dependency field name + value type: [or NONE] ─ script-first rule: [YES/NO + quote] ─ file paths written by this skill: [list or NONE] ─ trigger phrase: [or NONE] After all reads, produce ONE conflict table: | Field concept | Name in source A | Name in source B | Values differ? | |---|---|---|---| Do not resolve conflicts yet. Just surface them. This is the only output of Step 1.`

---

## Step 2 — Lock Decisions (H1–H7)

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 2 — LOCK 7 DECISIONS Build on: Step 1 conflict table + file extractions ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Using only the evidence from Step 1, lock these 7 decisions. For each, state: locked value | rationale | source file. No new file reads. Work from Step 1 output only. H1 — STATUS ENUM Single canonical list for all Apex task/entity files. Must be compatible with status-merge/SKILL.md values. Format: array literal, e.g. [open, in-progress, blocked, done, deferred] H2 — FILE PATH CONVENTION Canonical directory structure for epics, tasks, and project state. Format: file tree block. Must not conflict with existing skill paths. H3 — DEPENDENCY FIELD Canonical field name + value type. Rule: a 10-line Python script must be able to traverse it without ambiguity. State what that traversal looks like. H4 — SCRIPT LANGUAGE Bash or Python — for ALL deterministic operations. One answer. If exceptions exist, state the rule for when. H5 — CLUSTER ASSIGNMENT Assign all 20 processes to exactly one of three clusters:   A — PLAN  (pure SKILL.md, no scripts)  B — SYNC  (SKILL.md + read-only scripts)  C — SESSION (SKILL.md + write-gate scripts) Table format: | Process ID | Name | Cluster | One-line rationale | H6 — HANDOFF FORMAT Format for KB6 session handoff doc. Required sections (list them). File name convention. H7 — PRIORITY + URGENCY MODEL One model each. Must work from frontmatter fields alone. State the field name(s) and the value type. Output format: one decision block per H. Each block: locked value in a code fence, then rationale row, then source file path. No prose paragraphs. Write the locked decisions to:   apex-meta/harmonization/decisions.md Create the file. Use this structure: --- step: 2 status: locked generated: [today's date] --- # Apex Harmonization Decisions ## H1 Status Enum ... ## H2 File Paths ... [etc through H7]`

---

## Step 3 — Unified Field Schema

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 3 — UNIFIED FIELD SCHEMA Build on: apex-meta/harmonization/decisions.md ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read apex-meta/harmonization/decisions.md first. Produce the complete YAML frontmatter field schema for ALL task and entity files in Apex. Rules: - Every field must appear in at least one source from Step 1.   If it was in no source, do not include it. - If two sources used different names for the same concept,   use the H1–H3 locked names. Note the alias. - Mark each field: required | optional | computed (set by script) Table: | Field | Type | Required? | Default | Alias | Used by processes | Source path | After the table, produce the canonical task template as a YAML code block showing all fields:   ---  name:  status:          # H1 enum  created:  updated:  priority:        # H7  urgency:         # H7  depends_on:      # H3 — value type locked  parallel:  conflicts_with:  effort:          # size XS/S/M/L/XL  epic:            # parent epic slug  --- Write two files:   apex-meta/harmonization/field-schema.md   ← the table  apex-meta/harmonization/task-template.md  ← the YAML block +                                               body section scaffold`

---

## Step 4 — Integration Contracts

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 4 — INTEGRATION CONTRACTS Build on: decisions.md + field-schema.md ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read these files:   apex-meta/harmonization/decisions.md  apex-meta/harmonization/field-schema.md  .claude/skills/status-merge/SKILL.md  .claude/skills/flow-recap/SKILL.md  .claude/skills/project-kb-manager/SKILL.md  .claude/skills/PrecapNextDay/SKILL.md For each live skill, produce an integration contract: SKILL: [name] ─ Reads: [file path | fields consumed] ─ Writes: [file path | fields written] ─ Status values it expects: [list] ─ Compatible with H1 enum: YES / NO — if NO, state exact conflict ─ Compatible with H2 paths: YES / NO — if NO, state exact conflict ─ Compatible with H3 dep field: YES / NO — if NO, state exact conflict ─ Action required: NONE | MINOR ADAPT [what] | BREAKING [what] Then: one CONFLICT RESOLUTION TABLE | Skill | Conflict | H-decision | Minimum fix | Risk if unfixed | Then: one SAFE SEQUENCE List the 20 new PM/KB/PD processes in the order they must be implemented so that no new process breaks a live skill before the adaptation is done. Format: numbered list with one sentence rationale per step. Write to:   apex-meta/harmonization/integration-contracts.md`

---

## Step 5 — Cluster Briefs (build spec, not files)

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 5 — CLUSTER BRIEFS Build on: decisions.md + integration-contracts.md ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read:   apex-meta/harmonization/decisions.md  apex-meta/harmonization/integration-contracts.md  apex-meta/harmonization/field-schema.md For each of the three clusters (A PLAN, B SYNC, C SESSION), write a structured brief. This is the contract used in Step 6 to generate actual SKILL.md files. Do NOT write SKILL.md yet. CLUSTER [X] — [NAME] ──────────────────────────────────────────────── Processes:           [ID list] One SKILL or split?: [answer + rule] Trigger phrase(s):   [exact strings] Reads:               [path | fields] Writes:              [path | fields] Scripts:   [filename] | [what it does] | [input format] | [output format] Templates needed:    [filename | purpose] Base source:         [exact path in source-knowledge/ProjectRepos/] What to copy:        [what stays identical] What to change:      [field names, paths, language adaptations] Failure modes:   [scenario] → [how SKILL handles it] Validation gate:     [what operator approves before any write] ──────────────────────────────────────────────── Write to:   apex-meta/harmonization/cluster-A-brief.md  apex-meta/harmonization/cluster-B-brief.md  apex-meta/harmonization/cluster-C-brief.md`

---

## Step 6 — Generate SKILL files (Cluster B first — highest priority)

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 6 — GENERATE CLUSTER B SKILL FILES Build on: cluster-B-brief.md + all harmonization files Cluster B covers: PM4, PM5, PM7, PM8, KB4, KB5 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read ALL of these before writing anything:   apex-meta/harmonization/decisions.md  apex-meta/harmonization/field-schema.md  apex-meta/harmonization/integration-contracts.md  apex-meta/harmonization/cluster-B-brief.md  .claude/skills/status-merge/SKILL.md   ← do not break this  .claude/skills/flow-recap/SKILL.md     ← do not break this  source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/SKILL.md  source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md Generate these files. Write them to the repo. FILE 1: .claude/skills/apex-sync/SKILL.md   - Covers: PM4, PM5, PM7, PM8, KB4, KB5  - Triggers: "what's next", "any blockers", "stall check",               "rebuild registry", "sync state", "drift report"  - Scripts it calls (do not write scripts yet, reference them):      scripts/next_action.py      scripts/blocked_check.py      scripts/stall_detect.py      scripts/registry_build.py  - Must comply with H1 status enum, H2 paths, H3 dep field exactly  - Copy structure from ccpm track.md — adapt language and paths FILE 2: apex-meta/harmonization/cluster-B-scripts-spec.md   For each of the 4 scripts above, write a precise spec:  ─ Filename  ─ Purpose: one sentence  ─ Input: exact file paths and fields it reads  ─ Output: what it writes or prints  ─ Algorithm: pseudocode (5–15 lines max)  ─ Error handling: what it does if a file is missing or malformed  ─ Must not: list what the script must never do (e.g., write task files) After generating, run validation: □ H1 enum used consistently in SKILL.md □ H2 paths match decisions.md □ H3 dep field name matches decisions.md □ No field invented that is not in field-schema.md □ status-merge and flow-recap still compatible Report validation result before finishing.`

---

## Step 7 — Generate SKILL files (Cluster C, then A)

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX STEP 7 — GENERATE CLUSTER C + A SKILL FILES Build on: all harmonization files + cluster-B output ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Read:   apex-meta/harmonization/decisions.md  apex-meta/harmonization/field-schema.md  apex-meta/harmonization/cluster-C-brief.md  apex-meta/harmonization/cluster-A-brief.md  .claude/skills/apex-sync/SKILL.md   ← just generated, do not contradict CLUSTER C — SESSION SKILL Covers: PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6 Write: .claude/skills/apex-session/SKILL.md   - Triggers: "log session", "update status", "apply deltas",               "handoff", "next session prep", "operator approve"  - Write gate: ALL file mutations must show delta proposal                to operator first. Operator types CONFIRM to apply.  - References scripts: kb_write.py (apply JSON deltas safely)  - Base: llm-wiki surgical edit + gsd-core CONTEXT.md pattern  - KB6 output file: apex-meta/handoff/next-session.md Write: apex-meta/harmonization/cluster-C-scripts-spec.md   (same format as cluster-B-scripts-spec.md) CLUSTER A — PLAN SKILL Covers: PM1, PM2, PM3, PD1, PD2, PD4 Write: .claude/skills/apex-plan/SKILL.md   - Triggers: "capture project", "decompose", "assign dependencies",               "score priority", "focus recommendation", "new epic"  - No scripts. Pure SKILL.md reasoning + file writes.  - Operator approval gate before creating any new epic or task file.  - Base: ccpm structure.md + backlog.md field schema + crewAI task contract After all files written, run final validation: □ apex-plan, apex-sync, apex-session — no shared output file    written by two skills without a defined merge rule □ All three skills use H1 enum identically □ All three skills write to H2 paths identically □ KB6 handoff format (H6) present in apex-session □ PD5 operator gate present in both apex-session and apex-plan □ apex-sync does NOT write task content (read/compute only) □ status-merge and flow-recap inputs still satisfied Report: YES/NO per checkbox. If any NO — fix before finishing.`

---

## What this flow produces

|Step|Output artifact|Location in repo|
|---|---|---|
|1|Conflict table|Chat only (no file)|
|2|7 locked decisions|`apex-meta/harmonization/decisions.md`|
|3|Field schema + task template|`apex-meta/harmonization/field-schema.md` + `task-template.md`|
|4|Integration contracts + safe sequence|`apex-meta/harmonization/integration-contracts.md`|
|5|3 cluster briefs|`apex-meta/harmonization/cluster-[A/B/C]-brief.md`|
|6|apex-sync SKILL + script specs|`.claude/skills/apex-sync/SKILL.md` + `cluster-B-scripts-spec.md`|
|7|apex-plan + apex-session SKILL + script specs|`.claude/skills/apex-[plan/session]/SKILL.md` + `cluster-C-scripts-spec.md`|

Each step is a hard gate. Step N cannot start until Step N−1's output file exists in the repo — Claude will read it at the top of the next prompt. This is what prevents the cluster-f*ck: the schema is locked before any SKILL file is written, and every generation step validates against it before finishing.