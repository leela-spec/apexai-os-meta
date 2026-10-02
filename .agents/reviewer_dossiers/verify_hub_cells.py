import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

HUB_DATA = {
    'Alfred': {'active': (5, 21113), 'research': (10, 201716), 'stubs': (6, 7838), 'index': (1, 4141), 'total': (22, 234808)},
    'MetaOps': {'active': (6, 34714), 'research': (10, 160373), 'stubs': (5, 9982), 'index': (1, 4323), 'total': (22, 209392)},
    'MetaDetective': {'active': (10, 64753), 'research': (18, 683470), 'stubs': (10, 6934), 'index': (1, 7613), 'total': (39, 762770)},
    'MetaStrategy': {'active': (5, 24290), 'research': (9, 119506), 'stubs': (4, 2677), 'index': (1, 4098), 'total': (19, 150571)},
    'PromptsAndWorkflows': {'active': (7, 82877), 'research': (10, 208887), 'stubs': (5, 12716), 'index': (1, 5209), 'total': (23, 309689)},
    'InformaticsDesign': {'active': (7, 49259), 'research': (15, 127286), 'stubs': (4, 2893), 'index': (1, 5575), 'total': (27, 185013)},
    'KnowledgeBank': {'active': (8, 63982), 'research': (21, 298031), 'stubs': (5, 5444), 'index': (1, 7091), 'total': (35, 374548)},
    'AIHandlingAndRouting': {'active': (10, 151976), 'research': (15, 384542), 'stubs': (7, 3200), 'index': (1, 6512), 'total': (33, 546230)},
    'HygieneClean': {'active': (7, 48215), 'research': (14, 160676), 'stubs': (7, 22266), 'index': (1, 5230), 'total': (29, 236387)},
}

base = r"C:\Quasi Desktop\AI_PreperationUntil_06-26\LostAgents"

all_matched = True
for hub, exp in HUB_DATA.items():
    hp = os.path.join(base, hub)
    # 00_INDEX
    idx_p = os.path.join(hp, '00_INDEX')
    idx_files = os.listdir(idx_p)
    idx_bytes = sum(os.path.getsize(os.path.join(idx_p, f)) for f in idx_files)
    
    # 01_CURRENT
    cur_name = [d for d in os.listdir(hp) if d.startswith('01_')][0]
    cur_p = os.path.join(hp, cur_name)
    cur_files = os.listdir(cur_p)
    cur_bytes = sum(os.path.getsize(os.path.join(cur_p, f)) for f in cur_files)
    
    # 02_RESEARCH
    res_p = os.path.join(hp, '02_RESEARCH_AND_DESIGN')
    res_files = os.listdir(res_p)
    res_bytes = sum(os.path.getsize(os.path.join(res_p, f)) for f in res_files)
    
    # 90_SUPERSEDED
    sup_p = os.path.join(hp, '90_SUPERSEDED')
    sup_files = os.listdir(sup_p)
    sup_bytes = sum(os.path.getsize(os.path.join(sup_p, f)) for f in sup_files)
    
    tot_files = len(idx_files) + len(cur_files) + len(res_files) + len(sup_files)
    tot_bytes = idx_bytes + cur_bytes + res_bytes + sup_bytes
    
    m_idx = (len(idx_files), idx_bytes) == exp['index']
    m_cur = (len(cur_files), cur_bytes) == exp['active']
    m_res = (len(res_files), res_bytes) == exp['research']
    m_sup = (len(sup_files), sup_bytes) == exp['stubs']
    m_tot = (tot_files, tot_bytes) == exp['total']
    
    status = 'MATCH' if (m_idx and m_cur and m_res and m_sup and m_tot) else 'MISMATCH'
    if status == 'MISMATCH':
        all_matched = False
        print(f"{hub:22} MISMATCH:")
        print(f"  Index: actual={(len(idx_files), idx_bytes)}, exp={exp['index']}")
        print(f"  Active: actual={(len(cur_files), cur_bytes)}, exp={exp['active']}")
        print(f"  Research: actual={(len(res_files), res_bytes)}, exp={exp['research']}")
        print(f"  Stubs: actual={(len(sup_files), sup_bytes)}, exp={exp['stubs']}")
        print(f"  Total: actual={(tot_files, tot_bytes)}, exp={exp['total']}")
    else:
        print(f"{hub:22} EXACT 100% MATCH: {tot_files} files, {tot_bytes:,} bytes")

print("\nOVERALL STATUS:", "PERFECT 100% DISK VERIFICATION" if all_matched else "FAILED")
