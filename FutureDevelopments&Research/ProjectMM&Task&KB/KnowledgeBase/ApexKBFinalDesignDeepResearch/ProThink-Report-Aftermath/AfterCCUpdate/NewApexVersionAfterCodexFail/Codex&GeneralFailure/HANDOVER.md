# Codex Problem Analysis Handover

## Purpose

This folder converts `../ChatHistoryWithCodex.md` into evidence-addressable conversation records. Use the individual message files to identify Codex failures without loading the entire transcript into context.

## Start Here

1. Read `transcript-quality-report.md` to understand missing, truncated, or uncertain evidence.
2. Use `INDEX.md` to select only the messages relevant to the issue being investigated.
3. Verify claims against the cited source lines and, where necessary, Git commits or repository state.
4. Record each confirmed problem as a separate Markdown file. Distinguish transcript-confirmed evidence from user reports and claims requiring Git verification.

## Evidence Rules

- Do not treat a message containing `Show more` as complete evidence.
- Do not invent exact times for messages marked `upper_bound_only`.
- Do not treat the untimestamped trailing fragment as a complete user or assistant message.
- Preserve the distinction between user intent, Codex action, observed impact, root cause, and proposed prevention.
- Do not merge separate incidents merely because they share a broad category.

## Rebuilding the Message Set

Run `extract_chat_messages.py` against `../ChatHistoryWithCodex.md`. The script regenerates `messages/`, `fragments/`, `INDEX.md`, `extraction-report.json`, and `transcript-quality-report.md`. It does not remove this handover or future issue-analysis files.

The current normalized conversation date is `2026-07-13`, using Europe/Berlin summer time (`+02:00`).
