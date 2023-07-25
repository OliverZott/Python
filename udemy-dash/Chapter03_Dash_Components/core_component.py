from dash import Dash
from dash import dcc
from dash import html

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(["My DCC components example"], style={"margin": 30}),
        html.Div(
            [
                html.Label("MyDropdown"),
                dcc.Dropdown(
                    options=[
                        {"label": "Austria", "value": "AUT"},
                        {"label": "Germany", "value": "GER"},
                        {"label": "Italy", "value": "IT"},
                    ],
                    value="IT",
                    multi=True,
                    id="demo-dropdown",
                ),
            ],
            style={"margin": 30},
        ),
        html.Div(
            [
                html.Label("MySlider"),
                dcc.Slider(
                    min=-5,
                    max=10,
                    step=1,
                    marks={i: f"marker {i}" for i in range(-5, 10)},
                    value=1,
                ),
            ],
            style={"margin": 30},
        ),
        html.Div(
            [
                html.Label("MyRadio"),
                dcc.RadioItems(
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "Montreal", "value": "MTL"},
                        {"label": "San Francisco", "value": "SF"},
                    ],
                    value="MTL",
                    id="demo-radioitems",
                ),
            ],
            style={"margin": 30},
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
