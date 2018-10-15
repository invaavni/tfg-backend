"""app/__init__.py"""

from flask import Flask
from flask_cors import CORS

from config import APP_CONFIG
from .api import ini_api

def create_app(config_name):
    """This function creates the FLASK APP"""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('../config.py')
    app.logger.info('Server set to %s', config_name)
    ini_api(app)
    app.logger.info('API created succesfully')

    return app
