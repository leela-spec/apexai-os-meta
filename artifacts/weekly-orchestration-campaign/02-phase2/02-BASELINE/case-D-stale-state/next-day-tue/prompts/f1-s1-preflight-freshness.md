# Pre-flight with freshness stamp (F1-S1)

**Recommended surface:** session-local agent worker  
**Use when:** degraded-state week; schema check plus explicit input-age recording before any walk.  
**Expected return artifact:** schema verdict + FRESHNESS_STAMP block.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are checking index schema AND recording input ages.

Tasks:
1. Verify schema fields against reference set (canonical_id, path, owner, status, redirect_target).
2. Record last-modified timestamps of the index file and three sampled entries.
3. Compare sample ages against today's date.

Return:

```
SCHEMA_CHECK
fields_found / verdict / diff_notes (as standard)
FRESHNESS_STAMP
index_age_days: <n or unknown>
sample_ages: <three values>
freshness_class: CURRENT | AGED | STALE | UNKNOWN
```
