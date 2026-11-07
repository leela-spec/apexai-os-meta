---
type: architecture
title: Ultra Block Style Audit Findings
description: Answers: how much of the Apex ultra block is prose rather than signal-word bullets, which rules could be rewritten in the clause style, and does the rewrite save tokens?
tags: [ssot, architecture, informatics, ultra-block, audit, findings, draft]
timestamp: 2026-11-06
authority_tier: 3
status: draft
owner: architecture
---

# Ultra Block Style Audit Findings

## At a glance

- **Purpose:** measure how much of the 22-rule ultra block is prose and test whether the accepted signal-word clause ([SSOT-D-068](C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/2026-11-06-signal-word-rule-accepted.md)) fits it.

- **Conclusion:** 22 of 22 tags (100%) are prose; the block holds 0 signal bullets. 12 tags are `P-list`. All 12 rewrites cost tokens: 563 → 693 BPE tokens (+130, +23%). The style improves scannability and checkability; it does not compress.

- **Tags worth rewriting, if scannability outweighs the token cost:** `authoring` (11 items), `handover` (9), `communication` (8), `ground` (6). **Cheapest:** `recovery` (+3). Rewrite none for density.

- **Correction, 2026-11-06:** the "canonical" block audited here is `candidates/16-candidate-3A-ultra.md`, which is superseded. The real master is `specs/apex_contract_v1.0_ultra.xml` (23 rules, includes `<align>`). Against it the vendored copy differs only in `base_ref` and the `authoring` ref. The 22-rule counts and the vendored-vs-canonical list in Section 3 describe the stale file. See apex-carrier-map.md (`apexai-os-meta/apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md`) (Gap G1). The conclusion on token cost holds for the 22 shared rules.

- **Vendored copy differs from the stale `candidates/16` file** in three places (Section 3). Its `align` rule already uses bullets, but not the accepted form.

- **Status:** author-run. The independent verification in Section 5 has not run.

## 1. Table 1, per tag

Canonical block: 22 tags, 648 body words, 6,009 characters, 1,251 BPE tokens (`cl100k_base`, whole block including wrapper). `P blocks` counts contiguous non-bullet runs per tag body. `enumerable items` counts entries in lists of three or more parallel items, hand-labelled from the detector output.

| # | tag | words | sentences | S bullets | P blocks | enumerable items | class |
|---|---|---:|---:|---:|---:|---:|---|
| 01 | target | 36 | 3 | 0 | 1 | 0 | prose |
| 02 | product_first | 30 | 3 | 0 | 1 | 5 | prose |
| 03 | scope | 24 | 3 | 0 | 1 | 3 | prose |
| 04 | communication | 40 | 5 | 0 | 1 | 8 | prose |
| 05 | hold_position | 33 | 3 | 0 | 1 | 0 | prose |
| 06 | ground | 47 | 4 | 0 | 1 | 6 | prose |
| 07 | reuse | 27 | 3 | 0 | 1 | 4 | prose |
| 08 | context | 29 | 2 | 0 | 1 | 0 | prose |
| 09 | recovery | 19 | 2 | 0 | 1 | 4 | prose |
| 10 | stop_repairing | 22 | 2 | 0 | 1 | 0 | prose |
| 11 | current_truth | 23 | 3 | 0 | 1 | 3 | prose |
| 12 | surgical | 9 | 1 | 0 | 1 | 0 | prose |
| 13 | editing | 33 | 4 | 0 | 1 | 0 | prose |
| 14 | new_machinery | 33 | 3 | 0 | 1 | 3 | prose |
| 15 | detour | 15 | 2 | 0 | 1 | 0 | prose |
| 16 | authoring | 54 | 7 | 0 | 1 | 11 | prose |
| 17 | trade_off | 32 | 3 | 0 | 1 | 5 | prose |
| 18 | handover | 29 | 3 | 0 | 1 | 9 | prose |
| 19 | iterative | 38 | 3 | 0 | 1 | 5 | prose |
| 20 | schemas | 28 | 3 | 0 | 1 | 0 | prose |
| 21 | sync | 26 | 3 | 0 | 1 | 0 | prose |
| 22 | pointers | 21 | 2 | 0 | 1 | 0 | prose |

Tags with enumerable items are the 12 `P-list` tags. `align` is vendored-only and outside the 22 (Section 3).

## 2. Table 2, shape violations (S1 to S4)

The canonical block has 0 signal bullets (the S regex matches nothing), so S1 to S4 have nothing to test there. The vendored copy has 0 matches too, but 6 near-miss bullets in `align` put the colon outside the bold span:

| line | check | text |
|---|---|---|
| `docs/apex/apex-contract.md:22` | not S (colon outside bold) | `- **Input**: the literal ask, verbatim.` |
| `docs/apex/apex-contract.md:23` | not S | `- **Sources**: the artifacts you will open.` |
| `docs/apex/apex-contract.md:24` | not S | `- **Process**: how you will get and verify the facts, ...` |
| `docs/apex/apex-contract.md:25` | not S | `- **Skills**: the tools or skills you will invoke, or none.` |
| `docs/apex/apex-contract.md:26` | not S | `- **Output**: what you will change, and what the deliverable is.` |
| `docs/apex/apex-contract.md:27` | not S | `- **Redraft**: the shape of the future output - ...` |

These are outside the 22 rules. They differ from the accepted clause by one character position.

## 3. Vendored copy against canonical

Compared with a script that parses both files into tag, attributes and body.

- **Tag count:** canonical 22, vendored 23. `align` exists only in the vendored copy.
- **`product_first` body:** vendored adds one sentence: "Deliver a narrow version that runs, then widen it; first-pass completeness is not the target and generality bought before a second real case is waste."
- **`authoring` ref:** canonical `index.md`, vendored `specs/file-architecture.md`.
- **Wrapper `base_ref`:** canonical `apex-meta/informatics/final/`, vendored `docs/apex/` (expected repo-relative change).
- **Size claim reconciled:** the canonical file states 5,917 chars, 1,479 repo tokens and 1,225 BPE. The block without the `<apex_contract>` wrapper measures 5,919 chars, 1,479 repo tokens (`chars // 4`) and 1,221 BPE. The claim therefore excludes the wrapper; the residual gap is 2 chars and 4 BPE, attributed to whitespace and tokenizer version. The 1,251 BPE in Section 1 includes the wrapper.

## 4. Table 3, rewrite candidates

Tokens: `tiktoken` `cl100k_base`, tag body only. Original and rewrite text sit in the R-blocks below the table, one per row, because the full wording does not fit a table cell.

| tag | original | rewrite | tokens before | tokens after | constraints kept |
|---|---|---|---:|---:|---|
| product_first | R1 original | R1 rewrite | 39 | 52 | 4 of 4 |
| scope | R2 original | R2 rewrite | 33 | 41 | 4 of 4 |
| communication | R3 original | R3 rewrite | 59 | 72 | 10 of 10 |
| ground | R4 original | R4 rewrite | 65 | 76 | 6 of 6 |
| reuse | R5 original | R5 rewrite | 35 | 47 | 5 of 5 |
| recovery | R6 original | R6 rewrite | 27 | 30 | 4 of 4 |
| current_truth | R7 original | R7 rewrite | 31 | 40 | 4 of 4 |
| new_machinery | R8 original | R8 rewrite | 41 | 50 | 5 of 5 |
| authoring | R9 original | R9 rewrite | 87 | 110 | 12 of 12 |
| trade_off | R10 original | R10 rewrite | 48 | 57 | 7 of 7 |
| handover | R11 original | R11 rewrite | 45 | 58 | 4 of 4 |
| iterative | R12 original | R12 rewrite | 53 | 60 | 6 of 6 |

Rewrites follow `- **Signal:** item`, one item inline, several nested. Nested items carry no signal word. No rewrite changed a rule's meaning in the author's reading.

**Keep as prose (10 tags, no list of three or more):**

- `target`: its conditions ("outrank", "no change needed, say so and stop") are conditionals, not items.
- `hold_position`, `editing`, `detour`, `schemas`, `sync`: sequences of imperatives and conditions.
- `context`, `stop_repairing`, `surgical`, `pointers`: no list to nest.

### R1 `product_first`: 39 → 52 tokens (+13), 222 → 241 chars

Original:

```text
Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss. A passing verification script never defines done.
```

Rewrite:

```text
Build the working product before surrounding machinery.
- **Until a vertical slice runs, fix only:**
  - execution blockers
  - corruption
  - experiment invalidation
  - safety
  - data loss
A passing verification script never defines done.
```

Ledger, original constraint → rewrite location (4 of 4 kept):

- build product before machinery
- blocker whitelist (5 items)
- 'until slice runs' condition
- passing script never defines done

### R2 `scope`: 33 → 41 tokens (+8), 185 → 185 chars

Original:

```text
Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.
```

Rewrite:

```text
Do only authorized work and material enablers.
- **Report, never build:**
  - adjacent cleanup
  - redesign
  - speculative features
Analyzing or planning never authorizes implementing.
```

Ledger, original constraint → rewrite location (4 of 4 kept):

- only authorized work + material enablers
- report 3 item kinds
- report instead of building
- analysis/planning never authorizes implementing

### R3 `communication`: 59 → 72 tokens (+13), 306 → 339 chars

Original:

```text
Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.
```

Rewrite:

```text
- **Style:** active voice, explicit actor, conclusion first, one imperative per sentence.
- **Register:** Cool Blue, analytical: objective, dense, zero filler, flattery, or unearned agreement.
- **Uncertainty:** state plainly when evidence is incomplete; avoid empty hedges.
- **Report:** results and exact blockers; compress tool chatter.
```

Ledger, original constraint → rewrite location (10 of 10 kept):

- active voice
- explicit actor
- conclusion first
- one imperative per sentence
- analytical register (Cool Blue)
- objective, dense, zero filler/flattery/unearned agreement
- uncertainty stated plainly when evidence incomplete
- avoid empty hedges
- report results and exact blockers
- compress tool chatter

### R4 `ground`: 65 → 76 tokens (+11), 327 → 342 chars

Original:

```text
Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries. State the command producing any absence, zero, or count claim. Check what is checkable now instead of deferring it. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.
```

Rewrite:

```text
Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries.
- **State the command producing any:**
  - absence
  - zero
  - count claim
Check what is checkable now instead of deferring it.
- **Factual, design, or version questions:** cross-check ~3 authoritative sources grounded in the live environment.
```

Ledger, original constraint → rewrite location (6 of 6 kept):

- verify against artifacts (path:line) or live outputs
- never memory or summaries
- command for absence/zero/count claims
- check now, do not defer
- ~3 sources for factual/design/version questions
- grounded in live environment

### R5 `reuse`: 35 → 47 tokens (+12), 198 → 213 chars

Original:

```text
Before building, inspect repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.
```

Rewrite:

```text
- **Before building, inspect:**
  - repository scripts
  - installed tools
  - libraries
  - skills
Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.
```

Ledger, original constraint → rewrite location (5 of 5 kept):

- inspect before building
- 4 inspection targets
- adapt proven options over smallest surface
- compose modular parts
- build new only when nothing fits

### R6 `recovery`: 27 → 30 tokens (+3), 158 → 165 chars

Original:

```text
Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.
```

Rewrite:

```text
Work around incidental failures using the narrowest intent-preserving alternative.
- **Stop only for:** genuine target, safety, authorization, or integrity blockers.
```

Ledger, original constraint → rewrite location (4 of 4 kept):

- work around incidental failures
- narrowest intent-preserving alternative
- stop only for blockers
- 4 blocker kinds, 'genuine'

### R7 `current_truth`: 31 → 40 tokens (+9), 153 → 165 chars

Original:

```text
State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.
```

Rewrite:

```text
State active truth only.
- **Place in a changelog, never inline:**
  - history
  - superseded options
  - incident notes
Never name retired components in live rules.
```

Ledger, original constraint → rewrite location (4 of 4 kept):

- active truth only
- 3 item kinds go to changelog
- never inline
- never name retired components in live rules

### R8 `new_machinery`: 41 → 50 tokens (+9), 206 → 220 chars

Original:

```text
Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies.
```

Rewrite:

```text
- **Name first what it resolves:**
  - exact requirement
  - blocker
  - material risk
If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies.
```

Ledger, original constraint → rewrite location (5 of 5 kept):

- name what it resolves first
- 3 resolution kinds, 'exact'
- ~2-step ordinary-use condition
- fix data or logic directly
- no more machinery than risk justifies

### R9 `authoring`: 87 → 110 tokens (+23), 358 → 398 chars

Original:

```text
Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.
```

Rewrite:

```text
- **Frontmatter:**
  - flat YAML, colons on every line
  - inline bracket lists, no multiline dashes
  - concept files declare type, id, title, description, status
- **Body:**
  - front-load invariants, close on failure guards
  - one purpose per file, link listed files
  - exclude chat, code, logs
- **Tag rules:** [P0-P3 | I/E/R] 1-100 uncombined.
Open ref for tier definitions or bundle layout.
```

Ledger, original constraint → rewrite location (12 of 12 kept):

- flat YAML
- colons on every line
- inline bracket lists
- no multiline dashes
- concept-file 5 fields
- front-load invariants
- close on failure guards
- tag rules [P0-P3 | I/E/R] 1-100 uncombined
- one purpose per file
- link listed files
- exclude chat/code/logs
- open ref for tier defs/bundle layout

### R10 `trade_off`: 48 → 57 tokens (+9), 235 → 242 chars

Original:

```text
Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.
```

Rewrite:

```text
Decide routine reversible choices yourself.
- **Material trade-offs, per option:**
  - mechanism
  - concrete grounding
  - raw (I/E/R) estimates
- **Then:** a recommendation and one line per rejection.
Open ref for multi-candidate bake-offs.
```

Ledger, original constraint → rewrite location (7 of 7 kept):

- decide routine reversible choices yourself
- mechanism
- concrete grounding
- raw (I/E/R) estimates
- recommendation
- one line per rejection
- open ref for bake-offs

### R11 `handover`: 45 → 58 tokens (+13), 218 → 236 chars

Original:

```text
Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).
```

Rewrite:

```text
Never write a handover to defer resolvable work.
- **When needed, state:**
  - observations
  - reasoning chain
  - caveats
  - conclusion
  - reproduction commands
Open ref for delegation contracts (input ledger, process, output, DoD).
```

Ledger, original constraint → rewrite location (4 of 4 kept):

- never defer resolvable work
- 5 stated items
- 'when needed' condition
- open ref for delegation contracts + 4 parts

### R12 `iterative`: 53 → 60 tokens (+7), 253 → 259 chars

Original:

```text
Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.
```

Rewrite:

```text
Execute single-step tasks directly.
- **Multi-step work:**
  - write a compact preflight (target, inputs, scope, output, active step)
  - proceed step by step
  - create a file per step for multi-module projects
Open ref for route ladder or MMM decomposition.
```

Ledger, original constraint → rewrite location (6 of 6 kept):

- single-step executes directly
- multi-step condition
- compact preflight + 5 parts
- step by step
- file per step for multi-module
- open ref for route ladder/MMM


## 5. Verification, not yet run

- **Count:** rerun the counting commands and compare three tags by hand.
- **Rewrites:** check two rewrites, each original constraint against the rewrite alone.
- **Violations:** confirm `apex-contract.md:22-27` exist and break the S regex.
- Must be done by someone other than the author.

## Observation

- Canonical: QMD `qmd://apex-informatics-final/candidates/16-candidate-3A-ultra.md`, lines 40-104; extracted with `qmd get <uri> --full`, stripped to the XML block.
- Vendored: [apex-contract.md:16-91](C:/GitDev/Leela-Cloud-2026/docs/apex/apex-contract.md); `align` bullets at [apex-contract.md:22-27](C:/GitDev/Leela-Cloud-2026/docs/apex/apex-contract.md).
- Measured by script: 22 tags in canonical, 23 in vendored; canonical block 648 body words, 12 tags with a list of three or more entries; 12 rewrites total 563 → 693 BPE.
- Counting: Python with `re` and `tiktoken` (`cl100k_base`); scripts live in the session scratchpad and are not committed.
- `grep -nE '^\s*- \*\*[^*:]+:\*\*' docs/apex/apex-contract.md` returns no lines.

## Logic chain

- No S bullet exists in the 22 rules, so each tag is `prose`.
- A list of three or more parallel entries qualifies a block as `P-list`; 12 tags have one.
- Each `P-list` rewrite adds a signal label, newlines and indent while keeping the same words, so tokens rise.
- Inference: the cost comes from markup and will recur in any rewrite of this style. Measured: +130 tokens over 12 rewrites.

## Caveats

- Sentence counts and enumerable items use heuristics plus hand labels; both are author judgments.
- Token counts use one tokenizer; a Claude tokenizer may differ.
- Meaning preservation is the author's reading, not an independent check.
- The size claim differs from the measurement by 2 chars and 4 BPE after excluding the wrapper (Section 3); the cause is inferred, not proven.
- Whether signal bullets change model compliance is not measured here.

## Conclusion

The ultra block is entirely prose, and 12 of 22 rules contain lists that fit the signal-bullet clause. Rewriting them adds about 130 tokens across those 12 rules. Adopt the style for scannability, not for density.

## Verification method

Reproduce, from the repository root:

```bash
qmd get "qmd://apex-informatics-final/candidates/16-candidate-3A-ultra.md" --full \
  | sed -n '/^39: ```xml/,/^105: ```/p' | sed -E 's/^[0-9]+: ?//' | sed '1d;$d' > canon.xml
grep -nE '^\s*- \*\*[^*:]+:\*\*' docs/apex/apex-contract.md      # expect no output
grep -nE '^- \*\*[A-Za-z]+\*\*:' docs/apex/apex-contract.md      # expect lines 22-27
python -c "import re,tiktoken;e=tiktoken.get_encoding('cl100k_base');t=open('canon.xml',encoding='utf-8').read();b=re.sub(r'^<apex_contract[^>]*>\s*|\s*</apex_contract>\s*$','',t.strip());print(len(b),len(e.encode(b)))"   # expect 5919 1221
```

Files to inspect: [apex-contract.md](C:/GitDev/Leela-Cloud-2026/docs/apex/apex-contract.md), the canonical file above, and the R-blocks in Section 4.

Invalidation conditions:

- A signal bullet appears in `canon.xml`: Table 1 `S bullets` and the class column are wrong.
- Any R-block rewrite drops an original constraint listed in its ledger: that row's "constraints kept" is wrong.
- Re-tokenized rewrites save tokens in total: the conclusion that the style does not compress is wrong.
- The canonical file changes after 2026-11-06: all counts need rerunning.

Section 5 lists the independent checks. None has run by someone other than the author.
