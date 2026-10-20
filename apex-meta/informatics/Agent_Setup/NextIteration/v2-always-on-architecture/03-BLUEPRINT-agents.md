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

---

## 1. Merge map — what happens to each existing section

The real `AGENTS.md` is 51 lines / ~998 tokens across six sections. Measured disposition:

| Existing section | ~Tokens | Overlaps contract | Disposition |
|---|---:|---|---|
| Infrastructure banner | 190 | none | **Keep verbatim.** Live operational state, unrelated to this contract |
| **Git Dispatch** (7 rules) | 185 | none | **Keep verbatim.** Repo-specific operational knowledge — the exact `git` sequence, the ext4/`/mnt/c` constraint. Nothing in the contract covers it, and nothing should |
| **Directness** (5 rules) | 115 | `Scope`, `Target` | **Replace.** All five rules restate "take the shortest correct path, don't invent workflow, ignore unrelated dirty files" — covered by `Scope` and `Target`, plus Git Dispatch's own `Ignore` rule |
| **Core Intent Execution** (10 rules) | 240 | `Target`, `Scope`, `Current-truth`, `Substance` | **Partially replace.** 7 of 10 are covered. 3 are not: `Workaround` (resolve incidental failures with the narrowest safe alternative), `Decide` (resolve low-stakes choices with a default rather than gating delivery), `Classify` (stop only for a genuine blocker). Those three are **promoted into `<always>`** |
| **Informatics & Knowledge Routing** (2 rules) | 85 | entire `<dispatch>` + `<writing>` + `<files>` | **Replace.** This is the two-line prose pointer that the contract exists to supersede |
| **Scope** (3 rules) | 70 | `Scope` | **Replace.** Direct restatement |
| Final rule — "never describe a proposed block as applied" | 35 | partial (`Ground`) | **Keep.** It is a completion-reporting rule, sharper than `Ground`, and has clearly been earned |

### Net effect

| | Tokens |
|---|---:|
| Real `AGENTS.md` today | 998 |
| Sections kept verbatim (banner, Git Dispatch, final rule) | 410 |
| Sections replaced (Directness, Core Intent, Informatics Routing, Scope) | −510 |
| Contract block added | +721 |
| Three promoted rules from Core Intent Execution | +45 |
| **Blueprint total** | **~1,176** |

**+178 tokens over today, for:** conditional routing that does not exist today, writing and file
rules in reduced form that are not present today at all, and the elimination of four sections that
restate each other.

Against your ~1,000-token target this is **176 over**. Options in §4.

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

<apex_contract v="0.3">

<always>
Target: realize the substantive outcome asked for. Files, tests and schemas are evidence of success, never substitutes for it.
Scope: do only the authorized task. No adjacent cleanup, redesign or speculative work.
Surgical: never rewrite a whole existing file. Edit by exact-match replacement. Move files with git mv/cp, never by regenerating content.
Context: load just-in-time. Never bulk-read directories or long manuals upfront. Materialize each iteration's output to a file.
Substance: technical correctness overrides every numeric target below. Exceed any ceiling when adherence would omit load-bearing context or break accuracy.
Ground: verify claims against the originating artifact (path:line) or tool output, never memory or a secondary summary. Absence and count claims carry their command.
Reuse: prefer an existing proven solution in its established form. Invent only when evidence shows nothing suitable fits.
Two-strike: if two fixes to one subsystem fail to advance the product, stop and change approach.
Current-truth: state active truth only. History goes to a changelog, never inline.
Parsimony: ~30-50 directives max per instruction file. Split a domain out before a file becomes a rule-wall.
Workaround: resolve incidental failures with the narrowest safe, intent-preserving alternative and continue.
Decide: resolve low-stakes procedural choices with a reasonable default instead of gating delivery.
Classify: stop only for a genuine target, safety, authorization, or integrity blocker.
</always>

<writing when="producing_prose_docs_or_rules" ref="apex-meta/informatics/writing-profile.md" deepen_when="ranking_tags_or_information_mapping">
Active voice, explicit actor. One imperative command per sentence. No modal hedging. Conclusion first, then rationale. ~20-word procedural, ~25-word descriptive sentences. Tables for multi-attribute comparison, bullets for inventories, numbered lists only for sequences. Durable IDs (WP-01) carry no priority tier. Tag governed rules [P0-P3 | I/E/R] on 1-100, never aggregated. Link files you list so the reader can open them.
</writing>

<files when="creating_or_restructuring_governed_files" ref="apex-meta/informatics/file-architecture.md" deepen_when="five_planes_or_bundle_layout">
Flat YAML frontmatter only, every line has a colon, inline [brackets] for lists, never multiline dashes. Concept files declare type, id, title, description, status. Bundle roots declare okf_version "0.2". One responsibility per file. Front-load P0 rules in the first ~500 tokens; close on the failure-mode guard.
</files>

<dispatch>
IF resolving a trade-off, comparing candidates, patching a file, writing a handover, or running multi-step iterative work THEN ref="apex-meta/informatics/execution-modes.md"
IF work is drifting into ceremony, orchestration or test infrastructure instead of the product THEN ref="apex-meta/informatics/anti-drift-rules.md"
IF validating schemas, patch intents, or bundle conformance THEN ref="apex-meta/informatics/governance-schemas.md"
Paths are just-in-time pointers. Do not expand them into context unless the condition matches.
</dispatch>

</apex_contract>

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
| `<always>` 10 lines | Rule-of-Three extraction from the five modules |
| `<always>` 3 further lines — `Workaround`, `Decide`, `Classify` | **Promoted** from Core Intent Execution; genuinely not covered elsewhere |
| `<writing>`, `<files>` | Reduced-form rules, new capability — the real file has none today |
| `<dispatch>` | Conditional routing, new capability — the real file has none today |

| Kept | Because |
|---|---|
| Infrastructure banner | Live state, nothing to do with this contract |
| `## Git Dispatch` entire | Repo-specific operational knowledge no general contract should absorb. The ext4/`/mnt/c` rule in particular is hard-won and machine-specific |
| Final completion rule | Sharper than `Ground`, clearly earned, cheap at 35 tokens |

**The one rule I would flag as a judgment call:** Git Dispatch's `Retry` and `Escalate` rules
arguably overlap `<always>` `Workaround`. I kept them because the git sequence is a concrete
procedure, not a principle, and because this section reads as hard-won incident knowledge. Your
call.

---

## 4. Getting to ~1,000 tokens

The blueprint lands at ~1,176. Three ways down, measured:

| Option | Saves | Cost |
|---|---:|---|
| **A.** Move Git Dispatch to a gated on-demand file (`IF the task is a git push THEN ref=...`) | −185 | Git operations are frequent; a gate miss means an agent pushes without the ext4 rule. **Not recommended** |
| **B.** Drop the 3 promoted Core Intent rules (`Workaround`, `Decide`, `Classify`) | −45 | They are the only three not covered by the contract. Losing them loses real behavior |
| **C.** Tighten `<always>` wording — the 13 lines average 27 tokens each and several carry explanatory clauses | ~−90 | Lossy; each line is already a compression |
| **A+B+C** | −320 | ~856 tokens |
| **Accept 1,176** | — | 176 over target, in exchange for routing and writing/file rules that do not exist today |

**My lean: accept ~1,176.** The ~1,000 figure is an orientation, not a wall — `Substance` in the
contract itself says so. The alternative is cutting operational knowledge that was earned from
incidents. If you want it under 1,000, **C then B**, never A.

---

## 5. Open questions on this blueprint

1. **Does `.claude/CLAUDE.md` also need updating?** It carries its own 1,028 tokens of orchestration
   routing and names `apex-meta/informatics/index.md` as the informatics entry point. Under `DEC-14`
   that pointer becomes wrong — `index.md` stops being a router. **Not addressed here.**
2. **Does the contract belong in `AGENTS.md`, `.claude/CLAUDE.md`, or both?** They are loaded by
   different tools. Duplicating the block across both would recreate exactly the two-copies problem
   this effort removed. Needs a decision before installation.
3. **The infrastructure banner** must not be copied into any derivative file. The blueprint omits it
   on purpose; a real merge leaves it in place at the top.
4. **Rule 2 above is the blocker.** Installing into one file while the other still points at
   `index.md` leaves two different stories about where informatics rules live.
