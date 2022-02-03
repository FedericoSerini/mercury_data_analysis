import numpy as np

# Weighted Moving Average


class Wma:

    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_wma(self, look_back: int = 9):
        period = look_back
        d = (period * (period + 1)) / 2  # denominator
        weights = np.arange(1, period + 1)

        def linear(w):
            def _compute(x):
                return (w * x).sum() / d

            return _compute

        _close = self.data.close.rolling(period, min_periods=period)
        wma = _close.apply(linear(weights), raw=True)
        wma = wma.fillna(method='bfill')
        self.plot_wma(wma)
        wma = (self.data.close-wma.shift(1))*(10/self.data.close)
        return wma

    def plot_wma(self, wma):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'Weighted Moving Average'
            wma.plot()
            plt.legend([legend_label])
            plt.show()
