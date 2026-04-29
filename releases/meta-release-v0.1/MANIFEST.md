# meta-release-v0.1 MANIFEST

## Release identity

```yaml
release_id: meta-release-v0.1
release_type: bootstrap
release_status: release-candidate
source_basis_repo: leela-spec/MasterOfArts
source_basis_path: OpenClaw/07_finalopenclawsystem
target_meta_repo: leela-spec/apexai-os-meta
accepted_meta_commit: ec2eeaed4b713eb16b842c33322a85c1862c6eb1
bootstrap_pr: 1
runtime_config_included: false
project_template_materialized: false
```

## Purpose

This release records the first accepted ApexAI_OS Meta Operating Core bootstrap.

It freezes the merged meta core from `apexai-os-meta/main` at commit:

```text
ec2eeaed4b713eb16b842c33322a85c1862c6eb1
```

## Included source surfaces

The release includes the accepted contents of these root-level surfaces as of the accepted commit above:

```text
README.md
README-OpenClaw.md
CODEOWNERS
.github/pull_request_template.md
docs/*
managed/rules/*
managed/rituals/*
managed/agents/*
managed/agent_kb/*
managed/knowledge/*
managed/processes/*
inbox/learning/
```

## Managed rules included

```text
managed/rules/AGENTS.base.md
managed/rules/AGENT_SWARM_INTERACTION_CANON.md
managed/rules/ESCALATION_EXCEPTION_BLOCK.md
managed/rules/OPERATING_SPINE_CANON.md
managed/rules/PROJECT_INTERFACE_CONTRACT.md
managed/rules/PROMOTION_PROTOCOL.md
managed/rules/QA_HYGIENE_PROTOCOL.md
```

## Managed rituals included

```text
managed/rituals/BOOTSTRAP.md
managed/rituals/CHECKLISTS.md
managed/rituals/HEARTBEAT.md
managed/rituals/NIGHT_PLANNING_PROTOCOL.md
managed/rituals/SESSION_EXPORT_PROTOCOL.md
```

## Managed agent and KB surfaces included

```text
managed/agents/*
managed/agent_kb/AGENT_KB_INDEX.md
managed/agent_kb/<agent>/ESSENCE.md
managed/agent_kb/<agent>/BEST_PRACTICES.md
managed/agent_kb/<agent>/MISTAKES.md
managed/agent_kb/<agent>/TEMPLATES.md
managed/agent_kb/<agent>/LEARNING_QUEUE.md
```

The first-wave seed agents are:

```text
alfred
meta_ops
meta_strategy
meta_detective
special_ops__knowledge_bank
special_ops__informatics_design
special_ops__prompts_workflows
special_ops__ai_handling_routing
special_ops__hygiene_clean
```

## Managed knowledge and process surfaces included

```text
managed/knowledge/AGENT_KB_LANES.md
managed/knowledge/CROSS_REFERENCE_MANIFEST.md
managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
managed/knowledge/KB_STARTING_SOURCE_MAP.md
managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
managed/processes/AGENT_HANDOFF_CONTRACTS.md
managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md
managed/processes/HOLDING_ORCHESTRATION_FLOW.md
```

## Companion docs included

```text
docs/LEARNING_SYSTEM.md
docs/MEMORY_ARCHITECTURE.md
docs/PROCESS_BLUEPRINT_SYSTEM.md
docs/PROJECT_ROUTING.md
docs/README-docs.md
docs/ROLE_SYSTEM.md
```

## Hard exclusions

The following are not part of this release:

```text
managed/config/openclaw.json
user/*
NewFinals/
BaselinePatches/
AdvancedUpdateProcess/
raw project data
credentials/secrets
```

## Validation notes

- The bootstrap PR was merged into `main` before this release manifest was created.
- The release is commit-anchored rather than duplicate-file materialized inside `releases/`.
- `templates/project/` remains a separate materialization step after this release manifest.
- Runtime config remains excluded and manual-review only.

## Consumer rule

Consumers of `meta-release-v0.1` should use the accepted root-level paths at the anchored commit above as the release payload.

The manifest is the release index; the root-level files are the payload.
