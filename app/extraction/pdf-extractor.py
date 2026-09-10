import fitz

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrait le texte d'un fichier PDF.

    Args:
        file_path: chemin vers le fichier PDF.

    Returns:
        str: le texte extrait du PDF.
    """
    document = fitz.open(pdf_path)
    pages_text = []
    for page in document:
        text = page.get_text()
        pages_text.append(text)

    document.close()

    return "\n".join(pages_text)