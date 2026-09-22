---
okf: 0.2
type: exact_match_patch
id: c02-readme-status-advance
status: proposed_not_applied
target: apex-meta/handoff/universal-ai-instruction-system/README.md
base_commit: d38192dcaae5ef2ec804f82778a716e296b2ffe6
match_count_required: 1
---

# Purpose

Advance module status only after the C02 result and pilot patch have been deterministically applied and verified.

## old

~~~text
| C02 | `<research>` | Conditional Research Discipline | **NEXT** |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | QUEUED |
~~~

## new

~~~text
| C02 | `<research>` | Conditional Research Discipline | **DONE** |
| C03 | `<informatics>` | Conditional Informatics / Formal Authoring | **NEXT** |
~~~

## verify

- old block matched exactly once before edit;
- only the C02/C03 status rows changed;
- no other README content changed;
- no whole-file regeneration.
