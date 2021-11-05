import pandas as pd
from utils import trades_utils, price_volume_utils, bar_stats_utils


def get_time_bars(symbol, period):
    trades = trades_utils.get_trades_with_timestamp_index(symbol)
    resampled = trades.groupby(pd.Grouper(freq='1Min'))
    time_bars = bar_stats_utils.get_bar_stats(resampled)
    plot_to_show = price_volume_utils.price_volume(time_bars, "Time Bars | "+symbol+" | "+period)
    plot_to_show.show()


get_time_bars('BTCEUR', '2021-10-19')
get_time_bars('SOLEUR', '2021-10-19')
