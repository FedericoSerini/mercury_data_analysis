from technical_indicators.ema import Ema

""" Triple Exponential Moving Average """
#TODO test


class Tema:
    def __init__(self, look_back, original_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.should_plot = should_plot
        self.calculated_ema = Ema(look_back, self.data, False).calculate_ema()

    def __del__(self):
        self.data = []

    def calculate_tema(self):
        triple_ema = 3 * self.calculated_ema
        ema_ema_ema = (
            self.calculated_ema
                .ewm(ignore_na=False, span=self.look_back, adjust=True)
                .mean()
                .ewm(ignore_na=False, span=self.look_back, adjust=True)
                .mean()
        )

        tema = (
                triple_ema
                - 3 * self.calculated_ema.ewm(span=self.look_back, adjust=True).mean()
                + ema_ema_ema
        )
        self.plot_tema(tema)
        tema = (self.data.close-tema)*10/self.data.close
        return tema

    def plot_tema(self, tema):
        if self.should_plot:
            import matplotlib.pyplot as plt
            tema.plot()
            plt.legend(["TEMA"])
            plt.show()
