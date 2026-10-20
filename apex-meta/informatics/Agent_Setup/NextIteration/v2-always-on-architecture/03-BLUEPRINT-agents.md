---
type: Reference
id: V2-BLUEPRINT-AGENTS-v1.0
title: BLUEPRINT — AGENTS.md With The Contract Block Integrated
description: A non-active copy of the real AGENTS.md showing what it would look like with the informatics contract block integrated, plus the line-by-line merge map and measured size.
status: candidate_not_active
tags: [blueprint, agents-md, merge-map, non-active]
---

# BLUEPRINT — `AGENTS.md` With The Contract Block Integrated

> ## ⚠️ THIS IS NOT AN INSTRUCTION FILE
>
> This is a **copy** of `AGENTS.md` made on 2026-10-20, shown with the candidate contract block
> integrated, so the merge can be reviewed before anything is changed.
>
> - The **real** [`AGENTS.md`](../../../../../AGENTS.md) is untouched and remains authoritative.
> - No agent loads this file. It is named `03-BLUEPRINT-agents.md`, not `AGENTS.md`, specifically so
>   no tool or convention picks it up.
> - The infrastructure banner from the real file is **deliberately omitted** below — it is live
>   operational state that would rot in a copy, and reproducing it here would create exactly the
>   stale-duplicate problem this whole effort exists to remove. In a real merge it stays at the top,
>   untouched.
>
> **Updated to contract v0.4.** This blueprint previously embedded v0.3. It was revised in place
> rather than copied, because a blueprint showing a superseded block is stale guidance — the exact
> failure `<current_truth>` forbids. The v0.3 block is preserved in
> [02-informatics-contract-block.md](02-informatics-contract-block.md) and in git history.

---

## 1. Merge map — what happens to each existing section

The real `AGENTS.md` is 51 lines / ~998 tokens across six sections. Measured disposition:

| Existing section | ~Tokens | Overlaps contract | Disposition |
|---|---:|---|---|
| Infrastructure banner | 190 | none | **Keep verbatim.** Live operational state, unrelated to this contract |
| **Git Dispatch** (7 rules) | 185 | none | **Keep verbatim.** Repo-specific operational knowledge — the exact `git` sequence, the ext4/`/mnt/c` constraint. Nothing in the contract covers it, and nothing should |
| **Directness** (5 rules) | 115 | `Scope`, `Target` | **Replace.** All five rules restate "take the shortest correct path, don't invent workflow, ignore unrelated dirty files" — covered by `Scope` and `Target`, plus Git Dispatch's own `Ignore` rule |
| **Core Intent Execution** (10 rules) | 240 | `target`, `scope`, `current_truth` | **Replace.** 8 of 10 are covered. `Workaround` and `Classify` are not, and are carried by the new `<recovery>` tag inside the block. `Decide` is covered by `<trade_off>` |
| **Informatics & Knowledge Routing** (2 rules) | 85 | entire `<dispatch>` + `<writing>` + `<files>` | **Replace.** This is the two-line prose pointer that the contract exists to supersede |
| **Scope** (3 rules) | 70 | `Scope` | **Replace.** Direct restatement |
| Final rule — "never describe a proposed block as applied" | 35 | partial (`Ground`) | **Keep.** It is a completion-reporting rule, sharper than `Ground`, and has clearly been earned |

### Net effect

| | Tokens |
|---|---:|
| Real `AGENTS.md` today | 998 |
| Sections kept verbatim (banner 215, Git Dispatch 185, final rule 34) | 435 |
| Sections replaced (Directness, Core Intent, Informatics Routing, Scope) | −563 |
| Contract block v0.4 added | +1,357 |
| **Blueprint total** | **~1,792** |

**+794 tokens over today, for:** conditional routing that does not exist today, writing and file
rules in reduced form that are not present at all today, an anti-machinery guard, an
operator-challenge gate, and the elimination of four sections that restate each other.

Against the ~1,000-token orientation this is **792 over** — a real cost that needs a deliberate
decision, not a shrug. Options in §4.

---

## 2. The blueprint file

Everything below the line is what `AGENTS.md` would contain. Read it as the artifact, not as
instructions to you.

---

```markdown
# Codex Operating Note

> **📍 Current architecture & open work (start here).**
> [infrastructure banner kept verbatim from the real file — omitted in this blueprint copy
>  because it is live state that must not be duplicated]

<!--
  CONTRACT BLOCK v0.4 IS INSERTED HERE VERBATIM.

  It is NOT reproduced in this blueprint on purpose. The block is owned by
  07-contract-block-v0.4.md; copying its 1,357 tokens into a second document would
  re-create exactly the drift channel this whole effort removed (see D9, and WP-23
  single-owner instruction reuse). A real merge pastes the block from its owner file.

  Structure, for orientation:
    unconditional : target, product_first, scope, communication, ground, reuse,
                    context, recovery, stop_repairing, current_truth, surgical, pointers
    gated         : editing, new_machinery, detour, authoring, trade_off, schemas
-->
## Git Dispatch
- Trigger: A request to push known files starts with the Git commands, not repository analysis.
- Sequence: Run `git add -- <requested paths>`, `git commit`, and `git push`.
- Retry: On non-fast-forward, run `git pull --rebase` and retry the push.
- Ignore: Unrelated dirty files are irrelevant and must not trigger inspection, stashing, worktrees, branches, or discussion.
- Escalate: Investigate only an actual command failure involving the requested files, validation, authentication, or merge conflicts.
- Stop: Report success immediately after the push completes.
- Filesystem: Linux agents run in ext4 workspaces (`/root/workspaces/<repo>`), never `/mnt/c` (the slow WSL 9p bridge that stalls git and causes unkillable D-state locks).

## Completion Reporting
- Rule: Never describe a proposed block as applied. Completion requires the executor's exact-match result plus the required test evidence.
```

---

## 3. What changed, line by line

| Removed | Because |
|---|---|
| `## Directness` — all 5 rules | `Scope` + `Target` + Git Dispatch `Ignore` carry all of it |
| `## Core Intent Execution` — 7 of 10 rules | `Execute`/`Target` → `Target`; `Ignore` → Git Dispatch; `Preserve` → `Surgical`; `Report` + `Current-truth` + `No-changelog` → `Current-truth` |
| `## Informatics & Knowledge Routing` — both rules | Replaced by `<writing>`, `<files>`, `<dispatch>`. The `Authority:` line pointing at `standard.md` is obsolete — `standard.md` §2 now defers to the modular suite |
| `## Scope` — all 3 rules | Direct restatement of `Scope` |

| Added | Source |
|---|---|
| 11 unconditional rule tags | Rule-of-Three extraction from the five modules |
| `<recovery>` | **Promoted** from Core Intent Execution (`Workaround` + `Classify`), covered nowhere else |
| `<authoring>` | Reduced-form file and prose rules — the real file has none today |
| `<editing>`, `<new_machinery>`, `<detour>`, `<trade_off>`, `<schemas>` | Conditional gates on observable actions — the real file has no routing at all today |

| Kept | Because |
|---|---|
| Infrastructure banner | Live state, nothing to do with this contract |
| `## Git Dispatch` entire | Repo-specific operational knowledge no general contract should absorb. The ext4/`/mnt/c` rule in particular is hard-won and machine-specific |
| Final completion rule | Sharper than `Ground`, clearly earned, cheap at 35 tokens |

**The one rule I would flag as a judgment call:** Git Dispatch's `Retry` and `Escalate` rules
arguably overlap `<recovery>`. I kept them because the git sequence is a concrete procedure, not a
principle, and because this section reads as hard-won incident knowledge. Your call.

---

## 4. Getting to ~1,000 tokens

The blueprint lands at **~1,792** — 792 over the orientation. That is a much bigger gap than the
v0.3 blueprint's 176, and it needs a real decision rather than an appeal to `<substance>`.

| Option | Saves | Cost |
|---|---:|---|
| **A.** `<trade_off>` + `<schemas>` back to one-line pointers | −160 | Both are genuinely conditional; the agent would open the module anyway |
| **B.** Trim `<authoring>` — largest block at 180, duplicates what its `ref` points at | −90 | Mild |
| **C.** Compress the 12 unconditional rules by ~20% | −130 | Lossy; each is already compressed |
| **D.** Move the infrastructure banner out of `AGENTS.md` into the file it already points at | −215 | It is live operational state that arguably belongs in `ki-basis/docs/INFRASTRUCTURE.md`, which it already names as the source of truth. **Highest value per unit of risk** |
| **E.** Move Git Dispatch to a gated file | −185 | Git operations are frequent; a gate miss means pushing without the ext4 rule. **Not recommended** |
| **F.** Drop the `<surgical>` stub | −18 | Removes gate-failure insurance. **Not until `DEC-18` resolves** |
| **A+B+D** | **−465** | **≈1,327** |
| **A+B+C+D** | −595 | ≈1,197 |
| **Accept 1,792** | — | 792 over, for capability that does not exist today |

**My lean: A+B+D → ~1,327, and accept that.** Option D is the interesting one: the banner is a
215-token pointer to `ki-basis/docs/INFRASTRUCTURE.md`, which it *already declares* to be the single
source of truth. By `<current_truth>`, a pointer that long is itself a duplicate.

Reaching a true ~1,000 would require option C or E, both of which cut substance rather than
duplication. **I would not go below ~1,200 without evidence from the read-trace test** that the
removed content was not being used.

---

## 5. Open questions on this blueprint

**Question 2 below is resolved.** See `DEC-21` in
[01-decision-register.md](01-decision-register.md) Part F2: the contract goes to **all** surfaces
that carry the shared operating rules, because that is how the operator wants every agent to work.
There are **five** instruction surfaces, not two, and three of them are already hand-maintained
copies that have measurably drifted.

1. **`.claude/CLAUDE.md` names `apex-meta/informatics/index.md` as the informatics entry point.**
   Under `DEC-14` that pointer becomes wrong — `index.md` stops being a router. It needs updating
   to point at the contract, but it is **not** a carrier of the block: it holds orchestration
   routing, a different job.
2. ~~Does the contract belong in `AGENTS.md`, `.claude/CLAUDE.md`, or both?~~ **Resolved — `DEC-21`.**
   Owner `AGENTS.md`; carriers `CLAUDE.md` and `GEMINI.md`; pointer only in `.claude/CLAUDE.md` and
   `.github/copilot-instructions.md`; byte-identity enforced by test.
3. **The infrastructure banner** must not be copied into any derivative file. The blueprint omits it
   on purpose; a real merge leaves it in place at the top. Note that this banner is **itself one of
   the already-drifted sections** between `AGENTS.md` and `CLAUDE.md`.
4. **`D10` is live and independent of this work.** `GEMINI.md` is missing the entire
   `## Informatics & Knowledge Routing` section, so Gemini agents currently receive no informatics
   routing at all. It can be fixed now without waiting for the contract.
5. **New blocker, replacing the old one:** the byte-identity test must exist *before* three copies
   of a 1,622-token block are created, not after. Creating the copies first repeats `D9` at triple
   scale.
