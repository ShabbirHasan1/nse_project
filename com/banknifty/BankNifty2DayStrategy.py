# This file will check the one year data and check whether the Banknifty breaks two days high/low.
# If it breaks past two days high then we can trade on buy with the entry point as CMP+0.15%.
#
#   Target = EP + 1.5% (half of the lots) and SL = EP - 1.5%
# remaining half of the lots was executed when market breaks two days low.At this time we can trade on sell again.

# If it breaks past two days low  then we can trade on sell with the entry point as CMP-0.15%.
#
#   Target = EP - 1.5% (half of the lots) and SL = EP + 1.5%
# remaining half of the lots was executed when market breaks two days high. At this time we can trade on buy again.

from nsepy import get_history
from datetime import date, timedelta
import datetime


def get_future_data(start_date, end_date):
    data = get_history(symbol='BANKNIFTY', start=start_date, end=end_date, futures=True, index=True,
                       expiry_date=end_date)
    return data


def print_buy_trade_target_data(data):
    global trade_count
    global sl_hit_count
    global target_hit_count

    high_vals = dict(data['High'])
    low_vals = dict(data['Low'])
    date_values = list(high_vals.keys())
    #print(date_values[0], date_values[1])

    first_day_high = high_vals[date_values[0]]
    second_day_high = high_vals[date_values[1]]
    first_day_low = low_vals[date_values[0]]
    second_day_low = low_vals[date_values[1]]

    #print(first_day_high, second_day_high)

    index = 2
    while index < len(date_values):
        curr_day_high_val = high_vals[date_values[index]]
        if first_day_high > second_day_high:
            two_day_high_val = first_day_high
        else:
            two_day_high_val = second_day_high

        curr_day_low_val = low_vals[date_values[index]]
        if first_day_low > second_day_low:
            two_day_low_val = first_day_low
        else:
            two_day_low_val = second_day_low

        if curr_day_high_val > two_day_high_val:    # For Buy Trade Check
            entry_point = two_day_high_val + two_day_high_val * 0.0015
            if entry_point < curr_day_high_val:
                trade_count = trade_count + 1
                print('buy triggered at', date_values[index])
                sl_val = entry_point * 0.985
                target_val = entry_point * 1.015
                if low_vals[date_values[index]] < sl_val:
                    print('*** SL might hit on same day', date_values[index])
                    sl_hit_count = sl_hit_count + 1
                elif high_vals[date_values[index]] > target_val:
                    print('### Target might hit on same day', date_values[index])
                    target_hit_count = target_hit_count + 1
                    # traverse for next two days low and exit from the high trend
                    while curr_day_low_val < two_day_low_val or index < len(date_values):
                        index = index + 1
                        first_day_low = second_day_low
                        second_day_low = curr_day_low_val
                        curr_day_low_val = low_vals[date_values[index]]
                        if first_day_low > second_day_low:
                            two_day_low_val = first_day_low
                        else:
                            two_day_low_val = second_day_low
                    print('### After Buy trade target hit.. Sell Trade Triggers on', date_values[index])
                else:
                    while index < len(date_values) :
                        if low_vals[date_values[index]] < sl_val:
                            print('*** SL hit on', date_values[index])
                            sl_hit_count = sl_hit_count + 1
                            break
                        elif high_vals[date_values[index]] > target_val:
                            print('### Target hit on ', date_values[index])
                            target_hit_count = target_hit_count + 1
                            while index < len(date_values):
                                index = index + 1
                                first_day_low = second_day_low
                                second_day_low = curr_day_low_val
                                curr_day_low_val = low_vals[date_values[index]]
                                if first_day_low > second_day_low:
                                    two_day_low_val = first_day_low
                                else:
                                    two_day_low_val = second_day_low
                                if curr_day_low_val < two_day_low_val:
                                    break
                            print('### After Buy trade target hit.. Sell Trade Triggers on', date_values[index])
                            break
                        index = index + 1
            #index = index + 1
            first_day_high = second_day_high
            second_day_high = curr_day_high_val
        else:
            # index = index + 1
            first_day_high = second_day_high
            second_day_high = curr_day_high_val

        # process the sell trade
        if curr_day_low_val < two_day_low_val:
            entry_point = two_day_low_val - two_day_low_val * 0.0015
            if entry_point > curr_day_low_val:
                trade_count = trade_count + 1
                print('Sell triggered at', date_values[index])
                sl_val = entry_point * 1.015
                target_val = entry_point * 0.985
                if high_vals[date_values[index]] > sl_val :
                    print('*** SL might hit on same day', date_values[index])
                    sl_hit_count = sl_hit_count + 1
                elif low_vals[date_values[index]] < target_val :
                    print('### Target might hit on same day', date_values[index])
                    target_hit_count = target_hit_count + 1
                    # traverse for next two days high and exit from the high trend
                    while index < len(date_values):
                        index = index + 1
                        if index > len(date_values):
                            break
                        first_day_high = second_day_high
                        second_day_high = curr_day_high_val
                        #print(high_vals[date_values[index]])
                        curr_day_high_val = high_vals[date_values[index]]
                        if first_day_high > second_day_high:
                            two_day_high_val = first_day_high
                        else:
                            two_day_high_val = second_day_high
                        if curr_day_high_val > two_day_high_val:
                            break
                    print('### After Sell trade target hit.. Buy Trade Triggers on', date_values[index])
                else:
                    index = index + 1
                    while index < len(date_values) :
                        if high_vals[date_values[index]] > sl_val:
                            print('*** SL hit on', date_values[index])
                            sl_hit_count = sl_hit_count + 1
                            break
                        elif low_vals[date_values[index]] < target_val:
                            print('### Target hit on ', date_values[index])
                            target_hit_count = target_hit_count + 1
                            while index < len(date_values):
                                index = index + 1
                                first_day_high = second_day_high
                                second_day_high = curr_day_high_val
                                curr_day_high_val = high_vals[date_values[index]]
                                if first_day_high > second_day_high:
                                    two_day_high_val = first_day_high
                                else:
                                    two_day_high_val = second_day_high
                                if curr_day_high_val > two_day_high_val or index > len(date_values):
                                    break
                            print('### After Sell trade target hit.. Buy Trade Triggers on', date_values[index])
                            break   # outer loop break
                        index = index + 1
            #index = index + 1
            first_day_low = second_day_low
            second_day_low = low_vals[date_values[index]]
        else:
            #index = index + 1
            first_day_low = second_day_low
            second_day_low = low_vals[date_values[index]]


# Jan data
data = get_future_data(datetime.datetime(2020, 1, 1), datetime.datetime(2020, 1, 30))
# Feb Data
#data = data.append(get_future_data(datetime.datetime(2020, 1, 31), datetime.datetime(2020, 2, 27)))
# March Data
#data = data.append(get_future_data(datetime.datetime(2020, 2, 28), datetime.datetime(2020, 3, 26)))
# April Data
#data = data.append(get_future_data(datetime.datetime(2020, 3, 27), datetime.datetime(2020, 4, 30)))
# May Data
#data = data.append(get_future_data(datetime.datetime(2020, 5, 1), datetime.datetime(2020, 5, 28)))
# June Data
#data = data.append(get_future_data(datetime.datetime(2020, 5, 29), datetime.datetime(2020, 6, 25)))
# July Data
#data = data.append(get_future_data(datetime.datetime(2020, 6, 26), datetime.datetime(2020, 7, 30)))
# August Data
#data = data.append(get_future_data(datetime.datetime(2020, 7, 31), datetime.datetime(2020, 8, 27)))
# September Data
#data = data.append(get_future_data(datetime.datetime(2020, 8, 28), datetime.datetime(2020, 9, 24)))
# October Data
#data = data.append(get_future_data(datetime.datetime(2020, 9, 25), datetime.datetime(2020, 10, 29)))
# November Data
#data = data.append(get_future_data(datetime.datetime(2020, 10, 30), datetime.datetime(2020, 11, 26)))
# December Data
#data = data.append(get_future_data(datetime.datetime(2020, 11, 27), datetime.datetime(2020, 12, 31)))


trade_count = 0
sl_hit_count = 0
target_hit_count = 0

#high_vals = list(data['High'])
#print(high_vals)
try :
    print_buy_trade_target_data(data)
except RuntimeError:
    print(trade_count, sl_hit_count, target_hit_count)
#print_sell_tarde_target_data(data)

