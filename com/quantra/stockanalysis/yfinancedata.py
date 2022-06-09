import yfinance as yf
import csv
from datetime import date

data = yf.download('AAPL', start='2020-06-01', end='2020-06-10')
print(data.head())

