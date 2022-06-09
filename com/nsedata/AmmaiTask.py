# This code gets the February, March, April, May, June, July and August high values data and saves it to google sheet

import datetime
from datetime import date
from nsepy import get_history
import nsepy as nse
#from nsedata import GSReader
from CourseraPython.com.nsedata import GSReader


def get_month_high_value(equity_name, start_date, end_date):
    data = get_history(symbol=equity_name, start=start_date, end=end_date)
    high_vals = list(data['High'])
    if len(high_vals) == 0:
        return 0
    high_val = highValue(price_list=high_vals)
    return high_val


def highValue(price_list):
    high_value = price_list[0]
    for value in price_list:
        if high_value < value:
            high_value = value
    return high_value


def getLatestPrice(equity_name) :
    q = nse.get_quote(equity_name)
    latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    return float(latest_price)


nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL']

nse_shares_info_list = list()
#nseShareNames = list()
for equity_name in nseShareNames:
    print(equity_name)
    feb_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 2, 1),  datetime.datetime(2021, 2, 28))
    mar_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 3, 1),  datetime.datetime(2021, 3, 31))
    apr_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 4, 1),  datetime.datetime(2021, 4, 30))
    may_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 5, 1),  datetime.datetime(2021, 5, 31))
    june_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 6, 1),  datetime.datetime(2021, 6, 30))
    july_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 7, 1),  datetime.datetime(2021, 7, 31))
    aug_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 8, 1),  datetime.datetime(2021, 8, 31))
    sep_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 9, 1),  datetime.datetime(2021, 9, 30))
    oct_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 10, 1),  datetime.datetime(2021, 10, 31))
    nov_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 11, 1),  datetime.datetime(2021, 11, 30))
    dec_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 12, 1),  datetime.datetime(2021, 12, 31))
    jan_max_val = get_month_high_value(equity_name, datetime.datetime(2022, 1, 1),  datetime.datetime(2022, 1, 31))
    feb_1_max_val = get_month_high_value(equity_name, datetime.datetime(2022, 2, 1),  datetime.datetime(2022, 3, 2))
    #latest_price = getLatestPrice(equity_name)

    high_list = [feb_max_val, mar_max_val, apr_max_val, may_max_val, june_max_val, july_max_val, aug_max_val,
                sep_max_val, oct_max_val, nov_max_val, dec_max_val, jan_max_val, feb_1_max_val]
    max_price = highValue(high_list)
    latest_price = getLatestPrice(equity_name)
    percent_change = round(((max_price - latest_price) / max_price * 100), 2)
    nse_shares_info_list.append([equity_name, latest_price, max_price, percent_change])
GSReader.updateShareData(nse_shares_info_list)


nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']

nse_next50_shares_info_list = list()
for equity_name in nseNext50shareNames:
    print(equity_name)
    feb_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 2, 1),  datetime.datetime(2021, 2, 28))
    mar_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 3, 1),  datetime.datetime(2021, 3, 31))
    apr_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 4, 1),  datetime.datetime(2021, 4, 30))
    may_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 5, 1),  datetime.datetime(2021, 5, 31))
    june_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 6, 1),  datetime.datetime(2021, 6, 30))
    july_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 7, 1),  datetime.datetime(2021, 7, 31))
    aug_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 8, 1),  datetime.datetime(2021, 8, 31))
    sep_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 9, 1),  datetime.datetime(2021, 9, 30))
    oct_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 10, 1),  datetime.datetime(2021, 10, 31))
    nov_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 11, 1),  datetime.datetime(2021, 11, 30))
    dec_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 12, 1),  datetime.datetime(2021, 12, 31))
    jan_max_val = get_month_high_value(equity_name, datetime.datetime(2022, 1, 1),  datetime.datetime(2022, 1, 31))
    feb_1_max_val = get_month_high_value(equity_name, datetime.datetime(2022, 2, 1),  datetime.datetime(2022, 3, 2))

    high_list = [feb_max_val, mar_max_val, apr_max_val, may_max_val, june_max_val, july_max_val, aug_max_val,
                sep_max_val, oct_max_val, nov_max_val, dec_max_val, jan_max_val, feb_1_max_val]
    max_price = highValue(high_list)
    latest_price = getLatestPrice(equity_name)
    percent_change = round(((max_price - latest_price) / max_price * 100), 2)
    nse_next50_shares_info_list.append([equity_name, latest_price, max_price, percent_change])

GSReader.updateShareData(nse_next50_shares_info_list)
'''
nse_midcap_data = ['PRESTIGE', 'GMRINFRA', 'APOLLOHOSP', 'TATACOMM', 'FRETAIL', 'IDBI', 'SUPREMEIND',
                   'ESCORTS', 'RAMCOCEM', 'SAIL', 'APOLLOTYRE', 'MPHASIS', 'ASHOKLEY', 'BHEL', 'SCHAEFFLER',
                   'JINDALSTEL', 'CHOLAFIN', 'ISEC', 'NAM-INDIA', 'EMAMILTD', 'BHARATFORG', 'HUDCO',
                   'SUNTV', 'QUESS', 'VBL', 'IDFCFIRSTB', 'SUMICHEM', 'TVSMOTOR', 'CESC', 'DALBHARAT',
                   'MFSL', 'CROMPTON', 'AARTIIND',  'THERMAX', 'ERIS', 'GODREJAGRO',
                   'IOB', 'AUBANK', 'HAL', 'CUMMINSIND', 'MRPL', 'LTTS', 'RBLBANK', 'TTKPRESTIG', 'SUNDRMFAST',
                   'TATACONSUM', 'APLLTD', 'AMARAJABAT', 'NATIONALUM', 'ATUL', 'CASTROLIND', 'BAYERCROP',
                   'GODREJPROP', 'ALKEM', 'JUBLFOOD', 'CANBK', 'GLAXO', 'ADANIGAS', 'JKCEMENT', 'HEXAWARE',
                   'ADANIPOWER', 'IBVENTURES', 'CREDITACC', 'MRF', 'MOTILALOFS', 'UCOBANK', 'LICHSGFIN',
                   'FORTIS', 'SHRIRAMCIT', 'INDHOTEL', 'SYMPHONY', 'SYNGENE', 'JSWENERGY', 'GILLETTE', 'GUJGASLTD',
                   'ABB', 'ASTRAL', 'SUNDARMFIN', 'GODREJIND', 'NLCINDIA', 'SRF', 'WABCOINDIA',
                   'CHOLAHLDNG', 'CENTRALBK', 'HONAUT', 'POLYCAB', 'TORNTPOWER', 'PIIND', '3MINDIA', 'ENDURANCE',
                   'EXIDEIND', 'MANAPPURAM', 'MINDTREE', 'IPCALAB', 'VINATIORGA', 'TRENT', 'LALPATHLAB',
                   'SJVN', 'LTI', 'JUBILANT', 'SOLARINDS', 'NIACL', 'MGL', 'WHIRLPOOL', 'NATCOPHARM', 'RECLTD',
                   'BLUEDART', 'BALKRISIND', 'BANKINDIA', 'VGUARD', 'EIHOTEL', 'FEDERALBNK', 'GLENMARK', 'HATSUN',
                   'CUB', 'BATAINDIA', 'PFIZER', 'KANSAINER', 'TATAPOWER', 'OIL', 'PHOENIXLTD', 'ADANIGREEN',
                   'RAJESHEXPO', 'GSPL', 'AAVAS', 'RELAXO', 'IIFLWAM', 'VOLTAS', 'UNIONBANK', 'ABCAPITAL', 'SANOFI',
                   'ABFRL', 'PNBHOUSING', 'CRISIL', 'MINDAIND', 'COROMANDEL', 'AJANTPHARM', 'OBEROIRLTY', 'AIAENG',
                   'BEL', 'SKFINDIA', 'EDELWEISS']
nse_midcap_shares_info_list = list()
for equity_name in nse_midcap_data:
    print(equity_name)
    feb_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 2, 1),  datetime.datetime(2021, 2, 28))
    mar_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 3, 1),  datetime.datetime(2021, 3, 31))
    apr_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 4, 1),  datetime.datetime(2021, 4, 30))
    may_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 5, 1),  datetime.datetime(2021, 5, 31))
    june_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 6, 1),  datetime.datetime(2021, 6, 30))
    july_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 7, 1),  datetime.datetime(2021, 7, 31))
    aug_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 8, 1),  datetime.datetime(2021, 8, 31))
    sep_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 9, 1),  datetime.datetime(2021, 9, 30))
    oct_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 10, 1),  datetime.datetime(2021, 10, 31))
    nov_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 11, 1),  datetime.datetime(2021, 11, 30))
    dec_max_val = get_month_high_value(equity_name, datetime.datetime(2021, 12, 1),  datetime.datetime(2021, 12, 31))
    jan_max_val = get_month_high_value(equity_name, datetime.datetime(2022, 1, 1),  datetime.datetime(2022, 1, 31))
    feb_1_max_val = get_month_high_value(equity_name, datetime.datetime(2022, 2, 1),  datetime.datetime(2022, 2, 23))

    high_list = [feb_max_val, mar_max_val, apr_max_val, may_max_val, june_max_val, july_max_val, aug_max_val,
                sep_max_val, oct_max_val, nov_max_val, dec_max_val, jan_max_val, feb_1_max_val]
    max_price = highValue(high_list)
    latest_price = getLatestPrice(equity_name)
    percent_change = round(((max_price - latest_price) / max_price * 100), 2)
    nse_midcap_shares_info_list.append([equity_name, latest_price, max_price, percent_change])

GSReader.updateShareData(nse_midcap_shares_info_list) '''
