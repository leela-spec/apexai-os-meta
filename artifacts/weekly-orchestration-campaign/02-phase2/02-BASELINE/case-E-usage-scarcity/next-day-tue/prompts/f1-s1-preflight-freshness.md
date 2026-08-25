# Pre-flight with freshness stamp (F1-S1)

**Recommended surface:** local model (small context)  
**Use when:** quota-constrained week; schema + age stamping before any walk path.  
**Expected return artifact:** schema verdict + FRESHNESS_STAMP block.  
**Routing reference:** default-local (unverified pending operator confirmation)

## Prompt

Tasks:
1. Verify index schema fields against reference set (canonical_id, path, owner, status, redirect_target).
2. Record last-modified times of the index file and three sampled entries.

Return:

```
SCHEMA_CHECK
fields_found / verdict / diff_notes
FRESHNESS_STAMP
index_age_days / sample_ages / freshness_class: CURRENT|AGED|STALE|UNKNOWN
```
