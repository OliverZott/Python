from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State

import dash
from dash import dcc
from dash import html

app = dash.Dash(title=__name__)

app.layout = html.Div(
    [
        dcc.Input(
            id="number-in",
            value=1,
            style={
                "fontSize": 25,
                "height": 30,
            },
        ),
        html.Button(
            children="Submit",
            id="submit-val",
            n_clicks=0,
            style={
                "margin": 25,
                "padding": 10,
            },
        ),
        html.H1(
            id="number-out",
            children=[],
        ),
    ],
    style={
        "margin": 25,
        "padding": 10,
    },
)


@app.callback(
    Output(component_id="number-out", component_property="children"),
    [
        Input(component_id="submit-val", component_property="n_clicks"),
    ],
    State(component_id="number-in", component_property="value"),
)
def update_number(clicks: int, number: float) -> str:
    return f"The number was {number} and you clicked {clicks}-times"


if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
