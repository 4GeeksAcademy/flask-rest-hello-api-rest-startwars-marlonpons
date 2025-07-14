from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from database.db import db
from models.Favorite_Planet import FavoritePlanet


class Planet(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(100))
    terrain: Mapped[str] = mapped_column(String(100))

    residents = db.relationship("People", back_populates="homeworld")
    planet : Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")
    user = db.relationship("User", back_populates="favorite_planets")
    planet = db.relationship("Planet", back_populates="favorites")
    favorites = db.relationship("FavoritePlanet", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
        }