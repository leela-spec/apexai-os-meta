import re
from pathlib import Path

repo_root = Path(r"c:\GitDev\apexai-os-meta")
base = repo_root / "apex-meta" / "informatics" / "Agent_Setup" / "NextIteration" / "v2-always-on-architecture"

target_files = [
    base / "03-BLUEPRINT-agents.md",
    base / "13-candidate-3A-xml.md",
    base / "14-candidate-3B-hybrid.md"
]

print("=" * 70)
print("LINK INTEGRITY AUDIT")
print("=" * 70)

for fpath in target_files:
    print(f"\nAuditing links in: {fpath.name}")
    content = fpath.read_text(encoding="utf-8")

    # Match markdown links: [text](target)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, target in links:
        # Check target
        clean_target = target.strip()
        if clean_target.startswith("http://") or clean_target.startswith("https://"):
            # Web URL
            print(f"  [WEB URL] {clean_target} -> OK")
            continue

        if clean_target.startswith("file:///"):
            # file URL
            # e.g. file:///c:/GitDev/apexai-os-meta/AGENTS.md
            local_path = clean_target.replace("file:///", "")
            # handle windows path like c:/GitDev/...
            p = Path(local_path)
            exists = p.exists()
            print(f"  [FILE URL] {clean_target} -> {'EXISTS' if exists else 'BROKEN!'}")
            if not exists:
                print(f"    *** BROKEN LINK: {p} does not exist! ***")
            continue

        # Relative path
        rel_p = (fpath.parent / clean_target).resolve()
        exists = rel_p.exists()
        print(f"  [REL LINK] {clean_target} -> {'EXISTS' if exists else 'BROKEN!'}")
        if not exists:
            print(f"    *** BROKEN LINK: {rel_p} does not exist! ***")
