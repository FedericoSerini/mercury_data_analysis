from utils import dataset_utils
import pandas as pd
from technical_indicators.adx import Adx
from technical_indicators.rsi import Rsi
from technical_indicators.bbands import BBands


look_back = 14
dataset = dataset_utils.Dataset(dataset_filename='../data/2021-9-21.csv')
trades = dataset.get_trades_with_timestamp_index("BTCEUR")
resampled = trades.groupby(pd.Grouper(freq='1Min'))
olhc_data = dataset.get_ohlc(resampled)

adx = Adx(look_back=look_back, original_data=olhc_data, should_plot=True)
adx.calculate_adx()

rsi = Rsi(look_back=look_back, original_data=olhc_data, should_plot=True)
rsi.calculate_rsi_by_sma()

bbands = BBands(look_back=look_back, original_data=trades, olhc_data=olhc_data, should_plot=True)
bbands.calculate_bbands()
