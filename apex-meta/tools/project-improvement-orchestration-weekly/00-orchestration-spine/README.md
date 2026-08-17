# Module 00 — Orchestration Spine

## Purpose

Repair the **whole production Weekly Orchestration lifecycle** before detailed output modules are changed.

This is the highest-leverage module because repository evidence already shows that the recovered human-facing design was not effectively wired into the active skills, while current global contracts require substantial packet/gate machinery.

## Primary question

What is the smallest coherent, resilient Weekly Orchestration lifecycle that reliably moves from confirmed project truth to weekly planning, daily planning, execution, truthful evidence, recap/candidate changes and confirmed state update?

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

This composition is natively supported by Claude Code. Do **not** create a nested meta-skill hierarchy merely for visual neatness. Physical reorganization is allowed only if it improves maintainability or runtime behavior without duplicating authority.

## Explicit assumptions to revalidate

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

## Expected module result

1. A plain-language corrected lifecycle.
2. A justified component/transaction map.
3. Updated active global Weekly Orchestrator contracts encoding that lifecycle.
4. Superseded global contracts moved to archive/history where appropriate.
5. Clear module interfaces for Modules 01+.
6. Updated root `CURRENT-STATE.md` and `DECISIONS.md`.
7. First bounded handover for the next module.

## Not this module

Do not perfect the detailed Weekly Command Brief layout, Flow Card wording or sprint prompt design here. Change a stage file only as far as needed to remove global contradictions and establish the correct interface; detailed output behavior belongs to its module chat.
