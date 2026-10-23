---
type: Reference
id: RESULTS-03-currency-check
title: Architecture currency and assumptions - Findings
description: Reviews seven design claims against 2026 coding-agent documentation and empirical studies.
status: current
tags: [research-result, currency, rp-03]
---

# RP-03 - What is this architecture reasoning missing or assuming incorrectly?

**Verdict (confidence: high on the existence of new runtime features; medium on the strength of empirical conclusions):** The three-tier design principle remains usable, but several supporting assertions are **oversimplified or not demonstrated**: there is no evidence that **1,000 tokens** is a universally optimal instruction-file length; "front and end" positioning is not proven to improve obedience inside current coding-agent config files; and **file boundaries are not the only way to defer scope-specific text** when a harness provides native rule/skill attachment. The greatest dated developments are Claude Code's native AGENTS.md support (version 2.1.277+) and audit/loader controls, Gemini's configurable context filenames and imports, Copilot's multi-file instruction support, and agent skills' progressive disclosure. **The broad concept is current; the implementation assumptions lag documented 2026 harness capabilities.**

## Evidence - claim-by-claim verdict

| # | Original design claim | Verdict | Evidence and consequence |
|---:|---|---|---|
| 1 | Always-on + conditioned detail + lookup-only detail is the right three-tier separation | **Current as pattern, not universally correct as implementation** | OpenAI Skills load metadata first and full skill/references later; Cursor supports Always/Auto Attached/Agent Requested/Manual; Claude scoped rules. Distinguish task-conditioned model choice from harness-attached scope. [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills); [Cursor](https://docs.cursor.com/context/rules-for-ai) |
| 2 | Always-loaded instruction text should sit near 1,000 tokens; longer dilutes attention | **Unsupported numeric threshold** | Gloaguen's controlled coding-agent context-file benchmark finds >20% cost increase without general success improvement; it does not establish a 1,000-token optimum. McMillan's 25-500-line study found no detectable adherence effect of file size within its tested range; task identity mattered. [Gloaguen](https://arxiv.org/abs/2602.11988); [McMillan](https://www.alphaxiv.org/abs/2605.10039) |
| 3 | Place critical instructions at the start and end ("lost in middle") | **Oversimplified / population transfer problem** | General long-context retrieval studies motivate concern, but McMillan's *coding-agent config* factorial experiment did not detect a position effect in tested conditions (`p=0.16`). Cannot generalize that null to all tasks or rule types; cannot prescribe exact positioning as a proven compliance lever. [McMillan 2026](https://www.alphaxiv.org/abs/2605.10039) |
| 4 | A condition saves tokens only when it points at a separate file | **True for an already fully injected file, false if claimed as universal architecture** | Model-side `when=` text cannot hide already injected words. However native scoped rules, selective skill loads, and build-time filtered output can conditionally inject a subsection/artifact **without** treating each logical branch as its own top-level `.md` file. [Cursor](https://docs.cursor.com/context/rules-for-ai); [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills); [OASIS DITA processing](https://docs.oasis-open.org/dita/v1.1/CD02/archspec/behaviors.html) |
| 5 | Duplicate rules drift, and contradictions are worse than token redundancy | **First part verified locally; second part too categorical** | `GEMINI.md` lacks a whole informatics section on `main`; unmanaged manual copies demonstrably drift. A coding-agent factorial study did not detect a global compliance penalty from the **single tested direct contradiction**; that is not proof contradictions are harmless generally. More importantly, valid rules can conflict in scope. [Repo five files, `11-instruction-surface-architecture.md`](11-instruction-surface-architecture.md); [McMillan](https://www.alphaxiv.org/abs/2605.10039) |
| 6 | XML delimiters pay only where named attribute handles are needed; Markdown is cheaper elsewhere | **Plausible but not established as response-quality rule** | The actual candidate decomposition puts 111 tokens into tags and 319 into attributes; the repo measures a ~190-token whole-table alternative. Vendor docs recommend structure for delimiting disparate content, not per-rule superiority on this particular instruction mix. [Repo `09-contract-block-v0.5.md`](09-contract-block-v0.5.md); [Anthropic context docs](https://code.claude.com/docs/en/memory) |
| 7 | Hand-authored conditional routing is the correct loading mechanism | **Behind tool-specific practice** | Cursor's path matching/agent-requested modes, Claude path-scoped rules, and OpenAI progressively disclosed skills are available; whether any beat custom IF dispatch **on this repo** is unmeasured. [Cursor](https://docs.cursor.com/context/rules-for-ai); [Claude](https://code.claude.com/docs/en/memory); [OpenAI](https://developers.openai.com/blog/skills-agents-sdk) |

## Not considered - highest architecture impact first

1. **Cross-tool file loading changed and is not universal**. Claude Code v2.1.277+ supports AGENTS.md, but its default **ignores AGENTS.md when root/project CLAUDE instructions exist**, as here. A one-line Claude `@AGENTS.md` import and Gemini `@./AGENTS.md` import are vendor-supported alternatives to hand-maintained duplicate bodies; Copilot CLI can read multiple sources and imports. [Claude](https://code.claude.com/docs/en/memory); [Gemini](https://geminicli.com/docs/cli/gemini-md/); [Copilot](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions). **Impact: high**; requires reconciling `DEC-21`, not immediate implementation.
2. **Deterministic harness scope triggers exist**: file globs/path-scoped rules can load appropriate instructions when working on matching files, eliminating some language-model classifications. [Cursor](https://docs.cursor.com/context/rules-for-ai); [Claude](https://code.claude.com/docs/en/memory). **Impact: high**, tool-dependent.
3. **Skills are a standard progressive-disclosure primitive**: short name/description visible first, full instructions when selected; still model-mediated activation, with missed-selection risk. [OpenAI Skills](https://developers.openai.com/api/docs/guides/tools-skills); [OpenAI September 11, 2026 design discussion](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). **Impact: high** for conditional procedures; not a replacement for critical always-on rules.
4. **Prompt caching changes the economics**: OpenAI documents 1.25x cache writes and typical 0.1x reads for GPT-5.6+, alongside exact-prefix conditions; Anthropic and Gemini have independent mechanisms and minima. This reduces recurring input price, not context occupancy or obedience failures. [OpenAI](https://developers.openai.com/api/docs/guides/prompt-caching); [Google](https://ai.google.dev/gemini-api/docs/caching?lang=python). **Impact: high** on cost premise.
5. **Published 2026 coding-agent instruction file studies challenge structure folklore**: Gloaguen (Feb 2026 submission) finds inflated cost without reliable task-success gains; McMillan (May 2026) fails to detect several manipulated structural effects and finds task-dependent adherence. **Impact: high** on what to optimize, medium on generalization. [Gloaguen](https://arxiv.org/abs/2602.11988); [McMillan](https://www.alphaxiv.org/abs/2605.10039).
6. **Prompt audits/version checks** are shipping runtime capabilities: Claude's `/doctor prompt-audit` (documented from 2.1.283) can surface stale references/conflicts without a bespoke contract linter. Audit is not a replacement for behavioral evaluation. [Claude](https://code.claude.com/docs/en/memory). **Impact: medium** on maintenance.
7. **Universal vs repo-specific contract layers** should be distinct even if loaded together: one canonical universal source; repo facts in a separately marked section; tool entrypoints are adapters. [Repo `11-instruction-surface-architecture.md`](11-instruction-surface-architecture.md) (original open question); vendor import sources above. **Impact: high** on portability, none on runtime token count by itself.

## Still correct

- A file already fully injected incurs its full input-token footprint even when its contents contain a conditional `when=`. This is true by mechanism, independent of model quality.
- Duplicated manual rule sets create a measurable risk of drift in this repository: `GEMINI.md` is missing a whole section and the three instruction files differ. This risk should be removed by single-source ownership, not wished away.
- Task-specific details generally should not all be loaded into every session; vendor skill and scoped-rule products implement related selective-loading patterns.
- Critical operator-specific invariants still need a guaranteed entrypoint and tests when action enforcement matters. Retrieval-only instruction selection cannot provide that guarantee.

## Strongest case against the verdict

The repository is not necessarily on the versions needed for newer loader behavior. Built-in scoped rules can add hidden triggers and vendor dependencies, whereas a plain small root `AGENTS.md` plus conditional file links is easier to port. Controlled studies of context files are not controlled tests of this specific contract, and the 1,000-token goal may still be a useful *operational budget* if a team can show savings on its own tasks. Consequently these findings argue for a comparison, not for wholesale abandonment of static dispatch.

## What I could not find

- A vendor-neutral standard that guarantees **identical** path-scoped rules across all target IDEs, cloud agents and CLIs.
- A controlled replication of all seven claims on the operator's exact five-file layout and current model versions.
- The repo's measured cache hit rate, live instruction selection traces or a tested value for a 1,000-token maximum.
- Rigorous per-rule XML-vs-table comprehension comparisons in this exact domain.

## Consequence for the contract

- `DEC-16` and `DEC-M3`: retain narrow "already-loaded text cannot become un-loaded" arithmetic; correct any universal claim that *file boundary alone* enables selective loading.
- `DEC-17`: naming clarity remains operator-selected; direct performance evidence remains absent.
- `DEC-21`: reconsider carrier copies in light of official 2026 AGENTS.md/import semantics.
- `DEC-M1` and `DEC-M4`: deterministic byte/token accounting remains a useful **size** measurement, not an instruction-effectiveness result.
- Global recommendation: label tool/version, observed read traces, and billing mode separately; prefer native scope facilities where portable and available.
