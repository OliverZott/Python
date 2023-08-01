import datetime as dt

import pandas_datareader.data as web
from pandas_datareader import data as pdr

# Retrieve GOLD stock data
# gold_price = pdr.get_data_fred("GOLDPMGBD228NLBM")
# gold_price.tail()

start = dt.datetime(2018, 3, 26)
end = dt.datetime(2018, 3, 29)

stocks = web.DataReader("IBM", "yahoo", start, end).reset_index()
print(stocks.head())


start = dt.datetime(2023, 1, 1)
end = dt.datetime(2023, 8, 1)

tickers = ["MSFT", "GOOGL", "AAPL"]

for ticker in tickers:
    data = web.DataReader(ticker, "yahoo", start, end).reset_index()
    print(data)

#  If you want to get intraday stock data, you can use other libraries or APIs that provide this information
