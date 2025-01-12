# i want to calculate and visualize the performance metrics and trade stats, so
import pandas as pd
import matplotlib.pyplot as plt

class Performance:
    def __init__(self, trades):
        self.trades = pd.DataFrame(trades)

    def calculate_metrics(self):
        """trying to calculate key performance metrics."""
        