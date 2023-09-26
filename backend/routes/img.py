from ..main import app
from models.gallery import Gallery
from models.photo import Photo
from werkzeug.utils import secure_filename
import os
from database import db
from flask import request


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = '../frontend/public/img/galleries'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Chequea que el filename tenga un punto. 
# Luego divide el filename por el punto en dos partes
# la segunda parte del array que devuleve es la extension
# cehquea que esa extension este en ALLOW_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload/<string:filetype>/<int:gallery_id>', methods=['POST'])
def upload(filetype, gallery_id):
    if 'file' not in request.files:
        return {'ok': False, 'message': 'File not received'}

    file = request.files['file']
    
    if file.filename == '':
        return {'ok': False, 'message': 'File without name'}

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if filetype == "flyer":
            filename = str(gallery_id) + "." + filename.split(".")[-1]
            file.save(os.path.join(UPLOAD_FOLDER, filename))


            gallery = Gallery.query.get_or_404(gallery_id, description="Gallery not found")
            gallery.flyer = filename
            
            db.session.commit()


        else:
            gallery_folder = str(gallery_id)
            gallery_path = os.path.join(UPLOAD_FOLDER, gallery_folder)
            if not os.path.exists(gallery_path):
                os.makedirs(gallery_path)
            file.save(os.path.join(UPLOAD_FOLDER, gallery_folder, filename))

        photo = Photo(image = filename, gallery_id = gallery_id, type = filetype)
        db.session.add(photo)
        db.session.commit()

        return {'ok': True, 'message': 'File uploaded'}
    
    return {'ok': False, 'message': 'File is invalid'}
