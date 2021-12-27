from utils import dataset_utils
from logger.logger import Logger
import pandas as pd
from technical_indicators.adx import Adx
from technical_indicators.rsi import Rsi
from technical_indicators.bbands import BBands
from technical_indicators.trima import Trima
from technical_indicators.vwap import Vwap
from technical_indicators.obv import Obv
from technical_indicators.ema import Ema
from technical_indicators.ad import Ad
from technical_indicators.stoch import Stoch
from technical_indicators.dema import Dema
from technical_indicators.tema import Tema


class TechnicalIndicatorsCalculator:
    
    def __init__(self):
        self.log = Logger(TechnicalIndicatorsCalculator.__name__).get_log()
        self.look_back = 11
        dataset = dataset_utils.Dataset(dataset_filename='data/BTCUSDT_d.csv')
        self.trades = dataset.get_full_trades("BTCUSDT")
        #self.adx = Adx(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.rsi = Rsi(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #self.bbands = BBands(look_back=self.look_back, original_data=self.trades, olhc_data=self.trades, should_plot=False)
        #self.trima = Trima(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #self.vwap = Vwap(original_data=self.trades, should_plot=False)
        #self.obv = Obv(original_data=self.trades, should_plot=False)
        self.ema = Ema(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #self.dema = Dema(look_back=self.look_back, original_data=self.trades, should_plot=False)
        self.tema = Tema(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #self.ad = Ad(original_data=self.trades, should_plot=False)
        #self.stoch = Stoch(look_back=self.look_back, original_data=self.trades, should_plot=False)
        #WilliamsRIndicator - cls
        #WMAIndicator - cls
        #SMAIndicator - cls
        #HMAIndicator - cls
        #CCIIndicator - cls
        #CMOIndicator - cls
        #MACDIndicator - cls
        #PPOIndicator - cls
        #ROCIndicator - cls
        #ChaikinMoneyFlowIndicator
        #DirectionalMovementIndicator - cls
        #ParabolicSarIndicator - cls
        self.ml_data = self.trades.copy()

    def calculate(self):
        self.log.info("Start Technical Indicators Calculus")

        #self.log.info("ADX Calculus..")
        #self.ml_data['adx'] = self.adx.calculate_adx()

        self.log.info("RSI Calculus..")
        self.ml_data['rsi'] = self.rsi.calculate_rsi_by_sma()

        #self.log.info("BBANDS Calculus..")
        #self.bbands.calculate_bbands()

        #self.log.info("TRIMA Calculus..")
        #self.ml_data['trima'] = self.trima.calculate_trima()
        #self.ml_data['vwap'] = self.vwap.calculate_vwap() TODO fix

        self.log.info("OBV Calculus..")
        #self.ml_data['obv'] = self.obv.calculate_obv()

        self.log.info("TEMA Calculus..")
        self.ml_data['tema'] = self.tema.calculate_tema()

        self.log.info("AD Calculus..")
        #self.ml_data['ad'] = self.ad.calculate_ad()

        self.log.info("STOCH Calculus..")
        #self.ml_data['stoch'] = self.stoch.calculate_stoch()

        self.log.info("End Technical Indicators Calculus")
        return self.ml_data
