# Fichier : sens_always.py
sensor_brick = {
    "name": "Always",
    "type": "sensor",
    "description": "Le capteur Always s'active à chaque frame ou selon les pulses.",
    "parameters": {
        "pulse_true_level": {
            "type": "bool",
            "default": False,
            "description": "Active le capteur à chaque frame tant qu'il est vrai."
        },
        "pulse_false_level": {
            "type": "bool",
            "default": False,
            "description": "Active le capteur à chaque frame tant qu'il est faux."
        },
        "invert": {
            "type": "bool",
            "default": False,
            "description": "Inverse la sortie du capteur."
        }
    },
    "outputs": [
        "trigger"
    ]
}