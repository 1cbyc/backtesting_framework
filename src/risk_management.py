class RiskManagement:
    def __init__(self, capital, risk_per_trade):
        self.capital = capital
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, stop_loss_distance):
        """want to calculate the position size based on the stop loss distance
        Args:
            """