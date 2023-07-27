from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Location, User, Visit
from app import db

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/locations")
def locations():
    locations = Location.query.all()
    return render_template("locations/index.jinja", locations = locations)

@locations_blueprint.route("/locations/<id>")
def show(id):
    return "TODO: Show the location name and the users who have visited"
