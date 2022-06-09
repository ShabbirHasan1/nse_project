import nsepy as nifty
import pandas as pd
from nsepy import get_history
from datetime import date, timedelta


def a_day_in_previous_month(date):
    date_1 = pd.to_datetime(date, format="%Y-%m-%d") - pd.DateOffset(months=1)
    return date_1.date()


def maxValue(pricelist) :
    maxValue = pricelist[0]
    for value in pricelist :
        if maxValue < value :
            maxValue = value
    return maxValue


def minValue(pricelist):
    minValue = pricelist[0]
    for value in pricelist :
        if minValue > value :
            minValue = value
    return minValue


startdate = a_day_in_previous_month(date.today())
fileName = date.today().strftime("%d-%m-%Y") + '.csv'
csvRows = list()

shareNames = ['INDUSINDBK', 'HEROMOTOCO', 'NESTLEIND', 'POWERGRID', 'M&M', 'BAJAJ-AUTO', 'BRITANNIA', 'NTPC', 'HCLTECH',
              'HINDUNILVR', 'HINDALCO', 'HDFC', 'CIPLA', 'SHREECEM', 'UPL', 'BAJAJFINSV', 'DRREDDY', 'IOC', 'ASIANPAINT',
              'INFY', 'ONGC', 'LT', 'WIPRO', 'TCS', 'ADANIPORTS', 'COALINDIA', 'BPCL', 'RELIANCE', 'GAIL', 'ITC',
              'HDFCBANK', 'ULTRACEMCO', 'TITAN', 'KOTAKBANK', 'BHARTIARTL', 'JSWSTEEL', 'TECHM', 'AXISBANK', 'TATASTEEL',
              'ICICIBANK', 'VEDL', 'GRASIM', 'BAJFINANCE', 'EICHERMOT', 'MARUTI', 'TATAMOTORS', 'SUNPHARMA', 'SBIN',
              'ZEEL', 'INFRATEL', 'IRCTC']
csvHeaders = ['Name', 'Max Val', 'Min Val', 'Closing Val', 'Reduced %', 'Is Min Val Reached', 'Reduced 12%']
csvRows.append(csvHeaders)

for equityName in shareNames :
    data = get_history(symbol=equityName, start=startdate, end=date.today())

    highVals = list(data['High'])
    lowVals = list(data['Low'])

    maxVal = maxValue(pricelist=highVals)
    minVal = minValue(pricelist=lowVals)

    count = data['Close'].count()
    closeVal = data['Close'].values[count-1]

    reducedPercent = ((maxVal - closeVal)/maxVal) * 100

    buyingTime = False
    minValReached = False
    if closeVal < maxVal * 0.88:
        buyingTime = True
    if closeVal < minVal * 1.02:
        minValReached = True

    rowList = list()
    #rowList.append(date.today())
    rowList.append(equityName)
    rowList.append(maxVal)
    rowList.append(minVal)
    rowList.append(closeVal)
    rowList.append(reducedPercent)
    rowList.append(minValReached)
    rowList.append(buyingTime)
    csvRows.append(rowList)

import csv
fileLoc = 'c:/sharesInfo/'

with open(fileLoc + fileName, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in csvRows :
        writer.writerow(row)

#print(csvRows)
