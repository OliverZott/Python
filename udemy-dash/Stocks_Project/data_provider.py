import json
from datetime import datetime

import pandas as pd
import requests

# TODO: use dict
stocks = ["IBM", "MSFT", "AAPL", "GOOA"]


# TODO: use API with dayly stocks prices
refresh_type = ["TIME_SERIES_INTRADAY", "TIME_SERIES_WEEKLY_ADJUSTED"]  # TIME_SERIES_DAILY_ADJUSTED not working -> premium


class alphavantage_datareader:
    api_key = "14ZRWIEBC1DWVZY3"

    @staticmethod
    def get_intraday_data_from_alphavantage(stocks: str):
        api_key = "14ZRWIEBC1DWVZY3"
        url: str = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stocks}&interval=5min&apikey={api_key}"
        resp = requests.get(url)
        json_resp = resp.json()
        data = json_resp["Time Series (5min)"]
        df = pd.read_json(json.dumps(data))
        return df

    @staticmethod
    def get_weekly_data_from_alphavantage(stocks: str):
        api_key = "14ZRWIEBC1DWVZY3"
        url: str = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={stocks}&interval=5min&apikey={api_key}"
        resp = requests.get(url)
        json_resp = resp.json()
        data = json_resp["Weekly Adjusted Time Series"]
        df = pd.read_json(json.dumps(data))
        return df


if __name__ == "__main__":
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&interval=5min&apikey={alphavantage_datareader.api_key}"

    df2 = alphavantage_datareader.get_intraday_data_from_alphavantage("AAPL")
    print(df2.head())
    print(df2.tail())

    df3 = alphavantage_datareader.get_weekly_data_from_alphavantage("IBM")
    print(df3.head())
    print(df3.tail())
