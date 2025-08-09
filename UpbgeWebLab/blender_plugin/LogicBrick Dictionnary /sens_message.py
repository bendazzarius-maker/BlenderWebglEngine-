# sens_message.py

sensor = {
    "name": "Message",
    "type": "sensor",
    "description": "Détecte la réception d’un message envoyé via un actuator Message.",
    "parameters": {
        "subject": "Filtrage du message par sujet (string, vide = accepte tout)",
        "skip": "Nombre de frames ignorées entre deux évaluations (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)"
    },
    "outputs": [
        "onMessage"  # Déclenche si un message reçu correspond au sujet spécifié
    ]
}
