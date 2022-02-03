from utils.statistics.sma import Sma

""" Exponential Moving Average """


class Ema:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def __del__(self):
        self.data = []

    def calculate_ema(self, look_back):
        exponential_moving = self.data.close.ewm(span=look_back)
        exponential_moving_average = exponential_moving.mean()
        exponential_moving_average = exponential_moving_average.fillna(method='bfill')
        self.plot_ema(exponential_moving_average)
        return exponential_moving_average

    def calculate_ema_normalized(self, look_back):
        exponential_moving_average = self.calculate_ema(look_back)
        exponential_moving_average = (self.data.close-exponential_moving_average.shift(1))*10/self.data.close
        return exponential_moving_average

    def plot_ema(self, ema):
        if self.should_plot:
            import matplotlib.pyplot as plt
            ema.plot()
            plt.legend(["EMA"])
            plt.show()
