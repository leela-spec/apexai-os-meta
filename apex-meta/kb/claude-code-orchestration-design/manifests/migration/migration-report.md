# Claude Code Orchestration Design KB Migration Report

Generated: 2026-07-01T12:30:06Z

## Verdict

PARTIAL

## Git context

``yaml
branch: main
destination_root: apex-meta/kb/claude-code-orchestration-design
dry_run: False
lifecycle_executed: false
phase0_executed: false
phase1_executed: false
phase2_executed: false
old_roots_deleted_or_moved: false
``

## Git status before

``text
?? apex-meta/kb/claude-code-orchestration-design/
?? apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_CC.md
?? apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_CC_FBGem.md
?? apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_IT3_GPT.md
?? apex-meta/kb/claude-skill-design/manifests/projectrepos-corpus-intelligence/file-inventory.json
?? apex-meta/kb/lika-verein-taxes-accounting/raw/notes/ResearchAfterFirstKB/
?? scripts/merge_claude_orchestration_kbs.explicit.ps1
``

## Required source roots missing

None.

## Source root map

# Source Root Map

| ID | Source | Target | Required | Copied | Priority | Domains | Reason |
|---|---|---|---:|---:|---|---|---|
| $(@{id=claude-skill-design; source=apex-meta/kb/claude-skill-design; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence.; file_count=783; bytes_total=474150880; conflicts=0}.id) | $(@{id=claude-skill-design; source=apex-meta/kb/claude-skill-design; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence.; file_count=783; bytes_total=474150880; conflicts=0}.source) | $(@{id=claude-skill-design; source=apex-meta/kb/claude-skill-design; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence.; file_count=783; bytes_total=474150880; conflicts=0}.target) | True | True | $(@{id=claude-skill-design; source=apex-meta/kb/claude-skill-design; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence.; file_count=783; bytes_total=474150880; conflicts=0}.priority) | $([string]::Join(', ', @{id=claude-skill-design; source=apex-meta/kb/claude-skill-design; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence.; file_count=783; bytes_total=474150880; conflicts=0}.domains)) | Main existing Claude skill-design KB with schema, source inventories, Phase 0 artifacts, official docs, operator notes, and large corpus intelligence. |
| $(@{id=skill-design-best-practices; source=apex-meta/kb/skill-design-best-practices; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance.; file_count=5; bytes_total=19656; conflicts=0}.id) | $(@{id=skill-design-best-practices; source=apex-meta/kb/skill-design-best-practices; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance.; file_count=5; bytes_total=19656; conflicts=0}.source) | $(@{id=skill-design-best-practices; source=apex-meta/kb/skill-design-best-practices; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance.; file_count=5; bytes_total=19656; conflicts=0}.target) | True | True | $(@{id=skill-design-best-practices; source=apex-meta/kb/skill-design-best-practices; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance.; file_count=5; bytes_total=19656; conflicts=0}.priority) | $([string]::Join(', ', @{id=skill-design-best-practices; source=apex-meta/kb/skill-design-best-practices; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0-P1; reason=Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance.; file_count=5; bytes_total=19656; conflicts=0}.domains)) | Focused earlier skill best-practices KB with Phase 1 analysis of official skill-package guidance. |
| $(@{id=skill-best-practices-official-source-acquisition; source=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0; reason=Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources.; file_count=633; bytes_total=20594511; conflicts=0}.id) | $(@{id=skill-best-practices-official-source-acquisition; source=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0; reason=Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources.; file_count=633; bytes_total=20594511; conflicts=0}.source) | $(@{id=skill-best-practices-official-source-acquisition; source=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0; reason=Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources.; file_count=633; bytes_total=20594511; conflicts=0}.target) | True | True | $(@{id=skill-best-practices-official-source-acquisition; source=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0; reason=Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources.; file_count=633; bytes_total=20594511; conflicts=0}.priority) | $([string]::Join(', ', @{id=skill-best-practices-official-source-acquisition; source=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; required=True; copied=True; status=copied; domains=System.Object[]; priority=P0; reason=Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources.; file_count=633; bytes_total=20594511; conflicts=0}.domains)) | Raw official source-acquisition archive for Anthropic Agent Skills docs, official PDF, engineering article, Agent Skills specification, official repos, and academic/security sources. |
| $(@{id=claude-orchestration-agents; source=apex-meta/kb/claude-orchestration-agents; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; required=True; copied=True; status=copied; domains=System.Object[]; priority=P1-P3; reason=Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent.; file_count=1038; bytes_total=21652192; conflicts=0}.id) | $(@{id=claude-orchestration-agents; source=apex-meta/kb/claude-orchestration-agents; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; required=True; copied=True; status=copied; domains=System.Object[]; priority=P1-P3; reason=Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent.; file_count=1038; bytes_total=21652192; conflicts=0}.source) | $(@{id=claude-orchestration-agents; source=apex-meta/kb/claude-orchestration-agents; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; required=True; copied=True; status=copied; domains=System.Object[]; priority=P1-P3; reason=Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent.; file_count=1038; bytes_total=21652192; conflicts=0}.target) | True | True | $(@{id=claude-orchestration-agents; source=apex-meta/kb/claude-orchestration-agents; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; required=True; copied=True; status=copied; domains=System.Object[]; priority=P1-P3; reason=Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent.; file_count=1038; bytes_total=21652192; conflicts=0}.priority) | $([string]::Join(', ', @{id=claude-orchestration-agents; source=apex-meta/kb/claude-orchestration-agents; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; required=True; copied=True; status=copied; domains=System.Object[]; priority=P1-P3; reason=Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent.; file_count=1038; bytes_total=21652192; conflicts=0}.domains)) | Downloaded Claude orchestration agent repo corpus, including Claude Code best practices, BMAD, personal-os, claude-agents, awesome-claude-code, Aider, and SWE-agent. |
| $(@{id=prompt-engineer-research-base; source=apex-meta/kb/prompt-engineer-research-base; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; required=False; copied=True; status=copied; domains=System.Object[]; priority=P2; reason=Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns.; file_count=242; bytes_total=2845034; conflicts=0}.id) | $(@{id=prompt-engineer-research-base; source=apex-meta/kb/prompt-engineer-research-base; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; required=False; copied=True; status=copied; domains=System.Object[]; priority=P2; reason=Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns.; file_count=242; bytes_total=2845034; conflicts=0}.source) | $(@{id=prompt-engineer-research-base; source=apex-meta/kb/prompt-engineer-research-base; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; required=False; copied=True; status=copied; domains=System.Object[]; priority=P2; reason=Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns.; file_count=242; bytes_total=2845034; conflicts=0}.target) | False | True | $(@{id=prompt-engineer-research-base; source=apex-meta/kb/prompt-engineer-research-base; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; required=False; copied=True; status=copied; domains=System.Object[]; priority=P2; reason=Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns.; file_count=242; bytes_total=2845034; conflicts=0}.priority) | $([string]::Join(', ', @{id=prompt-engineer-research-base; source=apex-meta/kb/prompt-engineer-research-base; target=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; required=False; copied=True; status=copied; domains=System.Object[]; priority=P2; reason=Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns.; file_count=242; bytes_total=2845034; conflicts=0}.domains)) | Prompt/workflow research KB. Relevant only as supporting material for prompt-pack design and artifact-contract patterns. |


## Copy summary

# Copy Ledger

| Source root | Target root | Files | Bytes | Copied | Skipped identical | Conflicts |
|---|---|---:|---:|---:|---:|---:|
| $(@{source_root=apex-meta/kb/claude-skill-design; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; file_count=783; bytes_total=474150880; files_copied=783; files_skipped_identical=0; conflicts=0}.source_root) | $(@{source_root=apex-meta/kb/claude-skill-design; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design; file_count=783; bytes_total=474150880; files_copied=783; files_skipped_identical=0; conflicts=0}.target_root) | 783 | 474150880 | 783 | 0 | 0 |
| $(@{source_root=apex-meta/kb/skill-design-best-practices; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; file_count=5; bytes_total=19656; files_copied=5; files_skipped_identical=0; conflicts=0}.source_root) | $(@{source_root=apex-meta/kb/skill-design-best-practices; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/skill-design-best-practices; file_count=5; bytes_total=19656; files_copied=5; files_skipped_identical=0; conflicts=0}.target_root) | 5 | 19656 | 5 | 0 | 0 |
| $(@{source_root=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; file_count=633; bytes_total=20594511; files_copied=633; files_skipped_identical=0; conflicts=0}.source_root) | $(@{source_root=apex-meta/kb/_source-acquisitions/skill-best-practices-official-2026-06-23; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23; file_count=633; bytes_total=20594511; files_copied=633; files_skipped_identical=0; conflicts=0}.target_root) | 633 | 20594511 | 633 | 0 | 0 |
| $(@{source_root=apex-meta/kb/claude-orchestration-agents; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; file_count=1038; bytes_total=21652192; files_copied=1038; files_skipped_identical=0; conflicts=0}.source_root) | $(@{source_root=apex-meta/kb/claude-orchestration-agents; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents; file_count=1038; bytes_total=21652192; files_copied=1038; files_skipped_identical=0; conflicts=0}.target_root) | 1038 | 21652192 | 1038 | 0 | 0 |
| $(@{source_root=apex-meta/kb/prompt-engineer-research-base; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; file_count=242; bytes_total=2845034; files_copied=242; files_skipped_identical=0; conflicts=0}.source_root) | $(@{source_root=apex-meta/kb/prompt-engineer-research-base; target_root=apex-meta/kb/claude-code-orchestration-design/raw/source-groups/prompt-engineer-research-base; file_count=242; bytes_total=2845034; files_copied=242; files_skipped_identical=0; conflicts=0}.target_root) | 242 | 2845034 | 242 | 0 | 0 |


## Conflicts

None.

## Audit-only unmapped candidates

# Audit-Only Unmapped Candidates

These were not copied. They require operator review before adding to the explicit copy plan.

| Path | Reason | Tokens | Action |
|---|---|---|---|
| $(@{path=apex-meta/kb/apex-kb-skill-test; reason=folder_name_token_match; tokens=System.Object[]; copied=False; action=operator_review_required_before_adding_to_copy_plan}.path) | $(@{path=apex-meta/kb/apex-kb-skill-test; reason=folder_name_token_match; tokens=System.Object[]; copied=False; action=operator_review_required_before_adding_to_copy_plan}.reason) | $([string]::Join(', ', @{path=apex-meta/kb/apex-kb-skill-test; reason=folder_name_token_match; tokens=System.Object[]; copied=False; action=operator_review_required_before_adding_to_copy_plan}.tokens)) | $(@{path=apex-meta/kb/apex-kb-skill-test; reason=folder_name_token_match; tokens=System.Object[]; copied=False; action=operator_review_required_before_adding_to_copy_plan}.action) |


## Duplicate hash groups

Duplicate hash groups are reported in:

``text
manifests/migration/duplicate-hash-report.json
``

Duplicates were preserved. Nothing was deleted.

## Next allowed step

Run deterministic Phase 0 for:

``text
apex-meta/kb/claude-code-orchestration-design/
``

only after operator review.