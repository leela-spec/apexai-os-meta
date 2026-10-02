import os

sources = [
    (r"c:\GitDev\apexai-os-meta\.claude\agents\prompts-workflows.md", "prompts-workflows.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\CORE.md", "CORE.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\ESSENCE.md", "ESSENCE.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\BEST_PRACTICES.md", "BEST_PRACTICES.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\MISTAKES.md", "MISTAKES.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\TEMPLATES.md", "TEMPLATES.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md", "AGENT_HANDOFF_CONTRACTS.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\KBAudit\AnotherConstantFailure.md", "AnotherConstantFailure.md"),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\skill-creator\SKILL.md", "SKILL.md (skill-creator)"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md", "APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md", "APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md", "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md"),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md", "APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md", "PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md", "APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\LEARNING_QUEUE.md", "LEARNING_QUEUE.md (populated)"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\LEARNING_QUEUE.md", "LEARNING_QUEUE_empty.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\patches\RESTART-01_BEST_PRACTICES.patch.md", "RESTART-01_BEST_PRACTICES.patch.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\NewResearchBecauseOfConstantFailure\Untitled.md", "Untitled.md"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\NewResearchBecauseOfConstantFailure\promptworkflowsChat.py", "promptworkflowsChat.py"),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\skill-creator\scripts\__init__.py", "__init__.py"),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\BEST_PRACTICES_v_old.md", "BEST_PRACTICES_v_old.md")
]

for path, name in sources:
    if os.path.exists(path):
        size = os.path.getsize(path)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = sum(1 for _ in f)
        print(f"EXISTS: {name} | Size: {size:,} bytes | Lines: {lines:,} | Path: {path}")
    else:
        print(f"MISSING: {name} | Path: {path}")
