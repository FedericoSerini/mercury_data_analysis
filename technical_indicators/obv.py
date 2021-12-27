import numpy as np

""" On Balance Volume """


class Obv:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def __del__(self):
        self.data = []

    def calculate_obv(self):
        delta = np.sign(self.data.close.diff())
        obv = (delta*self.data.volume_cry).cumsum()
        self.plot_obv(obv)
        return obv

    def plot_obv(self, obv):
        if self.should_plot:
            import matplotlib.pyplot as plt
            obv.plot()
            plt.legend(["OBV"])
            plt.show()
