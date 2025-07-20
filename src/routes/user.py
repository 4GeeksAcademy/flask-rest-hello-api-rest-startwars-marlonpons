from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models.User import User


api = Blueprint("api/user", __name__)

@api.route("/")
def get_user():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))
    return jsonify({"all_users": all_users})



@api.route("/<user_id>")
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return jsonify({"usuario": user.serialize()})



@api.route("/create", methods=["POST"])
def register():

    body = request.get_json()
    new_user = User()
    new_user.email = body["email"]
    new_user.password = body["password"]
    new_user.is_active = True


    db.session.add(new_user)
    db.session.commit()

    print(body)

    return jsonify({"usuario": new_user.serialize()})

@api.route('/favorites', methods=['GET'])
def get_user_favorites():
    user_id = 1  # Usuario simulado

    # Obtener favoritos de personajes
    people_favs = Favorite_People.query.filter_by(user_id=user_id).all()
    people_favs_serialized = [{
        "id": fav.id,
        "people_id": fav.people_id,
        "name": People.query.get(fav.people_id).name
    } for fav in people_favs]

    # Obtener favoritos de planetas
    planet_favs = Favorite_Planet.query.filter_by(user_id=user_id).all()
    planet_favs_serialized = [{
        "id": fav.id,
        "planet_id": fav.planet_id,
        "name": Planet.query.get(fav.planet_id).name
    } for fav in planet_favs]

    return jsonify({
        "favorite_characters": people_favs_serialized,
        "favorite_planets": planet_favs_serialized
    }), 200