import numpy as np
from utils.statistics.sma import Sma

""" Average true range """


class Atr:

    def __init__(self, look_back, original_data):
        self.look_back = look_back
        self.data = original_data.copy()
        self.sma = Sma(look_back)

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
        average_true_range = self.sma.calculate_sma(true_range)
        return average_true_range
