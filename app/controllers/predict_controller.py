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

class PredictController(Resource):
    """Predict Controller"""
    @classmethod
    def get(cls):
        """This function uses a trained neural network to predict future dates of the currency"""
        currency = request.args.get('currency')
        final_date = request.args.get('finalDate')
        final_date = datetime.strptime(final_date, '%Y-%m-%d')
        initial_date = datetime.strptime('2018-01-01', '%Y-%m-%d')
        delta = final_date - initial_date 
 
        training_set = CsvService().getAllCurrencyDataBeforeDate(currency, '2018-01-01') 
        inputs = CsvService().getAllCurrencyBetweenDates(currency, '2017-11-02', '2018-01-01')

        inputs = np.array(inputs)
        inputs = inputs.reshape(-1, 1)

        scaler = MinMaxScaler()
        training_set_scaled = scaler.fit_transform(training_set)

        inputs = scaler.transform(inputs)

        regressor = load_model(os.path.join(
            os.path.dirname(__file__),
            '../trained_networks/ETH.h5'))

        for i in range(60, 60 + delta.days):
            x_test = []
            x_test.append(inputs[i-60:i, 0])
            x_test_np = np.array(x_test)
            x_test_np = np.reshape(x_test_np, (1, x_test_np.shape[1], 1))
            prediction = regressor.predict(x_test_np)
            inputs = np.append(inputs, prediction)
            inputs = inputs.reshape(-1, 1)

        prediction = scaler.inverse_transform(inputs[60:])
        prediction = prediction.tolist()
        prediction = [x[0] for x in prediction]

        K.clear_session()

        actual_date = initial_date
        labels = []
        while final_date != actual_date:
            labels.append(actual_date.strftime('%Y-%m-%d'))
            actual_date = actual_date + timedelta(days=1)

        return {'prediction': prediction, 'labels': labels}
