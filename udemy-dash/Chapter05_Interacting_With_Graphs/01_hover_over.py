import base64
import json
import os

import dash
import pandas as pd
import plotly.graph_objs as go
from dash import dcc
from dash import html
from dash.dependencies import Input
from dash.dependencies import Output
from dotenv import load_dotenv

# Data
load_dotenv()

DATA_BASE_PATH = str(os.getenv("DATA_BASE_PATH"))
IMAGE_BASE_PATH = str(os.getenv("IMAGE_BASE_PATH"))
file_name = "wheels.csv"
file_path = os.path.join(DATA_BASE_PATH, file_name)

df = pd.read_csv(file_path)

# App
app = dash.Dash()

app.layout = html.Div(
    id="outer-div",
    children=[
        dcc.Graph(
            id="wheels-graph",
            figure={
                "data": [
                    go.Scatter(
                        x=df["color"],
                        y=df["wheels"],
                        mode="markers",
                        marker=dict(
                            size=24,
                            color="#0BD43A",
                            opacity=0.6,
                            line={"width": 1.2},
                        ),
                    ),
                ],
                "layout": go.Layout(
                    title="Wheels-Graph",
                ),
            },
            style={
                "width": "60%",
                "float": "left",
            },
        ),
        html.Div(
            id="json-div",
            children=[
                html.Pre(
                    id="hover-data",
                    style={"paddingTop": 30},
                ),
                html.Img(
                    id="image",
                    src="img",
                    style={"width": "70%"},
                ),
            ],
            style={
                "width": "30%",
                "float": "right",
                "paddingTop": 45,
            },
        ),
    ],
    style={
        "margin": 25,
        "padding": 20,
    },
)


@app.callback(
    Output(component_id="hover-data", component_property="children"),
    Input(component_id="wheels-graph", component_property="hoverData"),
)
def update_json(hover_data: str) -> str:
    return json.dumps(hover_data, indent=2)


@app.callback(
    Output(component_id="image", component_property="src"),
    Input(component_id="wheels-graph", component_property="clickData"),
)
def update_image(hover_data: dict):
    if hover_data is None:
        return None

    color = hover_data["points"][0]["x"]
    wheels = hover_data["points"][0]["y"]

    image_name = df[(df["color"] == color) & (df["wheels"] == wheels)]["image"].values[0]
    image_path = os.path.join(IMAGE_BASE_PATH, image_name)

    return encode_image(image_path)


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return f"data:image/png;base64,{encoded.decode()}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
