import os
import shutil

base = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents\MetaOps"

dirs = [
    os.path.join(base, "00_INDEX"),
    os.path.join(base, "01_CURRENT_META_OPS"),
    os.path.join(base, "02_RESEARCH_AND_DESIGN"),
    os.path.join(base, "90_SUPERSEDED"),
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created dir: {d}")

# Copy 01_CURRENT_META_OPS files
current_meta_ops_copies = [
    (r"c:\GitDev\apexai-os-meta\.claude\agents\meta-ops.md", os.path.join(base, "01_CURRENT_META_OPS", "meta-ops.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-ops\ESSENCE.md", os.path.join(base, "01_CURRENT_META_OPS", "ESSENCE.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-ops\ROLE-SEED.md", os.path.join(base, "01_CURRENT_META_OPS", "ROLE-SEED.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-ops\INTEGRATION-apex-plan-sync-session.md", os.path.join(base, "01_CURRENT_META_OPS", "INTEGRATION-apex-plan-sync-session.md")),
]

for src, dst in current_meta_ops_copies:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(dst)} ({os.path.getsize(dst)} bytes)")

# Copy 02_RESEARCH_AND_DESIGN files
research_copies = [
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\OPERATING_SPINE_CANON.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "OPERATING_SPINE_CANON.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\AGENT_SWARM_INTERACTION_CANON.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "AGENT_SWARM_INTERACTION_CANON.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\rules\ESCALATION_EXCEPTION_BLOCK.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "ESCALATION_EXCEPTION_BLOCK.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\agent_kb_source_indexes\META_HEADS_KB_BASE_BUILD_INDEX.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "META_HEADS_KB_BASE_BUILD_INDEX.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\BasicFiles4Agents\Validation&Authority\Val&AuthResearchClaude.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "Val&AuthResearchClaude.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\BasicFiles4Agents\WorkflowResearch\WORKFLOW_BEST_PRACTICES_RESEARCH.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "WORKFLOW_BEST_PRACTICES_RESEARCH.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\Codex\CODEX_GIT_EXECUTION_ESSENCE.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "CODEX_GIT_EXECUTION_ESSENCE.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\Codex\CODEX_RESILIENT_MIGRATION_PROCESS.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "CODEX_RESILIENT_MIGRATION_PROCESS.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\AIHowTo\Codex\Failure&Research\Failure1-ConstantContextLoss.md", os.path.join(base, "02_RESEARCH_AND_DESIGN", "Failure1-ConstantContextLoss.md")),
]

for src, dst in research_copies:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(dst)} ({os.path.getsize(dst)} bytes)")

# Copy 90_SUPERSEDED files (with _empty.md suffix where applicable)
superseded_copies = [
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_ops\BEST_PRACTICES.md", os.path.join(base, "90_SUPERSEDED", "BEST_PRACTICES_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_ops\MISTAKES.md", os.path.join(base, "90_SUPERSEDED", "MISTAKES_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_ops\TEMPLATES.md", os.path.join(base, "90_SUPERSEDED", "TEMPLATES_empty.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\meta_ops\LEARNING_QUEUE.md", os.path.join(base, "90_SUPERSEDED", "LEARNING_QUEUE_empty.md")),
    (r"c:\GitDev\apexai-os-meta\apex-meta\orchestration\agents\meta-ops\legacy-hygiene-clean-TEMPLATES.md", os.path.join(base, "90_SUPERSEDED", "legacy-hygiene-clean-TEMPLATES.md")),
    (r"C:\Quasi Desktop\AI_PreperationUntil_06-26\OpenClaw Infrastructure Files\GAP_REGISTER.md", os.path.join(base, "90_SUPERSEDED", "GAP_REGISTER_empty.md")),
]

for src, dst in superseded_copies:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(dst)} ({os.path.getsize(dst)} bytes)")

print("\nAll initial directories created and files copied successfully!")
