---
type: DesignSpecification
title: Universal AI Instruction System — Global Snippet Grammar
description: Portable grammar for tiny self-sufficient behavior instructions with optional just-in-time routing to canonical methods.
status: candidate_for_cross_model_evaluation
created: 2026-09-04
---

# Universal AI Instruction System — Global Snippet Grammar

## Decision

Use **plain, compact natural-language Markdown as the canonical snippet representation**.

Do not require XML, YAML, or JSON in the always-on surface.

A runtime adapter MAY transform the canonical text when evaluation proves that runtime-specific syntax improves behavior.

## Canonical grammar

```text
**<Behavior name>.** <Core rule in one or two direct sentences>.
If <condition requiring deeper method>, follow <canonical method/reference>.
```

The reference sentence is optional.

## Required semantic fields

Every canonical snippet must encode these meanings, even when some are implicit:

| Field | Requirement |
|---|---|
| Behavior | Short recognizable label |
| Core rule | Enough instruction to produce acceptable baseline behavior without opening another file |
| Trigger | Observable condition that changes behavior or activates deeper guidance |
| Depth route | Optional canonical method/reference when more sophistication is needed |
| Direct-task escape | Explicit or inherited rule preventing ceremony on trivial work |

Do not add metadata merely because it can be serialized.

## Size target

Default target:

- 1–4 sentences;
- roughly 20–80 words;
- one behavior only;
- one deeper reference at most from the short surface.

Longer text requires evidence that the shorter version causes material failure.

## Wording rules

1. State the behavior before the explanation.
2. Use observable triggers instead of subjective labels such as `high complexity` when possible.
3. Keep exceptions close to the rule that needs them.
4. Prefer established vocabulary.
5. Do not restate deep method content.
6. Do not require the AI to reveal hidden chain-of-thought.
7. Do not make a preflight an approval gate unless another policy requires approval.
8. Do not force research, decomposition, review, or tools on simple work.
9. Use one canonical path or method name. Avoid reference chains in the snippet.
10. Keep runtime syntax out of canonical semantics.

## Trigger grammar

Prefer concrete conditions:

```text
If the task has material ambiguity, multiple dependent parts, consequential design choices, or acceptance conditions that are not obvious, ...
```

Avoid vague conditions:

```text
If the task feels complex, ...
```

A module may define a compact trigger set in its focused method.

## Reference grammar

Preferred:

```text
Follow `apex-meta/.../method.md` when that structure is needed.
```

For a Skill-capable adapter:

```text
Use the `<skill-name>` Skill when that structure is needed.
```

The canonical module remains the semantic owner. The Skill or adapter must not silently add conflicting rules.

## Runtime without file access

The snippet must still work by itself.

If deeper guidance is needed and the runtime cannot open the canonical reference:

1. preserve the short rule;
2. inline only the focused method needed for the active task;
3. do not inline unrelated examples, evidence, or module documentation;
4. disclose that deeper repository context was not directly retrievable when this affects execution.

## XML adapter rule

XML is optional derived syntax only.

An XML adapter may use a form such as:

```xml
<behavior name="context-management">
  <rule>Keep working context to the smallest high-signal set.</rule>
  <deepen when="long_or_context_heavy">Follow the canonical context method.</deepen>
</behavior>
```

Use this only if runtime-specific evaluation shows a measurable benefit.

Never maintain separate XML semantics.

## Why the uploaded Informatics XML should not become a second owner

The uploaded `adaptive_informatics` contract correctly expresses adaptive routing and five formal rules. Those rules already exist in `apex-meta/informatics/standard.md`.

The portable short surface should therefore point to that owner rather than duplicate its rule list.

Candidate grammar example for evaluation only:

```text
**Documentation discipline.** For technical documentation, architecture specifications, or templates, use structured, concise, current-truth output and the smallest sufficient context; otherwise respond naturally. Apply `apex-meta/informatics/standard.md` when deeper formatting or conformance rules are needed.
```

This example is **not authorized for global propagation**.

## Anti-patterns

### Rulebook compression

Bad:

```text
One 250-word snippet containing six independent behaviors.
```

Reason: it hides routing and recreates context bloat.

### Empty pointer

Bad:

```text
Follow the working method.
```

Reason: the short surface is not self-sufficient.

### Duplicate method

Bad:

```text
Short snippet repeats every field, exception, and example from the deep file.
```

Reason: one concept gains multiple owners.

### Format worship

Bad:

```text
The behavior is considered correct only when expressed as XML.
```

Reason: serialization is not the behavioral method.

### Ceremony trigger

Bad:

```text
For every task, produce a preflight, plan, matrix, review, and confidence score.
```

Reason: workflow complexity must earn itself.

## Evaluation variants

For selected modules, compare at least:

1. canonical Markdown snippet;
2. same semantics rendered as compact XML;
3. short snippet without deeper reference;
4. short snippet + JIT method loading.

Measure task quality, over-processing, instruction adherence, tool-call reliability, and context cost.

Do not adopt XML globally unless it materially wins across the runtimes where it will be used.
