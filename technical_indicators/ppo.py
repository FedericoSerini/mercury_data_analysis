import pandas as pd 

# Percentage Price Oscillator

class Ppo:

    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_ppo(self, look_back_fast: int = 12, look_back_slow: int = 26):
        data = self.data
        EMA_fast = pd.Series(
            data.close.ewm(ignore_na=False, span=look_back_fast, adjust=True).mean(),
            name="EMA_fast",
        )
        EMA_slow = pd.Series(
            data.close.ewm(ignore_na=False, span=look_back_slow, adjust=True).mean(),
            name="EMA_slow",
        )
        ppo = pd.Series(((EMA_fast - EMA_slow) / EMA_slow) * 100)
        ppo = ppo.fillna(method='bfill')
        self.plot_ppo(ppo)
        ppo = ppo.shift(1)/10
        return ppo

    def plot_ppo(self, ppo):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'PPO'
            ppo.plot()
            plt.legend([legend_label])
            plt.show()
