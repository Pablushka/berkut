from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from database import db

@dataclass
class Photo(db.Model):
    __tablename__ = "photos"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    gallery_id = db.Column(db.Integer, ForeignKey("galleries.id"))

    gallery = relationship("Gallery", back_populates = "photos")

    def __repr__(self):
        return f"Photo('{self.id}', '{self.image}', '{self.gallery_id}')"

    def to_dict(self):
        return {
            'id': self.id,
            'image': self.image,
            'gallery_id': self.gallery_id,
            'gallery': self.gallery.to_dict()
        }