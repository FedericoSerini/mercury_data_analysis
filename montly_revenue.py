import pandas as pd
import pandas_datareader.data as web
from utils import trades_utils
from pyfinance.ols import PandasRollingOLS


trades = trades_utils.get_trades_with_timestamp_index('BTCEUR')
monthly_prices = trades.price.resample('T').last()

outlier_cutoff = 0.01
data = pd.DataFrame()
lags = [1, 2, 3, 6, 9, 12]

for lag in lags:
    print(monthly_prices.head())
    monthly_prices = monthly_prices.pct_change(lag).dropna()
    print(monthly_prices.head())
    data[f'return_{lag}m'] = (monthly_prices
                              ##.stack()
                              .pipe(lambda x:
                                    x.clip(lower=x.quantile(outlier_cutoff),
                                           upper=x.quantile(1 - outlier_cutoff)))
                              .add(1)
                              .pow(1 / lag)
                              .sub(1))

data = data.dropna()
data.info()


for lag in [2, 3, 6, 9, 12]:
    data[f'momentum_{lag}'] = data[f'return_{lag}m'].sub(data.return_1m)
    data[f'momentum_3_12'] = data[f'return_12m'].sub(data.return_3m)
    print(data.head())

for t in range(1, 7):
    data[f'return_1m_t-{t}'] = data.groupby(level='timestamp').return_1m.shift(t)
    print(data.head())

for t in [1, 2 , 3, 6, 12]:
    data[f'target_{t}m'] = (data.groupby(level='timestamp') [f'return_{t}m'].shift(-t))
    print(data.head())


factors = ['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA']
factor_data = web.DataReader('F-F_Research_Data_5_Factors_2x3', 'famafrench', start='2000')[0].drop('RF', axis=1)
factor_data.index = factor_data.index.to_timestamp()
factor_data = factor_data.resample('M').last().div(100)
factor_data.index.name = 'date'
factor_data = factor_data.join(data['return_1m']).sort_index()
T = 24
betas = (factor_data
         .groupby(level='ticker', group_keys=False)
         .apply(lambda x: PandasRollingOLS(window=min(T, x.shape[0]-1), y=x.return_1m, x=x.drop('return_1m', axis=1)).beta))
