import pandas as pd
from pandas_datareader import data

data1 = data.get_data_yahoo('AAPL', '2017-01-01', '2018-01-01')
data1.head()