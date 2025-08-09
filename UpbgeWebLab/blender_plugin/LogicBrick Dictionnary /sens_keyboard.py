# sens_keyboard.py

sensor = {
    "name": "Keyboard",
    "type": "sensor",
    "description": "Détecte lorsqu'une touche du clavier est pressée, maintenue ou relâchée.",
    "parameters": {
        "key": "Touche détectée (str, ex: 'W', 'Enter', 'Space')",
        "first_modifier": "Modificateur primaire (str, ex: 'Shift', 'Ctrl', 'Alt')",
        "second_modifier": "Modificateur secondaire (str)",
        "log_toggle": "Active le mode de bascule avec cette touche (bool)",
        "target": "Nom de la propriété ou champ cible (str, optionnel)",
        "skip": "Nombre de frames ignorées entre deux évaluations (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)"
    },
    "outputs": [
        "onKeyPress"  # Déclenchement si la combinaison de touches est activée
    ]
}
