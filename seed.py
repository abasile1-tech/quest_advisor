from app import db
from models import Location, User
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Location.query.delete()
    User.query.delete()
    user1 = User(name="Bilbo")
    user2 = User(name="Frodo")
    user3 = User(name="Gollum")
    location1 = Location(name="The Prancing Pony", category="entertainment")
    location2 = Location(name="The Lisboa Fountain", category="culture")

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.add(location1)
    db.session.add(location2)
    db.session.commit()