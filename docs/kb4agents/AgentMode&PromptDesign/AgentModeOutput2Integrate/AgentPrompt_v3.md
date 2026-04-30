/agent

Use this prompt as the controlling instruction.

Repository: leela-spec/MasterOfArts

MISSION:
Produce a review-ready unified diff for exactly one existing Special Ops agent KB folder.

SELECTED_AGENT:
information_design

TARGET_FOLDER:
docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/agents/information_design/

TARGET_FILES:
1. BEST_PRACTICES.md
2. MISTAKES_FAILURES.md
3. LEARNING.md
4. AGENT_CARD.md
5. ESSENCE.md

SOURCE_INDEX:
SPECIAL_OPS_KB_BASE_BUILD_INDEX.md

PRIMARY OBJECTIVE:
Read the source index, read only the indexed sources assigned to SELECTED_AGENT, read the five existing target files, and produce one valid unified diff that improves those five files.

NON-GOALS:
- Do not create control artifacts.
- Do not create batch scope contracts.
- Do not create source claim caches.
- Do not create acceptance-test files.
- Do not create group-level artifacts.
- Do not audit all 35 files.
- Do not repair other agents.
- Do not browse the web.
- Do not commit, open a PR, or apply changes.

ITERATION RULE:
This run has exactly three phases.
After each phase, stop and return the required phase output.
Do not continue until the user replies CONTINUE.

PHASE 1 — SOURCE AND TARGET READ REPORT
Actions:
1. Read SPECIAL_OPS_KB_BASE_BUILD_INDEX.md.
2. Extract only the selected agent’s source list.
3. Read the selected agent’s indexed sources.
4. Read the five target files.

Return only:
- selected_agent
- sources_read
- target_files_read
- blockers
- proceed_recommendation

Stop after Phase 1.

PHASE 2 — PATCH PLAN
Actions:
1. For each target file, identify only the exact sections that need repair.
2. Do not draft full files.
3. Do not patch unrelated content.

Return only:
| File | Edit zones | Reason | Source basis | Risk |
|---|---|---|---|---|

Stop after Phase 2.

PHASE 3 — UNIFIED DIFF AND VALIDATION
Actions:
1. Generate one unified diff for the five target files.
2. Preserve untouched lines exactly.
3. Use valid hunk ranges.
4. Run git apply --check against the live repo state.
5. If git apply fails, fix the patch once and rerun.
6. Return final patch only if git apply passes.

Return only:
- ALL_CHANGES.patch
- git_apply_status
- files_changed
- files_not_changed
- blockers
- next_agent_recommendation

COMPLETION CRITERIA:
The task is complete only when a valid unified diff exists for the selected agent’s five files and git apply --check passes.

FAILURE RULE:
If a required primary source is missing, do not switch into control-batch mode.
Instead:
1. Patch only source-limit metadata and body caveats in the five target files.
2. Mark affected claims as blocked or provisional inside those five files.
3. Still produce a valid unified diff for the five target files if possible.