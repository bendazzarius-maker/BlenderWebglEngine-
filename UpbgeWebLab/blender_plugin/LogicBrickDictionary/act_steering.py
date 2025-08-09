# act_steering.py

actuator = {
    "name": "SteeringActuator",
    "type": "actuator",
    "description": "Déplace un objet vers une cible en utilisant le pathfinding.",
    "parameters": {
        "target": {
            "type": "str",
            "description": "Nom de l'objet cible",
        },
        "navmesh": {
            "type": "str",
            "description": "Nom de l'objet navmesh",
        },
        "behavior": {
            "type": "str",
            "description": "Comportement de steering",
            "enum": ["SEEK", "FLEE", "PATHFOLLOW", "PURSUIT", "EVASION"]
        },
        "distance": {
            "type": "float",
            "description": "Distance de freinage",
        },
        "speed": {
            "type": "float",
            "description": "Vitesse maximale",
        },
        "turn_speed": {
            "type": "float",
            "description": "Vitesse de rotation",
        },
        "acceleration": {
            "type": "float",
            "description": "Accélération maximale",
        },
        "enable_visualization": {
            "type": "bool",
            "description": "Active la visualisation du chemin",
        }
    },
    "inputs": ["trigger"]
}
