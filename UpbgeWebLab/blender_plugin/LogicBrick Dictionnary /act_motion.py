# act_motion.py

actuator = {
    "name": "MotionActuator",
    "type": "actuator",
    "description": "Applique une transformation ou une vitesse à l'objet.",
    "parameters": {
        "mode": {
            "type": "str",
            "description": "Mode de déplacement",
            "enum": ["SIMPLE", "SERVO"]
        },
        "dloc": {
            "type": "vec3",
            "description": "Déplacement local",
        },
        "drot": {
            "type": "vec3",
            "description": "Rotation locale",
        },
        "lin_velocity": {
            "type": "vec3",
            "description": "Vitesse linéaire",
        },
        "ang_velocity": {
            "type": "vec3",
            "description": "Vitesse angulaire",
        },
        "use_local": {
            "type": "bool",
            "description": "Interprète les valeurs en coordonnées locales",
        }
    },
    "inputs": ["trigger"]
}


LOGIC_BRICK_SPEC = {
    "id": "actuator.motion",
    "label": "Motion Actuator",
    "category": "actuator",
    "version": "1.0",
    "sockets": {
        "inputs": [
            {"name": "Trigger", "id": "in_trigger", "type": "bool", "default": False},
            {
                "name": "Linear Velocity",
                "id": "in_lin_velocity",
                "type": "vector",
                "default": [0.0, 0.0, 0.0],
            },
            {
                "name": "Angular Velocity",
                "id": "in_ang_velocity",
                "type": "vector",
                "default": [0.0, 0.0, 0.0],
            },
            {
                "name": "Use Local",
                "id": "in_use_local",
                "type": "bool",
                "default": False,
            },
        ],
        "outputs": [],
    },
    "properties": [],
    "codegen": {
        "kind": "template",
        "template": "if ({trigger}) applyMotion({lin_velocity}, {ang_velocity}, {use_local});",
        "emits": [],
    },
}


def serialize_instance(instance: dict) -> dict:
    """Serialize a motion actuator instance."""

    inputs = {
        "trigger": instance.get("trigger", False),
        "lin_velocity": instance.get("lin_velocity", [0.0, 0.0, 0.0]),
        "ang_velocity": instance.get("ang_velocity", [0.0, 0.0, 0.0]),
        "use_local": instance.get("use_local", False),
    }
    return {
        "type": LOGIC_BRICK_SPEC["id"],
        "inputs": inputs,
        "codegen": LOGIC_BRICK_SPEC["codegen"],
        "outputs": [],
    }


def register() -> None:
    """Placeholder register to follow block order."""


def unregister() -> None:
    """Placeholder unregister to follow block order."""

