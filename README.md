# backtesting_framework
building a backtesting engine tailored to ICT trading models.

my intents is to import these libraries:

`pandas
yfinance
matplotlib
plotly`

my plan is to test ICT strategies I am learning, like the order blocks (OB) and fair value gap (FVG).

literally, i just had to import all necessary modules for me to work well:

```python
    from src.data_loader import DataLoader
    from src.strategy import ICTStrategy
    from src.backtester import Backtester
    from src.performance import Performance
```

i also created the data loader too:
```python
    data_loader = DataLoader(symbol='EURUSD', start_date='2022-01-01', end_date='2023-01-01')
    data = data_loader.fetch_data()
```

for now, i think i want to define a custom strategy for this, maybe order block strategy first.

let me run the backtest atp:
```python
    backtester = Backtester(strategy, data)
    backtester.run()
```

time to evaluate the performance of the model i am learning:
```python
    performance = Performance(backtester.trades)
    metrics = performance.calculate_metrics()
    print(metrics)
    performance.plot_performance()
```

since it is the weekend, i need to test this strategy on crypto markets. so i have added ccxt to the libraries i am installing.

this whole thing is hinged on utilizing order block strategy!

## random dump

i think i want to change the approach i take, let me put three strategies we can use. order block, fair value gap and breaker block. so, yeah.

i want to get data from OANDA, dukascopy or Alpha Vantage API outrightly.

so, i will `download_data` to fetch the market data from the data provider endpoint, then `resample_data` to get the data to the desired timeframe i intend to use. well, i also `clean_data` to remove the missing values from the marketdata i got.

i just finished coding the `engine.py` itself. so now i have added the backtester class to handle executing trades based on the strategy signals. i also added `execute_trade` class to execute buy and sell orders, and also updating cash and position. however, the `run` class i added is to help me loop through the data and execute the strategy signals. as well as the  `get_balance` class to return the account balance (cash + position value) over time...as much as i also added the `get_trade_log` class to return the log of trades made during the backtest.

i admit, my order block strategy is a simple strategy that generates a "buy" signal if the closing price is above the 5-period moving average and a "sell" signal if it’s below.

let me work out the performance metrics side of things. creating the `performance.py` script is the way to go right now. let me see if i can wrap my head around it.

okay, let me continue. i stopped at `performance.py` the other day. my wife fell sick!