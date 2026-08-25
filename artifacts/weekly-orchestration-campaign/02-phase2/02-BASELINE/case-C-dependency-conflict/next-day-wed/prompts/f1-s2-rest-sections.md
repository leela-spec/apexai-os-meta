# Draft remaining outline sections (F1-S2)

**Recommended surface:** session-local agent worker  
**Use when:** after S1 completes; writes prose for all sections beyond the first three.  
**Expected return artifact:** complete draft covering every mapped section.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are completing the ACIM workshop outline draft.

Inputs:
- S1 output (style and citation pattern to match)
- SOURCE_MAP entries for all remaining sections

Rules:
1. Same citation rule as S1: canonical IDs only.
2. `[GAP: <topic>]` placeholders where sources are missing; never invent.

Return: remaining sections + `COVERAGE: <done>/<assigned>` + list of GAP markers introduced.
