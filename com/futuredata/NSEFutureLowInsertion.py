import datetime
from nsepy import get_history
from CourseraPython.com.nsedata import GSReader


def populate_future_least_values():
    start_date = datetime.datetime(2020, 10, 30)
    end_date = datetime.datetime(2020, 11, 26)

    nse_future_info_list = list()
    for future_name in nse_future_names:
        data = get_future_data(future_name=future_name, start_date=start_date, end_date=end_date)
        low_vals = list(data['Low'])
        least_val = least_value(price_list=low_vals)

        nse_future_info_list.append([future_name, least_val])

    GSReader.updateFutureData(nse_future_info_list)


def least_value(price_list) :
    low_value = price_list[0]
    for value in price_list :
        if low_value > value :
            low_value = value
    return low_value


def get_future_data(future_name, start_date, end_date):
    print(future_name)
    data = get_history(symbol=future_name, start=start_date, end=end_date, futures=True, expiry_date=end_date)
    return data


nse_future_names = ['ACC','ADANIENT','ADANIPORTS', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'BOSCHLTD', 'ASHOKLEY',
                 'CHOLAFIN', 'AUROPHARMA', 'AXISBANK', 'AMARAJABAT', 'BAJAJFINSV', 'BAJFINANCE', 'DRREDDY', 'BALKRISIND',
                 'BANDHANBNK', 'BANKBARODA', 'GODREJCP', 'BEL', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BRITANNIA',
                 'CADILAHC', 'CANBK', 'CIPLA', 'HEROMOTOCO', 'HINDPETRO', 'COALINDIA', 'IOC', 'COFORGE', 'LUPIN', 'COLPAL',
                 'CONCOR', 'CUMMINSIND', 'DIVISLAB', 'DLF', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL',
                 'GLENMARK', 'GMRINFRA', 'GODREJPROP', 'GRASIM', 'BAJAJ-AUTO', 'HCLTECH', 'HINDUNILVR', 'IBULHSGFIN',
                 'ICICIBANK', 'HAVELLS', 'IDEA', 'IDFCFIRSTB', 'IGL', 'INDIGO', 'INDUSINDBK', 'INFRATEL', 'INFY', 'ITC',
                 'JINDALSTEL', 'ICICIGI', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'PFC', 'LICHSGFIN', 'LT', 'M&M',
                 'M&MFIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'RECLTD', 'MINDTREE', 'MOTHERSUMI',
                 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'RELIANCE', 'NAUKRI', 'NESTLEIND', 'NMDC', 'NTPC', 'SRTRANSFIN',
                 'ONGC', 'VOLTAS', 'PAGEIND', 'PEL', 'PETRONET', 'PIDILITIND', 'PNB', 'PVR', 'RBLBANK', 'SAIL', 'SBIN',
                 'SHREECEM', 'SIEMENS', 'SRF', 'SUNTV', 'TATACHEM', 'TATACONSUM', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM',
                 'TORNTPHARM', 'TORNTPOWER', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'WIPRO', 'ZEEL', 'ASIANPAINT',
                 'BATAINDIA', 'BERGEPAINT', 'BHEL', 'HDFC', 'HDFCLIFE', 'BPCL', 'DABUR', 'POWERGRID', 'RAMCOCEM',
                 'HDFCBANK', 'HINDALCO', 'ICICIPRULI', 'MGL', 'SBILIFE', 'SUNPHARMA', 'TATAMOTORS', 'TITAN',]


populate_future_least_values()
# November Data
#data = get_future_data(datetime.datetime(2020, 10, 30), datetime.datetime(2020, 11, 26))
# December Data
#data = data.append(get_future_data(datetime.datetime(2020, 11, 27), datetime.datetime(2020, 12, 31)))
