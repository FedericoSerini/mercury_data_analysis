from utils.statistics.sma import Sma

""" Triangular Moving Average """


class Trima:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot
        self.sma = Sma(look_back)

    def __del__(self):
        self.data = []

    def calculate_trima(self):
        sma = self.sma.calculate_sma(self.data.close)
        trima = sma.rolling(window=self.look_back).sum()/self.look_back
        trima = trima.fillna(method='bfill')
        self.plot_trima(trima)
        return trima

    def plot_trima(self, trima):
        if self.should_plot:
            import matplotlib.pyplot as plt
            trima.plot()
            plt.legend(["TRIMA"])
            plt.show()
