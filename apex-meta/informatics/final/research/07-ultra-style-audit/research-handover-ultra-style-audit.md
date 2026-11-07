---
type: architecture
title: Ultra Block Style Audit Handover
description: Answers: how much of the Apex ultra block is written as signal-word bullets or compact format clauses instead of prose, and which rules could be rewritten that way without losing meaning?
tags: [ssot, architecture, informatics, ultra-block, audit, handover, draft]
timestamp: 2026-11-06
authority_tier: 3
status: deferred
owner: architecture
---

# Ultra Block Style Audit Handover

## At a glance

- **Priority:** deferred. The signal-bullet rule is decided ([SSOT-D-068](C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/2026-11-06-signal-word-rule-accepted.md)); this audit is not needed for the spec-shape work. Run it only after the [online research](C:/GitDev/Leela-Cloud-2026/docs/ssot/architecture/spec-organization/online-research/README.md).

- **Purpose:** measure how much of the always-on ultra block is prose, and find rules that fit the compact clause style.

- **Style under audit:** the accepted clause from [SSOT-D-068](C:/GitDev/Leela-Cloud-2026/docs/ssot/decisions/2026-11-06-signal-word-rule-accepted.md):
  - `Bullets: "- **Signal:** item"; one item inline, several nested, 2-space indent, any depth.`

- **Deliverable:** `docs/ssot/architecture/spec-organization/ultra-style-audit-findings.md`.

- **Boundary:** read-only audit. No edit to the ultra block, any spec or any other file.

## 1. The style, made checkable

- **Signal bullet (S):** a line matching `^( *)- \*\*[^*:]+:\*\*( .*)?$`.

- **Shape checks** (each is a yes or no on one S bullet):
  - `S1`: the bullet has text after the colon, or two or more nested bullets, never one nested bullet alone.
  - `S2`: the bullet has inline text or nested bullets, never both.
  - `S3`: each nested line is indented exactly 2 spaces deeper than its parent; no tabs.
  - `S4`: inline text holds at most one item: no run of two or more `;` joining items.

- **Prose block (P):** a block of the ultra file that is not an S bullet, not a table row and not a code line.
  - measure per block: words, sentences, and **enumerable items** (a comma- or semicolon-list of three or more parallel items).
  - flag a block `P-list` when it has three or more enumerable items. Such a block could be a signal bullet with nested items.

- **Format clause (F):** a sentence that states how something must be shaped by showing an exemplar.
  - pattern: `Topic: "exemplar"; constraint, constraint.`
  - a block is `F-candidate` when it describes a shape, layout or format in prose and an exemplar would be shorter.

## 2. Input and priority ledger

| Priority | Source | Use it for | Ignore |
|---|---|---|---|
| 1 | QMD `apex-informatics-final/specs/apex_contract_v1.0_ultra.xml` | the canonical ultra block, 23 rules (the earlier 22-rule candidate is archived under `candidates/_archive/`) | other candidates (`3A`, `3B`, `3C`) |
| 2 | [apex-contract.md](C:/GitDev/Leela-Cloud-2026/docs/apex/apex-contract.md) | the vendored copy; check that it matches priority 1 | the README |
| 3 | [writing-profile.md](C:/GitDev/Leela-Cloud-2026/docs/apex/specs/writing-profile.md) and the files in `docs/apex/specs/execution-modes/` | the text the ultra block points to; audit only if a rule in priority 1 is a bare pointer | rules unrelated to formatting |

## 3. Process

- **Step 1, count deterministically:**
  - split the ultra block by tag; for each tag compute words, sentences, S bullets, P blocks, enumerable items.
  - use a command, not a read-through, and record the command. Example: a short script that tokenizes the block.

- **Step 2, classify each tag:** one of `signal-bullets`, `compact-clause`, `prose`, `mixed`.

- **Step 3, check the shape rules** `S1` to `S4` on every S bullet; list each violation with line number.

- **Step 4, find candidates:** for each `P-list` or `F-candidate` block, write one rewrite in the clause style.
  - keep every constraint of the original. Build a meaning-preservation ledger: original constraint → where it sits in the rewrite.
  - report the saving: characters and tokens before and after. State the token method.

- **Anti-drift:**
  - do not edit the ultra block or propose new rules; propose rewrites of existing wording only.
  - do not judge whether a rule is correct, only how it is written.
  - do not rewrite a block when the rewrite loses a condition. Mark it `keep as prose` and say which condition.
  - do not widen to the other candidates or to research files.

## 4. Output

- **Path:** `docs/ssot/architecture/spec-organization/ultra-style-audit-findings.md`.

- **Head:** a purpose bullet; a conclusion bullet with the share of prose tags; a bullet naming the tags worth rewriting.

- **Table 1, per tag:** `tag | words | sentences | S bullets | P blocks | enumerable items | class`.

- **Table 2, shape violations:** `line | check | text`.

- **Table 3, rewrite candidates:** `tag | original | rewrite | tokens before | tokens after | constraints kept`.

- **Example rows (illustrative shape only, not measured):**
  - `| scope | 38 | 2 | 0 | 1 | 0 | prose |`
  - `| authoring | "Flat YAML frontmatter: ..." | "Frontmatter: flat YAML, colon per line, inline lists; concept files add type, id, title, description, status." | 52 | 41 | 7 of 7 |`

## 5. Definition of done and independent verification

- **Done when:**
  - every one of the 22 rules appears in Table 1.
  - every rewrite candidate has a complete meaning-preservation ledger.
  - the vendored copy was compared with the canonical file and any difference is stated.

- **Verification, by someone other than the author:**
  - rerun the counting command and compare three tags by hand.
  - take two rewrites and check each original constraint against the rewrite alone.
  - confirm every flagged violation line exists and breaks the stated check.
  - A script that only confirms the file has tables does not count.

- **Report:** end the findings file with five blocks: Observation (links and exact commands), Logic chain, Caveats (write "No caveats" if none), Conclusion, Verification method.

- **Constraints to restate, since a fresh agent sees no repository instructions:**
  - never edit, move or delete any file except the one output file.
  - never commit or push.
  - never present an inference as a measurement.
