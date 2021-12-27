import datetime


from utils import dataset_utils
import pandas as pd
from utils.technical_indicators_calculator import TechnicalIndicatorsCalculator
from utils.machine_learning_dataset_creator import MachineLearningDataset


look_back = 11
dataset = dataset_utils.Dataset(dataset_filename='data/BTCUSDT_d.csv')
trades = dataset.get_full_trades("BTCUSDT")

start = datetime.datetime.now()

mlds = MachineLearningDataset(trades, look_back)
buy_sell_label = mlds.prepare_data_for_ml()

tic = TechnicalIndicatorsCalculator()
a = tic.calculate()
res = buy_sell_label.join(a)
res.drop(['open', 'high', 'low', 'volume_fiat', 'volume_cry', 'trade_count', 'timestamp', 'symbol'], axis=1, inplace=True)

end = datetime.datetime.now()
