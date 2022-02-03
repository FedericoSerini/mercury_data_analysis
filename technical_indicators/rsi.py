from utils.statistics.sma import Sma

""" Relative Strength Index """


class Rsi:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def __del__(self):
        self.data = []

    def calculate_rsi_by_sma(self,look_back: int = 14):
        sma = Sma()
        close = self.data.close
        delta = close.diff()
        up, down = delta.clip(lower=0), delta.clip(upper=0)
        up = sma.calculate_sma(up, look_back)
        down = sma.calculate_absolute_sma(down,look_back)
        rs = up / down
        rsi = 100.0 - (100.0 / (1.0 + rs))
        self.plot_rsi(rsi, 'SMA')
        rsi = rsi.fillna(method='bfill')
        rsi = (rsi.shift(1)/50)-1
        return rsi

    def calculate_rsi_by_ewma(self, look_back):
        close = self.data['close']
        delta = close.diff()
        up, down = delta.clip(lower=0), delta.clip(upper=0)
        roll_up1 = up.ewm(span=look_back).mean()  # todo refactor
        roll_down1 = down.abs().ewm(span=look_back).mean()  # todo refactor
        rs = roll_up1 / roll_down1
        rsi = 100.0 - (100.0 / (1.0 + rs))
        self.plot_rsi(rsi, 'EWMA')
        return rsi

    def plot_rsi(self, rsi, origin):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'RSI via {type}'.format(type=origin)
            rsi.plot()
            plt.legend([legend_label])
            plt.show()
