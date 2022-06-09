
class BankNiftyDayData:

    def __init__(self):
        self.day_high = 0
        self.day_low = 0

    def __init__(self, data, index):
        high_vals = dict(data['High'])
        low_vals = dict(data['Low'])
        date_values = list(high_vals.keys())

        self.day_high = high_vals[date_values[index]]
        self.day_low = low_vals[date_values[index]]

    def __init__(self, year_data, index):
        self.day_high = year_data.high_vals[year_data.date_values[index]]
        self.day_low = year_data.low_vals[year_data.date_values[index]]