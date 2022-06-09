import nsepy as nse
import datetime
from datetime import date
from CourseraPython.com.nsedata import GSReader
from nsepy import get_history


def get_latest_price(future_name):
    q = nse.get_quote(future_name, instrument='FUTSTK', expiry=datetime.datetime(2021, 2, 25))
    latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    return float(latest_price)


def get_dec_least_price(future_name):
    dec_fut_start_date = datetime.datetime(2021, 1, 29)
    dec_fut_end_date = datetime.datetime(date.today().year, date.today().month, date.today().day)
    dec_fut_expiry_date = datetime.datetime(2021, 2, 25)

    dec_data = get_future_data(future_name=future_name, start_date=dec_fut_start_date, end_date=dec_fut_end_date,
                               expiry_date=dec_fut_expiry_date)
    low_vals = list(dec_data['Low'])
    return least_value(price_list=low_vals)


def least_value(price_list) :
    low_value = price_list[0]
    for value in price_list :
        if low_value > value :
            low_value = value
    return low_value


def get_future_data(future_name, start_date, end_date, expiry_date):
    #print(future_name, start_date, end_date)
    data = get_history(symbol=future_name, start=start_date, end=end_date, futures=True, expiry_date=expiry_date)
    return data


def print_trade_taken_futures():
    future_data = GSReader.get_november_future_low_price()
    for future_name in nse_future_names:
        print(future_name)
        latest_price = get_latest_price(future_name)
        if future_name == 'L%26TFH' or future_name == 'M%26M' or future_name == 'M%26MFIN':
        #    print(future_name.replace("%26", "&"))
            continue

        nov_least_price = future_data[future_name]
        dec_least_price = get_dec_least_price(future_name)

        if nov_least_price > dec_least_price:
            least_price = dec_least_price
        else:
            least_price = nov_least_price

        trade_price = (least_price * 102)/100
        if latest_price <= trade_price:
            print(future_name, ' ', latest_price)


nse_future_names = ['ACC','ADANIENT','ADANIPORTS', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'BOSCHLTD', 'ASHOKLEY',
                 'CHOLAFIN', 'AUROPHARMA', 'AXISBANK', 'AMARAJABAT', 'BAJAJFINSV', 'BAJFINANCE', 'DRREDDY', 'BALKRISIND',
                 'BANDHANBNK', 'BANKBARODA', 'GODREJCP', 'BEL', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BRITANNIA',
                 'CADILAHC', 'CANBK', 'CIPLA', 'HEROMOTOCO', 'HINDPETRO', 'COALINDIA', 'IOC', 'COFORGE', 'LUPIN', 'COLPAL',
                 'CONCOR', 'CUMMINSIND', 'DIVISLAB', 'DLF', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL',
                 'GLENMARK', 'GMRINFRA', 'GODREJPROP', 'GRASIM', 'BAJAJ-AUTO', 'HCLTECH', 'HINDUNILVR', 'IBULHSGFIN',
                 'ICICIBANK', 'HAVELLS', 'IDEA', 'IDFCFIRSTB', 'IGL', 'INDIGO', 'INDUSINDBK', 'INFRATEL', 'INFY', 'ITC',
                 'JINDALSTEL', 'ICICIGI', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L%26TFH', 'PFC', 'LICHSGFIN', 'LT', 'M%26M',
                 'M%26MFIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'RECLTD', 'MINDTREE', 'MOTHERSUMI',
                 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'RELIANCE', 'NAUKRI', 'NESTLEIND', 'NMDC', 'NTPC', 'SRTRANSFIN',
                 'ONGC', 'VOLTAS', 'PAGEIND', 'PEL', 'PETRONET', 'PIDILITIND', 'PNB', 'PVR', 'RBLBANK', 'SAIL', 'SBIN',
                 'SHREECEM', 'SIEMENS', 'SRF', 'SUNTV', 'TATACHEM', 'TATACONSUM', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM',
                 'TORNTPHARM', 'TORNTPOWER', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'WIPRO', 'ZEEL', 'ASIANPAINT',
                 'BATAINDIA', 'BERGEPAINT', 'BHEL', 'HDFC', 'HDFCLIFE', 'BPCL', 'DABUR', 'POWERGRID', 'RAMCOCEM',
                 'HDFCBANK', 'HINDALCO', 'ICICIPRULI', 'MGL', 'SBILIFE', 'SUNPHARMA', 'TATAMOTORS', 'TITAN',]


#print_latest_price()
print_trade_taken_futures()