from flask import request, jsonify
from app import app, db
from app.models import Image
from app.utils import process_image

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    new_image = Image(filename=file.filename, data=file.read())
    db.session.add(new_image)
    db.session.commit()

    processed_image = process_image(new_image.data)
    return jsonify({"filename": new_image.filename, "processed_image": processed_image})
