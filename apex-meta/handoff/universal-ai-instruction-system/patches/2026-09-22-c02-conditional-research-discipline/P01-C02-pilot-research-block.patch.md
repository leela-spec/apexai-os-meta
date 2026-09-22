---
okf: 0.2
type: exact_match_patch
id: c02-pilot-research-block
status: proposed_not_applied
target: apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md
base_commit: d38192dcaae5ef2ec804f82778a716e296b2ffe6
match_count_required: 1
---

# Purpose

Replace only the existing C02 research block. No other part of the pilot may change.

## old

~~~text
  <research when="the task depends on current, external, niche, contested, or comparative evidence"
            principles="landscape-scan,source-authority,triangulation">
    Research before canonizing a recommendation. Prefer primary or authoritative sources and distinguish verified facts from inference.
  </research>
~~~

## new

~~~text
  <research when="the task requires multi-step evidence synthesis, broad or representative coverage, or resolution of material disagreement beyond normal grounding"
            principles="research-planning,iterative-search,source-triangulation,contradiction-tracking,stopping-criteria"
            ref="apex-meta/handoff/universal-ai-instruction-system/module-deepening/C02-conditional-research-discipline/SKILL.md"
            deepen_when="ordinary grounding is insufficient because the answer depends on coverage, synthesis, or unresolved conflicting evidence">
    Frame the research question and decision need, plan the evidence needed, search and follow leads iteratively across appropriate source classes, and preserve material gaps or conflicts. Stop when additional searching is unlikely to change the answer materially; synthesize only what the evidence supports.
  </research>
~~~

## verify

- old block matched exactly once before edit;
- only this C02 block changed;
- no surrounding module wording changed;
- no whole-file regeneration;
- diff is localized to this block.
