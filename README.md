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

since it is the weekend, i need to test this strategy on crypto markets.