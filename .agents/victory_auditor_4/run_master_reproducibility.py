import os, json, sys
sys.stdout.reconfigure(encoding="utf-8")

print("======================================================================")
print("APEX OS MULTI-AGENT DEEP AUDIT: COMPREHENSIVE REPRODUCIBILITY SUITE")
print("======================================================================")

# 1. Verify 1,153 Census Assets in agent_knowledge_matrix.json
matrix_path = r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json"
assert os.path.exists(matrix_path), f"Missing matrix: {matrix_path}"
with open(matrix_path, "r", encoding="utf-8") as f:
    matrix = json.load(f)
print(f"[1/5] Census Matrix: Exactly {len(matrix)} assets loaded from JSON.")
assert len(matrix) == 1153, f"Expected 1153 assets, found {len(matrix)}"

# 2. Verify Physical Disk Existence (Sample & Check All Staged)
staged_root = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents"
hubs = ["Alfred", "MetaOps", "MetaDetective", "MetaStrategy", "PromptsAndWorkflows", 
        "InformaticsDesign", "KnowledgeBank", "AIHandlingAndRouting", "HygieneClean"]

print("[2/5] Verifying 9 LostAgents Staging Hubs...")
total_staged_files = 0
total_staged_bytes = 0
for h in hubs:
    hp = os.path.join(staged_root, h)
    assert os.path.isdir(hp), f"Missing hub: {h}"
    idx = os.path.join(hp, "00_INDEX", "INDEX.md")
    assert os.path.exists(idx), f"Missing INDEX.md in {h}"
    h_files = [os.path.join(r, f) for r, d, fs in os.walk(hp) for f in fs]
    for f in h_files:
        assert os.path.getsize(f) > 0, f"Zero-byte file: {f}"
    h_bytes = sum(os.path.getsize(f) for f in h_files)
    total_staged_files += len(h_files)
    total_staged_bytes += h_bytes
    print(f"      - {h:22}: {len(h_files):2d} files | {h_bytes:7,d} bytes | INDEX: OK")

assert total_staged_files == 249, f"Expected 249 staged files, found {total_staged_files}"
assert total_staged_bytes == 3009408, f"Expected 3,009,408 bytes, found {total_staged_bytes}"
print(f"      -> Staging Total: {total_staged_files} files, {total_staged_bytes:,d} bytes (100% Match!)")

# 3. Verify the 8 Crown Jewels + Alfred Benchmark
print("[3/5] Verifying the Crown Jewels...")
jewels = [
    ("Meta Ops", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\OPERATING_SPINE_CANON.md", 13202, 291),
    ("Meta Detective", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_detective\appendices\Failures\FAILURE_AND_ANTI_DRIFT_LEDGER.md", 116262, 201),
    ("Meta Strategy", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_strategy\Appendices\DecisionMakingProcessReseearch_gem.md", 5442, 97),
    ("Prompts & Workflows", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md", 25687, 591),
    ("Informatics Design", r"c:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md", 8739, 159),
    ("Knowledge Bank", r"c:\GitDev\apexai-os-meta\.claude\skills\llm-wiki\SKILL.md", 35827, 640),
    ("AI Handling & Routing", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__ai_handling_routing\2Do_context_file_authority_reference.md", 17480, 391),
    ("Hygiene Clean", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\QA_HYGIENE_PROTOCOL.md", 15103, 424),
    ("Alfred Benchmark", r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\Alfred\02_RESEARCH_AND_DESIGN\Apex Alfred Orchestration Realization in Claude.md", 48548, 402)
]
for name, path, exp_sz, exp_ln in jewels:
    assert os.path.exists(path), f"Missing crown jewel: {path}"
    act_sz = os.path.getsize(path)
    act_ln = len(open(path, "rb").readlines())
    print(f"      - {name:22}: {act_sz:6,d} B | {act_ln:4d} L | {os.path.basename(path)}")
    assert act_sz == exp_sz, f"{name}: Size mismatch {act_sz} != {exp_sz}"

# 4. Verify 9 Unified Doctrine Specifications
print("[4/5] Verifying 9 Unified Doctrine Specifications...")
unified_specs = [
    ("Alfred", "01_CURRENT_ALFRED", "ALFRED_UNIFIED_DOCTRINE.md", 14713, 273),
    ("MetaOps", "01_CURRENT_META_OPS", "META_OPS_UNIFIED_DOCTRINE.md", 18249, 188),
    ("MetaDetective", "01_CURRENT_META_DETECTIVE", "META_DETECTIVE_UNIFIED_DOCTRINE.md", 20462, 261),
    ("MetaStrategy", "01_CURRENT_META_STRATEGY", "META_STRATEGY_UNIFIED_DOCTRINE.md", 16519, 217),
    ("PromptsAndWorkflows", "01_CURRENT_PROMPTS_AND_WORKFLOWS", "PROMPTS_AND_WORKFLOWS_UNIFIED_DOCTRINE.md", 31405, 360),
    ("InformaticsDesign", "01_CURRENT_INFORMATICS_DESIGN", "INFORMATICS_DESIGN_UNIFIED_DOCTRINE.md", 26795, 311),
    ("KnowledgeBank", "01_CURRENT_KNOWLEDGE_BANK", "KNOWLEDGE_BANK_UNIFIED_DOCTRINE.md", 26842, 314),
    ("AIHandlingAndRouting", "01_CURRENT_AI_HANDLING_AND_ROUTING", "AI_HANDLING_AND_ROUTING_UNIFIED_DOCTRINE.md", 27482, 296),
    ("HygieneClean", "01_CURRENT_HYGIENE_CLEAN", "HYGIENE_CLEAN_UNIFIED_DOCTRINE.md", 13692, 175)
]
tot_uni_b = 0
tot_uni_l = 0
for hub, sub, fname, sz, ln in unified_specs:
    fp = os.path.join(staged_root, hub, sub, fname)
    assert os.path.exists(fp), f"Missing unified spec: {fp}"
    act_sz = os.path.getsize(fp)
    act_ln = len(open(fp, "rb").readlines())
    tot_uni_b += act_sz
    tot_uni_l += act_ln
    assert act_sz == sz, f"{fname}: Size mismatch"
    print(f"      - {hub:22}: {act_sz:6,d} B | {act_ln:4d} L | {fname}")

assert tot_uni_b == 196159, f"Expected 196,159 bytes, found {tot_uni_b}"
assert tot_uni_l == 2395, f"Expected 2,395 lines, found {tot_uni_l}"
print(f"      -> Unified Doctrine Total: {tot_uni_b:,d} bytes, {tot_uni_l:,d} lines (100% Match!)")

# 5. Verify Quarantine Count (53 Files)
print("[5/5] Verifying 53 Quarantined Files in 90_SUPERSEDED...")
tot_quarantine = sum(len(os.listdir(os.path.join(staged_root, h, "90_SUPERSEDED"))) for h in hubs)
assert tot_quarantine == 53, f"Expected 53 quarantined files, found {tot_quarantine}"
print(f"      -> Quarantined Stubs: Exactly {tot_quarantine} stubs verified across all 9 hubs.")

print("\n======================================================================")
print("ALL AUDIT INVARIANTS MATHEMATICALLY CONFIRMED & GROUNDED ON DISK!")
print("======================================================================")
