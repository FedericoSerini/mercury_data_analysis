# Commodity Channel Index

class Cci:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_cci(self, look_back: int = 20):
        tp = (self.data.high + self.data.low + self.data.close) / 3
        tp_rolling = tp.rolling(window=look_back, min_periods=0)
        mad = tp_rolling.apply(lambda s: abs(s - s.mean()).mean(), raw=True)
        cci = (tp - tp_rolling.mean()) / (0.015 * mad)
        cci = cci.fillna(method='bfill')
        self.plot_cci(cci)
        cci = (cci.shift(1)/300)
        return cci

    def plot_cci(self, cci):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'CCI'
            cci.plot()
            plt.legend([legend_label])
            plt.show()
