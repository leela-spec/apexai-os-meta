import json

with open(r"c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json", "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for r in data:
    avg = (r["quality"] + r["quantity"] + r["machine_readability"] + r["operational_value"]) / 4.0
    w_avg = round((r["quality"] * 0.3) + (r["quantity"] * 0.2) + (r["machine_readability"] * 0.2) + (r["operational_value"] * 0.3), 2)
    comp = r["composite_score"]
    if abs(avg - comp) > 1e-4:
        count += 1
        if count <= 15:
            print("%-35s Q:%d Qt:%d MR:%d OV:%d Comp:%.2f Avg:%.2f W_Avg:%.2f" % (r["file_name"][:35], r["quality"], r["quantity"], r["machine_readability"], r["operational_value"], comp, avg, w_avg))
print("Total discrepancies with simple avg:", count)
