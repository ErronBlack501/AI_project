from app.extraction.pdf_extractor import extract_text_pdf
from app.extraction.layout_analyzer import analyse_layout

import pymupdf

PDF_PATH = "data/test/cv_test.pdf"

def get_blocks(pdf_path: str) -> list[dict]:
    document = pymupdf.open(pdf_path)
    blocks = []

    for page_nb, page in enumerate(document):
        page_blocks = page.get_text("blocks")

        for block in page_blocks:
            x0, y0, x1, y1, text = block[:5]
            text = text.strip()
            if not text:
                continue

            blocks.append({
                "page": page_nb + 1,
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1,
                "text": text
            })

    document.close()
    return blocks

blocks = get_blocks(PDF_PATH)
zones = analyse_layout(blocks)

for zone_name, zone_blocks in zones.items():
    print("\n" + "=" * 60)
    print(f"ZONE : {zone_name.upper()}")
    print("=" * 60)

    zone_blocks.sort(key=lambda block: block["y0"])

    for block in zone_blocks:
        print(
            f"\n[{block['x0']:.1f}, {block['y0']:.1f}]"
            f" - [{block['x1']:.1f}, {block['y1']:.1f}]"
        )

        print(block["text"])