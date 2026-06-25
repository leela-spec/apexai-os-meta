from pathlib import Path
import subprocess
import sys

ROOT = Path("apex-meta/kb/claude-skill-design/sources/curated/official-pdfs")
pdfs = sorted(ROOT.rglob("*.pdf"))

print(f"pdfs found: {len(pdfs)}")

for pdf in pdfs:
    md = pdf.with_suffix(".md")
    code = f"""
import pymupdf4llm
from pathlib import Path
pdf = Path(r'''{pdf}''')
md = Path(r'''{md}''')
text = pymupdf4llm.to_markdown(str(pdf))
md.write_text(text, encoding='utf-8')
"""
    result = subprocess.run([sys.executable, "-c", code], text=True, capture_output=True)

    if result.returncode == 0 and md.exists() and md.stat().st_size > 0:
        pdf.unlink()
        print(f"converted: {md}")
    else:
        print(f"FAILED: {pdf}")
        print(result.stderr)

print("done")
