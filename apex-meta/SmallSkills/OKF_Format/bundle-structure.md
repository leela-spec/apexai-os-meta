---
type: Reference
title: OKF Bundle Directory Structure
description: How an OKF bundle is laid out on disk, and what the two reserved filenames are for.
tags: [okf, format-spec, bundle-structure, index, log]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
status: stable
---

# What a bundle is

An OKF bundle is a directory tree of markdown files — nothing more exotic than that. It's designed to be distributed as a git repository so version history and attribution come for free, though a tarball or a subdirectory inside a larger repo both work too.[^okf-spec]

# Reserved filenames

Two filenames carry special meaning and must never be used as an ordinary concept document:

- **`index.md`** — a navigation page. It can appear at any directory level, not just the root. Its body is a set of markdown-linked entries with one-line descriptions, so a reader can decide what to open next without opening every file.[^okf-spec] Only the bundle-root `index.md` may carry frontmatter, and if it does, that frontmatter is exactly one field: `okf_version`.[^okf-spec]
- **`log.md`** — a change history, grouped by ISO 8601 date (`YYYY-MM-DD`), newest entry first. Leading bold words like **Update** or **Creation** are a scanning convention, not a required field.[^okf-spec]

Every other `.md` file in the bundle is an individual concept document.[^okf-spec]

# Where things live

Nothing prescribes subdirectories beyond a loose convention: a `references/` folder for mirroring external material or code that concepts point to.[^okf-spec] Beyond that, flat is fine — [Claude_Design](../Prompting/Claude_Design/index.md) in this repo is a flat, 7-concept bundle plus its own `index.md`/`log.md`.

# Related

- [Frontmatter Fields](frontmatter-fields.md)
- [Conformance Rules](conformance-rules.md)
