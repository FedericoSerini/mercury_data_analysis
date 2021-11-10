""" Simple Moving Average """


class Sma:

    def __init__(self, look_back):
        self.look_back = look_back

    def calculate_sma(self, data):
        return data.rolling(self.look_back).mean()

    def calculate_absolute_sma(self, data):
        return data.abs().rolling(self.look_back).mean()
