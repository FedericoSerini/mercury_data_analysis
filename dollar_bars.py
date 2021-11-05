import pandas as pd
from utils import trades_utils, price_volume_utils, bar_stats_utils


def get_dollar_bars(symbol, period):
    trades = trades_utils.get_trades_with_timestamp_index(symbol)
    value_per_min = trades.shares.mul(trades.price).sum()/(60*7.5) # min per trading day
    trades['cumul_val'] = trades.shares.mul(trades.price).cumsum()
    df = trades.reset_index()
    by_value = df.groupby(df.cumul_val.div(value_per_min).round().astype(int))
    dollar_bars = pd.concat([by_value.timestamp.last().to_frame('timestamp'), bar_stats_utils.get_bar_stats(by_value)], axis=1)
    plot_to_show = price_volume_utils.price_volume(dollar_bars.set_index('timestamp'),
             'Dollar Bars | '+symbol+' | '+period)
    plot_to_show.show()


get_dollar_bars('BTCEUR', '2021-10-19')
get_dollar_bars('SOLEUR', '2021-10-19')
