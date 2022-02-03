""" Simple Moving Average """


class Sma:

    def __init__(self):
        self.p = ""

    def calculate_sma_normalized(self, data, look_back: int = 41):
        sma = data.rolling(look_back).mean()
        sma = sma.fillna(method='bfill')
        sma = (data - sma.shift(1)) * (10 / data)
        return sma

    def calculate_sma(self, data, look_back):
        sma = data.rolling(look_back).mean()
        sma = sma.fillna(method='bfill')
        return sma

    def calculate_absolute_sma(self, data, look_back):
        sma = data.abs().rolling(look_back).mean()
        sma = sma.fillna(method='bfill')
        return sma
