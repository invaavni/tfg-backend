"""API file"""

from flask_restful import Api
from .controllers.trainer_controller import TrainerController
from .controllers.currency_controller import CurrencyController
from .controllers.predict_test_controller import PredictTestController
from .controllers.predict_controller import PredictController

def ini_api(app):
    """Function that sets the API"""
    url = app.config['API_URL']
    api = Api(app)
    api.add_resource(TrainerController, url + '/train', endpoint='train')
    api.add_resource(CurrencyController, url + '/currencies', endpoint='currencies')
    api.add_resource(PredictTestController, url + '/predict/test', endpoint='predict/test')
    api.add_resource(PredictController, url + '/predict', endpoint='predict')
