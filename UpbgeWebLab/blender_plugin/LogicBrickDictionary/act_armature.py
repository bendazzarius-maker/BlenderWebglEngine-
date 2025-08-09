# act_armature.py

actuator = {
    "name": "ArmatureActuator",
    "type": "actuator",
    "description": "Contrôle les actions d'une armature.",
    "parameters": {
        "action": {
            "type": "str",
            "description": "Nom de l'action à jouer",
        },
        "start_frame": {
            "type": "int",
            "description": "Frame de départ",
        },
        "end_frame": {
            "type": "int",
            "description": "Frame de fin",
        },
        "layer": {
            "type": "int",
            "description": "Calque cible",
        },
        "priority": {
            "type": "int",
            "description": "Priorité de l'action",
        },
        "mode": {
            "type": "str",
            "description": "Mode d'exécution",
            "enum": ["PLAY", "STOP", "LOOP", "PINGPONG"]
        }
    },
    "inputs": ["trigger"]
}
