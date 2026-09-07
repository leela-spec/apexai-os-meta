---
type: ExactMatchPatch
title: P01 — Add AI-native A01 alternative without replacing baseline
status: NOT_APPLIED
target: apex-meta/handoff/universal-ai-instruction-system/module-deepening/A01-target-outcome-alignment/README.md
---

# P01 — A01 additive alternative

<old>
### Equivalent compact Markdown control

```markdown
**Target — intent-preserving realization & validation:** Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; use the depth, rigor, completeness, and effort the outcome actually requires.
```

## 2. Why A01 and A09 are now one module
</old>

<new>
### Equivalent compact Markdown control

```markdown
**Target — intent-preserving realization & validation:** Realize and validate the substantive intended outcome. Treat files, tests, checklists, schemas, and metrics as evidence of success, not substitutes for it; use the depth, rigor, completeness, and effort the outcome actually requires.
```

### Alternative B — AI-native outcome-first candidate

**Status:** unselected comparison candidate from `../../10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md`. The final root XML above remains the completed baseline / Alternative A until later evaluation selects a winner.

```xml
<target principles="outcome-first,success-criteria,validation,stopping-condition,anti-proxy-optimization">
  Realize the intended useful result, not merely a named artifact or check. Treat tests, schemas, metrics, and other acceptance signals as evidence; continue until the result is substantively satisfied, then stop.
</target>
```

Equivalent compact Markdown:

```markdown
**Target — outcome first / stopping condition / anti-proxy:** Realize the intended useful result, not merely a named artifact or check. Treat tests, schemas, metrics, and other acceptance signals as evidence; continue until the result is substantively satisfied, then stop.
```

**Why retain this alternative:** current OpenAI/ChatGPT guidance emphasizes outcome-first prompting, explicit success/stopping conditions, leaner persistent instructions, and avoiding redundant process scaffolding. This version preserves the operator-critical anti-checkmark behavior while moving execution-depth language out of the target rule so A04 can own workflow depth.

**Evaluation question:** does Alternative B reduce over-analysis and context cost while preserving A01's protection against superficial file/test/checkmark completion?

## 2. Why A01 and A09 are now one module
</new>
