# Module 00 — Orchestration Spine

## Purpose

Repair the **whole production Weekly Orchestration lifecycle** before detailed output modules are changed.

This is the highest-leverage module because repository evidence already shows that the recovered human-facing design was not effectively wired into the active skills, while current global contracts require substantial packet/gate machinery.

## Primary question

What is the smallest coherent, resilient Weekly Orchestration lifecycle that reliably moves from confirmed project truth to weekly planning, daily planning, execution, truthful evidence, recap/candidate changes and confirmed state update?

## Mandatory execution order

A fresh Master must use the Module 00 files in this order:

1. **`01-ARCHITECTURE-RESEARCH-PROMPT.md`** — run an independent current-docs + repo research pass to decide whether the existing `weekly-orchestrator -> stage agents -> stage skills` composition is actually the simplest justified native architecture.
2. **`02-MACRO-INTEGRATION-GUIDANCE.md`** — lock why the validated operator design must be integrated into runtime authority rather than merely stored as templates.
3. **`03-MESO-INTEGRATION-GUIDANCE.md`** — map the target design to the actual Weekly Orchestrator, PrecapWeek, PrecapNextDay, Flow Cards, prompt files, evidence, recap, status mutation and ProjectStatus components.
4. **`04-MICRO-INTEGRATION-SEQUENCE.md`** — execute the ordered global-spine migration, stale-authority retirement, static integration verification and Module 01 handoff.

Do not skip directly to implementation before the architecture research decision is recorded. Do not rerun broad design discovery after the research result unless new evidence contradicts the validated design.

## Master responsibilities

Understand and challenge:

- `.claude/skills/weekly-orchestrator/SKILL.md`;
- weekly-orchestrator shared references, especially handoff/gate/review contracts;
- all weekly stage agents;
- their preloaded stage skills;
- Session / Sync / ProjectStatus relationships;
- deterministic versus AI responsibilities;
- artifact persistence and ownership;
- recovered operator-output design;
- current W34 behavior.

For each stage/transaction identify:

`producer -> payload -> consumer -> concrete value -> AI/deterministic/operator -> persistent/ephemeral -> gate/review condition`.

## Current topology to verify

The repo currently uses:

- one central production skill: `.claude/skills/weekly-orchestrator/`;
- peer stage agents under `.claude/agents/` such as `apex-precap-week`, `apex-precap-next-day`, `apex-flow-recap`, `apex-status-merge`;
- peer stage skills under `.claude/skills/` such as `PrecapWeek`, `PrecapNextDay`, `ProjectStatus`, `PromptEngineer`, `apex-session`, `apex-sync`;
- stage agents may preload their owning skill through agent frontmatter.

Claude Code supports skills and subagents as distinct composable primitives, but **native support does not prove that every current wrapper agent is useful**. The architecture research must test each agent against actual needs for context isolation, tool/permission boundaries, parallel work, model specialization and repeatability.

Do **not** create a nested meta-skill hierarchy merely for visual neatness. Do not retain custom stage agents merely because they already exist.

## Explicit assumptions to revalidate

- current skill + agent composition and whether wrapper agents duplicate skill behavior;
- G1-G5 structure and which gates are truly blocking;
- universal weekly handoff envelope;
- mandatory Sync reads;
- ProjectStatus as a stage/artifact;
- evidence normalization as mandatory vs conditional;
- daily StatusMerge behavior;
- independent review trigger behavior;
- packet families and persistence;
- role/accountability doctrine value;
- current planning stage interfaces;
- prompt-pack requirement.

## Known integration failure to correct

The validated operator-output templates were promoted into owning packages, but the recorded activation validation changed **zero contracts, zero entrypoints and zero runtime behavior**. Current PrecapWeek and PrecapNextDay entrypoints still encode schema-first packet behavior.

Therefore Module 00 must treat **runtime wiring and stale-authority removal** as the real integration problem. Template presence alone is not activation.

## Expected module result

1. Accepted simplest runtime composition for skills/subagents.
2. A plain-language corrected lifecycle.
3. A justified component/transaction map.
4. Updated active global Weekly Orchestrator contracts encoding that lifecycle.
5. Stage interfaces aligned with the validated operator-output design.
6. Superseded global contracts moved to archive/history where appropriate.
7. Clear module interfaces for Modules 01+.
8. Updated root `CURRENT-STATE.md` and `DECISIONS.md`.
9. First bounded handover for the next module.

## Not this module

Do not perfect the detailed Weekly Command Brief layout, Flow Card wording or sprint prompt design here. Change a stage file only as far as needed to remove global contradictions and establish the correct interface; detailed output behavior belongs to its module chat.
