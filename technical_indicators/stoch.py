from utils.statistics.sma import Sma

""" Stochastic """


class Stoch:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot
        self.sma = Sma(look_back)

    def __del__(self):
        self.data = []

    def calculate_stoch(self):
        highest_high = self.data.high.rolling(self.look_back).max()
        lowest_low = self.data.low.rolling(self.look_back).min()
        stoch = (self.data.close - lowest_low) / (highest_high-lowest_low) * 100
        return stoch

    def plot_stoch(self, stoch):
        if self.should_plot:
            import matplotlib.pyplot as plt
            stoch.plot()
            plt.legend(["STOCH"])
            plt.show()
