#   This program will notify the user with the whatsapp msg with the list of futures which values reach it's last five
#   days low. The notifier msg includes the target value and the SL value.

from CourseraPython.com.futuredata.FutureDayData import FutureDayData
import CourseraPython.com.nsedata.TimeComparison as timeComparison
from twilio.rest import Client

import datetime
from datetime import date, timedelta

import nsepy as nse
from nsepy import get_history


def get_dec_future_data(future_name):
    start_date = datetime.datetime(2021, 1, 1)
    end_date = date.today() - timedelta(days=1)
    dec_fut_expiry_date = datetime.datetime(2021, 1, 28)

    data = get_history(symbol=future_name, start=start_date.date(), end=end_date, futures=True,
                       expiry_date=dec_fut_expiry_date.date())
    return data


def get_five_day_low_high_values(start_date, dec_data):
    low_vals = dict(dec_data['Low'])

    five_day_date = get_date(5, start_date, low_vals.keys())
    fourth_day_date = get_date(4, start_date, low_vals.keys())
    third_day_date = get_date(3, start_date, low_vals.keys())
    second_day_date = get_date(2, start_date, low_vals.keys())
    first_day_date = get_date(1, start_date, low_vals.keys())

    five_day_low_vals = [low_vals[five_day_date], low_vals[fourth_day_date], low_vals[third_day_date],
                         low_vals[second_day_date], low_vals[first_day_date]]
    low_value = get_least_value(five_day_low_vals)

    high_vals = dict(dec_data['High'])
    five_day_high_vals = [high_vals[five_day_date], high_vals[fourth_day_date], high_vals[third_day_date],
                         high_vals[second_day_date], high_vals[first_day_date]]
    high_value = get_least_value(five_day_high_vals)
    return FutureDayData(low_value, high_value)


def get_date(days, start_date, date_values):
    while True:
        trade_date = start_date-timedelta(days=days)
        if not date_values.__contains__(trade_date):
            days = days + 1
        else:
            break
    return trade_date


def get_least_value(five_day_values):
    low_value = five_day_values[0]
    for value in five_day_values :
        if low_value > value :
            low_value = value
    return low_value


def notify_trade_futures():

    notified_list = list()
    futures_data = populate_future_data()
    while True:
        msg = ''
        for future_name in nse_future_names:
            day_data = futures_data[future_name]
            trade_entry_val = day_data.low_val * 1.01
            fut_latest_price = get_latest_price(future_name)

            if fut_latest_price <= trade_entry_val:
                sl_hit_val = fut_latest_price - (day_data.high_val - fut_latest_price)
                target_hit_val = day_data.high_val
                if not notified_list.__contains__(future_name):
                    msg = msg + ' \n ' + future_name + ' value = ' + str(round(fut_latest_price, 2)) + ' Target = ' + \
                          str(round(target_hit_val,2)) + ' SL = ' + str(round(sl_hit_val,2))
                    notified_list.append(future_name)
        print(msg)
        #if msg != '':
            #send_whatsapp_msg(msg)

        timeComparison.sleep10mins()
        if timeComparison.isClosingTime():
            break


def send_whatsapp_msg(msg):
    account_sid = 'AC19460e393ee78da313b92a2156b487e1'
    auth_token = '59a42b278c17f1426bcdb01bc9d5a036'
    client = Client(account_sid, auth_token)
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+919000017580'

    client.messages.create(body=str(msg), from_=from_whatsapp_number, to=to_whatsapp_number)


def populate_future_data():
    future_data = dict()
    today = date.today()
    for future_name in nse_future_names:
        dec_data = get_dec_future_data(future_name)
        day_data = get_five_day_low_high_values(today, dec_data)
        future_data[future_name] = day_data
    return future_data


def get_latest_price(future_name):
    fut_expiry_date = datetime.datetime(2021, 1, 28)
    q = nse.get_quote(future_name, instrument='FUTSTK', expiry=fut_expiry_date)
    latest_price = str(q['data'][0]['lastPrice']).replace(',', '')
    return float(latest_price)


#nse_future_names = ['ACC','ADANIENT','ADANIPORTS', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'BOSCHLTD', 'ASHOKLEY',
#                 'CHOLAFIN', 'AUROPHARMA', 'AXISBANK', 'AMARAJABAT', 'BAJAJFINSV', 'BAJFINANCE', 'DRREDDY', 'BALKRISIND',
#                 'BANDHANBNK', 'BANKBARODA', 'GODREJCP', 'BEL', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BRITANNIA',
#                 'CADILAHC', 'CANBK', 'CIPLA', 'HEROMOTOCO', 'HINDPETRO', 'COALINDIA', 'IOC', 'COFORGE', 'LUPIN', 'COLPAL',
#                 'CONCOR', 'CUMMINSIND', 'DIVISLAB', 'DLF', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL',
#                 'GLENMARK', 'GMRINFRA', 'GODREJPROP', 'GRASIM', 'BAJAJ-AUTO', 'HCLTECH', 'HINDUNILVR', 'IBULHSGFIN',
#                 'ICICIBANK', 'HAVELLS', 'IDEA', 'IDFCFIRSTB', 'IGL', 'INDIGO', 'INDUSINDBK', 'INFY', 'ITC',
#                 'JINDALSTEL', 'ICICIGI', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L%26TFH', 'PFC', 'LICHSGFIN', 'LT', 'M%26M',
#                 'M%26MFIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'RECLTD', 'MINDTREE', 'MOTHERSUMI',
#                 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'RELIANCE', 'NAUKRI', 'NESTLEIND', 'NMDC', 'NTPC', 'SRTRANSFIN',
#                 'ONGC', 'VOLTAS', 'PAGEIND', 'PEL', 'PETRONET', 'PIDILITIND', 'PNB', 'PVR', 'RBLBANK', 'SAIL', 'SBIN',
#                 'SHREECEM', 'SIEMENS', 'SRF', 'SUNTV', 'TATACHEM', 'TATACONSUM', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM',
#                 'TORNTPHARM', 'TORNTPOWER', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'WIPRO', 'ZEEL', 'ASIANPAINT',
#                 'BATAINDIA', 'BERGEPAINT', 'BHEL', 'HDFC', 'HDFCLIFE', 'BPCL', 'DABUR', 'POWERGRID', 'RAMCOCEM',
#                 'HDFCBANK', 'HINDALCO', 'ICICIPRULI', 'MGL', 'SBILIFE', 'SUNPHARMA', 'TATAMOTORS', 'TITAN',]


nse_future_names = ['ADANIPORTS', 'AXISBANK', 'CIPLA', 'IOC', 'DRREDDY', 'BAJFINANCE', 'DIVISLAB', 'GRASIM', 'BAJAJ-AUTO',
                    'HINDUNILVR', 'INDUSINDBK', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'MARUTI', 'TATASTEEL', 'RBLBANK',
                    'TATAMOTORS', 'ASIANPAINT', 'WIPRO', 'ULTRACEMCO', 'TECHM', 'BHARTIARTL', 'EICHERMOT', 'FEDERALBNK',
                    'HDFCLIFE', 'ICICIBANK', 'INFY', 'JSWSTEEL', 'POWERGRID', 'TITAN', 'UPL']
notify_trade_futures()
