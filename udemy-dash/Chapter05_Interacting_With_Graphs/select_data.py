import json
import os

import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input
from dash.dependencies import Output
from dotenv import load_dotenv

import dash
from dash import dcc
from dash import html

np.random.seed(42)
x1 = np.linspace(0.1, 5, 50)  # lhs - double
x2 = np.linspace(5.1, 10, 50)  # rhs - single
y = np.random.randint(0, 50, 50)

df1 = pd.DataFrame({"x": x1, "y": y})
# df2 = pd.DataFrame({"x": x1, "y": y})
df3 = pd.DataFrame({"x": x2, "y": y})

df = pd.concat([df1, df3])

# Dash App
app = dash.Dash(title=__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="my-plot",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["x"],
                                y=df["y"],
                                mode="markers",
                            )
                        ],
                        "layout": go.Layout(
                            title="Random Scatter Plot",
                            hovermode="closest",
                        ),
                    },
                ),
            ],
            style={
                "width": "30%",
                "display": "inline-block",
            },
        ),
        html.Div(
            [
                html.H1(
                    id="density",
                    style={"paddingTop": 25},
                )
            ],
            style={
                "width": "30%",
                "display": "inline-block",
                "verticalAlign": "top",
            },
        ),
        html.Div(
            [
                html.Pre(
                    id="hover-data",
                    style={"paddingTop": 30},
                ),
                html.Pre(
                    id="selected-data",
                    style={"paddingTop": 30},
                ),
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="density", component_property="children"),
    [
        Input(component_id="my-plot", component_property="selectedData"),
    ],
)
def find_density(selectedData) -> str:
    print(selectedData)
    # try:
    #     pts = len(selectedData["points"])
    #     print(pts)
    # except SystemError as e:
    #     print(e)
    # rng_or_lp = list(selectedData.keys())
    # rng_or_lp.remove("points")
    # max_x = max(selectedData[rng_or_lp[0]]["x"])
    # min_x = min(selectedData[rng_or_lp[0]]["x"])
    # max_y = max(selectedData[rng_or_lp[0]]["y"])
    # min_y = min(selectedData[rng_or_lp[0]]["y"])
    # area = (max_x - min_x) * (max_y - min_y)
    # d = pts / area
    return f"Density = {selectedData}"


@app.callback(
    Output(component_id="hover-data", component_property="children"),
    Input(component_id="my-plot", component_property="hoverData"),
)
def update_json(hover_data: str) -> str:
    return json.dumps(hover_data, indent=2)


@app.callback(
    Output(component_id="selected-data", component_property="children"),
    Input(component_id="my-plot", component_property="selectedData"),
)
def update_selectedData(selectedData):
    return json.dumps(selectedData, indent=2)


# Run App
if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
