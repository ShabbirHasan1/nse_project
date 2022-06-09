
class DayData:

    def __init__(self):
        self.row_index = 0
        self.low_val = 0
        self.high_val = 0

    def __init__(self, row_index, low_val, high_val):
        self.row_index = row_index
        self.low_val = low_val
        self.high_val = high_val

    def set_row_index(self, row_index):
        self.row_index = row_index

    def set_low_val(self, low_val):
        self.low_val = low_val

    def set_high_val(self, high_val):
        self.high_val = high_val
