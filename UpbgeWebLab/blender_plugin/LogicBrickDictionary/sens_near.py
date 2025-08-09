# sens_near.py

sensor = {
    "name": "NearSensor",
    "type": "sensor",
    "description": "Détecte la proximité d'un objet ou d'une propriété spécifiée lorsque la distance est inférieure au seuil.",
    "parameters": {
        "skip": "Nombre de frames ignorées entre chaque évaluation (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)",
        "property": "Nom de la propriété à détecter sur l'objet cible (str)",
        "distance": "Distance minimale pour déclencher la détection (float)",
        "reset_distance": "Distance à partir de laquelle réinitialiser le compteur (float)"
    },
    "outputs": [
        "onNear"
    ]
}
