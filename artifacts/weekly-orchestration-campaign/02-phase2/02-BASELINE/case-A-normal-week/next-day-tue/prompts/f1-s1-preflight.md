# Pre-flight schema check (F1-S1)

**Recommended surface:** session-local agent worker  
**Use when:** before the validation walk; confirms the Lika main index schema is unchanged since Monday.  
**Expected return artifact:** checklist header block: schema field list + changed/unchanged verdict.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are checking a YAML index file for schema stability.

Input: `Lika/SSoT/index.yaml` (path as provided in the dispatch context).
Reference schema fields recorded Monday: canonical_id, path, owner, status, redirect_target.

Tasks:
1. Read the index and list every top-level entry field you find.
2. Compare against the reference field set above.
3. Return EXACTLY this structure:

```
SCHEMA_CHECK
fields_found: <comma-separated list>
verdict: UNCHANGED | CHANGED
diff_notes: <one line or "none">
```

Constraints:
- Do not walk file paths; do not evaluate entries. Schema only.
- If the file cannot be read, return `SCHEMA_CHECK ... verdict: UNREADABLE` with the error.
