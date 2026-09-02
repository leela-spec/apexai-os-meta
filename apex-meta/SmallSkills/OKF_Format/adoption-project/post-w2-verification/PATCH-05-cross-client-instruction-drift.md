---
type: Plan
title: PATCH-05 — Cross-Client Instruction Drift
description: Exact-match patch pack to stop Cursor, Kiro, Windsurf, generic agent, and Hermes instruction surfaces from misidentifying the Apex repository as an Obsidian-only wiki framework.
tags: [patch, cursor, kiro, windsurf, hermes, agents, routing]
status: proposed_not_applied
---

# Intent

Remove the highest-impact cross-client prompt drift while preserving existing wiki capabilities as opt-in support.

Current failure mode:

```text
normal Apex request
  -> client loads always-on Obsidian rule
  -> repo is falsely classified as an Obsidian Wiki framework
  -> stale .skills/wiki-* routes can outrank current APEX OS routing
```

Target behavior:

```text
normal Apex request
  -> shared repo authority / client router
  -> selected APEX entrypoint

explicit wiki/vault request
  -> client-local wiki compatibility capability
```

This patch intentionally does **not** normalize or delete mirrored Skill packages. That requires a separate inventory of canonical source, generated mirror, client-specific adaptation, and dead copy.

**Do not apply this file as a whole-file rewrite. Apply each exact-match block independently.**

# A. Cursor — make the Obsidian rule conditional

Current Cursor frontmatter makes this file universal twice: `alwaysApply: true` and `globs: "**/*"`. Remove both universal triggers and let the description route only explicit wiki/vault work.

## Block 1 — Cursor rule frontmatter

<file>.cursor/rules/obsidian-wiki.mdc</file>
<old>---
description: Obsidian Wiki skill-based framework for building and maintaining knowledge bases. Use these rules whenever engaging with the vault, wiki, ingestion, or knowledge management.
globs: "**/*"
alwaysApply: true
---</old>
<new>---
description: Use only for explicit Obsidian wiki or vault setup, ingest, query, maintenance, migration, or repair work. This is a legacy compatibility capability inside APEX OS, not the repository identity.
alwaysApply: false
---</new>

## Block 2 — Cursor rule body

<file>.cursor/rules/obsidian-wiki.mdc</file>
<old># Obsidian Wiki — Agent Context

This project is a **skill-based framework** for building and maintaining an Obsidian knowledge base.

## Quick Orientation

1. Resolve config via `AGENTS.md`: honor an inline `@name` vault override first, then `.env`, then the global config (`~/.config/obsidian-wiki/config`, XDG-style; legacy `~/.obsidian-wiki/config` still honored). This gives `OBSIDIAN_VAULT_PATH` — where the wiki lives.
2. Read `.manifest.json` at the vault root to see what's already been ingested.
3. Skills are in `.skills/` (also at `.cursor/skills/`). Each subfolder has a `SKILL.md`.

## When to Use Skills

| User says something like… | Read this skill |
|---|---|
| "set up my wiki" / "initialize" | `.skills/wiki-setup/SKILL.md` |
| "ingest" / "add this to the wiki" / "process this export" / "ingest this data" | `.skills/wiki-ingest/SKILL.md` |
| "/wiki-history-ingest claude" / "/wiki-history-ingest codex" | `.skills/wiki-history-ingest/SKILL.md` |
| "import my Claude history" | `.skills/claude-history-ingest/SKILL.md` |
| "import my Codex history" | `.skills/codex-history-ingest/SKILL.md` |
| "what's the status" / "show the delta" | `.skills/wiki-status/SKILL.md` |
| "what do I know about X" / any question | `.skills/wiki-query/SKILL.md` |
| "use my vault as context" / "context pack for X" / "bounded context" | `.skills/wiki-context-pack/SKILL.md` |
| "audit" / "lint" / "find broken links" | `.skills/wiki-lint/SKILL.md` |
| "rebuild" / "start over" / "archive" | `.skills/wiki-rebuild/SKILL.md` |
| "link my pages" / "cross-reference" | `.skills/cross-linker/SKILL.md` |
| "fix my tags" / "normalize tags" | `.skills/tag-taxonomy/SKILL.md` |
| "create a new skill" | `.skills/skill-creator/SKILL.md` |

## Key Rules

- **Compile, don't retrieve.** Update existing pages, don't just append.
- **Always update `.manifest.json`** after ingesting.
- **Always update `index.md` and `log.md`** after any operation.
- **Use `[[wikilinks]]`** to connect related pages.
- **Frontmatter is required** on every wiki page.</old>
<new># Obsidian Wiki — Cursor Compatibility

APEX OS is the repository identity. Follow `AGENTS.md` for shared repository invariants and use current APEX entrypoints for normal work.

Apply this rule only after the operator explicitly asks for Obsidian wiki/vault work. Then inspect the matching `.cursor/skills/` package before acting and follow that package's current contract.

Do not route arbitrary repository questions to a wiki-query Skill. Do not impose Obsidian wikilinks, manifests, or wiki frontmatter on general APEX documentation.</new>

# B. Kiro — use conditional auto inclusion

Kiro supports auto-included steering files selected from their name and description. The existing `inclusion: always` incorrectly makes a legacy wiki capability the project identity.

## Block 3 — Kiro steering frontmatter

<file>.kiro/steering/obsidian-wiki.md</file>
<old>---
inclusion: always
---</old>
<new>---
inclusion: auto
name: obsidian-wiki
description: Use only for explicit Obsidian wiki or vault setup, ingest, query, maintenance, migration, or repair work. This is a legacy compatibility capability inside APEX OS, not the repository identity.
---</new>

## Block 4 — Kiro steering body

<file>.kiro/steering/obsidian-wiki.md</file>
<old># Obsidian Wiki — Agent Context

This project is a **skill-based framework** for building and maintaining an Obsidian knowledge base.

## Quick Orientation

1. Resolve config via `AGENTS.md`: honor an inline `@name` vault override first, then `.env`, then the global config (`~/.config/obsidian-wiki/config`, XDG-style; legacy `~/.obsidian-wiki/config` still honored). This gives `OBSIDIAN_VAULT_PATH` — where the wiki lives.
2. Read `.manifest.json` at the vault root to see what's already been ingested.
3. Skills are in `.skills/` (also at `.kiro/skills/`). Each subfolder has a `SKILL.md`.

## When to Use Skills

| User says something like… | Read this skill |
|---|---|
| "set up my wiki" / "initialize" | `wiki-setup` |
| "ingest" / "add this to the wiki" / "process these docs" / "process this export" / "ingest this data" | `wiki-ingest` |
| "import my Claude history" / "mine my conversations" | `claude-history-ingest` |
| "import my Codex history" | `codex-history-ingest` |
| "import my Hermes history" | `hermes-history-ingest` |
| "import my OpenClaw history" | `openclaw-history-ingest` |
| "import my Pi history" | `pi-history-ingest` |
| "what's the status" / "show the delta" | `wiki-status` |
| "what do I know about X" | `wiki-query` |
| "use my vault as context" / "context pack for X" / "bounded context" | `wiki-context-pack` |
| "audit" / "lint" / "find broken links" | `wiki-lint` |
| "rebuild" / "archive" / "restore" | `wiki-rebuild` |
| "link my pages" / "cross-reference" | `cross-linker` |
| "fix my tags" | `tag-taxonomy` |
| "update wiki" / "sync to wiki" | `wiki-update` |
| "export wiki" / "export graph" | `wiki-export` |

## Core Rules

- **Compile, don't retrieve** — update existing pages, don't append or duplicate.
- **Track everything** — update `.manifest.json`, `index.md`, and `log.md` after every operation.
- **Connect with `[[wikilinks]]`** — every page should link to related pages.
- **Frontmatter required** — every page needs `title`, `category`, `tags`, `sources`, `created`, `updated`.

For full context, read `AGENTS.md` at the repo root.</old>
<new># Obsidian Wiki — Kiro Compatibility

APEX OS is the repository identity. Follow `AGENTS.md` for shared repository invariants and use current APEX entrypoints for normal work.

Apply this steering file only for an explicit Obsidian wiki/vault task. Then inspect the matching `.kiro/skills/` package before acting and follow that package's current contract.

Do not route generic knowledge questions or normal repository maintenance into the wiki system. Obsidian-specific manifests, wikilinks, and page metadata apply only inside the selected wiki/vault workflow.</new>

# C. Windsurf — remove false identity without guessing a new activation schema

The currently committed Windsurf file uses `activation: "always-on"`. This audit did not establish the exact activation-key migration supported by the user's active Windsurf/Devin host. Therefore this patch removes the dangerous content immediately but preserves the existing activation field. A later runtime-specific patch may make it conditional after host verification.

## Block 5 — Windsurf frontmatter description/name only

<file>.windsurf/rules/obsidian-wiki.md</file>
<old>---
name: "Obsidian Wiki"
activation: "always-on"
---</old>
<new>---
name: "APEX OS Compatibility"
activation: "always-on"
---</new>

## Block 6 — Windsurf body

<file>.windsurf/rules/obsidian-wiki.md</file>
<old># Obsidian Wiki — Agent Context

This project is a **skill-based framework** for building and maintaining an Obsidian knowledge base.

## Quick Orientation

1. Resolve config via `AGENTS.md`: honor an inline `@name` vault override first, then `.env`, then the global config (`~/.config/obsidian-wiki/config`, XDG-style; legacy `~/.obsidian-wiki/config` still honored). This gives `OBSIDIAN_VAULT_PATH` — where the wiki lives.
2. Read `.manifest.json` at the vault root to see what's already been ingested.
3. Skills are in `.skills/` (also at `.windsurf/skills/`). Each subfolder has a `SKILL.md`.

## When to Use Skills

| User says something like… | Read this skill |
|---|---|
| "set up my wiki" / "initialize" | `.skills/wiki-setup/SKILL.md` |
| "ingest" / "add this to the wiki" / "process this export" / "ingest this data" | `.skills/wiki-ingest/SKILL.md` |
| "/wiki-history-ingest claude" / "/wiki-history-ingest copilot" / "/wiki-history-ingest codex" / "/wiki-history-ingest hermes" / "/wiki-history-ingest openclaw" / "/wiki-history-ingest pi" | `.skills/wiki-history-ingest/SKILL.md` |
| "import my Claude history" | `.skills/claude-history-ingest/SKILL.md` |
| "import my Codex history" | `.skills/codex-history-ingest/SKILL.md` |
| "import my Pi history" | `.skills/pi-history-ingest/SKILL.md` |
| "what's the status" / "show the delta" | `.skills/wiki-status/SKILL.md` |
| "what do I know about X" / any question | `.skills/wiki-query/SKILL.md` |
| "use my vault as context" / "context pack for X" / "bounded context" | `.skills/wiki-context-pack/SKILL.md` |
| "audit" / "lint" / "find broken links" | `.skills/wiki-lint/SKILL.md` |
| "rebuild" / "start over" / "archive" | `.skills/wiki-rebuild/SKILL.md` |
| "link my pages" / "cross-reference" | `.skills/cross-linker/SKILL.md` |
| "fix my tags" / "normalize tags" | `.skills/tag-taxonomy/SKILL.md` |
| "create a new skill" | `.skills/skill-creator/SKILL.md` |

## Key Rules

- **Compile, don't retrieve.** Update existing pages, don't just append.
- **Always update `.manifest.json`** after ingesting.
- **Always update `index.md` and `log.md`** after any operation.
- **Use `[[wikilinks]]`** to connect related pages.
- **Frontmatter is required** on every wiki page.</old>
<new># APEX OS — Windsurf Compatibility

`AGENTS.md` is the shared repository operating authority. Do not classify this repository as an Obsidian Wiki framework and do not route ordinary questions into wiki Skills.

Obsidian wiki/vault support is an opt-in capability only. When the operator explicitly requests that capability, inspect the matching `.windsurf/skills/` package and follow its current contract. Otherwise no Obsidian-specific manifest, wikilink, or frontmatter rule applies.</new>

# D. Generic `.agent` client — neutralize the always-on stale identity

The host-specific activation semantics of `.agent/rules/` were not independently established in this review. Preserve its current key and make the always-loaded content safe and minimal.

## Block 7 — generic agent rule frontmatter

<file>.agent/rules/obsidian-wiki.md</file>
<old>---
alwaysApply: true
description: Obsidian Wiki skill-based framework — routing, conventions, and core rules.
---</old>
<new>---
alwaysApply: true
description: APEX OS compatibility rule. Obsidian wiki/vault capabilities are opt-in only and do not define the repository identity.
---</new>

## Block 8 — generic agent rule body

<file>.agent/rules/obsidian-wiki.md</file>
<old># Obsidian Wiki — Agent Context

This project is a **skill-based framework** for building and maintaining an Obsidian knowledge base.

## Quick Orientation

1. Resolve config via `AGENTS.md`: honor an inline `@name` vault override first, then `.env`, then the global config (`~/.config/obsidian-wiki/config`, XDG-style; legacy `~/.obsidian-wiki/config` still honored). This gives `OBSIDIAN_VAULT_PATH` — where the wiki lives.
2. Read `.manifest.json` at the vault root to see what's already been ingested.
3. Skills are in `.skills/` (also at `.agents/skills/`). Each subfolder has a `SKILL.md`.

## When to Use Skills

| User says something like… | Read this skill |
|---|---|
| "set up my wiki" / "initialize" | `wiki-setup` |
| "ingest" / "add this to the wiki" / "process this export" / "ingest this data" | `wiki-ingest` |
| "import my Claude history" | `claude-history-ingest` |
| "import my Codex history" | `codex-history-ingest` |
| "import my Hermes history" | `hermes-history-ingest` |
| "import my OpenClaw history" | `openclaw-history-ingest` |
| "import my Pi history" | `pi-history-ingest` |
| "what's the status" / "show the delta" | `wiki-status` |
| "what do I know about X" | `wiki-query` |
| "use my vault as context" / "context pack for X" / "bounded context" | `wiki-context-pack` |
| "audit" / "lint" / "find broken links" | `wiki-lint` |
| "rebuild" / "archive" / "restore" | `wiki-rebuild` |
| "link my pages" / "cross-reference" | `cross-linker` |
| "fix my tags" | `tag-taxonomy` |
| "update wiki" / "sync to wiki" | `wiki-update` |
| "export wiki" / "export graph" | `wiki-export` |

## Core Rules

- **Compile, don't retrieve** — update existing pages, don't append or duplicate.
- **Track everything** — update `.manifest.json`, `index.md`, and `log.md` after every operation.
- **Connect with `[[wikilinks]]`** — every page should link to related pages.
- **Frontmatter required** — every page needs `title`, `category`, `tags`, `sources`, `created`, `updated`.

For full context, read `AGENTS.md` at the repo root.</old>
<new># APEX OS — Generic Agent Compatibility

Follow `AGENTS.md` for shared repository invariants and current routing. Do not classify this repository as an Obsidian Wiki framework.

Obsidian wiki/vault Skills are opt-in support. Use them only when the operator explicitly requests wiki/vault setup, ingest, query, maintenance, migration, or repair. For that task, inspect the matching `.agents/skills/` package before acting.

Do not impose wiki-specific manifests, wikilinks, metadata, or query routing on general Apex work.</new>

# E. Hermes — synchronize the current shared route without deleting the compatibility file

The current `.hermes.md` is an older copy of the shared root operating rules and lacks the W1 informatics route. Do not delete or replace it with an import until the active Hermes host confirms its startup-loading behavior.

## Block 9 — identify the surface correctly

<file>.hermes.md</file>
<old># Codex Operating Note</old>
<new># Hermes Operating Note

Shared repository authority: `AGENTS.md`. This file is a Hermes compatibility surface and must not override newer shared repository rules.</new>

## Block 10 — add the current Informatics route

<file>.hermes.md</file>
<old>- No-changelog: Do not retain old errors, rejected options, prior versions, incident narratives, or "what changed" explanations in current-truth content.

## Apex KB Dispatch</old>
<new>- No-changelog: Do not retain old errors, rejected options, prior versions, incident narratives, or "what changed" explanations in current-truth content.

## Informatics & Knowledge Routing
- Trigger: Requests to create, edit, audit, or validate repository knowledge files or documentation follow the canonical standard at `apex-meta/informatics/index.md`.
- Authority: The canonical profile in `apex-meta/informatics/standard.md` overrides ad-hoc formatting conventions or generic agent habits.

## Apex KB Dispatch</new>

# Not patched in this wave

## Root `CLAUDE.md`

It remains a byte-style compatibility mirror of `AGENTS.md`, while `.claude/CLAUDE.md` is the actual APEX Claude activation router. Do not delete or import-rewrite it until a real Claude `/memory` or equivalent instruction-load trace proves which surfaces are loaded and whether deduplication reduces context without removing required instructions.

## Skill mirrors

Do not normalize `.agents/skills/`, `.cursor/skills/`, `.kiro/skills/`, `.pi/skills/`, `.windsurf/skills/`, or other mirrors in this patch. First classify each repeated package as:

```yaml
mirror_class:
  - canonical_source
  - deterministic_mirror
  - client_specific_adaptation
  - independent_live_package
  - obsolete_copy
```

Only then design a source-to-mirror synchronization gate.

# Verification after application

```text
1. Cursor: open a normal Apex code/document task. The Obsidian rule must not attach solely because any file is open.
2. Cursor: ask explicitly for Obsidian wiki maintenance. The compatibility rule should become relevant.
3. Kiro: normal Apex task must route from AGENTS/current APEX context; explicit wiki task may auto-include the wiki steering file.
4. Windsurf and generic `.agent`: normal task may see the compatibility note, but it must identify APEX OS and impose zero wiki-specific rules.
5. Hermes: a knowledge-authoring request must discover apex-meta/informatics/index.md; a normal orchestration request must not be redirected to wiki behavior.
6. Repository-wide search on current instruction surfaces must find no statement that the whole project/repository “is a skill-based framework for building and maintaining an Obsidian knowledge base.”
```
