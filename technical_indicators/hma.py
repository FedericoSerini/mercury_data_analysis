import math
import numpy as np
# Hull Moving Average


class Hma:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_hma(self):
        period = self.look_back
        half_length = int(period / 2)
        sqrt_length = int(math.sqrt(period))

        wmaf = self.calculate_wma(self.data,half_length)
        wmas = self.calculate_wma(self.data,period)
        self.data["deltawma"] = 2 * wmaf - wmas
        hma = self.calculate_wma( self.data, column="deltawma", look_back=sqrt_length)
        self.plot_hma(hma)
        return hma

    def calculate_wma(self, data, look_back, column: str = "close"):
        period = look_back
        d = (period * (period + 1)) / 2  # denominator
        weights = np.arange(1, period + 1)

        def linear(w):
            def _compute(x):
                return (w * x).sum() / d

            return _compute

        _close = data[column].rolling(period, min_periods=period)
        wma = _close.apply(linear(weights), raw=True)
        return wma

    def plot_hma(self, hma):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'HMA'
            hma.plot()
            plt.legend([legend_label])
            plt.show()

