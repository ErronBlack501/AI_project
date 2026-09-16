from typing import Any

def analyse_layout(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Analyse et regroupe les blocs de texte.

    Args:
        blocks: liste de blocs contenant x0, y0, x1 et y1.

    Returns:
        Un dictionnaire contenent les zones détectées.
    """

    if not blocks:
        return {}

    #Déterminer les limites horizontales du documment
    min_x = min(block["x0"] for block in blocks)
    max_x = max(block["x1"] for block in blocks)

    document_width = max_x - min_x
    if document_width <= 0:
        return {"zone_1": blocks}

    threshold = min_x + document_width * 0.35

    zones = {"left": [], "right": []}

    for block in blocks:
        center_x = (block["x0"] + block["x1"]) / 2

        if center_x < threshold:
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