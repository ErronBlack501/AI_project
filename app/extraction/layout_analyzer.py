from typing import Any

def analyse_layout(blocks: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """
    Analyse et regroupe les blocs de texte.

    Args:
        blocks: liste de blocs contenant x0, y0, x1 et y1.

    Returns:
        Un dictionnaire contenent les zones détectées.
    """

    if not blocks:
        return {}

    # -- Déterminer la largeur globale du documment
    min_x = min(block["x0"] for block in blocks)
    max_x = max(block["x1"] for block in blocks)

    document_width = max_x - min_x
    if document_width <= 0:
        return {"zone_1": blocks}

    # Position approximative de la séparation des colonnes
    threshold = min_x + document_width * 0.35
    full_width_threshold = document_width * 0.75

    zones = {
        "full_width": [],
        "left": [],
        "right": []
    }

    # -- Regrouper les blocs par zone
    for block in blocks:
        x0 = block["x0"]
        x1 = block["x1"]
        block_width = x1 - x0

        center_x = (x0 + x1) / 2

        if block_width >= full_width_threshold:
            zones["full_width"].append(block)
        elif center_x < threshold:
            zones["left"].append(block)
        else:
            zones["right"].append(block)

    # Supprime les zones vides
    zone = {
        name: zone
        for name, zone in zones.items()
        if zone
    }

    return zones