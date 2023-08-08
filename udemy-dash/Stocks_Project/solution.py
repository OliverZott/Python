from datetime import datetime

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from iexfinance.stocks import get_historical_data

import dash

# import pandas_datareader.data as web


# Create list of companies for dropdown menu
nsdq = pd.read_csv("../data/NASDAQcompanylist.csv")
nsdq.set_index("Symbol", inplace=True)


# Create a list of options
options = []
for tic in nsdq.index:
    mydict = {}

    mydict["label"] = nsdq.loc[tic]["Name"]

    mydict["value"] = tic

    options.append(mydict)


# Creat webapp
app = dash.Dash()


# Create html layout
app.layout = html.Div(
    [
        html.H1("Stock Ticker Dashboard"),
        html.Div(
            [
                html.H3("Enter a stock symbol:", style={"paddingRight": "30px"}),
                dcc.Dropdown(id="my_stock_picker", options=options, value=["TSLA"], multi=True),  # Default value
            ],
            style={"display": "inline-block", "verticalAlign": "top", "width": "30%"},
        ),
        html.Div(
            [
                html.H3("Select a start and end date:"),
                dcc.DatePickerRange(
                    id="my_date_picker",
                    min_date_allowed=datetime(2015, 1, 1),
                    max_date_allowed=datetime.today(),
                    start_date=datetime(2019, 1, 1),
                    end_date=datetime.today(),
                ),
            ],
            style={"display": "inline-block"},
        ),
        html.Div(
            [html.Button(id="submit-button", n_clicks=0, children="Submit", style={"fontSize": 24, "marginLeft": "30px"})],
            style={"display": "inline-block"},
        ),
        dcc.Graph(id="my_graph", figure={"data": [{"x": [1, 2], "y": [3, 1]}], "layout": {"title": "Default Title"}}),
    ]
)


@app.callback(
    Output("my_graph", "figure"),
    [Input("submit-button", "n_clicks")],
    [State("my_stock_picker", "value"), State("my_date_picker", "start_date"), State("my_date_picker", "end_date")],
)
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], "%Y-%m-%d")
    end = datetime.strptime(end_date[:10], "%Y-%m-%d")
    traces = []

    for tic in stock_ticker:
        df = get_historical_data(tic, start, end, token="<gib hier deinen Key ein>", output_format="pandas")

        traces.append({"x": df.index, "y": df["open"], "name": tic})

    #       df = web.DataReader(stock_ticker,'moex',start,end)

    fig = {"data": traces, "layout": {"title": stock_ticker}}

    return fig


if __name__ == "__main__":
    app.run_server()
