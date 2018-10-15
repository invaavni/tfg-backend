"""Service which takes care of all data in the csv file"""
import os
import pandas as pd

class CsvService():
    """Class which takes care of all data in the csv file"""
    def getAllCurrencyDataBeforeDate(self, currency, date):
        """Returns all data related to a currency before a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/crypto-markets.csv'))
        data = data.iloc[:, :].values
        data = [x[5:6] for x in data if x[1] == currency and x[3] < date]
        return data

    def getAllCurrencyDataAfterDate(self, currency, date):
        """Returns all data related to a currency after a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/crypto-markets.csv'))
        data = data.iloc[:, :].values
        data = [x[5:6] for x in data if x[1] == currency and x[3] >= date]
        return data

    def getAllCurrencyBetweenDates(self, currency, initial_date, final_date):
        """Returns all data related to a currency after a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/crypto-markets.csv'))
        data = data.iloc[:, :].values
        data = [x[5:6] for x in data if x[1] == currency and x[3] >= initial_date and x[3] < final_date]
        return data

    def getAllCurrencyData(self, currency):
        """Returns all data related to a currency"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/crypto-markets.csv'))
        data = data.iloc[:, :].values
        data = [x[5:6] for x in data if x[1] == currency]
        return data

    def getMarketCapBeforeDate(self, date):
        """Returns all data related to a marketCap before a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/marketCap.csv'))
        data = data.iloc[:, :].values
        data = [x[1:] for x in data if x[0] < date]
        return data

    def getMarketCapAfterDate(self, date):
        """Returns all data related to a marketCap after a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/marketCap.csv'))
        data = data.iloc[:, :].values
        data = [x[1:] for x in data if x[0] >= date]
        return data

    def getMarketCapBetweenDates(self, initial_date, final_date):
        """Returns all data related to a marketCap after a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/marketCap.csv'))
        data = data.iloc[:, :].values
        data = [x[1:] for x in data if x[0] >= initial_date and x[0] < final_date]
        return data

    def getMarketCap(self):
        """Returns all data related to a marketCap"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/marketCap.csv'))
        data = data.iloc[:, :].values
        data = [x[1:] for x in data]
        return data
        
    def getAllDataBeforeDate(self, date):
        """Returns all data before a certain date"""
        data = pd.read_csv(os.path.join(
            os.path.dirname(__file__),
            '../dataset/crypto-markets.csv'))
        data = data.iloc[:, :].values
        data = [x[5:6] for x in data if x[3] < date]
        return data
