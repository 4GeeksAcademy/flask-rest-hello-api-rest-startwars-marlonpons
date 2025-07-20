
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from database.db import db
from models.Favorite_People import FavoritePeople
from models.Favorite_Planet import FavoritePlanet

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorite_people : Mapped[List["FavoritePeople"]] = relationship("FavoritePeople",back_populates="user")
    favorite_planets : Mapped[List["FavoritePlanet"]] = relationship("FavoritePlanet",back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
