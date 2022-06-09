
class BankNiftyYearData:

    def __init__(self, data):
        self.data = data
        self.high_vals = dict(data['High'])
        self.low_vals = dict(data['Low'])
        self.date_values = list(self.high_vals.keys())