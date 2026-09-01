---
type: Research
title: Where the "Informatics Design Research" Actually Is
description: Resolves a hard-to-recall reference by distinguishing the real research document from same-named agent/doctrine files that are not research.
tags: [okf, informatics-design, apex-meta, knowledge-base]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: practice-guide
    resource: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md"
    title: Informatics design formats practice guide
  - id: token-efficient-doc
    resource: "apex-meta/kb/claude-code-orchestration-design/wiki/summaries/token-efficient-information-design.md"
    title: Token-efficient information design
  - id: doctrine-file
    resource: ".claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md"
    title: Informatics-design doctrine (weekly-orchestrator role)
status: stable
---

# The actual research

**[`informatics-design-formats-practice-guide.md`](../../../kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md)** (created 2026-07-10) is the real match — a source-cited, confidence-rated synthesis literally titled "Informatics Design."[^practice-guide] Its sibling, **`token-efficient-information-design.md`** (same folder, 2026-07-02/07-10), covers progressive-disclosure and token economy with the same source-cited, comparative structure.[^token-efficient-doc]

# What it is not — false leads ruled out

- `.claude/agents/informatics-design.md` and `.claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md`[^doctrine-file] — these are an **agent persona and a compressed rulebook** (chunking rules: "one chunk, one job"; failure modes: "mixed-purpose blob," "TODO fossilization"), not a research writeup. Genuinely useful — see [Apex-Meta OKF Usage Audit](apex-meta-okf-usage-audit.md) for how it should combine with real OKF mechanics — but it isn't what "research" was pointing to.
- `apex-meta/fable-orchestrator/APEX_Orchestration_User_Stories/00_INFORMATION_CONNECTION_LEDGER.md` — matched the keyword search on "information," not "informatics"; it's a data-connection ledger for user stories, unrelated.
- `FutureDevelopments&Research/.../Apex_KB_Final_Architecture_Deep_Research_Report.md` — a genuine large deep-research report, but about KB *compilation architecture*, not informatics/information-design conventions specifically. Likely a false positive on the keyword match, not a duplicate of the practice guide.

# Related

- [Apex-Meta OKF Usage Audit](apex-meta-okf-usage-audit.md) — this doctrine's chunking rules are one of the three inputs the eventual unified design guide needs to reconcile
