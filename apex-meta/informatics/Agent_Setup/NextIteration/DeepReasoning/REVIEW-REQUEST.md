---
type: Reference
id: DR-REVIEW-REQUEST-v1.0
title: Independent Review Request — Canonical Ownership Pass
description: Operator control packet for independently reviewing the Apex Informatics canonical-ownership pass, with GitHub paths, a copy-paste reviewer prompt, and exact revert commands.
status: current
tags: [review, verification, control, rollback]
---

# Independent Review Request — Canonical Ownership Pass

**State:** the patches are **applied, committed, and pushed to `main`**. They are not a proposal
sitting in a buffer — they are live. This document exists so you can verify them independently and
revert cleanly if review rejects them.

**Repository:** `leela-spec/apexai-os-meta` · branch `main`

## 1. The three commits

| Commit | Contents | Risk |
|---|---|---|
| [`6b7f54ee`](https://github.com/leela-spec/apexai-os-meta/commit/6b7f54ee) | Baseline snapshot — the suite exactly as it was before any change | None (rollback anchor) |
| [`53d969c0`](https://github.com/leela-spec/apexai-os-meta/commit/53d969c0) | Research tree only — 13 new files, no live file touched | None (additive) |
| [`f925be40`](https://github.com/leela-spec/apexai-os-meta/commit/f925be40) | **The patches under review** — 10 files changed | **This is what to review** |

**Full change in one view:**
<https://github.com/leela-spec/apexai-os-meta/compare/6b7f54ee...f925be40>

## 2. Revert commands

The split is deliberate: you can drop the patches and keep the research.

```bash
# Revert ONLY the live-file patches; keeps the research tree
git revert --no-commit f925be40 && git commit -m "revert: canonical ownership pass pending review"

# Or inspect first, revert nothing
git diff 6b7f54ee..f925be40 -- apex-meta/informatics/

# Restore a single file to its pre-change state
git checkout 6b7f54ee -- apex-meta/informatics/governance-schemas.md
```

## 3. Files changed — GitHub paths

All links point at the **current** state on `main`. Append `?plain=1` to any blob URL to see raw
Markdown instead of rendered.

### Live specification files (the substance of the review)

| File | Δ | What changed |
|---|---:|---|
| [`apex-meta/informatics/governance-schemas.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/governance-schemas.md) | **+46 / −176** | 93-line JSON schema copy removed; frontmatter + Q&A + tier blocks removed; `GS-16/18/19` retired |
| [`apex-meta/informatics/file-architecture.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/file-architecture.md) | +25 / −43 | `FA-04` collision fixed → `FA-13`; topology tree corrected; §5/§6 collapsed |
| [`apex-meta/informatics/writing-profile.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/writing-profile.md) | +31 / −17 | Gains tier table + `WP-23/24/25`; §4/§5 swapped |
| [`apex-meta/informatics/index.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/index.md) | +11 / −6 | `tags` added; §3 compressed to rule ranges |
| [`apex-meta/informatics/anti-drift-rules.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/anti-drift-rules.md) | +7 / −7 | Canonical markers; `AD-27` links relativized |
| [`apex-meta/informatics/execution-modes.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/execution-modes.md) | +3 / −3 | Canonical markers; §4.2 preamble |
| [`apex-meta/informatics/standard.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/standard.md) | +4 / −3 | §2 precedence ladder only — body untouched |
| [`apex-meta/informatics/general-informatics-router.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/general-informatics-router.md) | **0** | Byte-identical to baseline, by design |

### Agent instruction surface (outside the bundle — check this one carefully)

| File | Δ | What changed |
|---|---:|---|
| [`.claude/rules/informatics.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/rules/informatics.md) | +3 / −3 | Routes through the `<informatics>` gates; names the modular suite as owner of local profile rules |

### Tests

| File | Δ | What changed |
|---|---:|---|
| [`apex-meta/informatics/tests/test_canonical_ownership.py`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/tests/test_canonical_ownership.py) | +224 / −0 | **New** — 4 guard classes, 11 tests |
| [`apex-meta/informatics/tests/test_tier5_adversarial.py`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/tests/test_tier5_adversarial.py) | +27 / −6 | **One assertion rewritten** — `test_tas_02` |

### Research record (read-only context for the reviewer)

Root: [`apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/`](https://github.com/leela-spec/apexai-os-meta/tree/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning)

| File | Purpose |
|---|---|
| [`index.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/index.md) | Navigation + rule→research cross-reference |
| [`00-master-matrix.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/00-master-matrix.md) | 96-rule audit matrix, defect register D1–D9 |
| [`01-system-wide-overlap-and-token-audit.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/01-system-wide-overlap-and-token-audit.md) | Ownership map, token scorecard, D9 analysis |
| [`02-new-rules-discovery-and-qa-bakeoff.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/02-new-rules-discovery-and-qa-bakeoff.md) | 8 decision matrices, web research, the 3 new rules |
| [`03-research-backlog-and-open-questions.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/03-research-backlog-and-open-questions.md) | `RBL-01..08` deferred items |
| [`04-consolidated-patch-and-verification.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/04-consolidated-patch-and-verification.md) | 25-entry patch ledger, scorecard, forensic report |
| [`modules/M01-routers-and-index.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/modules/M01-routers-and-index.md) | Router/index/authority record |
| [`modules/M02-writing-profile.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/modules/M02-writing-profile.md) | `WP` record |
| [`modules/M03-file-architecture.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/modules/M03-file-architecture.md) | `FA` record |
| [`modules/M04-execution-modes.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/modules/M04-execution-modes.md) | `EM` record |
| [`modules/M05-anti-drift-rules.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/modules/M05-anti-drift-rules.md) | `AD` record |
| [`modules/M06-governance-schemas.md`](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/modules/M06-governance-schemas.md) | `GS` record — the largest change |

## 4. Your 10-minute control check

Run these yourself before trusting any reviewer, AI or human. Each is one command with a
pass/fail answer.

```bash
git fetch origin && git checkout main && git pull
```

| # | Command | Expected |
|---|---|---|
| 1 | `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` | `OKF Errors: 0 \| Apex Profile Errors: 0` |
| 2 | `python -m pytest apex-meta/informatics/tests/ -q` | `196 passed` |
| 3 | `git checkout 6b7f54ee -- apex-meta/informatics/ && python -m pytest apex-meta/informatics/tests/ -q` | Baseline still green — then `git checkout main -- apex-meta/informatics/` to undo |
| 4 | `git diff 6b7f54ee..HEAD --stat -- apex-meta/informatics/*.md .claude/` | Only the 8 files in §3 changed, nothing else |
| 5 | `git diff 6b7f54ee..HEAD -- apex-meta/informatics/general-informatics-router.md` | **Empty** — proves the router is untouched |

Check 3 matters most: it proves the tests were not rewritten to fit the patches. If the baseline
suite passes under the new test file, the guards are measuring real invariants.

## 5. Copy-paste prompt for an independent AI reviewer

Give the reviewer repository access, then paste this verbatim. It is written to make the reviewer
adversarial rather than agreeable.

---

> You are an independent reviewer. Another AI modified a specification suite in the GitHub
> repository `leela-spec/apexai-os-meta`, branch `main`. **Your job is to find what it got wrong,
> not to confirm it.** Assume its self-reported findings may be overstated or fabricated until you
> verify each one against the actual files.
>
> **The change:** `git diff 6b7f54ee..f925be40`
> **Its own claims:** `apex-meta/informatics/Agent_Setup/NextIteration/DeepReasoning/04-consolidated-patch-and-verification.md`
>
> Verify each item independently. For every one, answer CONFIRMED / OVERSTATED / FALSE and cite
> `path:line` from the files themselves — never from the agent's own research documents, which are
> the thing under review.
>
> **A. Were the claimed defects real?**
> 1. `D1` — did `apex-meta/informatics/file-architecture.md` at commit `6b7f54ee` really define
>    `FA-04` twice, for two unrelated rules?
> 2. `D9` — this is the central claim. At `6b7f54ee`, `governance-schemas.md` embedded a JSON
>    Schema. Compare it to `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json`.
>    Did the embedded copy really omit `maxLength` bounds the authoritative file enforces? Parse
>    both as JSON and diff them. If the claim is true, the published contract was weaker than the
>    enforced one — confirm or refute that specific consequence.
> 3. `D2` — did `file-architecture.md` and `governance-schemas.md` really publish contradictory
>    frontmatter contracts (`tags`, `version`)? Does the new merged contract match what
>    `apex-meta/scripts/okf_validator.py` actually enforces? Read the validator source.
> 4. `D4`, `D3`, `D6`, `D7` — verify each at `6b7f54ee` the same way.
>
> **B. Did the fixes lose anything?**
> For each block deleted from `governance-schemas.md`, confirm the content survives in the file
> named as its new owner. Specifically: do the priority-tier definitions exist in
> `writing-profile.md`? Do the frontmatter schemas exist in `file-architecture.md`? Do the Q&A and
> bake-off formats exist in `execution-modes.md`? **Name anything that was deleted and not
> relocated.**
>
> **C. Is single-module self-sufficiency intact?**
> The router dispatches an agent to exactly ONE module per task via `<informatics>` gates in
> `index.md`. Read each of the five module files in isolation and ask: could an agent given only
> this file execute its domain, or does it now depend on following a `Canonical:` pointer to
> another file? Flag every case where a cross-reference replaced something load-bearing.
>
> **D. Were the tests weakened?**
> `test_tier5_adversarial.py::test_tas_02` was rewritten. Compare both versions. Does the new one
> test *more* or *less* than the old one? Could the new version pass while the specification and
> the authoritative schema disagree? Then read the new file `tests/test_canonical_ownership.py` and
> try to defeat each of its four guard classes — write a change that introduces the defect it
> claims to catch, and report any guard that does not fire.
>
> **E. Are the three new rules justified?**
> `WP-23`, `WP-24`, `WP-25` in `writing-profile.md`. For each: is there real evidence behind it in
> the repository's own operator lore (`apex-meta/AI-Snippets/Snippets.md`,
> `apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md`), or is it invented? Quote the source line
> or state that none exists. Flag any rule that duplicates an existing one.
>
> **F. Are the numbers honest?**
> The agent reports −129 lines and −807 tokens (−14% / −5%) and admits missing its own −13%
> projection. Recompute line counts yourself. Does its decomposition in `04-...md` §4 Caveats
> account for the gap, or does it hide anything?
>
> **G. Scope discipline**
> Did it change anything outside what a specification-compression task authorizes? Pay particular
> attention to `.claude/rules/informatics.md` and `apex-meta/informatics/standard.md`, which are
> instruction surfaces rather than specification content. Was changing them justified?
>
> **Deliver:** a table of every claim with CONFIRMED / OVERSTATED / FALSE and its `path:line`
> evidence; a list of anything lost, broken, or unjustified; and a single verdict — ACCEPT,
> ACCEPT WITH FIXES (list them), or REVERT (say which commit and why).

---

## 6. Things to push back on

The reviewer may miss these. They are the judgment calls most worth your own scrutiny:

1. **Short duplicated rules were deliberately kept.** `AD-03` still restates `EM-01`, and five more
   like it. The reasoning is in [02](02-new-rules-discovery-and-qa-bakeoff.md) Q1, but a reviewer
   could reasonably argue they should have been removed. If you disagree with the premise that one
   gate loads one module, the whole dedup policy changes — that is `RBL-01`.
2. **`writing-profile.md` grew 24%.** Intentional consolidation, but it is the one file that got
   bigger.
3. **`.claude/rules/informatics.md` was edited.** This file is loaded into every session touching
   the bundle. Small diff, large blast radius.
4. **The token result missed its projection by more than half** (−5% actual vs −13% projected).
   Accounted for in [04](04-consolidated-patch-and-verification.md) §4, but worth checking the
   arithmetic yourself.
5. **`D8` was declined, not fixed.** Reasoning in [M06](modules/M06-governance-schemas.md) §7.
6. **`RBL-07` is unrelated and urgent:** a plaintext password and API token sit in
   `apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md` lines 66-69, in a tracked file. Not touched
   by this pass. Needs rotation, not just deletion.
