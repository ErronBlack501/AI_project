import pymupdf

PDF_PATH = "data/test/cv_test.pdf"

def debug_pdf(pdf_path: str) -> None:
    """
    Débogue le processus d'extraction de texte d'un fichier PDF.

    """
    document = pymupdf.open(pdf_path)
    
    for page_number, page in enumerate(document, start=1):
        blocks = page.get_text("blocks")

        # Tri vertical puis horizontal
        blocks.sort(key=lambda block: (block[1], block[0]))

        for index, block in enumerate(blocks, start=1):
            x0, y0, x1, y1, text = block[:5]
            text = text.strip()

            if not text:
                continue

            print(f"/nBloc {index}")
            print(f"Position : x0={x0:.2f}, y0={y0:.2f}, "
                  f"x1={x1:.2f}, y1={y1:.2f}")
            print(f"Largeur : {x1 - x0:.2f}, Hauteur : {y1 - y0:.2f}")
            print(f"Texte : {text}")

    document.close()

if __name__ == "__main__":
    debug_pdf(PDF_PATH)