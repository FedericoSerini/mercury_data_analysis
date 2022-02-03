import pandas as pd

class Psar:

    
    def __init__(self, original_data, should_plot):
        self.data = original_data.copy()
        self.should_plot = should_plot

    def calculate_psar(self, iaf: int = 0.02, maxaf: int = 0.2):
        data = self.data
        length = len(data)
        high, low, close = data.high, data.low, data.close
        psar = close[0 : len(close)]
        psarbull = [None] * length
        psarbear = [None] * length
        bull = True
        af = iaf
        hp = high[0]
        lp = low[0]

        for i in range(2, length):
            if bull:
                psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
            else:
                psar[i] = psar[i - 1] + af * (lp - psar[i - 1])

            reverse = False

            if bull:
                if low[i] < psar[i]:
                    bull = False
                    reverse = True
                    psar[i] = hp
                    lp = low[i]
                    af = iaf
            else:
                if high[i] > psar[i]:
                    bull = True
                    reverse = True
                    psar[i] = lp
                    hp = high[i]
                    af = iaf

            if not reverse:
                if bull:
                    if high[i] > hp:
                        hp = high[i]
                        af = min(af + iaf, maxaf)
                    if low[i - 1] < psar[i]:
                        psar[i] = low[i - 1]
                    if low[i - 2] < psar[i]:
                        psar[i] = low[i - 2]
                else:
                    if low[i] < lp:
                        lp = low[i]
                        af = min(af + iaf, maxaf)
                    if high[i - 1] > psar[i]:
                        psar[i] = high[i - 1]
                    if high[i - 2] > psar[i]:
                        psar[i] = high[i - 2]

            if bull:
                psarbull[i] = psar[i]
            else:
                psarbear[i] = psar[i]

        psar = pd.Series(psar, name="psar", index=data.index)
        psar = psar.fillna(method='bfill')
        self.plot_psar(psar)
        psar = psar.shift(1)/data.close
        return psar

    def plot_psar(self, psar):
        if self.should_plot:
            import matplotlib.pyplot as plt
            legend_label = 'PSAR'
            psar.plot()
            plt.legend([legend_label])
            plt.show()

