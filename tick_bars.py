from utils import trades_utils
import matplotlib.pyplot as plt


def get_tick_bars(symbol, period):
    tick_bars = trades_utils.get_trades_with_timestamp_index(symbol)
    tick_bars.index = tick_bars.index.time
    tick_bars.price.plot(figsize=(10, 5), title="Tick Bars | "+symbol+" | "+period, lw=1)
    #normaltest(tick_bars.price.pct_change().dropna())
    plt.show()


get_tick_bars('BTCEUR', '2021-10-19')
get_tick_bars('SOLEUR', '2021-10-19')
