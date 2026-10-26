import re
from pathlib import Path

INFORMATICS_DIR = Path(r"c:\GitDev\apexai-os-meta\apex-meta\informatics")

for fname in ["anti-drift-rules.md", "governance-schemas.md"]:
    content = (INFORMATICS_DIR / fname).read_text(encoding="utf-8")
    content_no_code = re.sub(r"```[\s\S]*?```", "", content)
    c_no_tags = re.sub(r"\[P[0-3]\s*\|\s*I\d+/E\d+/R\d+\]", "", content_no_code)
    c_no_tags = re.sub(r"\[P<tier>\s*\|\s*I<[^>]+>/E<[^>]+>/R<[^>]+>\]", "", c_no_tags)
    c_no_tags = re.sub(r"\(I<[^>]+>/E<[^>]+>/R<[^>]+>\)", "", c_no_tags)
    pat = re.compile(r"/\s*R(?![a-zA-Z0-9_<>])")
    for m in pat.finditer(c_no_tags):
        print(fname, "MATCH:", repr(m.group(0)), "CTX:", repr(c_no_tags[max(0, m.start()-30):min(len(c_no_tags), m.end()+30)]))
