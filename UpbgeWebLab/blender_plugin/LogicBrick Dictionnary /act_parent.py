# act_parent.py

actuator = {
    "name": "ParentActuator",
    "type": "actuator",
    "description": "Change ou supprime le parent d'un objet.",
    "parameters": {
        "mode": {
            "type": "str",
            "description": "Opération à réaliser",
            "enum": ["SET", "CLEAR"]
        },
        "parent": {
            "type": "str",
            "description": "Nom de l'objet parent (pour SET)",
        },
        "compound": {
            "type": "bool",
            "description": "Combine la physique avec le parent",
        },
        "ghost": {
            "type": "bool",
            "description": "Retire la collision de l'objet enfant",
        }
    },
    "inputs": ["trigger"]
}
