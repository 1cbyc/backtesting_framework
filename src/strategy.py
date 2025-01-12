class ICTStrategy:
    """Base class for ICT strategies."""

    def enter_trade(self, market_data):
        raise NotImplementedError("Subclasses should implement this!")

    def exit_trade(self, market_data):
        raise NotImplementedError("Subclasses should implement this!")

class OrderBlockStrategy(ICTStrategy):
    """basic order block strategy."""

    def enter_trade(self, market_data):
        """my logic to enter a trade based on order block."""
        last_candle = market_data.iloc[-1]  # Get the last row (candle)
        close = last_candle['Close']
        high = last_candle['High']
        low = last_candle['Low']

        if close > high - 0.001:  # base sample logic
            return {'type': 'buy', 'price': close}
        elif close < low + 0.001:
            return {'type': 'sell', 'price': close}
        return None

    def exit_trade(self, market_data):
        """my logic to exit the trade."""
        last_candle = market_data.iloc[-1]  # to get the last row (candle)
        close = last_candle['Close']
        high = last_candle['High']
        low = last_candle['Low']

        if close > high - 0.001:
            return {'type': 'sell', 'price': close}
        elif close < low + 0.001:
            return {'type': 'buy', 'price': close}
        return None
