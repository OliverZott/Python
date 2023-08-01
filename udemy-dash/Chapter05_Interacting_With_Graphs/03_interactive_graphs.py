import os
import sys

from dotenv import load_dotenv

load_dotenv()
path = str(os.getenv("UTILS_PATH"))
sys.path.append(str(os.getenv("UTILS_PATH")))

import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input
from dash.dependencies import Output
from data_provider import get_filepath
from numpy import random

import dash
from dash import dcc
from dash import html

# Data
df = pd.read_csv(get_filepath("mpg.csv"))

df["year"] = df["model_year"] + random.randint(-4, 5, len(df)) * 0.1

app = dash.Dash()

app.layout = html.Div(
    id="outer-div",
    children=[
        html.Div(
            [
                dcc.Graph(
                    id="base-plot",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["year"] + 1900,
                                y=df["mpg"],
                                mode="markers",
                                text=df["name"],
                                hovertext=df["name"],
                                hoverinfo="text",
                            )
                        ],
                        "layout": go.Layout(
                            title="Scatterplot - mpg.csv",
                            xaxis={"title": "Model Year"},
                            yaxis={"title": "MPG"},
                        ),
                    },
                )
            ],
            style={"width": "50%", "display": "inline-block"},
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id="plot-acc",
                    figure={
                        "data": [
                            go.Scatter(
                                x=[0, 1],
                                y=[0, 1],
                                mode="lines",
                            )
                        ],
                        "layout": go.Layout(
                            title="Acceleration",
                            margin={"l": 0},
                        ),
                    },
                )
            ],
            style={
                "width": "20%",
                "heigth": "50%",
                "display": "inline-block",
            },
        ),
        html.Div(
            children=[
                dcc.Markdown(id="stats-md"),
            ],
            style={
                "width": "20%",
                "heigth": "50%",
                "display": "inline-block",
            },
        ),
    ],
)


@app.callback(
    Output(component_id="plot-acc", component_property="figure"),
    Input(component_id="base-plot", component_property="hoverData"),
)
def update_acceleration(hoverData: dict) -> dict:
    # print(hoverData)
    if hoverData is None:
        index = 0
    else:
        index = hoverData["points"][0]["pointIndex"]
    fig = {
        "data": [
            go.Scatter(
                x=[0, 1],
                y=[0, 60 / df.iloc[index]["acceleration"]],
                mode="lines",
                line={"width": 2 * df.iloc[index]["cylinders"]},
            )
        ],
        "layout": go.Layout(
            title=f"Acceleration {df.iloc[index]['name']}",
            xaxis={"visible": False},
            yaxis={"visible": False, "range": [0, 60 / df["acceleration"].min()]},
            margin={"l": 0},
            height=300,
        ),
    }
    return fig


@app.callback(
    Output(component_id="stats-md", component_property="children"),
    Input(component_id="base-plot", component_property="hoverData"),
)
def update_stats(hoverData: dict) -> str:
    if hoverData is None:
        index = 0
    else:
        index = hoverData["points"][0]["pointIndex"]

    stats = f"""
        {df.iloc[index]["cylinders"]} cylinders
        {df.iloc[index]["displacement"]} displacement
        {df.iloc[index]["acceleration"]} acceleration
"""
    return stats


if __name__ == "__main__":
    app.run(debug=True)
