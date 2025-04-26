from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

VALID_BADGE_LEVELS = ['1', '2', '3', '4']
VALID_BRANCHES = ['Orthodoxe', 'Catholique', 'Protestant']
VALID_PARISHES = [
    "01 - Ain", "02 - Aisne", "03 - Allier", "04 - Alpes-de-Haute-Provence", "05 - Hautes-Alpes",
    "06 - Alpes-Maritimes", "07 - Ardèche", "08 - Ardennes", "09 - Ariège", "10 - Aube",
    "11 - Aude", "12 - Aveyron", "13 - Bouches-du-Rhône", "14 - Calvados", "15 - Cantal",
    "16 - Charente", "17 - Charente-Maritime", "18 - Cher", "19 - Corrèze", "2A - Corse-du-Sud",
    "2B - Haute-Corse", "21 - Côte-d'Or", "22 - Côtes-d'Armor", "23 - Creuse", "24 - Dordogne",
    "25 - Doubs", "26 - Drôme", "27 - Eure", "28 - Eure-et-Loir", "29 - Finistère", "30 - Gard",
    "31 - Haute-Garonne", "32 - Gers", "33 - Gironde", "34 - Hérault", "35 - Ille-et-Vilaine",
    "36 - Indre", "37 - Indre-et-Loire", "38 - Isère", "39 - Jura", "40 - Landes",
    "41 - Loir-et-Cher", "42 - Loire", "43 - Haute-Loire", "44 - Loire-Atlantique",
    "45 - Loiret", "46 - Lot", "47 - Lot-et-Garonne", "48 - Lozère", "49 - Maine-et-Loire",
    "50 - Manche", "51 - Marne", "52 - Haute-Marne", "53 - Mayenne", "54 - Meurthe-et-Moselle",
    "55 - Meuse", "56 - Morbihan", "57 - Moselle", "58 - Nièvre", "59 - Nord", "60 - Oise",
    "61 - Orne", "62 - Pas-de-Calais", "63 - Puy-de-Dôme", "64 - Pyrénées-Atlantiques",
    "65 - Hautes-Pyrénées", "66 - Pyrénées-Orientales", "67 - Bas-Rhin", "68 - Haut-Rhin",
    "69 - Rhône", "70 - Haute-Saône", "71 - Saône-et-Loire", "72 - Sarthe", "73 - Savoie",
    "74 - Haute-Savoie", "75 - Paris", "76 - Seine-Maritime", "77 - Seine-et-Marne",
    "78 - Yvelines", "79 - Deux-Sèvres", "80 - Somme", "81 - Tarn", "82 - Tarn-et-Garonne",
    "83 - Var", "84 - Vaucluse", "85 - Vendée", "86 - Vienne", "87 - Haute-Vienne",
    "88 - Vosges", "89 - Yonne", "90 - Territoire de Belfort", "91 - Essonne",
    "92 - Hauts-de-Seine", "93 - Seine-Saint-Denis", "94 - Val-de-Marne",
    "95 - Val-d'Oise", "971 - Guadeloupe", "972 - Martinique", "973 - Guyane",
    "974 - La Réunion", "976 - Mayotte"
]

def register_user(username, email, password, badge_level, branch, parish, role=None, tiktok_handle=None, discord_id=None):
    print(f"[REGISTER] Mot de passe brut : {password}")
    hashed = generate_password_hash(password)
    print(f"[REGISTER] Hash généré : {hashed}")
    user = User(
        username=username,
        email=email,
        password_hash=hashed,
        role=role if role is not None else "",
        badge_level=badge_level,
        branch=branch,
        parish=parish,
        tiktok_handle=tiktok_handle,
        discord_id=discord_id,
    )
    db.session.add(user)
    db.session.commit()
    return user





def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    print(f"[LOGIN] Email cherché : {email}")
    print(f"[LOGIN] Password entré : {password}")
    print(f"[LOGIN] Password hash en base : {user.password_hash}")
    if user:
        result = check_password_hash(user.password_hash, password)
        print(f"[LOGIN] Résultat check_password_hash : {result}")
        return user if result else None
    return None


def validate_registration_data(data):
    required_fields = ['username', 'email', 'password', 'badge_level', 'branch', 'parish']  # role enlevé ici
    for field in required_fields:
        if field not in data:
            return f"'{field}' is required"

    if data['badge_level'] not in VALID_BADGE_LEVELS:
        return "Badge level invalide. Doit être 1, 2, 3 ou 4."

    if data['branch'] not in VALID_BRANCHES:
        return "Branche invalide. Doit être Orthodoxe, Catholique ou Protestant."

    if data['parish'] not in VALID_PARISHES:
        return "Département invalide. Merci de choisir un département français."

    return None