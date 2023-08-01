from dash.dependencies import Input
from dash.dependencies import Output

import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(id="live-update-text"),
        dcc.Interval(
            id="interval-component",
            interval=2000,
            n_intervals=0,
        ),
    ]
)


@app.callback(
    Output(component_id="live-update-text", component_property="children"),
    [
        Input(component_id="interval-component", component_property="n_intervals"),
    ],
)
def update_layout(n):
    return html.H1(f"Crash free for {n}")


if __name__ == "__main__":
    app.run(debug=True)
