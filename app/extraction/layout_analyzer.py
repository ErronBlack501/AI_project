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
        return {"full_width": blocks}

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

        analyzed_block = block.copy()

        if block_width >= full_width_threshold:
            zone = "full_width"
        elif center_x < threshold:
            zone = "left"
        else:
            zone = "right"

        analyzed_block["zone"] = zone
        zones[zone].append(analyzed_block)

    # Supprime les zones vides
    return {
        name: zone_blocks
        for name, zone_blocks in zones.items()
        if zone_blocks
    }

def ordonner_blocs(zones: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    """
    Construit un order de lecture à partir des zones détectées.

    Args:
        zones: zones produites par analyse_layout().

    Returns:
        Liste des blocs dans leur ordre de lecture.
    """

    ordered_blocks = []

    # -- Ajouter les blocs de la zone full_width
    full_width_blocks = sorted(
        zones.get("full_width", []),
        key=lambda block: (block["y0"], block["x0"])
    )
    ordered_blocks.extend(full_width_blocks)

    # -- Ajouter les blocs de la zone left
    left_blocks = sorted(
        zones.get("left", []),
        key=lambda block: (block["y0"], block["x0"])
    )
    ordered_blocks.extend(left_blocks)

    # -- Ajouter les blocs de la zone right
    right_blocks = sorted(
        zones.get("right", []),
        key=lambda block: (block["y0"], block["x0"])
    )
    ordered_blocks.extend(right_blocks)

    return ordered_blocks