---
type: Research
title: Leela SSOT — OKF 0.1 to 0.2 Migration Assessment
description: What was actually verified about migrating Leela-Cloud-2026's docs/ssot bundle from OKF 0.1 to 0.2, and why it hasn't been executed yet.
tags: [okf, leela-cloud-2026, ssot, migration, governance]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: leela-root-index
    resource: "repo:Leela-Cloud-2026 path:docs/ssot/index.md"
    title: Leela SSOT root index — declares okf_version 0.1
  - id: leela-gate-script
    resource: "repo:Leela-Cloud-2026 path:scripts/check_ssot_contracts.py:503-504"
    title: Root-index okf_version presence check
  - id: leela-sample-concepts
    resource: "repo:Leela-Cloud-2026 path:docs/ssot/features/sequencing/spec.md, docs/ssot/architecture/materialization.md, docs/ssot/architecture/cross-feature.md"
    title: Sampled SSOT concept file frontmatter
status: draft
stale_after: 2026-12-01T00:00:00Z
---

# Current state, verified directly

`docs/ssot/index.md` declares `okf_version: "0.1"`.[^leela-root-index] Sampled concept files (`sequencing/spec.md`, `architecture/materialization.md`, `architecture/cross-feature.md`) all carry a genuine `type` field plus a rich **custom local profile**: `authority_tier`, `baseline_ids`, `owner`, `source_commit`, `canon_source_commit`, `normative_status`, `migration_action`.[^leela-sample-concepts] None of Google's standard v0.2 provenance fields (`sources`, `generated`, `verified`, `stale_after`) are in use — a repo-wide check found only **1 of 161** `docs/ssot/**/*.md` files uses any of them.

# Why the version bump itself is safe

`scripts/check_ssot_contracts.py:503-504` only asserts that the key `okf_version` **exists** in the root index — it does not check the value.[^leela-gate-script] Bumping `"0.1"` → `"0.2"` will not break that gate. v0.2 is additive-only by spec design: existing v0.1-shaped concept files stay valid with no rewrite required.

# The migration is really two different-sized moves

1. **Trivial and safe**: change the one string in `docs/ssot/index.md`. Nothing else has to change for this to be honest, since v0.2's new fields are all optional.
2. **Optional and large**: backfill `sources`/`generated`/`verified`/`stale_after` across some or all of 161 files to actually gain v0.2's provenance value. Not required by the spec. This is a separate initiative, not a migration detail.

# Why nothing has been changed yet

Leela-Cloud-2026's own `AGENTS.md` requires reporting expected blast radius before changing more than ten tracked files, and treats `docs/ssot/` changes as governed (decision records, `STATE.md` logging, re-running `check_ssot_contracts.py`/`generate_ssot_views.py --check`). Even the one-line version bump touches the file that all 161 others authority-chain from, so it was held for an explicit go-ahead rather than done ad hoc.

# Related

- [Tooling Option Comparison](tooling-option-comparison.md) — `okf-skills`' `--migrate` flag could handle the optional backfill move, once vetted further
- [Next Steps](next-steps.md)
