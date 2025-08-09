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


LOGIC_BRICK_SPEC = {
    "id": "sensor.keyboard",
    "label": "Keyboard Sensor",
    "category": "sensor",
    "version": "1.0",
    "sockets": {
        "inputs": [
            {"name": "Key", "id": "in_key", "type": "string", "default": ""},
            {
                "name": "First Modifier",
                "id": "in_first_modifier",
                "type": "string",
                "default": "",
            },
            {
                "name": "Second Modifier",
                "id": "in_second_modifier",
                "type": "string",
                "default": "",
            },
        ],
        "outputs": [
            {"name": "Pressed", "id": "out_pressed", "type": "bool", "default": False}
        ],
    },
    "properties": [],
    "codegen": {
        "kind": "template",
        "template": "input.isKeyDown({key})",
        "emits": ["out_pressed"],
    },
}


def serialize_instance(instance: dict) -> dict:
    """Serialize a keyboard sensor instance."""

    inputs = {
        "key": instance.get("key", LOGIC_BRICK_SPEC["sockets"]["inputs"][0]["default"]),
        "first_modifier": instance.get("first_modifier", ""),
        "second_modifier": instance.get("second_modifier", ""),
    }
    return {
        "type": LOGIC_BRICK_SPEC["id"],
        "inputs": inputs,
        "codegen": LOGIC_BRICK_SPEC["codegen"],
        "outputs": [s["id"] for s in LOGIC_BRICK_SPEC["sockets"]["outputs"]],
    }


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""

