import os
import shutil

staging_root = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\KnowledgeBank"
dirs = [
    os.path.join(staging_root, "00_INDEX"),
    os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK"),
    os.path.join(staging_root, "02_RESEARCH_AND_DESIGN"),
    os.path.join(staging_root, "90_SUPERSEDED")
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Directory ready: {d}")

# Copy map
copies = [
    # 01_CURRENT_KNOWLEDGE_BANK
    (r"c:\GitDev\apexai-os-meta\.claude\agents\knowledge-bank.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "knowledge-bank.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\agents\apex-kb-operator.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "apex-kb-operator.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\CORE.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "CORE.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\ESSENCE.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "ESSENCE.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\BEST_PRACTICES.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "BEST_PRACTICES.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\MISTAKES.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "MISTAKES.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\TEMPLATES.md",
     os.path.join(staging_root, "01_CURRENT_KNOWLEDGE_BANK", "TEMPLATES.md")),

    # 02_RESEARCH_AND_DESIGN
    (r"c:\GitDev\apexai-os-meta\.claude\skills\llm-wiki\SKILL.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "SKILL_llm-wiki.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\wiki-lint\SKILL.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "SKILL_wiki-lint.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\wiki-query\SKILL.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "SKILL_wiki-query.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\wiki-ingest\SKILL.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "SKILL_wiki-ingest.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\wiki-export\SKILL.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "SKILL_wiki-export.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\session-brain\SKILL.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "SKILL_session-brain.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\APPENDIX_KB_DATABASE_SCHEMA.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_DATABASE_SCHEMA.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\APPENDIX_KB_EXAMPLES.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_EXAMPLES.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_CANDIDATE_LEDGER.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_CANDIDATE_LEDGER.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_INFORMATION_RANKING_LEDGER.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_INFORMATION_RANKING_LEDGER.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_PROMOTION_TRACE.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_PROMOTION_TRACE.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_SOURCE_MANIFEST.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_SOURCE_MANIFEST.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\APPENDIX_KB_SOURCE_NOTES.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_SOURCE_NOTES.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\PROMPTFLOW_KB_BASE_BUILD.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "PROMPTFLOW_KB_BASE_BUILD.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\knowledge\KB_STARTING_SOURCE_MAP.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "KB_STARTING_SOURCE_MAP.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\knowledge\AGENT_KB_LANES.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "AGENT_KB_LANES.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\appendices\KBFuture.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "KBFuture.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\knowledge\KB_PROMOTION_LEDGER_TEMPLATE.md",
     os.path.join(staging_root, "02_RESEARCH_AND_DESIGN", "KB_PROMOTION_LEDGER_TEMPLATE.md")),

    # 90_SUPERSEDED
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\BEST_PRACTICES.md",
     os.path.join(staging_root, "90_SUPERSEDED", "BEST_PRACTICES_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\MISTAKES.md",
     os.path.join(staging_root, "90_SUPERSEDED", "MISTAKES_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\TEMPLATES.md",
     os.path.join(staging_root, "90_SUPERSEDED", "TEMPLATES_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__knowledge_bank\LEARNING_QUEUE.md",
     os.path.join(staging_root, "90_SUPERSEDED", "LEARNING_QUEUE_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agents\special_ops__knowledge_bank.md",
     os.path.join(staging_root, "90_SUPERSEDED", "special_ops__knowledge_bank_v2.md")),
]

for src, dst in copies:
    if os.path.exists(src):
        shutil.copy2(src, dst)
        size = os.path.getsize(dst)
        with open(dst, 'r', encoding='utf-8', errors='ignore') as f:
            lines = sum(1 for _ in f)
        print(f"Copied: {os.path.basename(dst)} ({size} B, {lines} L)")
    else:
        print(f"ERROR: Source does not exist: {src}")
