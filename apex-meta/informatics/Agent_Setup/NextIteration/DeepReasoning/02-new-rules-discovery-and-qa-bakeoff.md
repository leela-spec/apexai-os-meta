---
type: Reference
id: DR-QA-BAKEOFF-v1.0
title: New Rule Discovery & Structural Decision Bake-Off
description: Q&A Decision Matrices resolving every structural compression choice in the Apex Informatics compression pass, external research citations, operator-lore coverage cross-check, and the newly discovered rules.
status: current
tags: [research, decision-matrix, bake-off, new-rules, web-research]
---

# New Rule Discovery & Structural Decision Bake-Off

**Bottom line:** eight structural decisions resolved below, three genuinely missing rules found —
two from operator lore that the suite never codified, one from positional-attention research that
costs zero tokens to adopt.

## 1. External Research Base

Searched October 2026. Only queries whose answer changes a patch decision were run.

| # | Question | Finding | Decides |
|---|---|---|---|
| R1 | Does restating instructions degrade compliance? | Stacking instructions collapses instruction-following through *interference*; ~12% of individually-satisfiable instruction pairs fail far more than their solo rates predict ([Instruction Stacking Collapse](https://arxiv.org/pdf/2608.02639)) | Q1 |
| R2 | Is *conflicting* worse than *redundant*? | Yes, and sharply. All evaluated models decline steeply under conflicting instructions; models overweight the most recent or most salient and silently violate the other ([IHEval](https://aclanthology.org/2025.naacl-long.425.pdf), [PRIME](https://arxiv.org/html/2606.22470)) | Q1, Q2, Q4 |
| R3 | Where do instructions actually get read? | U-shaped utilization curve — primacy at the start, recency at the end, with the middle neglected ([Lost in the Middle](https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf), [Found in the Middle](https://arxiv.org/pdf/2406.16008)) | Q5, `WP-25` |
| R4 | XML tags or Markdown headings? | XML costs ~5–15% more tokens than equivalent Markdown; it earns that cost when a block needs a *nameable, attribute-carrying handle* or mixes instructions with source text ([XML vs Markdown 2026](https://dev.to/manishramavat/xml-tags-dont-help-short-prompts-heres-when-they-actually-matter-2026-25gf), [Structured Prompting](https://www.ml4devs.com/what-is/structured-prompting/)) | Q6 |
| R5 | How large should an always-on instruction file be? | 2026 convention: root `CLAUDE.md` under ~100 lines (some practitioners 50–60), `AGENTS.md` under ~150 lines, with task-specific content split out under progressive disclosure ([A Complete Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md), [Agent Instruction Files](https://codex.danielvaughan.com/2026/05/27/agent-instruction-files-agents-md-claude-md-cross-tool-portability-codex-cli/)) | `RBL-02` |

**Key asymmetry from R1 + R2:** redundancy and contradiction are not the same failure. Redundancy
costs tokens and some interference. Contradiction costs *correctness* and is resolved by the model
unpredictably. That asymmetry is the backbone of Q1 and makes defects **D2** and **D9** the highest
priority items in this pass.

## 2. Structural Decision Matrices

### Q1 — At what granularity should duplication be removed?

- *Question:* Should every repeated concept be reduced to a single owner plus pointers, or only repeated blocks?
- *Options:*
  - **Option A (Block-only dedup):** Delete duplicated blocks ≥8 lines (schemas, tables, JSON, catalogs). Retain ≤2-line rule restatements but force their wording into agreement with the owner. *Grounding:* an agent asked to "write the architecture doc" hits the `file_creation_or_structure` gate, loads `file-architecture.md` alone, and must find the frontmatter schema there — but it does not need the P0–P3 tier table restated to do so. `(I92/E90/R12)`
  - **Option B (Full pointer-ification):** Every duplicate concept becomes a 1-line link to its owner. *Grounding:* the same agent now follows a pointer from `FA` to `WP` to learn what `P1` means mid-task, turning one file read into two. `(I70/E85/R45)`
  - **Option C (Leave duplication; fix only contradictions):** Patch `D2`/`D9` and stop. *Grounding:* minimal-risk pass that resolves the correctness defects and ignores the ~2,200 recoverable tokens. `(I55/E95/R08)`
- *Recommendation:* Option A
- *Reasoning:* R2 establishes that contradiction, not restatement, drives the sharp compliance declines — so the expensive duplicates are precisely the large blocks that have drifted (`D2`, `D9`), while a 22-token invariant restated across two modules is cheap insurance that keeps single-gate JIT routing self-sufficient. R1's interference effect is real but scales with directive count, and Option A removes ~2,200 tokens of declarative bulk without removing a single directive, so it reduces size without increasing hops.
- *Notes:*
  - Option B — Rejected because `test_cis_01`–`cis_05` assert single-module isolation; bare pointers break the guarantee those tests exist to protect.
  - Option C — Rejected because it leaves a 93-line drifted schema copy in place as a standing drift channel.

### Q2 — Which file owns the OKF frontmatter contracts?

- *Question:* `file-architecture.md` §3 and `governance-schemas.md` §2.1 both define the root-index and concept frontmatter schemas, and they disagree. Which becomes canonical?
- *Options:*
  - **Option A (`FA` owns, `GS` points):** The authoring surface holds the schema. *Grounding:* "create a new concept doc in the bundle" routes to `file_creation_or_structure` → `FA`. The agent needs the YAML block inline at exactly that moment. `(I90/E92/R10)`
  - **Option B (`GS` owns, `FA` points):** The schema file holds all schemas. *Grounding:* conceptually tidy — `GS` already owns `patch_intent` and the diagnostics catalog — but every file-creation task now needs a second load to see the frontmatter it must write. `(I65/E88/R35)`
  - **Option C (Keep both, reconcile wording):** Both files keep a full copy, synchronized. *Grounding:* no extra hop, but re-arms the exact drift channel that produced `D2` and `D9`. `(I40/E95/R70)`
- *Recommendation:* Option A
- *Reasoning:* Ownership should follow the load path, not the taxonomy. `FA` is what the router actually hands an agent at authoring time, and `GS` retains what is genuinely its own — the concept-type table, the tri-class diagnostics catalog, and the conformance gate — so neither file becomes a stub.
- *Notes:*
  - Option B — Rejected because it imposes a second file load on the suite's most frequent authoring task.
  - Option C — Rejected because synchronized-copy discipline is what already failed twice in this bundle.

**Conflict resolution for D2:** the merged contract declares `type`, `id`, `title`, `description`,
`status` as required on concept documents and `tags` as expected; `version` becomes explicitly
optional. Root index declares `okf_version`, `title`, `description` required and `tags` expected.
This matches what `okf_validator.py` actually enforces, so the published contract and the gate agree.

### Q3 — What happens to `general-informatics-router.md`?

- *Question:* The router reproduces `index.md` §1, §2 and §5 near-verbatim at ~500 tokens. Delete, diverge, or declare?
- *Options:*
  - **Option A (Declare the derivation):** Keep the file; add one line stating it is a standalone embeddable copy of `index.md` §1–2 and that `index.md` is canonical. *Grounding:* the operator pastes this block into a different repository's `AGENTS.md`, where a relative link back to `index.md` would not resolve — so the copy must stay self-contained. `(I82/E88/R08)`
  - **Option B (Delete the router):** Fold it into `index.md`. *Grounding:* removes 500 tokens and the duplication outright, but destroys the portable artifact and breaks `test_live_07` plus five `test_cis_*` fixtures that read the router directly. `(I45/E80/R60)`
  - **Option C (Make it a pointer):** Replace the body with a link to `index.md`. *Grounding:* an embeddable snippet whose content lives behind a path that does not exist in the target repository is non-functional. `(I20/E92/R75)`
- *Recommendation:* Option A
- *Reasoning:* This duplication is a deliverable, not an accident — `index.md` §3 already describes the router as a "compact standalone agent-facing embeddable JIT router template." The defect is that nothing in either file says so, which leaves a future auditor to re-litigate it as drift. One declarative line converts unexplained duplication into a documented artifact contract at a cost of ~15 tokens.
- *Notes:*
  - Option B — Rejected because it destroys the portable embed, the file's entire reason to exist.
  - Option C — Rejected because a pointer to a non-resolving path is worse than no file.

### Q4 — How should the `patch_intent.v1` schema be represented?

- *Question:* `GS` §2.2 embeds 93 lines of JSON Schema that has drifted from the authoritative `patch-intent-schema.json` (**D9**). Inline, link, or contract-plus-link?
- *Options:*
  - **Option A (Operative contract + link):** State required fields, the operation enum, and the four safety invariants in ~12 lines; link the authoritative JSON as single source. *Grounding:* an agent writing a patch intent needs to know `safety.require_unique_match` must be `true` and that `line_number` is forbidden — it does not need the `maxLength` of `nearby_phrases` items in its context window, and the executor validates that anyway. `(I94/E92/R10)`
  - **Option B (Keep the inline copy, re-synchronize it):** Paste the current authoritative JSON over the stale copy. *Grounding:* fixes today's drift, costs 1,200 tokens on every `governance_and_schemas` load, and guarantees the same drift returns at the next schema revision. `(I40/E95/R65)`
  - **Option C (Link only):** Delete the schema section; cite the JSON file. *Grounding:* the agent now cannot state the safety invariants without a file read it may not be permitted to make. `(I55/E80/R40)`
- *Recommendation:* Option A
- *Reasoning:* The specification's job is to state the contract an agent must satisfy; the JSON file's job is to be the machine-checkable artifact. Option A assigns each its own role, removes the suite's single largest block, and closes a drift channel that has already silently weakened the published contract — the inline copy dropped every `maxLength` bound the real schema enforces.
- *Notes:*
  - Option B — Rejected because synchronized-copy discipline already failed here; re-arming it repeats a known defect.
  - Option C — Rejected because the safety invariants are the operative part and must survive in-context.

### Q5 — What occupies the final section of each governed file?

- *Question:* Three of five modules end on traceability link lists. Given recency bias, is that the right use of the terminal position?
- *Options:*
  - **Option A (End on operative content):** Reorder so each module's last block is its failure-mode guard or its strongest operative rule; traceability links move above it. *Grounding:* `writing-profile.md` currently ends with a speculative "Future Architecture Note" and a link list, placing its Not-To-Dos in the neglected middle — swapping §4 and §5 costs zero tokens and relocates four anti-pattern guards into the recency slot. `(I84/E88/R06)`
  - **Option B (Leave ordering as-is):** Traceability last. *Grounding:* conventional document layout, familiar to human readers, wastes the highest-attention tail position on `file:///` links. `(I30/E85/R10)`
  - **Option C (Duplicate key rules into a closing summary):** Restate the P0 invariants at the end of every file. *Grounding:* captures recency deliberately, but adds ~150 tokens per file and re-creates intra-file duplication. `(I60/E70/R55)`
- *Recommendation:* Option A
- *Reasoning:* R3 is one of the better-replicated findings in long-context behavior, and Option A exploits it at literally zero token cost — it is pure reordering. `anti-drift-rules.md` already ends on its Failure Modes section and is the best-structured file in the suite by this measure; the change simply brings the others into line.
- *Notes:*
  - Option B — Rejected because it spends the file's highest-attention position on reference links.
  - Option C — Rejected because it buys recency with duplication, which Q1 exists to remove.

### Q6 — Keep the `<informatics>` XML dispatch gates?

- *Question:* XML tags cost ~5–15% more tokens than Markdown. Are the `<informatics>` and `<execution_dispatch>` blocks earning that premium?
- *Options:*
  - **Option A (Keep XML for dispatch only):** Routing gates stay XML; all rule content stays Markdown. *Grounding:* `<informatics when="..." ref="..." deepen_when="...">` carries three machine-readable attributes and is parsed as a unit by `test_cis_01`–`cis_05`; a Markdown heading cannot carry attributes. `(I88/E90/R08)`
  - **Option B (Convert gates to Markdown tables):** A routing table with `when`/`ref`/`payload` columns. *Grounding:* ~10% cheaper and human-scannable, but loses the nameable block boundary the tests and the agent both key on. `(I50/E82/R35)`
  - **Option C (Convert the whole suite to XML):** *Grounding:* uniform structure, ~5–15% token penalty across 17,000 tokens for content that is already unambiguous prose. `(I25/E88/R50)`
- *Recommendation:* Option A
- *Reasoning:* R4's rule is precise — XML earns its premium exactly where a block needs a nameable, attribute-carrying handle, which is what a conditional routing gate is and what nothing else in the suite is. The current split is already correct; this matrix confirms it rather than changing it.
- *Notes:*
  - Option B — Rejected because the attribute triple is the dispatch contract, not decoration.
  - Option C — Rejected because it pays a token premium on 17,000 tokens of prose that gains nothing.

### Q7 — Which rule keeps the ID `FA-04`? (**D1**)

- *Question:* Two unrelated rules both carry `FA-04`. Renumbering must not break durable-ID immutability (`WP-15`) more than necessary.
- *Options:*
  - **Option A (First occurrence keeps `FA-04`; Flat-YAML becomes `FA-13`):** Substance Over Ceremony retains `FA-04`; the frontmatter serialization rule moves to the end of the ID range. *Grounding:* `FA-05`..`FA-12` keep their current IDs, so every existing cross-reference in the suite and tests stays valid; only the one genuinely ambiguous ID moves. `(I88/E92/R10)`
  - **Option B (Renumber `FA-05`..`FA-12` upward by one):** Sequential IDs matching document order. *Grounding:* tidy ordering, invalidates eight existing durable IDs and every reference to them. `(I35/E90/R70)`
  - **Option C (Suffix disambiguation, `FA-04a` / `FA-04b`):** *Grounding:* no renumbering, but introduces a second ID grammar the validator and `WP-15` do not define. `(I30/E80/R55)`
- *Recommendation:* Option A
- *Reasoning:* Durable IDs exist precisely so references survive revision (`WP-15`), so the correct repair disturbs exactly one ID rather than eight. Appending `FA-13` outside document order is a cosmetic cost; breaking eight live cross-references is a real one.
- *Notes:*
  - Option B — Rejected because it invalidates eight durable IDs to fix a single collision.
  - Option C — Rejected because it invents an ID grammar no rule or validator defines.

### Q8 — How is the `standard.md` authority conflict resolved? (**D7**)

- *Question:* `.claude/rules/informatics.md` names `standard.md` as the overriding canonical profile, while the modular suite now governs the same domains.
- *Options:*
  - **Option A (Precedence note + rule-file pointer update):** Add a short precedence block to `standard.md` deferring to the modular suite for prose, architecture, adapters, drift, and schemas; update `.claude/rules/informatics.md` to route to `index.md` first. *Grounding:* an agent editing `apex-meta/informatics/**` currently loads the scoped rule file, is told `standard.md` overrides, and may apply a superseded prose rule over `WP-14`. `(I88/E90/R12)`
  - **Option B (Deprecate `standard.md`):** Mark `status: deprecated`. *Grounding:* decisive, but the file holds genuinely unique §1 scope/non-scope and §2 upstream-OKF precedence content that nothing else carries. `(I50/E78/R55)`
  - **Option C (Leave as-is):** *Grounding:* two live documents each claiming override authority over the same domains — the textbook conflicting-instruction case R2 measures. `(I15/E95/R80)`
- *Recommendation:* Option A
- *Reasoning:* `standard.md` §2 already establishes a layered precedence model, so the repair is to extend that existing ladder with the modular suite rather than to invent a new mechanism or discard a file that still owns unique scope content. It also honors the operator's scope decision: reconcile authority, do not rewrite the body.
- *Notes:*
  - Option B — Rejected because §1 and §2 content has no other home.
  - Option C — Rejected because unresolved dual authority is the measured failure mode, not a cosmetic untidiness.

## 3. Operator-Lore Coverage Cross-Check

Every operational insight in [Snippets.md](../../../../AI-Snippets/Snippets.md)
and `2Dos Ai Instructions.md` lines 1–265, checked against the live suite.

> **Source resolution.** `2Dos Ai Instructions.md` is **not tracked in git** and exists only on the
> operator's machine. The tracked equivalent on `origin/main` is
> [2Dos.md](../../../../AI-Snippets/Orga/2Dos.md), which carries the same content at **different line
> numbers** — the offset is inconsistent (+35 to +52 across spot checks), so the `2Dos:NN` references
> below are **against the untracked file and will not match `2Dos.md` line-for-line**. Locate the
> content by searching rather than by line number. Verified anchors: `2Dos:28` → `2Dos.md:63`,
> `2Dos:41` → `2Dos.md:84`, `2Dos:144-145` → `2Dos.md:196`, `2Dos:199-203` → `2Dos.md:250`,
> `2Dos:204-206` → `2Dos.md:177`, `2Dos:235` → `2Dos.md:286`.

| Lore source | Insight | Status |
|---|---|---|
| Snippets §adaptive_informatics | Gate formal standards on intent; casual chat exempt | ✅ `WP-09` |
| Snippets §Q&A | Matrix format with grounding for a non-expert reader | ✅ `EM-06` §2.1 |
| Snippets §anti-drift 1–8 | Target, reuse, product-first, two-strike, sunk-cost, advancement, proportionality, stop-on-drift | ✅ `AD-01`,`AD-11`,`AD-10`,`AD-02`,`AD-07`,`AD-12`,`AD-13`,`AD-09` |
| Snippets §"one rule for me" | Operator challenge boundary | ✅ `AD-05` |
| Snippets §overcorrecting | Minimalism; no precautionary guardrails | ✅ `AD-18` |
| Snippets §overcorrecting | **"Reuse existing instructions instead of restating them"** | ❌ **MISSING** → `WP-23` |
| Snippets §iterative | Master matrix → implementation map → per-step files → recreate master | ✅ `EM-10` §6.2 |
| Snippets §Formula REI | Expected-value composite score | ✅ Correctly **excluded**; `WP-07` and the `AD` Not-To-Dos ban aggregation |
| Snippets §MMM | Macro/Meso/Micro table | ✅ `EM` §6.3 |
| Snippets §patch format 1–8 | One change per block, copy verbatim, no line numbers, unique context, exact whitespace, honest uncertainty, no assumed application | ✅ `EM-08` §4.1 items 1–7 |
| Snippets §application | Iterative application, pragmatic workarounds, sync after | ✅ `EM-08` item 8, `EM-12` |
| 2Dos:3 | Sync = push+pull, no deletion, separate commits for out-of-scope files | ✅ `EM-12` |
| 2Dos:10 | Handover: intent/outcome, input, process, output, DoD | ✅ `EM-09` §5.1 |
| 2Dos:11 | Conscious step-by-step context loading | ✅ `EM-03`, `AD-04` |
| 2Dos:16 | Deterministic moves only, never rewrites | ✅ `AD-23` |
| 2Dos:17 | Guard against self-verifying superficial scripts | ✅ `AD` §4 Not-To-Dos |
| 2Dos:18 | Work-finish protocol: update READMEs/plans, check branches | ✅ `EM-10` §6.2 step 4 |
| 2Dos:19-21 | Stale residual names; balance eradication against needed warnings | ✅ `AD-15`, `WP-08` |
| 2Dos:28-29 | Operator complaint: "too much overlap" | ⚠️ Addressed structurally by this pass; codified as `WP-23` |
| **2Dos:41** | **"if listing files: create them with an embedded link so i can quickly open them/see path"** | ❌ **MISSING** → `WP-24` |
| 2Dos:44 | Overcorrection: surgical edits only | ✅ `AD-22` |
| 2Dos:51-55 | Four handover dimensions: input / process / output / tests | ✅ `EM-09` §5.1 |
| 2Dos:204-206 | Pre-addition gate: confirm ordinary use doesn't already surface it | ✅ `AD-25` |
| 2Dos:199-203 | Checkable ambiguity resolved now, not deferred | ✅ `EM-02`, `AD-06` |
| 2Dos:144-145 | Intra-file duplication is a named defect pattern | ⚠️ Not a rule; grounds **D6** and the `COLLAPSE_INTRA` verdict |

**Coverage result: 23 of 26 insights already codified.** Two genuine gaps and one structural gap,
specified below.

> **Unrelated finding, flagged not acted on:** `2Dos Ai Instructions.md` lines 66-69 contain a
> plaintext password and an API token for the OpenProject instance, in a file tracked by git.
> Out of scope for this pass and deliberately not reproduced here. Logged as `RBL-07`.

## 4. Newly Discovered Rules

### `WP-23` — Single-Owner Instruction Reuse

- **Proposed tag:** `[P1 | I90/E92/R08]`
- **Statement:** Reuse an existing instruction instead of restating it. When a concept already has a
  canonical owner in the suite, reference it; never copy its schema, table, or worked example into a
  second file. Restate only the one-line operative imperative a module needs to stay self-sufficient.
- **Grounding:** [Snippets.md:60-61](../../../../AI-Snippets/Snippets.md)
  states it as an operator directive; the operator's prior forensic pass applied it as
  *"owned here, pointer-only"* ([2Dos:235](../../../../AI-Snippets/Orga/2Dos.md));
  and this suite's defects **D2**, **D6** and **D9** are three independent realizations of its
  absence. R2 supplies the mechanism: copies drift, drift becomes contradiction, contradiction
  degrades compliance sharply.
- **Why it belongs in `writing-profile.md`:** it governs authoring behavior across governed
  artifacts, which is `WP`'s domain, and it sits naturally beside `WP-18` (parsimony) and `WP-20`
  (no default-behavior rules).
- **Self-application:** this rule is the one that would have prevented the entire defect class this
  pass exists to repair. Adding it is the durable fix; the patches are the one-time repair.

### `WP-24` — Clickable File References

- **Proposed tag:** `[P2 | I82/E90/R06]`
- **Statement:** When listing, citing, or recommending repository files, render each as a clickable
  Markdown link to its path rather than as bare text, so the reader can open it directly.
- **Grounding:** [2Dos:41](../../../../AI-Snippets/Orga/2Dos.md)
  — *"if listing files: create them with an embedded link so i can quickly open them/see path."*
  A standing operator ergonomics requirement that the suite never codified, despite `AD-27` and the
  traceability sections already practising it informally.
- **Interaction with `WP-22`:** `WP-22` mandates backtick quoting for paths; `WP-24` governs the
  case where a path is *presented for the reader to open*. Backticks for inline identifiers, links
  for file listings.

### `WP-25` — Terminal-Position Operative Content

- **Proposed tag:** `[P2 | I80/E86/R06]`
- **Statement:** Close every governed specification file with operative content — its failure-mode
  guard or its strongest actionable rule. Place traceability links, upstream references, and
  non-normative notes before that closing block, never after it.
- **Grounding:** R3's U-shaped utilization curve means the final block of a file sits in the
  recency-favoured position. `anti-drift-rules.md` already does this (its Not-To-Dos are last) and
  is the best-structured file in the suite by this measure; `writing-profile.md` and
  `governance-schemas.md` currently spend that position on `file:///` link lists.
- **Cost:** zero. The change is a section reorder, not added content — which is why it is adopted
  despite `E86` rather than a higher evidence tier.
- **Pairing:** `WP-25` is the tail-end complement to `WP-06` (top-loaded primacy). Together they
  state the positional contract for a governed file: invariants first, operative guard last,
  reference material in the middle where attention is cheapest.

## 5. Rules Challenged but Retained

| Rule | Challenge | Verdict |
|---|---|---|
| `AD-27` Sibling module linkage | Uses absolute `file:///c:/GitDev/...` URLs that break on any other machine or checkout | **Retain the rule, fix the links** — convert to relative paths; same fix applies to the traceability sections of `WP`, `FA`, `GS`. Tracked as `RBL-05`. |
| `WP` §5 Future Architecture Note | Speculative roadmap inside a live spec, contradicting `FA-01` current-truth separation | **Relocate** to `RBL-03`; it is a real idea in the wrong plane |
| `AD-26` parsimony ceiling (~30–50 directives) | `anti-drift-rules.md` itself carries 28 rules plus 6 not-to-dos = 34 directives | **Retain** — inside the stated orientation, and `WP-01` governs. Logged as `RBL-04` for measurement rather than pre-emptive restructuring |
| `GS-15` Directive accounting separation | Appears redundant with `WP-18` | **Retain** — it defines *how to count* directives, which `WP-18` assumes but never specifies. Genuinely unique. |
