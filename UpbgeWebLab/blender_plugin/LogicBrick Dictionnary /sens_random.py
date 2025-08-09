# sens_random.py

sensor = {
    "name": "RandomSensor",
    "type": "sensor",
    "description": "Génère un nombre aléatoire ou change de valeur à chaque évaluation selon le seed.",
    "parameters": {
        "skip": "Nombre de frames ignorées entre chaque évaluation (int)",
        "level": "Pulse sur niveau vrai (bool)",
        "tap": "Pulse uniquement lors du changement de valeur (bool)",
        "invert": "Inverse la logique de sortie (bool)",
        "seed": "Valeur de départ pour l'initialisation du générateur aléatoire (int)"
    },
    "outputs": [
        "onRandom",
        "value"
    ]
}
