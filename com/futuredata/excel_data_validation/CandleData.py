
class CandleData:

    def __init__(self):
        self.row_index = 0
        self.date = ''
        self.low_val = 0
        self.high_val = 0

    def __init__(self, row_index, date, high_val, low_val):
        self.row_index = row_index
        self.low_val = low_val
        self.high_val = high_val
        self.date = date

    def set_index(self, row_index):
        self.row_index = row_index

