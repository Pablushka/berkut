from dataclasses import dataclass
from datetime import datetime
from database import db
from sqlalchemy import event
from config import settings, SECRET_KEY


@dataclass
class User(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    secret = db.Column(db.String(254), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.email}', '{self.last_login}', '{self.is_active}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'last_login': self.last_login.strftime("%d-%m-%Y"),
            'is_active': self.is_active,
            'is_admin': self.is_admin
        }

    def get_secret(self):
        return SECRET_KEY.decrypt(self.secret, 'ascii')


@ event.listens_for(User, 'before_insert')
def receive_before_insert(mapper, connection, target):
    "listen for the 'before_insert' event"

    print("before insert")
    target.secret = SECRET_KEY.encrypt(bytes(target.secret, 'ascii'))


# @event.listens_for(User, 'before_update')
# def receive_before_update(mapper, connection, target):
#     "listen for the 'before_update' event"

#     print("before update")
#     print(target.secret)
#     target.secret = settings.encrypt(bytes(target.secret, 'ascii'))
