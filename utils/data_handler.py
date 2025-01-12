import pandas as pd
import requests

def download_data(symbol, start_date, end_date, interval='1d'):
    url = f'https://api.example.com/data?symbol={symbol}&start={start_date}&end={end_date}&interval={interval}'