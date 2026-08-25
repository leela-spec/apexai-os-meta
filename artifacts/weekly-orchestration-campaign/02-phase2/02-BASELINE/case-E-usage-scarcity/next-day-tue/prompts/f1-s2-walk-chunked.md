# Chunked validation walk (F1-S2 - chunked fallback)

**Recommended surface:** local model  
**Use when:** operator-approved fallback for quota weeks; validates the index in bounded chunks.  
**Expected return artifact:** per-chunk findings lists + merged summary with consistency check.  
**Routing reference:** pending operator approval (CHUNKED_FALLBACK option)

## Prompt

You are validating a large index in chunks because the full context does not fit the available surface envelope.

Procedure:
1. Split index entries into consecutive chunks of at most 50 entries.
2. For each chunk apply standard walk rules (path exists, single listing, valid status, redirect targets exist).
3. After all chunks, run a cross-chunk consistency pass: duplicates ACROSS chunks, orphan files claimed by two chunks.

Return:

```
CHUNKED_WALK_REPORT
chunks: <n>
findings: <standard lines with chunk id prefix>
cross_chunk_issues: <list or none>
quality_note: "chunked execution - cross-chunk blind spots possible"
```

Stop: any unreadable chunk -> report which and stop.
