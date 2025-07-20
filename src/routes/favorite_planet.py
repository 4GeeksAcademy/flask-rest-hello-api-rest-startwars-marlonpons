from flask import Blueprint, jsonify
from src.database.db import db
from src.models.Favorite_Planet import Favorite_Planet
from src.models.Planet import Planet

api = Blueprint("favorite_planet", __name__)

# Añadir planeta favorito
@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = 1  # Usuario simulado

    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planeta no encontrado"}), 404

    new_favorite = Favorite_Planet(user_id=user_id, planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": "Planeta agregado a favoritos"}), 201


# Eliminar planeta favorito
@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def remove_favorite_planet(planet_id):
    user_id = 1  # Usuario simulado

    favorite = Favorite_Planet.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if not favorite:
        return jsonify({"error": "Favorito no encontrado"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": "Planeta favorito eliminado"}), 200
