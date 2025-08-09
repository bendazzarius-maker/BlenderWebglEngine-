# sens_radar.py

sensor = {
    "name": "RadarSensor",
    "type": "sensor",
    "description": "Détecte les objets ou propriétés dans un cône défini autour de l’objet selon un axe, un angle et une distance.",
    "parameters": {
        "skip": {
            "type": "int",
            "default": 0,
            "description": "Nombre de frames ignorées entre chaque évaluation."
        },
        "level": {
            "type": "bool",
            "default": false,
            "description": "Pulse True: active la sortie tant que la condition est vraie."
        },
        "tap": {
            "type": "bool",
            "default": false,
            "description": "Pulse uniquement sur changement d’état (True ou False)."
        },
        "invert": {
            "type": "bool",
            "default": false,
            "description": "Inverse la logique de sortie."
        },
        "property": {
            "type": "str",
            "default": "",
            "description": "Nom de la propriété à rechercher dans l’objet détecté."
        },
        "axis": {
            "type": "str",
            "default": "+X",
            "description": "Axe de projection du radar (+X, -X, +Y, -Y, +Z, -Z)."
        },
        "angle": {
            "type": "float",
            "default": 0.0,
            "description": "Angle d’ouverture du cône de détection (en degrés)."
        },
        "distance": {
            "type": "float",
            "default": 0.0,
            "description": "Distance maximale de détection."
        }
    },
    "outputs": [
        "onRadar"
    ]
}
