# sens_ray.py

sensor = {
    "name": "RaySensor",
    "type": "sensor",
    "description": "Envoie un rayon dans une direction pour détecter un objet ou une propriété.",
    "parameters": {
        "skip": "Nombre de frames ignorées entre chaque évaluation (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)",
        "property": "Nom de la propriété à détecter (str)",
        "axis": "Axe du rayon (\"+X\", \"-X\", \"+Y\", \"-Y\", \"+Z\", \"-Z\") (str)",
        "range": "Longueur du rayon (float)",
        "xray": "Mode X-Ray : ignore les intersections avec l'objet de départ (bool)",
        "mask": "Masque de collision : liste de couches ou bitmask indiquant quelles couches tester (list[int] ou int)"
    },
    "outputs": [
        "onRayHit",
        "hitObject",
        "hitPosition"
    ]
}
