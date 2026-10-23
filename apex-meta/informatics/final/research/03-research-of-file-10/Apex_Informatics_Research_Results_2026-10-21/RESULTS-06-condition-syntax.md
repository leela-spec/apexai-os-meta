---
type: Reference
id: RESULTS-06-condition-syntax
title: Conditional rule serialization and format - Findings
description: Assesses XML, bullets, tables, abbreviations and mixed layouts for rule adherence and tokens.
status: current
tags: [research-result, serialization, rp-06]
---

# RP-06 - Compact condition syntax and serialization

**Verdict (confidence: medium on the trade-off; low on the optimal encoding for this actual agent setup):** A wholesale table format is a **credible compression candidate, not a proven superior contract**. Repo-local measurements found a three-rule slice at **221 tokens for XML, 198 for conditional bullets (-10%), and 190 for a table (-14%)**; the author extrapolated approximately **-190 tokens (12%)** for the complete 1,622-token candidate. Neither the three-rule sample nor outside studies establishes that a table preserves correct rule triggering across these 22 rules. **Keep the operator's chosen tagged format until a matched 22-rule fidelity/read-trace comparison; test a hybrid list + conditional table alongside complete tables.** The secondary `deepen_when` is unproven and should be a separate experimental variable, not silently dropped during a format trial.

## Evidence

| Claim | Source link | Evidence type | Supports / undermines |
|---|---|---|---|
| Author's measured three-rule comparison: XML **221**, IF/bullets **198**, table **190** tokens; extrapolated around **-190** for whole block. | [`05-research-prompt-packets.md`, RP-06 preamble](05-research-prompt-packets.md) | Repository-reported local measurement; method and tokenizer not independently replicated here | Supports a table as cheaper **for those specific rules** |
| Vendor guidance treats Markdown sections/lists and XML boundaries as useful ways to distinguish instructions, context and metadata; gives **no uniform XML-vs-table compliance ranking**. | [OpenAI prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering); [Anthropic prompting](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables) | Vendor docs | Supports either clear markup or Markdown; no guarantee of gate enforcement |
| A controlled **July 2026 unreviewed preprint** tested markdown, plain, prose and tabular formats at 10-160 simultaneous instructions over five models; **no consistent format winner**, with model-specific reversals. Exact per-model advantages cannot be transported to coding-agent file reads. | [Eliav, *Prompt Design at Scale*, arXiv:2607.19257](https://arxiv.org/abs/2607.19257) | Controlled preprint; synthetic instruction compliance, **not** file-loading agents | Undermines a universal claim that tables or XML always work best |
| LongTableBench covered **5,950 QA cases** across **seven table representations** and found meaningful limits of format-sensitive long-context table reasoning; its target is **table data comprehension**, not directives in a contract. | [Li et al., EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.638/) | Peer-reviewed controlled benchmark, adjacent domain | Cautions against presuming tables are neutral for comprehension |
| The literal v0.5 XML has **13 unconditional named rule tags, nine conditional named rules**, and **five `deepen_when=` occurrences**. | [`09-contract-block-v0.5.md`, section 2](09-contract-block-v0.5.md) | Repository text inspection (current `main`, 2026-10-20) | Corrects RP-06's stated 12+9 and RP-08/09's inconsistent depth-attribute counts |
| Coding-agent read-trace experiment compares gated and ungated wording, not all serialization variants; its own thresholds are pre-registered but **not executed**. | [`04-empirical-test-protocol.md`, sections 2 and 7](04-empirical-test-protocol.md) | Local protocol (design, not data) | Leaves serialization and conditional compliance unresolved |

## Comparison of required alternatives

**Token figures are the repository's reported three-rule slice, not costs independently measured for the full v0.5 block.** `TBD` is intentional: there is no evidence-backed token figure for that variant.

| Format | Token cost / savings | Parsing and rule-application reliability | Distinct risk; evidence |
|---|---|---|---|
| 1. Paired XML tags with attributes | **221 / three-rule slice**; full existing block **1,622** | Clear labels and metadata; no automatic parser interprets `when` | Attributes *look executable*, though they are model-readable text; [OpenAI](https://developers.openai.com/api/docs/guides/prompt-engineering) |
| 2. Bullet `IF condition -> ref: rule` | **198 / same slice** (23 fewer; **10.4%**) | Clear in natural language; conditional fidelity unmeasured | A multi-clause condition and a reference may be conflated |
| 3. Markdown table | **190 / same slice** (31 fewer; **14.0%**); whole-block saving **~190 hypothesized** | Tabular row/column relationships likely comprehensible, but no relevant measured superiority | Long sentences, `|` inside cells, escaped line breaks and flattened multi-step behavior; [Eliav](https://arxiv.org/abs/2607.19257); [LongTableBench](https://aclanthology.org/2025.findings-emnlp.638/) |
| 4. Abbreviated attributes (`w=`, `r=`) | **TBD**, tokenizer dependent | *Probably* worse self-description for unfamiliar agents | Models must infer an undocumented legend; savings not established |
| 5. Heading per rule, prose condition beneath | **TBD** | Readable and easy to inspect; model benefit unmeasured | Heading markup and repeated labels may use more tokens |
| 6. Hybrid: unconditional bullets, conditional table | **TBD**; cannot automatically reuse either **-39** or **-190** result | Separates always-on obligations from conditional dispatch; plausible semantic clarity | Loses per-rule tag handles, long conditional table cells |
| 7. Runtime-native scoped rules/skills, plus small always-on contract | Token budget **depends on activation**, not measured for repo | Scoped loader gives a concrete loading mechanism; model still may ignore loaded instructions | Portability and configuration across tools; [Claude](https://code.claude.com/docs/en/memory); [Cursor](https://docs.cursor.com/context/rules-for-ai) |

**Ranking for a trial:** (1) existing XML as control; (2) whole-table and hybrid as two compression challengers; (3) conditional bullets as simple fallback; (4) runtime-native scopes where cross-tool behavior permits; (5) headings; (6) abbreviated attributes last. This ranks **experimental priority**, not proven accuracy.

### The three direct answers

1. **Separate 'go deeper' condition:** `deepen_when` names useful distinctions but is **not a parser-controlled trigger**. RP-08 could find no controlled evidence that it earns its cost beyond `when` + `ref`. For v0.5 **five** attributes exist, while the manuscript claims six and nine in different places; the reported **-99-token** saving must be measured on the literal v0.5 before adoption. Test `when+ref` versus `when+ref+deepen_when` with **identical surrounding text**.
2. **Tables and long rule bodies:** Yes, the risk of poorer *human readability* is immediate for multi-sentence cells, and model accuracy could vary, but a quantified model compliance loss on these particular rules has **not been shown**. Splitting one rule across multiple table rows could change meaning. LongTableBench assesses a different domain; Eliav's controlled preprint gives no universal format winner.
3. **Unconditional versus conditional rules:** **Yes**. Unconditional directives can be short labelled bullets; conditional ones need distinguishable applicability, extra-reference location and escalation. A hybrid is architecturally attractive, but its token savings must be measured and its behavioral interpretation tested.

### Same rule, rendered as the recommended hybrid's conditional table row

Existing `<editing>` rule semantics, formatted for *comparison*, not for installation:

| Applies when | Open full reference when | Short rule |
|---|---|---|
| Changing, moving or deleting an existing file | Edit spans multiple blocks or will go to a deterministic executor: `apex-meta/informatics/execution-modes.md` | Replace only exact lines copied from the file just read. Make one edit at a time. Move/copy with `git mv` / `cp`, not by rewriting contents. |

The example preserves the **same depth condition**, so it is an encoding trial, not a `deepen_when` ablation. Keep a separate uncontrolled set of universal rules as labelled bullets if experimenting with hybrid layout.

## Strongest case against the verdict

XML named tags have a **real clarity benefit** for owners: each directive has a stable named boundary, `when` and `ref` are separate fields, and nested formatting can preserve long bodies without unwieldy table cells. Vendor guidance explicitly supports XML for mixed content. If the three-rule table saving came from shortening or omitting semantically important punctuation rather than representational overhead, its inferred ~190 saving is misleading. Format trials can cost more than the eventual context savings, especially when cached input is cheap. The safest production action may be **retain XML permanently** and stop optimizing this axis until a genuine compliance defect appears. Conversely, if matched tests find identical triggering and task completion for a shorter table, refusing the table would irrationally protect an untested aesthetic preference. Neither path is validated without the local trial.

## What I could not find

- A controlled head-to-head test of XML attributes versus `IF ->` bullets versus tables **for conditional tool-based file opening** across ~22 coding-agent directives.
- An independent tokenizer reproduction of the three-rule figures or of the extrapolated full-block **-190**.
- A controlled result showing short `w=` / `r=` attributes retain semantic reliability.
- Evidence of a 10%+ rule-following loss induced specifically by long Markdown table cells in **this** workload.
- A native runtime parser for the custom `when`, `ref`, `deepen_when` syntax in this repository.

## Consequence for the contract

- **`DEC-17`** named tags: the operator's clarity choice **survives as an interim decision**; tests could overturn it, not the token saving alone. The author's **-39 unconditional-tag swap** is not evidence that wholesale format changes only save 39.
- **`DEC-M1`** remains true: all text physically in the always-on file consumes tokens regardless of conditional wording; caching changes price, not presence.
- **`DEC-16` / `DEC-M2`**: no claim of gate success follows from cheaper encoding. Test read traces and compliance separately.
- **`RP-09` floor**: the reported full-table **~1,432** candidate undercuts the assertion that 1,476 is a hard structural floor, **without establishing safe task performance**. A combined table + depth removal cannot be costed by simple addition without remeasurement.
- **Scope discipline**: this report proposes experiments and text examples only. It does **not** change the installed rules, contract candidate, or decision register.
