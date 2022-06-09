from datetime import date, timedelta
from nsepy import get_history

from pivotbossstrategies.valuearearelationships.CPRData import CPRData


def getEquityData(equity_name) :
    cpr_day = date.today() - timedelta(days=2)
    data = get_history(symbol=equity_name, start=cpr_day, end=date.today())
    return data


def printNarrowRangeAndOutsideRangeOpenDays(equity_name) :
    data = getEquityData(equity_name)
    index = 0
    yesterday_data = CPRData()

    for row in data.itertuples():

        if index == 0:
            yesterday_data.pp = (row.High + row.Low + row.Close) / 3
            yesterday_data.bc = (row.High + row.Low) / 2
            yesterday_data.tc = (yesterday_data.pp - yesterday_data.bc) + yesterday_data.pp
            if yesterday_data.bc > yesterday_data.tc:
                yesterday_data.tc = (row.High + row.Low) / 2
                yesterday_data.bc = (yesterday_data.pp - yesterday_data.bc) + yesterday_data.pp
            index = index + 1
            yesterday_data.cpr_date = row.Index
            yesterday_high = row.High
            yesterday_low = row.Low
            continue
        range_width = (yesterday_data.tc - yesterday_data.bc)/100
        if range_width <= 0.01 :
            if (row.Open > yesterday_high or row.Open < yesterday_low) :
                print(equity_name, range_width, row.Index, 'Trend Day')

        yesterday_high = row.High
        yesterday_low = row.Low
        yesterday_data.pp = (row.High + row.Low + row.Close) / 3
        yesterday_data.bc = (row.High + row.Low) / 2
        yesterday_data.tc = (yesterday_data.pp - yesterday_data.bc) + yesterday_data.pp
        yesterday_data.cpr_date = row.Index
        if yesterday_data.bc > yesterday_data.tc:
            yesterday_data.tc = (row.High + row.Low) / 2
            yesterday_data.bc = (yesterday_data.pp - yesterday_data.bc) + yesterday_data.pp

nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL', 'IRCTC', 'MCXCRUDEX']
nse_midcap_data = ["PRESTIGE", "GMRINFRA", "APOLLOHOSP", "TATACOMM", "FRETAIL", "IDBI", "SUPREMEIND", "M%26MFIN",
                   "ESCORTS", "RAMCOCEM", "SAIL", "APOLLOTYRE", "MPHASIS", "ASHOKLEY", "BHEL", "SCHAEFFLER",
                   "JINDALSTEL", "CHOLAFIN", "ISEC", "NAM-INDIA", "EMAMILTD", "BHARATFORG", "BBTC", "HUDCO",
                   "SUNTV", "QUESS", "L%26TFH", "VBL", "IDFCFIRSTB", "SUMICHEM", "TVSMOTOR", "CESC", "DALBHARAT",
                   "MFSL", "CROMPTON", "AARTIIND", "AKZOINDIA", "IBULHSGFIN", "THERMAX", "ERIS", "GODREJAGRO",
                   "IOB", "AUBANK", "HAL", "CUMMINSIND", "MRPL", "LTTS", "RBLBANK", "TTKPRESTIG", "SUNDRMFAST",
                   "TATACONSUM", "APLLTD", "AMARAJABAT", "NATIONALUM", "ATUL", "CASTROLIND", "BAYERCROP",
                   "GODREJPROP", "ALKEM", "JUBLFOOD", "CANBK", "GLAXO", "ADANIGAS", "JKCEMENT", "HEXAWARE",
                   "ADANIPOWER", "IBVENTURES", "CREDITACC", "IDEA", "MRF", "MOTILALOFS", "UCOBANK", "LICHSGFIN",
                   "FORTIS", "SHRIRAMCIT", "INDHOTEL", "SYMPHONY", "SYNGENE", "JSWENERGY", "GILLETTE", "GUJGASLTD",
                   "ABB", "ASTRAL", "SUNDARMFIN", "GODREJIND", "NLCINDIA", "SRF", "IRCTC", "WABCOINDIA",
                   "CHOLAHLDNG", "CENTRALBK", "HONAUT", "POLYCAB", "TORNTPOWER", "PIIND", "3MINDIA", "ENDURANCE",
                   "EXIDEIND", "MANAPPURAM", "NIITTECH", "MINDTREE", "IPCALAB", "VINATIORGA", "TRENT", "LALPATHLAB",
                   "SJVN", "LTI", "JUBILANT", "SOLARINDS", "NIACL", "MGL", "WHIRLPOOL", "NATCOPHARM", "RECLTD",
                   "BLUEDART", "BALKRISIND", "BANKINDIA", "VGUARD", "EIHOTEL", "FEDERALBNK", "GLENMARK", "HATSUN",
                   "CUB", "BATAINDIA", "PFIZER", "KANSAINER", "TATAPOWER", "OIL", "PHOENIXLTD", "ADANIGREEN",
                   "RAJESHEXPO", "GSPL", "AAVAS", "RELAXO", "IIFLWAM", "VOLTAS", "UNIONBANK", "ABCAPITAL", "SANOFI",
                   "ABFRL", "PNBHOUSING", "CRISIL", "MINDAIND", "COROMANDEL", "AJANTPHARM", "OBEROIRLTY", "AIAENG",
                   "BEL", "SKFINDIA", "EDELWEISS"]
for equityName in nse_midcap_data:
    printNarrowRangeAndOutsideRangeOpenDays(equityName)
