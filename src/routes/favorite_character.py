from flask import Flask, request, jsonify, Blueprint
from src.database.db import db
from src.models.Favorite_People import Favorite_People
from src.models.User import User
from src.models.People import People

api = Blueprint("favorite_character", __name__)

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user_id = 1  # ID fijo temporal mientras no hay autenticación
    character = People.query.get(people_id)

    if not character:
        return jsonify({"error": "Personaje no encontrado"}), 404

    new_fav = Favorite_People(user_id=user_id, people_id=people_id)
    db.session.add(new_fav)
    db.session.commit()

    return jsonify({"message": "Personaje favorito agregado"}), 201

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def remove_favorite_people(people_id):
    user_id = 1  # ID fijo temporal mientras no hay autenticación
    
    favorite = Favorite_People.query.filter_by(user_id=user_id, people_id=people_id).first()

    if not favorite:
        return jsonify({"error": "Favorito no encontrado"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Personaje favorito eliminado"}), 200