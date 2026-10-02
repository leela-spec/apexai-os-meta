import os
import json
import datetime
from pathlib import Path

BASE_DIR = Path(r"c:\GitDev\apexai-os-meta").resolve()

# Scope 1: Active Agent Contracts: .claude/agents/*.md
# Scope 2: Orchestration Agent Doctrines & Manifests: apex-meta/orchestration/agents/ (including CORE.md, ESSENCE.md, DOCTRINE-MANIFEST.md, and all subdirectories/agent folders)
# Scope 3: System Core & Workflows: apex-meta/orchestration/ (00-START-HERE.md, ARCHITECTURE.md, workflows/, schemas/, user-stories/, new_final_v4/, architecture-improvements/)
# Scope 4: Skill Implementations: .claude/skills/ and apex-meta/skills/

files_to_check = []

# Scope 1
scope1_dir = BASE_DIR / ".claude" / "agents"
if scope1_dir.exists():
    for p in scope1_dir.rglob("*.md"):
        if p.is_file():
            files_to_check.append(("Scope 1: Active Agent Contracts", p))

# Scope 2
scope2_dir = BASE_DIR / "apex-meta" / "orchestration" / "agents"
if scope2_dir.exists():
    for p in scope2_dir.rglob("*"):
        if p.is_file():
            files_to_check.append(("Scope 2: Orchestration Agent Doctrines & Manifests", p))

# Scope 3
orch_dir = BASE_DIR / "apex-meta" / "orchestration"
for direct_file in ["00-START-HERE.md", "ARCHITECTURE.md"]:
    p = orch_dir / direct_file
    if p.exists() and p.is_file():
        files_to_check.append(("Scope 3: System Core & Workflows", p))

for sub in ["workflows", "schemas", "user-stories", "new_final_v4", "architecture-improvements"]:
    s_dir = orch_dir / sub
    if s_dir.exists():
        for p in s_dir.rglob("*"):
            if p.is_file():
                files_to_check.append(("Scope 3: System Core & Workflows", p))

# Scope 4
scope4_dir1 = BASE_DIR / ".claude" / "skills"
if scope4_dir1.exists():
    for p in scope4_dir1.rglob("*"):
        if p.is_file():
            files_to_check.append(("Scope 4: Skill Implementations", p))

scope4_dir2 = BASE_DIR / "apex-meta" / "skills"
if scope4_dir2.exists():
    for p in scope4_dir2.rglob("*"):
        if p.is_file():
            files_to_check.append(("Scope 4: Skill Implementations", p))

# Deduplicate just in case
seen = set()
unique_files = []
for scope, p in files_to_check:
    norm_path = str(p.resolve())
    if norm_path not in seen:
        seen.add(norm_path)
        unique_files.append((scope, p))

results = []

for scope, p in unique_files:
    stat = p.stat()
    size = stat.st_size
    mtime = datetime.datetime.fromtimestamp(stat.st_mtime, tz=datetime.timezone.utc).isoformat()
    
    # Read content to get line count, frontmatter, preview
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        line_count = len(lines)
    except Exception as e:
        lines = []
        line_count = 0

    has_yaml = False
    yaml_keys = []
    if len(lines) > 1 and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                has_yaml = True
                # extract keys
                for yline in lines[1:i]:
                    if ":" in yline and not yline.strip().startswith("#"):
                        key = yline.split(":")[0].strip()
                        if key and not key.startswith("-"):
                            yaml_keys.append(key)
                break

    # First non-empty lines for preview
    preview = []
    for l in lines[:25]:
        sl = l.strip()
        if sl:
            preview.append(sl)

    results.append({
        "scope": scope,
        "absolute_path": str(p),
        "rel_path": str(p.relative_to(BASE_DIR)),
        "file_name": p.name,
        "byte_size": size,
        "line_count": line_count,
        "last_modified": mtime,
        "has_yaml_frontmatter": has_yaml,
        "yaml_keys": yaml_keys,
        "preview": preview[:5]
    })

out_json = BASE_DIR / ".agents" / "explorer_repo_inv" / "raw_inventory.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Total files discovered: {len(results)}")
scope_counts = {}
for r in results:
    scope_counts[r['scope']] = scope_counts.get(r['scope'], 0) + 1
for s, c in scope_counts.items():
    print(f"  {s}: {c}")
