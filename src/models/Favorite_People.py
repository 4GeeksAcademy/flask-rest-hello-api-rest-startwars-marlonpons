from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database.db import db

class FavoritePeople(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    character_id: Mapped[int] = mapped_column(db.ForeignKey('people.id'))

    user = db.relationship("User", back_populates = "favorite_people")
    people = db.relationship("People",back_populates = "favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people": self.people.serialize()
        }