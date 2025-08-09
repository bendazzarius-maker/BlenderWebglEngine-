# act_game.py

actuator = {
    "name": "GameActuator",
    "type": "actuator",
    "description": "Contrôle l'exécution du jeu (quitter, redémarrer, charger...).",
    "parameters": {
        "mode": {
            "type": "str",
            "description": "Action à effectuer",
            "enum": [
                "START_GAME",
                "RESTART_GAME",
                "QUIT_GAME",
                "LOAD_GAME",
                "SAVE_GAME",
                "SUSPEND_SCENE",
                "RESUME_SCENE",
                "SUSPEND_PHYSICS",
                "RESUME_PHYSICS",
                "SUSPEND_LOGIC",
                "RESUME_LOGIC"
            ]
        },
        "file_path": {
            "type": "str",
            "description": "Chemin du fichier pour START_GAME/LOAD_GAME/SAVE_GAME",
        },
        "scene_name": {
            "type": "str",
            "description": "Nom de la scène cible pour SUSPEND_SCENE ou RESUME_SCENE",
        }
    },
    "inputs": ["trigger"]
}
