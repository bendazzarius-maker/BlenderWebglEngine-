# act_message.py

actuator = {
    "name": "MessageActuator",
    "type": "actuator",
    "description": "Envoie un message à d'autres objets.",
    "parameters": {
        "to": {
            "type": "str",
            "description": "Nom de l'objet destinataire (vide pour diffuser)",
        },
        "subject": {
            "type": "str",
            "description": "Sujet du message",
        },
        "body": {
            "type": "str",
            "description": "Contenu du message ou nom de propriété (selon body_type)",
        },
        "body_type": {
            "type": "str",
            "description": "Type de corps du message",
            "enum": [
                "STRING",
                "PROPERTY"
            ]
        }
    },
    "inputs": ["trigger"]
}
