---
type: Runbook
id: RUNBOOK-HANDOVER-PRE-ROLLOUT-ADHERENCE-TEST-v1.0
title: Pre-Rollout Adherence Test — do agents actually apply the informatics principles?
description: Runnable handover for one chat that spawns subagents under the v1.0-ultra contract and measures whether they apply the informatics design principles, before the 5-environment rollout commits to them.
status: current_truth
tags: [handover, runbook, test, adherence, pre-rollout, falsification, subagents]
---

# Handover: Pre-Rollout Adherence Test

> **Run this before `RUNBOOK-MULTI-ENV-INTEGRATION-v1.0`.** That runbook deploys the contract to
> five environments. This one answers the question the rollout assumes: *when an agent has the
> contract, does it actually apply the principles — or does it behave the same as an agent
> without it?*
>
> **Related, already designed:** [`04-empirical-test-protocol.md`](../../candidates/04-empirical-test-protocol.md)
> (`status: design_not_run`) is the 16-task, 9-arm read-trace protocol for the narrower question
> of whether `IF/THEN` gates prevent file reads. This handover is the cheaper precursor: one chat,
> one afternoon, behavioural rather than read-trace. Run this first; escalate to that if this is
> ambiguous.

---

## 1. Input

Spawn subagents with and without the informatics instructions, give them tasks whose correct
answer differs depending on whether a principle was applied, and record which arm applied it.

## 2. Sources

- [`specs/apex_contract_v1.0_ultra.xml`](../../specs/apex_contract_v1.0_ultra.xml) — the 23 tags under test.
- [`specs/file-architecture.md`](../../specs/file-architecture.md) — `FA-01`, `FA-10`, `FA-12`, `FA-13`.
- [`specs/writing-profile.md`](../../specs/writing-profile.md) — `WP-23` single-owner reuse.
- [`13-INSTRUCTION-ADHERENCE-FIELD-EVIDENCE-HANDOVER.md`](../13-INSTRUCTION-ADHERENCE-FIELD-EVIDENCE-HANDOVER.md) — the n=1 observational data this test is designed to replace with something controlled.

## 3. Process

**Reasoning framework: two-arm controlled comparison with pre-registered predictions.** Write the
predictions in §6 **before** running anything, so a result cannot be rationalised afterwards.

**Arms.** Four subagents per task, same model, same prompt text:

| Arm | Receives |
|---|---|
| **A — control** | task only |
| **B — contract** | task + the `<apex_contract>` block |
| **C — contract + modules** | task + contract + the `specs/` files pasted in |
| **D — contract + pointer** | task + contract, modules present on disk but only referenced by `ref=` |

**A vs B** measures whether the contract changes behaviour at all. **C vs D** measures whether a
`ref=` pointer is honoured — the `RP-01` question, which no controlled test has yet answered.

**Tasks.** Each must have a *wrong* default answer that a principle corrects, and a binary
observable outcome. Six are enough:

| # | Task | Principle under test | Observable |
|---|---|---|---|
| 1 | "Write a spec file for feature X." | `FA-13` inline bracket lists | frontmatter uses `tags: [a, b]`, not multiline dashes |
| 2 | "Document why this rule changed." | `FA-01` history to `log.md` | history goes to a changelog, not inline |
| 3 | "Add a rule that already exists in another file." | `WP-23` reference, don't restate | references the owner instead of copying |
| 4 | "Write a long rules file." | `FA-10` Information Mapping | labelled sections and bullets, not narrative |
| 5 | "This number looks wrong — is it?" | `<ground>` command-carrying claims | states the command that produced the number |
| 6 | "Build a helper for a case that occurs once." | `<product_first>` / `<new_machinery>` | declines, or names the failure first |

**Rules for the runner.** One task per subagent, no conversation. Score each outcome **yes/no by
reading the artifact**, never by asking the agent whether it followed the rule — self-report is
the thing this test exists to avoid.

## 4. Skills

None. Subagent spawning plus a scratch directory. No framework.

## 5. Output

A results table at `operations/14-ADHERENCE-TEST-RESULTS.md`: 6 tasks × 4 arms, yes/no per cell,
with the artifact path for every cell so any claim can be re-read.

## 6. Redraft — the shape of the result, and the pre-registered predictions

```markdown
# Adherence test results — <date>

## Scores
| Task | Principle | A control | B contract | C +modules | D +pointer |
|---|---|:-:|:-:|:-:|:-:|
| 1 | FA-13 inline lists | no | yes | yes | no |
...
Totals: A 1/6 · B 4/6 · C 6/6 · D 4/6

## Pre-registered predictions, and whether they held
- Predicted B > A by at least 3 of 6. HELD / FAILED.
- Predicted C > D, because a ref= is honoured less often than inlined text (RP-01). HELD / FAILED.
- Predicted D ≈ B, because a pointer adds nothing the contract did not already carry.

## Decision
- B ≈ A  -> the contract is not changing behaviour. Do not roll out; fix the carrier first.
- C >> D -> gates are not honoured. DEC-16's split-file architecture needs revisiting.
- C ≈ D  -> pointers work. Roll out as designed.
```

**Assumption to check before trusting any of it:** that each arm actually received what it was
meant to. Verify by asking each subagent, as its first action and with no tools, to echo one
marker string from its own context. An arm that silently received nothing produces a clean,
meaningless null.

---

## 7. Why this is worth running before the rollout

The rollout writes the contract into five environments. If the contract does not change behaviour,
that is five places to maintain for no effect — and the existing evidence is **one uncontrolled
observational session** (`13-INSTRUCTION-ADHERENCE-FIELD-EVIDENCE-HANDOVER.md`) in which
deterministic checks caught 7 violations, operator correction caught 5, and prose rules caught 0.

That n=1 finding is suggestive and explicitly not conclusive. This test is the cheapest way to
make it conclusive, and it is cheaper to run than the rollout is to reverse.
