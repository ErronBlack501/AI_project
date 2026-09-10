import re

SECTION_PATTERN = {
    "contact": [
        "CONTACT",
        "COORDONNEES",
        "PERSONAL INFORMATION",
        "CONTACT INFORMATION",
    ],
    "education": [
        "EDUCATION",
        "EDUCATIONS",
        "FORMATION",
        "FORMATIONS",
    ],
    "experience": [
        "EXPERIENCE",
        "EXPÉRIENCE",
        "EXPÉRIENCES",
        "EXPERIENCES PROFESSIONNELLES",
        "EXPÉRIENCE PROFESSIONNELLE",
        "WORK EXPERIENCE",
        "PROFESSIONAL EXPERIENCE",
    ],
    "skills": [
        "SKILLS",
        "COMPETENCES",
        "COMPÉTENCES",
        "TECHNICAL SKILLS",
        "SOFT SKILLS",
    ],
    "languages": [
        "LANGUAGES",
        "LANGUES",
        "LANGUE",
    ],
    "certifications": [
        "CERTIFICATIONS",
        "CERTIFICATS",
        "CERTIFICAT",
    ],
    "interrests": [
        "INTERESTS",
        "INTERETS",
        "INTÉRÊTS",
        "CENTRES D'INTERET",
        "CENTRES D'INTÉRÊT",
        "HOBBIES",
    ],
    "qualities": [
        "QUALITIES",
        "QUALITÉS",
        "ATTRIBUTES",
        "PERSONAL QUALITIES",
        "SOFT SKILLS",
    ],
}

def normalize_section_title(title: str) -> str:
    """
    Normalise le titre d'une section en supprimant les accents et en le mettant en majuscules.
    """
    title = title.strip().upper()

    # Supprime les accents
    replacements = {
        "É": "E",
        "È": "E",
        "Ê": "E",
        "Ë": "E",
        "À": "A",
        "Â": "A",
        "Ä": "A",
        "Î": "I",
        "Ï": "I",
        "Ô": "O",
        "Ö": "O",
        "Ù": "U",
        "Û": "U",
        "Ü": "U",
        "Ç": "C",
    }

    for old, new in replacements.items():
        title = title.replace(old, new)

    title = re.sub(r"\s+", " ", title)

    return title

def detect_section(line: str) -> str | None:
    """
    Détermine si une ligne correspond à un titre de section.

    Returns:
        Le nom de la section si elle est détectée, sinon None.
    """

    normalized_line = normalize_section_title(line)

    for section, patterns in SECTION_PATTERN.items():
        for pattern in patterns:
            if normalized_line == normalize_section_title(pattern):
                return section

    return None