# act_edit_object.py

actuator = {
    "name": "EditObjectActuator",
    "type": "actuator",
    "description": "Ajoute, supprime, remplace ou modifie un objet dans la scène selon le mode sélectionné.",
    "parameters": {
        "mode": {
            "type": "str",
            "description": "Mode d'édition de l'objet",
            "enum": [
                "ADD_OBJECT",       # Ajouter un nouvel objet
                "END_OBJECT",       # Terminer (supprimer) un objet
                "REPLACE_MESH",     # Remplacer le maillage d'un objet
                "TRACK_TO",         # Orientation pour pointer vers une cible
                "DYNAMICS"          # Opérations sur la physique/dynamique
            ]
        },
        # Paramètres communs
        "object": {
            "type": "str",
            "description": "Nom de l'objet cible (pour ADD, TRACK_TO, END)",
            "optional": true
        },
        # Paramètres spécifiques à ADD_OBJECT
        "time": {
            "type": "float",
            "description": "Durée de vie de l'objet (ADD_OBJECT)",
            "optional": true
        },
        "linear_velocity": {
            "type": "list",
            "items": { "type": "float" },
            "description": "Vélocité linéaire (x, y, z) appliquée à l'objet ajouté",
            "optional": true
        },
        "angular_velocity": {
            "type": "list",
            "items": { "type": "float" },
            "description": "Vélocité angulaire (x, y, z) appliquée à l'objet ajouté",
            "optional": true
        },
        "full_duplication": {
            "type": "bool",
            "description": "Dupliquer complètement les données de l'objet (ADD_OBJECT)",
            "optional": true
        },
        # Paramètres spécifiques à REPLACE_MESH
        "mesh": {
            "type": "str",
            "description": "Nom du nouveau maillage (REPLACE_MESH)",
            "optional": true
        },
        "mesh_type": {
            "type": "str",
            "description": "Type de maillage à remplacer",
            "enum": ["GFX", "PHYS"],
            "optional": true
        },
        # Paramètres spécifiques à TRACK_TO
        "up_axis": {
            "type": "str",
            "description": "Axe vers le haut du suivi (TRACK_TO)",
            "enum": ["X_AXIS", "Y_AXIS", "Z_AXIS"],
            "optional": true
        },
        "track_axis": {
            "type": "str",
            "description": "Axe qui pointe vers la cible (TRACK_TO)",
            "enum": ["X_AXIS", "Y_AXIS", "Z_AXIS"],
            "optional": true
        },
        # Paramètres spécifiques à DYNAMICS
        "dynamic_operation": {
            "type": "str",
            "description": "Opération dynamique à effectuer",
            "enum": [
                "RESTORE_DYNAMICS",  # Restaurer la dynamique
                "SUSPEND_DYNAMICS",  # Suspendre la dynamique
                "ENABLE_RIGID_BODY", # Activer le corps rigide
                "DISABLE_RIGID_BODY",# Désactiver le corps rigide
                "SET_MASS",          # Définir la masse
                "RESTORE_PHYSICS",   # Restaurer la physique
                "SUSPEND_PHYSICS"    # Suspendre la physique
            ],
            "optional": true
        },
        "mass": {
            "type": "float",
            "description": "Nouvelle masse de l'objet (SET_MASS)",
            "optional": true
        }
    },
    "inputs": ["trigger"]
}
