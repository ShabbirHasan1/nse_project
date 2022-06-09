#   This program will find the low values of previous 5 days for the current day.
#   If the current latest price is 101% of 5 days lowest value then it will observe the last 5 days least high value,
#   Which will be the target.
#   This code back tests the data for October month

import datetime
from datetime import date, timedelta
from nsepy import get_history

from CourseraPython.com.futuredata.FutureDayData import FutureDayData
from CourseraPython.com.futuredata.FutureTradesStats import FuturesTradesStats
from CourseraPython.com.futuredata.TradeStats import TradeStats


def get_next_date(start_date, date_values):
    days = 1
    while True:
        trade_date = start_date + timedelta(days=days)
        if trade_date > date.today():
            return None
        if not date_values.__contains__(trade_date):
            days = days + 1
        else:
            break
    return trade_date


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


def get_dec_future_data(future_name):
    start_date = datetime.datetime(2020, 9, 25)
    #end_date = datetime.datetime(date.today().year, date.today().month, date.today().day)
    end_date = datetime.datetime(2020, 10, 29)
    dec_fut_expiry_date = datetime.datetime(2020, 10, 29)

    data = get_history(symbol=future_name, start=start_date, end=end_date, futures=True,
                       expiry_date=dec_fut_expiry_date)
    return data


def get_trade_stats_on_futures():
    trade_stats = TradeStats()

    for future_name in nse_future_names:
        start_date = datetime.datetime(2020, 10, 5).date()
        #if future_name == 'L%26TFH' or future_name == 'M%26M' or future_name == 'M%26MFIN':
        #    continue
        dec_data = get_dec_future_data(future_name)
        low_vals = dict(dec_data['Low'])
        if low_vals == {}:
            continue
        while start_date <= date.today():
            current_day_low_val = low_vals[start_date]
            day_data = get_five_day_low_high_values(start_date, dec_data)
            trade_entry_val = day_data.low_val * 1.01
            if current_day_low_val <= trade_entry_val:
                print(future_name, ' Trade executed on ', start_date, ' at ',trade_entry_val,  'target = ', day_data.high_val)
                target_hit_date = get_target_hit_date(start_date, dec_data, day_data.high_val)
                trade_stats.increase_trade_hit_count()
                # Update Specific future Data
                is_dict_contains_future = future_wise_data.keys().__contains__(future_name)
                if is_dict_contains_future:
                    fut_specific_data = future_wise_data.get(future_name)
                else:
                    fut_specific_data = FuturesTradesStats()
                fut_specific_data.increase_trade_hit_count()
                future_wise_data[future_name] = fut_specific_data

                if target_hit_date is None:
                    #print(future_name, '### Target not yet Hit ')
                    sl_hit_val = trade_entry_val - (day_data.high_val - trade_entry_val)
                    sl_hit_date = get_sl_hit_date(start_date, dec_data, sl_hit_val)
                    if sl_hit_date is not None:
                        print(future_name, '$$$$ SL hit on ', sl_hit_date)
                        trade_stats.increase_sl_hit_points(day_data.high_val - trade_entry_val)
                        trade_stats.increase_sl_hit_count()
                        start_date = sl_hit_date

                        # Update Specific future Data
                        fut_specific_data = future_wise_data[future_name]
                        fut_specific_data.increase_sl_hit_count()

                    else:
                        print('@@@ SL/Target did not hit for the future', future_name)
                        trade_stats.increase_no_result_count()
                        start_date = None
                else:
                    print(future_name, '*** Target Hit on ', target_hit_date)
                    trade_stats.increase_target_hit_count()
                    trade_stats.increase_trade_hit_points(day_data.high_val - trade_entry_val)
                    start_date = target_hit_date

                    # Update Specific future Data
                    fut_specific_data = future_wise_data[future_name]
                    fut_specific_data.increase_target_hit_count()

            if start_date is not None:
                start_date = get_next_date(start_date, low_vals.keys())  # moves to next date
            if start_date is None:
                break

    return trade_stats


def get_target_hit_date(start_date, dec_data, target_val):
    high_vals = dict(dec_data['High'])
    while start_date < date.today():
        if high_vals[start_date] >= target_val:
            return start_date
        else:
            #print('==== ', start_date)
            start_date = get_next_date(start_date, high_vals.keys())
            if start_date is None:
                start_date = date.today()
    return None


def get_sl_hit_date(start_date, dec_data, sl_value):
    high_vals = dict(dec_data['Low'])
    while start_date < date.today():
        if high_vals[start_date] <= sl_value:
            return start_date
        else:
            start_date = get_next_date(start_date, high_vals.keys())
            if start_date is None:
                start_date = date.today()
    return None



nse_future_names = ['ACC','ADANIENT','ADANIPORTS', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'BOSCHLTD', 'ASHOKLEY',
                 'CHOLAFIN', 'AUROPHARMA', 'AXISBANK', 'AMARAJABAT', 'BAJAJFINSV', 'BAJFINANCE', 'DRREDDY', 'BALKRISIND',
                 'BANDHANBNK', 'BANKBARODA', 'GODREJCP', 'BEL', 'BHARATFORG', 'BHARTIARTL', 'BIOCON', 'BRITANNIA',
                 'CADILAHC', 'CANBK', 'CIPLA', 'HEROMOTOCO', 'HINDPETRO', 'COALINDIA', 'IOC', 'COFORGE', 'LUPIN', 'COLPAL',
                 'CONCOR', 'CUMMINSIND', 'DIVISLAB', 'DLF', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL',
                 'GLENMARK', 'GMRINFRA', 'GODREJPROP', 'GRASIM', 'BAJAJ-AUTO', 'HCLTECH', 'HINDUNILVR', 'IBULHSGFIN',
                 'ICICIBANK', 'HAVELLS', 'IDEA', 'IDFCFIRSTB', 'IGL', 'INDIGO', 'INDUSINDBK', 'INFRATEL', 'INFY', 'ITC',
                 'JINDALSTEL', 'ICICIGI', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L%26TFH', 'PFC', 'LICHSGFIN', 'LT', 'M%26M',
                 'M%26MFIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'RECLTD', 'MINDTREE', 'MOTHERSUMI',
                 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'RELIANCE', 'NAUKRI', 'NESTLEIND', 'NMDC', 'NTPC', 'SRTRANSFIN',
                 'ONGC', 'VOLTAS', 'PAGEIND', 'PEL', 'PETRONET', 'PIDILITIND', 'PNB', 'PVR', 'RBLBANK', 'SAIL', 'SBIN',
                 'SHREECEM', 'SIEMENS', 'SRF', 'SUNTV', 'TATACHEM', 'TATACONSUM', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM',
                 'TORNTPHARM', 'TORNTPOWER', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'WIPRO', 'ZEEL', 'ASIANPAINT',
                 'BATAINDIA', 'BERGEPAINT', 'BHEL', 'HDFC', 'HDFCLIFE', 'BPCL', 'DABUR', 'POWERGRID', 'RAMCOCEM',
                 'HDFCBANK', 'HINDALCO', 'ICICIPRULI', 'MGL', 'SBILIFE', 'SUNPHARMA', 'TATAMOTORS', 'TITAN',]

future_wise_data = dict()
stats = get_trade_stats_on_futures()
print('total trades = ', stats.trade_hit_count)
print('total target hits = ', stats.target_hit_count)
print('total SL hits = ', stats.sl_hit_count)
print('total Win points = ', stats.target_hit_points)
print('total Loose points = ', stats.sl_hit_points)

traded_futures = future_wise_data.keys()
for future_name in traded_futures:
    future_specific_data = future_wise_data[future_name]
    print(future_name, ' ', future_specific_data.trade_hit_count, future_specific_data.target_hit_count,
          future_specific_data.sl_hit_count)