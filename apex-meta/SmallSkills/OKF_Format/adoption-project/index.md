# OKF Adoption Project — Research & Next Steps

Working notes for rolling out OKF 0.2 as the standard for this repo's knowledge files, and for the Leela-Cloud-2026 SSOT. Nested under [OKF_Format](../index.md) because it's specifically about operationalizing that reference bundle, not a standalone concern.

* [Implementation Waves W0-W2](implementation-waves-w0-w2.md) - Approved compatibility-first implementation plan for baseline measurement, canonical informatics/routing lock, and deterministic validation/authoring support.
* [Patch Sequences A1-A2](patch-sequences-a1-a2.md) - Reviewable patch sequence for W1/A1 and W2/A2, including file sets, verification gates, stop boundaries, and rollback discipline.
* [Tooling Option Comparison](tooling-option-comparison.md) - Home-grown validator vs. installing the `okf-skills` community toolkit, with due-diligence findings.
* [Leela SSOT Migration Assessment](leela-ssot-migration-assessment.md) - What moving `docs/ssot/` from OKF 0.1 to 0.2 actually requires, and what's safe to do without asking first.
* [Informatics Design Research Location](informatics-design-research-location.md) - Where the prior "Informatics Design Research" actually lives, and which similarly-named files are false leads.
* [Apex-Meta OKF Usage Audit](apex-meta-okf-usage-audit.md) - Why the `.okf.md` files already in this repo (last two weeks) are not spec-conformant.
* [Next Steps](next-steps.md) - The open decisions and action items this research produced.

# Scope

This folder contains the 2026-09-01 research snapshot plus the approved first implementation plans. The plans authorize only W0-W2 and patch sequences A1-A2; they do not record those waves as executed. No later repository migration wave, cross-repository rollout, or mass retrofit is authorized here.

Two local `type` values are used beyond Claude_Design's `Playbook`/`Reference`: **`Research`** (a dated finding, may go stale) and **`Plan`** (an evolving or approved implementation plan). This is what "define your own local profile" (see [Conformance Rules](../conformance-rules.md)) looks like in practice — OKF doesn't register these centrally, so extending the vocabulary here is expected, not a deviation.
