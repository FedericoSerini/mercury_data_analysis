# Percentage Price Oscillator

class Ppo:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_ppo(self):
        period = self.look_back
        roc = (self.data.close.diff(period) / self.data.close.shift(period)) * 100
        self.plot_ppo(roc)
        return roc

    def plot_ppo(self, roc):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'PPO'
            roc.plot()
            plt.legend([legend_label])
            plt.show()
