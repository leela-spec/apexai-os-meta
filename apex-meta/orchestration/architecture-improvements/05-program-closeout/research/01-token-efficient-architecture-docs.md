---
type: Reference
title: Token-efficient, AI-friendly architecture documentation — verified best practice
status: stable
generated: { by: "claude/opus-4.8", at: "2026-09-28" }
tags: [research, documentation, ai-agents, tokens]
---

# Token-efficient architecture docs for AI agents (research summary)

Condensed from a 2026-09-28 web-research pass; sources at the bottom. Guidance, not gospel — the conventions below are de-facto, not standards-body ratified (flagged).

## Best practices (highest leverage first)
1. **One canonical entry point agents auto-discover.** Use `AGENTS.md` at repo root (Linux-Foundation-stewarded convention, 30k+ repos; nearest-file-wins in monorepos). Keep it **short and point to** the deep docs, don't inline them.
2. **Progressive disclosure / just-in-time context — the biggest token win.** A short index that links to detailed docs beats one large doc; the agent loads a detail doc only when the task needs it. (Anthropic, *Effective context engineering*, 2025: "smallest set of high-signal tokens." A secondary benchmark reported ~2.68× token reduction — directional, not primary.)
3. **Structure for machine parsing:** stable headings + tables (not long prose), machine-readable YAML frontmatter (`status`/`date`/`owner`), **link don't inline**, one topic per file. Duplication is where staleness + contradiction (agent confusion) start.
4. **Lightweight frameworks, used minimally:** MADR (Markdown ADRs, v4.0 2024-09-17) with `status: proposed|accepted|deprecated|superseded by ADR-NNNN`; arc42 (use a subset); C4 (natural progressive-disclosure levels); Mermaid diagrams-as-code (diffable, cheaper than an image — but keep scoped; huge graphs cost more than a table).
5. **`llms.txt`** for web-hosted docs only (not repo-internal) — convention, not a ratified standard.

## Superseded-doc redirect pattern (what we applied to the ki-basis docs)
Keep the stale file reachable, but put a notice **first** that links to current truth, plus machine-readable frontmatter:
```markdown
---
status: superseded
superseded_by: <path to current doc>
superseded_on: 2026-09-28
---
> **⚠️ SUPERSEDED — do not ground in this file.** Current source of truth: **[<title>](<path>)**.
> Retained for history only.
```
Rationale: agents weight leading tokens (notice read first); a single explicit link removes a navigation decision; frontmatter lets a CI gate detect staleness mechanically.

## Verdict on our bundle structure (index + architecture + decisions + runbook + questions + handover)
- Sound and best-practice-aligned (short index = progressive disclosure; Mermaid diagrams-as-code). Keep both.
- **Main fix:** separate the **durable architecture** (stable home, survives — e.g. `ki-basis/docs/`, arc42/C4-lite + Mermaid) from the **time-bound initiative folder** (gaps/plan/handover — tombstoned on completion). Otherwise an agent later grounds in an archived migration folder.
- Convert the append-only decision log toward per-decision status-bearing records where individual supersession matters; add `status:` frontmatter to every file; keep the handover bundle-local and tombstone it on completion.

## Sources (accessed 2026-09-28)
Anthropic *Effective context engineering for AI agents* (2025); agents.md; MADR (github.com/adr/madr) v4.0; arc42 + C4 + docs-as-code example; Read the Docs *Deprecating content*; Slack Design *On writing for deprecation*; llmstxt.org. Flags: the 2.68× figure is secondary; `AGENTS.md`/`llms.txt` are conventions, not ratified standards.
