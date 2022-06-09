from datetime import date
from cpr.CPRDayBean import CPRDayBean
from nsepy import get_history

equity_names = ['HEROMOTOCO', 'NESTLEIND', 'BAJAJ-AUTO', 'BRITANNIA', 'HINDUNILVR', 'HDFC', 'SHREECEM', 'BAJAJFINSV',
                'DRREDDY', 'ASIANPAINT', 'TCS', 'RELIANCE', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BAJFINANCE',
                'EICHERMOT', 'MARUTI', 'HDFCAMC', 'PGHH', 'OFSS', 'DMART', 'BOSCHLTD', 'COLPAL', 'ICICIGI', 'PEL', 'UBL',
                'DIVISLAB', 'ACC', 'PIDILITIND', 'INDIGO', 'BAJAJHLDNG', 'SIEMENS', 'PAGEIND', 'COFORGE', 'BAYERCROP',
                'BALKRISIND', 'JUBLFOOD', 'AFFLE', 'LALPATHLAB', 'SRF', 'BLUEDART', 'TATAELXSI', 'ESABINDIA', 'LAURUSLABS',
                'PERSISTENT', 'VSTIND', 'GILLETTE', 'BBTC', 'MCX', 'ICRA', 'HONAUT', 'LTI', 'LTTS', 'MAHSCOOTER', 'SOLARINDS',
                'CERA', 'WHIRLPOOL', 'APOLLOHOSP', 'ASTRAZEN', 'CRISIL', 'MPHASIS', 'MINDTREE', 'METROPOLIS', 'FINEORG',
                'SFL', 'SANOFI', 'IRCTC', 'TTKPRESTIG', 'VAIBHAVGBL', 'BASF', 'BATAINDIA', 'INDIAMART', 'TEAMLEASE',
                'ALKYLAMINE', 'ESCORTS', 'ENDURANCE', 'GMMPFAUDLR', 'MRF', 'VINATIORGA', 'BHARATRAS', 'RATNAMANI',
                'AJANTPHARM', 'LUXIND', 'AIAENG', 'NILKAMAL', 'GLAXO', 'ZYDUSWELL', 'TASTYBITE', 'ALKEM', 'SKFINDIA',
                '3MINDIA', 'NAVINFLUOR', 'JKCEMENT', 'ASTRAL', 'TIMKEN', 'AKZOINDIA', 'PFIZER', 'JCHAC', 'VMART', 'ATUL',
                'AARTIIND', 'APLAPOLLO', 'IPCALAB', 'SCHAEFFLER', 'LAXMIMACH', 'PGHL', 'AAVAS', 'GALAXYSURF', 'DIXON',
                'VENKEYS', 'SUNDARMFIN', 'GARFIBRES', 'PIIND', 'WABCOINDIA', 'PVR', 'SUPREMEIND', 'AMBER']

startDate = date(2020, 9, 10)
for equity_name in equity_names:
    index = 0
    #cprData = CPRData.getEquityData(equity_name, startDate, date.today())

    data = get_history(symbol=equity_name, start=startDate, end=date.today())
    today_cpr_data = CPRDayBean()
    for row in data.itertuples() :
        if index == 0:
            today_cpr_data.calculateCPR(row)
            index += 1
            continue

        tomorrow_cpr_data = CPRDayBean()
        tomorrow_cpr_data.calculateCPR(row)
        if tomorrow_cpr_data.BC > today_cpr_data.TC : #and row.Open > tomorrow_cpr_data.TC:
            print(equity_name, 'uptrend on', row.Index)
        today_cpr_data.calculateCPR(row)