from dataclasses import dataclass

from database import db


@dataclass
class Event(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Event('{self.date}', '{self.title}', '{self.text}')"

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'title': self.title,
            'text': self.text
        }
