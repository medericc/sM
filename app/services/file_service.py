from flask import jsonify
from .firebase_service import upload_file_to_firebase
from .file_db_service import save_file

def upload_file(files, user_id):
    if 'file' not in files:
        return jsonify({"error": "No file part in the request"}), 400

    file = files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Upload to Firebase
    public_url = upload_file_to_firebase(file)
    if not public_url:
        return jsonify({"error": "File upload failed"}), 500

    # Save to DB
    saved_file = save_file(user_id, public_url)

    return jsonify({
        "id": saved_file.id,
        "url": saved_file.url
    }), 201
