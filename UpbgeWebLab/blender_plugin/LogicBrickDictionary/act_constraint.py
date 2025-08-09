# act_constraint.py

actuator = {
    "name": "ConstraintActuator",
    "type": "actuator",
    "description": "Applique une contrainte between l’objet et une cible selon différents modes.",
    "parameters": {
        "constraint": {
            "type": "str",
            "description": "Type de contrainte à appliquer",
            "enum": [
                "LOCATION_CONSTRAINT",   # Contrainte de position
                "DISTANCE_CONSTRAINT",   # Contrainte de distance
                "ORIENTATION_CONSTRAINT",# Contrainte d'orientation
                "FORCE_FIELD_CONSTRAINT" # Contrainte de champ de force
            ]
        },
        "limit": {
            "type": "str",
            "description": "Limite appliquée sur l'axe",
            "enum": [
                "NONE",  # Aucune limite
                "LOC_X", # Limite sur X
                "LOC_Y", # Limite sur Y
                "LOC_Z"  # Limite sur Z
            ]
        },
        "min": {
            "type": "float",
            "description": "Valeur minimale de la limite"
        },
        "damping": {
            "type": "float",
            "description": "Coefficient d'amortissement"
        },
        "distance": {
            "type": "float",
            "description": "Distance pour la DistanceConstraint"
        },
        "angle": {
            "type": "float",
            "description": "Angle en degrés pour OrientationConstraint"
        },
        "target": {
            "type": "str",
            "description": "Nom de l’objet cible de la contrainte"
        },
        "use_logic": {
            "type": "bool",
            "description": "Active ou désactive le mode logique"
        }
    },
    "inputs": ["trigger"]
}
