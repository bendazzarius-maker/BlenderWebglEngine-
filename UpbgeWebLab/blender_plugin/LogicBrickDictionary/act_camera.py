# act_camera.py

actuator = {
    "name": "CameraActuator",
    "type": "actuator",
    "description": "Change la caméra active ou configure le suivi d'une cible.",
    "parameters": {
        "camera": {
            "type": "str",
            "description": "Nom de la caméra qui devient active."
        },
        "mode": {
            "type": "str",
            "description": "Mode d'opération du Camera Actuator.",
            "enum": [
                "SET_CAMERA",    # Définit la caméra active
                "TRACK_TO"       # Active le suivi vers une cible
            ]
        },
        "tracking_target": {
            "type": "str",
            "description": "Nom de l'objet à suivre (pour TRACK_TO)."
        },
        "use_logic": {
            "type": "bool",
            "description": "Active le traitement logique du déclencheur."
        }
    },
    "inputs": ["trigger"]
}
