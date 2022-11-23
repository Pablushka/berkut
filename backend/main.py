from flask import Flask, redirect, render_template, request, url_for, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from markupsafe import escape

from database import db
from models.event import Event

from datetime import datetime


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/db/project.sqlite"

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
    # return the render of the home page in the frotend folder

    return render_template('index.html')
    # return redirect(url_for('frontend', filename='home.html'))


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


@app.route('/events', methods=['POST'])  # type: ignore
def create_event():
    if request.method == 'POST':

        request_data = request.get_json()

        if request_data:
            data = request_data

            new_date = datetime.strptime(data['date'], "%d-%m-%Y")
            title = data['title']
            text = data['text']

            db.session.add(Event(date=new_date, title=title,  text=text))
            db.session.commit()
            return f"Event('{new_date}', '{title}', '{text}')"


@app.route('/byebye')
def good_bye():
    return '<h1>Adios monchito!</h1>'


@app.route('/greet/<int:doc>')
def add_surname(doc):
    return f"<h1>Hola persona con el doc # {escape(doc)}</h1>"


@app.route('/greet/<name>')
def greet_user(name):
    return f"<h1>Hola, {escape(name)}!</h1>"


@app.route('/city', methods=['GET', 'POST'])
def get_city_data():
    if request.method == 'POST':
        name = request.form['name']
        pop = request.form['population']
        return f"<h1>{escape(name)} tiene {escape(pop)} habitantes</h1>"
    else:
        return "<h1>Toma tu data: ......</h1>"


@app.route('/json-example', methods=['POST'])
def json_example():

    data = {'name': '', 'population': ''}

    request_data = request.get_json()

    if request_data:
        data = request_data

    return f"<h1>{escape(data['name'])} tiene {escape(data['population'])} habitantes</h1>"


@app.errorhandler(500)
def server_error_500(e):
    app.logger.error('An error occurred during a request. %s', e)
    return "An internal error occured", 500


@app.errorhandler(404)
def server_error_404(e):
    app.logger.error('Resource does not exists. %s', e)
    return "Resource does not exists", 404


if __name__ == '__main__':
    app.run(debug=True)

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
