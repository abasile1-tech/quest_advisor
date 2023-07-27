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
    return "TODO: Show the user's name and the lcoations they have visited"
