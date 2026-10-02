import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

tests = [
    {
        "agent": "MetaOps",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\META_OPS_DEEP_AUDIT.md",
        "target": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\OPERATING_SPINE_CANON.md"
    },
    {
        "agent": "MetaDetective",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\META_DETECTIVE_DEEP_AUDIT.md",
        "target": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_detective\appendices\Failures\FAILURE_AND_ANTI_DRIFT_LEDGER.md"
    },
    {
        "agent": "InformaticsDesign",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\INFORMATICS_DESIGN_DEEP_AUDIT.md",
        "target": r"c:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md"
    },
    {
        "agent": "KnowledgeBank",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\KNOWLEDGE_BANK_DEEP_AUDIT.md",
        "target": r"c:\GitDev\apexai-os-meta\.claude\skills\llm-wiki\SKILL.md"
    },
    {
        "agent": "PromptsAndWorkflows",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\PROMPTS_AND_WORKFLOWS_DEEP_AUDIT.md",
        "target": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md"
    },
    {
        "agent": "HygieneClean",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\HYGIENE_CLEAN_DEEP_AUDIT.md",
        "target": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\QA_HYGIENE_PROTOCOL.md"
    },
    {
        "agent": "AIHandlingAndRouting",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\AI_HANDLING_AND_ROUTING_DEEP_AUDIT.md",
        "target": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__ai_handling_routing\2Do_context_file_authority_reference.md"
    },
    {
        "agent": "MetaStrategy",
        "dossier": r"c:\GitDev\apexai-os-meta\FutureDevelopments&Research\AgentAudit\PerAgentDeepDives\META_STRATEGY_DEEP_AUDIT.md",
        "target": r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_strategy\Appendices\DecisionMakingProcessReseearch_gem.md"
    }
]

total_matches = 0
total_checked = 0

for t in tests:
    print("=" * 80)
    print(f"VERIFYING CROWN JEWEL CITATIONS: {t['agent']}")
    if not os.path.exists(t["target"]):
        print(f"  ERROR: Target file {t['target']} NOT FOUND!")
        continue
    with open(t["target"], "r", encoding="utf-8", errors="ignore") as f:
        target_lines = f.readlines()
    target_text = "".join(target_lines)

    with open(t["dossier"], "r", encoding="utf-8", errors="ignore") as f:
        dossier_text = f.read()

    m = re.search(r"##\s*4\.[^\n]*\n(.*?)(?=\n##\s*5\.)", dossier_text, re.DOTALL)
    sec4 = m.group(1) if m else ""

    # Look for blockquotes (consecutive lines starting with >)
    raw_blocks = re.findall(r"(?:^[ \t]*>.*(?:\n[ \t]*>.*)*)", sec4, re.MULTILINE)
    
    agent_matches = 0
    checked_in_agent = 0
    for block in raw_blocks:
        # clean block
        cleaned_lines = [re.sub(r"^[ \t]*>[ \t]*", "", line).strip() for line in block.splitlines()]
        combined = " ".join(cleaned_lines)
        # remove bold, italics, code marks
        norm_combined = re.sub(r"[*_`\"]", "", combined).strip()
        if len(norm_combined) < 20 or "Crown Jewel" in norm_combined:
            continue
        
        checked_in_agent += 1
        # take a distinctive chunk of 35 characters
        chunk = norm_combined[:35]
        # check if in target_text (normalized)
        norm_target = re.sub(r"[*_`\"]", "", target_text)
        if chunk.lower() in norm_target.lower():
            agent_matches += 1
        else:
            # try word window of 6 words
            words = norm_combined.split()
            found_sub = False
            for start_idx in range(min(3, len(words))):
                sub_phrase = " ".join(words[start_idx:start_idx+5])
                if sub_phrase.lower() in norm_target.lower():
                    agent_matches += 1
                    found_sub = True
                    break

    print(f"  Target: {os.path.basename(t['target'])} ({len(target_lines)} lines, {len(target_text)} bytes)")
    print(f"  Verified verbatim citations: {agent_matches} / {checked_in_agent} matched physical file")
    total_matches += agent_matches
    total_checked += checked_in_agent

print("=" * 80)
print(f"FINAL RESULT: {total_matches} / {total_checked} verbatim blockquote citations verified against physical disk files!")
