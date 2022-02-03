from utils import dataset_utils
from logger.logger import Logger
from technical_indicators.cci import Cci
from technical_indicators.cmo import Cmo
from technical_indicators.dmi import Dmi
from technical_indicators.ema import Ema
from technical_indicators.hma import Hma
from technical_indicators.roc import Roc
from technical_indicators.rsi import Rsi
from technical_indicators.macd import Macd
from technical_indicators.ppo import Ppo
from technical_indicators.psar import Psar
from technical_indicators.cmfi import Cmfi
from utils.statistics.sma import Sma
from technical_indicators.tema import Tema
from technical_indicators.williams import Williams
from technical_indicators.wma import Wma


class TechnicalIndicatorsCalculator:
    
    def __init__(self):
        self.log = Logger(TechnicalIndicatorsCalculator.__name__).get_log()
        dataset = dataset_utils.Dataset(dataset_filename='data/BTCUSDT_d.csv')
        self.trades = dataset.get_full_trades("BTCUSDT")
        self.cci = Cci(original_data=self.trades, should_plot=False)
        self.cmfi = Cmfi(original_data=self.trades, should_plot=False)
        self.cmo = Cmo(original_data=self.trades, should_plot=False)
        self.dmi = Dmi(original_data=self.trades)
        self.hma = Hma(original_data=self.trades, should_plot=False)
        self.macd = Macd(original_data=self.trades, should_plot=False)
        self.ppo = Ppo(original_data=self.trades, should_plot=False)
        self.psar = Psar(original_data=self.trades, should_plot=False)
        self.roc = Roc(original_data=self.trades, should_plot=False)
        self.rsi = Rsi(original_data=self.trades, should_plot=False)
        self.sma = Sma()
        self.ema = Ema(original_data=self.trades, should_plot=False)
        self.tema = Tema(original_data=self.trades, should_plot=False)
        self.williams = Williams(original_data=self.trades, should_plot=False)
        self.wma = Wma(original_data=self.trades, should_plot=False)
        self.ml_data = self.trades.copy()

    def calculate(self):
        self.log.info("Start Technical Indicators Calculus")

        for i in range(5, 20):
            look_back = i+1
            self.ml_data['cci'+str(look_back)] = self.cci.calculate_cci(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['cmfi'+str(look_back)] = self.cmfi.calculate_cmfi(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['cmo'+str(look_back)] = self.cmo.calculate_cmo(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['dmi'+str(look_back)] = self.dmi.calculate_dmi(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['hma'+str(look_back)] = self.hma.calculate_hma(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['macd'+str(look_back)] = self.macd.calculate_macd(look_back, look_back*2)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['ppo'+str(look_back)] = self.ppo.calculate_ppo(look_back, look_back*2)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['psar'+str(look_back)] = self.psar.calculate_psar(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['roc'+str(look_back)] = self.roc.calculate_roc(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['rsi'+str(look_back)] = self.rsi.calculate_rsi_by_sma(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['sma'+str(look_back)] = self.sma.calculate_sma_normalized(data=self.trades.close, look_back=look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['tema'+str(look_back)] = self.tema.calculate_tema(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['williams'+str(look_back)] = self.williams.calculate_williams(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['wma'+str(look_back)] = self.wma.calculate_wma(look_back)

        for i in range(5, 20):
            look_back = i + 1
            self.ml_data['ema' + str(look_back)] = self.ema.calculate_ema_normalized(look_back)

        self.log.info("End Technical Indicators Calculus")
        return self.ml_data
