# lg_expression.py

controller = {
    "name": "ExpressionController",
    "type": "controller",
    "description": "Évalue une expression Python personnalisée basée sur les entrées connectées et déclenche une sortie si l'expression est vraie.",
    "parameters": {
        "expression": "Expression Python ou logique à évaluer utilisant les variables d'entrée (str)"
    },
    "inputs": {
        "inputs": "Liste des entrées booléennes utilisées dans l'expression (list of bool)"
    },
    "outputs": [
        "result"
    ]
}
