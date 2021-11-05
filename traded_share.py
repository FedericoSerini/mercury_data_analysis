from utils import trades_utils
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def traded_share(period):
    trades = trades_utils.get_all_trades_plain()
    trades['value'] = trades.quantity.mul(trades.price)
    trades['value_share'] = trades.value.div(trades.value.sum())

    trade_summary = trades.groupby('symbol').value_share.sum().sort_values(ascending=False)
    trade_summary.iloc[:50].plot.bar(figsize=(14, 6), color='darkblue', title='Share of Traded Value | '+period)
    f = lambda y, _: '{:.0%}'.format(y)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(f))
    plt.show()


traded_share('2021-10-19')