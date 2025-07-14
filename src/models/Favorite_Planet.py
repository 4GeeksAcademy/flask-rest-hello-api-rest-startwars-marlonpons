from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database.db import db


class FavoritePlanet(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    planet_id: Mapped[int] = mapped_column(db.ForeignKey('planet.id'))

    user = db.relationship("User", back_populates="favorite_planets")
    planet = db.relationship("Planet", back_populates="favorites")
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet": self.planet.serialize()
        }