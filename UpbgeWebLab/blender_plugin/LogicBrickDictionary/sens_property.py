# sens_property.py

sensor = {
    "name": "PropertySensor",
    "type": "sensor",
    "description": "Déclenche lorsque la valeur d'une propriété spécifiée remplit la condition définie.",
    "parameters": {
        "skip": "Nombre de frames ignorées entre chaque évaluation (int)",
        "level": "Pulse mode actif sur niveau vrai (bool)",
        "tap": "Pulse uniquement sur changement (bool)",
        "invert": "Inverse la logique de sortie (bool)",
        "property_name": "Nom de la propriété à vérifier sur l'objet cible (str)",
        "evaluation": "Type de comparaison à utiliser (str: 'Equal','Not Equal','Less','Less or Equal','Greater','Greater or Equal')",
        "value": "Valeur à comparer (float/int/bool/str)"
    },
    "outputs": [
        "onProperty"
    ]
}
