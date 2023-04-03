from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the extension
db = SQLAlchemy()

# Create the app
app = Flask(__name__)

# Configure SQLite db, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the extension
db.init_app(app)

# DEFINE A MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True)

# CREATE THE TABLES
with app.app_context():
    db.create_all()

    # INSTANTIATE
    # panda = User(username="Panda", email="panda@gmail.com")
    # sarah = User(username="sarah", email="sarahn@gmail.com")
    # db.session.add(panda)
    # db.session.add(sarah)
    # db.session.commit()

    # QUERY
    sarah = User.query.filter_by(username="sarah").first()
    print(sarah)

    # DELETE
    db.session.delete(sarah)
    db.session.commit()