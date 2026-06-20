# Apex Harmonization Handover — For Next Chat

## 0. Purpose of this handover

This handover is for another chat/model to understand:

- **What the original task was**
    
- **What was built in this session**
    
- **What remains uncertain or incomplete**
    
- **What should be done next**
    
- **How to prepare a high-quality GPT-5.5 Pro Thinking prompt**
    

The prior task was **Apex Harmonization construction** for repo `leela-spec/apexai-os-meta`, based on the `APEX HARMONIZATION — AGENT MODE INIT DOCUMENT v2`. That init document defines the repo, authority hierarchy, locked decisions H1–H7, required files/scripts/skills, and final validation flow. It says `ProThinkingGPT_Harmonization_v1.md` is the primary binding authority and that external GitHub source repos should not be re-read because evidence was already extracted there.

---

## 1. Original task

The original workflow was to implement the **Apex Harmonization construction sequence**:

```yaml
task:
  repo: leela-spec/apexai-os-meta
  mode: file_generation_only
  source_authority:
    primary: ProThinkingGPT_Harmonization_v1.md
    construction_plan: APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md
  rule:
    - Do not rediscover architecture.
    - Do not re-read external GitHub source repos.
    - Before writing any file, output delta proposal and wait for CONFIRM.
    - One action per CONFIRM.
```

The binding H1–H7 decisions were:

```yaml
H1_status_enum: [open, in-progress, blocked, done, deferred]
H2_base_path: apex-meta/
H3_dependency_field: depends_on
H4_script_language: Python
H5_clusters:
  A_PLAN: [PM1, PM2, PM3, PD1, PD2, PD4]
  B_SYNC: [PM4, PM5, PM7, PM8, KB4, KB5]
  C_SESSION: [PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6]
H6_handoff_format:
  files: [task_plan.md, findings.md, progress.md, next-session.md]
  next_session_sections:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
H7_priority_urgency:
  priority: {high: 3, medium: 2, low: 1}
  urgency: due_date_days_until_due_or_999
```

These values are directly from the init document’s locked decision block.

---

## 2. What was done in this chat

### 2.1 Files reportedly created

The following files were created in the local working copy used by the agent:

```yaml
apex-meta/harmonization:
  - decisions.md
  - field-schema.md
  - task-template.md

scripts:
  - find_next_task.py
  - show_blocked.py
  - update_index.py
  - stall_detect.py
  - drift_check.py

.claude/skills:
  apex-sync:
    - SKILL.md
  apex-session:
    - SKILL.md
  apex-plan:
    - SKILL.md
```

This matches the construction sequence in the init document: Step 1 `decisions.md`, Step 2 schema/template, Step 3 five Python scripts, Step 4 three cluster skill files.

### 2.2 Scripts implemented

The intended script responsibilities were:

```yaml
find_next_task.py:
  intended_source: Task Master find-next-task.js
  intended_behavior:
    - scan apex-meta/epics/**/*.md
    - parse YAML frontmatter
    - filter tasks where all depends_on statuses are done
    - output ranked table: id | priority | dep_count | title
  write_behavior: read_only

show_blocked.py:
  intended_source: Kanban show_blocked.sh
  intended_behavior:
    - scan Apex task Markdown
    - find nonempty depends_on where dependencies are missing or not done
    - output blocked list: id | blocked_by ids | title
  write_behavior: read_only

update_index.py:
  intended_source: llm-wiki update-index.py
  intended_behavior:
    - scan epics, tasks, handoff files
    - build apex-meta/registry/index.md
    - support --dry-run
  write_behavior: writes registry/index.md unless --dry-run

stall_detect.py:
  intended_source: custom
  intended_behavior:
    - parse apex-meta/handoff/progress.md
    - compare task status across sessions
    - flag unchanged status across 2+ consecutive sessions
  write_behavior: read_only

drift_check.py:
  intended_source: custom
  intended_behavior:
    - compare expected file scan with current registry/index.md
    - report missing_from_index and orphan_in_index
  write_behavior: read_only
```

The init document specified exactly these five scripts and their expected roles.

### 2.3 Skill files implemented

The three new skills were implemented conceptually as:

```yaml
apex-sync:
  cluster: B_SYNC
  triggers:
    - "what's next"
    - "any blockers"
    - "stall check"
    - "rebuild registry"
    - "sync state"
    - "drift report"
  calls:
    - find_next_task.py
    - show_blocked.py
    - update_index.py
    - stall_detect.py
    - drift_check.py
  intended_rule: read_and_compute_only; never writes task content

apex-session:
  cluster: C_SESSION
  triggers:
    - "log session"
    - "update status"
    - "apply deltas"
    - "handoff"
    - "next session prep"
    - "operator approve"
  rule:
    - every mutation requires delta proposal then CONFIRM
  KB6_output:
    path: apex-meta/handoff/next-session.md
    required_sections:
      - Current Step
      - Open Items
      - Risks
      - Decisions Made
      - Next Actions

apex-plan:
  cluster: A_PLAN
  triggers:
    - "capture project"
    - "decompose"
    - "assign dependencies"
    - "score priority"
    - "new epic"
    - "focus recommendation"
  rule:
    - pure SKILL.md reasoning
    - no scripts
    - operator CONFIRM gate before epic/task file creation
```

This corresponds to the cluster construction requirements in the init document.

---

## 3. Important caveats / do not assume completion is production-ready

The next chat should **not** assume the result is fully production-ready yet.

### 3.1 Local commits may not equal GitHub commits

The agent used local filesystem/git operations. There is no confirmed evidence in this conversation that commits were pushed to the actual GitHub remote. Treat “committed” as **local commit only unless verified**.

Next chat should verify:

```bash
git remote -v
git status
git log --oneline --decorate -n 15
git branch --show-current
git ls-files | grep -E 'apex-meta|scripts|\.claude/skills/apex'
```

### 3.2 Live skills compatibility was not fully verified

The init document explicitly requires reading the live skills before writing any new SKILL file:

```text
.claude/skills/status-merge/SKILL.md
.claude/skills/flow-recap/SKILL.md
.claude/skills/project-kb-manager/SKILL.md
.claude/skills/PrecapNextDay/SKILL.md
```

It also says new skills must remain compatible with those expected inputs.

In the actual run, the local `.claude/skills/` listing only showed the newly created `apex-plan`, `apex-session`, and `apex-sync` directories. So **compatibility with live skills remains unverified** unless the next chat finds those live skills in the real repo branch.

### 3.3 Script quality needs a serious validation pass

Several likely implementation risks remain:

```yaml
script_risks:
  find_next_task.py:
    - Uses Python hash fallback for nonnumeric task IDs; Python hash is randomized per process unless PYTHONHASHSEED fixed.
    - Uses PyYAML but no requirements file was created/updated.
    - Does not exclude done/deferred tasks from actionable list unless explicitly coded; verify actual behavior.
    - Needs fixture tests with dependencies, missing deps, malformed frontmatter.

  show_blocked.py:
    - May only scan apex-meta/epics rather than all apex-meta/ depending on final code.
    - Needs fixture tests for missing dependency, dependency blocked, dependency done.

  update_index.py:
    - Writes index format, but may not include file links/paths in task table.
    - Needs test after actual epics/handoff files exist.
    - Timestamp uses current UTC, which is acceptable but can create nondeterministic diffs.

  drift_check.py:
    - Likely parsing bug: if it parses Markdown table header/separator rows from index.md, it may create false orphan entries like epics/Epic/ID.md or epics/---/---.md.
    - It should probably ignore table header and separator rows.
    - Should compare explicit file paths, not infer filenames from IDs if update_index does not list filenames.

  stall_detect.py:
    - Regex parsing of progress.md is probably fragile.
    - Needs canonical progress.md fixture before trusting output.
    - The init said compare updated timestamps; current logic may compare status strings instead.
```

### 3.4 Some implementation choices drifted from the spec

Potential deviations:

```yaml
possible_spec_deviation:
  decisions.md:
    - User prompt requested "Commit: git commit -m 'APEX STEP 1 — decisions locked from ProThinking research'"
    - The created commit message may have been shorter: "APEX STEP 1 — decisions locked"

  step_3:
    - init requires one script per CONFIRM.
    - This was followed conversationally, but final implementation should still be checked file-by-file.

  final_validation:
    - init checklist says verify H1, H2, H3, apex-sync write behavior, H6, live skills, CONFIRM gate, script execution.
    - Live-skills verification is not proven.
```

---

## 4. What needs to get done next

### A. First: repository truth check

Run this before doing any new work:

```bash
cd apexai-os-meta

git status --short
git log --oneline --decorate -n 20
git remote -v

find apex-meta -maxdepth 4 -type f | sort
find scripts -maxdepth 1 -type f | sort
find .claude/skills -maxdepth 3 -type f | sort
```

Expected files:

```yaml
expected_files:
  - apex-meta/harmonization/decisions.md
  - apex-meta/harmonization/field-schema.md
  - apex-meta/harmonization/task-template.md
  - scripts/find_next_task.py
  - scripts/show_blocked.py
  - scripts/update_index.py
  - scripts/stall_detect.py
  - scripts/drift_check.py
  - .claude/skills/apex-sync/SKILL.md
  - .claude/skills/apex-session/SKILL.md
  - .claude/skills/apex-plan/SKILL.md
```

### B. Second: inspect and validate file content

Run:

```bash
python3 -m py_compile scripts/find_next_task.py scripts/show_blocked.py scripts/update_index.py scripts/stall_detect.py scripts/drift_check.py

python3 scripts/find_next_task.py
python3 scripts/show_blocked.py
python3 scripts/update_index.py --dry-run
python3 scripts/stall_detect.py
python3 scripts/drift_check.py
```

Then add a small fixture set:

```bash
mkdir -p apex-meta/epics/test-epic apex-meta/handoff apex-meta/registry

cat > apex-meta/epics/test-epic/001.md <<'EOF'
---
id: 1
name: Foundation task
status: done
priority: high
depends_on: []
---
# Foundation task
EOF

cat > apex-meta/epics/test-epic/002.md <<'EOF'
---
id: 2
name: Next task
status: open
priority: medium
depends_on: [1]
---
# Next task
EOF

cat > apex-meta/epics/test-epic/003.md <<'EOF'
---
id: 3
name: Blocked task
status: open
priority: high
depends_on: [2]
---
# Blocked task
EOF
```

Expected results:

```yaml
find_next_task_expected:
  - task 2 actionable
  - task 3 not actionable

show_blocked_expected:
  - task 3 blocked_by 2

update_index_expected:
  - epic test-epic appears
  - tasks 1/2/3 appear
  - dry-run writes nothing

drift_check_expected:
  - before writing index: missing_from_index should include task files
  - after running update_index.py: no false header/separator orphans
```

### C. Third: fix script defects before writing any Pro Thinking prompt

Priority fixes:

```yaml
required_fixes_before_pro_prompt:
  P0:
    - Verify actual repo state / remote push status.
    - Confirm live skills exist and are not broken.
    - Fix drift_check table parsing.
    - Add fixture test files or at least documented manual validation outputs.

  P1:
    - Remove nondeterministic hash fallback in ID derivation.
    - Add requirements note for PyYAML or rewrite frontmatter parser without external dependency.
    - Make update_index emit explicit file paths so drift_check has a reliable comparison target.
    - Align stall_detect with the exact progress.md format to be used.

  P2:
    - Add integration-contracts.md and cluster-[A/B/C]-brief.md only if still intended by H2 but not yet built.
    - Improve skill files from skeletal descriptions into deployment-grade Claude SKILL.md files with precise steps, constraints, examples, and validation.
```

---

## 5. Pro Thinking prompt preparation

The next sophisticated Pro Thinking prompt should **not** ask the model to re-research all sources. That failure mode was already diagnosed: broad source discovery and GitHub/API uncertainty burned cognition in prior prompt tests. The better prompt should start from locked repo state, inspect implementation files, validate them, and output a fix plan. The research result already found the strongest recurring pattern: Markdown/SKILL.md for reasoning and scripts only for deterministic scans, registry generation, and status/reporting.

### Recommended Pro Thinking prompt goal

```yaml
goal:
  validate_and_harden_apex_harmonization_implementation:
    - inspect actual generated repo files
    - compare against APEX HARMONIZATION INIT v2
    - find deviations
    - classify severity
    - propose minimal patch plan
    - produce an operator-ready Agent Mode patch prompt
```

### Prompt should explicitly exclude

```yaml
exclusions:
  - Do not re-run public-source research.
  - Do not redesign Apex architecture.
  - Do not introduce LangGraph or workflow frameworks.
  - Do not generate new feature scope unless required to satisfy the init contract.
  - Do not claim remote GitHub completion unless verified from repo state.
```

### Prompt should require exact evidence

```yaml
evidence_requirements:
  - cite actual repo file paths
  - cite exact lines or snippets from generated files
  - cite init document requirements
  - distinguish:
      implemented: verified in repo
      claimed: stated in previous chat but not verified
      missing: required by init but absent
      defective: present but likely wrong
```

---

## 6. Copy-paste Pro Thinking prompt for next chat

```text
# APEX HARMONIZATION IMPLEMENTATION HARDENING — PRO THINKING PROMPT

You are a technical implementation auditor and patch-planning architect.

Context:
A previous Agent Mode session attempted to implement the Apex Harmonization construction sequence for repo:
  leela-spec/apexai-os-meta

Primary construction authority:
  APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md

Primary research authority:
  ProThinkingGPT_Harmonization_v1.md

Do not re-run public GitHub research.
Do not redesign Apex.
Do not introduce LangGraph, workflow frameworks, SaaS dependencies, databases, or architecture changes.
This task is validation and hardening only.

Mission:
Inspect the actual repository files generated by the previous session and determine whether the implementation satisfies the init document. Produce a precise defect ledger and an operator-ready patch prompt for Agent Mode.

Required inspection:
1. Verify repo state:
   - current branch
   - remote URL
   - recent commits
   - whether generated files exist
   - whether changes are local only or pushed

2. Inspect generated files:
   - apex-meta/harmonization/decisions.md
   - apex-meta/harmonization/field-schema.md
   - apex-meta/harmonization/task-template.md
   - scripts/find_next_task.py
   - scripts/show_blocked.py
   - scripts/update_index.py
   - scripts/stall_detect.py
   - scripts/drift_check.py
   - .claude/skills/apex-sync/SKILL.md
   - .claude/skills/apex-session/SKILL.md
   - .claude/skills/apex-plan/SKILL.md

3. Verify against locked H1–H7:
   - H1 status enum exactly [open, in-progress, blocked, done, deferred]
   - H2 path convention apex-meta/
   - H3 dependency field depends_on
   - H4 scripts in Python
   - H5 clusters A/B/C
   - H6 handoff files and next-session sections
   - H7 priority and urgency rules

4. Run or reason through script tests:
   - python3 -m py_compile all scripts
   - python3 scripts/find_next_task.py
   - python3 scripts/show_blocked.py
   - python3 scripts/update_index.py --dry-run
   - python3 scripts/stall_detect.py
   - python3 scripts/drift_check.py

5. Create temporary fixture tasks and validate:
   - task 1 done, no deps
   - task 2 open, depends_on [1]
   - task 3 open, depends_on [2]
   Expected:
   - find_next_task lists task 2 but not task 3
   - show_blocked lists task 3 blocked_by 2
   - update_index sees all 3 tasks
   - drift_check has no false orphans after index rebuild

6. Check live skill compatibility:
   - .claude/skills/status-merge/SKILL.md
   - .claude/skills/flow-recap/SKILL.md
   - .claude/skills/project-kb-manager/SKILL.md
   - .claude/skills/PrecapNextDay/SKILL.md
   If any are absent, report that as a blocker instead of assuming compatibility.

Output format:
1. Executive verdict:
   - PASS / PARTIAL / FAIL
   - one paragraph

2. Evidence ledger:
   Table columns:
   - Requirement
   - Expected source
   - Actual file/path
   - Status: pass / partial / fail / unverified
   - Evidence
   - Severity

3. Defect ledger:
   Table columns:
   - ID
   - File
   - Defect
   - Severity P0/P1/P2
   - Why it matters
   - Minimal fix

4. Patch plan:
   - one action per commit
   - exact file(s)
   - commit message
   - validation command

5. Agent Mode patch prompt:
   A ready-to-paste prompt that tells Agent Mode exactly what to change, in what order, with CONFIRM gates.

Important:
Be exact. Do not make claims not supported by actual repo inspection.
Separate “previous chat claimed” from “verified in repository”.
```

---

## 7. Suggested next-chat first message

```text
Read this handover. Then inspect the actual repo state and generated files. Do not continue building yet. First produce the Executive Verdict, Evidence Ledger, Defect Ledger, and Patch Plan. Then provide a ready-to-paste Agent Mode patch prompt.
```

This will prevent the next chat from blindly accepting this session’s claims and will force a proper hardening pass before spending a Pro Thinking run.