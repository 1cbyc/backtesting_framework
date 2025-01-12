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

i also created the data loader