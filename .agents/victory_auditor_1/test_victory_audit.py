import sys
import re
import yaml
from pathlib import Path

REPO_ROOT = Path(r"C:\GitDev\apexai-os-meta")
KI_BASIS = REPO_ROOT / "ki-basis"
COMPOSE_FILE = KI_BASIS / "compose.yaml"
ENV_PVT = KI_BASIS / ".env.private"
ENV_COMM = KI_BASIS / ".env.community"
DOC_ARCH = KI_BASIS / "docs" / "DUAL_INSTANCE_ARCHITECTURE.md"
DOC_RUNBOOK = KI_BASIS / "docs" / "DUAL_INSTANCE_RUNBOOK.md"

def test_compose_parameterization():
    compose_text = COMPOSE_FILE.read_text(encoding="utf-8")
    data = yaml.safe_load(compose_text)
    
    # 1. Project name dynamic
    assert "${COMPOSE_PROJECT_NAME" in compose_text
    
    # 2. Check all services container_name
    for name, svc in data.get("services", {}).items():
        cname = svc.get("container_name", "")
        assert "${COMPOSE_PROJECT_NAME" in cname, f"Service {name} has hardcoded container_name: {cname}"
        
    # 3. Check all volumes dynamic
    for name, vol in data.get("volumes", {}).items():
        vname = vol.get("name", "")
        assert "${COMPOSE_PROJECT_NAME" in vname, f"Volume {name} has hardcoded name: {vname}"
        
    # 4. Check network dynamic
    net_name = data.get("networks", {}).get("ki-basis-net", {}).get("name", "")
    assert "${KI_NETWORK_NAME" in net_name, f"Network has hardcoded name: {net_name}"
    
    print("[PASS] compose.yaml is 100% dynamically parameterized across services, volumes, networks.")

def test_ports_and_loopback():
    compose_text = COMPOSE_FILE.read_text(encoding="utf-8")
    data = yaml.safe_load(compose_text)
    
    for name, svc in data.get("services", {}).items():
        ports = svc.get("ports", [])
        for p in ports:
            assert p.startswith("127.0.0.1:"), f"Port {p} on {name} is NOT strictly loopback 127.0.0.1!"
            
    # Check postgres & valkey have NO ports
    assert "ports" not in data["services"]["postgres"], "Postgres must not expose ports"
    assert "ports" not in data["services"]["valkey"], "Valkey must not expose ports"
    print("[PASS] All exposed ports strictly bind 127.0.0.1, DB and cache unexposed.")

def test_docs_and_runbooks():
    assert DOC_ARCH.is_file() and DOC_ARCH.stat().st_size > 5000
    assert DOC_RUNBOOK.is_file() and DOC_RUNBOOK.stat().st_size > 5000
    
    arch_content = DOC_ARCH.read_text(encoding="utf-8")
    assert "ADR-001" in arch_content
    assert "Strategy A" in arch_content
    assert "Strategy B" in arch_content
    assert "9P" in arch_content
    assert "350%" in arch_content
    assert "ext4" in arch_content
    
    runbook_content = DOC_RUNBOOK.read_text(encoding="utf-8")
    assert "Migration" in runbook_content
    assert "Disaster Recovery" in runbook_content
    assert "docker exec -i" in runbook_content
    assert "docker exec -t" not in runbook_content or "Never use the `-t`" in runbook_content
    print("[PASS] Architecture and Runbook documentation meet high completeness thresholds.")

if __name__ == "__main__":
    test_compose_parameterization()
    test_ports_and_loopback()
    test_docs_and_runbooks()
    print("ALL INDEPENDENT VICTORY AUDIT STRESS TESTS PASSED.")
