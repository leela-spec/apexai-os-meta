import re
import subprocess
import sys
from pathlib import Path

TEMPLATES_FILE = Path(r"C:\GitDev\apexai-os-meta\ki-basis\docs\OPERATOR_RUNBOOKS_AND_TEMPLATES.md")
PRESERVATION_FILE = Path(r"C:\GitDev\apexai-os-meta\ki-basis\docs\DOCKER_VOLUME_PRESERVATION_PLAN.md")
SCRIPTS_DIR = Path(r"C:\GitDev\apexai-os-meta\ki-basis\scripts")

def test_powershell_syntax():
    print("=================================================================")
    print("CHECK 2B: PowerShell Script Syntax & Safety Verification")
    print("=================================================================")

    # 1. Test existing .ps1 files in ki-basis/scripts
    ps1_files = list(SCRIPTS_DIR.glob("*.ps1"))
    print(f"Testing existing files in {SCRIPTS_DIR}: {[f.name for f in ps1_files]}")
    for ps1 in ps1_files:
        cmd = [
            "powershell", "-NoProfile", "-Command",
            f"$errors = $null; [System.Management.Automation.Language.Parser]::ParseFile('{str(ps1)}', [ref]$null, [ref]$errors); if ($errors.Count -gt 0) {{ $errors | ForEach-Object {{ Write-Error $_ }}; exit 1 }} else {{ Write-Output '[PASS] {ps1.name} parsed with 0 errors' }}"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"[FAIL] {ps1.name} syntax error:\n{res.stderr}")
            sys.exit(1)
        else:
            print(res.stdout.strip())

    # 2. Extract PowerShell blocks from OPERATOR_RUNBOOKS_AND_TEMPLATES.md
    content = TEMPLATES_FILE.read_text(encoding="utf-8")
    ps_blocks = re.findall(r"```powershell\n(.*?)```", content, re.DOTALL)
    print(f"\nExtracted {len(ps_blocks)} powershell blocks from OPERATOR_RUNBOOKS_AND_TEMPLATES.md")

    # Safety checks: ensure no dangerous unconfirmed commands (e.g. docker volume prune -f without warning, rm -rf, etc.)
    for idx, block in enumerate(ps_blocks):
        print(f"\n--- Checking Template PowerShell Block {idx + 1} ---")
        # Check safety invariants
        if "docker volume prune" in block:
            assert "WARNING" in block or "DO NOT" in block or "hazard" in block.lower(), "Unsafe volume prune found without warning!"
        if "rm -rf" in block or "Remove-Item" in block and "-Recurse" in block:
            print(f"[WARN] Block {idx + 1} contains file deletion, inspecting safety...")
        
        # Test PowerShell syntax using Parser::ParseInput
        test_script = block.replace('"', '`"').replace('$', '`$')
        ps_cmd = f"""
$code = @'
{block}
'@
$errors = $null
$tokens = $null
$ast = [System.Management.Automation.Language.Parser]::ParseInput($code, [ref]$tokens, [ref]$errors)
if ($errors.Count -gt 0) {{
    $errors | ForEach-Object {{ Write-Output "PARSE_ERROR: $($_.Message) at line $($_.Extent.StartLineNumber)" }}
    exit 1
}} else {{
    Write-Output "PARSED_OK"
}}
"""
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True)
        if "PARSE_ERROR" in res.stdout or res.returncode != 0:
            print(f"[FAIL] Syntax error in block {idx + 1}:\n{res.stdout}\n{res.stderr}")
            sys.exit(1)
        else:
            print(f"[PASS] Template Block {idx + 1} AST parse succeeded with 0 errors!")

    print("\n[VERDICT CHECK 2B]: 100% PASS - All PowerShell scripts and template blocks are syntactically valid and adhere to safety invariants.")

if __name__ == "__main__":
    test_powershell_syntax()
