---
type: Reference
id: V2-DISCUSSION-v1.0
title: Discussion & Open Threads — Operator Feedback on v0.4
description: Operator feedback on the v0.4 contract block, item by item, with analysis, draft reformulations, two new rules the suite has never had, and the research queue.
status: open_discussion
tags: [discussion, feedback, open-threads, reformulation, research-queue]
---

# Discussion & Open Threads — Operator Feedback on v0.4

**Status: nothing applied.** This file records operator feedback, my analysis of each item, draft
reformulations where I have one, and what still needs research. v0.4 in
[07-contract-block-v0.4.md](07-contract-block-v0.4.md) is unchanged.

---

## 0. A regression I introduced — found by the operator

> *"And where are all the if clauses now with the Q&A and stuff like that? They're all missing.
> What happened to them?"*

**Correct. I dropped three of them.** v0.3 had one blanket clause covering five adapters:

> `IF resolving a trade-off, comparing candidates, patching a file, writing a handover, or running
> multi-step iterative work THEN ref="execution-modes.md"`

When I split that into specific observable-action gates, three adapters lost any gate at all:

| Adapter | Live rule | v0.3 | v0.4 | Status |
|---|---|---|---|---|
| Q&A Decision Matrix | `EM-06` | ✅ blanket | ✅ `<trade_off>` | kept |
| Comparison & Bake-Off | `EM-07` | ✅ blanket | ⚠️ only inside `<trade_off>`'s `deepen_when` | **weakened** |
| Exact-Match Patch | `EM-08` | ✅ blanket | ✅ `<editing>` | kept |
| **Handover & Handoff** | `EM-09` | ✅ blanket | ❌ **none** | **lost** |
| **Iterative / MMM** | `EM-10` | ✅ blanket | ❌ **none** | **lost** |
| **Git Sync** | `EM-12` | ✅ blanket | ❌ **none** | **lost** |

This is a straightforward loss of coverage caused by replacing one broad gate with narrow ones and
not auditing what the broad gate had been carrying. The fix is three more gates, all keyed on
observable actions:

```xml
<handover when="ending a session, delegating to a subagent, or writing any handoff document"
          ref="apex-meta/informatics/execution-modes.md"
          deepen_when="the handover must carry input ledger, process, output contract and definition of done">
Do not write a handover to defer something you can resolve now with the tools you have. When a handover is genuinely needed, state what was observed, the reasoning chain, the caveats, the conclusion, and the exact commands to reproduce it.
</handover>

<iterative when="the task spans multiple modules, needs research, or cannot be finished in one pass"
           ref="apex-meta/informatics/execution-modes.md"
           deepen_when="you need the route ladder or the macro/meso/micro decomposition">
Execute a clear single-step task directly. For a multi-step task write a short preflight (target, inputs, scope, output, active step) and work step by step. For a multi-module project, create a file per step so later steps read the distilled artifact rather than re-reading sources.
</iterative>

<sync when="the operator asks to sync, synch, commit or push">
Run the git commands first, not repository analysis. Preserve every file: never drop unrelated dirty files because they are out of scope — commit them separately. On non-fast-forward, pull with rebase and retry.
</sync>
```

`<sync>` overlaps the `Git Dispatch` section kept verbatim in the blueprint. **Open question:**
keep both, or let `<sync>` replace that section? Cost ~70 tokens either way, so it is a clarity
call. My lean: let `<sync>` carry the behaviour and keep `Git Dispatch` only for the repo-specific
facts a general rule cannot know (the ext4 / `/mnt/c` constraint).

---

## 1. `<target>` — the sentence is wrong, not just wishy-washy

> *"Files, tests, schemas, checklists and metrics are evidence of success, never substitutes for
> it. This is for me very irritating… the biggest problem of the AI is that it invents flaky test
> schemas and checklists that are very bad, and then it follows these extremely bad fake test
> checklists and files and thereby creates a completely biased product."*

**You are describing a sharper failure than the sentence covers.** My wording treats all evidence
artifacts the same. Your point is that the dangerous ones are the artifacts **the agent wrote
itself** — it authors a weak test, the test passes, and the passing test replaces your actual
requirement. The operator's criteria get silently swapped for self-authored ones.

That is a different and more specific claim, and it is the one worth encoding.

You also asked for the positive form — *"work specifically with the characteristics that are
enabled and reach them"* — and for operator-given criteria to outrank environment-inferred ones.

### Draft

```xml
<target>Deliver the working result the operator specified, judged against the characteristics they
named. Those characteristics come first; anything inferred from the codebase or environment comes
second. Never invent your own acceptance criteria and then satisfy those instead — a test, schema
or checklist you wrote yourself is evidence of nothing until it is validated against the stated
requirement. Where your artifact and the operator's requirement disagree, the requirement wins.</target>
```

**What changed:** names the operator's characteristics as the measure; ranks them above
environment inference; names self-authored criteria as the specific danger rather than evidence in
general; adds a conflict-resolution rule. Four sentences, ~85 tokens (was 60).

**Still needs research** — `RP-05` below. I do not know whether "never invent your own acceptance
criteria" is the most effective phrasing, or whether a positive construction ("validate against
the stated requirement before reporting completion") outperforms a prohibition.

### On "a green check never upgrades an unfinished result"

You asked for something more specific. That line is now redundant with the stronger sentence above
and with `<product_first>`, which you said is good and which already carries *"never write a
verification script whose passing becomes the definition of done."* **My lean: delete the green-check
line from `<target>`** rather than rewrite it — the concept now has a clear owner in
`<product_first>`, and keeping it in two places is the duplication this whole effort removes.

---

## 2. `<product_first>` — keep as is

> *"this is actually good in the product first"*

No change proposed. You also identified the most important clause in it: *"a script verification
doesn't become the definition of done."* Noted as the load-bearing sentence of that rule, so it
should survive any future trim.

---

## 3. `<ground>` — add external verification

> *"always check your reasoning through verified official sources for that topic that includes the
> environment and topic context of the task at hand. Because often the AI is reasoning something
> from its own hallucinated logic instead of checking the web."*

**Agreed, and the corpus already has a better version than anything I would write.** The pilot's
`<grounding>` block:

> *"For normal factual, methodological, design, recommendation, or implementation work, search the
> web before relying on model reasoning. Ground the search in the actual frame, problem, task,
> environment, version, and constraints; use at least three verified-quality sources by default,
> prioritizing authoritative primary and established/battle-tested evidence."*

That covers exactly your point including the environment/version context. My `<ground>` only covers
grounding against repository artifacts, not against external reality — a real gap.

### Draft

```xml
<ground>Verify claims against the originating artifact (path:line) or live tool output, never memory
or a secondary summary. Any claim of absence, zero, or a count carries the exact command that
produced it. If a fact is checkable now, check it instead of deferring it. For factual, design,
version or tooling questions, consult current authoritative sources rather than reasoning from
model knowledge — ground the search in the actual environment, version and constraints at hand.</ground>
```

~100 tokens, was 74. **Open question:** the pilot specifies *"at least three verified-quality
sources by default."* A number makes it checkable but risks ceremony on trivial lookups. I left it
out; say if you want it in.

---

## 4. `<reuse>` — add modularity and name the asset classes

> *"we want to build things in a modular way and use existing skill sets, tools, scripts, software,
> then building our own"*

Agreed. My version says "an existing proven solution" abstractly, which is weak — naming the asset
classes makes it actionable.

### Draft

```xml
<reuse>Before building anything, check what already exists: repository scripts, installed tools,
established libraries, published skills. Use a fit-for-purpose option in its proven form, adapting
only the smallest necessary surface. Compose from modular parts rather than writing a monolith.
Build new only when evidence shows nothing suitable fits.</reuse>
```

~75 tokens, was 43.

---

## 5. New rule — do not be a pushover

> *"often the AI, when I say something, the AI overcorrects insanely only focuses on the new
> information whereas I am just want to clarify a little aspect. As also the AI shouldn't be a
> pushover and be very critical of what I say and what it thinks."*

**This is a genuine gap. No rule anywhere in the suite covers it** — verified by searching the
whole corpus for anti-sycophancy or push-back language. Nothing.

You are describing two related failures:

1. **Scope of correction.** You clarify one small thing; the agent rewrites everything around it.
2. **Capitulation.** You push back; the agent reverses position without new evidence.

These are measurable and well-studied. Sycophancy research finds RLHF-trained models *"systematically
reverse correct answers when users push back — not because they're confused, but because agreement
was rewarded"*, and that small system-prompt changes swing the rate by **30–40%**
([Sycophancy Tax](https://tianpan.co/blog/2026/04/10/sycophancy-tax-agreeable-llms-production),
[Sycophancy Mitigation](https://arxiv.org/pdf/2509.16742)).

The specific phrasing measured as effective is close to what you asked for:

> *"If I disagree with you without giving new evidence, do not change your answer"*

### Draft

```xml
<hold_position>When the operator pushes back without new evidence, do not reverse your position —
restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change
what was challenged and leave the surrounding work alone. State disagreement plainly when the
evidence supports it.</hold_position>
```

**Placement: unconditional.** It has to apply during a conversation, and there is no observable
action that reliably precedes capitulation — same reasoning that killed the drift gate. ~65 tokens.

**Note the overlap with `<editing>`**, which already says *"change only what was challenged."*
Failure 1 appears in both. Options: keep the editing clause for file edits and `<hold_position>` for
reasoning, or move it entirely to `<hold_position>`. **My lean: move it** — overcorrection is one
behaviour, not two, and it happens in prose as often as in files. That also answers your separate
question about extending `<surgical>`: the overcorrection guard moves out of `<editing>` into
`<hold_position>`, and `<surgical>`/`<editing>` stay purely about file mutation.

---

## 6. New rule — tonality

> *"This is also the tonality of the AI. I think this was sometimes described as the color blue…
> a scientifical very critical rational type of a style."*

**My reading, to confirm:** you mean **Cool Blue** from Insights Discovery — *"objective, detached,
cautious, analytical, precise, questioning and formal,"* people who *"want to understand the evidence
before they act, ask probing questions… and will not take anything on hearsay"*
([Insights Discovery](https://blog.insights.com/en-us/blog/your-guide-to-communicating-with-cool-blue-energy)).

If that is the referent, it maps cleanly onto `<communication>` and does not need its own tag:

```xml
<communication>Write in active voice with an explicit actor. One imperative command per sentence.
No modal hedging. State the conclusion first, then the reasoning. Report the result and the exact
unresolved blocker; compress routine tool activity. Hold a precise, analytical, evidence-first
register — no flattery, no enthusiasm padding, no agreement that has not been earned.</communication>
```

~85 tokens, was 65.

**Confirm the Cool Blue reading before this is adopted.** If you meant a different colour model, the
wording changes — several systems use blue for the opposite trait (True Colors uses blue for
relationship-oriented warmth).

---

## 7. `<surgical>` / `<editing>` — smoother condition

> *"I wonder if the editing when can be written a little bit smoother."*

Current: `when="about to modify, move, rename or delete an existing file"` — four verbs, clunky.

| Candidate | Tokens | Note |
|---|---:|---|
| `"changing a file that already exists"` | 8 | Smoothest, but loses move/rename/delete |
| `"changing, moving or deleting a file that already exists"` | 12 | **Preferred.** "Changing" absorbs rename; three verbs read cleanly |
| `"about to modify, move, rename or delete an existing file"` | 13 | Current |

**My lean: candidate 2.** With the overcorrection clause moved to `<hold_position>` (§5), the body
also shortens by ~30 tokens.

---

## 8. `<new_machinery>` — keep, but research it

> *"The new machinery looks kind of good, but I want more research on that too."*

No change proposed pending `RP-07`. It is already in the test queue as `DEC-20`, which tests whether
observable-action gates fire at all. The additional research question is narrower: whether a
*pre-action* check is the right intervention for over-building, or whether something else works
better.

---

## 9. Named tags — still want this researched

> *"at the moment what I see is that these tags are now repeated constantly, I still want this
> researched if this is the actual token efficient way."*

Fair — `<target>…</target>` writes the name twice. Candidate forms, unmeasured:

| Form | Example | Trade-off |
|---|---|---|
| Paired tags (current) | `<target>…</target>` | Clearest; name repeated |
| Attribute form | `<r id="target">…</r>` | Name appears once; less readable |
| Open-only | `<target>` … next tag implies close | Cheapest; ambiguous boundary — the exact thing tags are for |
| Bullets | `- Target: …` | 17 tokens cheaper total; you found it less clear |

`DEC-17` is already recorded as decided on clarity grounds with the cost measured at 1.3%. The open
part is whether a cheaper form keeps the clarity. Added as `RP-06`.

---

## 10. Research queue

Three new questions, to be written as prompt packets alongside the existing three in
[05-research-prompt-packets.md](05-research-prompt-packets.md).

| ID | Question | Decides |
|---|---|---|
| **RP-05** | How should an instruction prevent an agent substituting self-authored acceptance criteria for the operator's stated requirements? Is a prohibition, a positive validation duty, or an ordering rule most effective? | `<target>` wording |
| **RP-06** | Is there an XML form cheaper than paired tags that keeps unambiguous block boundaries? What is the measured parsing difference between paired tags, attribute form, and bullets at this scale? | `DEC-17` final form |
| **RP-07** | What actually reduces over-building in agents — a pre-action check, a budget, a post-hoc review, or something else? Is `<new_machinery>`'s "confirm ordinary use doesn't already surface it" the right intervention? | `<new_machinery>` |

---

## 11. Summary of proposed changes

| # | Change | Token delta | Status |
|---|---|---:|---|
| 0 | **Restore `<handover>`, `<iterative>`, `<sync>` gates** | +180 | **Regression fix — should happen regardless** |
| 1 | `<target>` rewritten around self-authored criteria | +25 | Pending `RP-05` |
| 1b | Delete the green-check line (now owned by `<product_first>`) | −15 | Ready |
| 3 | `<ground>` gains external-source verification | +26 | Ready |
| 4 | `<reuse>` names asset classes and modularity | +32 | Ready |
| 5 | **New `<hold_position>`** | +65 | Ready |
| 5b | Move overcorrection out of `<editing>` into `<hold_position>` | −30 | Ready |
| 6 | `<communication>` gains the analytical register | +20 | **Confirm Cool Blue reading first** |
| 7 | `<editing>` condition smoothed | −1 | Ready |
| | **Net** | **+302** | → block ≈ **1,659** |

That pushes the block well past the orientation again, and the blueprint to ~2,094. The trim options
in [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md) §4 become necessary rather than optional —
particularly option D, moving the 215-token infrastructure banner into the file it already declares
the source of truth.

**I am not proposing we chase ~1,000 at the cost of these rules.** Two of them (`<hold_position>`,
the `<target>` rewrite) address failures you have observed directly, which is better evidence than
a token orientation. But the growth should be a decision, not an accident — so it is stated here
rather than absorbed quietly.

---

## 12. What needs your answer

1. **Cool Blue** — is that the referent for the tonality rule?
2. **Overcorrection** — move it wholly into `<hold_position>`, or keep a copy in `<editing>`?
3. **`<sync>` vs `Git Dispatch`** — let the gate carry the behaviour, or keep both?
4. **Three sources** — should `<ground>` name a minimum source count, or stay unquantified?
5. **Growth** — accept ~1,659 and trim the blueprint elsewhere, or cut something here?
