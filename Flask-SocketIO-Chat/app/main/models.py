from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db = SQLAlchemy(app)
migrate = Migrate()

class Room(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    room_names = db.Column(db.String(500))

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(500))

db.create_all()