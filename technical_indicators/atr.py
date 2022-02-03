import numpy as np
from utils.statistics.sma import Sma

""" Average true range """


class Atr:

    def __init__(self, look_back, original_data):
        self.look_back = look_back
        self.data = original_data.copy()

    def __del__(self):
        self.data = []

    def calculate_tr(self):
        """ Calculates the True Range """
        self.data['H-L'] = self.data.high - self.data.low
        self.data['H-C'] = np.abs(self.data.high - self.data.close.shift(1))
        self.data['L-C'] = np.abs(self.data.low - self.data.close.shift(1))
        self.data['TR'] = self.data[['H-L', 'H-C', 'L-C']].max(axis=1)
        return self.data['TR']

    def calculate_atr(self):
        """ Calculates the Average True Range """
        true_range = self.calculate_tr()
        average_true_range = Sma().calculate_sma(true_range, self.look_back)
        average_true_range = average_true_range.fillna(method='bfill')
        return average_true_range
