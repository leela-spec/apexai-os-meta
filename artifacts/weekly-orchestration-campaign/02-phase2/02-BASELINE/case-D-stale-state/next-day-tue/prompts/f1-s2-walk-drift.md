# Drift-aware validation walk (F1-S2)

**Recommended surface:** session-local agent worker  
**Use when:** after freshness-stamped pre-flight in a degraded-state week.  
**Expected return artifact:** findings list where each finding is classed ERROR or DRIFT_SUSPECTED.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

Standard SSoT validation walk with one addition:

Classification rule additions:
- If a finding could plausibly result from the index being outdated relative to disk reality (files moved/renamed after last index write), tag it DRIFT_SUSPECTED instead of its normal class.
- Definite structural errors (bad status value, duplicate listing inside the index itself) stay ERROR regardless of age.

Return format:

```
WALK_REPORT
coverage / findings lines (entry | class | note) where class includes DRIFT_SUSPECTED
drift_ratio: <suspected>/<total>
```

Stop condition: if drift_ratio exceeds 0.3 at any point, STOP early and report - bulk drift needs an operator decision, not a walk-through.
