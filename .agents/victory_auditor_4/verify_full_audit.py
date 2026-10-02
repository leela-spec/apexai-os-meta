import os
import re
import sys

dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"
dossiers = [
    "META_OPS_DEEP_AUDIT.md",
    "META_DETECTIVE_DEEP_AUDIT.md",
    "META_STRATEGY_DEEP_AUDIT.md",
    "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
    "INFORMATICS_DESIGN_DEEP_AUDIT.md",
    "KNOWLEDGE_BANK_DEEP_AUDIT.md",
    "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
    "HYGIENE_CLEAN_DEEP_AUDIT.md",
]
master_index = "ALL_AGENTS_DEEP_AUDIT_INDEX.md"

def resolve_path(p):
    p = p.strip().strip("`").strip('"').strip("'")
    if os.path.exists(p):
        return p
    # Try extended prefix if on windows
    if not p.startswith("\\\\?\\") and os.path.exists("\\\\?\\" + p):
        return "\\\\?\\" + p
    return None

def count_lines_and_bytes(filepath):
    sz = os.path.getsize(filepath)
    with open(filepath, "rb") as f:
        lines = f.read().splitlines()
    return sz, len(lines)

print("================================================================================")
print("TEST 1: PARSING TABLES ACROSS ALL 8 DOSSIERS & MASTER INDEX FOR PATH GROUNDING")
print("================================================================================")

all_paths_checked = {}
phantom_paths = []
size_mismatches = []
line_mismatches = []

files_to_scan = dossiers + [master_index]

for doc in files_to_scan:
    doc_path = os.path.join(dossier_dir, doc)
    with open(doc_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Regex to find table rows with paths (looking for paths starting with C:\ or c:\ or relative paths)
    table_rows = re.findall(r"^\|([^|\n]+(?:\|[^|\n]+)+)\|?$", text, re.MULTILINE)
    
    doc_paths_found = 0
    for row in table_rows:
        cols = [c.strip() for c in row.split("|")]
        # Search columns for path-like strings
        for i, col in enumerate(cols):
            clean_col = col.strip("`").strip()
            if re.search(r"^[c-zC-Z]:\\", clean_col) or clean_col.startswith(r"\\?\C:"):
                raw_path = clean_col
                # Check if there are size/line columns nearby
                claimed_size = None
                claimed_lines = None
                for other_col in cols:
                    oc = other_col.replace(",", "").strip()
                    # size or lines
                    m_size = re.search(r"^(\d+)\s*(?:B|bytes)?$", oc, re.I)
                    # Often table has: Comp | Q | Qt | MR | OV | Size (Bytes) | Lines | Status | Path
                
                resolved = resolve_path(raw_path)
                if not resolved:
                    phantom_paths.append((doc, raw_path))
                else:
                    sz, lines = count_lines_and_bytes(resolved)
                    all_paths_checked[raw_path] = (resolved, sz, lines)
                doc_paths_found += 1
    print(f"{doc:38s}: Found {doc_paths_found:3d} path references in tables")

print(f"\nUnique absolute paths checked across all tables: {len(all_paths_checked)}")
print(f"Phantom paths detected: {len(phantom_paths)}")
if phantom_paths:
    for doc, p in phantom_paths:
        print(f"  PHANTOM: [{doc}] {p}")

print("\n================================================================================")
print("TEST 2: CROWN JEWEL VERBATIM CITATION AUDIT")
print("================================================================================")

crown_jewels = [
    {
        "agent": "Meta Ops",
        "dossier": "META_OPS_DEEP_AUDIT.md",
        "file": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\OPERATING_SPINE_CANON.md",
        "quotes": [
            "This file defines the top-level operating law for the living OpenClaw system",
            "Govern in this order: operating spine -> project interface control -> knowledge promotion -> file production",
            "The authority chain is `BePr_SSOT -> SSOT -> OpState`",
            "The operating spine runs through four nested loops",
            "The operating spine preserves two orthogonal splits",
            "QA/Hygiene is a co-equal control lane and may block progress work"
        ]
    },
    {
        "agent": "Meta Detective",
        "dossier": "META_DETECTIVE_DEEP_AUDIT.md",
        "file": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\agent_kb_source_indexes\FAILURE_AND_ANTI_DRIFT_LEDGER.md",
        "quotes": [
            "Seven-column schema", # Or table schema check
            "KB-INFORMATICS-DESIGN-010"
        ]
    },
    {
        "agent": "Meta Strategy",
        "dossier": "META_STRATEGY_DEEP_AUDIT.md",
        "file": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\BasicFiles4Agents\DecisionMakingProcessReseearch_gem.md",
        "quotes": [
            "Cognitive Architecture",
            "First Principles"
        ]
    },
    {
        "agent": "Prompts & Workflows",
        "dossier": "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
        "file": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\AGENT_HANDOFF_CONTRACTS.md",
        "quotes": [
            "Stop conditions",
            "Packet minimums"
        ]
    },
    {
        "agent": "Informatics Design",
        "dossier": "INFORMATICS_DESIGN_DEEP_AUDIT.md",
        "file": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md",
        "quotes": [
            "One chunk, one job",
            "Progressive disclosure",
            "STE ceilings"
        ]
    },
    {
        "agent": "Knowledge Bank",
        "dossier": "KNOWLEDGE_BANK_DEEP_AUDIT.md",
        "file": r"c:\GitDev\apexai-os-meta\.claude\skills\llm-wiki\SKILL.md",
        "quotes": [
            "three-layer architecture",
            "raw sources"
        ]
    },
    {
        "agent": "AI Handling & Routing",
        "dossier": "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
        "file": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\BasicFiles4Agents\2Do_context_file_authority_reference.md",
        "quotes": [
            "500-token",
            "Directive"
        ]
    },
    {
        "agent": "Hygiene Clean",
        "dossier": "HYGIENE_CLEAN_DEEP_AUDIT.md",
        "file": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\QA_HYGIENE_PROTOCOL.md",
        "quotes": [
            "QA_HYGIENE_PROTOCOL",
            "finding classes"
        ]
    }
]

for cj in crown_jewels:
    print(f"\nVerifying Crown Jewel for {cj['agent']}:")
    target_f = resolve_path(cj["file"])
    if not target_f:
        print(f"  FAILED: Crown Jewel physical file missing: {cj['file']}")
        continue
    sz, lcnt = count_lines_and_bytes(target_f)
    print(f"  Physical File: {target_f}")
    print(f"  Verified Size: {sz:,d} bytes | Verified Lines: {lcnt}")
    
    with open(target_f, "r", encoding="utf-8", errors="replace") as f:
        file_text = f.read()
    
    for q in cj["quotes"]:
        # case-insensitive check
        found = bool(re.search(re.escape(q), file_text, re.I))
        print(f"    Citation [{q[:40]}...]: {'FOUND' if found else 'NOT FOUND'}")

print("\n================================================================================")
print("TEST 3: FULL CENSUS DATASET GROUNDING (agent_knowledge_matrix.json)")
print("================================================================================")

matrix_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json"
if os.path.exists(matrix_path):
    import json
    with open(matrix_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    missing_assets = []
    for item in data:
        p = item.get("absolute_path")
        if not resolve_path(p):
            missing_assets.append(p)
    print(f"Total Census Assets in Dataset: {len(data)}")
    print(f"Missing / Phantom Assets: {len(missing_assets)}")
    if missing_assets:
        for ma in missing_assets[:10]:
            print(f"  MISSING: {ma}")
else:
    print(f"Matrix JSON missing at {matrix_path}")

