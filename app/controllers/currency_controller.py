"""Currency Controller file"""

from flask_restful import Resource
from ..dataset.currencies import CURRENCIES_NAMES, CURRENCIES_SYMBOLS

class CurrencyController(Resource):
    """Currency Controller"""
    @classmethod
    def get(cls):
        """This function returns the list of available currencies"""
        return {'names': CURRENCIES_NAMES, 'symbols': CURRENCIES_SYMBOLS}
