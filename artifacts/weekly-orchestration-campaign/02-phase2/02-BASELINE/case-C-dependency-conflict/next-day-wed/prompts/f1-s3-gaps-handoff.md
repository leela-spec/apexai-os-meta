# Gap check and THU handoff prep (F1-S3)

**Recommended surface:** session-local agent worker  
**Use when:** end of WED sprint; verifies draft against source map and stages Thursday intake.  
**Expected return artifact:** gap list + staged handoff note with draft file path.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are closing out the WED outline sprint.

Tasks:
1. Compare the complete draft against SOURCE_MAP: every mapped section covered?
2. Collect all [GAP:] markers into a single list.
3. Classify each gap: FIX_BY_THU_NOON (source exists, was missed) | OPERATOR_DECISION (no canonical source).
4. Stage a handoff note: draft path + gap classification + what THU morning must do first.

Return:

```
THU_HANDOFF
coverage: <n_of_m sections>
gaps:
- topic: <t> | class: <FIX_BY_THU_NOON|OPERATOR_DECISION> | note
first_action_thu: <one line>
```
