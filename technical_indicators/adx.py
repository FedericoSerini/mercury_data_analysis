from technical_indicators.atr import Atr

""" Average Directional Movement"""


class Adx:

    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.should_plot = should_plot
        self.data = original_data.copy()
        self.calculated_atr = Atr(look_back, self.data).calculate_atr()

    def __del__(self):
        self.data = []

    def get_positive_directional_index(self):
        positive_directional_movement = self.data.high.diff()
        positive_directional_movement[positive_directional_movement < 0] = 0
        positive_directional_index = 100 * (
                positive_directional_movement.ewm(alpha=1 / self.look_back).mean() / self.calculated_atr)  # todo refactor
        return positive_directional_index

    def get_negative_directional_index(self):
        negative_directional_movement = self.data.low.diff()
        negative_directional_movement[negative_directional_movement > 0] = 0
        negative_directional_index = abs(
            100 * (negative_directional_movement.ewm(alpha=1 / self.look_back).mean() / self.calculated_atr))  # todo refactor
        return negative_directional_index

    def calculate_adx(self):
        pdi = self.get_positive_directional_index()
        ndi = self.get_negative_directional_index()
        dx = (abs(pdi - ndi) / abs(pdi + ndi)) * 100
        adx = ((dx.shift(1) * (self.look_back - 1)) + dx) / self.look_back
        adx_smooth = adx.ewm(alpha=1 / self.look_back).mean() # todo refactor
        self.plot_adx(pdi, ndi, adx_smooth)
        return adx_smooth

    def plot_adx(self, pdi, ndi, adx_smooth):
        if self.should_plot:
            import matplotlib.pyplot as plt
            ax1 = plt.subplot2grid((11, 1), (0, 0), rowspan=5, colspan=1)
            ax2 = plt.subplot2grid((11, 1), (7, 0), rowspan=5, colspan=1)
            ax1.plot(self.data['close'], linewidth=2, color='#ff9800')
            ax1.set_title('BTC EUR CLOSING PRICE')
            ax2.plot(pdi, color='#26a69a', label='+ DI 14', linewidth=3, alpha=0.3)
            ax2.plot(ndi, color='#f44336', label='- DI 14', linewidth=3, alpha=0.3)
            ax2.plot(adx_smooth, color='#2196f3', label='ADX 14', linewidth=3)
            ax2.axhline(25, color='grey', linewidth=2, linestyle='--')
            ax2.legend()
            ax2.set_title('BTC EUR ADX 14')
            plt.show()
