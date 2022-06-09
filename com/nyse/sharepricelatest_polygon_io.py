import websocket
import datetime

from nyse import MathOps
from nyse.CandleData import CandleData
import sys, traceback


def on_message(ws, message):
    #print(message)
    try:
        msg_list = message.split(",")
        date_entry = msg_list[5].split(":")
        date_entry = date_entry[1].rstrip("}]")
        date_entry = int(date_entry) / 1000
        date_obj = datetime.datetime.fromtimestamp(date_entry)

        ask_val = msg_list[3].split(":")[1]
        currency = msg_list[1].split(":")[1].strip("\"")

        candle_obj = candle_obj_dict.get(currency, None)
        if candle_obj is None:
            candle_obj = CandleData()
            candle_obj_dict[currency] = candle_obj

        if currency.endswith('/JPY') :
            handleJapanCurrency(candle_obj, ask_val, date_obj, currency)
            return

        if MathOps.isIgnoredMsg(ask_val, candle_obj):
            return

        if candle_obj.curr_value == 0 or\
                (date_obj.minute % 5 == 0 and \
                (candle_obj.start_time.minute != date_obj.minute and
                 candle_obj.start_time.second != date_obj.second)):
            candle_obj.start_time = date_obj
            candle_obj.open_value = ask_val

        candle_obj.curr_value = ask_val
        is_green_candle = True
        if candle_obj.curr_value < candle_obj.open_value:
            is_green_candle = False
        if MathOps.isCloseToWholeNumber(ask_val, is_green_candle, candle_obj):
            print(candle_obj.start_time, currency, ' reaching whole number', candle_obj.closest_whole_number, ask_val)
        #print(candle_obj.start_time, candle_obj.curr_value, candle_obj.open_value)
    except Exception as exception_val:
        print(exception_val)
        traceback.print_exc(file=sys.stdout)


def handleJapanCurrency(candle_obj, ask_val, date_obj, currency) :
    if MathOps.isIgnoredMsgForJPNCurrency(ask_val, candle_obj):
        return

    if candle_obj.curr_value == 0 or \
            (date_obj.minute % 5 == 0 and \
             (candle_obj.start_time.minute != date_obj.minute and
              candle_obj.start_time.second != date_obj.second)):
        candle_obj.start_time = date_obj
        candle_obj.open_value = ask_val

    candle_obj.curr_value = ask_val
    is_green_candle = True
    if candle_obj.curr_value < candle_obj.open_value:
        is_green_candle = False
    if MathOps.isCloseToWholeNumberForJapanCurrency(ask_val, is_green_candle, candle_obj):
        print(candle_obj.start_time, currency, ' reaching whole number', candle_obj.closest_whole_number, ask_val)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send('{"action":"auth","params":"_UB2XQ2tym7l_OEOwqjsUQdDR6bSIQysfBHhTb"}')
    ws.send('{"action":"subscribe","params":"C.EUR/USD,C.USD/CAD,C.AUD/USD,C.AUD/JPY,C.EUR/JPY,C.EUR/NZD,C.GBP/AUD,C.GBP/USD,C.NZD/USD,C.USD/JPY,C.AUD/CAD,C.AUD/CHF,C.AUD/NZD,C.CAD/CHF,C.CAD/JPY,C.EUR/AUD,C.EUR/CAD,C.EUR/CHF,C.EUR/GBP,C.GBP/CAD,C.EUR/CAD,C.EUR/CHF,C.EUR/GBP,C.GBP/CAD,C.GBP/CHF,C.GBP/JPY,C.GBP/NZD,C.NZD/JPY,C.USD/CHF"}')
    #ws.send('{"action":"subscribe","params":"C.USD/CHF"}')


candle_obj_dict = dict()

#candle_obj = CandleData(datetime.datetime.today(), 0, 0, 0)
#if __name__ == "__main__":
    # websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://socket.polygon.io/forex", on_message=on_message, on_error=on_error,
                                on_close=on_close)
ws.on_open = on_open
ws.run_forever()
