import math


def truncate_digits(input_val, exp_num_of_digits):
    myDigits = 10 ** exp_num_of_digits
    return int(input_val * myDigits) / myDigits


def isCloseToWholeNumber(ask_val, is_green_candle, candle_obj):
    value = truncate_digits(float(ask_val), 4)
    value = str(value).replace('.', '')
    value = int(value)

    if is_green_candle and value % 100 >= 90:
        candle_obj.closest_whole_number = truncate_digits(float(ask_val), 2)
        return True
    if not is_green_candle and value % 100 <= 10:
        candle_obj.closest_whole_number = truncate_digits(float(ask_val), 2)
        return True
    return False


def isCloseToWholeNumberForJapanCurrency(ask_val, is_green_candle, candle_obj):
    value = math.trunc(float(ask_val))

    if is_green_candle and value % 10 == 9:
        candle_obj.closest_whole_number = (math.trunc(value/10) + 1) * 10
        return True
    if not is_green_candle and value % 10 == 1:
        candle_obj.closest_whole_number = (math.trunc(value/10)) * 10
        return True
    return False


def isIgnoredMsg(ask_val, candle_obj):
    whole_number = truncate_digits(float(ask_val), 2)
    if candle_obj.closest_whole_number == whole_number:
        return True
    return False


def isIgnoredMsgForJPNCurrency(ask_val, candle_obj):
    whole_number = math.trunc(float(ask_val))

    if float(candle_obj.open_value) <= float(ask_val) :
        whole_number = (math.trunc(whole_number / 10) + 1) * 10
    else:
        whole_number = math.trunc(whole_number / 10) * 10

    if candle_obj.closest_whole_number == whole_number:
        return True
    return False


val = 79.94
val = math.trunc(val)
#print(math.trunc(val/10) + 1)
# print()

# val = val - val/1.1800
# print(val)
