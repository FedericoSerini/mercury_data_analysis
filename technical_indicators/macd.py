import pandas as pd

# MACD

class Macd:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_macd(self, look_back_fast: int = 12, look_back_slow: int = 26):
        data = self.data 
        EMA_fast = pd.Series(
            data.close.ewm(ignore_na=False, span=look_back_fast, adjust=True).mean(),
            name="EMA_fast",
        )
        EMA_slow = pd.Series(
            data.close.ewm(ignore_na=False, span=look_back_slow, adjust=True).mean(),
            name="EMA_slow",
        )
        macd = pd.Series(EMA_fast - EMA_slow)
        macd = macd.fillna(method='bfill')

        max_macd = macd.max()
        min_macd = macd.min()

        normalized_macd = (2*(macd.shift(1) - min_macd) / (max_macd - min_macd))-1
        self.plot_macd(macd)

        return normalized_macd

    def plot_macd(self, macd):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'MACD'
            macd.plot()
            plt.legend([legend_label])
            plt.show()
