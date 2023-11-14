from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 
from flask_login import LoginManager
from flask_cors import CORS

from config import config_options

db = SQLAlchemy()
cors = CORS()

login_manager = LoginManager()

def create_app(config_name='production'):

    # app
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    # initialization
    db.init_app(app)
    cors.init_app(app,resources={r"/*": {"origins": "*"}})
    login_manager.init_app(app)

    # blueprints

    # routing

    # registration

    # export
    return app
