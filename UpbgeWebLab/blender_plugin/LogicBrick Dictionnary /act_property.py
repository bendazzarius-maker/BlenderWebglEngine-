# act_property.py

actuator = {
    "name": "PropertyActuator",
    "type": "actuator",
    "description": "Modifie une propriété d'objet.",
    "parameters": {
        "property": {
            "type": "str",
            "description": "Nom de la propriété ciblée",
        },
        "mode": {
            "type": "str",
            "description": "Type de modification",
            "enum": ["ASSIGN", "ADD", "COPY", "TOGGLE"]
        },
        "value": {
            "type": "str",
            "description": "Valeur ou nom de propriété source selon le mode",
        }
    },
    "inputs": ["trigger"]
}
