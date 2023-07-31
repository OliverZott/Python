from dash.dependencies import Input
from dash.dependencies import Output

import dash
from dash import dcc
from dash import html

app = dash.Dash()


app.layout = html.Div(
    [
        dcc.RangeSlider(
            min=-6,
            max=6,
            step=1,
            id="slider",
            value=[-2, 2],
            marks={i: f"{i}°C" for i in range(-6, 7)},
        ),
        html.Div(
            id="output-div",
            children=[],
        ),
    ],
    style={"margin": 25},
)


@app.callback(
    Output(component_id="output-div", component_property="children"),
    [
        Input(component_id="slider", component_property="value"),
    ],
)
def update_headding(value: list) -> int:
    return value[0] * value[1]


if __name__ == "__main__":
    app.run(debug=True)
