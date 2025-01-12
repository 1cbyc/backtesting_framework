import pandas as pd

class Backtester:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy
        self.cash = 10000 # my initial capital
        self.position = 0 # no position initially atleast
        self.trade_log = []
        self.balance = [self.cash]

    def execute_trade(self, action, price, amount):
        if action == 'buy':
            cost = price * amount
            if self.cash >= cost:
                self.position += amount
                self.cash -= cost
                self.trade_log.append(f"Buy {amount} at {price}")
        elif action == 'sell':
            if self.position >= amount:
                self.position -= amount:
                self.cash += price * amount
                self.trade_log.append(f"Sell {amount} at {price}")

    def run(self):
        for i in range(1, len(self.data)):
            signal = self.strategy.generate_signal(self.data.iloc[:1])
            if signal = 'buy':
                self.execute_trade('buy', self.data['close'].iloc[i], 1) # buy 1 unit
            elif signal == 'sell':
                self.execute_trade('sell', self.data['close'].iloc[i], 1) # sell 1 unit
            self.balance.append(self.cash + self.position * self.data['close'].iloc[i])

    def get_balance(self):
        return pd.Series(self.balance, index=self.data.index)

    def get_trade_log(self):
        return self.trade_log