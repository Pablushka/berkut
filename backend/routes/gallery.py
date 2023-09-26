from ..main import app
from models.gallery import Gallery
from models.photo import Photo
import os
from database import db
UPLOAD_FOLDER = '../frontend/public/img/galleries'





@app.route('/gallery/<string:filetype>/<int:gallery_id>/<int:photo_id>/', methods=['DELETE'])
def delete(gallery_id, photo_id, filetype):

    image = Photo.query.get_or_404(photo_id, description="Photo not found")
    gallery_path = os.path.join(UPLOAD_FOLDER, str(gallery_id))
    flyer_path = os.path.join(os.path.join(UPLOAD_FOLDER, image.image))
    photo_path = os.path.join(os.path.join(UPLOAD_FOLDER, str(gallery_id), image.image))

    if filetype == "flyer":
         os.remove(flyer_path)

    else:
        if os.path.isdir(gallery_path):
            if os.path.isfile(photo_path):
                os.remove(photo_path)
            
    db.session.delete(image)
    db.session.commit()
        
    return {'ok': True, 'message': 'File was deleted'}
