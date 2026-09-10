from app.nlp.section_detector import detect_section

def parse_sections(text: str) -> dict[str, list[str]]:
    """
    Regroupe le contenu du CV par section.

    Args:
        text: le texte nettoyé du CV.

    Returns:
        Dictionnaire contenant les différentes sections et leur contenu.
    """
    sections = {}
    current_section = None

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # Vérifier si la ligne correspons à un titre de section
        detected_section = detect_section(line)
        if detected_section:
            current_section = detected_section

            # Créer la section si elle n'existe pas encore
            if current_section not in sections:
                sections[current_section] = []
            continue

        # Ajouter la ligne à la section actuelle
        if current_section:
            sections[current_section].append(line)
        
    return sections