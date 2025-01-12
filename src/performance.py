# i want to calculate and visualize the performance metrics and trade stats, so
import pandas as pd
import matplotlib.pyplot as plt

class Performance:
    def __init__(self, trades):
        self.trades = pd.DataFrame(trades)

    def calculate_metrics(self):
        """trying to calculate key performance metrics."""
        self.trades['profit'] = self.trades['exit_price'] - self.trades['entry_price']
        total_profit = self.trades['profit'].sum()
        win_rate = len(self.trades[self.trades['profit'] > 0]) / len(self.trades)
        max_drawdown = self.trades['profit'].min()

        # so, assuming all trades are of equal size...
        total_trades = len(self.trades)
        avg_profit = self.trades['profit'].mean()

        return {
            'total_profit': total_profit,
            'win_rate': win_rate,
            'max_drawdown': max_drawdown,
            'total_trades': total_trades,
            'avg_profit': avg_profit
        }

    def plot_performance(self):
        """so to generate the performance chart, this would do:"""
        self.trades['equity_curve'] = self.trades['profit'].cumsum()
        plt.figure(figsize=(10, 6))
        plt.plot(self.trades['equity_curve'], label='Equity Curve')
        plt.title('Backtest Performance')
        plt.xlabel('Trade')
        plt.ylabel('Cummulative Profit')
        plt.legend()
        plt.show()