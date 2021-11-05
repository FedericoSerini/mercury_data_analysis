import pandas as pd


def get_trades_with_timestamp_index(symbol):
    store = pd.read_csv('/Users/federicoserini/WebstormProjects/binance_socket/resources/2021-9-21.csv', delimiter=';')
    trades = store[['symbol', 'price', 'event_time', 'quantity']]
    trades = trades.loc[trades['symbol'] == symbol]

    trades['event_time'] = pd.to_datetime(trades['event_time'], unit="ms")
    trades = trades.rename(columns={"quantity": "shares", "event_time": "timestamp"})

    trades = trades.set_index('timestamp')
    return trades


def get_all_trades_plain_with_timestamp_index():
    store = pd.read_csv('/Users/federicoserini/WebstormProjects/binance_socket/resources/2021-9-19.csv', delimiter=';')
    trades = store[['symbol', 'price', 'event_time', 'quantity']]
    trades['event_time'] = pd.to_datetime(trades['event_time'], unit="ms")
    trades = trades.rename(columns={"quantity": "shares", "event_time": "timestamp"})
    trades = trades.set_index('timestamp')
    return trades


def get_all_trades_plain_with_symbol_index():
    store = pd.read_csv('/Users/federicoserini/WebstormProjects/binance_socket/resources/2021-9-19.csv', delimiter=';')
    trades = store[['symbol', 'price', 'event_time', 'quantity']]
    trades = trades.set_index('symbol')
    return trades


def get_all_trades_plain():
    store = pd.read_csv('/Users/federicoserini/WebstormProjects/binance_socket/resources/2021-9-19.csv', delimiter=';')
    trades = store[['symbol', 'price', 'event_time', 'quantity']]
    return trades
