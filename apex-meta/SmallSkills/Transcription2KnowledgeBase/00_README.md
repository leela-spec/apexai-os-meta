---
type: Reference
title: Transcription2KnowledgeBase SmallSkill
description: Component status and non-goals for the transcript-to-vault Hermes skill.
---

# Transcription2KnowledgeBase SmallSkill

Turns a transcript into source-grounded Markdown notes in an Obsidian vault, via LangExtract,
run through Hermes. Manual trigger only. No database, no custody spine, no adaptive learning —
those are explicitly deferred (see Non-Goals and the research handover).

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The actual skill: frontmatter + step-by-step procedure. Source of truth for what gets installed into Hermes. |
| `RESEARCH-HANDOVER-adaptive-schema-selection.md` | Open sub-problem: automatic/improving extraction-schema selection across domains. Not started, not required for v1. |
| `LEARNINGS-2026-10-02-first-extraction-run.md` | Trial log from the first live run: 3 root causes found and fixed, 1 quota wall hit. |
| `00_README.md` | This file. |

## Component status (live, private Hermes instance)

| Component | State | Where |
|---|---|---|
| `transcript-to-vault` skill (this skill) | **Installed** | `/root/.hermes/skills/research/transcript-to-vault/SKILL.md` |
| `langextract-usage` (Google's official skill) | **Installed**, SAFE scan verdict | `/root/.hermes/skills/langextract-usage/` |
| `config.yaml` free-model routing | **Applied**, Hermes restarted | `/root/.hermes/config.yaml` — `model.default: nvidia/nemotron-3.5-lightning:free` + 4-model fallback chain + `auxiliary.free_only`, copied from `community-hermes`'s live config. Backup at `/root/.hermes/config.yaml.bak-20261001T100108Z`. |
| `qmd` skill | **Not installed — blocked on operator decision** | `hermes skills install official/research/qmd` scanned **DANGEROUS** (sudo privilege escalation, background-daemon persistence, edits `config.yaml` itself). Step 7 of `SKILL.md` falls back to a bare `qmd` CLI call until this is resolved one way or the other. |
| Gateway auth (`API_SERVER_KEY`) | **Known mismatch, unresolved** | `ki-basis/.env.private`'s `HERMES_API_SERVER_KEY` does not match the live `/opt/data/.env` (`API_SERVER_KEY`) inside the container — `invoke-hermes.ps1` gets a 401 from outside. Irrelevant to this skill itself, since it reads `API_SERVER_KEY` from `$HERMES_HOME/.env` directly (same container, no cross-file dependency) — but flagged here since it blocks any *external* smoke test of the gateway. |
| Output vault | **Confirmed live** | `/root/workspaces/MasterOfArts/Health/PEM_LongCovid_MeCFS/` — real `.obsidian/` present. |

## Non-Goals (guardrails — do not drift back into these)

- No TTK custody spine, no Macro/Meso/Micro output, no reuse of `transcript_pipeline_v2` (see that system's own research index: it did not deliver a working product; separately, its "LangExtract" adapter isn't real LangExtract — it shells out to a Claude Code subscription).
- No SQLite or any rigid per-field schema. Output is plain Markdown, frontmatter capped at `title` / `summary` / `tags` / `source` — this repo already has an operator-verified failure case for exactly this over-engineering pattern: `apex-meta/AI-Snippets/AIFailure/AI-Failure-RAG-Metadata-Overengineering.md`.
- No adaptive/learning schema selection in v1 — one LLM call drafts categories fresh per transcript, every time. The "make this smarter across domains over time" problem is real but unsolved industry-wide (see the research handover); not blocking v1.
- No automatic trigger (no file-watcher, no cron) in v1 — invoked manually, e.g. `/transcript-to-vault <path>`.
- No direct OpenRouter API key extraction from `/root/.hermes/.env` — that path was investigated and rejected; it bypasses Hermes' own credential rotation and isn't a documented integration point.
- No reinventing LangExtract usage — defer to its own official skill rather than writing new install/parameter documentation.
