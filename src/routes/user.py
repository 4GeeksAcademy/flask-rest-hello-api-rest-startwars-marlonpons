from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models.User import User


api = Blueprint("api/user", __name__)

@api.route("/")
def get_user():
    all_users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), all_users))
    return jsonify({"all_users": all_users})

"""
En la clase Horacio dejo las funciones con el mismo nombre -get_user- y funciono
A mi me lanzo este error: AssertionError: View function mapping is overwriting an existing endpoint function: api/user.get_user
Por tanto tuve que cambiar el nombre de las funciones
"""
@api.route("/<user_id>")
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return jsonify({"usuario": user.serialize()})

@api.route("/create", methods=["POST"])
def register():

    body = request.get_json()
    """
    new_user = User(
        email=body["email"],
        password=body["password"],
        is_active=True
        )
    """  

    #De esta manera como se hizo en clase Postam me da error
    new_user = User()
    new_user.email = body["email"]
    new_user.password = body["password"]
    new_user.is_active = True


    db.session.add(new_user)
    db.session.commit()

    print(body)

    return jsonify({"usuario": new_user.serialize()})