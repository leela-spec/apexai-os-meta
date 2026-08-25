# Section skeleton from locked TOC (F2-S1)

**Recommended surface:** session-local agent worker  
**Use when:** ACIM workshop outline prep; derives the ordered section list from locked content only.  
**Expected return artifact:** ordered section list with one-line purpose per section.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are drafting the skeleton of an ACIM workshop outline from locked sources.

Input: table of contents of the locked ACIM content set (IDs as provided in dispatch context from `ACIM/SSoT/index.yaml` canonical entries).

Tasks:
1. Derive the workshop arc as an ordered list of sections.
2. One line of purpose per section.
3. Mark any TOC area you had to skip with SKIP:<reason>.

Return format:

```
SECTION_SKELETON
sections:
1. <title> - <purpose line>
...
gaps: <SKIP items or "none">
```

Constraints:
- use ONLY canonical IDs; if a needed topic exists only in redirect/archive material, list it under gaps instead of using it.
- do not write prose content; structure only.
