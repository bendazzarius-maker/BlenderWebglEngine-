# act_action.py

actuator = {
    "name": "ActionActuator",
    "type": "actuator",
    "description": "Joue ou contrôle une action (animation) d’un objet.",
    "parameters": {
        "action": {
            "type": "str",
            "default": "",
            "description": "Nom de l'action ou de l'animation à jouer."
        },
        "start_frame": {
            "type": "int",
            "default": 0,
            "description": "Frame de démarrage de l'action."
        },
        "end_frame": {
            "type": "int",
            "default": 0,
            "description": "Frame de fin de l'action."
        },
        "mode": {
            "type": "str",
            "default": "PLAY",
            "description": "Mode de l'action (PLAY, STOP, FLIPPER, etc.)."
        }
    },
    "inputs": [
        "trigger"
    ]
}
