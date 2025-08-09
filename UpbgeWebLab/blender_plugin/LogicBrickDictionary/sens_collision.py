# sens_collision.py

sensor = {
    "name": "Collision",
    "type": "sensor",
    "description": "Détecte une collision entre l'objet courant et d'autres objets avec une propriété donnée.",
    "parameters": {
        "property": "Nom de la propriété à détecter sur l'objet en collision (string, peut être vide pour détecter toute collision)",
        "material": "Matériau à détecter (non exposé dans l'UI par défaut mais accessible via API)",
        "pulse": "Permet d'activer la détection en continu (bool)",
        "use_m_p": "Utilise le mode 'Material/Property' si activé (bool)",
        "level": "Pulse mode - active un signal permanent si condition vraie (bool)",
        "tap": "Détecte uniquement une transition (montée ou descente) de signal (bool)",
        "invert": "Inverse la sortie logique (bool)",
        "skip": "Nombre de frames à ignorer entre deux évaluations (int)"
    },
    "outputs": [
        "onCollision",  # True si une collision est détectée
        "collidingObject"  # Référence à l'objet en collision (si applicable)
    ]
}
