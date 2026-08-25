# Draft core outline sections 1-3 (F1-S1)

**Recommended surface:** session-local agent worker  
**Use when:** WED deadline sprint; writes prose for the first three workshop sections only.  
**Expected return artifact:** drafted sections 1-3 with inline canonical source IDs.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are drafting workshop outline prose for ACIM.

Input: SOURCE_MAP entries for sections 1, 2, 3 (canonical IDs from TUE mapping).

Rules:
1. Prose must cite at least one canonical source ID per paragraph.
2. Do not use redirect/archive material.
3. Match the section purposes given in the skeleton.

Return: the drafted sections followed by `COVERAGE: <sections done>/<assigned>`.

Stop: if a needed source is missing or ambiguous, write `[GAP: <topic>]` in place of the passage and continue - do not invent content.
