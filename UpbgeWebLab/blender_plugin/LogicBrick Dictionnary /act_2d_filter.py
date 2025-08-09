# act_2d_filter.py

actuator = {
    "name": "Filter2DActuator",
    "type": "actuator",
    "description": "Applique un filtre 2D sur le rendu.",
    "parameters": {
        "mode": {
            "type": "str",
            "description": "Type de filtre à appliquer",
            "enum": [
                "CUSTOMFILTER",
                "BLUR",
                "SHARPEN",
                "DESATURATE",
                "INVERT",
                "SEPIA",
                "GAUSSIAN",
                "LAPLACIAN",
                "SOBEL",
                "PREWITT"
            ]
        },
        "pass_number": {
            "type": "int",
            "description": "Indice du filtre (pour l'ordre de traitement)",
        },
        "shader_text": {
            "type": "str",
            "description": "Nom du texte pour un filtre personnalisé",
        }
    },
    "inputs": [
        "trigger"
    ]
}
