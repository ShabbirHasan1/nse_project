#   This program will find the low values of november for each future and keep it in dictionary.
#   In december it will catch low value of each future on every day and compare it's November leave value.
#   If the december least value is less than or equal to 1% above the november value then trade triggers.


from CourseraPython.com.nsedata import GSReader
from nsepy import get_history
import datetime
from datetime import date


def get_dec_future_data(future_name):
    start_date = datetime.datetime(2020, 11, 27)
    end_date = datetime.datetime(date.today().year, date.today().month, date.today().day)
    dec_fut_expiry_date = datetime.datetime(2020, 12, 31)

    data = get_history(symbol=future_name, start=start_date, end=end_date, futures=True,
                       expiry_date=dec_fut_expiry_date)
    return data


def print_trade_taken_futures():
    future_data = GSReader.get_november_future_low_price()
    for future_name in nse_future_names:
        if future_name == 'L%26TFH' or future_name == 'M%26M' or future_name == 'M%26MFIN':
        #    print(future_name.replace("%26", "&"))
            continue
        nov_least_price = future_data[future_name]
        dec_data = get_dec_future_data(future_name)
        low_vals = dict(dec_data['Low'])

        for key in low_vals:
            dec_low_val = low_vals[key]
            if dec_low_val < nov_least_price * 1.01:
                print(future_name, ' ', key)


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

print_trade_taken_futures()