---
type: Reference
id: REF-INFRASTRUCTURE-ONLINE-ACCESS
title: Online access and link conversion
description: Repository-root-relative navigation and the reusable path converter for an authenticated repository processor.
status: current
tags: [informatics, infrastructure, paths, links]
---

# Online access

Every navigation path starts at the repository root. For example, `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml` identifies a file inside the repository without a drive, workstation directory, hostname, or branch. The processor resolves these paths using its authenticated repository connection.

Start at [the infrastructure evidence index](apex-meta/informatics/final/research/11-infrastructure-evidence-index/index.md). Resolve its destinations from the repository root rather than from the containing document's folder. These are repository identifiers for the processing program; a Markdown renderer that assumes document-relative destinations needs a repository-root resolver.

## Named source

The original Untitled 5.md has been moved into this repository's evidence bundle as [infrastructure-activation-research-brief.md](apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md). The move preserves its content bytes. The source remains a retained conversation brief, not a newly adopted specification.

## Reusable script

The [repository path converter](scripts/repo_relative_index_paths.py) uses the Python standard library. It normalizes this index's navigation to repository-root-relative paths and removes the mistakenly added GitHub URL and remote-status columns from the TSV inventories. It requires no network request or GitHub visibility check.

```powershell
python scripts/repo_relative_index_paths.py
python scripts/repo_relative_index_paths.py --apply
```

The default run previews changes. `--apply` replaces only verified byte spans and preserves untouched bytes. Repeating the command makes no changes when paths already match. File and directory destinations use the same root-relative convention. Paths containing spaces use Markdown angle delimiters. Section anchors are preserved. The script leaves remote snapshots and the source brief unchanged.

The converter reports changed spans and unresolved external paths. Paths outside this repository remain explicit gaps. Path validation checks the local repository structure; it makes no assertion about public availability or the processing program's permissions.

## Online-only reading rules

Use each TSV's `repository_path` directly. Use the separate `line` field for decision locations. Read source documents before treating indexed snippets as decisions. Original URLs and workstation paths inside preserved evidence remain provenance or reproduction context, rather than navigation instructions.

## Failure guards

The processor must have access to the repository revision containing these files. A valid repository-relative path does not establish that access. Do not publish unrelated files merely because they appear in the discovery inventory. Paths outside the repository require separate accessible evidence or an explicit gap. Hook, agent, skill, and infrastructure configuration remain unchanged by this conversion.
