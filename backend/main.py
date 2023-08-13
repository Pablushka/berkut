from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
from flask_cors import CORS
from flask_migrate import Migrate
from markupsafe import escape
from config import settings
from database import db
from models.event import Event
from models.user import User
from models.gallery import Gallery
from models.photo import Photo
from werkzeug.utils import secure_filename
from sqlalchemy import select
import os
import pyotp
from qr import new_qr_code
from mails import send_registration_email
from datetime import datetime, timedelta
import pyotp
from mails import send_registration_email
from qr import new_qr_code


# Lista de tipos de imágenes permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# La carpeta que tiene las fotos
UPLOAD_FOLDER = '../frontend/public/img/galleries'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Chequea que el filename tenga un punto. 
# Luego divide el filename por el punto en dos partes
# la segunda parte del array que devuleve es la extension
# cehquea que esa extension este en ALLOW_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


attempts = {}

app = Flask(__name__)

app.config["SECRET_KEY"] = settings["FLASK_SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/project.sqlite"
app.config["SESSION_TYPE"] = 'sqlalchemy'

cors = CORS(app, resources={r"/*": {"origins": "*"}},
            supports_credentials=True)

db.init_app(app)

# Configuro la session para que use la base de datos
app.config['SESSION_SQLALCHEMY'] = db
# Creo una server side session
ss_session = Session(app)

# render_as_batch=True is needed for SQLite support
migrate = Migrate(app, db, render_as_batch=True)


def login_attemp (email:str): 
    if email in attempts:
        attempts [email]["attempts"] +=1
    else:
        attempts [email] = {"attempts": 1, "block_until": None}

def is_not_block (email:str):
    if not email in attempts:
        return True
    
    # checar que si los intentos >=3 y no tiene fecha de vencimiento
    # hay que devolver false
    if attempts[email]["attempts"] >= 3 and attempts[email]["block_until"] is None:
        attempts[email]["block_until"] = datetime.now() + timedelta(minutes = 10)
        return False
    
    # si el usuario esta bloqueado y ademas esta dentro 
    # de fecha de vencimiento hay que devolver false
    if not attempts[email]["block_until"] is None:
       if attempts[email]["block_until"] >= datetime.now():
           return False
       
    # si pasa la fecha de vencimiento
    # hay que devolver true
    if not attempts[email]["block_until"] is None:
        if attempts[email]["block_until"] <= datetime.now():
            attempts[email]["attempts"] = 0
            attempts[email]["block_until"] = None
            return True
        
    return True
       
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
            filename = str(gallery_id) + "." + filename.split(".")[1]
            file.save(os.path.join(UPLOAD_FOLDER, filename))
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


    
@app.route('/')
def index():
    # return the render of the home page in the frotend folder

    return render_template('index.html')
    # return redirect(url_for('frontend', filename='home.html'))


@app.route('/login', methods=['POST'])  # type: ignore
def login():
    # get the json from the request
    data = request.get_json()

    # if the request has data (is not None), create a new user
    if data:
        email = data['email']
        password = data['password']

        # buscar el usuario en la base de datos
        # checquear que su password es correcta
        # si es correcta, darle acceso a la app


@app.route('/users', methods=['GET'])  # type: ignore
def getUsers():
    # get all users ordered by name
    users = User.query.order_by(User.name).all()

    return jsonify([u.to_dict() for u in users])


@app.route('/users', methods=['POST', 'PATCH'])  # type: ignore
def create_or_update_user():
    # get the json from the request
    data = request.get_json()

    if request.method == 'POST':
        # reemplazar por hashlib.sha256('SALTA'.encode('utf-8') + 'passwords'.encode('utf-8')).hexdigest()
        # hash = hashlib.sha256()

        # if the request has data (is not None), create a new user
        if data:

            if User.query.filter_by(email=data['email']).first():
                return {"ok": False, "message": "email already exists"}

            token = pyotp.random_base32()

            name = data['name']
            email = data['email']

            # hash.update(data['password'].encode('utf-8'))
            # password = hash.hexdigest()

            # datetime.strptime(data['last_login'], "%d-%m-%Y")
            last_login = datetime.now()
            is_active = False
            is_admin = False

            user = User(name=name, email=email, token=token,
                        last_login=last_login, is_active=is_active, is_admin=is_admin)

            db.session.add(user)
            db.session.commit()

            # genera codigo qr
            totp_uri = pyotp.totp.TOTP(token, interval=45).provisioning_uri(
                name=email, issuer_name="Berkut")

            qr = new_qr_code(totp_uri)

            # Enviar email al usuario con el token y las instrucciones para activar su cuenta

            if send_registration_email(email, name, qr, token, user.id):
                return {"ok": True, "message": "email sent", "user": user.to_dict()}
            else:
                return {"ok": False, "message": "email not sent"}

    if request.method == 'PATCH':

        if data:
            id = data['id']
            is_admin = (data['is_admin'] == 'true')
            is_active = (data['is_active'] == 'true')
            level = data['level']

            # email = data['email']

            user = User.query.get_or_404(id, description="User not found")

            user.is_admin = is_admin
            user.is_active = is_active
            user.level = level

            # user.name = name
            # user.email = email

            db.session.commit()
            # return event as json
            return jsonify(user.to_dict())


# type: ignore
@app.route('/users/verify', methods=['POST'])
def verify_user_token():

    # if "user" in session:
    #     print("Session ->", session.get("user"))
    # else:
    #     print("Session ->", "No hay session")

    # get the json from the request
    data = request.get_json()
    if is_not_block (data['email']) == False:
        return {"ok": False, "message": "muchos intentos, usuario bloqueado por 10 min"}


    # buscar el usuario con ese email en la base de datos
    user = User.query.filter_by(email=data['email']).first()

    if user:
        # checkear que su token es correcto
        totp = pyotp.TOTP(user.token)
        new_acces_code = totp.now()  # => '492039'

        is_valid = int(data['access_code']) == int(new_acces_code)

        if is_valid:
            session["user"] = user.to_dict()

            user.is_active = True
            db.session.commit()

            return {"ok": True, "message": "welcome", 'user': {"id": user.id, "name": user.name}}
        else:
            # si no es correcto, emitimos un mensaje de error
            login_attemp (data['email'])
            return {"ok": False, "message": "invalid access code"}
    
    login_attemp (data['email'])
    return {"ok": False, "message": "user not found"}


@app.route('/users/<int:id>', methods=['DELETE'])  # type: ignore
def delete_user(id):
    # TODO: averiguar porque el mensaje de descripcion no se muestra
    user = User.query.get_or_404(id, description="User not found")

    # borrado fisico
    # db.session.delete(user)
    # db.session.commit()

    # borrado logico
    user.is_active = False
    db.session.commit()

    return jsonify(user.to_dict())


@app.route('/users/<int:id>', methods=['PATCH'])  # type: ignore
def undelete_user(id):
    # TODO: averiguar porque el mensaje de descripcion no se muestra
    user = User.query.get_or_404(id, description="User not found")

    # borrado fisico
    # db.session.delete(user)
    # db.session.commit()

    # borrado logico
    user.is_active = True
    db.session.commit()

    return jsonify(user.to_dict())


@app.route('/users/<int:id>', methods=['GET'])  # type: ignore
def get_user(id):
    user = User.query.get_or_404(id, description="User not found")

    return jsonify(user.to_dict())


@app.route('/events/<string:edate>/<string:title>/<string:text>')
def eventsByGet(edate, title, text):

    new_date = datetime.strptime(edate, "%d-%m-%Y")

    db.session.add(Event(date=new_date, title=title,  text=text))
    db.session.commit()
    return f"Event('{edate}', '{title}', '{text}')"


@app.route('/events', methods=['GET'])  # type: ignore
def getEvents():
    # event = db.get_or_404(Event, 1, description="Event not found")

    # get all events ordered by date
    events = Event.query.order_by(Event.date).all()

    return jsonify([e.to_dict() for e in events])


@app.route('/events/<int:id>', methods=['DELETE'])  # type: ignore
def deleteEvent(id):
    # TODO: averiguar porque el mensaje de descripcion no se muestra
    event = Event.query.get_or_404(id, description="Event not found")

    db.session.delete(event)
    db.session.commit()

    return jsonify(event.to_dict())


@app.route('/events', methods=['POST', 'PATCH'])  # type: ignore
def create_or_update_event():

    # si el request es un post, se crea un nuevo evento
    if request.method == 'POST':

        # se obtiene el json del request
        data = request.get_json()

        # si el request tiene data (no es None), se crea un nuevo evento
        if data:

            new_date = datetime.strptime(data['date'], "%d-%m-%Y")
            title = data['title']
            text = data['text']

            event = Event(date=new_date, title=title,  text=text)
            db.session.add(event)
            db.session.commit()

            return jsonify(event.to_dict())

    if request.method == 'PATCH':

        # se obtiene el json del request
        data = request.get_json()

        # si el request tiene data (no es None), se crea un nuevo evento
        if data:

            id = data['id']
            new_date = datetime.strptime(data['date'], "%d-%m-%Y")
            title = data['title']
            text = data['text']

            event = Event.query.get_or_404(id, description="Event not found")

            event.date = new_date
            event.title = title
            event.text = text

            db.session.commit()
            # return event as json
            return jsonify(event.to_dict())
        

        
@app.route('/gallery', methods=['POST', 'PATCH'])
def create_or_edit_gallery():
    if request.method == 'POST':

        data = request.get_json()

        if data:
            flyer = data['flyer']
            title = data['title']
            date = data['date']
            datetime_object = datetime.strptime(date, '%Y-%m-%d')
        
            gallery = Gallery(title=title,  flyer=flyer, date=datetime_object)
            db.session.add(gallery)
            db.session.commit()

            return jsonify(gallery.to_dict())
        
    if request.method == 'PATCH':

        data = request.get_json()

        if data:

            id = data['id']
            flyer = data['flyer']
            title = data['title']
            date = data['date']
            datetime_object = datetime.strptime(date, '%Y-%m-%d')

            gallery = Gallery.query.get_or_404(id, description="Gallery not found")

            gallery.flyer = flyer
            gallery.title = title
            gallery.date = datetime_object

            db.session.commit()

            return jsonify(gallery.to_dict())
        
# Elimina la galeria de la base de datos por ID
@app.route('/gallery/<int:id>', methods=['DELETE'])
def deleteGallery(id):

    gallery = Gallery.query.get_or_404(id, description="Gallery not found")

    db.session.delete(gallery)
    db.session.commit()

    return jsonify(gallery.to_dict())

        
@app.route('/photo', methods=['POST'])
def create_photo():
    data = request.get_json()
    
    if data:
        # Obtener el nombre de la imagen y la carpeta
        image_name = data["image"]
        gallery_id = data["gallery_id"]

        # Verificar si la imagen existe en la carpeta
        save_path = os.path.join(UPLOAD_FOLDER, str(gallery_id))
        image_path = os.path.join(save_path, image_name)
        if os.path.exists(image_path):
            return {"ok": False, "message": "Image exist in the folder"}

        # Verificar si la imagen existe en la base de datos
        existing_photo = Photo.query.filter_by(image=image_name).first()
        if existing_photo:
            return {"ok": False, "message": "Image exist in the database"}
        else:
            photo = Photo(image=data["image"],  gallery_id=data["gallery_id"])
            db.session.add(photo)
            db.session.commit()

        return jsonify(photo.to_dict())
    
    return {"ok": False, "message": "No photo"}
        
@app.route('/galleries', methods=['GET'])
def get_galleries():
    galleries = Gallery.query.order_by(Gallery.date).all()
    return jsonify([gallery.to_dict() for gallery in galleries])
    #return jsonify(galleries)


@app.route('/gallery/<int:gallery_id>/<string:type>')
def get_photos(gallery_id, type):
    gallery = Gallery.query.get_or_404(gallery_id)
    photos = [photo.to_dict() for photo in gallery.photos if photo.type == type]
    return jsonify(photos)
    

@app.errorhandler(500)
def server_error_500(e):
    app.logger.error('An error occurred during a request. %s', e)
    return "An internal error occured", 500


@app.errorhandler(404)
def server_error_404(e):
    app.logger.error('Resource does not exists. %s', e)
    return "Resource does not exists", 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


# Ejemplos de rutas
# /user/create
# /user/delete
# /user/update
# /user/delivery

# /products/create
# /products/delete
# /products/update
# /products/customer_service/<product_id>

# NAVEGADOR --> REQUEST --> SERVER (FLASK)
# SERVER --> RESPONSE --> NAVEGADOR

# URL
# PROTOCOL + HOST + PORT + ROUTE + QUERY_STRING
# http://localhost:5000/....
