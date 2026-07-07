# APEX Loop-Skill Audit Patch Manifest

```yaml
patch_manifest:
  repo: leela-spec/apexai-os-meta
  base_branch: main
  purpose: "APEX loop-skill audit metadata, root index, stale source-gap, and proposal-naming cleanup"
  generated_as: local_patch_pack_artifact
  source_access_method: GitHub_connector_live_main_fetches
  non_goals:
    - no_runtime
    - no_scheduler
    - no_agent
    - no_calendar_write
    - no_project_execution
    - no_direct_project_kb_mutation
    - no_architecture_redesign
    - no_PR_creation
    - no_push

  patch_to_target_map:
    "001-root-claude-skill-index.patch": ".claude/Claude.md"
    "002-raw-flow-dump-normalize-manifest.patch": ".claude/skills/raw-flow-dump-normalize/package-manifest.md"
    "003-flow-recap-manifest.patch": ".claude/skills/flow-recap/package-manifest.md"
    "004-flow-recap-contract-source-gaps.patch": ".claude/skills/flow-recap/references/flow-recap-packet-contract.md"
    "005-flow-recap-example-source-gaps.patch": ".claude/skills/flow-recap/examples/apex-minimal-flow-recap-example.md"
    "006-model-usage-log-manifest.patch": ".claude/skills/model-usage-log/package-manifest.md"
    "007-model-usage-delta-contract-source-gaps.patch": ".claude/skills/model-usage-log/references/model-usage-delta-contract.md"
    "008-status-merge-manifest.patch": ".claude/skills/status-merge/package-manifest.md"
    "009-status-merge-skill-output-naming.patch": ".claude/skills/status-merge/SKILL.md"
    "010-status-merge-packet-contract-output-naming.patch": ".claude/skills/status-merge/references/status-merge-packet-contract.md"
    "011-status-merge-next-precap-context-source-gaps.patch": ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md"
    "012-status-merge-example-source-gaps.patch": ".claude/skills/status-merge/examples/apex-minimal-status-merge-example.md"

  expected_changed_files:
    - .claude/Claude.md
    - .claude/skills/raw-flow-dump-normalize/package-manifest.md
    - .claude/skills/flow-recap/package-manifest.md
    - .claude/skills/flow-recap/references/flow-recap-packet-contract.md
    - .claude/skills/flow-recap/examples/apex-minimal-flow-recap-example.md
    - .claude/skills/model-usage-log/package-manifest.md
    - .claude/skills/model-usage-log/references/model-usage-delta-contract.md
    - .claude/skills/status-merge/package-manifest.md
    - .claude/skills/status-merge/SKILL.md
    - .claude/skills/status-merge/references/status-merge-packet-contract.md
    - .claude/skills/status-merge/references/next-precaphandoff-context-contract.md
    - .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md

  live_main_blob_sha_observed:
    ".claude/Claude.md": "341995a821144d7fc2a5fc67dcaca102f1f93cd7"
    ".claude/skills/raw-flow-dump-normalize/package-manifest.md": "c60a67588632ecf5a2f1fc63a553863bdedd3d16"
    ".claude/skills/flow-recap/package-manifest.md": "d20bfbbd5644c5b1d9b120bdf2eb8da60fac0394"
    ".claude/skills/flow-recap/references/flow-recap-packet-contract.md": "ce8cd76065e4a6afed4cd1636c34806d3b6ec348"
    ".claude/skills/flow-recap/examples/apex-minimal-flow-recap-example.md": "ca0a940c81ad867698fc7bba8efa1d765d227e0d"
    ".claude/skills/model-usage-log/package-manifest.md": "9e4b1c7adbfa26778ed8e1e0190ee6458ee6e955"
    ".claude/skills/model-usage-log/references/model-usage-delta-contract.md": "e2ff7b26f19805cc4135368704a8597596000054"
    ".claude/skills/status-merge/package-manifest.md": "4bbe250450800faac81a5973a8fadb827fb82d93"
    ".claude/skills/status-merge/SKILL.md": "e5a7413f680d51c254eb0c8ac79c4df3a8c98d07"
    ".claude/skills/status-merge/references/status-merge-packet-contract.md": "3d4eab69364d598ea2008f7fad89d55075962908"
    ".claude/skills/status-merge/references/next-precaphandoff-context-contract.md": "9c0298c38fd7605cea388b72fb2ec74a0454279a"
    ".claude/skills/status-merge/examples/apex-minimal-status-merge-example.md": "8b07b304694dfdc161a91551e7dd7387c80b2ddc"
```
