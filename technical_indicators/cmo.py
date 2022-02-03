# Chande Momentum Oscillator


class Cmo:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_cmo(self, look_back):
        delta = self.data.close.diff()

        # positive gains (up) and negative gains (down) Series
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        # EMAs of ups and downs
        _gain = up.ewm(com=look_back, adjust=True).mean()
        _loss = down.ewm(com=look_back, adjust=True).mean().abs()

        cmo = 100 * ((_gain - _loss) / (_gain + _loss))
        cmo = cmo.fillna(method='bfill')
        self.plot_cmo(cmo)
        cmo = (cmo.shift(1)/100)
        return cmo

    def plot_cmo(self, cmo):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'CMO'
            cmo.plot()
            plt.legend([legend_label])
            plt.show()
