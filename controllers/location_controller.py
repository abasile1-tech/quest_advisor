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
    location = Location.query.get(id)
    users = User.query.join(Visit).filter(Visit.location_id == id)
    return render_template("locations/show.jinja", location=location, users=users)