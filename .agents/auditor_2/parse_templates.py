import re
import yaml

with open(r"C:\GitDev\apexai-os-meta\ki-basis\docs\OPERATOR_RUNBOOKS_AND_TEMPLATES.md", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"###\s+([^\r\n]+)\r?\n```(?:yaml|docker-compose)\s*\r?\n(.*?)```", re.DOTALL)
matches = pattern.findall(content)
print(f"Found {len(matches)} matching YAML blocks.\n")

for title, block in matches:
    print(f"==================================================")
    print(f"Section: {title}")
    print(f"==================================================")
    parsed = yaml.safe_load(block)
    assert isinstance(parsed, dict), "Parsed content must be a dictionary"
    
    print("Compose Project Name:", parsed.get("name"))
    print("Networks:", list(parsed.get("networks", {}).keys()))
    
    volumes = parsed.get("volumes", {})
    print(f"Volumes ({len(volumes)} total):")
    for vname, vspec in volumes.items():
        is_ext = vspec.get("external") if isinstance(vspec, dict) else False
        real_name = vspec.get("name") if isinstance(vspec, dict) else None
        print(f"  - {vname}: external={is_ext}, name={real_name}")
        assert is_ext is True, f"Volume {vname} in {title} must have external: true"
    
    services = parsed.get("services", {})
    print(f"Services ({len(services)} total):")
    for sname, sspec in services.items():
        cname = sspec.get("container_name")
        ports = sspec.get("ports", [])
        print(f"  - {sname}: container_name={cname}, ports={ports}")
    print("\n")

print("ALL COMPOSE BLOCKS PARSED SUCCESSFULLY AND ALL VOLUMES HAVE external: true!")
