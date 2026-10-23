---
type: Reference
id: V2-CONTRACT-BLOCK-v1.0
title: Informatics Contract Block — Standalone Candidate
description: The standalone 721-token always-on contract block with per-rule provenance back to the live rules it compresses, measurement, and the compression losses made explicit.
status: candidate_not_active
tags: [candidate, contract-block, always-on, provenance]
---

# Informatics Contract Block — Standalone Candidate

> **Not active.** This file is a candidate artifact. No agent loads it. Its intended production use
> is to be embedded inside an always-on instruction file — see
> [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md) for what that looks like. Do not instruct agents
> to read *this* file at runtime; that would defeat its purpose.

**Measured: 721 tokens.** `<always>` 303 · `<writing>` 140 · `<files>` 113 · `<dispatch>` 133.

---

## 1. The block

```xml
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
```

---

## 2. Provenance — every line traced to the rule it compresses

Each `<always>` line is a lossy compression of one or more live rules. **This table is what you need
to review** — it shows exactly what was dropped.

| Contract line | Compresses | What is lost |
|---|---|---|
| Target | `AD-01`, `EM-04`, `AD-09` stop-on-drift, `AD-12` product advancement | The explicit drift list (ceremony, orchestration, schemas, wrappers, test infra) and the "every work unit must advance the product" test |
| Scope | `AD-18` zero-speculation, `AD-05` operator challenge boundary | The operator-challenge question — *"does this need fixing before we can test the product?"* — which is a concrete decision procedure, not a principle |
| Surgical | `EM-01`, `AD-03`, `GS-02`, `AD-23` deterministic moves | The 8-step Mode A protocol (one change per block, copy verbatim, no line numbers, disambiguating context, exact whitespace, honest uncertainty, no assumed application). **Heavy loss** — mitigated only by the `execution-modes.md` pointer |
| Context | `EM-03`, `AD-04`, `EM-10` route 0/1/2 | The Input Priority Ledger structure and the three-route complexity ladder |
| Substance | `WP-01`, `FA-04`, `AD-08` | The explicit grant of authority to *authors as well as agents*, and the "unnatural prose" trigger |
| Ground | `AD-19`, `WP-04`, `AD-20`, `WP-16` | Nothing material — these compress cleanly |
| Reuse | `AD-11`, `EM-07` ELSE-IF | The "battle-proven in established form" nuance from the pilot's `<reuse>` — adapted rather than merely researched |
| Two-strike | `AD-02`, `EM-05`, `AD-24` | Per-subsystem strike tracking and the reset-on-success mechanic |
| Current-truth | `FA-01`, `AD-15`, `WP-08`, `FA-09` | The residual-name mechanism: *why* stale names cause ghost-reasoning, and the migration-file escape hatch |
| Parsimony | `WP-18`, `FA-12`, `GS-14`, `AD-26`, `GS-15` | How to *count* directives (`GS-15`: compliance directives counted separately from declarative content) |

| `<writing>` clause | Compresses |
|---|---|
| Active voice, one command, no hedging | `WP-05`, `WP-02`, `WP-03` |
| Conclusion first | `WP-12`, `AD-17` |
| ~20 / ~25 words | `WP-14` — **drops** the target-vs-advisory-gate reconciliation |
| Tables / bullets / numbered | `WP-11` |
| Durable IDs | `WP-15`, `FA-07`, `GS-08` |
| `[P0-P3 | I/E/R]` never aggregated | `WP-07`, `GS-04` — **drops** the tier semantics table and the I/E/R dimension definitions |
| Link files you list | `WP-24` |
| *not carried* | `WP-10` Information Mapping, `WP-13` ~150-word blocks, `WP-17` compact examples, `WP-19` syntax exemptions, `WP-20` no-default-behavior rules, `WP-21` heading depth, `WP-22` typography, `WP-23` single-owner reuse, `WP-25` terminal position |

| `<files>` clause | Compresses |
|---|---|
| Flat YAML, colon per line, inline brackets | `FA-13`, `GS-05` |
| Concept + root frontmatter fields | `FA-05`, `FA-06`, `GS-06`, `GS-07` — **drops** the full field table and the required/expected/optional distinction |
| One responsibility per file | `FA-10` |
| Front-load; close on failure guard | `FA-02`, `WP-06`, `WP-25` |
| *not carried* | `FA-03` five planes, `FA-08` sub-bundle boundary, `FA-11` changelog allocation, the plane token orientations |

---

## 3. What this means for review

**Nine of twenty-five writing rules and four of thirteen file rules are not carried at all.** That
is the design working as intended — they are reachable through `ref=` when `deepen_when` fires. But
it is also the central risk: it only works if the agent notices it needs depth.

The two heaviest compressions are worth your specific attention:

1. **`Surgical`** collapses the entire 8-step exact-match patch protocol into one line. Patch
   discipline is the rule the operator has emphasized most, and a one-line version may not carry it.
   If any clause should be expanded, it is this one.
2. **`[P0-P3 | I/E/R]` without the tier table.** The contract says to tag rules but not what the
   tiers mean. An agent authoring a new rule could tag it plausibly and wrongly.

Both are candidates for promotion from pointer to inline — at a cost of roughly 80 and 120 tokens
respectively, which would take the block to ~920 and still fit the ~1,000-token target.

---

## 4. Deliberate design choices

| Choice | Reason |
|---|---|
| `<writing>` and `<files>` are inline, the other three are pointers | The agent writes prose and touches files on nearly every task; those rules earn their 253 tokens. Patch, drift and schema work are genuinely conditional. |
| Every group carries `when=` even though gating saves no tokens here | Gating reduces the number of instructions competing for compliance, and prevents speculative downstream reads (`DEC-M2`) |
| `deepen_when` is separate from `when` | `when` says "this group applies"; `deepen_when` says "this group is not enough, open the file". Two different signals. |
| `<dispatch>` uses plain IF/THEN prose, not XML attributes | Three one-line conditions do not need attribute structure; prose is cheaper and equally unambiguous |
| The closing line forbids auto-expansion | Directly from the operator's pilot design: *"Plain paths are JIT pointers, not import directives. Do not auto-expand them into context."* |
| No `<informatics>` wrapper around everything | The rules in `<always>` are universal, not informatics-specific. Nesting them under an informatics tag would imply they only bind during knowledge authoring. |

---

## 5. Measurement

Reproduce with the same heuristic used throughout (`~4 chars per token`):

```bash
python -c "import sys,pathlib; sys.path.insert(0,'apex-meta/informatics/tests'); from test_tier5_adversarial import estimate_tokens; p=pathlib.Path('apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/02-informatics-contract-block.md'); t=p.read_text(encoding='utf-8'); b=t.split('```xml')[1].split('```')[0]; print('block tokens:', estimate_tokens(b))"
```

| Section | Tokens | Share |
|---|---:|---:|
| `<always>` | 303 | 42% |
| `<writing>` | 140 | 19% |
| `<files>` | 113 | 16% |
| `<dispatch>` | 133 | 18% |
| wrapper + whitespace | 32 | 5% |
| **Total** | **721** | — |

Against the ~1,000-token target: **279 tokens of headroom**, enough to expand both heavy
compressions identified in §3 if you choose to.
