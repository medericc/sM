import uuid
import datetime
import firebase_admin
from firebase_admin import credentials, storage
from flask import current_app

# Initialiser Firebase si ce n'est pas déjà fait
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")  # fichier JSON de config Firebase
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'your-firebase-bucket.appspot.com'
    })

def upload_file_to_firebase(file, folder="uploads"):
    """
    Upload un fichier à Firebase Storage et retourne l'URL publique.
    """
    if not file:
        return None

    bucket = storage.bucket()
    extension = file.filename.split('.')[-1]
    filename = f"{folder}/{uuid.uuid4().hex}.{extension}"

    blob = bucket.blob(filename)
    blob.upload_from_file(file, content_type=file.content_type)
    blob.make_public()

    return blob.public_url
