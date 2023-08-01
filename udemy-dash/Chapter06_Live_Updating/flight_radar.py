import numpy as np
import plotly.graph_objs as go
import requests
from dash.dependencies import Input
from dash.dependencies import Output

import dash
from dash import dcc
from dash import html

counter_list = list()

app = dash.Dash()


app.layout = html.Div(
    id="outer-div",
    children=[
        html.Pre(
            id="flight-counter-text",
        ),
        dcc.Graph(
            id="live-update-graph",
            style={"width": 1200},
        ),
        dcc.Interval(
            id="interval-component",
            interval=5000,
            n_intervals=0,
        ),
    ],
)


@app.callback(
    Output(component_id="flight-counter-text", component_property="children"),
    [
        Input(component_id="interval-component", component_property="n_intervals"),
    ],
)
def update_layout(n):
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # used by the server to determine how to format the response or what content to return.
    # Some servers may block requests that do not include a User-Agent header or that use an unrecognized user agent string,
    # so it is common practice to include this header when making requests to web servers.
    res = requests.get(url=url, headers={"User-Agent": "Mozilla/5.0"})
    data = res.json()
    counter = 0

    print(data["stats"]["total"])

    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]

    counter_list.append(counter)
    return html.H1(f"All flights: {counter} and list: {counter_list}")


@app.callback(
    Output(component_id="live-update-graph", component_property="figure"),
    [
        Input(component_id="interval-component", component_property="n_intervals"),
    ],
)
def update_counter_graph(n):
    fig = {
        "data": [
            go.Scatter(
                x=[i for i in range(0, len(counter_list), 1)],
                y=counter_list,
                mode="lines+markers",
            ),
        ],
        "layout": go.Layout(
            title="Worldwide flights",
        ),
    }
    return fig


if __name__ == "__main__":
    app.run(debug=True)
