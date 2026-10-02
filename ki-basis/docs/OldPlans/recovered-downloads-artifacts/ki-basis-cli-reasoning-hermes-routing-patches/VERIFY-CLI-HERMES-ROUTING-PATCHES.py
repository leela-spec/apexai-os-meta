from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: python VERIFY-CLI-HERMES-ROUTING-PATCHES.py C:\\GitDev\\apexai-os-meta")
repo = Path(sys.argv[1])
base = repo / "apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization"

checks = {
    base / "00-START-HERE.md": [
        "one reasoning/routing logic",
        "05A-CLI-REASONING-HERMES-ROUTING.md",
        "heavy-reasoning CLI agent -> Hermes local API",
    ],
    base / "04A-DOCKER-BACKGROUND-RUNTIME.md": [
        "Dashboard can remain closed",
        "True Docker-Engine-only",
    ],
    base / "05A-CLI-REASONING-HERMES-ROUTING.md": [
        "CLI agent powers Hermes",
        "API_SERVER_ENABLED=true",
        "OpenRouter will be configured now",
        "Privacy routing",
        "Do not build placeholders now",
    ],
    base / "05-HERMES-AI-CONTROL-STACK.md": [
        "FUTURE REAL-SKILL INTEGRATION",
        "05A-CLI-REASONING-HERMES-ROUTING.md",
    ],
    repo / "ki-basis/compose.yaml": [
        'API_SERVER_ENABLED: "true"',
        'API_SERVER_HOST: "0.0.0.0"',
        "HERMES_API_SERVER_KEY",
    ],
    repo / "ki-basis/.env.example": [
        "HERMES_API_SERVER_KEY=",
    ],
    repo / "ki-basis/scripts/invoke-hermes.ps1": [
        "HERMES_API_SERVER_KEY",
        "/v1/chat/completions",
    ],
    repo / "apex-meta/Alpine/ARCHITEKTUR-BASIS.md": [
        "CLI-first/background-only",
        "heavy-reasoning CLI agents call Hermes",
        "research/Docker-Desktop-Windows.md",
    ],
    base / "09-FINAL-INDEPENDENT-CLOSURE.md": [
        "CLI-reasoning/Hermes-routing bridge",
        "invalid Hermes API key",
        "no permanent parallel direct-product",
    ],
    base / "HANDOVER-NEXT-CHAT.md": [
        "CLI reasoning / Hermes routing bridge",
        "bb9333f7",
    ],
}
errors = []
for path, markers in checks.items():
    if not path.exists():
        errors.append(f"missing {path}")
        continue
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            errors.append(f"{path.name}: missing marker {marker!r}")

if errors:
    print("VERIFY FAIL")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)
print("VERIFY PASS — one canonical CLI -> Hermes routing architecture is present.")
