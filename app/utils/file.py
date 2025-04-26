import uuid
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase App (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'your-firebase-bucket.appspot.com'
    })

def upload_file_to_firebase(file, folder="uploads"):
    if not file:
        return None

    bucket = storage.bucket()
    extension = file.filename.split('.')[-1]
    filename = f"{folder}/{uuid.uuid4().hex}.{extension}"

    blob = bucket.blob(filename)
    blob.upload_from_file(file, content_type=file.content_type)
    blob.make_public()

    return blob.public_url
