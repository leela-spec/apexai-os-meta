import os

candidate_files = [
    # Meta Ops
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\ARCHITECTURE.md",
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\DOCTRINE-MANIFEST.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\OPERATING_SPINE_CANON.md",
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-ops\INTEGRATION-apex-plan-sync-session.md",
    # Meta Detective
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_detective\appendices\Failures\FAILURE_AND_ANTI_DRIFT_LEDGER.md",
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-detective\CORE.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_detective\appendices\Failures\AnotherConstantFailure.md",
    # Meta Strategy
    r"C:\GitDev\apexai-os-meta\.claude\agents\meta-strategy.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_strategy\Appendices\DecisionMakingProcessReseearch_gem.md",
    # Prompts & Workflows
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\Patching\APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\Patching\APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\KBAudit\AGENT_PATCH_CONTRACT.md",
    # Informatics Design
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\informatics-design\CORE.md",
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\schemas\handoff-packet.schema.md",
    r"C:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md",
    # Knowledge Bank
    r"C:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\knowledge-bank\CORE.md",
    r"C:\GitDev\apexai-os-meta\.claude\skills\llm-wiki\SKILL.md",
    r"C:\GitDev\apexai-os-meta\.claude\skills\wiki-lint\SKILL.md",
    # AI Handling & Routing
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__ai_handling_routing\appendices\KBAudit\2Do_context_file_authority_reference.md",
    r"C:\GitDev\apexai-os-meta\.claude\skills\AIRouting\SKILL.md",
    # Hygiene Clean
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\QA_HYGIENE_PROTOCOL.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__hygiene_clean\TEMPLATES.md",
]

for p in candidate_files:
    exists = os.path.exists(p)
    size = os.path.getsize(p) if exists else 0
    lines = len(open(p, 'r', encoding='utf-8', errors='ignore').readlines()) if exists else 0
    print(f"[{'EXISTS' if exists else 'MISSING'}] {os.path.basename(p)}")
    print(f"  Path: {p}")
    print(f"  Size: {size:,} bytes | Lines: {lines}")
