#!/usr/bin/env python3
"""Extract and inventory picture-bearing pages from a PDF.

This is intentionally narrow: it does not convert the full PDF to Markdown.
It extracts embedded images where possible and renders pages that contain
large image blocks so the visual material can be inspected separately.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def safe_stem(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in value).strip("_")


def render_page(page: fitz.Page, out_path: Path, zoom: float) -> None:
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix, alpha=False)
    pix.save(out_path)


def page_image_blocks(page: fitz.Page, min_area_ratio: float) -> list[dict[str, Any]]:
    page_area = float(page.rect.width * page.rect.height) or 1.0
    blocks: list[dict[str, Any]] = []
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") != 1:
            continue
        bbox = block.get("bbox") or [0, 0, 0, 0]
        width = max(0.0, float(bbox[2]) - float(bbox[0]))
        height = max(0.0, float(bbox[3]) - float(bbox[1]))
        ratio = (width * height) / page_area
        if ratio >= min_area_ratio:
            blocks.append(
                {
                    "bbox": [round(float(v), 2) for v in bbox],
                    "width_pt": round(width, 2),
                    "height_pt": round(height, 2),
                    "area_ratio": round(ratio, 4),
                    "ext": block.get("ext"),
                    "xref": block.get("xref"),
                }
            )
    return blocks


def extract_pdf_images(
    doc: fitz.Document,
    page: fitz.Page,
    out_dir: Path,
    page_number: int,
    min_width: int,
    min_height: int,
) -> list[dict[str, Any]]:
    extracted: list[dict[str, Any]] = []
    seen_xrefs: set[int] = set()

    for image_index, image in enumerate(page.get_images(full=True), start=1):
        xref = int(image[0])
        if xref in seen_xrefs:
            continue
        seen_xrefs.add(xref)

        width = int(image[2])
        height = int(image[3])
        if width < min_width and height < min_height:
            continue

        image_data = doc.extract_image(xref)
        ext = image_data.get("ext") or "bin"
        name = f"page-{page_number:04d}_xref-{xref}_{image_index}.{safe_stem(ext)}"
        out_path = out_dir / name
        out_path.write_bytes(image_data["image"])
        extracted.append(
            {
                "page": page_number,
                "xref": xref,
                "width_px": width,
                "height_px": height,
                "colorspace": image[5],
                "bits_per_component": image[4],
                "file": str(out_path),
            }
        )

    return extracted


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract picture evidence from a PDF without full text conversion.")
    parser.add_argument("pdf", help="Input PDF path.")
    parser.add_argument("--out-dir", default="artifacts/pdf-picture-extraction/ET-Heller-NARM")
    parser.add_argument("--min-width", type=int, default=300)
    parser.add_argument("--min-height", type=int, default=300)
    parser.add_argument("--min-area-ratio", type=float, default=0.04)
    parser.add_argument("--render-zoom", type=float, default=2.0)
    parser.add_argument("--render-page", type=int, action="append", default=[], help="Also render a specific 1-based PDF page.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = (repo_root / args.out_dir).resolve() if not Path(args.out_dir).is_absolute() else Path(args.out_dir)
    images_dir = out_dir / "images"
    pages_dir = out_dir / "pages"
    images_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    pages: list[dict[str, Any]] = []
    all_images: list[dict[str, Any]] = []
    render_pages: set[int] = set(args.render_page)

    for page_index in range(doc.page_count):
        page_number = page_index + 1
        page = doc.load_page(page_index)
        blocks = page_image_blocks(page, args.min_area_ratio)
        extracted = extract_pdf_images(doc, page, images_dir, page_number, args.min_width, args.min_height)
        all_images.extend(extracted)

        if blocks or extracted:
            render_pages.add(page_number)
            pages.append(
                {
                    "page": page_number,
                    "image_block_count": len(blocks),
                    "extracted_image_count": len(extracted),
                    "image_blocks": blocks,
                    "extracted_images": extracted,
                }
            )

    rendered: list[dict[str, Any]] = []
    for page_number in sorted(p for p in render_pages if 1 <= p <= doc.page_count):
        page = doc.load_page(page_number - 1)
        out_path = pages_dir / f"page-{page_number:04d}.png"
        render_page(page, out_path, args.render_zoom)
        rendered.append({"page": page_number, "file": str(out_path)})

    report = {
        "generated_at": iso_now(),
        "pdf": str(pdf_path),
        "page_count": doc.page_count,
        "thresholds": {
            "min_width": args.min_width,
            "min_height": args.min_height,
            "min_area_ratio": args.min_area_ratio,
            "render_zoom": args.render_zoom,
        },
        "picture_page_count": len(pages),
        "extracted_image_count": len(all_images),
        "rendered_page_count": len(rendered),
        "pages": pages,
        "rendered_pages": rendered,
    }

    json_path = out_dir / "picture-extraction-report.json"
    md_path = out_dir / "picture-extraction-report.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# PDF Picture Extraction Report",
        "",
        f"Generated: `{report['generated_at']}`",
        f"PDF: `{report['pdf']}`",
        f"Pages in PDF: `{report['page_count']}`",
        f"Picture pages: `{report['picture_page_count']}`",
        f"Extracted images: `{report['extracted_image_count']}`",
        f"Rendered pages: `{report['rendered_page_count']}`",
        "",
        "## Picture Pages",
        "",
        "| page | image blocks | extracted images | rendered page |",
        "|---:|---:|---:|---|",
    ]
    rendered_by_page = {item["page"]: item["file"] for item in rendered}
    for item in pages:
        page_number = item["page"]
        lines.append(
            f"| {page_number} | {item['image_block_count']} | {item['extracted_image_count']} | `{rel(Path(rendered_by_page.get(page_number, '')), repo_root) if page_number in rendered_by_page else ''}` |"
        )
    lines.extend(["", "## Outputs", "", f"- JSON report: `{rel(json_path, repo_root)}`", f"- Images: `{rel(images_dir, repo_root)}`", f"- Rendered pages: `{rel(pages_dir, repo_root)}`", ""])
    md_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"PDF pages: {doc.page_count}")
    print(f"Picture pages: {len(pages)}")
    print(f"Extracted images: {len(all_images)}")
    print(f"Rendered pages: {len(rendered)}")
    print(f"Report: {rel(json_path, repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
