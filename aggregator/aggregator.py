
import datetime

import time
from utils import dataset_utils
import pandas as pd

symbol = "BTCEUR"

dataset = dataset_utils.Dataset(dataset_filename='../data/2021-9-21.csv')
trades = dataset.get_full_trades(symbol)
#resampled = trades.groupby(pd.Grouper(freq='0.25Min'))
#olhcv_data = dataset.get_ohlcv(resampled)

today = datetime.date.today()
# today as timestamp
date = str(today.year)+"-"+str(today.month)+"-"+str(today.day)+" 00:00:00"
timestamp = str(time.time())
symbol = symbol
open = str(trades.price[0])
high = str(trades.price.max())
low = str(trades.price.min())
close = str(trades.price.iloc[-1])
volume_cry = str(trades.quantity.sum())  # sum quantity
volume_fiat = str((trades.quantity * trades.price).sum())  # sum quantity * price
trade_count = str(len(trades))  # size

print(timestamp+" "+date+" "+symbol+" "+open+" "+high+" "+low+" "+close+" "+volume_cry+" "+volume_fiat+" "+trade_count)