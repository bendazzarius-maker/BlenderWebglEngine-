# lg_xor.py

controller = {
    "name": "XorController",
    "type": "controller",
    "description": "Retourne vrai si une seule des entrées est vraie.",
    "inputs": {
        "input_1": {
            "type": "bool",
            "description": "Première entrée booléenne"
        },
        "input_2": {
            "type": "bool",
            "description": "Deuxième entrée booléenne"
        },
        "input_n": {
            "type": "bool",
            "description": "Entrées booléennes supplémentaires"
        }
    },
    "outputs": [
        "result"
    ]
}
