# sens_actuator.py

sensor = {
    "name": "Actuator",
    "type": "sensor",
    "description": "Détecte l'état d'un Actuator spécifique. Permet de déclencher d'autres logiques si un actuator est actif ou inactif.",
    "parameters": {
        "actuator": "Nom de l'actuator à surveiller (string)",
        "level": "Active le pulse mode en niveau (bool)",
        "tap": "Détecte une transition rapide d'état (bool)",
        "invert": "Inverse la condition (bool)",
        "skip": "Nombre de frames à sauter entre chaque évaluation (int)"
    },
    "outputs": [
        "trigger_on_actuator_state"  # Booléen, True si l'état correspond
    ]
}
