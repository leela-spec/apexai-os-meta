---
type: Research
title: OKF Tooling — Home-Grown Validator vs. Installing okf-skills
description: Comparison of building a small local validator against installing the third-party okf-skills Claude Code plugin, with due-diligence findings on the latter.
tags: [okf, tooling, decision-pending, validator, automation]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-skills-repo
    resource: https://github.com/scaccogatto/okf-skills
    title: scaccogatto/okf-skills — OKF toolkit for Claude Code
  - id: okf-skill-repo
    resource: https://github.com/mattjoyce/okf-skill
    title: mattjoyce/okf-skill — Claude Code skill for OKF
  - id: openknowledge-workflow
    resource: https://openknowledge.ai/docs/workflows/supporting-open-knowledge-format
    title: Supporting the Open Knowledge Format
status: draft
stale_after: 2026-12-01T00:00:00Z
---

# The two options

**Option A — spec + local profile + home-grown validator.** Just the Apache-2.0 spec, a written local-profile doc (type vocabulary, required fields, templates), and a small script checking conformance. Zero external dependency; an afternoon of work; you own every line.

**Option B — install a community toolkit.** Three candidates surfaced during research, none of them official Google tooling — the spec itself (`GoogleCloudPlatform/knowledge-catalog`) is the only confirmed-official artifact:

| Toolkit | What it adds |
|---|---|
| `scaccogatto/okf-skills`[^okf-skills-repo] | `/okf:okf` (author/maintain), `/okf:validate` (strict/warning conformance), `/okf:visualize` (interactive HTML knowledge graph), a GitHub Action, and a **`--migrate` flag that rewrites v0.1→v0.2** |
| `mattjoyce/okf-skill`[^okf-skill-repo] | Lighter: teaches the OKF mental model plus a dependency-free `validate_okf.py`. No visualization, no CI action. |
| `openknowledge.ai`'s `ok` CLI + plugin[^openknowledge-workflow] | `ok seed`/`ok lint`/`ok audit`, real-time Problems-panel linting, a companion agent skill. Different domain/maintainer than the other two — an entirely separate third project, not affiliated with Google. |

# Due diligence on scaccogatto/okf-skills

Checked directly rather than assumed, since it's the strongest automation candidate: **353 stars, 32 forks, MIT license, 44 commits**, a documented release process requiring version bumps for shipped changes, and it dogfoods its own validation in `.okf/`. Reads as genuinely maintained — but it is a **single-maintainer project**, not a team or an official Google release. That's the real trade-off: automation and migration tooling for free, in exchange for depending on one person's continued interest.

# Recommendation

If installing something: **`scaccogatto/okf-skills`** over the other two, specifically because its `--migrate` flag is directly useful for [the Leela migration](leela-ssot-migration-assessment.md). Try `/okf:validate` read-only against [OKF_Format](../index.md) and [Claude_Design](../../Prompting/Claude_Design/index.md) first — bundles already known to be conformant — before trusting `--migrate` output against anything that matters, like Leela's SSOT.

# Status: undecided

No toolkit has been installed. This file records the comparison, not a decision.

# Related

- [Leela SSOT Migration Assessment](leela-ssot-migration-assessment.md)
- [Next Steps](next-steps.md)
