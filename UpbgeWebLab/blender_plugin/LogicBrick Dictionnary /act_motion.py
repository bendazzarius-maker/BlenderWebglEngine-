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
