class RiskManagement:
    def __init__(self, capital, risk_per_trade):
        self.capital = capital
        self.risk_per_trade = risk_per_trade

    def calculate_position_size(self, stop_loss_distance):
        """want to calculate the position size based on the stop loss distance
        Args:
            stop_loss_distance (float): The distance from the entry to the stop-loss price.
        Returns:
            float: The position size.
        """
        risk_amount = self.capital * self.risk_per_trade
        position_size = risk_amount / stop_loss_distance
        return position_size