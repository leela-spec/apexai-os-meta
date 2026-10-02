import os
import re

dossier_dir = r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives"

crown_jewels = {
    "META_OPS_DEEP_AUDIT.md": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\OPERATING_SPINE_CANON.md",
    "META_DETECTIVE_DEEP_AUDIT.md": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_detective\appendices\Failures\FAILURE_AND_ANTI_DRIFT_LEDGER.md",
    "META_STRATEGY_DEEP_AUDIT.md": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_strategy\Appendices\DecisionMakingProcessReseearch_gem.md",
    "PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md",
    "INFORMATICS_DESIGN_DEEP_AUDIT.md": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md",
    "KNOWLEDGE_BANK_DEEP_AUDIT.md": r"c:\GitDev\apexai-os-meta\.claude\skills\llm-wiki\SKILL.md",
    "AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__ai_handling_routing\2Do_context_file_authority_reference.md",
    "HYGIENE_CLEAN_DEEP_AUDIT.md": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\QA_HYGIENE_PROTOCOL.md",
}

for dname, target_path in crown_jewels.items():
    dp = os.path.join(dossier_dir, dname)
    with open(dp, "r", encoding="utf-8") as f:
        dtext = f.read()
    with open(target_path, "r", encoding="utf-8", errors="replace") as f:
        target_text = f.read()

    print(f"=== Verifying Citations in {dname} ===")
    m4 = re.search(r"## 4\..*?(?=## 5|\Z)", dtext, re.S)
    if not m4:
        print("  NO SECTION 4!")
        continue
    sec4 = m4.group(0)
    
    # Check explicitly documented line/section citations:
    line_citations = re.findall(r"Lines?\s+(\d+)(?:[–-](\d+))?:?(.*?)(?=(?:####|###|\n\s*\n\s*\n|\Z))", sec4, re.S)
    print(f"  Found {len(line_citations)} line citation sections")
    
    # Check quotes
    quotes = re.findall(r'>\s*["*]*(.*?)["*]*\s*$', sec4, re.M)
    verified = 0
    missed = 0
    for q in quotes:
        clean = q.replace("*", "").replace('"', '').strip()
        if len(clean) > 20:
            sub = clean[:40]
            if sub.lower() in target_text.lower():
                verified += 1
            else:
                # check if key phrase in target_text
                words = clean.split()
                if len(words) >= 4 and " ".join(words[:4]).lower() in target_text.lower():
                    verified += 1
                else:
                    print(f"    Quote snippet: '{sub}...' -> NOT FOUND")
                    missed += 1
    print(f"  Verified Quotes: {verified} | Misses: {missed}")
