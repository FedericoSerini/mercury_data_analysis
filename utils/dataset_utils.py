import pandas as pd


class Dataset:
    def __init__(self, dataset_filename):
        self.filename = dataset_filename

    def get_trades_with_timestamp_index(self, symbol):
        store = pd.read_csv(self.filename, delimiter=';')
        trades = store[['symbol', 'price', 'event_time', 'quantity']]
        trades = trades.loc[trades['symbol'] == symbol]

        trades['event_time'] = pd.to_datetime(trades['event_time'], unit="ms")
        trades = trades.rename(columns={"quantity": "shares", "event_time": "timestamp"})

        trades = trades.set_index('timestamp')
        return trades

    def get_all_trades_plain_with_timestamp_index(self):
        store = pd.read_csv(self.filename, delimiter=';')
        trades = store[['symbol', 'price', 'event_time', 'quantity']]
        trades['event_time'] = pd.to_datetime(trades['event_time'], unit="ms")
        trades = trades.rename(columns={"quantity": "shares", "event_time": "timestamp"})
        trades = trades.set_index('timestamp')
        return trades

    def get_all_trades_plain_with_symbol_index(self):
        store = pd.read_csv(self.filename, delimiter=';')
        trades = store[['symbol', 'price', 'event_time', 'quantity']]
        trades = trades.set_index('symbol')
        return trades

    def get_all_trades_plain(self):
        store = pd.read_csv(self.filename, delimiter=';')
        trades = store[['symbol', 'price', 'event_time', 'quantity']]
        return trades

    def get_full_trades(self, symbol):
        trades = pd.read_csv(self.filename, delimiter=';')
        trades = trades.loc[trades['symbol'] == symbol]
        trades = trades.set_index('date')
        return trades

    def get_vol(self, agg_trades):
        return agg_trades.shares.sum().to_frame('vol')

    def get_txn(self, agg_trades):
        return agg_trades.shares.size().to_frame('txn')

    def get_ohlc(self, agg_trades):
        return agg_trades.price.ohlc()

    def get_ohlcv(self, agg_trades):
        ohlcv = agg_trades.price.ohlc()
        ohlcv['volume'] = self.get_vol(agg_trades)
        return ohlcv
