import pandas as pd
import yfinance as yf

class DataLoader:
    def __init__(self, symbol, start_date, end_date, interval='1d'):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def fetch_data(self):
        """trying to fetch historical price data using yfinance"""
        data = yf.download(self.symbol, start=self.start_date, end=self.end)