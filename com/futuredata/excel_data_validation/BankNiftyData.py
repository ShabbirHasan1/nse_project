
class BankNiftyData:

    def __init__(self):
        self.time = ''
        self.low_val = 0
        self.high_val = 0
        self.close_val = 0
        self.ema_val = 0

    def __init__(self, time, high_val, low_val, close_val, ema_val):
        self.low_val = low_val
        self.high_val = high_val
        self.time = time
        self.close_val = close_val
        self.ema_val = ema_val