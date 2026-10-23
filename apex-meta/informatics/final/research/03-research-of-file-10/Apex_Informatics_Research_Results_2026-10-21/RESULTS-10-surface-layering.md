---
type: Reference
id: RESULTS-10-surface-layering
title: Instruction surfaces and universal layering - Findings
description: Verifies major agents' instruction-file loading and recommends a portable layer without unverified copy synchronization.
status: current
tags: [research-result, surfaces, layering, rp-10]
---

# RP-10 - Which tools load which instruction files, and where should universal instructions live?

**Verdict (confidence: high for the cited vendor-documented support, medium for the recommended interoperability design, low for behavior in the operator's untested local versions):** `AGENTS.md` is **supported by several major agents but not unconditionally loaded by every client, in every configuration**. Critically, Claude Code **v2.1.277+ supports AGENTS.md natively**, but when this repository contains `CLAUDE.md` and `.claude/CLAUDE.md`, the default is to load Claude files **instead**; Gemini CLI defaults to `GEMINI.md` unless configured otherwise. GitHub Copilot support varies by client. The prior `DEC-21` three-byte-identical-copy solution is **not necessary as a permanent architecture**: Claude Code, Gemini CLI, and Copilot CLI document real import/include mechanisms, allowing one canonical `AGENTS.md` plus tool-specific entrypoints. Preserve compatibility for surfaces that lack imports or fail to load AGENTS.md automatically; do not delete any file on research evidence alone.

## Evidence - Part 1: actual file-loading matrix

Legend: **Y** = vendor-documented native load in ordinary supported mode; **C** = conditional; **N** = not a documented discovery target, **U** = unverified. "Reads" means vendor-documented loader behavior, **not** independently traced on this machine. Local repo contents confirmed via GitHub `main` on 2026-10-20.

| Tool / surface | `AGENTS.md` | `CLAUDE.md` | `GEMINI.md` | `.claude/CLAUDE.md` | `.github/copilot-instructions.md` | Source / precedence |
|---|---|---|---|---|---|---|
| **Codex CLI** | **Y**, hierarchical root-to-CWD, `AGENTS.override.md` override; opt-in by file presence | **N**, unless configured as alternate filename | **N**, unless configured as alternate filename | **N** | **N** | [OpenAI Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide); [Codex workflow](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex) |
| **Claude Code >=2.1.277, default** | **C**: Y only if no relevant project `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` | **Y** (root/parents) | **N** | **Y**, and can block `AGENTS.md` default | **N** | [Anthropic official memory docs, AGENTS.md and precedence](https://code.claude.com/docs/en/memory) |
| **Claude Code configured 'both'** | **Y**, if setting `claude-md-and-agents-md` | **Y** | **N** | **Y** | **N** | [Anthropic `Project instructions` modes](https://code.claude.com/docs/en/memory) |
| **Gemini CLI, default** | **N**, unless explicitly imported or configured | **N**, unless configured through `context.fileName` | **Y**, root + ancestor + just-in-time child | **N** | **N** | [Gemini CLI context hierarchy, imports and configuration](https://geminicli.com/docs/cli/gemini-md/) |
| **Gemini CLI configured** | **C**: Y if `context.fileName` includes `AGENTS.md` | **C**: possible if configured | **C**: possible when retained | **N** unless named and relevant | **N** unless named and relevant | [Gemini `context.fileName` documentation](https://geminicli.com/docs/reference/configuration/) |
| **GitHub Copilot CLI** | **Y** | **Y** | **Y** | **Y**, documented alternate Claude path | **Y** | [GitHub Copilot CLI instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions); combines applicable files and deduplicates some identical copies; **no general precedence** |
| **Copilot cloud agent** | **Y** | **Y** | **Y** | **U** as project agent context (not documented here) | **Y** | [GitHub support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support); support varies across Copilot modes |
| **Copilot Chat in VS Code** | **Y** | **N** per native supported-types matrix | **N** per matrix | **N** per matrix | **Y** | [GitHub support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support); applicable rules combined, no universal priority |
| **Cursor** | **Y** root only in documented v1.5 behavior | **N** as native repo rule | **N** | **N** | **N** | [Cursor official rules](https://docs.cursor.com/context/rules-for-ai): `.cursor/rules/*.mdc` is richer alternative; nested AGENTS.md is not supported in cited version |

**Other widely used agent:** Windsurf Cascade has an independent rules system and pre-read hooks, but its exact default support for all five filenames was **not established** from sufficient first-party evidence in this run. Mark `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/CLAUDE.md`, and `.github/copilot-instructions.md` as **U**, not Y, for Windsurf. [Windsurf hook documentation](https://docs.windsurf.com/windsurf/cascade/hooks).

### Precedence, subdirectories and imports

- **Codex:** Global-to-directory instructions are merged in path order, with more specific directory context later; `AGENTS.md` is **optional**, not generated for all repositories by convention. Trust/configuration can affect loading. [OpenAI](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.3-codex).
- **Claude Code:** Default `CLAUDE.md` **or** `AGENTS.md`, not both. A `CLAUDE.md` in `.claude/` counts for suppressing native AGENTS.md loading. `@AGENTS.md` in `CLAUDE.md` is a genuine **eager import**; Claude supports nested project guidance and `.claude/rules/*.md` with `paths:`. Check `/memory` or `/context`. [Anthropic](https://code.claude.com/docs/en/memory).
- **Gemini CLI:** `GEMINI.md` hierarchy is concatenated global -> workspace -> JIT when touched; `@./AGENTS.md` is a real import, and configuring `context.fileName` to `AGENTS.md` is also supported. Verify exact content via `/memory show`. [Gemini CLI](https://geminicli.com/docs/cli/gemini-md/).
- **Copilot:** It is a product family, not one loader. CLI combines instructions and supports `@relative/path` in `AGENTS.md`, `CLAUDE.md` and `.github/copilot-instructions.md`, but not in `GEMINI.md`; Copilot code review and different IDEs expose different sets of files. Copilot CLI **subagents may not inherit repository instructions by default**. [GitHub CLI docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions); [feature matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support).
- **Cursor:** `AGENTS.md` is a simple root-level option; file-pattern automatic attachment is in `.cursor/rules/*.mdc`, not in plain AGENTS.md. [Cursor](https://docs.cursor.com/context/rules-for-ai).

### Local repository verification

`AGENTS.md` and `CLAUDE.md` contain `## Informatics & Knowledge Routing`; `GEMINI.md` **does not** on `main` fetched 2026-10-20. All five reported instruction files exist. `CLAUDE.md` and `.claude/CLAUDE.md` coexist, so Claude Code's default AGENTS.md support **does not rescue this repository from drift by itself**. This is a real compatibility and routing issue, not an assumption. Evidence: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/CLAUDE.md`, `.github/copilot-instructions.md` as fetched from `main`.

## Part 2 - Ranked layering recommendation

| Rank / alternative | Portability, drift, cost | Survives actual loading behavior? | Recommendation |
|---|---|---|---|
| **1. One canonical repo-root `AGENTS.md` with clearly separated UNIVERSAL and REPOSITORY sections; thin tool-specific entrypoints** | Single maintained rule body, local visibility, minimal sync error; cross-repo universal segment still needs a source-of-truth mechanism | **Yes with documented adapters:** Claude root `CLAUDE.md` may `@AGENTS.md`; Gemini `GEMINI.md` may `@./AGENTS.md`; Codex, Cursor and compatible Copilot read AGENTS.md directly. Copilot product variants may still need `.github` rules | **Best immediate option**, but operator must reconcile existing tool-specific content and evaluate eager-import exception |
| **2. Two files, `UNIVERSAL.md` + per-repo instructions, imported by root instruction files** | More portable and separately versionable; adds an eager loader hop, and some clients don't support imports | **Mixed**: Claude/Gemini/Copilot CLI support imports; Codex has no vendor-documented universal `@path` include behavior comparable to those importers | Defer unless universal content spans many repos and distribution is proven |
| **3. Versioned universal package installed into each repo (generated output)** | Strong single-source provenance; requires synchronization/change review, but can produce plain `AGENTS.md` artifacts understandable by every tool | **Yes**, because generated outputs are ordinary files. Generation is build-time, not per-agent imports | Best long-term multi-repo option **if** the number of consumer repos justifies it. Not required for this research-only run |
| **4. Universal rules in skills/tool descriptions only** | Smaller baseline, but no guaranteed activation for universal rules; different agent surface coverage | **No as sole carrier**: tool descriptions trigger only when used; skills can be discoverable rather than auto-loaded | Complement for detailed conditional workflows, never replacement for critical always-on invariants |
| **5. Three byte-identical copies hand maintained + equality test (`DEC-21`)** | Explicit compatibility but multiplies content and opportunities for drift | **Yes**, mechanically, yet unnecessary for several documented loaders | Fallback for unsupported environments; **not** preferred permanent design |

## Part 3 - Direct answers

**Are three byte-identical hand-maintained copies the correct 2026 solution?** **No, as a default design.** A canonical `AGENTS.md` with supported imports/aliases or an installation-time generated artifact supersedes uncontrolled triple editing. However, because the repo's current Claude files suppress native AGENTS.md and Gemini defaults to GEMINI.md, **simply deleting `CLAUDE.md` and `GEMINI.md` would be unsafe**, especially while `.claude/CLAUDE.md` remains.

**Where should portable universal content live?** Initially as a **clearly delimited, versioned canonical section** of `AGENTS.md`, consumed through supported tool-specific entrypoints. If reused across several repos, make a separately versioned source artifact or package and distribute reviewed copies at install/update time. For machine-specific preferences, optional user-level global files exist (Claude `~/.claude/CLAUDE.md`, Codex `~/.codex/AGENTS.md`, Gemini `~/.gemini/GEMINI.md`); those are **not shared, repo-versioned portability solutions**. [Claude](https://code.claude.com/docs/en/memory); [Codex](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide); [Gemini](https://geminicli.com/docs/cli/gemini-md/).

## Strongest case against the verdict

Shims and imports are additional loader-specific moving parts; import support differs even inside one vendor's product. A fully duplicated compact block avoids uncertainty when portability matters more than editing overhead. Also, a file that auto-loads across agents may expose unnecessary rules and inflate inference cost. If the organization must support old Claude Code, multiple Copilot clients, sandboxed agent runtimes and diverse IDEs without a controlled version matrix, **generated copies** may be more reliable than imports. The correct object of elimination is **hand maintenance**, not necessarily identical deployed bytes.

## What this invalidates

- **`DEC-21` rationale partly invalidated:** "imports are not supported across target tools" is no longer true for Gemini CLI or Copilot CLI; Claude Code now has native AGENTS.md capability as well. An equality test over three hand copies is not the only workable resolution.
- **Repo-wide native `AGENTS.md` assumption falsified:** Claude's default loader in the present five-file setup will not necessarily read it; Gemini defaults to another filename.
- **Universal/repo mixing:** no need to make source content non-portable; use a universal and repo-specific separation within the owner until a multi-repo distribution mechanism is justified.
- **`D10` remains real:** the absent Gemini routing section must be resolved as a distinct implementation task after operator review, not silently changed by this research package.

## What I could not find

- Empirical launch traces and actual installed **local version/settings** of all agents used by the operator.
- One universally implemented, unconditional cross-tool `@path` include standard that *every* tool/IDE mode honors.
- Definitive 2026 Windsurf file-discovery/precedence for all five filenames with enough first-party evidence.
- A proven end-to-end automated portability tool that preserves the repository's invariants across all five surfaces with no build-time or runtime compatibility exceptions.

## Consequence for the contract

**Do not implement `DEC-21`'s three-copy byte-identity test as an irreversible architectural commitment.** Treat its motivation (same universal meaning for all tools) as sound, and the manual-copy mechanism as supersedable. Author one canonical universal body plus repo-specific facts, use documented shims where necessary, and locally inspect loaded context in each target tool/version before removing copies. `DEC-12` and `DEC-13` remain proposed, not made true by these compatibility findings.
