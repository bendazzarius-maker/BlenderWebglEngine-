# act_sound.py

actuator = {
    "name": "SoundActuator",
    "type": "actuator",
    "description": "Joue un fichier audio.",
    "parameters": {
        "sound": {
            "type": "str",
            "description": "Nom du son ou chemin du fichier",
        },
        "mode": {
            "type": "str",
            "description": "Mode de lecture",
            "enum": ["PLAY", "STOP", "LOOP", "PINGPONG", "END"]
        },
        "volume": {
            "type": "float",
            "description": "Volume de lecture",
        },
        "pitch": {
            "type": "float",
            "description": "Hauteur du son",
        }
    },
    "inputs": ["trigger"]
}
