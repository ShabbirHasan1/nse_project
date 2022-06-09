import pandas_datareader.data as web
import quandl

quandl.ApiConfig.api_key = 'Wer3xy6taUFJokWCSkMS'
#quandl.ApiConfig.api_version = '2015-04-09'
#quandl.ApiConfig.verify_ssl = False


tickers = ['EURUSD', 'USDCAD', 'AUDUSD', 'AUDJPY', 'EURJPY', 'EURNZD', 'GBPAUD', 'GBPUSD', 'NZDUSD', 'USDJPY', 'AUDCAD',
           'AUDCHF', 'AUDNZD', 'CADCHF', 'CADJPY', 'EURAUD', 'AURCAD', 'EURCHF', 'EURGBP', 'GBPCAD', 'EURCAD', 'EURCHF',
           'EURGBP', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'NZDJPY', 'USDCHF']

#mydata = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")

start_date = '2020-7-24'
end_date = '2020-8-6'
# FXCM/H1
#data = quandl.get("EUR/USD", start_date=start_date, end_date=end_date, returns="numpy")
data = quandl.get_table('FXCM/H1', date='2017-07-02', symbol='EUR/CAD')
#conversion_data = quandl.get('ECB/EURUSD', start = '2015-01-01', end='2015-01-05')
conversion_data = web.DataReader('ECB/EURUSD', data_source='quandl', start = '2020-08-01', end='2020-08-06', api_key='Wer3xy6taUFJokWCSkMS')
print(conversion_data.head(5))
#print(conversion_data.Open)
#print(type(conversion_data))

print(conversion_data.loc['2015-01-02'])

#print(data)
