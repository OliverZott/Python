"""
TODO:

- other api for dayly-prices and various stocks
- outsource each rendered component (div, graphs, dropdowns, ...)  
- check if multi stocks --> various calls to api and create new df for displaying

"""

import json
from datetime import date

import numpy as np
import pandas as pd
import plotly.graph_objs as go
import requests
from dash.dependencies import Input
from dash.dependencies import Output
from dotenv import load_dotenv

import dash
from dash import dcc
from dash import html

stocks = ["IBM", "MSFT", "AAPL", "ATVI"]


# Data


# Dash App
app = dash.Dash(title=__name__)

app.layout = html.Div(
    children=[
        html.Div(
            id="select-stock-div",
            children=[
                html.H1("Stocks"),
                dcc.Dropdown(
                    id="stock-dropdown",
                    options=stocks,
                    value=stocks[0],
                    multi=False,
                ),
            ],
            style={
                "width": "30%",
                "height": "200px",
                "display": "inline-block",
                "margin": 20,
                "padding": 10,
            },
        ),
        html.Div(
            id="date-select-div",
            children=[
                html.H1("Date-Range"),
                dcc.DatePickerRange(
                    id="stock-date-picker",
                    month_format="YYYY MM DD",
                    end_date_placeholder_text="YYYY MM DD ",
                    start_date=date(2017, 6, 21),
                ),
            ],
            style={
                "width": "30%",
                "height": "200px",
                "display": "inline-block",
                "margin": 20,
                "padding": 10,
            },
        ),
        html.Div(
            id="stock-graph-div",
            children=[dcc.Graph(id="stock-graph")],
        ),
    ]
)

api_key = "14ZRWIEBC1DWVZY3"

def get_data(stock: str):
    url: str = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={stock}&interval=5min&apikey={api_key}"
    print(url)
    resp = requests.get(url)
    json_resp = resp.json()
    data = json_resp["Weekly Adjusted Time Series"]
    # data = json_resp["Weekly Adjusted Time Series"]
    df = pd.read_json(json.dumps(data))
    return df.T


def get_all_data(stocks: list):
    lst = []
    for stock in stocks:
        df = get_data(stock)
        lst.append(df)
    # df = pd.DataFrame()
    df = pd.concat(lst)
    return df

@app.callback(
    Output(component_id="stock-graph", component_property="figure"),
    [
        Input(component_id="stock-dropdown", component_property="value"),
        # Input(component_id="stock-date-picker", component_property="value"),
    ],
)
def update_stock_graph(stock):
    print(stock)
    df = get_data(stock)

    data = [
        go.Scatter(
            x=df.index,
            y=df["4. close"],
            mode="markers+lines",
            marker=dict(
                size=5,
                opacity=0.6,
                line={"width": 0.5, "color": "black"},
            ),
        )
    ]

    layout = go.Layout(
        title=f"Stocks - {stock}",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Closing Price"),
    )

    fig = {
        "data": data,
        "layout": layout,
    }

    return fig


# Run App
if __name__ == "__main__":

    # testing functions



    # app.run(
    #     debug=True,
    #     dev_tools_hot_reload=True,
    #     dev_tools_ui=True,
    #     use_reloader=True,
    # )
