import pandas as pd
import requests

def download_data(symbol, start_date, end_date, interval='1d'):
    url = f'https://api.example.com/data?symbol={symbol}&start={start_date}&end={end_date}&interval={interval}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['prices'])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

def resample_data(df, timeframe='1H'):
    return df.resample(timeframe).agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum'})

def clean_data(df):
    df.dropna(inplace=True)
    return df