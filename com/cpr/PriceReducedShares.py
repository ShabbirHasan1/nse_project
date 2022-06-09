from datetime import date, timedelta
from nsepy import get_history

# This code return share prices and it's change in a day where it's price gets reduced by more than 5%

def getIncreasedSharePrice(equity_name, traded_date, close_price) :
    next_day = traded_date + timedelta(days=1)
    new_price = get_history(equity_name, next_day, next_day)
    close_vals = list(new_price['HIGH'])

    if len(close_vals) == 0 :
        while True:
            next_day = next_day + timedelta(days=1)
            new_price = get_history(equity_name, next_day, next_day)
            close_vals = list(new_price['Close'])
            if len(close_vals) != 0:
                break

    #print(next_day, close_vals)
    increased_percent = ((close_vals[0] - close_price) * 100)/close_price
    return increased_percent


nse_midcap_data = ['PRESTIGE', 'GMRINFRA', 'APOLLOHOSP', 'TATACOMM', 'FRETAIL', 'IDBI', 'SUPREMEIND', 'M%26MFIN',
                   'ESCORTS', 'RAMCOCEM', 'SAIL', 'APOLLOTYRE', 'MPHASIS', 'ASHOKLEY', 'BHEL', 'SCHAEFFLER',
                   'JINDALSTEL', 'CHOLAFIN', 'ISEC', 'NAM-INDIA', 'EMAMILTD', 'BHARATFORG', 'BBTC', 'HUDCO',
                   'SUNTV', 'QUESS', 'L%26TFH', 'VBL', 'IDFCFIRSTB', 'SUMICHEM', 'TVSMOTOR', 'CESC', 'DALBHARAT',
                   'MFSL', 'CROMPTON', 'AARTIIND', 'AKZOINDIA', 'IBULHSGFIN', 'THERMAX', 'ERIS', 'GODREJAGRO',
                   'IOB', 'AUBANK', 'HAL', 'CUMMINSIND', 'MRPL', 'LTTS', 'RBLBANK', 'TTKPRESTIG', 'SUNDRMFAST',
                   'TATACONSUM', 'APLLTD', 'AMARAJABAT', 'NATIONALUM', 'ATUL', 'CASTROLIND', 'BAYERCROP',
                   'GODREJPROP', 'ALKEM', 'JUBLFOOD', 'CANBK', 'GLAXO', 'ADANIGAS', 'JKCEMENT', 'HEXAWARE',
                   'ADANIPOWER', 'IBVENTURES', 'CREDITACC', 'IDEA', 'MRF', 'MOTILALOFS', 'UCOBANK', 'LICHSGFIN',
                   'FORTIS', 'SHRIRAMCIT', 'INDHOTEL', 'SYMPHONY', 'SYNGENE', 'JSWENERGY', 'GILLETTE', 'GUJGASLTD',
                   'ABB', 'ASTRAL', 'SUNDARMFIN', 'GODREJIND', 'NLCINDIA', 'SRF', 'IRCTC', 'WABCOINDIA',
                   'CHOLAHLDNG', 'CENTRALBK', 'HONAUT', 'POLYCAB', 'TORNTPOWER', 'PIIND', '3MINDIA', 'ENDURANCE',
                   'EXIDEIND', 'MANAPPURAM', 'NIITTECH', 'MINDTREE', 'IPCALAB', 'VINATIORGA', 'TRENT', 'LALPATHLAB',
                   'SJVN', 'LTI', 'JUBILANT', 'SOLARINDS', 'NIACL', 'MGL', 'WHIRLPOOL', 'NATCOPHARM', 'RECLTD',
                   'BLUEDART', 'BALKRISIND', 'BANKINDIA', 'VGUARD', 'EIHOTEL', 'FEDERALBNK', 'GLENMARK', 'HATSUN',
                   'CUB', 'BATAINDIA', 'PFIZER', 'KANSAINER', 'TATAPOWER', 'OIL', 'PHOENIXLTD', 'ADANIGREEN',
                   'RAJESHEXPO', 'GSPL', 'AAVAS', 'RELAXO', 'IIFLWAM', 'VOLTAS', 'UNIONBANK', 'ABCAPITAL', 'SANOFI',
                   'ABFRL', 'PNBHOUSING', 'CRISIL', 'MINDAIND', 'COROMANDEL', 'AJANTPHARM', 'OBEROIRLTY', 'AIAENG',
                   'BEL', 'SKFINDIA', 'EDELWEISS']
nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL', 'IRCTC']

nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'L%26TFH', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']

nse_smallcap_250 = ['THYROCARE', 'MCX', 'BSOFT', 'WESTLIFE','BHARATRAS', 'ADVENZYMES', 'MOIL', 'BIRLACORPN',
                      'BAJAJELEC', 'KEC', 'ASTERDM', 'AEGISCHEM', 'TASTYBITE', 'METROPOLIS', 'INTELLECT', 'DCAL',
                      'HINDCOPPER', 'REPCOHOME', 'OMAXE', 'RENUKA', 'FCONSUMER', 'GEPIL', 'LAURUSLABS', 'PTC', 'FDC',
                      'BDL', 'JKLAKSHMI', 'SONATSOFTW', 'CGCL', 'PERSISTENT', 'RALLIS', 'RAIN', 'JSLHISAR', 'WELCORP',
                      'UJJIVAN', 'FINCABLES', 'JKTYRE', 'PGHL', 'IDFC', 'BAJAJCON', 'ZENSARTECH', 'FLUOROCHEM',
                      'ZYDUSWELL', 'WELSPUNIND', 'VMART', 'HEIDELBERG', 'CEATLTD', 'CDSL', 'CENTURYPLY', 'SEQUENT',
                      'TIMKEN', 'PRSMJOHNSN', 'GMMPFAUDLR', 'AFFLE', 'EQUITAS', 'INDOCO', 'CENTURYTEX', 'PHILIPCARB',
                      'GSFC', 'CHAMBLFERT', 'IEX', 'MAHINDCIE', 'TATAELXSI', 'HSCL', 'EIDPARRY', 'INFIBEAM',
                      'BALRAMCHIN', 'JAICORPLTD', 'ORIENTREF', 'POLYMED', 'ORIENTELEC', 'DBL', 'TCNSBRANDS', 'ESSELPACK',
                      'TATASTLBSL', 'INDIANB', 'GNFC', 'JMFINANCIL', 'LAXMIMACH', 'UJJIVANSFB', 'CYIENT', 'MASFIN',
                      'INOXLEISUR', 'BRIGADE', 'LUXIND', 'VAIBHAVGBL', 'COCHINSHIP', 'LINDEINDIA', 'KRBL', 'KNRCON',
                      'SOBHA', 'CARERATING', 'TIINDIA', 'PRAJIND', 'TEAMLEASE', 'ESABINDIA', 'KEI', 'NFL','KSCL',
                      'SUPRAJIT', 'MMTC', 'ALLCARGO', 'JUSTDIAL', 'NCC', 'KARURVYSYA', 'VSTIND', 'GRAPHITE', 'RADICO',
                      'ALKYLAMINE', 'NBCC', 'JSL', 'DCBBANK', 'GMDCLTD', 'IFBIND', 'JCHAC', 'FSL', 'HIMATSEIDE',
                      'DEEPAKNTR', 'BASF', 'BLUESTARCO', 'CARBORUNIV', 'VRLLOG', 'STARCEMENT', 'NESCO', 'IRB',
                      'DCMSHRIRAM', 'JINDALSAW', 'GALAXYSURF', 'BALMLAWRIE', 'AMBER', 'ORIENTCEM', 'RATNAMANI',
                      'WOCKPHARMA', 'SPANDANA', 'TAKE', 'KPRMILL', 'KAJARIACER', 'MAHSCOOTER', 'TATAINVEST', 'ELGIEQUIP',
                      'PVR', 'SUDARSCHEM', 'VESUVIUS', 'GHCL', 'NBVENTURES', 'JBCHEPHARM', 'STAR', 'JAMNAAUTO',
                      'KOLTEPATIL', 'INDOSTAR', 'STRTECH', 'MIDHANI', 'BEML', 'GESHIP', 'ASAHIINDIA', 'PNCINFRA',
                      'CAPLIPOINT', 'ITI', 'JKPAPER', 'HEG', 'RITES', 'MAHLOG', 'JAGRAN', 'TIMETECHNO', 'INGERRAND',
                      'NILKAMAL', 'MINDACORP', 'GUJALKALI', 'ICRA', 'TVTODAY', 'GRINDWELL', 'BLISSGVS', 'KPITTECH',
                      'SPICEJET', 'GODFRYPHLP', 'DELTACORP', 'SCI', 'GPPL', 'KSB', 'GREAVESCOT', 'ITDC', 'ECLERX',
                      'JYOTHYLAB', 'GET%26D', 'BOMDYEING', 'SPARC', 'SADBHAV', 'SWSOLAR', 'IFCI', 'RCF', 'LEMONTREE',
                      'DBCORP', 'BSE', 'TCIEXP', 'GRANULES', 'SFL', 'ASTRAZEN', 'IRCON', 'TV18BRDCST', 'DHANUKA',
                      'VENKEYS', 'AVANTIFEED', 'SUZLON', 'VIPIND', 'INDIACEM', 'FINEORG', 'RVNL', 'IIFL', 'GULFOILLUB',
                      'CCL', 'RAYMOND', 'APLAPOLLO', 'SCHNEIDER', 'SOUTHBANK', 'INDIAMART', 'REDINGTON', 'FINPIPE',
                      'SHOPERSTOP', 'MHRIL', 'NAVINFLUOR', 'KTKBANK', 'KALPATPOWR', 'MAHABANK', 'CHENNPETRO', 'VARROC',
                      'SUNTECK', 'GARFIBRES', 'CERA', 'VAKRANGEE', 'VTL', 'LAOPALA', 'UFLEX', 'TRIDENT', 'ENGINERSIN',
                      'NH', 'DISHTV', 'IBREALEST', 'CANFINHOME', 'GRSE', 'SIS', 'DIXON', 'CSBBANK', 'J%26KBANK',
                      'SWANENERGY', 'HFCL', 'HATHWAY', 'HERITGFOOD', 'ARVINDFASN', 'ASHOKA', 'MAHSEAMLES']

startDate = date(2020, 3, 23)
for equity_name in nse_smallcap_250:
    index = 0
    data = get_history(symbol=equity_name, start=startDate, end=date.today())
    for row in data.itertuples() :
        if index == 0:
            yesterday_close_price = row.Close
            index += 1
            continue

        reduced_percent = ((yesterday_close_price- row.Close) * 100) / yesterday_close_price
        if reduced_percent > 5:
            increased_percent = getIncreasedSharePrice(equity_name, row.Index, row.Close)
            print(row.Index, equity_name, reduced_percent, ' nextday increased by ', increased_percent)
        yesterday_close_price = row.Close