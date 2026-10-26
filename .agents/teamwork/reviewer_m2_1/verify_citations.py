import os
import re

plane4_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics"
m2_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"

rule_files = [
    "rule-09-recovery.md",
    "rule-10-stop-repairing.md",
    "rule-11-current-truth.md",
    "rule-12-surgical.md",
    "rule-13-editing.md",
    "rule-14-new-machinery.md",
    "rule-15-detour.md",
]

# Read canonical modules
p4_contents = {}
for mod in ["writing-profile.md", "file-architecture.md", "execution-modes.md", "anti-drift-rules.md", "governance-schemas.md"]:
    with open(os.path.join(plane4_dir, mod), "r", encoding="utf-8") as f:
        p4_contents[mod] = f.read()

print("Verifying canonical rule IDs cited in M2 files:")
all_found = True
for rf in rule_files:
    fpath = os.path.join(m2_dir, rf)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()

    # Find citations like `AD-07`, `EM-05`, etc.
    citations = re.findall(r"`([A-Z]{2}-\d{2})`", text)
    for cite in sorted(set(citations)):
        prefix = cite[:2]
        target_mod = {
            "WP": "writing-profile.md",
            "FA": "file-architecture.md",
            "EM": "execution-modes.md",
            "AD": "anti-drift-rules.md",
            "GS": "governance-schemas.md",
            "SB": None, # semantic block
        }.get(prefix)
        if target_mod:
            if cite not in p4_contents[target_mod]:
                print(f"[{rf}] Rule ID {cite} NOT found in canonical module {target_mod}!")
                all_found = False
            else:
                pass

print(f"All canonical rule ID citations verified in Plane 4 modules: {all_found}")
