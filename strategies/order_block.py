class OrderBlockStrategy:
    def __init__(self):
        self.name = "Order Block Strategy"

    def generate_signal(self, data):
        # putting a simple strategy based on order blocks (breakout above a block)