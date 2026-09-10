import re

def clean_text(text: str) -> str:
    """
    Nettoie le texte extrait d'un CV.

    Args:
        text: le texte brut extrait du CV.

    Returns:
        Le texte nettoyé.
    """

    # Remplacer les retours à la ligne par \n
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Supprimer les espaces en début et fin de ligne
    lines = [line.strip() for line in text.split('\n')]

    # Supprimer les lignes vides
    lines = [line for line in lines if line]

    # Nettoyer les espaces multiples à l'intérieur des lignes
    lines = [re.sub(r'\s+', ' ', line) for line in lines]

    # Reconstituer le texte nettoyé
    cleaned_text = '\n'.join(lines)

    return cleaned_text