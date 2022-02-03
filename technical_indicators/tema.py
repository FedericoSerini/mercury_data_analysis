from technical_indicators.ema import Ema

""" Triple Exponential Moving Average """
#TODO test


class Tema:
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def __del__(self):
        self.data = []

    def calculate_tema(self, look_back):
        calculated_ema = Ema(self.data, False).calculate_ema(look_back)
        triple_ema = 3 * calculated_ema
        ema_ema_ema = (
            calculated_ema
                .ewm(ignore_na=False, span=look_back, adjust=True)
                .mean()
                .ewm(ignore_na=False, span=look_back, adjust=True)
                .mean()
        )

        tema = (
                triple_ema
                - 3 * calculated_ema.ewm(span=look_back, adjust=True).mean()
                + ema_ema_ema
        )
        self.plot_tema(tema)
        tema = tema.fillna(method='bfill')
        tema = (self.data.close-tema.shift(1))*10/self.data.close
        return tema

    def plot_tema(self, tema):
        if self.should_plot:
            import matplotlib.pyplot as plt
            tema.plot()
            plt.legend(["TEMA"])
            plt.show()
