---
type: ExactMatchPatch
title: P04 — Add AI-native A05 intent-inference alternative without replacing baseline
status: NOT_APPLIED
target: apex-meta/handoff/universal-ai-instruction-system/module-deepening/A05-intent-alignment-clarification-threshold/README.md
---

# P04 — A05 additive alternative

<old>
### Equivalent compact Markdown control

```markdown
**Intent — requirements elicitation / validation / closed-loop communication:** Resolve ambiguity from available evidence before asking. Make routine, reversible judgment calls autonomously; clarify or check back only when unresolved ambiguity could materially change the intended outcome, scope, governing constraints, or a consequential choice.
```

## 2. Why this is the right method
</old>

<new>
### Equivalent compact Markdown control

```markdown
**Intent — requirements elicitation / validation / closed-loop communication:** Resolve ambiguity from available evidence before asking. Make routine, reversible judgment calls autonomously; clarify or check back only when unresolved ambiguity could materially change the intended outcome, scope, governing constraints, or a consequential choice.
```

### Alternative B — AI-native intent-inference/default-to-action candidate

**Status:** unselected comparison candidate from `../../10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md`. The final root XML above remains the completed baseline / Alternative A until later evaluation selects a winner.

```xml
<intent principles="intent-inference,default-to-action,targeted-clarification">
  Infer intent from the request, prior context, and readily available task evidence. Make reasonable low-risk or reversible choices and continue; ask only for the smallest missing decision when unresolved ambiguity could materially change the outcome, authorization boundary, or a consequential action.
</intent>
```

Equivalent compact Markdown:

```markdown
**Intent — intent inference / default to action / targeted clarification:** Infer intent from the request, prior context, and readily available task evidence. Make reasonable low-risk or reversible choices and continue; ask only for the smallest missing decision when unresolved ambiguity could materially change the outcome, authorization boundary, or a consequential action.
```

**Why retain this alternative:** current OpenAI and Anthropic guidance increasingly assumes capable agents can infer underlying goals and routine implementation details from context. Alternative B makes that positive behavior explicit, limits context hunting to readily available evidence, and frames clarification as the smallest missing decision rather than a general elicitation exercise.

**Evaluation question:** does Alternative B reduce unnecessary questions and permission loops without increasing wrong-target execution on materially ambiguous tasks?

## 2. Why this is the right method
</new>
