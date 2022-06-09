
from nsepy import get_history
import datetime

from CourseraPython.com.banknifty.BankNiftyDayData import BankNiftyDayData
from CourseraPython.com.banknifty.BankNiftyAlgoResult import BankNiftyAlgoResult
from CourseraPython.com.banknifty.BankNiftyYearData import BankNiftyYearData


def print_buy_trade_target_data(year_data):

    first_day_data = BankNiftyDayData(year_data, 0)
    second_day_data = BankNiftyDayData(year_data, 1)
    output = BankNiftyAlgoResult()

    index = 2
    curr_day_data = BankNiftyDayData(year_data, index)
    while True:
        #curr_day_data = BankNiftyDayData(year_data, index)
        two_day_high_val = get_two_day_high_val(first_day_data, second_day_data)
        two_day_low_val = get_two_day_low_val(first_day_data, second_day_data)

        if curr_day_data.day_high > two_day_high_val:    # For Buy Trade Check
            entry_point = two_day_high_val + two_day_high_val * 0.0015
            if entry_point < curr_day_data.day_high:    # Buy Trade Triggered
                output.increase_trade_count()
                print('buy triggered at', year_data.date_values[index])
                sl_val = entry_point * 0.985
                target_val = entry_point * 1.015

                if year_data.high_vals[year_data.date_values[index]] > target_val:
                    print('### Target might hit on same day', year_data.date_values[index])
                    output.increase_target_hit_count()
                    index = get_sell_trade_index(first_day_data, second_day_data, curr_day_data, index, year_data)
                elif year_data.low_vals[year_data.date_values[index]] < sl_val:
                    print('*** SL might hit on same day', year_data.date_values[index], entry_point, sl_val)
                    output.increase_sl_hit_count()
                else:
                    index = index + 1
                    while index < len(year_data.date_values): # traverse next days for target hit or sl
                        if year_data.low_vals[year_data.date_values[index]] < sl_val:
                            print('*** SL hit on', year_data.date_values[index])
                            output.increase_sl_hit_count()
                            break
                        elif year_data.high_vals[year_data.date_values[index]] > target_val:
                            print('### Target hit on ', year_data.date_values[index])
                            output.increase_target_hit_count()
                            index = get_sell_trade_index(first_day_data, second_day_data, curr_day_data, index,
                                                         year_data)
                            break
                        index = index + 1
        index = index + 1
        if index >= len(year_data.date_values):
            break
        #print(index, curr_day_data.day_high)
        curr_day_data = traverse_to_next_day(first_day_data, second_day_data, curr_day_data, index)
    return output

def get_two_day_high_val(first_day_data, second_day_data):
    if first_day_data.day_high > second_day_data.day_high:
        two_day_high_val = first_day_data.day_high
    else:
        two_day_high_val = second_day_data.day_high
    return two_day_high_val


def get_two_day_low_val(first_day_data, second_day_data):
    if first_day_data.day_low < second_day_data.day_low:
        two_day_low_val = first_day_data.day_low
    else:
        two_day_low_val = second_day_data.day_low
    return two_day_low_val


def get_sell_trade_index(first_day_data, second_day_data, curr_day_data, index, year_data):
    while True:
        index = index + 1
        if index == len(year_data.date_values):
            break
        curr_day_data = traverse_to_next_day(first_day_data, second_day_data, curr_day_data, index)
        two_day_low_val = get_two_day_low_val(first_day_data, second_day_data)
        if curr_day_data.day_low < two_day_low_val:
            break

    print('### After Buy trade target hit.. Sell Trade Triggers on', year_data.date_values[index])
    return index


def traverse_to_next_day(first_day_data, second_day_data, curr_day_data, index):
    first_day_data.day_low = second_day_data.day_low
    first_day_data.day_high = second_day_data.day_high

    second_day_data.day_low = curr_day_data.day_low
    second_day_data.day_high = curr_day_data.day_high
    curr_day_data = BankNiftyDayData(year_data, index)
    return curr_day_data


def get_future_data(start_date, end_date):
    data = get_history(symbol='BANKNIFTY', start=start_date, end=end_date, futures=True, index=True,
                       expiry_date=end_date)
    return data

# Jan data
data = get_future_data(datetime.datetime(2020, 1, 1), datetime.datetime(2020, 1, 30))
# Feb Data
data = data.append(get_future_data(datetime.datetime(2020, 1, 31), datetime.datetime(2020, 2, 27)))
# March Data
data = data.append(get_future_data(datetime.datetime(2020, 2, 28), datetime.datetime(2020, 3, 26)))
# April Data
data = data.append(get_future_data(datetime.datetime(2020, 3, 27), datetime.datetime(2020, 4, 30)))
# May Data
data = data.append(get_future_data(datetime.datetime(2020, 5, 1), datetime.datetime(2020, 5, 28)))
# June Data
data = data.append(get_future_data(datetime.datetime(2020, 5, 29), datetime.datetime(2020, 6, 25)))
# July Data
data = data.append(get_future_data(datetime.datetime(2020, 6, 26), datetime.datetime(2020, 7, 30)))
# August Data
data = data.append(get_future_data(datetime.datetime(2020, 7, 31), datetime.datetime(2020, 8, 27)))
# September Data
data = data.append(get_future_data(datetime.datetime(2020, 8, 28), datetime.datetime(2020, 9, 24)))
# October Data
data = data.append(get_future_data(datetime.datetime(2020, 9, 25), datetime.datetime(2020, 10, 29)))
# November Data
data = data.append(get_future_data(datetime.datetime(2020, 10, 30), datetime.datetime(2020, 11, 26)))
# December Data
#data = data.append(get_future_data(datetime.datetime(2020, 11, 27), datetime.datetime(2020, 12, 31)))

year_data = BankNiftyYearData(data)
print(list(year_data.high_vals.values()))

output = print_buy_trade_target_data(year_data)
print(output.trade_count, output.target_hit_count, output.sl_hit_count)