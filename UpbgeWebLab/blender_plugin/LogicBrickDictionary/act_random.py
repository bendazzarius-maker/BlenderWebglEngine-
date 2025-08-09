# act_random.py

actuator = {
    "name": "RandomActuator",
    "type": "actuator",
    "description": "Assigne une valeur aléatoire à une propriété.",
    "parameters": {
        "property": {
            "type": "str",
            "description": "Nom de la propriété ciblée",
        },
        "distribution": {
            "type": "str",
            "description": "Type de distribution aléatoire",
            "enum": ["BOOL", "INT", "FLOAT"]
        },
        "min": {
            "type": "float",
            "description": "Valeur minimale",
        },
        "max": {
            "type": "float",
            "description": "Valeur maximale",
        },
        "seed": {
            "type": "int",
            "description": "Graine de génération",
        }
    },
    "inputs": ["trigger"]
}
