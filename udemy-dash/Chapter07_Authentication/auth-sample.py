"""
HTTP Basic Auth:
- simplest way for web authentification
- hardcoded set of usernames and passwords
- users have to know their data
- user can't create own account
- user can't change password

OAuth (Plotly OAuth)
- Autentification through plotly registration (costs)

"""

import dash_auth
from dash.dependencies import Input
from dash.dependencies import Output

from dash import Dash
from dash import dcc
from dash import html

USER_PASSWORD = [
    ["user", "pw"],
    ["admin", "admin"],
]

app = Dash(__name__)

auth = dash_auth.BasicAuth(app, USER_PASSWORD)

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.Label("MySlider"),
                dcc.RangeSlider(
                    id="range-slider",
                    min=-5,
                    max=5,
                    step=1,
                    marks={i: f"marker {i}" for i in range(-5, 10)},
                ),
            ],
            style={"margin": 30},
        ),
        html.H1(id="product"),
    ]
)


@app.callback(
    Output(component_id="product", component_property="children"),
    Input(component_id="range-slider", component_property="value"),
)
def update_product(value_list):
    if value_list is None:
        return "undefined"
    print(value_list)
    return value_list[0] * value_list[1]


if __name__ == "__main__":
    app.run(debug=True)
