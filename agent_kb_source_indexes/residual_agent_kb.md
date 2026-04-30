# residual_agent_kb Source Index

Use this file for high-impact sources that are not easy to assign to one existing agent/sub-agent without creating weak ownership.
This is a parking and decision surface, not accepted KB content.

## Primary Residual Inputs

|source|lane|score|role|reason|read mode|exists|
|---|---|---:|---|---|---|---|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\07_finalopenclawsystem\NewFinals\ResourceScreeningLedgers\PROJECT_CARD_CANDIDATES.md`|`resource_screening`||`residual`|High-impact project-card candidates from presearch; placement depends on later portfolio/project-card decisions.|`skim`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\07_finalopenclawsystem\NewFinals\ResourceScreeningLedgers\OPEN_QUESTIONS_AND_BLOCKERS.md`|`resource_screening`||`residual`|Open blockers and placement questions from the presearch run; preserve for routing decisions.|`read full`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\07_finalopenclawsystem\NewFinals\ResourceScreeningLedgers\SOURCE_INVENTORY_LEDGER.md`|`resource_screening`||`residual`|Full presearch inventory and duplicate/access-blocker ledger; control evidence, not agent KB content.|`skim`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\07_finalopenclawsystem\NewFinals\ResourceScreeningLedgers\MASTER_IDEA_LEDGER.md`|`resource_screening`||`residual`|Full idea ledger with weighted evidence; use to audit generated per-agent selections.|`skim`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\07_finalopenclawsystem\NewFinals\ResourceScreeningLedgers\ESSENCE_CANDIDATES.md`|`resource_screening`||`residual`|Compact doctrine candidates that require second-agent verification before promotion.|`skim`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\04_final-system-setup\OpenCore\01_runtime_base\managed\config\openclaw.json`|`runtime_config`||`residual`|Runtime config is high-impact but not owned by a listed agent lane; requires explicit config owner decision.|`use as evidence only`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\04_final-system-setup\OpenCore\01_runtime_base\user\TOOLS.md`|`runtime_tools`||`residual`|User tool surface is high-value runtime context but lacks a defined agent owner in the map.|`skim`|yes|
|`[LOCAL_OPENCLAW_SOURCE]\OpenClaw\04_final-system-setup\OpenCore\01_runtime_base\managed\rituals\HEARTBEAT.md`|`runtime_rituals`||`residual`|Heartbeat ritual is operationally important but sits between meta_ops, hygiene, and runtime ownership.|`skim`|yes|

## Supporting / Control Inputs

_None identified from the current ledgers._

## Known Access Blocker

- `[LOCAL_RESOURCES]\UpdateProcessSSOTS` - access denied during inventory; already recorded in `SOURCE_INVENTORY_LEDGER.md`.

## Placement Questions

- Runtime config, user tool surfaces, and ritual files may need a dedicated runtime/memory owner if they should not be absorbed by `meta_ops` or `alfred`.
- Resource-screening ledgers should remain control evidence unless a future agent explicitly owns source-screening operations.
- Any residual item promoted from here needs second-agent validation and an explicit target lane.
