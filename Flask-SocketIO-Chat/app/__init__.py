from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




migrate = Migrate()



def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug

    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

    db = SQLAlchemy()


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app

class Room(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    room_names = db.Column(db.String(500))

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(500))



if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)