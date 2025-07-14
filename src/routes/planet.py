from flask import Flask, request, jsonify, Blueprint
from database.db import db
from models.Planet import Planet

api = Blueprint("api/planets", __name__)

@api.route("/", methods=["GET"])
def get_planets():
    all_planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(),all_planets))

    return jsonify({"all_planets": all_planets})


@api.route("/<planet_id>")
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return jsonify({"Planet": planet.serialize()})