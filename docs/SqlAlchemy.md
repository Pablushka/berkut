# Instalación

Antas de hacer esto se debe tener el entorno virtual activado. Para instalar SqlAlchemy, se debe ejecutar el siguiente comando:

```bash
pip install -U Flask-SQLAlchemy
```

El flag `-U` es para actualizar la versión de Flask-SQLAlchemy si ya se tiene instalada. Es lo mismo que usar `--upgrade`.

# Configuarar SqlAlchemy

En nuestra applicación flask se debe setear la clave _SQLALCHEMY_DATABASE_URI_ con la dirección de la base de datos. En nuestro caso, usaremos una base de datos sqlite. Para esto, se debe agregar la siguiente línea en el archivo `app.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db/project.sqlite"
```

# Inicializar la base de datos

```python
from database import db

db.init_app(app)
```

# Crear modelos

Para crear modelos, se debe crear una clase que herede de `db.Model`. Esta clase debe tener un atributo `id` que sea de tipo `db.Integer` y sea la llave primaria. Es una buena práctica crear un archivo por cada modelo dentro de una carpeta que contenga todos nuestros modelos. Por ejemplo, en el archivo `models/user.py` crearemos el modelo `User`:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
```

# Instalar Flask-Migrate

Para poder hacer migraciones de la base de datos, se debe instalar Flask-Migrate. Para esto, se debe ejecutar el siguiente comando:

```bash
pip install -U Flask-Migrate
```

# Configurar Flask-Migrate

Para configurar Flask-Migrate, se debe agregar las siguientes líneas en el archivo `app.py`:

```python
from flask import Flask
from flask_migrate import Migrate
from models.user import User
from database import db

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db/project.sqlite"

# initialize the app with the extension
db.init_app(app)

#
migrate = Migrate(app, db)
```

# Inicializar la base de datos

Para inicializar la base de datos, se debe ejecutar el siguiente comando:

```bash
flask --app my_app db init
```

Esto crea una carpeta `migrations` en la raíz del proyecto. En esta carpeta se guardan los archivos de migración.

# Crear migraciones

Para crear migraciones, se debe ejecutar el siguiente comando:

```bash
flask --app my_app db migrate -m "Primer migración"
```

Esto crea un archivo en la carpeta `migrations/versions` con el nombre de la migración. En este caso, el archivo se llama `<un numero raro aqui>_primer_migracion.py`.

# Aplicar migraciones

Para aplicar migraciones, se debe ejecutar el siguiente comando:

```bash
flask db upgrade
```
