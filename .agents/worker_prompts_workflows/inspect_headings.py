with open(r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\processes\AGENT_HANDOFF_CONTRACTS.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in AGENT_HANDOFF_CONTRACTS: {len(lines)}")
for idx, line in enumerate(lines):
    if line.startswith('#'):
        print(f"Line {idx+1}: {line.strip()}")

print("\n--- AnotherConstantFailure ---")
with open(r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\KBAudit\AnotherConstantFailure.md', 'r', encoding='utf-8') as f:
    af_lines = f.readlines()

print(f"Total lines in AnotherConstantFailure: {len(af_lines)}")
for idx, line in enumerate(af_lines):
    if line.startswith('#'):
        print(f"Line {idx+1}: {line.strip()}")
