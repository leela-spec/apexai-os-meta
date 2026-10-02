import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

def check_file(path_str):
    exists = os.path.exists(path_str)
    print(f"Path: {path_str} -> Exists: {exists}")
    if not exists:
        # search if filename exists anywhere
        base = os.path.basename(path_str)
        # search in GitDev
        found = []
        for root, dirs, files in os.walk(r"c:\GitDev\apexai-os-meta"):
            if base in files:
                found.append(os.path.join(root, base))
        for root, dirs, files in os.walk(r"C:\Quasi Desktop\AI_PreperationUntil_06-26"):
            if base in files:
                found.append(os.path.join(root, base))
        if found:
            print(f"  --> But file '{base}' was found at:")
            for f in found:
                print(f"      {f}")
        else:
            print(f"  --> File '{base}' NOT FOUND anywhere!")

print("=== CHECKING QUESTIONABLE PATHS ===")
paths_to_test = [
    r"c:\GitDev\apexai-os-meta\.claude\agents\weekly-orchestrator.md",
    r"c:\GitDev\apexai-os-meta\.claude\agents\ai-handling-routing.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\NewResearchBecauseOfConstantFailure\Recap&ProcessImprovs\APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS_v2.md",
    r"C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\NewResearchBecauseOfConstantFailure\Recap&ProcessImprovs\APPENDIX_KB_PREIMAGE_CHECKED_SCAFFOLD_MUTATION_PROCESS_v3.md",
    r"C:\Quasi Desktop\agent_kb_source_indexes",
    r"C:\GitDev\apexai-os-meta\.claude\skills\evidence",
    r"c:\GitDev\apexai-os-meta\.claude\agents\meta-ops.md",
    r"c:\GitDev\apexai-os-meta\.claude\agents\meta-detective.md",
    r"c:\GitDev\apexai-os-meta\.claude\agents\meta-strategy.md",
]

for p in paths_to_test:
    check_file(p)

print("\n=== LISTING ALL FILES IN .claude/agents/ ===")
agents_dir = r"c:\GitDev\apexai-os-meta\.claude\agents"
if os.path.exists(agents_dir):
    for f in os.listdir(agents_dir):
        print(f"  {f}")
