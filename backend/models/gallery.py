from dataclasses import dataclass
from sqlalchemy.orm import relationship

from database import db

@dataclass
class Gallery(db.Model):
    __tablename__ = "galleries"
    id = db.Column(db.Integer, primary_key=True)
    flyer = db.Column(db.String(255))
    title = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False)

    photos = relationship("Photo", back_populates = "gallery")

    def __repr__(self):
        return f"Gallery('{self.id}', '{self.title}', '{self.flyer}', '{self.date}')"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'flyer': self.flyer,
            'date': self.date
        }