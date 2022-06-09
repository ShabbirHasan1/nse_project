import nsepy as nse
import datetime


def get_future_live_data(future_name) :
    q = nse.get_quote(symbol = future_name, instrument='FUTSTK', expiry=datetime.datetime(2020, 12, 31))
    #latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    print(q['data'][0])
    return list(q['data'][0]['High'])


print(get_future_live_data('PAGEIND'))