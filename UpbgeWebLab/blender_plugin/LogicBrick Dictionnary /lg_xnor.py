# lg_xnor.py

# Logic Gate: XNOR (Exclusive-NOR)
# Prefix: lg_

gate = {
    "name": "XnorController",
    "type": "logic_gate",
    "description": "Retourne vrai si un nombre pair d'entrées est vrai (inverse du XOR).",
    "inputs": [
        "input_1",  # Première entrée booléenne
        "input_2",  # Deuxième entrée booléenne
        "..."      # Pour prise en charge de plusieurs entrées
    ],
    "outputs": [
        "result"  # Résultat booléen de l'opération XNOR
    ]
}
