import datetime

from datetime import date, timedelta
from nsepy import get_history
from nsedata import GSReader


def fetch_equity_data(shares_dict, share_names, start_date) :
    share_data_list = list()
    for equityName in share_names:
        data = get_history(symbol=equityName, start=start_date, end=date.today())
        low_vals = list(data['Low'])
        least_val = leastValue(price_list=low_vals)

        high_vals = list(data['High'])
        high_val = highValue(price_list=high_vals)

        percent_change = round(((high_val-least_val)/least_val)*100, 2)
        share_data_list.append([equityName, least_val, high_val, percent_change])
        #shares_dict[equityName] = share_data_list
    GSReader.updateShareData(share_data_list)


def leastValue(price_list) :
    low_value = price_list[0]
    for value in price_list :
        if low_value > value :
            low_value = value
    return low_value


def highValue(price_list):
    high_value = price_list[0]
    for value in price_list :
        if high_value < value :
            high_value = value
    return high_value


def insertDataIntoSheet(equity_price_info_dict, nseShareNames) :
    rows = list()
    for share_name in nseShareNames:
        rows.append(equity_price_info_dict.get(share_name))
    GSReader.updateShareData(rows)


startDate = date.today() - timedelta(days=30)
nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL']

nseFirst50SharesInfoDict = dict()
fetch_equity_data(nseFirst50SharesInfoDict, nseShareNames, startDate)
#insertDataIntoSheet(nseFirst50SharesInfoDict, nseShareNames)
print(nseFirst50SharesInfoDict)

nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'L%26TFH', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']

nseNext50SharesInfoDict = dict()
fetch_equity_data(nseNext50SharesInfoDict, nseNext50shareNames, startDate)
#insertDataIntoSheet(nseNext50SharesInfoDict, nseNext50shareNames)
print(nseNext50SharesInfoDict)

nse_midcap_data = ['PRESTIGE', 'GMRINFRA', 'APOLLOHOSP', 'TATACOMM', 'FRETAIL', 'IDBI', 'SUPREMEIND', 'M%26MFIN',
                   'ESCORTS', 'RAMCOCEM', 'SAIL', 'APOLLOTYRE', 'MPHASIS', 'BHEL', 'SCHAEFFLER',
                   'JINDALSTEL', 'CHOLAFIN', 'ISEC', 'NAM-INDIA', 'EMAMILTD', 'BHARATFORG', 'HUDCO',
                   'SUNTV', 'QUESS', 'L%26TFH', 'VBL', 'IDFCFIRSTB', 'SUMICHEM', 'TVSMOTOR', 'CESC', 'DALBHARAT',
                   'MFSL', 'CROMPTON', 'AARTIIND', 'AKZOINDIA', 'THERMAX', 'ERIS', 'GODREJAGRO',
                   'IOB', 'AUBANK', 'HAL', 'CUMMINSIND', 'MRPL', 'LTTS', 'RBLBANK', 'TTKPRESTIG', 'SUNDRMFAST',
                   'TATACONSUM', 'APLLTD', 'AMARAJABAT', 'NATIONALUM', 'ATUL', 'CASTROLIND', 'BAYERCROP',
                   'GODREJPROP', 'ALKEM', 'JUBLFOOD', 'CANBK', 'GLAXO', 'ADANIGAS', 'JKCEMENT', 'HEXAWARE',
                   'ADANIPOWER', 'IBVENTURES', 'CREDITACC', 'MRF', 'MOTILALOFS', 'UCOBANK', 'LICHSGFIN',
                   'FORTIS', 'SHRIRAMCIT', 'INDHOTEL', 'SYMPHONY', 'SYNGENE', 'JSWENERGY', 'GILLETTE', 'GUJGASLTD',
                   'ABB', 'ASTRAL', 'SUNDARMFIN', 'GODREJIND', 'NLCINDIA', 'SRF', 'WABCOINDIA',
                   'CHOLAHLDNG', 'CENTRALBK', 'HONAUT', 'POLYCAB', 'TORNTPOWER', 'PIIND', '3MINDIA', 'ENDURANCE',
                   'EXIDEIND', 'MANAPPURAM', 'NIITTECH', 'MINDTREE', 'IPCALAB', 'VINATIORGA', 'TRENT', 'LALPATHLAB',
                   'SJVN', 'LTI', 'JUBILANT', 'SOLARINDS', 'MGL']

nseMideCapSharesInfoDict = dict()
fetch_equity_data(nseMideCapSharesInfoDict, nse_midcap_data, startDate)
#insertDataIntoSheet(nseMideCapSharesInfoDict, nse_midcap_data)
print(nseMideCapSharesInfoDict)

nse_midcap_data_1 = ['WHIRLPOOL', 'NATCOPHARM', 'RECLTD', 'BLUEDART', 'BALKRISIND', 'BANKINDIA', 'VGUARD', 'EIHOTEL', 'FEDERALBNK', 'GLENMARK',
                    'HATSUN', 'CUB', 'BATAINDIA', 'PFIZER', 'KANSAINER', 'TATAPOWER', 'OIL', 'PHOENIXLTD',
                    'ADANIGREEN', 'RAJESHEXPO', 'GSPL', 'AAVAS', 'RELAXO', 'IIFLWAM', 'VOLTAS', 'UNIONBANK',
                    'ABCAPITAL', 'SANOFI', 'ABFRL', 'PNBHOUSING', 'CRISIL', 'MINDAIND', 'COROMANDEL', 'AJANTPHARM',
                    'OBEROIRLTY', 'AIAENG', 'BEL', 'SKFINDIA', 'EDELWEISS']

nseMideCapSharesInfoDict_1 = dict()
fetch_equity_data(nseMideCapSharesInfoDict_1, nse_midcap_data_1, startDate)
#insertDataIntoSheet(nseMideCapSharesInfoDict_1, nse_midcap_data_1)
print(nseMideCapSharesInfoDict_1)
