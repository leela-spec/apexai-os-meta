---
okf_version: "0.2"
type: future-development
title: Deferred QMD skill install (private Hermes) — local hybrid search for the Obsidian vault
description: Installing Hermes' official "qmd" skill (local BM25 + vector + reranked search over the vault) was attempted and deferred after Hermes' own security scanner returned a DANGEROUS verdict. Recorded for future realization with a lower-risk recipe and revisit triggers.
tags: [hermes, qmd, obsidian, search, security, deferred, future-development]
status: deferred
decided: 2026-10-01
program_ref: apexai-os-meta/apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md (T20)
---

# Deferred: QMD skill install (private Hermes)

## Operator decision (2026-10-01): **DEFER**
`hermes skills install official/research/qmd` on the private instance returned a **DANGEROUS**
scan verdict. The operator does not want to proceed on that basis. This file records what QMD
is, why the scan fired, which of those risks are actually real in this environment, and a
ready-to-run lower-risk recipe so it can be picked up later without re-analysis.

## What it is (plain terms)
QMD (`@tobilu/qmd`, by Tobi Lütke) is a local search tool: it combines ordinary keyword search,
AI-style meaning-based search, and a re-ranking pass, all running on-device over the Markdown
vault — no cloud calls. Hermes has an official optional skill that installs and wires it up as
an on-demand tool the agent can call when answering questions from the vault.

## Why it would matter later (the value)
- Plain keyword search misses relevant notes that use different words for the same idea; QMD's
  meaning-based layer catches those.
- Pure meaning-based search alone is often imprecise for exact terms (names, error strings);
  QMD's keyword layer plus reranking fixes that.
- It's the one piece this session's `transcript-to-vault` skill defers to for indexing — without
  it, newly written notes are not re-indexed for fast semantic search (they're still on disk and
  readable, just not search-optimized).

## Why it was deferred — the scan, and what's actually true here
Hermes' scanner flagged four things. Checked against the real skill source and this specific
container, only one is a genuine live risk:

| Scanner flag | Severity | Actually true in this container |
|---|---|---|
| `sudo apt-get install nodejs` | HIGH | Node v26.5.1 is already installed here. The skill's own install steps check for Node first and only escalate if missing — moot, provided that check is actually followed rather than skipped. |
| systemd/launchd daemon setup | MEDIUM | This container runs `s6-svscan`, not systemd or launchd. The step would fail/no-op, not succeed-and-persist. Separately, the daemon is **optional** — an on-demand, no-daemon mode exists and is the documented default for light use (~19s cold start per query). |
| Edits `~/.hermes/config.yaml` | CRITICAL | Real, but limited to adding one `mcp_servers.qmd: {command: qmd, args: [mcp]}` entry — a placeholder for exactly this already exists in the live config, currently `enabled: false`. |
| Unpinned `npm install -g @tobilu/qmd` | MEDIUM | **The one real, unavoidable risk** — always installs whatever is currently tagged `latest`. Same category of risk already accepted for the `langextract-usage` skill's unpinned `pip install langextract`. |

## Trigger to revisit (do it when ANY of these become true)
- QMD (or Hermes' own skill for it) ships a release that pins a specific npm version instead of
  `latest`, removing the one real residual risk.
- The vault grows large/varied enough that plain `qmd update` (CLI, no MCP skill) or manual
  `grep`/Obsidian search stops being good enough for finding things.
- The operator decides the unpinned-install risk is acceptable as-is (it's the same class of
  risk already accepted elsewhere in this stack).

## Ready-to-run recipe (lower-risk than the default skill install, for whoever implements this later)
Skip the full `hermes skills install official/research/qmd` flow (it would still trip the
scanner). Do the minimal, container-appropriate version by hand instead:
1. `docker exec ki-basis-hermes npm install -g @tobilu/qmd` — Node/npm already present, no sudo
   needed. (Pin a specific version here once one is confirmed stable, instead of `latest`.)
2. Verify: `docker exec ki-basis-hermes qmd --version`.
3. Edit `/root/.hermes/config.yaml` (back up first, matching the existing
   `config.yaml.bak-<timestamp>` convention): flip the existing `mcp_servers.qmd.enabled` to
   `true`. Do not add anything else — no daemon, no systemd/launchd step.
4. Restart `ki-basis-hermes` (`docker restart ki-basis-hermes`) so the MCP entry is picked up.
5. Verify: ask Hermes a vault question that requires search; confirm it calls the `qmd` MCP tool
   and returns results.
6. Only if query latency becomes a real problem: revisit the optional background-daemon mode
   from the official skill doc — but re-check for an s6-compatible supervision approach first,
   since the skill's own systemd/launchd steps still won't work in this container as written.

## Related
- This decision's trigger: `apex-meta/SmallSkills/Transcription2KnowledgeBase/00_README.md` (component status table) and `SKILL.md` (Pitfalls section) in the same project — `transcript-to-vault`'s Step 7 falls back to a bare `qmd` CLI call until this is resolved.
- Sibling deferred-item convention: `ki-basis/docs/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md`.
