from utils.statistics.sma import Sma

""" Relative Strength Index """


class Rsi:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot
        self.sma = Sma(look_back)

    def __del__(self):
        self.data = []

    def calculate_rsi_by_sma(self):
        close = self.data.close
        delta = close.diff()
        up, down = delta.clip(lower=0), delta.clip(upper=0)
        up = self.sma.calculate_sma(up)
        down = self.sma.calculate_absolute_sma(down)
        rs = up / down
        rsi = 100.0 - (100.0 / (1.0 + rs))
        self.plot_rsi(rsi, 'SMA')
        rsi = (rsi/50)-1
        return rsi

    def calculate_rsi_by_ewma(self):
        close = self.data['close']
        delta = close.diff()
        up, down = delta.clip(lower=0), delta.clip(upper=0)
        roll_up1 = up.ewm(span=self.look_back).mean()  # todo refactor
        roll_down1 = down.abs().ewm(span=self.look_back).mean()  # todo refactor
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
