# OKF Adoption Project — Research & Next Steps

Working notes for rolling out OKF 0.2 as the standard for this repo's knowledge files, and for the Leela-Cloud-2026 SSOT. Nested under [OKF_Format](../index.md) because it's specifically about operationalizing that reference bundle, not a standalone concern.

* [Tooling Option Comparison](tooling-option-comparison.md) - Home-grown validator vs. installing the `okf-skills` community toolkit, with due-diligence findings.
* [Leela SSOT Migration Assessment](leela-ssot-migration-assessment.md) - What moving `docs/ssot/` from OKF 0.1 to 0.2 actually requires, and what's safe to do without asking first.
* [Informatics Design Research Location](informatics-design-research-location.md) - Where the prior "Informatics Design Research" actually lives, and which similarly-named files are false leads.
* [Apex-Meta OKF Usage Audit](apex-meta-okf-usage-audit.md) - Why the `.okf.md` files already in this repo (last two weeks) are not spec-conformant.
* [Next Steps](next-steps.md) - The open decisions and action items this research produced.

# Scope

This is a snapshot of research done 2026-09-01, not a standing decision record — nothing here has been executed yet except creating [OKF_Format](../index.md) and [Claude_Design](../../Prompting/Claude_Design/index.md) themselves. Two new `type` values are introduced here beyond Claude_Design's `Playbook`/`Reference`: **`Research`** (a dated finding, may go stale) and **`Plan`** (an open, evolving checklist). This is what "define your own local profile" (see [Conformance Rules](../conformance-rules.md)) looks like in practice — OKF doesn't register these centrally, so extending the vocabulary here is expected, not a deviation.
