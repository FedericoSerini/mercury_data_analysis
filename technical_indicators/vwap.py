import numpy as np

""" Volume Weighted Average Price """


class Vwap:

    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def __del__(self):
        self.data = []

    def calculate_vwap(self):
        vwap = self.data.T.apply(lambda x: np.average(x.price, weights=x.shares)).to_frame('vwap')
        self.plot_vwap(vwap)
        return vwap

    def plot_vwap(self, vwap):
        if self.should_plot:
            import matplotlib.pyplot as plt
            vwap.plot()
            plt.legend(["VWAP"])
            plt.show()
