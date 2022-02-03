

class Williams:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_williams(self, look_back: int = 14):
        highest_high = self.data.high.rolling(center=False, window=look_back).max()
        lowest_low = self.data.low.rolling(center=False, window=look_back).min()
        wr = (highest_high - self.data.close) / (highest_high - lowest_low)
        self.plot_williams(wr)
        wr = wr * -100
        wr = wr.fillna(method='bfill')
        wr = (wr.shift(1)/50)+1
        return wr

    def plot_williams(self, williams):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'Williams %R'
            williams.plot()
            plt.legend([legend_label])
            plt.show()
