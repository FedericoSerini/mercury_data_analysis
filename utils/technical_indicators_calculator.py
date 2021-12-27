from utils import dataset_utils
from logger.logger import Logger
import pandas as pd
from technical_indicators.adx import Adx

from technical_indicators.cci import Cci
from technical_indicators.cmo import Cmo
from technical_indicators.dmi import Dmi
from technical_indicators.ema import Ema
from technical_indicators.hma import Hma
from technical_indicators.roc import Roc
from technical_indicators.rsi import Rsi
from technical_indicators.bbands import BBands
from technical_indicators.trima import Trima
from technical_indicators.vwap import Vwap
from technical_indicators.obv import Obv

from technical_indicators.ad import Ad
from technical_indicators.stoch import Stoch
from utils.statistics.sma import Sma
from technical_indicators.dema import Dema
from technical_indicators.tema import Tema
from technical_indicators.williams import Williams
from technical_indicators.wma import Wma


class TechnicalIndicatorsCalculator:
    
    def __init__(self):
        self.log = Logger(TechnicalIndicatorsCalculator.__name__).get_log()
        self.look_back = 11
        dataset = dataset_utils.Dataset(dataset_filename='data/BTCUSDT_d.csv')
        self.trades = dataset.get_full_trades("BTCUSDT")

        self.cci = Cci(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.cmo = Cmo(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.dmi = Dmi(look_back=self.look_back, original_data=self.trades)
        self.hma = Hma(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.roc = Roc(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.rsi = Rsi(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.sma = Sma(look_back=self.look_back)
        self.ema = Ema(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.tema = Tema(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.williams = Williams(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.wma = Wma(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #MACDIndicator -  review
        #PPOIndicator - review
        #ChaikinMoneyFlowIndicator
        #ParabolicSarIndicator - review
        self.ml_data = self.trades.copy()

    def calculate(self):
        self.log.info("Start Technical Indicators Calculus")

        self.log.info("CCI Calculus..")
        self.ml_data['cci'] = self.cci.calculate_cci()

        self.log.info("CMO Calculus..")
        self.ml_data['cmo'] = self.cmo.calculate_cmo()

        self.log.info("DMI Calculus..")
        self.ml_data['dmi'] = self.dmi.calculate_dmi()

        self.log.info("HMA Calculus..")
        self.ml_data['hma'] = self.hma.calculate_hma()

        self.log.info("ROC Calculus..")
        self.ml_data['roc'] = self.roc.calculate_roc()

        self.log.info("RSI Calculus..")
        self.ml_data['rsi'] = self.rsi.calculate_rsi_by_sma()

        self.log.info("SMA Calculus..")
        self.ml_data['sma'] = self.sma.calculate_sma(data=self.trades.close)

        self.log.info("TEMA Calculus..")
        self.ml_data['tema'] = self.tema.calculate_tema()

        self.log.info("Williams %R Calculus..")
        self.ml_data['williams'] = self.williams.calculate_williams()

        self.log.info("WMA Calculus..")
        self.ml_data['wma'] = self.wma.calculate_wma(self.look_back)

        self.log.info("End Technical Indicators Calculus")
        return self.ml_data

    # self.adx = Adx(look_back=self.look_back, original_data=self.trades, should_plot=False)
    # self.bbands = BBands(look_back=self.look_back, original_data=self.trades, olhc_data=self.trades, should_plot=False)
    # self.dema = Dema(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #self.ad = Ad(original_data=self.trades, should_plot=False)
        #self.stoch = Stoch(look_back=self.look_back, original_data=self.trades, should_plot=False)
    # self.trima = Trima(look_back=self.look_back, original_data=self.trades, should_plot=False)
    # self.vwap = Vwap(original_data=self.trades, should_plot=False)
    # self.obv = Obv(original_data=self.trades, should_plot=False)



    # self.log.info("AD Calculus..")
    # self.ml_data['ad'] = self.ad.calculate_ad()

    # self.log.info("STOCH Calculus..")
    # self.ml_data['stoch'] = self.stoch.calculate_stoch()

    # self.log.info("ADX Calculus..")
    # self.ml_data['adx'] = self.adx.calculate_adx()

    #self.log.info("BBANDS Calculus..")
        #self.bbands.calculate_bbands()

        #self.log.info("TRIMA Calculus..")
        #self.ml_data['trima'] = self.trima.calculate_trima()
        #self.ml_data['vwap'] = self.vwap.calculate_vwap() TODO fix

        #self.log.info("OBV Calculus..")
        #self.ml_data['obv'] = self.obv.calculate_obv()