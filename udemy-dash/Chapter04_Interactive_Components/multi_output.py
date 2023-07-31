import base64
import os

import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output
from dotenv import load_dotenv

import dash
from dash import dcc
from dash import html

load_dotenv()

DATA_BASE_PATH = str(os.getenv("DATA_BASE_PATH"))
IMAGE_BASE_PATH = str(os.getenv("IMAGE_BASE_PATH"))
file_name = "wheels.csv"
file_path = os.path.join(DATA_BASE_PATH, file_name)

# Data
df = pd.read_csv(file_path)
print(df.head())

# Dash App
app = dash.Dash(title=__name__)

app.layout = html.Div(
    children=[
        dcc.RadioItems(
            id="wheels",
            options=[i for i in df["wheels"].unique()],
            value=df["wheels"].min(),
        ),
        html.Div(id="wheels-output"),
        html.Hr(),
        dcc.RadioItems(
            id="colors",
            options=[{"label": str(i), "value": str(i)} for i in df["color"].unique()],
            value=df["color"][0],
        ),
        html.Div(id="colors-output"),
        html.Img(
            id="display-image",
            src="children",
            height=300,
        ),
    ]
)


@app.callback(
    Output(component_id="wheels-output", component_property="children"),
    [
        Input(component_id="wheels", component_property="value"),
    ],
)
def update_wheels(wheels: str) -> str:
    return f"Your wheel-count selection: {wheels}"


@app.callback(
    Output(component_id="colors-output", component_property="children"),
    [
        Input(component_id="colors", component_property="value"),
    ],
)
def update_colors(color_input: str) -> str:
    return f"Your color selection: {color_input}"


@app.callback(
    Output(component_id="display-image", component_property="src"),
    [
        Input(component_id="colors", component_property="value"),
        Input(component_id="wheels", component_property="value"),
    ],
)
def update_image(color: str, wheels: str) -> str:
    image_name = df[(df["wheels"] == wheels) & (df["color"] == color)]["image"].values[0]
    image_path = os.path.join(IMAGE_BASE_PATH, image_name)
    return encode_image(image_path)


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return f"data:image/png;base64,{encoded.decode()}"


# Run App
if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
