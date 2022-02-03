from technical_indicators.ema import Ema

""" Double Exponential Moving Average """
#TODO test


class Dema:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot
        self.calculated_ema = Ema(look_back, original_data, False).calculate_ema()

    def __del__(self):
        self.data = []

    def calculate_dema(self):
        dema = 2 * self.calculated_ema - self.calculated_ema.ewm(span=self.look_back, adjust=True).mean()
        dema = dema.fillna(method='bfill')
        self.plot_dema(dema)
        return dema

    def plot_dema(self, dema):
        if self.should_plot:
            import matplotlib.pyplot as plt
            dema.plot()
            plt.legend(["DEMA"])
            plt.show()
