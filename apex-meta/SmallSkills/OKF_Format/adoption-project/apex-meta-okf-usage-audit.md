---
type: Research
title: Apex-Meta's Existing .okf.md Files Are Not Spec-Conformant
description: Files using the .okf.md naming convention in recent commits do not follow the real OKF v0.2 spec, predating this session's grounding in the actual specification.
tags: [okf, apex-meta, drift, audit, conformance]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: commit-db55b79d
    resource: "repo:apexai-os-meta commit:db55b79d"
    title: "feat(simulation): materialize complete 2-week hermes weekly orchestration simulation suite"
  - id: commit-9fa466c3
    resource: "repo:apexai-os-meta commit:9fa466c3"
    title: "docs(campaign): reviewer handover for independent phase-4 review assignment"
  - id: hermes-handover-admission
    resource: "apex-meta/AI-Snippets/AIFailure/HERMES-MIGRATION-HANDOVER-OKF-v0.2.md"
    title: Hermes migration handover — self-admitted best-effort OKF format
status: draft
stale_after: 2026-12-01T00:00:00Z
---

# What was checked

Both commits from the last two weeks that touched `.okf.md`-suffixed files were read directly, not inferred from filenames.[^commit-db55b79d][^commit-9fa466c3]

# What was found

- `00-PROGRAM.okf.md` / `01-TASK-GRAPH.okf.md` (under `apex-meta/tools/project-improvement-orchestration-weekly/simulations/hermes-e2e-two-week-v1/`) use a **body-embedded** `okf: {id, version, status, document_role}` block instead of YAML frontmatter — no `type`, no `sources`. This fails the spec's first conformance rule (parseable YAML frontmatter) outright.
- `reviewer-03-marketing-information-design.okf.md` (both W01 and W02 runs) has **no frontmatter at all**, despite the `.okf.md` extension.
- A separate file states the problem plainly in its own metadata table: *"Format | OKF v0.2 (best-effort; no canonical schema was available to the author)."*[^hermes-handover-admission]

# What this means

The `.okf.md` naming convention already in wide use across this repo predates anyone checking it against Google's actual spec — including this session, before [OKF_Format](../index.md) was built from the real `SPEC.md`. This is pre-existing drift, not something introduced by summarizing the spec in this project's own words. It's a separate problem from — and larger than — the citation-hygiene issues found and fixed in [Claude_Design](../../Prompting/Claude_Design/index.md).

No `.okf.md` file has been retrofitted. Whether to retrofit existing files or govern new ones only is an open call — see [Next Steps](next-steps.md).

# Related

- [Informatics Design Research Location](informatics-design-research-location.md) — the doctrine that should pair with real OKF mechanics once this is reconciled
- [Next Steps](next-steps.md)
