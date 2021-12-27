# Commodity Channel Index

class Cci:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_cci(self):
        tp = (self.data.high + self.data.low + self.data.close) / 3
        tp_rolling = tp.rolling(window=self.look_back, min_periods=0)
        mad = tp_rolling.apply(lambda s: abs(s - s.mean()).mean(), raw=True)
        cci = (tp - tp_rolling.mean()) / (0.015 * mad)
        self.plot_cci(cci)
        return cci

    def plot_cci(self, cci):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'CCI'
            cci.plot()
            plt.legend([legend_label])
            plt.show()
