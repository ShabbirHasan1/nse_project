
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import date, timedelta
#import math
from nyse import sharepricelatest_polygon_restclient


def MonthBackValueDate():
    fort_night_date = date.today() - timedelta(days=30)
    return fort_night_date


def getChangeVals(close_vals):
    price_changes = []
    previous_day_val = 0
    for close_val in close_vals:
        if previous_day_val == 0 :
            previous_day_val = close_val
            continue
        price_changes.append(close_val - previous_day_val)
        previous_day_val = close_val
    return price_changes


def getGainAvg(price_changes) :
    gain_avg_vals = list()
    index = 0
    sum = 0
    while index < 14:
        if price_changes[index] >= 0:
            sum += price_changes[index]
        index += 1
    gain_avg_vals.append(sum/14)

    gain_avg_index = 0
    #gain_avg_vals.get
    while index < len(price_changes):
        gain_avg_vals.append(((gain_avg_vals.__getitem__(gain_avg_index) * 13) + price_changes[index]) / 14)
        #if price_changes[gain_avg_index] == 0:
        #    gain_avg_vals.append(((gain_avg_vals.__getitem__(gain_avg_index) * 13) + 0)/14)
        #else:

        gain_avg_index += 1
        index += 1
    return gain_avg_vals


def getLossAvg(price_changes) :
    loss_avg_vals = []
    index = 0
    sum = 0
    #print('price changes = ', price_changes)
    while index < 14:
        if price_changes[index] <= 0:
            sum += abs(price_changes[index])
        index += 1

    loss_avg_vals.append(sum/14)

    loss_avg_index = 0
    while index < len(price_changes):
        loss_avg_vals.append(((loss_avg_vals[loss_avg_index] * 13) + price_changes[index]) / 14)
        #if price_changes[loss_avg_index] == 0:
        #    loss_avg_vals[loss_avg_index + 1] = ((loss_avg_vals[loss_avg_index] * 13) + 0)/14
        #else:
        loss_avg_index += 1
        index += 1
    return loss_avg_vals


def getRSIValues(gain_avg_vals, loss_avg_vals) :
    rs_vals = []
    rsi_vals = []
    index = 0
    while index < len(gain_avg_vals):
        rs_vals.append(gain_avg_vals[index]/loss_avg_vals[index])
        rsi_vals.append(100 - (100/(1+rs_vals[index])))
        index = index + 1
    return rsi_vals


yf.pdr_override()
tickers = ['EURUSD=X', 'USDCAD=X', 'AUDUSD=X', 'AUDJPY=X', 'EURJPY=X', 'EURNZD=X', 'GBPAUD=X', 'GBPUSD=X', 'NZDUSD=X', 'USDJPY=X', 'AUDCAD=X',
           'AUDCHF=X', 'AUDNZD=X', 'CADCHF=X', 'CADJPY=X', 'EURAUD=X', 'EURCAD=X', 'EURCHF=X', 'EURGBP=X', 'GBPCAD=X', 'EURCAD=X', 'EURCHF=X',
           'EURGBP=X', 'GBPCAD=X', 'GBPCHF=X', 'GBPJPY=X', 'GBPNZD=X', 'NZDJPY=X', 'USDCHF=X']

for ticker in tickers:
    data = pdr.get_data_yahoo(ticker, start=MonthBackValueDate(), end=date.today())
    close_vals = data['Close']
    for close_val in close_vals:
        print(type(close_val))
    #print(type(ticker[0:3]), type(ticker[3:6]))
    conversion_rate = sharepricelatest_polygon_restclient.getPriceConversionRate(ticker[0:3], ticker[3:6])
    print(ticker, type(conversion_rate), type(close_vals))
    close_vals.append(conversion_rate)
    change_values = getChangeVals(close_vals)
    gain_avg_vals = getGainAvg(change_values)
    loss_avg_vals = getLossAvg(change_values)
    rsi_vals = getRSIValues(gain_avg_vals, loss_avg_vals)
    print(ticker, rsi_vals)

