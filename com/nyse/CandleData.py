import datetime


class CandleData:
    def __init__(self, start_time, curr_value, open_value, close_value, closest_whole_number):
        self.start_time = start_time
        self.curr_value = curr_value
        self.open_value = open_value
        self.close_value = close_value
        self.closest_whole_number = closest_whole_number

    def __init__(self):
        self.start_time = None
        self.curr_value = 0
        self.open_value = 0
        self.close_value = 0
        self.closest_whole_number = 0