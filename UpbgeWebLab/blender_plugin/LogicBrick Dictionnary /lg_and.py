# lg_and.py

controller = {
    "name": "AndController",
    "type": "controller",
    "description": "Retourne vrai si toutes les entrées sont vraies.",
    "inputs": {
        "input_1": "Première entrée logique (bool)",
        "input_2": "Deuxième entrée logique (bool)",
        "...": "Autres entrées possibles (bool)"
    },
    "outputs": {
        "result": "Résultat logique (bool)"
    }
}


LOGIC_BRICK_SPEC = {
    "id": "controller.and",
    "label": "AND Controller",
    "category": "controller",
    "version": "1.0",
    "sockets": {
        "inputs": [
            {"name": "Inputs", "id": "in_inputs", "type": "bool", "default": False}
        ],
        "outputs": [
            {"name": "Result", "id": "out_result", "type": "bool", "default": False}
        ],
    },
    "properties": [],
    "codegen": {
        "kind": "template",
        "template": "({exprs})",
        "emits": ["out_result"],
    },
}


def serialize_instance(instance: dict) -> dict:
    """Serialize an AND controller instance."""

    inputs = instance.get("inputs", [])
    return {
        "type": LOGIC_BRICK_SPEC["id"],
        "inputs": {"inputs": inputs},
        "codegen": LOGIC_BRICK_SPEC["codegen"],
        "outputs": [s["id"] for s in LOGIC_BRICK_SPEC["sockets"]["outputs"]],
    }


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""

