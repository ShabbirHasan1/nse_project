import nsepy as nse


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

nseNext50shareNames = ['PETRONET', 'HDFCAMC', 'ADANITRANS', 'SRTRANSFIN', 'PGHH', 'HINDZINC', 'CADILAHC', 'HDFCLIFE',
                       'OFSS', 'NHPC', 'DMART', 'SBILIFE', 'BANDHANBNK', 'ICICIPRULI', 'BERGEPAINT', 'BOSCHLTD',
                       'BIOCON', 'HINDPETRO', 'LUPIN', 'AMBUJACEM', 'COLPAL', 'MARICO', 'ICICIGI', 'MOTHERSUMI', 'PEL',
                       'UBL', 'DIVISLAB', 'AUROPHARMA', 'ACC', 'HAVELLS', 'PIDILITIND', 'L%26TFH', 'MCDOWELL-N', 'DABUR',
                       'GICRE', 'INDIGO', 'BAJAJHLDNG', 'ASHOKLEY', 'SIEMENS', 'PFC', 'NMDC', 'PNB', 'PAGEIND',
                       'GODREJCP', 'DLF', 'BANKBARODA', 'NIACL', 'CONCOR', 'IBULHSGFIN', 'IDEA']

nseMidCapShareNames = ['STAR', 'COFORGE', 'NESCO', 'KAJARIACER', 'MANAPPURAM', 'IIFL', 'HINDCOPPER', 'WESTLIFE',
                       'ADANIGREEN', 'FRETAIL', 'JAMNAAUTO', 'DISHTV', 'HATSUN', 'KPITTECH', 'GRAPHITE', 'IBREALEST',
                       'BAJAJCON', 'BAYERCROP', 'TRIDENT', 'ERIS', 'NFL', 'AUBANK', 'BALKRISIND', 'SEQUENT',
                       'COROMANDEL', 'UJJIVAN', 'JINDALSTEL', 'PRESTIGE', 'GLENMARK', 'CANFINHOME', 'INTELLECT',
                       'MHRIL', 'ELGIEQUIP', 'NLCINDIA', 'RADICO', 'JUBLFOOD', 'MAHSEAMLES', 'AFFLE', 'STARCEMENT',
                       'ALLCARGO', 'LALPATHLAB', 'GULFOILLUB', 'NH', 'SRF', 'BLUEDART', 'RVNL', 'TATAPOWER', 'EQUITAS',
                       'SCHNEIDER', 'TATAELXSI', 'VESUVIUS', 'JUSTDIAL', 'ECLERX', 'ESABINDIA', 'LAURUSLABS', 'CHAMBLFERT',
                       'PERSISTENT', 'CROMPTON', 'THYROCARE', 'JUBILANT', 'HEG', 'HATHWAY', 'VSTIND', 'GMRINFRA', 'FORTIS',
                       'GILLETTE', 'ASTERDM', 'KOLTEPATIL', 'ITDC', 'ARVINDFASN', 'MAHLOG', 'BALRAMCHIN', 'TVSMOTOR',
                       'PNCINFRA', 'LEMONTREE', 'TRENT', 'ENGINERSIN', 'BBTC', 'CCL', 'CHOLAFIN', 'NATCOPHARM', 'GPPL',
                       'FEDERALBNK', 'MGL', 'MFSL', 'RBLBANK', 'IDFCFIRSTB', 'EMAMILTD', 'JBCHEPHARM', 'MCX',
                       'IRCON', 'ICRA', 'SAIL', 'SUMICHEM', 'HONAUT', 'PHILIPCARB', 'SIS', 'IBULHSGFIN', 'SUNTV', 'NCC',
                       'SHOPERSTOP', 'ITI', 'LTI', 'EIHOTEL', 'GSPL', 'WOCKPHARMA', 'GESHIP', 'LTTS', 'RAYMOND', 'MINDAIND',
                       'TATAINVEST', 'KPRMILL', 'VOLTAS', 'SWANENERGY', 'CASTROLIND', 'SPICEJET', 'MAHSCOOTER', 'SOLARINDS',
                       'NATIONALUM', 'BOMDYEING', 'ZENSARTECH', 'CERA', 'CHOLAHLDNG', 'PRAJIND', 'WHIRLPOOL', 'CARERATING',
                       'GEPIL', 'RITES', 'SOUTHBANK', 'CANBK', 'RECLTD', 'APOLLOHOSP', 'BEL', 'EDELWEISS', 'IFBIND', 'KTKBANK',
                       'RELAXO', 'IDBI', 'PRSMJOHNSN', 'ASHOKLEY', 'GUJGASLTD', 'ASTRAZEN', 'GODREJAGRO', 'JKLAKSHMI',
                       'INFIBEAM', 'TATASTLBSL', 'AMARAJABAT', 'DHANUKA', 'BRIGADE', 'TCNSBRANDS', 'POLYCAB', 'INDIANB',
                       'CRISIL', 'MPHASIS', 'VIPIND', 'MINDTREE', 'IIFLWAM', 'METROPOLIS', 'BLISSGVS', 'RAMCOCEM',
                       'PNBHOUSING', 'ASAHIINDIA', 'FINEORG', 'INDOCO', 'SFL', 'LICHSGFIN', 'AEGISCHEM', 'M%26MFIN', 'BSOFT',
                       'SANOFI', 'IRCTC', 'GMDCLTD', 'GSFC', 'TTKPRESTIG', 'MMTC', 'RAJESHEXPO', 'COCHINSHIP', 'VAIBHAVGBL',
                       'VTL', 'TIMETECHNO', 'TATACONSUM', 'JMFINANCIL', 'BASF', 'BATAINDIA', 'INDIAMART', 'TEAMLEASE',
                       'BALMLAWRIE', 'HSCL', 'SYNGENE', 'SADBHAV', 'GREAVESCOT', 'ALKYLAMINE', 'ESCORTS', 'OIL', 'JKPAPER',
                       'NBVENTURES', 'ENDURANCE', 'OMAXE', 'SUDARSCHEM', 'GMMPFAUDLR', 'INDOSTAR', 'MRF', 'INDHOTEL',
                       'SYMPHONY', 'CUB', 'DCMSHRIRAM', 'VINATIORGA', 'BAJAJELEC', 'BHEL', 'J%26KBANK', 'MAHABANK',
                       'ADVENZYMES', 'ABB', 'DBCORP', 'SUZLON', 'SUNTECK', 'BHARATRAS', 'BLUESTARCO', 'ISEC', 'AVANTIFEED',
                       'KALPATPOWR', 'CSBBANK', 'DALBHARAT', 'KANSAINER', 'LAOPALA', 'JKTYRE', 'VARROC', 'GODREJPROP',
                       'LINDEINDIA', 'BHARATFORG', 'RATNAMANI', 'CENTURYTEX', 'UJJIVANSFB', 'PHOENIXLTD', 'POLYMED', 'MRPL',
                       'IDFC', 'CENTURYPLY', 'TAKE', 'CAPLIPOINT', 'BIRLACORPN', 'SCI', 'AJANTPHARM', 'LUXIND', 'JSLHISAR',
                       'ASHOKA', 'KEC', 'CENTRALBK', 'GET%26D', 'JINDALSAW', 'HFCL', 'EXIDEIND', 'RCF', 'AIAENG', 'CEATLTD',
                       'NILKAMAL', 'UNIONBANK', 'NAM-INDIA', 'UCOBANK', 'GLAXO', 'HERITGFOOD', 'ZYDUSWELL', 'PTC', 'VBL',
                       'CHENNPETRO', 'JYOTHYLAB', 'APOLLOTYRE', 'BEML', 'FCONSUMER', 'TASTYBITE', 'SOBHA', 'ORIENTELEC',
                       'WELCORP', 'KARURVYSYA', 'KEI', 'ADANIGAS', 'TORNTPOWER', 'FINCABLES', 'TCIEXP', 'APLLTD', 'BDL',
                       'ALKEM', 'SKFINDIA', 'THERMAX', 'HIMATSEIDE', 'HEIDELBERG', 'FINPIPE', 'GODFRYPHLP',
                       'UFLEX', 'HUDCO', 'GHCL', 'MAHINDCIE', 'INOXLEISUR', 'ABFRL', '3MINDIA', 'NAVINFLUOR', 'IFCI',
                       'JAICORPLTD', 'JAGRAN', 'ORIENTREF', 'SHRIRAMCIT', 'JKCEMENT', 'TV18BRDCST', 'OBEROIRLTY', 'FDC',
                       'RALLIS', 'NIACL', 'BSE', 'EIDPARRY', 'MINDACORP', 'CREDITACC', 'CDSL', 'CESC', 'WELSPUNIND', 'KSB',
                       'ASTRAL', 'JSL', 'IOB', 'FSL', 'MOTILALOFS', 'INDIACEM', 'GNFC', 'GUJALKALI', 'CGCL', 'GODREJIND',
                       'TATACOMM', 'NBCC', 'SUPRAJIT', 'TIMKEN', 'DCBBANK', 'VGUARD', 'AKZOINDIA', 'IRB', 'ADANIPOWER',
                       'PFIZER', 'JCHAC', 'INGERRAND', 'SJVN', 'DBL', 'KSCL', 'VMART', 'MASFIN', 'REPCOHOME', 'ATUL', 'KRBL',
                       'AARTIIND', 'DELTACORP', 'VRLLOG', 'SPANDANA', 'ORIENTCEM', 'APLAPOLLO', 'HAL', 'MOIL', 'TVTODAY',
                       'IPCALAB', 'REDINGTON', 'SCHAEFFLER', 'RENUKA', 'SWSOLAR', 'LAXMIMACH', 'IEX', 'CARBORUNIV',
                       'SUNDRMFAST', 'PGHL', 'AAVAS', 'MIDHANI', 'GRINDWELL', 'SONATSOFTW', 'GALAXYSURF', 'QUESS',
                       'VAKRANGEE', 'DIXON', 'VENKEYS', 'RAIN', 'DEEPAKNTR', 'SUNDARMFIN', 'SPARC', 'GARFIBRES', 'KNRCON',
                       'TIINDIA', 'ABCAPITAL', 'PIIND', 'FLUOROCHEM', 'WABCOINDIA', 'GRSE', 'IDEA', 'PVR', 'BANKINDIA',
                       'DCAL', 'JSWENERGY', 'CUMMINSIND', 'CYIENT', 'SUPREMEIND', 'GRANULES', 'AMBER']


for equity_name in nseShareNames:
    latest_price = getLatestPrice(equity_name)
    if latest_price >= 10000:
        print(equity_name + '\t' + str(latest_price))

for equity_name in nseNext50shareNames:
    latest_price = getLatestPrice(equity_name)
    if latest_price >= 10000:
        print(equity_name + '\t' + str(latest_price))

for equity_name in nseMidCapShareNames:
    latest_price = getLatestPrice(equity_name)
    if latest_price >= 10000:
        print(equity_name + '\t' + str(latest_price))
