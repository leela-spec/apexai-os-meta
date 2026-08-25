# Findings classification handoff (F1-S3)

**Recommended surface:** session-local agent worker  
**Use when:** after a completed WALK_REPORT exists; prepares remediation intake.  
**Expected return artifact:** classification summary: each finding tagged FIX_NOW or DEFER with one-line reason.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are classifying validation findings from a WALK_REPORT.

Classification rules:
- FIX_NOW: missing-path on canonical entries, broken redirects, duplicate listings.
- DEFER: cosmetic inconsistencies, orphan files outside current scope, anything requiring archive deletion (operator-reserved).

Return format:

```
CLASSIFICATION_SUMMARY
fix_now_count: <n>
defer_count: <n>
items:
- entry: <id> | FIX_NOW|DEFER | reason: <one line>
operator_flags: <list of items needing operator decision, or "none">
```

Constraints:
- every finding gets exactly one classification.
- archive-related items ALWAYS land in operator_flags.
