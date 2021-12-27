

class Williams:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_williams(self):
        highest_high = self.data.high.rolling(center=False, window=self.look_back).max()
        lowest_low = self.data.low.rolling(center=False, window=self.look_back).min()
        wr = (highest_high - self.data.close) / (highest_high - lowest_low)
        self.plot_williams(wr)
        return wr * -100

    def plot_williams(self, williams):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'Williams %R'
            williams.plot()
            plt.legend([legend_label])
            plt.show()
