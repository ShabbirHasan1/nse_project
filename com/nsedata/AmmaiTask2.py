# This code picks nifty50, next50 & midcap last one month data and saves the data into google sheet
# along with persent reduced.

from nsepy import get_history
from nsedata import GSReader
from datetime import date, timedelta
import nsepy as nse

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


def one_month_before_date():
    last_month_date = date.today() - timedelta(days=30)
    return last_month_date


def getLatestPrice(equity_name) :
    q = nse.get_quote(equity_name)
    latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    return float(latest_price)


nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL']

nseShareNames = list()
nse_shares_info_list = list()
for equity_name in nseShareNames:
    latest_price = getLatestPrice(equity_name)
    max_price = get_month_high_value(equity_name, one_month_before_date(), date.today())
    percent_change = round(((max_price-latest_price)/max_price*100), 2)
    nse_shares_info_list.append([equity_name, latest_price, max_price, percent_change])
GSReader.updateSepMonthData(nse_shares_info_list)

nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'L%26TFH', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']
nse_next50_shares_info_list = list()
for equity_name in nseNext50shareNames:
    latest_price = getLatestPrice(equity_name)
    max_price = get_month_high_value(equity_name, one_month_before_date(), date.today())
    percent_change = round(((max_price - latest_price) / max_price * 100), 2)
    nse_next50_shares_info_list.append([equity_name, latest_price, max_price, percent_change])
GSReader.updateSepMonthData(nse_next50_shares_info_list)

nse_midcap_data = ['PRESTIGE', 'GMRINFRA', 'APOLLOHOSP', 'TATACOMM', 'FRETAIL', 'IDBI', 'SUPREMEIND', 'M%26MFIN',
                   'ESCORTS', 'RAMCOCEM', 'SAIL', 'APOLLOTYRE', 'MPHASIS', 'ASHOKLEY', 'BHEL', 'SCHAEFFLER',
                   'JINDALSTEL', 'CHOLAFIN', 'ISEC', 'NAM-INDIA', 'EMAMILTD', 'BHARATFORG', 'HUDCO',
                   'SUNTV', 'QUESS', 'L%26TFH', 'VBL', 'IDFCFIRSTB', 'SUMICHEM', 'TVSMOTOR', 'CESC', 'DALBHARAT',
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
    latest_price = getLatestPrice(equity_name)
    max_price = get_month_high_value(equity_name, one_month_before_date(), date.today())
    percent_change = round(((max_price - latest_price) / max_price * 100), 2)
    nse_midcap_shares_info_list.append([equity_name, latest_price, max_price, percent_change])
GSReader.updateSepMonthData(nse_midcap_shares_info_list)