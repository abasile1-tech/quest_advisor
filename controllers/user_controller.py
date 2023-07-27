from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import User, Location, Visit

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users = users)

@users_blueprint.route("/users/<id>")
def show(id):
    user = User.query.get(id)
    locations = Location.query.join(Visit).filter(Visit.user_id == id)
    return render_template("users/show.jinja", user=user, locations=locations)
