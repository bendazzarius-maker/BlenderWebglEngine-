# lg_pythoncontroller.py

controller = {
    "name": "PythonController",
    "type": "controller",
    "description": "Exécute un script Python personnalisé attaché à l'objet.",
    "parameters": {
        "script_name": {
            "type": "str",
            "default": "",
            "description": "Nom du bloc de texte ou du script Python à exécuter."
        }
    },
    "inputs": [
        "trigger"
    ],
    "outputs": [
        "trigger"
    ]
}
