# sens_delay.py

sensor = {
    "name": "Delay",
    "type": "sensor",
    "description": "Déclenche un signal après un certain délai et/ou pendant une durée définie.",
    "parameters": {
        "delay": "Nombre de frames avant de déclencher le signal (int)",
        "duration": "Nombre de frames pendant lesquelles le signal reste actif après le délai (int)",
        "repeat": "Si activé, répète le cycle Delay + Duration en boucle (bool)",
        "level": "Pulse mode - active un signal permanent si condition vraie (bool)",
        "tap": "Détecte uniquement une transition (montée ou descente) de signal (bool)",
        "invert": "Inverse la sortie logique (bool)",
        "skip": "Nombre de frames à ignorer entre deux évaluations (int)"
    },
    "outputs": [
        "onDelay"  # Signal émis après le délai et pendant la durée spécifiée
    ]
}
