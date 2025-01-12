from src.data_loader import DataLoader
from src.strategy import OrderBlockStrategy
from src.backtester import Backtester
from src.performance import Performance


data_loader = DataLoader(symbol='EURUSD=X', start_date='2022-01-01', end_date='2023-01-01')
data = data_loader.fetch_data()