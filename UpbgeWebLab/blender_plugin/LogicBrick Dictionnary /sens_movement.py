# sens_movement.py

sensor = {
    "name": "MovementSensor",
    "type": "sensor",
    "description": "Détecte si l’objet a bougé d’une certaine distance entre deux évaluations.",
    "parameters": {
        "skip": "Nombre de frames ignorées entre deux évaluations (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)",
        "distance": "Distance minimale de déplacement avant déclenchement (float)",
        "reset_distance": "Distance à partir de laquelle réinitialiser le compteur (float)"
    },
    "outputs": [
        "onMovement"
    ]
}
