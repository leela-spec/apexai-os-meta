import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

DOSSIER_DIR = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
INDEX_FILE = os.path.join(DOSSIER_DIR, "ALL_AGENTS_DEEP_AUDIT_INDEX.md")

ALL_FILES = [
    INDEX_FILE,
    os.path.join(DOSSIER_DIR, "META_OPS_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "META_DETECTIVE_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "META_STRATEGY_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "INFORMATICS_DESIGN_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "KNOWLEDGE_BANK_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md"),
    os.path.join(DOSSIER_DIR, "HYGIENE_CLEAN_DEEP_AUDIT.md"),
]

GITDEV_ROOT = r"c:\GitDev\apexai-os-meta"
QUASI_ROOT = r"C:\Quasi Desktop\AI_PreperationUntil_06-26"

# Let's extract paths
# Common path patterns:
# 1. Backtick paths: `c:\...` or `C:\...`
# 2. Table cells with paths
# 3. Relative paths mentioned in tables

def extract_and_check_paths(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    fname = os.path.basename(filepath)
    print(f"\n==========================================")
    print(f"CHECKING PATHS IN: {fname}")
    print(f"==========================================")
    
    # 1. Absolute paths
    abs_paths = re.findall(r"[`\"']?([a-zA-Z]:\\[^`\"'\n\r<>|*?]+(?:\.[a-zA-Z0-9_-]+|\b))[`\"']?", content)
    # clean trailing punctuation/backticks
    cleaned_abs = set()
    for p in abs_paths:
        p = p.strip("`'\" \t.,;:)")
        # filter out things that are clearly not file paths or are just drive roots
        if len(p) > 3 and "\\" in p:
            cleaned_abs.add(p)
            
    print(f"Found {len(cleaned_abs)} distinct absolute path references.")
    missing_abs = []
    found_abs = []
    for p in sorted(cleaned_abs):
        # Check if exists as file or dir
        if os.path.exists(p):
            found_abs.append(p)
        else:
            # check if it has ellipsis or placeholder like "..."
            if "..." in p or "<" in p:
                continue
            missing_abs.append(p)
            
    print(f"  Verified existing on disk: {len(found_abs)}")
    if missing_abs:
        print(f"  WARNING: {len(missing_abs)} absolute paths NOT found on disk:")
        for m in missing_abs[:20]:
            print(f"    - {m}")
        if len(missing_abs) > 20:
            print(f"    ... and {len(missing_abs) - 20} more.")
    else:
        print("  ALL valid absolute paths confirmed to exist on disk! (0 phantom paths)")

    # 2. Inspect table rows in Section 5 (Leaderboard) and Section 8 (Staging)
    # Tables usually have columns like | File Name | ... | Verified Physical Path |
    # Let's extract all paths from markdown tables:
    table_rows = re.findall(r"^\|.*\|$", content, re.MULTILINE)
    table_paths = []
    for row in table_rows:
        cells = [c.strip() for c in row.split("|")[1:-1]]
        for cell in cells:
            cell_clean = cell.strip("`'\" ")
            if "\\" in cell_clean or "/" in cell_clean:
                # might be a path
                if cell_clean.startswith("c:\\") or cell_clean.startswith("C:\\"):
                    table_paths.append(cell_clean)
                elif cell_clean.startswith("GitDev:"):
                    rel = cell_clean.replace("GitDev:", "").strip(" `\\/")
                    table_paths.append(os.path.join(GITDEV_ROOT, rel))
                elif cell_clean.startswith("Quasi:"):
                    rel = cell_clean.replace("Quasi:", "").strip(" `\\/")
                    table_paths.append(os.path.join(QUASI_ROOT, rel))
                elif cell_clean.startswith("LostAgents\\"):
                    table_paths.append(os.path.join(QUASI_ROOT, cell_clean))
                elif cell_clean.startswith(".claude\\") or cell_clean.startswith("apex-meta\\"):
                    table_paths.append(os.path.join(GITDEV_ROOT, cell_clean))

    print(f"Found {len(table_paths)} paths in tables.")
    missing_table = []
    found_table = []
    for p in table_paths:
        p = p.strip("`'\" \t.,;:)")
        if "..." in p:
            continue
        if os.path.exists(p):
            found_table.append(p)
        else:
            missing_table.append(p)
    print(f"  Table paths verified existing: {len(found_table)}")
    if missing_table:
        print(f"  WARNING: {len(missing_table)} table paths not found on disk:")
        for m in missing_table[:10]:
            print(f"    - {m}")
    else:
        print("  ALL table paths exist on disk!")

for f in ALL_FILES:
    extract_and_check_paths(f)
