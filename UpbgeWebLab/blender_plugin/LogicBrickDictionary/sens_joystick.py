# sens_joystick.py

sensor = {
    "name": "Joystick",
    "type": "sensor",
    "description": "Détecte les événements provenant d'une manette de jeu (axes et boutons).",
    "parameters": {
        "joystick_index": "Index de la manette (int) - généralement 0 pour le premier contrôleur",
        "event_type": "Type d’événement détecté (str): 'Stick Directions', 'Stick Axis', 'Button Pressed', etc.",
        "all_events": "Détecter tous les événements du type sélectionné (bool)",
        "stick": "Joystick utilisé (str): 'Left Stick' ou 'Right Stick'",
        "stick_direction": "Direction détectée (str): 'Up', 'Down', 'Left', 'Right', etc.",
        "threshold": "Seuil de déclenchement pour les mouvements d'axe (int, entre 0 et 32767)",
        "skip": "Nombre de frames ignorées entre deux évaluations (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)"
    },
    "outputs": [
        "onJoystickEvent"  # Déclenchement si la condition de la manette est remplie
    ]
}
