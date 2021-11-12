from utils.statistics.sma import Sma

""" Exponential Moving Average """


class Ema:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot
        self.sma = Sma(look_back)

    def __del__(self):
        self.data = []

    def calculate_ema(self):
        exponential_moving = self.data.close.ewm(span=self.look_back)
        exponential_moving_average = exponential_moving.mean()
        self.plot_ema(exponential_moving_average)
        return exponential_moving_average

    def plot_ema(self, ema):
        if self.should_plot:
            import matplotlib.pyplot as plt
            ema.plot()
            plt.legend(["EMA"])
            plt.show()
