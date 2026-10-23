---
type: Reference
id: RESULTS-08-deepen-when-mechanics
title: Deepen-when condition mechanics - Findings
description: Explains whether custom depth attributes actually influence an agent to open the referenced file.
status: current
tags: [research-result, depth, rp-08]
---

# RP-08 - How does `deepen_when` actually work?

**Verdict (confidence: high on how the mechanism works; low on whether the attribute improves this repo's read decisions):** `deepen_when` is **not a switch or rule evaluated by software** in the current contract. It is a text suggestion the model can read and interpret. It may help the agent understand when the brief rule is insufficient, but there is **no identified independent experiment** showing that adding this particular attribute improves file-reading decisions compared with `when` + `ref` alone. **Default recommendation: drop the extra attribute from the candidate until a read-trace A/B proves it changes behavior beneficially**, preserving any truly necessary escalation conditions in normal prose. The claimed saving is **99 tokens according to the candidate's own ledger, not independently retokenized**.

## Part 1 - Plain-language explanation

Imagine giving someone a quick rule on a sticky note: **"When writing a governed document, use these basic rules. The complete handbook is at `index.md`. Open the handbook if you need exact frontmatter requirements."**

The person's choice to open the handbook is not decided by the sticky note itself. They read the note, judge whether the task needs those details, and decide to fetch the book. An AI coding agent works similarly. Its model sees the words inside the tag, including `deepen_when`, and may decide to call a `Read` tool. **There is no automatic condition checker simply because the text looks like XML**. If the agent's actual tool/runtime explicitly interprets an attribute, that is different; no such parser has been identified in the candidate's setup.

Three meanings:

- **`when`**: "For which tasks does this abbreviated rule apply?"
- **`ref`**: "Where is the full reference if I need it?"
- **`deepen_when`**: "What missing detail would justify reading the full reference?"

The last is **a second subjective judgment**, not a guarantee. An agent may open the full file for safety, skip it because the summary sounds sufficient, or misread the scope. A native path-scoped rule or skill loader may provide a better-defined activation mechanism, but it still does not guarantee the model uses all loaded instructions correctly. [Claude](https://code.claude.com/docs/en/memory); [Cursor](https://docs.cursor.com/context/rules-for-ai); [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills).

## Evidence

| Claim | Source link | Evidence type | Supports / undermines |
|---|---|---|---|
| Coding agents can respond to repo instructions, yet context files may increase exploration/cost without improving task success. | [Gloaguen et al. 2026](https://arxiv.org/abs/2602.11988) | Controlled coding-agent benchmark | Supports that prose conditions could influence behavior, but undermines assumption of efficient selection |
| Coding-agent instruction adherence depends on task; measured file-architecture changes did not produce detectable controlled differences in tested conditions. | [McMillan 2026](https://www.alphaxiv.org/abs/2605.10039) | Controlled factorial coding-agent study | No direct evidence for depth attribute |
| The candidate explicitly defines `deepen_when` as one of its text attributes and gives it a reported 99-token cost. | [`09-contract-block-v0.5.md`, sections 2 and 4](09-contract-block-v0.5.md) | Repository source and reported size measurement | Establishes the hypothesis and cost, not its effect |
| Vendor-native scope and conditional activation mechanisms exist; unlike XML text, Cursor's `globs` and Claude's rule `paths` have loader-defined behavior. | [Cursor rules](https://docs.cursor.com/context/rules-for-ai); [Claude memory](https://code.claude.com/docs/en/memory) | Vendor documentation | Supports distinction between interpreted text and runtime gate |

## Part 2 - Variant comparison

| Variant | Token consequence | Expected behavior (hypothesis) | Evidence |
|---|---|---|---|
| `when` + `ref` + `deepen_when` | Baseline v0.5: **1,622 tokens** | Provides explicit extra reason to read; may reduce under-reading or cause over-reading depending wording | **No direct controlled evidence** |
| `when` + `ref`, remove `deepen_when` | **1,622 - 99 = 1,523**, according to repo ledger | The model must judge necessity from task and summary; fewer competing conditions | Numeric claim from [`09`](09-contract-block-v0.5.md); behavior untested |
| `when` + `ref`, short natural-language instruction in rule body | **TBD**; would recover some, not necessarily all, of the 99 tokens | Equivalent semantic intent in clearer language; may be easier to understand | No matched experiment |
| `ref` alone, no predicate/depth | **TBD** (removes both attribute classes; no source measurement) | Likely more speculative opening because the link appears relevant to many tasks, but not proven | No matched experiment |

**Suggested shortest *behavior-preserving* formulation for testing**, not an instruction change: `Read ref only if exact frontmatter/schema detail is needed.` In the actual `<authoring>` tag, the exact triggering condition should be measured against simply keeping the existing `ref=` and inline rules. Do not claim the test sentence costs fewer tokens until tokenized.

### Source integrity correction: count mismatch

A direct inspection of the literal XML in [`09-contract-block-v0.5.md`](09-contract-block-v0.5.md), fetched from `main` on 2026-10-20, finds **five `deepen_when=` attributes**: `<editing>`, `<authoring>`, `<trade_off>`, `<handover>`, and `<iterative>`. The handover and `RP-08` introduction say **six**, and `RP-09`'s copy-paste prompt says **nine**. These counts cannot all describe current v0.5. Treat the **99-token saving as an unreplicated author estimate** and remeasure on the five actual fields with the correct tokenizer before treating it as verified.

## Part 3 - Failure modes

- **Opens on every task:** `ref` is so enticing that the depth condition is ignored; the intended benefit collapses.
- **Never opens when needed:** summary sounds complete, causing agent to miss schema or repair details.
- **Wrong reason:** another rule or repository cue triggers reading, so an observed read cannot be attributed to `deepen_when` without matched controls.
- **Multiple independent triggers:** an attribute and prose both suggest opening, making it impossible to know which mattered in an uncontrolled run.

There are **no credible measured rates** for the above specific attribute behaviors in the evidence reviewed.

## Strongest case against dropping it

For schema authoring and nontrivial edits, there may be a genuine two-threshold requirement: the reduced rule applies to many tasks, while the precise schema or multi-block patch protocol is needed only rarely. Explicitly naming that second threshold could spare thousands of tokens on routine tasks or prevent a costly under-read. The potential saved downstream work may greatly exceed its 99-token cost. Because prompts can influence tool use, deleting it *before* measurement could remove a high-value cue. This is why the recommendation is **a tested simplification, not an irreversible deletion**.

## What I could not find

- A published test isolating `deepen_when` from `ref` across controlled coding-agent tasks.
- A measured under-/over-read percentage for any of the four variants.
- An official parser in this repo that acts on `deepen_when`.
- Tokenizer-verifiable support that the 99-token figure applies to **five** attributes in the current actual XML rather than the claimed six or nine.

## Consequence for the contract

- **`deepen_when`: UNVERIFIED utility**, 99-token **claimed** size opportunity. Prefer `when+ref` in a comparison candidate, not a live edit.
- `DEC-16` and `DEC-M2` remain unconfirmed, as already found in `RP-01`.
- `RP-06` must compare syntax *and* semantics under matched model, task and tool version, without assuming the custom XML attributes are execution directives.
