# This class will read the excel sheet BankNifty-5Min-Data and validates the data for the below scenarios
# BUY Trade : close_val > ema_val
#        SL = Low of Candle
#       Target = Any candle closes below 200 EMA close price of that candle
#
# SELL Trade : close_val < ema_val
#       SL : High of Candle
#       Target = Next buy trade trigger point

import xlrd

from CourseraPython.com.futuredata.excel_data_validation.BankNiftyData import BankNiftyData
from CourseraPython.com.futuredata.excel_data_validation.BankNiftyTradeData import BankNiftyTradeData


def get_row_data(row_index):
    if row_index >= sheet.nrows:  # max rows
        return None
    row_val = sheet.row_values(row_index)
    return BankNiftyData(row_val[0], float(row_val[2]), float(row_val[3]), float(row_val[4]),
                         float(row_val[5]))


def process_row_data():
    if row_data.close_val > row_data.ema_val:       # Buy Trade
        trade_data.is_buy_trade_triggered = True
        trade_data.trade_entry = row_data.close_val
        trade_data.sl_val = row_data.low_val
        print('buy trade triggerd at ', row_data.time, ' SL = ', trade_data.sl_val)
    elif row_data.close_val < row_data.ema_val:     # Sell Trade
        trade_data.is_sell_trade_triggered = True
        trade_data.trade_entry = row_data.close_val
        trade_data.sl_val = row_data.high_val
        print('sell trade triggerd at ', row_data.time, ' SL = ', trade_data.sl_val)


file_loc = "C:/future-data/BankNifty-5Min-Data.xlsx"
wb = xlrd.open_workbook(file_loc)
result = dict()

sheet = wb.sheet_by_index(0)  # Reads the first sheet
row_data = get_row_data(1)  # First Row
trade_data = BankNiftyTradeData()
process_row_data()
trade_points = 0

i = 2
while i < sheet.nrows:
    row_data = get_row_data(int(i))
    if trade_data.is_buy_trade_triggered:
        if trade_data.sl_val > row_data.low_val:   # SL hits
            trade_points = trade_points - (trade_data.trade_entry - trade_data.sl_val)
            trade_data.is_buy_trade_triggered = False
            print('Buy Trade SL Hit at ', row_data.time, ' loss = ', trade_data.trade_entry - trade_data.sl_val)
        elif row_data.close_val < row_data.ema_val :  # Sell trade triggers from Buy trade
            profit_points = row_data.close_val - trade_data.trade_entry
            trade_points = trade_points + profit_points
            trade_data.is_sell_trade_triggered = True
            trade_data.is_buy_trade_triggered = False
            trade_data.trade_entry = row_data.close_val
            trade_data.sl_val = row_data.high_val
            print('sell trade triggered at ', row_data.time,
                  ' profit = ', profit_points,
                  ' SL = ', trade_data.sl_val)
            continue
    elif trade_data.is_sell_trade_triggered:
        if trade_data.sl_val > row_data.high_val:  # SL hits
            trade_points = trade_points - (trade_data.sl_val - trade_data.trade_entry)
            trade_data.is_sell_trade_triggered = False
            print('Sell Trade SL Hit at ', row_data.time, ' loss = ', trade_data.sl_val - trade_data.trade_entry)
        elif row_data.close_val > row_data.ema_val: # Buy trade triggers from Sell trade
            profit_points = trade_data.trade_entry - row_data.close_val
            trade_points = trade_points + profit_points
            trade_data.is_buy_trade_triggered = True
            trade_data.is_sell_trade_triggered = False
            trade_data.trade_entry = row_data.close_val
            trade_data.sl_val = row_data.low_val
            print('buy trade triggered at ', row_data.time,
                  ' profit = ', profit_points,
                  ' SL = ', trade_data.sl_val)
            continue
    if trade_data.is_sell_trade_triggered is False and trade_data.is_buy_trade_triggered is False:
        process_row_data()
    i = i + 1


print(trade_points)

