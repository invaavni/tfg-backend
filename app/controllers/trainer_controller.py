"""Trainer Controller file"""

import numpy as np
import os
from flask_restful import Resource, current_app
from sklearn.preprocessing import MinMaxScaler
from flask import request
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras import backend as K
from ..services.csv_service import CsvService
from ..dataset.currencies import CURRENCIES_SYMBOLS

class TrainerController(Resource):
    """Trainer Controller"""
    @classmethod
    def post(cls):
        """This function trains a neural network for the currency passed as parameter"""
        
        training_set = CsvService().getAllDataBeforeDate('2018-01-01')

        scaler = MinMaxScaler()
        training_set_scaled = scaler.fit_transform(training_set)

        x_train = []
        y_train = []

        for currency in CURRENCIES_SYMBOLS:
            current_app.logger.info(currency)
            trs = CsvService().getAllCurrencyDataBeforeDate(currency, '2018-01-01')
            if len(trs) > 60:
                trs = np.array(trs)
                trss = scaler.transform(trs)
                for i in range(60, len(trss)):
                    x_train.append(trss[i-60:i, 0])
                    y_train.append(trss[i, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        regressor = Sequential()

        regressor.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        regressor.add(Dropout(0.2))

        regressor.add(LSTM(units=50, return_sequences=True))
        regressor.add(Dropout(0.2))

        regressor.add(LSTM(units=50, return_sequences=True))
        regressor.add(Dropout(0.2))

        regressor.add(LSTM(units=50))
        regressor.add(Dropout(0.2))

        regressor.add(Dense(units=1))

        regressor.compile(optimizer='adam', loss='mean_squared_error')

        regressor.fit(x_train, y_train, epochs=100, batch_size=32)

        regressor.save(os.path.join(
            os.path.dirname(__file__),
            '../trained_networks/TOP.h5'))

        K.clear_session()

        return "done"
