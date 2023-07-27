from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Visit, User, Location
from app import db

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    visits = Visit.query.all()
    return render_template("visits/index.jinja", visits = visits)

# NEW
# GET '/visits/new'
@visits_blueprint.route("/visits/new", methods=['GET'])
def new_visit():
    users = User.query.all()
    locations = Location.query.all()
    return render_template("visits/new.jinja", users = users, locations = locations)

# CREATE
# POST '/visits'
@visits_blueprint.route("/visits",  methods=['POST'])
def create_visit():
    user_id = request.form['user_id']
    location_id = request.form['location_id']
    review = request.form['review']
    visit = Visit(user_id = user_id, location_id = location_id, review=review)
    db.session.add(visit)
    db.session.commit()
    return redirect('/visits')


# DELETE
# DELETE '/visits/<id>/delete'
@visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
def delete_visit(id):
    Visit.query.filter_by(id = id).delete()
    db.session.commit()
    return redirect('/visits')