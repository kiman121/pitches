from flask import Flask
from flask_boostrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

# Instatiating
boostrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    '''
    Function that creates a instance of the app
    Args:
        config_name: configuration setting (development,production or test)
    '''
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
    