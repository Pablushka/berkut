from crypt import methods
from flask import Flask, url_for, request, redirect, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    # return the render of the home page in the frotend folder

    return render_template('home.html')
    # return redirect(url_for('frontend', filename='home.html'))


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


@app.route('/json-example', method=['POST'])
def json_example():

    data = request.get_json()
    return f"<h1>{escape(data['name'])} tiene {escape(data['population'])} habitantes</h1>"


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
