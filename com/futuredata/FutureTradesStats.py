
class FuturesTradesStats:

    def __init__(self):
        self.sl_hit_count = 0
        self.trade_hit_count = 0
        self.target_hit_count = 0

    def increase_sl_hit_count(self):
        self.sl_hit_count = self.sl_hit_count + 1

    def increase_trade_hit_count(self):
        self.trade_hit_count = self.trade_hit_count + 1

    def increase_target_hit_count(self):
        self.target_hit_count = self.target_hit_count + 1
