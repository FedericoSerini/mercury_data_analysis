import datetime

from utils import dataset_utils
from utils.technical_indicators_calculator import TechnicalIndicatorsCalculator
from utils.machine_learning_dataset_creator import MachineLearningDataset

symbol = ["BTCUSDT", "ETHUSDT", "LTCUSDT", "DOGEUSDT", "NEOUSDT", "BNBUSDT", "XRPUSDT", "LINKUSDT", "EOSUSDT",
          "TRXUSDT", "ETCUSDT", "XLMUSDT", "ZECUSDT", "ADAUSDT", "QTUMUSDT", "DASHUSDT", "XMRUSDT", "BTTUSDT"]


def start():
    start = datetime.datetime.now()

    for sim in symbol:
        look_back = 11
        dataset = dataset_utils.Dataset(dataset_filename='../mercury/'+sim+'_d.csv')
        trades = dataset.get_full_trades(symbol=sim)

        mlds = MachineLearningDataset(trades, look_back)
        buy_sell_label = mlds.prepare_data_for_ml()

        tic = TechnicalIndicatorsCalculator()
        a = tic.calculate()
        res = buy_sell_label.join(a)
        res.drop(['open', 'high', 'low', 'volume_fiat', 'volume_cry', 'trade_count', 'timestamp', 'symbol'], axis=1, inplace=True)
        res.to_csv(path_or_buf="../mercury/"+sim+".csv", header=None, index=False)

    end = datetime.datetime.now()
    execution_time = str(end-start)

    return {'exec-time': execution_time, 'ticker': symbol, 'granularity': 'day',
            'resource': '../mercury/res.csv'}
