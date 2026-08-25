# Source-ID mapping (F2-S2)

**Recommended surface:** session-local agent worker  
**Use when:** after F2-S1 section skeleton exists; attaches canonical source IDs to each outline section.  
**Expected return artifact:** mapping table section -> source IDs, zero unresolved references.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are mapping canonical source IDs onto workshop outline sections.

Inputs:
- SECTION_SKELETON output from F2-S1
- `ACIM/SSoT/index.yaml` ID space

Tasks:
1. For each section, select every canonical source ID that feeds it.
2. Verify each selected ID resolves to a canonical (not redirect/archive) entry.

Return format:

```
SOURCE_MAP
sections:
- section: <title>
  sources: [<id>, <id>]
unresolved: <section names with no resolvable source, or "none">
```

Stop condition:
- any section with no canonical source goes to `unresolved`; never substitute redirect/archive IDs silently.
