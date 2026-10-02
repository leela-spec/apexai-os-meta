import json

with open(r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# check how many match weighted vs unweighted vs other
match_weighted = 0
match_unweighted = 0
match_other = 0

for r in data:
    q, qt, mr, ov = r["quality"], r["quantity"], r["machine_readability"], r["operational_value"]
    comp = r["composite_score"]
    w = round(q*0.3 + qt*0.2 + mr*0.2 + ov*0.3, 2)
    u = round((q + qt + mr + ov)/4.0, 2)
    if abs(w - comp) < 0.05:
        match_weighted += 1
    elif abs(u - comp) < 0.05:
        match_unweighted += 1
    else:
        match_other += 1

print(f"Match weighted (0.3/0.2/0.2/0.3): {match_weighted}")
print(f"Match unweighted (mean): {match_unweighted}")
print(f"Match other: {match_other}")
