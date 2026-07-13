---
title: "Standalone AI instructions — execute v2 Tier 0 (macro token architecture)"
purpose: "Self-contained prompt for a fresh chat with zero prior context to run the first isolated goal from orchestration-betterment-plan-v2.md"
---

Repo root: `C:\GitDev\apexai-os-meta`, branch `main`. Read
`apex-meta/fable-orchestrator/orchestration-betterment-plan-v2.md` in full first — it is the
authoritative plan; everything below just scopes you to its first isolated goal.

**Your goal: execute ONLY Tier 0 (items 0a-0d) of that plan.** Do not touch Tier 1, Tier 2, or
`apex-meta/fable-orchestrator/Newplan.md` (a separate, unrelated plan) — those are out of scope for
this run.

Tier 0 is: relocate the always-loaded token cost in `.claude/CLAUDE.md` down to a compact activation
seed (~1,600 → ~400-500 tokens) by moving the core_loop table, full skills table, agents table, and
artifact_paths out to their already-existing single home in
`.claude/skills/weekly-orchestrator/SKILL.md` and its references (do not duplicate — point, don't
copy); then diet every project skill's and agent's `description:` frontmatter field to ≤75 words each
("Use this skill when…", inputs→outputs, one does-not-do clause) without touching skill/agent body
content; then add the one-line compaction-protection note to the weekly-orchestrator contract. Full
detail, file list, and rationale are in the plan document's Tier 0 section — follow it exactly.

Guard-rail: subtraction and relocation only. No new files, engines, hooks, or state machines.

Work local-file only. No git commit or push unless explicitly asked. Run to completion without
per-step approval; halt only on a genuinely missing required input or an unsafe write.

When done, verify per the plan's "Token math" and "No-loss check" verification steps (before/after
`wc -c` on CLAUDE.md, confirm every relocated fact still resolves at its new pointer target) and
report the measured token reduction in one summary.
