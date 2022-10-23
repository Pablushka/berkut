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

# Crear modelos

Para crear modelos, se debe crear una clase que herede de `db.Model`. Esta clase debe tener un atributo `id` que sea de tipo `db.Integer` y sea la llave primaria. Es una buena práctica crear un archivo por cada modelo dentro de una carpeta que contenga todos nuestros modelos. Por ejemplo, en el archivo `models/user.py` crearemos el modelo `User`:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```
