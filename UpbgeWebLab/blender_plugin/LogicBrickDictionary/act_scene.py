# act_scene.py

actuator = {
    "name": "SceneActuator",
    "type": "actuator",
    "description": "Gestion de la scène (ajout, suppression, suspension...).",
    "parameters": {
        "mode": {
            "type": "str",
            "description": "Action sur la scène",
            "enum": [
                "SET_SCENE",
                "ADD_SCENE",
                "REMOVE_SCENE",
                "SUSPEND_SCENE",
                "RESUME_SCENE",
                "REPLACE_SCENE",
                "SET_CAMERA"
            ]
        },
        "scene": {
            "type": "str",
            "description": "Nom de la scène cible",
        },
        "camera": {
            "type": "str",
            "description": "Nom de la caméra pour SET_CAMERA",
        },
        "use_logic": {
            "type": "bool",
            "description": "Inclure la logique lors de l'ajout de scène",
        }
    },
    "inputs": ["trigger"]
}
