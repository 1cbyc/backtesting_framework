class OrderBlockStrategy:
    def __init__(self):
        self.name = "Order Block Strategy"

    def generate_signal(self, data):
        # putting a simple strategy based on order blocks (breakout above a block)
        if data['close'].iloc[-1] > data['close'].rolling(window=5).mean().iloc[-1]:
            return 'buy'
        elif data['close'].iloc[-1] < data['close'].rolling(window=5).mean().iloc[-1]:
            return 'sell'
        return 'hold'