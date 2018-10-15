"""Predict Controller file"""

from datetime import datetime, timedelta
import os
import numpy as np
from keras import backend as K
from flask_restful import Resource, current_app
from flask import request
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from ..services.csv_service import CsvService
from ..helpers.math_helper import MathHelper

class PredictTestController(Resource):
    """Predict Controller"""
    @classmethod
    def get(cls):
        """This function uses a trained neural network to predict future dates of the currency"""
        currency = request.args.get('currency')
        if currency == 'CAP':
            training_set = CsvService().getMarketCapBeforeDate('2018-01-01')
            inputs = CsvService().getMarketCapAfterDate('2017-11-02')
            real_data = CsvService().getMarketCapAfterDate('2018-01-01')
        else:
            training_set = CsvService().getAllCurrencyDataBeforeDate(currency, '2018-01-01')
            inputs = CsvService().getAllCurrencyDataAfterDate(currency, '2017-11-02')
            real_data = CsvService().getAllCurrencyDataAfterDate(currency, '2018-01-01')

        inputs = np.array(inputs)
        inputs = inputs.reshape(-1, 1)

        scaler = MinMaxScaler()
        training_set_scaled = scaler.fit_transform(training_set)

        inputs = scaler.transform(inputs)

        x_test = []
        for i in range(60, len(inputs)):
            x_test.append(inputs[i-60:i, 0])
        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

        regressor = load_model(os.path.join(
            os.path.dirname(__file__),
            '../trained_networks/ETH.h5'))

        prediction = regressor.predict(x_test)
        prediction = scaler.inverse_transform(prediction)
        prediction = prediction.tolist()
        prediction = [x[0] for x in prediction]

        K.clear_session()

        real_data = np.array(real_data)
        real_data = real_data.tolist()
        real_data = [x[0] for x in real_data]

        labels = []
        for i in range(0, 84):
            date = datetime.strptime('2018-01-01', '%Y-%m-%d')
            date = date + timedelta(days=i)
            labels.append(date.strftime('%Y-%m-%d'))

        r_squared = MathHelper().rsquared(real_data, prediction)

        return {
            'prediction': prediction,
            'realData': real_data,
            'labels': labels,
            'r_squared': r_squared
            }
