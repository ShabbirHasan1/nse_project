# This class will read the excel sheet and validates the data for the below scenarios
# First it will check the lowest value for the past 4 days
# During the 5th day if the candle value is <= lowest_value * 101% then trade will be entered
# Target = 4 day lowest high value
# SL = Trade_entry - (4 day lowest high value - trade_entry)%
# At end it will print total trade values

import xlrd

from CourseraPython.com.futuredata.excel_data_validation.CandleData import CandleData
from CourseraPython.com.futuredata.excel_data_validation.DayData import DayData
from CourseraPython.com.futuredata.excel_data_validation.TradeInfo import TradeInfo
from CourseraPython.com.futuredata.excel_data_validation.TradeStats import TradeStats


def get_candle_data(row_index):
    if row_index >= sheet.nrows:      # max rows
        return None
    row_val = sheet.row_values(row_index)
    date_val = row_val[1].split('T')[0]         # 2 column is date column
    return CandleData(int(row_val[0]), date_val, float(row_val[3]), float(row_val[4]))


def get_day_data(row_index):
    first_candle = get_candle_data(row_index)    # First Row
    day_data = DayData(row_index, first_candle.low_val, first_candle.high_val)

    row_index = row_index + 1
    next_candle = get_candle_data(row_index)    # Next Row
    if next_candle is None:
        return
    while first_candle.date == next_candle.date:
        if day_data.low_val > next_candle.low_val:
            day_data.set_low_val(next_candle.low_val)

        if day_data.high_val < next_candle.high_val:
            day_data.set_high_val(next_candle.high_val)

        first_candle = next_candle
        row_index = row_index + 1
        next_candle = get_candle_data(row_index)
        if next_candle is None:
            break
        day_data.set_row_index(next_candle.row_index)
    return day_data


def get_low_value(first_day_val, second_day_val, third_day_val, fourth_day_val):
    low_val = first_day_val
    if second_day_val < low_val:
        low_val = second_day_val
    if third_day_val < low_val:
        low_val = third_day_val
    if fourth_day_val < low_val:
        low_val = fourth_day_val
    return low_val


def scan_candles_for_target_or_sl_hit(row_index):
    candle_data = get_candle_data(row_index)  # First Row
    while True:
        if candle_data.low_val <= trade_info.trade_sl_level:
            print('SL hit on ', candle_data.date, ' value = ', trade_info.trade_sl_level)
            trade_stats.increase_sl_hit_count()
            trade_info.reset_values()
            break
        elif candle_data.high_val >= trade_info.trade_target_level:
            print('Target hit on ', candle_data.date, ' value = ', trade_info.trade_target_level)
            trade_stats.increase_target_hit_count()
            trade_info.reset_values()
            break
        row_index = row_index + 1
        next_candle = get_candle_data(row_index)  # Next Row
        if next_candle is None:
            return
        if candle_data.date != next_candle.date:
            break
        else:
            candle_data = next_candle


def scan_candles_for_trade_info(four_day_low_val, row_index, four_day_low_high_val):
    candle_data = get_candle_data(row_index)  # First Row
    trade_triggerd_val = round(four_day_low_val * 0.98, 2)
    while True:
        if candle_data.low_val <= trade_triggerd_val:
            print('Trade Triggered on ', candle_data.date)
            trade_stats.increase_trade_hit_count()
            trade_info.set_values(True, trade_triggerd_val, four_day_low_high_val,
                                  trade_triggerd_val - (four_day_low_high_val - trade_triggerd_val))
            scan_candles_for_target_or_sl_hit(row_index)
            break
        row_index = row_index + 1
        next_candle = get_candle_data(row_index)  # Next Row
        if next_candle is None or candle_data.date != next_candle.date:
            break
        else:
            candle_data = next_candle


future_dict = {0: 'ADANIPORTS', 1: 'ASIANPAINT', 2: 'BAJAJ_AUTO', 3: 'BAJAJFINSV', 4: 'BAJFINANCE', 5: 'BANDHANBNK',
               6: 'BHARTIARTL', 7: 'BPCL', 8: 'BRITANNIA', 9: 'CIPLA', 10: 'COALINDIA', 11: 'DIVISLAB', 12: 'DRREDDY',
               13: 'EICHERMOT', 14: 'FEDERALBNK', 15: 'GAIL', 16: 'GRASIM', 17: 'HCLTECH', 18: 'HDFC', 19: 'HDFCBANK',
               20: 'HDFCLIFE', 21: 'HEROMOTOCO', 22: 'HINDALCO', 23: 'HINDUNILVR', 24: 'ICICIBANK', 25: 'INDUSINDBK',
               26: 'INFY', 27: 'IOC', 28: 'ITC', 29: 'JSWSTEEL', 30: 'KOTAKBANK', 31: 'LT', 32: 'M&M', 33: 'MARUTI',
               34: 'NTPC', 35: 'ONGC', 36: 'POWERGRID', 37: 'RBLBANK', 38: 'RELIANCE', 39: 'SBILIFE', 40: 'SBIN',
               41: 'SUNPHARMA', 42: 'TATAMOTORS', 43: 'TATASTEEL', 44: 'TCS', 45: 'TECHM', 46: 'TITAN', 47: 'ULTRACEMCO',
               48: 'UPL', 49: 'WIPRO', 50: 'AXISBANK'}

file_loc = "C:/future-data/50_FUTURES_DATA.xlsx"
wb = xlrd.open_workbook(file_loc)
result = dict()

for fut_key in future_dict:
    sheet = wb.sheet_by_index(fut_key)

    first_day_data = get_day_data(1)
    #print(first_day_data.high_val, ' ', first_day_data.low_val, ' ', first_day_data.row_index)
    second_day_data = get_day_data(first_day_data.row_index)
    #print(second_day_data.high_val, ' ', second_day_data.low_val, ' ', second_day_data.row_index)
    third_day_data = get_day_data(second_day_data.row_index)
    #print(third_day_data.high_val, ' ', third_day_data.low_val, ' ', third_day_data.row_index)
    fourth_day_data = get_day_data(third_day_data.row_index)
    #print(fourth_day_data.high_val, ' ', fourth_day_data.low_val, ' ', fourth_day_data.row_index)

    trade_stats = TradeStats()
    trade_info = TradeInfo(False, 0, 0, 0)

    fifth_day_data = get_day_data(fourth_day_data.row_index)

    while fifth_day_data is not None:

        high_low_val = get_low_value(first_day_data.high_val, second_day_data.high_val, third_day_data.high_val,
                                    fourth_day_data.high_val)
        if trade_info.is_trade_triggered:
            scan_candles_for_target_or_sl_hit(fourth_day_data.row_index)
        else:
            low_low_val = get_low_value(first_day_data.low_val, second_day_data.low_val, third_day_data.low_val,
                                        fourth_day_data.low_val)
            if fifth_day_data.low_val <= low_low_val * 0.98:
                scan_candles_for_trade_info(low_low_val, fourth_day_data.row_index, high_low_val)

        first_day_data = second_day_data
        second_day_data = third_day_data
        third_day_data = fourth_day_data
        fourth_day_data = fifth_day_data
        fifth_day_data = get_day_data(fourth_day_data.row_index)

    result[fut_key] = trade_stats


for fut_key in result:
    fut_trade_stats = result.get(fut_key)
    print(future_dict.get(fut_key), '\t', fut_trade_stats.trade_hit_count, '\t', fut_trade_stats.target_hit_count, '\t',
          fut_trade_stats.sl_hit_count)