from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models.People import People

api = Blueprint("api/Peoples", __name__)
#listar todos los personajrs
@api.route("/", methods=["GET"])
def get_peoples():
    all_peoples = People.query.all()
    all_peoples = list(map(lambda x: x.serialize(),all_peoples))

    return jsonify({"all_peoples": all_peoples})

#lo mismo que la anterior pero seleccionando por id
@api.route("/<people_id>")
def get_people_by_id(people_id):
    people = People.query.get(people_id)
    return jsonify({"People": people.serialize()})