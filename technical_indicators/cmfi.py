class Cmfi:

    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_cmfi(self, look_back):
        data = self.data
        period = look_back
        mfv = ((data.close - data.low) - (data.high - data.close)) / (data.high - data.low)
        mfv = mfv.fillna(0.0)  # float division by zero
        mfv *= data.volume_fiat
        cmf = (mfv.rolling(period, min_periods=0).sum() / data.volume_fiat.rolling(period, min_periods=0).sum())
        cmf = cmf.fillna(method='bfill')
        self.plot_cmfi(cmf)
        return cmf.shift(1)

    def plot_cmfi(self, cmfi):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'CMFI'
            cmfi.plot()
            plt.legend([legend_label])
            plt.show()
