from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from database.db import db
from models.Favorite_People import FavoritePeople

class People(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(20))
    height: Mapped[str] = mapped_column(String(10))
    mass: Mapped[str] = mapped_column(String(10))

    homeworld = db.relationship("Planet", back_populates="residents")
    favorites = db.relationship("FavoritePeople", back_populates="people")
    planet_id = mapped_column(db.ForeignKey('planet.id'))
    people : Mapped[List["FavoritePeople"]] = relationship(back_populates = "people")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "planet_id": self.planet_id
        }