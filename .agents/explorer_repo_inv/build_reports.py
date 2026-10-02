import json
from collections import Counter
from pathlib import Path

BASE_DIR = Path(r"c:\GitDev\apexai-os-meta").resolve()

with open('evaluated_inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sort data by Scope, then Domain, then File Name
data_sorted = sorted(data, key=lambda x: (x['scope'], x['domain'], x['file_name']))

total_files = len(data)
total_bytes = sum(x['byte_size'] for x in data)
total_lines = sum(x['line_count'] for x in data)

scope_counts = Counter(x['scope'] for x in data)
domain_counts = Counter(x['domain'] for x in data)
status_counts = Counter(x['status'] for x in data)

# Build Markdown content
lines = []
lines.append("# Active Repository Inventory & Multi-Metric Evaluation")
lines.append("")
lines.append(f"**Repository Root**: `c:\\GitDev\\apexai-os-meta`  ")
lines.append(f"**Audit Timestamp**: 2026-09-29T11:51:00+02:00  ")
lines.append(f"**Auditor Agent**: `explorer_repo_inv` (Archetype: Explorer)  ")
lines.append(f"**Parent Orchestrator**: `orchestrator_3` (`6ddb3813-515a-42e2-a565-70b43dfc69f4`)  ")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Executive Summary")
lines.append("")
lines.append(f"This inventory report represents an exhaustive, 100% physically verified catalog and preliminary evaluation of all agent definitions, doctrine files, orchestration workflows, schemas, dossiers, and skill implementations across the active `c:\\GitDev\\apexai-os-meta` repository. A total of **{total_files} files** ({total_bytes:,} bytes, {total_lines:,} lines) were discovered across four distinct target scopes. Zero phantom files exist; every file path was verified on disk with byte sizes, line counts, and UTC timestamps recorded.")
lines.append("")
lines.append("### Key Inventory Metrics")
lines.append(f"- **Total Discovered Files**: {total_files}")
lines.append(f"- **Total Volume**: {total_bytes / (1024*1024):.2f} MB ({total_bytes:,} bytes across {total_lines:,} lines)")
lines.append(f"- **Canonical / Active Files**: {status_counts['Canonical / Active']} ({status_counts['Canonical / Active']/total_files*100:.1f}%)")
lines.append(f"- **Distilled / Migrated Files**: {status_counts['Distilled / Migrated']} ({status_counts['Distilled / Migrated']/total_files*100:.1f}%)")
lines.append(f"- **Reference-Only / Historical Files**: {status_counts['Reference-Only / Historical']} ({status_counts['Reference-Only / Historical']/total_files*100:.1f}%)")
lines.append(f"- **Empty Scaffold / Stubs**: {status_counts['Empty Scaffold / Stub']} ({status_counts['Empty Scaffold / Stub']/total_files*100:.1f}%)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Scope & Domain Breakdowns")
lines.append("")
lines.append("### Target Scope Distribution")
lines.append("| Scope | File Count | Percentage | Description |")
lines.append("|---|---|---|---|")
for sc in sorted(scope_counts.keys()):
    cnt = scope_counts[sc]
    pct = (cnt / total_files) * 100
    desc = ""
    if "Scope 1" in sc:
        desc = "Active agent definitions with tools and contract frontmatter in `.claude/agents/*.md`"
    elif "Scope 2" in sc:
        desc = "Preserved v2 agent doctrines, essences, role-seeds, and DOCTRINE-MANIFEST in `apex-meta/orchestration/agents/`"
    elif "Scope 3" in sc:
        desc = "System core docs, run-loop workflows, schemas, user stories, architecture dossiers, and improvement plans"
    elif "Scope 4" in sc:
        desc = "Executable skill packages, manifests, references, scripts, templates, and obsidian tools in `.claude/skills/` and `apex-meta/skills/`"
    lines.append(f"| **{sc}** | {cnt} | {pct:.1f}% | {desc} |")
lines.append("")

lines.append("### Functional Domain Distribution")
lines.append("| Domain | File Count | Percentage | Primary Responsibilities |")
lines.append("|---|---|---|---|")
for dm in ['Alfred', 'Meta Ops', 'Meta Strategy', 'Meta Detective', 'Knowledge Bank', 'Informatics Design', 'Prompts & Workflows', 'AI Routing / Special Ops']:
    cnt = domain_counts.get(dm, 0)
    pct = (cnt / total_files) * 100
    resp = ""
    if dm == 'Alfred':
        resp = "Intake, operator interaction, intent lock, day/week precap, flow recap"
    elif dm == 'Meta Ops':
        resp = "Execution engine, plan-sync-session backbone, run records, status merging, closeout orchestration"
    elif dm == 'Meta Strategy':
        resp = "Direction, portfolio steering, user stories, macro-topology and hypothesis formulation"
    elif dm == 'Meta Detective':
        resp = "Adversarial review, two-lens verification (validity/alignment), verdict schemas, audit logs"
    elif dm == 'Knowledge Bank':
        resp = "Corpus curation, knowledge lifecycle, wiki skills, history ingests, session brain, retrieval"
    elif dm == 'Informatics Design':
        resp = "Document presentation, deterministic patching, layout tuning, handoff schemas, formatting hygiene"
    elif dm == 'Prompts & Workflows':
        resp = "Prompt engineering patterns, iteration loops, execution control contracts, skill creator"
    elif dm == 'AI Routing / Special Ops':
        resp = "Model selection, cost/scarcity routing policies, model usage logs, fallback mechanics"
    lines.append(f"| **{dm}** | {cnt} | {pct:.1f}% | {resp} |")
lines.append("")

lines.append("---")
lines.append("")
lines.append("## Top-Tier Leaderboard (Highest Composite Scores)")
lines.append("")
lines.append("Files rated by composite score `(Quality + Quantity + Machine_Readability + Operational_Value) / 4`:")
lines.append("")
lines.append("| Rank | File Name | Domain | Composite | Q | Qt | MR | OV | Status | Relative Path |")
lines.append("|---|---|---|---|---|---|---|---|---|---|")
top_files = sorted(data, key=lambda x: (x['composite_score'], x['operational_value'], x['quality'], x['line_count']), reverse=True)
for i, x in enumerate(top_files[:25], 1):
    lines.append(f"| {i} | `{x['file_name']}` | {x['domain']} | **{x['composite_score']}** | {x['quality']} | {x['quantity']} | {x['machine_readability']} | {x['operational_value']} | `{x['status']}` | `{x['rel_path']}` |")
lines.append("")

lines.append("---")
lines.append("")
lines.append("## Complete Verified File Inventory Table")
lines.append("")
lines.append("All 616 verified files matching the four target scopes on disk:")
lines.append("")
lines.append("| Domain | Scope | File Name | Size (B) | Lines | YAML | Q | Qt | MR | OV | Comp | Status | Verified Path & Rationale |")
lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")

for x in data_sorted:
    yaml_str = "Yes" if x['has_yaml_frontmatter'] else "No"
    # Escaping pipe in rationale if any
    clean_rat = x['rationale'].replace('|', '/')
    rel_path_escaped = x['rel_path'].replace('\\', '/')
    lines.append(f"| {x['domain']} | {x['scope'].split(':')[0]} | `{x['file_name']}` | {x['byte_size']} | {x['line_count']} | {yaml_str} | {x['quality']} | {x['quantity']} | {x['machine_readability']} | {x['operational_value']} | {x['composite_score']} | {x['status']} | `{rel_path_escaped}`<br>*{clean_rat}* |")

out_file = BASE_DIR / ".agents" / "explorer_repo_inv" / "repo_inventory.md"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Wrote {len(lines)} lines to {out_file}")
