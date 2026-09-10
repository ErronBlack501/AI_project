import pymupdf

def extract_text_pdf(pdf_path: str) -> str:
    """
    Extrait le texte d'un fichier PDF.

    Args:
        file_path: chemin vers le fichier PDF.

    Returns:
        str: le texte extrait du PDF.
    """

    document = pymupdf.open(pdf_path)
    pages_text = []
    for page in document:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda block: (block[1], block[0]))

        page_lines = []

        for block in blocks:
            text = block[4].strip()
            if text:
                page_lines.append(text)

        pages_text.append("\n".join(page_lines))

    document.close()

    return "\n".join(pages_text)