---
type: ExactMatchPatch
title: P06 — Add research-profile alternatives to program README
status: NOT_APPLIED
target: apex-meta/handoff/universal-ai-instruction-system/README.md
---

# P06 — Program README additive research-profile alternatives

<old>
- Treat the existing XML wording as a hypothesis to test, not wording to defend.
- Explicitly test whether a rule over-triggers, creates unnecessary approvals/ceremony, duplicates current model capability, or suppresses useful autonomy.
- Do not request or record hidden chain-of-thought. Use concise observable rationale, comparison tables, and scenario traces instead.

## Evaluation standard per module
</old>

<new>
- Treat the existing XML wording as a hypothesis to test, not wording to defend.
- Explicitly test whether a rule over-triggers, creates unnecessary approvals/ceremony, duplicates current model capability, or suppresses useful autonomy.
- Do not request or record hidden chain-of-thought. Use concise observable rationale, comparison tables, and scenario traces instead.

### Research-profile alternatives retained for evaluation

The AI-native-first order above is the **current default candidate**, not proof that evidence order itself should never be tested. Preserve the prior discipline-first style as an explicit comparator rather than silently deleting it from the program's conceptual history.

#### Profile A — AI-native-first

```text
current OpenAI / ChatGPT / Codex evidence
  -> independent mature-agent convergence
  -> established external discipline
  -> local synthesis
```

Use when the immediate question is how current agents should actually behave, especially where model capabilities, prompt sensitivity, context architecture, autonomy, tool use, Skills/plugins, or over-triggering may have changed recently.

#### Profile B — discipline-first comparator

```text
established external discipline / vocabulary
  -> mature agent implementations
  -> current AI-specific adaptation
  -> local synthesis
```

Retain as a comparison profile when durable domain methodology may reveal requirements, failure modes, or trade-offs that product guidance under-specifies. Do **not** treat formality or age as evidence that Profile B is superior.

#### Comparison rule

When evidence-order itself is under evaluation, run the same module/scenarios under both profiles and compare resulting behavior, wording, context cost, omissions, over-triggering, and portability. Do not silently blend the profiles and then attribute the result to either one.

## Evaluation standard per module
</new>
