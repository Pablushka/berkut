from dataclasses import dataclass
from datetime import datetime
from database import db


@dataclass
class User(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    token = db.Column(db.String(254), nullable=False)
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
