from utils.statistics.sma import Sma


class BBands:
    def __init__(self, look_back, original_data, olhc_data, should_plot):
        self.look_back = look_back
        self.data = original_data.copy()
        self.ohlc_data = olhc_data.copy()
        self.should_plot = should_plot
        self.sma = Sma(look_back)

    def __del__(self):
        self.data = []

    def calculate_bbands(self):
        sma = self.sma.calculate_sma(self.data.price)
        std = self.data.price.rolling(self.look_back).std()  # refactor
        bollinger_up = sma + std * 2  # Calculate top band
        bollinger_down = sma - std * 2  # Calculate bottom band
        close = self.ohlc_data.close
        self.plot_bbands(close, bollinger_up, bollinger_down)
        return [close, bollinger_up, bollinger_down]

    def plot_bbands(self, close, bollinger_up, bollinger_down):
        if self.should_plot:
            import matplotlib.pyplot as plt
            plt.title('Bollinger Bands')
            plt.xlabel('Days')
            plt.ylabel('Closing Prices')
            plt.plot(close, label='Closing Prices')
            plt.plot(bollinger_up, label='Bollinger Up', c='g')
            plt.plot(bollinger_down, label='Bollinger Down', c='r')
            plt.legend()
            plt.show()
