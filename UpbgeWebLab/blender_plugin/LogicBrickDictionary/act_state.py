# act_state.py

actuator = {
    "name": "StateActuator",
    "type": "actuator",
    "description": "Change l'état logique de l'objet.",
    "parameters": {
        "operation": {
            "type": "str",
            "description": "Mode de modification",
            "enum": ["SET", "ADD", "SUB"]
        },
        "mask": {
            "type": "int",
            "description": "Masque d'état à appliquer",
        }
    },
    "inputs": ["trigger"]
}
