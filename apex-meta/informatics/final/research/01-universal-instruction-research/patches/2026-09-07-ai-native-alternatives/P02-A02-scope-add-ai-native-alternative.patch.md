---
type: ExactMatchPatch
title: P02 — Add AI-native A02 autonomy alternative without replacing baseline
status: NOT_APPLIED
target: apex-meta/handoff/universal-ai-instruction-system/module-deepening/A02-scope-non-goals/README.md
---

# P02 — A02 additive alternative

<old>
### Equivalent compact Markdown control

```markdown
**Scope — scope control / non-goals:** Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
```

## 2. Why this is the right method
</old>

<new>
### Equivalent compact Markdown control

```markdown
**Scope — scope control / non-goals:** Stay within the authorized task: perform work that directly realizes or materially enables the target and respect governing constraints. Do not act on adjacent improvements, opportunistic cleanup/redesign, or speculative future work unless that broader work is explicitly authorized.
```

### Alternative B — AI-native authorization/autonomy candidate

**Status:** unselected comparison candidate from `../../10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md`. The final root XML above remains the completed baseline / Alternative A until later evaluation selects a winner.

```xml
<scope principles="authorization-mode,autonomy-boundaries,non-goals">
  Match action to the request: analysis/review/planning does not authorize implementation; change/build/fix requests authorize in-scope local changes and relevant non-destructive validation without asking. Keep incidental improvements separate and confirm before destructive, external, costly, or materially scope-expanding actions.
</scope>
```

Equivalent compact Markdown:

```markdown
**Scope — authorization mode / autonomy boundaries / non-goals:** Match action to the request: analysis/review/planning does not authorize implementation; change/build/fix requests authorize in-scope local changes and relevant non-destructive validation without asking. Keep incidental improvements separate and confirm before destructive, external, costly, or materially scope-expanding actions.
```

**Why retain this alternative:** current OpenAI guidance frames useful autonomy positively: permit safe in-scope local work and relevant non-destructive validation without repeated approval, but stop before destructive, external, costly, or materially scope-expanding actions. This gives A02 a positive execution role instead of only constraining adjacent work.

**Evaluation question:** does Alternative B reduce permission loops and under-execution without increasing scope creep or unsafe boundary crossing relative to Alternative A?

## 2. Why this is the right method
</new>
