# act_collection.py

actuator = {
    "name": "CollectionActuator",
    "type": "actuator",
    "description": "Gère l'état d'une collection ou superpose/retire une collection en jeu.",
    "parameters": {
        "collection": {
            "type": "str",
            "description": "Nom de la collection ciblée"
        },
        "mode": {
            "type": "str",
            "description": "Opération à effectuer",
            "enum": [
                "SUSPEND_COLLECTION",        # Suspend la collection
                "RESUME_COLLECTION",         # Reprend la collection suspendue
                "ADD_OVERLAY_COLLECTION",    # Superpose la collection
                "REMOVE_OVERLAY_COLLECTION"  # Retire la superposition
            ]
        },
        "overlay_camera": {
            "type": "str",
            "description": "Nom de la caméra à utiliser pour la superposition (uniquement pour ADD_OVERLAY_COLLECTION)"
        },
        "use_logic": {
            "type": "bool",
            "description": "Active le traitement logique
