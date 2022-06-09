# This class will read the excel sheet BankNifty_OneDay_Data and validates the data for the below scenarios
# BUY Trade :
#       Entry : 2 days Higher high + 0.15%
#       SL = Buy Entry - 1.5%
#       Target = Buy Entry + 1.5%
#
# SELL Trade :
#       Entry : 2 days lower low - 0.15%
#       SL : Buy Entry + 1.5%
#       Target = Buy Entry - 1.5%


import xlrd

from CourseraPython.com.futuredata.excel_data_validation.BankNiftyData import BankNiftyData
from CourseraPython.com.futuredata.excel_data_validation.BankNiftyTradeData import BankNiftyTradeData


def get_row_data(row_index):
    if row_index >= sheet.nrows:  # max rows
        return None
    row_val = sheet.row_values(row_index)
    return BankNiftyData(row_val[0], float(row_val[2]), float(row_val[3]), float(row_val[4]),
                         float(row_val[5]))


def get_high_value(first_val, second_val):
    if first_val > second_val:
        return first_val
    return second_val


def get_low_value(first_val, second_val):
    if first_val < second_val:
        return first_val
    return second_val


file_loc = "C:/future-data/BankNifty_OneDay_Data.xlsx"
wb = xlrd.open_workbook(file_loc)
result = dict()

sheet = wb.sheet_by_index(0)  # Reads the first sheet
first_row = get_row_data(1)
second_row = get_row_data(2)

trade_data = BankNiftyTradeData()
i = 3
trade_count = 0
sl_count = 0
target_count = 0
sl_points = 0
target_points = 0

while i < sheet.nrows:
    next_row = get_row_data(int(i))
    if trade_data.is_buy_trade_triggered:
        next_row.low_val  > trade_data.trade_entry * 0.985

    two_day_higher_high = get_high_value(first_row.high_val, second_row.high_val)
    two_day_lower_low = get_low_value(first_row.low_val, second_row.low_val)

    buy_trade_entry = two_day_higher_high * 1.0015
    sell_trade_entry = two_day_lower_low * 0.99998





    #if (not trade_data.is_buy_trade_triggered and
    #    not trade_data.is_sell_trade_triggered):



third_row = get_row_data()