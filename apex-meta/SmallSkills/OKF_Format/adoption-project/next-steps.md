---
type: Plan
title: OKF Adoption — Open Decisions and Next Steps
description: The unresolved decisions and action items produced by this research round, kept as a single checklist so nothing gets re-derived from memory later.
tags: [okf, plan, roadmap, decisions-pending]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
status: draft
---

# Open decisions

- [ ] **Tooling**: install `scaccogatto/okf-skills`, or stay with a home-grown validator? See [Tooling Option Comparison](tooling-option-comparison.md). Leaning toward installing, pending a read-only `/okf:validate` trial against [OKF_Format](../index.md) and [Claude_Design](../../Prompting/Claude_Design/index.md).
- [ ] **Leela migration**: execute the one-line `okf_version: "0.1"` → `"0.2"` bump in `docs/ssot/index.md`? Verified safe (see [Leela SSOT Migration Assessment](leela-ssot-migration-assessment.md)), but withheld pending explicit go-ahead given this repo's governance rules.
- [ ] **Retrofit scope**: for the non-conformant `.okf.md` files found in [the audit](apex-meta-okf-usage-audit.md) — retrofit existing files, or write the new standard to govern only new files going forward?

# Action items

- [ ] Draft the unified design guide for "how we build knowledge-base files," reconciling three inputs:
  1. Real OKF v0.2 mechanics ([OKF_Format](../index.md))
  2. The existing content-quality doctrine (chunking rules, failure modes) in `informatics-design-doctrine.md` — see [Informatics Design Research Location](informatics-design-research-location.md)
  3. A fix or explicit non-fix for the ad hoc `.okf.md` convention already in use
- [ ] If Option B tooling is adopted, re-vet the `openknowledge.ai` `ok` CLI/plugin ecosystem separately — it was named in earlier research but not put through the same due-diligence pass as `okf-skills`.
- [ ] Once the unified guide exists, decide whether `SmallSkills/OKF_Format` itself needs a `type: Standard` or similar concept file declaring it as the adopted repo standard, rather than leaving that status implicit.

# Related

- [Tooling Option Comparison](tooling-option-comparison.md)
- [Leela SSOT Migration Assessment](leela-ssot-migration-assessment.md)
- [Apex-Meta OKF Usage Audit](apex-meta-okf-usage-audit.md)
