import pandas as pd
from utils import trades_utils, price_volume_utils, bar_stats_utils


def volume_bars(symbol, period):
    trades = trades_utils.get_trades_with_timestamp_index(symbol)
    min_per_trading_day = 60 * 7.5
    trades_per_min = trades.shares.sum() / min_per_trading_day
    trades['cumul_vol'] = trades.shares.cumsum()
    df = trades.reset_index()
    by_vol = (df.groupby(df.cumul_vol.
                     div(trades_per_min)
                     .round().astype(int)))
    vol_bars = pd.concat([by_vol.timestamp.last().to_frame('timestamp'),
                      bar_stats_utils.get_bar_stats(by_vol)], axis=1)
    plot_to_show = price_volume_utils.price_volume(vol_bars.set_index('timestamp'), "Volume Bars | "+symbol+" | "+period)
    plot_to_show.show()


volume_bars('BTCEUR', '2021-10-19')
volume_bars('SOLEUR', '2021-10-19')
