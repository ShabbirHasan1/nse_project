
class TradeInfo:
    def __init__(self):
        self.is_trade_triggered = False
        self.trade_entry_point = 0
        self.trade_target_level = 0
        self.trade_sl_level = 0

    def __init__(self, is_trade_triggered, trade_entry_point, trade_target_level, trade_sl_level):
        self.is_trade_triggered = is_trade_triggered
        self.trade_entry_point = trade_entry_point
        self.trade_target_level = trade_target_level
        self.trade_sl_level = trade_sl_level

    def set_values(self, is_trade_triggered, trade_entry_point, trade_target_level, trade_sl_level):
        self.is_trade_triggered = is_trade_triggered
        self.trade_entry_point = trade_entry_point
        self.trade_target_level = trade_target_level
        self.trade_sl_level = trade_sl_level

    def reset_values(self):
        self.is_trade_triggered = False
        self.trade_entry_point = 0
        self.trade_target_level = 0
        self.trade_sl_level = 0
