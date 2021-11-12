import datetime

from utils import dataset_utils
import pandas as pd
from technical_indicators.adx import Adx
from technical_indicators.rsi import Rsi
from technical_indicators.bbands import BBands
from technical_indicators.trima import Trima
from technical_indicators.vwap import Vwap
from technical_indicators.obv import Obv
from technical_indicators.ema import Ema

look_back = 14
dataset = dataset_utils.Dataset(dataset_filename='data/2021-9-21.csv')
trades = dataset.get_trades_with_timestamp_index("BTCEUR")
resampled = trades.groupby(pd.Grouper(freq='1Min'))
olhc_data = dataset.get_ohlc(resampled)
olhcv_data = dataset.get_ohlcv(resampled)

start = datetime.datetime.now()

adx = Adx(look_back=look_back, original_data=olhc_data, should_plot=True)
adx.calculate_adx()

rsi = Rsi(look_back=look_back, original_data=olhc_data, should_plot=True)
rsi.calculate_rsi_by_sma()

bbands = BBands(look_back=look_back, original_data=trades, olhc_data=olhc_data, should_plot=True)
bbands.calculate_bbands()

trima = Trima(look_back=look_back, original_data=olhc_data, should_plot=True)
trima.calculate_trima()

vwap = Vwap(original_data=trades, should_plot=True)
vwap.calculate_vwap()

obv = Obv(original_data=olhcv_data, should_plot=True)
obv.calculate_obv()

ema = Ema(look_back=look_back, original_data=olhc_data, should_plot=True)
ema.calculate_ema()

end = datetime.datetime.now()
print(end-start)