import quandl
from datetime import datetime

from quantrautil import get_quantinsti_api_key
api_key = 'Wer3xy6taUFJokWCSkMS'#get_quantinsti_api_key()

data = quandl.get('EOD/AAPL', start_date='2017-06-01', end_date='2017-06-30', api_key = api_key)
print(data.head())
