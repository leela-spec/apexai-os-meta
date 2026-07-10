---
title: "Follow-up: max-run-20260709 repair backlog"
page_type: audit_item
kb_slug: "claude-code-orchestration-design"
source_refs: []
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "needs_review"
---

# Follow-up: max-run-20260709 repair backlog

```yaml
scope: "16 pages under wiki/*/max-run-20260709/ still flagged by quality --strict"
reasons_observed: [concept_micro_not_evidenced, single_claim_concept_thin, thin_macro_meso_micro, single_claim_summary]
status: not_started
recommended_approach: candidate_driven_only
```

This is the explicit follow-up the content-value redesign plan deferred rather than folding in: the 25-page `max-run-20260709/` batch (16 of which still trip `quality --strict`) was left untouched by design, to avoid recreating the "complete the whole file list under pressure" trap the same batch's own root-cause report already diagnosed. The 74 non-max-run legacy pages were independently remediated by a concurrent process during this same work window and are no longer part of this backlog.

Recommended next step: run the same per-page draft-check-retry-escalate loop (`SKILL.md`) against exactly these 16 pages, one at a time, using `quality --strict --json`'s live reason codes per page -- not a blind batch rewrite. `flag-repair-candidate` is now available to record any page that still fails after 2 redrafts.
