# act_visibility.py

actuator = {
    "name": "VisibilityActuator",
    "type": "actuator",
    "description": "Affiche ou cache un objet et ses enfants.",
    "parameters": {
        "visible": {
            "type": "bool",
            "description": "Rend l'objet visible ou invisible",
        },
        "occlusion": {
            "type": "bool",
            "description": "Active l'occlusion de l'objet",
        },
        "children": {
            "type": "bool",
            "description": "Applique aussi aux enfants",
        }
    },
    "inputs": ["trigger"]
}
