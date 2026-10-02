import shutil
import os

base_target = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\PromptsAndWorkflows"

copies = [
    # 01_CURRENT_PROMPTS_AND_WORKFLOWS
    (r"c:\GitDev\apexai-os-meta\.claude\agents\prompts-workflows.md",
     os.path.join(base_target, "01_CURRENT_PROMPTS_AND_WORKFLOWS", "prompts-workflows.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\CORE.md",
     os.path.join(base_target, "01_CURRENT_PROMPTS_AND_WORKFLOWS", "CORE.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\ESSENCE.md",
     os.path.join(base_target, "01_CURRENT_PROMPTS_AND_WORKFLOWS", "ESSENCE.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\BEST_PRACTICES.md",
     os.path.join(base_target, "01_CURRENT_PROMPTS_AND_WORKFLOWS", "BEST_PRACTICES.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\MISTAKES.md",
     os.path.join(base_target, "01_CURRENT_PROMPTS_AND_WORKFLOWS", "MISTAKES.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\TEMPLATES.md",
     os.path.join(base_target, "01_CURRENT_PROMPTS_AND_WORKFLOWS", "TEMPLATES.md")),

    # 02_RESEARCH_AND_DESIGN
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "AGENT_HANDOFF_CONTRACTS.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\KBAudit\AnotherConstantFailure.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "AnotherConstantFailure.md")),
    (r"c:\GitDev\apexai-os-meta\.claude\skills\skill-creator\SKILL.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "SKILL.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\prompts-workflows\APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\LEARNING_QUEUE.md",
     os.path.join(base_target, "02_RESEARCH_AND_DESIGN", "LEARNING_QUEUE_populated.md")),

    # 90_SUPERSEDED
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw_Setup\migration_payload\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\LEARNING_QUEUE.md",
     os.path.join(base_target, "90_SUPERSEDED", "LEARNING_QUEUE_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\BEST_PRACTICES_v_old.md",
     os.path.join(base_target, "90_SUPERSEDED", "BEST_PRACTICES_v_old.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\patches\RESTART-01_BEST_PRACTICES.patch.md",
     os.path.join(base_target, "90_SUPERSEDED", "RESTART-01_BEST_PRACTICES.patch.md"))
]

for src, dst in copies:
    shutil.copy2(src, dst)
    print(f"Copied: {os.path.basename(src)} -> {dst} ({os.path.getsize(dst)} bytes)")

# Quarantined stubs for Untitled and promptworkflowsChat
untitled_stub = os.path.join(base_target, "90_SUPERSEDED", "Untitled_empty.md")
with open(untitled_stub, "w", encoding="utf-8") as f:
    f.write("# EMPTY_STATE QUARANTINE STUB: Untitled.md\n\n"
            "- **Original Origin:** `Previous_OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/NewResearchBecauseOfConstantFailure/Untitled.md`\n"
            "- **Source State:** 0 bytes, 0 lines\n"
            "- **Quarantine Rationale:** Abandoned 0-byte scratchpad file. Quarantined in `90_SUPERSEDED/` with `_empty.md` suffix to prevent downstream search traversal confusion.\n"
            "- **Ecosystem Status:** `Empty Scaffold / Stub`\n")
print(f"Created: Untitled_empty.md ({os.path.getsize(untitled_stub)} bytes)")

chat_stub = os.path.join(base_target, "90_SUPERSEDED", "promptworkflowsChat_empty.py")
with open(chat_stub, "w", encoding="utf-8") as f:
    f.write("# EMPTY_STATE QUARANTINE STUB: promptworkflowsChat.py\n\n"
            "# Original Origin: Previous_OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/NewResearchBecauseOfConstantFailure/promptworkflowsChat.py\n"
            "# Source State: 0 bytes, 0 lines\n"
            "# Quarantine Rationale: Abandoned 0-byte Python script draft. Quarantined in 90_SUPERSEDED/ with _empty.py suffix.\n"
            "# Ecosystem Status: Empty Scaffold / Stub\n")
print(f"Created: promptworkflowsChat_empty.py ({os.path.getsize(chat_stub)} bytes)")
