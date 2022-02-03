# Accumulation/Distribution
import numpy as np


class Ad:

    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def __del__(self):
        self.data = []

    def calculate_ad(self):
        money_flow_multiplier = ((self.data.close - self.data.low) - (self.data.high - self.data.close)) / (
                self.data.high - self.data.low)
        ad = (money_flow_multiplier * self.data.volume_cry).cumsum()
        self.plot_ad(ad)
        ad = (ad / 50) - 1
        ad = ad.fillna(method='bfill')
        return ad

    def plot_ad(self, ad):
        if self.should_plot:
            import matplotlib.pyplot as plt
            ad.plot()
            plt.legend(["AD"])
            plt.show()
