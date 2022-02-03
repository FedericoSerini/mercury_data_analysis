# Rate-of-Change

class Roc:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_roc(self,look_back):
        period = look_back
        roc = (self.data.close.diff(period) / self.data.close.shift(period)) * 100
        roc = roc.fillna(method='bfill')
        self.plot_roc(roc)
        roc = roc.shift(1)/20
        return roc

    def plot_roc(self, roc):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'ROC'
            roc.plot()
            plt.legend([legend_label])
            plt.show()
