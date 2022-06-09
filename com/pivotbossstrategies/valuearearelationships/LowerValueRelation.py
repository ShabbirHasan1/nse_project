from datetime import date, timedelta
from nsepy import get_history

from pivotbossstrategies.valuearearelationships.CPRData import CPRData


def getEquityData(equity_name) :
    cpr_day = date.today() - timedelta(days=30)
    data = get_history(symbol=equity_name, start=cpr_day, end=date.today())
    return data


def printHigherValueDays(equity_name) :
    data = getEquityData(equity_name)
    index = 0

    day_before_yesterday = CPRData()
    yesterday_day = CPRData()

    for row in data.itertuples():
        if index == 0:
            day_before_yesterday.pp = (row.High + row.Low + row.Close) / 3
            day_before_yesterday.bc = (row.High + row.Low) / 2
            day_before_yesterday.tc = (day_before_yesterday.pp - day_before_yesterday.bc) + day_before_yesterday.pp
            if day_before_yesterday.bc > day_before_yesterday.tc:
                day_before_yesterday.tc = (row.High + row.Low) / 2
                day_before_yesterday.bc = (day_before_yesterday.pp - day_before_yesterday.bc) + day_before_yesterday.pp
            index = index + 1
            day_before_yesterday.cpr_date = row.Index
            #print(row.Index , previous_day.pp, previous_day.bc, previous_day.tc)    # Yesterday
            continue
        if index == 1 :
            index = index + 1
            yesterday_day.pp = (row.High + row.Low + row.Close) / 3
            yesterday_day.bc = (row.High + row.Low) / 2
            yesterday_day.tc = (yesterday_day.pp - yesterday_day.bc) + yesterday_day.pp
            yesterday_day.cpr_date = row.Index
            if yesterday_day.bc > yesterday_day.tc:
                yesterday_day.tc = (row.High + row.Low) / 2
                yesterday_day.bc = (yesterday_day.pp - yesterday_day.bc) + yesterday_day.pp
            #print(row.Index, present_day.pp, present_day.bc, present_day.tc, row.Open)  # Present Day
            continue
        index += 1

        if yesterday_day.tc < day_before_yesterday.bc :
            if row.Open > (yesterday_day.tc) :
                #print(day_before_yesterday.cpr_date, yesterday_day.cpr_date)
                print(equity_name, 'Bullish Day', row.Index, row.Open, yesterday_day.tc)
            if row.Open < (yesterday_day.bc) :
                #print(day_before_yesterday.cpr_date, yesterday_day.cpr_date)
                print(equity_name, 'Bearish Day', row.Index, row.Open, yesterday_day.bc)
        day_before_yesterday.pp = yesterday_day.pp
        day_before_yesterday.tc = yesterday_day.tc
        day_before_yesterday.bc = yesterday_day.bc
        day_before_yesterday.cpr_date = yesterday_day.cpr_date

        yesterday_day.pp = (row.High + row.Low + row.Close) / 3
        yesterday_day.bc = (row.High + row.Low) / 2
        yesterday_day.tc = (yesterday_day.pp - yesterday_day.bc) + yesterday_day.pp
        yesterday_day.cpr_date = row.Index
        if yesterday_day.bc > yesterday_day.tc:
            yesterday_day.tc = (row.High + row.Low) / 2
            yesterday_day.bc = (yesterday_day.pp - yesterday_day.bc) + yesterday_day.pp


nseShareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M%26M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC',
                 'HCLTECH', 'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY',
                 'IOC', 'ASIANPAINT', 'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL',
                 'RELIANCE', 'GAIL', 'ITC', 'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL',
                 'TECHM', 'AXISBANK', 'TATASTEEL', 'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI',
                 'TATAMOTORS', 'SUNPHARMA', 'SBIN', 'ZEEL', 'INFRATEL', 'IRCTC']

for equityName in nseShareNames:
    printHigherValueDays(equityName)
