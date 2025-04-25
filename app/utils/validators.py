import re
from flask import jsonify

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_required_fields(data, required_fields):
    """
    Vérifie si les champs requis sont présents dans `data`.
    Retourne une réponse JSON d'erreur si manquant, sinon None.
    """
    missing = [field for field in required_fields if field not in data or not data[field]]
    if missing:
        return jsonify({"error": f"Champs manquants : {', '.join(missing)}"}), 400
    return None

def validate_role(role):
    return role in ['admin', 'subadmin', 'user']

def validate_branch(branch):
    return branch in ['orthodoxe', 'catholique', 'pentecotiste']
