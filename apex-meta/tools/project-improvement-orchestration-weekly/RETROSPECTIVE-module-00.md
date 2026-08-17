# Module 00 Retrospective — Resilience, Simplicity, Target Drift, Additional Value

Written at Module 00 closure (2026-08-17), after the forked-skill topology migration (D012/D013) landed and passed its fresh-context test. This is analysis, not a decision or a status — kept separate from `DECISIONS.md` and `CURRENT-STATE.md` so neither has to carry it.

## Resilience

- The fresh-context test was the real proof, not the static checks. Two subagents with zero memory of this migration correctly reconstructed the entire dispatch model — including a genuinely ambiguous case (the loop was actually sitting at an unconfirmed G2, not a clean stage boundary) — purely from repo content. That is the actual thing this project is trying to buy: a system that survives context loss, not just one that looks clean to someone who already knows the story.
- Silent local-only masking is a resilience trap. `.claude/Claude.md` vs `CLAUDE.md` worked fine on this Windows checkout because NTFS is case-insensitive and git's `core.ignorecase=true` hid the mismatch from `git status`. It would have silently broken on any case-sensitive checkout (Linux CI, etc.) with no local signal anything was wrong. Passing locally isn't evidence of portability.
- A schema is only as trustworthy as its least-honest field. `next_state` and `prerequisites` sat in `handoff-schema.md` looking load-bearing (no default, required-looking) but had zero producers or consumers anywhere. Dead-but-plausible-looking fields are a resilience risk in the other direction — they teach people to stop trusting "required."
- Archive-don't-delete (D007) paid for itself immediately. Every superseded file kept its replacement pointer, which is what let the fresh-context agents correctly say "these six agents exist but are retired, not current" instead of either missing them or getting confused by them.

## Simplicity

- The topology simplification was real, not cosmetic. Collapsing `parent -> named agent -> agent body -> preloaded skill -> stage` into `parent -> Skill fork -> stage` is a genuine hop removed, not a rename.
- Complexity was concentrated, not evenly spread. PrecapWeek and PrecapNextDay each carried 700-1300+ line rigid schema files (fixed project rosters, mandatory numeric ratings, giant machine-artifact triads); the other four packages were already close to lean. Bloat correlated with how early and how detailed a package's original authoring pass was — not with the underlying task's real difficulty.
- Simplifying isn't always deleting. PrecapNextDay's old schemas didn't need rewriting — they needed demotion from "required gate" to "optional depth." Same file, different authority. Smaller and safer than a rewrite, and it's what the plan actually called for.
- Evidence beats intuition for what to cut. Of roughly 17 handoff-envelope fields, only 2 turned out to be dead. Grepping for actual producers/consumers corrected the instinct-based guess in both directions — kept fields that looked suspicious, cut two that looked fine on the surface.

## Target drift

- The clearest instance predated this session entirely: the Weekly Command Brief template had already been "promoted" in an earlier pass but never wired into the actual runtime contract — design work done, entrypoint never updated. Exactly the failure mode D011 exists to catch, and the single biggest reason this Module 00 effort was needed.
- Naming drift accumulates silently. Three of six skills (`PrecapWeek`, `PrecapNextDay`, `ProjectStatus`) had frontmatter `name:` fields that didn't match their PascalCase directories — leftover from before a naming convention existed, never reconciled since nothing broke.
- Doctrine orphaning is an invisible failure mode. `meta-strategy-doctrine.md` was only ever read by the wrapper agent that got archived — `weekly-orchestrator` never referenced it directly. Archiving the agent would have silently orphaned real strategic-judgment content (option-framing, WRAP technique, reversibility analysis) with no error, no broken link, nothing — it would just stop being read by anything.
- Superseding artifacts get created before superseded ones get retired, and the loose end lingers. Seen three times: the duplicated `.md.md` plan filename, old-vs-new template pairs sitting side by side in `PrecapNextDay/templates/`, and the orphaned doctrine above. None of these were caught by normal use — only by an explicit "who still points here" audit.

## Additional value beyond the ask

- Fixed a real cross-platform portability bug (`CLAUDE.md` casing) unrelated to the orchestration topology itself.
- Fixed two broken relative-path references in the blueprint reference files that predated this migration (a `references/` prefix bug that was wrong even before this session touched anything).
- Flagged a naming-collision risk worth knowing about: `apex-project-status` is used both as an agent identifier and as a legacy state-file basename (`state/apex-project-status.md`). Three grep hits during the topology audit were this collision, not real dependencies. A future grep-based audit could reach the wrong conclusion here if it doesn't check context.

## Generalizable lessons for later modules / other audits

- When retiring a component, always search for "who reads this file," not just "who is this file about." The orphaned-doctrine finding only surfaces from the first question.
- A grep hit is a lead, not a conclusion — check whether the match is the thing itself or a coincidental string collision before acting on it.
- Prefer demotion (change what reads a file, and how strictly) over rewriting a file's internals, when the goal is "this is no longer required" rather than "this content is wrong."
- Consumer-audit every field/artifact before removing it, even when the removal looks obviously safe — the ratio here (2 dead out of ~17) suggests intuition alone over-predicts bloat.
