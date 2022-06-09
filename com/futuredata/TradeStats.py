
class TradeStats:

    def __init__(self):

        self.sl_hit_count = 0
        self.trade_hit_count = 0
        self.target_hit_count = 0
        self.no_result = 0
        self.target_hit_points = 0
        self.sl_hit_points = 0

    def increase_sl_hit_count(self):
        self.sl_hit_count = self.sl_hit_count + 1

    def increase_trade_hit_count(self):
        self.trade_hit_count = self.trade_hit_count + 1

    def increase_no_result_count(self):
        self.no_result = self.no_result + 1

    def increase_target_hit_count(self):
        self.target_hit_count = self.target_hit_count + 1

    def increase_trade_hit_points(self, points):
        self.target_hit_points = self.target_hit_points + points

    def increase_sl_hit_points(self, points):
        self.sl_hit_points = self.sl_hit_points + points
