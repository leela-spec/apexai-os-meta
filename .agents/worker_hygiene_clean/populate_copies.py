import os
import shutil
import sys

staging_root = r'C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\HygieneClean'

d_index = os.path.join(staging_root, '00_INDEX')
d_current = os.path.join(staging_root, '01_CURRENT_HYGIENE_CLEAN')
d_research = os.path.join(staging_root, '02_RESEARCH_AND_DESIGN')
d_superseded = os.path.join(staging_root, '90_SUPERSEDED')

for d in [d_index, d_current, d_research, d_superseded]:
    os.makedirs(d, exist_ok=True)

# 1. Copies to 01_CURRENT_HYGIENE_CLEAN
copies_current = [
    (r'c:\GitDev\apexai-os-meta\.claude\skills\weekly-orchestrator\references\roles\hygiene-clean-doctrine.md',
     os.path.join(d_current, 'hygiene-clean-doctrine.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\ESSENCE.md',
     os.path.join(d_current, 'ESSENCE.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\BEST_PRACTICES.md',
     os.path.join(d_current, 'BEST_PRACTICES.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\MISTAKES.md',
     os.path.join(d_current, 'MISTAKES.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\TEMPLATES.md',
     os.path.join(d_current, 'TEMPLATES.md')),
]

for src, dst in copies_current:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(src)} -> {dst}")

# 2. Copies to 02_RESEARCH_AND_DESIGN
copies_research = [
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\QA_HYGIENE_PROTOCOL.md',
     os.path.join(d_research, 'QA_HYGIENE_PROTOCOL.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\Q&A&HygieneFuture.md',
     os.path.join(d_research, 'Q&A&HygieneFuture.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\PROMPTFLOW_SPECIAL_OPS_HYGIENE_CLEAN_KB_UPDATE_FOLDER_LOCAL_CORRECTED.md',
     os.path.join(d_research, 'PROMPTFLOW_SPECIAL_OPS_HYGIENE_CLEAN_KB_UPDATE_FOLDER_LOCAL_CORRECTED.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\CODEX_APPLY_PLAN_HYGIENE_CLEAN_PATCHSET.md',
     os.path.join(d_research, 'CODEX_APPLY_PLAN_HYGIENE_CLEAN_PATCHSET.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\APPENDIX_KB_SOURCE_MANIFEST.md',
     os.path.join(d_research, 'APPENDIX_KB_SOURCE_MANIFEST.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\APPENDIX_KB_CANDIDATE_LEDGER.md',
     os.path.join(d_research, 'APPENDIX_KB_CANDIDATE_LEDGER.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md',
     os.path.join(d_research, 'APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\APPENDIX_KB_INFORMATION_RANKING_LEDGER.md',
     os.path.join(d_research, 'APPENDIX_KB_INFORMATION_RANKING_LEDGER.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md',
     os.path.join(d_research, 'APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\ChangesHygiene.md',
     os.path.join(d_research, 'ChangesHygiene.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md',
     os.path.join(d_research, 'PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\PATCHSET_VALIDATION_REPORT.md',
     os.path.join(d_research, 'PATCHSET_VALIDATION_REPORT.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\LEARNING_QUEUE.md',
     os.path.join(d_research, 'LEARNING_QUEUE.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agents\special_ops__hygiene_clean.md',
     os.path.join(d_research, 'special_ops__hygiene_clean.md')),
]

for src, dst in copies_research:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(src)} -> {dst}")

# 3. Copies to 90_SUPERSEDED (Quarantined Stubs & Historical Bridges)
copies_superseded = [
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\BEST_PRACTICES.md',
     os.path.join(d_superseded, 'BEST_PRACTICES_empty.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\MISTAKES.md',
     os.path.join(d_superseded, 'MISTAKES_empty.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\TEMPLATES.md',
     os.path.join(d_superseded, 'TEMPLATES_empty.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\LEARNING_QUEUE.md',
     os.path.join(d_superseded, 'LEARNING_QUEUE_empty.md')),
    (r'c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-ops\legacy-hygiene-clean-TEMPLATES.md',
     os.path.join(d_superseded, 'legacy-hygiene-clean-TEMPLATES.md')),
    (r'c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\legacy-hygiene-clean-ESSENCE.md',
     os.path.join(d_superseded, 'legacy-hygiene-clean-ESSENCE.md')),
    (r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\appendices\ChangesHygiene2.md',
     os.path.join(d_superseded, 'ChangesHygiene2.md')),
]

for src, dst in copies_superseded:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(src)} -> {dst}")

print("Static copies complete.")
