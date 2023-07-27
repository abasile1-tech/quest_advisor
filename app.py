from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{PASSWORD}@localhost:5432/quest_advisor"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.visit_controller import visits_blueprint
from controllers.location_controller import locations_blueprint
from controllers.user_controller import users_blueprint

app.register_blueprint(visits_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)