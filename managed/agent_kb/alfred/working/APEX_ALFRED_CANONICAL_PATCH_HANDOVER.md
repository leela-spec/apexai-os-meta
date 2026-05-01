# APEX_ALFRED_CANONICAL_PATCH_HANDOVER

## 0. File role

```yaml
file_id: APEX_ALFRED_CANONICAL_PATCH_HANDOVER
repo: leela-spec/apexai-os-meta
path: managed/agent_kb/alfred/working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md
status: working_handover_prompt
canonical_status: non_canonical
created_for: next_chat_continuation
purpose: hand off the remaining Alfred KB canonical patch, source/audit update, and final consistency work after corrected process-handover appendices were committed
source_branch: main
write_policy: direct_to_main_if_operator_confirms
```

This handover assumes the previous chat already corrected the invalid V/U/L/F direction and committed the working locks plus operational appendices on `main`.

The next chat must not rely on memory. It must re-read the listed files from the repo before making any patch.

---

## 1. Current committed state

The following commits are already on `main`:

| Commit | Change |
|---|---|
| `e864ed63cafe8bbf5296e9cb5eb078d175cb194f` | Corrected `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`; replaced invalid V/U/L/F model with `EVD / IMP / RSK + URG`. |
| `a93eaf69c0d5d064d4e6b04e0275da5c04631d73` | Corrected `APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md`; blocked V/U/L/F regeneration and redirected to `APPENDIX_PROCESS_HANDOVER_PRIORITY.md`. |
| `e3446b434c2141d056180f1ef0352cf100ae41df` | Updated `ALFRED_WORKFLOW_DECISION_LOCK.md`; resolved prior open questions against corrected priority model. |
| `e521881f2480422dfa1ee70c2b0307f6a3c99814` | Added `APPENDIX_PROCESS_HANDOVER_PRIORITY.md`. |
| `98179ba9cf0220a8ab6ef6d4f0f6f29fa9de7b00` | Added `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`. |
| `cd59f3aba7a2bffb50f01850b2a0b5caa6f144f8` | Added `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`. |
| `bd629dd3fd0be9989f37a404add34d8564bed455` | Added `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`. |

---

## 2. Core corrected decision

The valid model is:

```yaml
agent_handoff_metrics_v1:
  EVD: 1-100
  IMP: 1-100
  RSK: 1-100

process_handover_priority_v1:
  metrics:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
    URG: 1-100
  controls:
    readiness: ready|partial|missing_input|blocked|operator_decision_needed
    lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3
  rationale:
    impact_reason:
    urgency_reason:
    unlocks: []
    risk_note:
    next_action:
```

### 2.1 Explicitly rejected

Do not reintroduce:

- `value / urgency / leverage / fit` as canonical fields.
- 0-3 orientation scoring as the Alfred/Apex process-handover model.
- `fit` as a score.
- `leverage` as a score.
- `value` as separate from `IMP`.
- automatic P0 craft-flow assignment.
- more than four P1 craft-flow assignments per normal day.
- Session Export direct mutation of OpState.
- pattern promotion after one occurrence.

### 2.2 Field mapping

```yaml
superseded_vulf_mapping:
  value: IMP
  urgency: URG
  leverage: rationale.unlocks
  fit:
    - readiness
    - constraints
    - hard_flags
```

---

## 3. Files the next chat must read first

### 3.1 Working locks

- `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- `managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md`
- `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md`
- `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md`

### 3.2 New appendices

- `managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`

### 3.3 Canonical Alfred KB files to patch compactly

- `managed/agent_kb/alfred/ESSENCE.md`
- `managed/agent_kb/alfred/BEST_PRACTICES.md`
- `managed/agent_kb/alfred/MISTAKES.md`
- `managed/agent_kb/alfred/TEMPLATES.md`
- `managed/agent_kb/alfred/LEARNING_QUEUE.md`
- `managed/agent_kb/alfred/README.md`

### 3.4 Source/audit files to update carefully

- `managed/agent_kb/alfred/SOURCE_MANIFEST.md`
- `managed/agent_kb/alfred/COVERAGE_AUDIT.md`

### 3.5 Process references to inspect but not overwrite unless necessary

- `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- `managed/rituals/NIGHT_PLANNING_PROTOCOL.md`
- `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- `managed/knowledge/AGENT_KB_LANES.md`
- `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`

---

## 4. Remaining work

The working locks and appendices are in place. The remaining task is to compact-promote their accepted parts into canonical/supporting files without duplicating full schemas everywhere.

### Patch order

```text
1. Run no-write consistency audit.
2. Patch ESSENCE.md.
3. Patch BEST_PRACTICES.md.
4. Patch MISTAKES.md.
5. Patch TEMPLATES.md.
6. Patch LEARNING_QUEUE.md.
7. Patch SOURCE_MANIFEST.md and COVERAGE_AUDIT.md.
8. Patch README.md.
9. Run final consistency gate.
```

Patch one file per commit unless pairing `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` is explicitly cleaner.

---

## 5. Prompt 0 — bootstrap for next chat

Copy this into the next chat first:

```text
You are continuing Alfred KB integration work in `leela-spec/apexai-os-meta` on `main`.

Task:
Finish the canonical patch pass after the corrected Alfred/Apex process-handover model was committed.

Critical correction:
- Do not use `value / urgency / leverage / fit` as canonical fields.
- The valid process-handover model is `EVD / IMP / RSK + URG`, 1-100.
- `value` is absorbed into `IMP`.
- `urgency` becomes `URG`.
- `leverage` becomes `rationale.unlocks`.
- `fit` becomes readiness, constraints, and hard flags.

Read first:
- managed/agent_kb/alfred/working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md
- managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
- managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md
- managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
- managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md
- managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
- managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
- managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md
- managed/agent_kb/alfred/ESSENCE.md
- managed/agent_kb/alfred/BEST_PRACTICES.md
- managed/agent_kb/alfred/MISTAKES.md
- managed/agent_kb/alfred/TEMPLATES.md
- managed/agent_kb/alfred/LEARNING_QUEUE.md
- managed/agent_kb/alfred/SOURCE_MANIFEST.md
- managed/agent_kb/alfred/COVERAGE_AUDIT.md
- managed/agent_kb/alfred/README.md

First output, before writes:
1. What changed already.
2. What remains to patch.
3. Any contradictions found.
4. Exact file-by-file patch plan.
5. Confirmation that V/U/L/F will not be reintroduced.

Then patch directly on `main`, one file at a time, unless told otherwise.
```

---

## 6. Prompt 1 — no-write consistency audit

```text
Run a no-write consistency audit before canonical patches.

Check:
1. Working locks reject V/U/L/F and use `EVD / IMP / RSK + URG`.
2. Appendices use corrected fields only.
3. `AGENT_HANDOFF_CONTRACTS.md` remains authoritative for first-wave handoffs.
4. Session Export remains trace and does not mutate OpState.
5. Pattern learning remains candidate-first.
6. Daily Command Board does not become a giant dashboard.
7. Canonical files can be patched compactly without copying whole schemas.
8. Source/audit files can record working-lock provenance without implying canonical promotion.

Output:
- PASS/FAIL table.
- Contradictions.
- Minimal patch plan.
- Files safe to patch.
- Files not safe to patch yet.

Do not write files in this audit pass.
```

---

## 7. Patch instructions by file

### 7.1 ESSENCE.md

Patch compactly.

Add to identity/boundary doctrine:

- Alfred may use `EVD / IMP / RSK + URG` for time-sensitive process-handover priority.
- Alfred uses P0-P3 classification for Daily Command Board and process-handover routing.
- Alfred respects four-craft-flow day constraints.
- Alfred creates Daily Command Board recommendations and bounded MetaOps handoffs.
- Alfred treats Session Export as trace, OpState changes as delta candidates, and patterns as candidates until promoted.
- Alfred must not silently mutate SSOT, OpState, calendar, or canonical KB.
- Alfred must not reintroduce a second personal assistant actor or treat Leela as runtime.

Do not include full schemas.

### 7.2 BEST_PRACTICES.md

Add short practice sections:

- Process-handover priority practice: `EVD / IMP / RSK + URG`.
- Readiness/lane/hard flag use.
- P0-P3 classification practice.
- Daily Command Board practice.
- MetaOps craft-flow handoff practice.
- Session Export / OpState separation practice.
- Tracking practice.
- Pattern candidate practice.
- Rhythm profile practice.
- Weekly preview / monthly directional practice.

Must include explicit negative rules:

- Do not use weighted total scoring.
- Do not reintroduce V/U/L/F.
- Do not assign more than four P1 craft-flow items.
- Do not auto-assign P0.
- Do not let Session Export mutate OpState directly.
- Do not promote patterns without threshold.

### 7.3 MISTAKES.md

Add failure modes:

- Reintroducing V/U/L/F as second metric system.
- Treating Leela app as runtime.
- Reintroducing second current-system personal assistant actor.
- Using weighted score totals as if precise.
- Treating lane as importance.
- Ignoring hard flags.
- Assigning more than four P1 craft-flow items.
- Auto-assigning P0 without operator confirmation.
- Mutating board after operator lock.
- Putting full Session Export trace into OpState.
- Letting Session Export update OpState directly.
- Promoting patterns after one occurrence.
- Tracking mood/energy/BP-XP in Alfred v1 despite exclusion.
- Overbuilding weekly/monthly planning before daily tracking exists.
- Making the Daily Command Board a giant dashboard.

### 7.4 TEMPLATES.md

Add compact templates only, not full appendix copies:

1. Project Packet v1
2. Daily Command Board v1
3. MetaOps Craft Flow Handoff v1
4. Operator-required Session Export correction
5. OpState Delta Candidate v1
6. Tracking Record v1
7. Pattern Candidate v1
8. Weekly Preview v1
9. Monthly Direction Map placeholder

Use `EVD / IMP / RSK + URG`, readiness, lane, hard flags, and P-class where priority control is needed.

### 7.5 LEARNING_QUEUE.md

Add future candidates only:

- Full Weekly Rhythm Plan v1.1.
- Monthly Direction Map operationalization.
- Low-risk OpState auto-apply classes.
- Future Algorithm from tracking evidence.
- Future BP/XP relation.
- Future mood/energy tracking reconsideration.
- Pattern library storage structure.
- Automation of candidate detection.
- Visualization of Daily Command Board.
- Calibration of `EVD / IMP / RSK + URG` and P-class rules from real use.

Do not put already-accepted appendix content here as if it were merely a candidate.

### 7.6 SOURCE_MANIFEST.md

Update provenance and source status.

Add:

- corrected `APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- corrected `APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md`
- updated `ALFRED_WORKFLOW_DECISION_LOCK.md`
- four appendices
- relationship to `AGENT_HANDOFF_CONTRACTS.md`
- relationship to uploaded Alfred/Rhythm/Sequencing/Daily/Craft Flow source materials if directly available

Do not imply final canonical promotion merely because files exist.

### 7.7 COVERAGE_AUDIT.md

Add coverage delta:

- Validated: metric collision corrected.
- Validated: `EVD / IMP / RSK` retained.
- Validated: `URG` added only for process handovers.
- Validated: V/U/L/F rejected as canonical.
- Validated: Session Export / OpState separation preserved.
- Validated: candidate/canonical separation preserved.
- Still provisional/future: weekly full Rhythm Plan, monthly planning, Algorithm calibration, BP/XP integration, mood/energy tracking.

### 7.8 README.md

Update navigation/index:

Add the new appendices under active subordinate appendices:

- `appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md`
- `appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`
- `appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md`
- `appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md`

Add quick lookup routes:

| Need | Route |
|---|---|
| process handover priority | `APPENDIX_PROCESS_HANDOVER_PRIORITY.md` |
| Daily Command Board | `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md` |
| MetaOps craft-flow handoff | `APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md` |
| Session Export / OpState | `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md` |
| Tracking | `APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md` |
| Pattern learning | `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md` |
| Rhythm profile | `APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md` and Daily Board appendix |

---

## 8. Final consistency gate

After patches, run this gate:

```text
Verify final state:
1. Alfred-only actor rule holds everywhere.
2. Leela app is not treated as runtime.
3. V/U/L/F is absent as canonical model.
4. `EVD / IMP / RSK` remains intact for first-wave handoffs.
5. `URG` appears only as process-handover extension.
6. Appendices hold detail; canonical files remain compact.
7. Daily Command Board is usable, not bloated.
8. MetaOps handoff is bounded and not over-prescriptive.
9. Session Export remains trace.
10. OpState remains delta-candidate only.
11. Pattern learning remains candidate-first.
12. Tracking remains minimal and excludes mood/energy/BP-XP.
13. Weekly/monthly planning are not prematurely operationalized.
14. Source/audit controls reflect reality.
15. README navigation is clear.

Output:
- Final pass/fail.
- Commit list.
- Any remaining blockers.
- Next recommended action.
```

---

## 9. Expected final commit sequence

Recommended commit messages:

```text
docs: compact Alfred essence for process handovers
docs: add Alfred process handover practices
docs: add Alfred handover drift mistakes
docs: add Alfred process handover templates
docs: add Alfred future improvement candidates
docs: update Alfred source and coverage controls
docs: update Alfred KB index for process handover appendices
```

---

## 10. Stop conditions

Stop and ask the operator before patching if:

- a file already contains conflicting newer guidance;
- a patch would require changing `AGENT_HANDOFF_CONTRACTS.md` beyond a pointer/update note;
- a canonical file would need full-schema duplication to make sense;
- the next chat is tempted to revive V/U/L/F;
- source/audit files would need to claim manual sources as fully read when they were not directly read;
- canonical promotion would exceed compact doctrine and become implementation detail.

---

## 11. Handover summary

The next chat's job is not to redesign the model. The model is already corrected.

The next chat's job is to:

1. re-read the corrected working locks and appendices;
2. run a no-write consistency audit;
3. compact-promote stable parts into canonical Alfred KB files;
4. update source/audit controls;
5. update README navigation;
6. run a final consistency gate.

The critical invariant is:

```text
Preserve EVD / IMP / RSK, add URG only for process handovers, and never reintroduce V/U/L/F as canonical fields.
```
