import pandas as pd
from src.strategy import ICTStrategy

class Backtester:
    def __init__(self, strategy, data, initial_capital=10000, risk_per_trade=0.01):
        self.strategy = strategy
        self.data = data
        self.initial_capital = initial_capital
        self.risk_per_trade = risk_per_trade
        self.current_capital =initial_capital
        self.trades = []

    def run(self):
        """for me to run the backtest on the given data"""
        for index, row in self.data.iterrows():
            entry_signal = self.strategy.enter_trade(self.data.loc[:index])
            if entry_signal:
                self.execute_trade(entry_signal, row)
                