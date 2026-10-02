import os
import shutil

target_base = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\InformaticsDesign"
dirs = [
    os.path.join(target_base, "00_INDEX"),
    os.path.join(target_base, "01_CURRENT_INFORMATICS_DESIGN"),
    os.path.join(target_base, "02_RESEARCH_AND_DESIGN"),
    os.path.join(target_base, "90_SUPERSEDED"),
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print("Ensured directory:", d)

# Files to copy for 01_CURRENT_INFORMATICS_DESIGN
current_files = [
    (r"C:\GitDev\apexai-os-meta\.claude\agents\informatics-design.md", "informatics-design.md"),
    (r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\CORE.md", "CORE.md"),
    (r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\ESSENCE.md", "ESSENCE.md"),
    (r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\BEST_PRACTICES.md", "BEST_PRACTICES.md"),
    (r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\MISTAKES.md", "MISTAKES.md"),
    (r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\TEMPLATES.md", "TEMPLATES.md"),
]

for src, dst_name in current_files:
    dst = os.path.join(target_base, "01_CURRENT_INFORMATICS_DESIGN", dst_name)
    shutil.copy2(src, dst)
    print(f"Copied {dst_name}: {os.path.getsize(dst)} bytes")

# Files to copy for 02_RESEARCH_AND_DESIGN
research_files = [
    (r"C:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md", "standard.md"),
    (r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\schemas\handoff-packet.schema.md", "handoff-packet.schema.md"),
    (r"C:\GitDev\apexai-os-meta\.claude\skills\obsidian-layout-adjustment\SKILL.md", "SKILL_obsidian-layout-adjustment.md"),
    (r"C:\GitDev\apexai-os-meta\.claude\skills\deterministic-markdown-patcher2\SKILL.md", "SKILL_deterministic-markdown-patcher2.md"),
    (r"C:\GitDev\apexai-os-meta\.claude\skills\graph-colorize\SKILL.md", "SKILL_graph-colorize.md"),
    (r"C:\GitDev\apexai-os-meta\.claude\skills\informatics-authoring\SKILL.md", "SKILL_informatics-authoring.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\agent_kb_source_indexes\KB_INFORMATICS_DEEP_RESEARCH_ONLINE_REPO_INDEX.yaml", "KB_INFORMATICS_DEEP_RESEARCH_ONLINE_REPO_INDEX.yaml"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\BasicFiles4Agents\InformationsDesign\INFORMATION_DESIGN_80_20_ESSENCE.md", "INFORMATION_DESIGN_80_20_ESSENCE.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\appendices\PromptFlowInfoDesi.md", "PromptFlowInfoDesi.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\kb4agents\special_ops_kb_factory_output\special_ops_kb_factory_output\agents\information_design\AGENT_CARD.md", "AGENT_CARD.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\appendices\APPENDIX_KB_SOURCE_MANIFEST.md", "APPENDIX_KB_SOURCE_MANIFEST.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\appendices\APPENDIX_KB_CANDIDATE_LEDGER.md", "APPENDIX_KB_CANDIDATE_LEDGER.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\appendices\APPENDIX_KB_INFORMATION_RANKING_LEDGER.md", "APPENDIX_KB_INFORMATION_RANKING_LEDGER.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\appendices\APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md", "APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\appendices\APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md", "APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md"),
]

for src, dst_name in research_files:
    dst = os.path.join(target_base, "02_RESEARCH_AND_DESIGN", dst_name)
    shutil.copy2(src, dst)
    print(f"Copied {dst_name}: {os.path.getsize(dst)} bytes")

# Files to copy for 90_SUPERSEDED (quarantine empty scaffolds)
superseded_files = [
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\BEST_PRACTICES.md", "BEST_PRACTICES_empty.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\MISTAKES.md", "MISTAKES_empty.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\TEMPLATES.md", "TEMPLATES_empty.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__informatics_design\LEARNING_QUEUE.md", "LEARNING_QUEUE_empty.md"),
]

for src, dst_name in superseded_files:
    dst = os.path.join(target_base, "90_SUPERSEDED", dst_name)
    shutil.copy2(src, dst)
    print(f"Copied {dst_name}: {os.path.getsize(dst)} bytes")

print("Initial staging copy completed successfully.")
